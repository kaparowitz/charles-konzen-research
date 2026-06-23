#!/usr/bin/env python3
"""
check_surname_canon.py — deploy-gate check for the surname-trail single source.

Three guards, all derived from data/surname-attestations.json:

  1. FRESHNESS  — the AUTOGEN tables in germany/konzen-puzzle.html match what
                  the generator would produce. (Catches hand-edits between markers
                  and a JSON change that wasn't re-rendered.)
  2. STALE TEXT — no retracted surname phrasings survive anywhere, including in
                  the card *generator's source data* (scripts/build-evidence-cards.py),
                  which plain HTML greps miss.
  3. COUNTS     — the canonical count words on konzen-puzzle.html agree with the
                  JSON-derived counts (eight attestations, six collapse, etc.).

Exit 0 if clean, 1 if any guard fails. Called from scripts/check_canon.sh.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import surname_canon as sc  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PUZZLE = ROOT / "germany" / "konzen-puzzle.html"
CARD_GEN = ROOT / "scripts" / "build-evidence-cards.py"

fail = 0


def err(msg: str) -> None:
    global fail
    fail = 1
    print(f"  ✗ {msg}")


# ── Guard 1: AUTOGEN regions are fresh ───────────────────────────────────────
def check_freshness() -> None:
    txt = PUZZLE.read_text(encoding="utf-8")
    expected = {
        "surname-chronology": sc.chronology_table_html(),
        "surname-phonetic": sc.phonetic_table_html(),
    }
    for name, want in expected.items():
        m = re.search(
            r"<!-- AUTOGEN:" + re.escape(name) + r" START.*?-->(.*?)<!-- AUTOGEN:"
            + re.escape(name) + r" END -->",
            txt, re.DOTALL,
        )
        if not m:
            err(f"AUTOGEN markers for '{name}' missing in konzen-puzzle.html")
            continue
        if m.group(1).strip() != want.strip():
            err(f"AUTOGEN region '{name}' is STALE — run: python3 scripts/build-surname-trail.py")


# ── Guard 2: no retracted phrasings anywhere (HTML + the card generator) ──────
STALE = [
    (r"seven attestations|7 attestations", "stale count 'seven attestations' (canon: nine)"),
    (r"seven (distinct )?American (Charles-family )?(renderings|spellings|captures)",
     "stale 'seven American renderings/spellings/captures' (canon: nine)"),
    (r"of the seven distinct surname renderings", "stale 'seven distinct surname renderings' (canon: nine)"),
    (r"eight attestations|8 attestations", "stale count 'eight attestations' (canon: nine — the 1895 Gould's directory Gannsen was added 21 Jun 2026)"),
    (r"eight (distinct )?American (Charles-family )?(renderings|spellings|captures)",
     "stale 'eight American renderings/spellings/captures' (canon: nine)"),
    (r"Six of (the )?eight", "stale 'Six of eight … collapse' (canon: 'Six of nine')"),
    (r"geb (<em>)?Konsen", "stale 1890 reading 'geb Konsen' (canon: geb Konzen, the z-form)"),
    (r"Konsen-again", "stale '(Konsen-again 1890)' label (canon: Konzen 1890)"),
    (r"Jansen 1880\b", "stale 'Jansen 1880' (canon: Jansen 1881; 1880 is the Gonson census)"),
    (r"(?<!at least )\b(?:five|5)\s+(?:independent |different )?scribes\b",
     "un-hedged scribe count 'five scribes' (canon: 'at least five' / '5+' — the two "
     "Nollau entries may be distinct hands; see data/surname-attestations.json scribes_note)"),
]


def iter_targets():
    skip_dirs = {"_archive", "_backup_originals", ".git", ".netlify", "notes", "notes_view", "session_notes_docx"}
    skip_files = {"errata.html", "changelog.html"}
    for p in ROOT.rglob("*.html"):
        if any(part in skip_dirs for part in p.parts):
            continue
        if p.name in skip_files:
            continue
        yield p
    if CARD_GEN.exists():
        yield CARD_GEN  # scan the card generator's source data too


def check_stale() -> None:
    for p in iter_targets():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for pat, label in STALE:
            for m in re.finditer(pat, txt):
                line = txt[: m.start()].count("\n") + 1
                err(f"{p.relative_to(ROOT)}:{line} — {label}")


# ── Guard 3: canonical counts on konzen-puzzle.html match the JSON ────────────
def check_counts() -> None:
    txt = PUZZLE.read_text(encoding="utf-8")
    want = {
        f"{sc.CANON['n_attestations']} attestations or 'Nine attestations'": (
            "Nine attestations" in txt or f"{sc.CANON['n_attestations']} attestations" in txt
        ),
        "metric shows 9 record attestations": ">9</div><div class=\"lbl\">record" in txt
        or "9</div><div class=\"lbl\">record" in txt,
        "phonetic split 'three [kɔn], three [ɡɔn]'": (
            f"three render as" in txt
        ),
    }
    # numeric agreement: collapse count text "Six of nine"
    if not re.search(r"Six of (the )?nine", txt):
        err("konzen-puzzle.html missing 'Six of nine … collapse' phrasing (canon n_collapse=6)")
    for label, ok in want.items():
        if not ok:
            err(f"konzen-puzzle.html: expected {label}")


# ── Guard 4: a contiguous list of the surname trail must be the canonical 8,
#    in canonical (chronological) order. Operates on tag-stripped lines and only
#    on contiguous list "runs" (names joined by separators / "and"), so prose
#    that merely mentions a name out of sequence is not falsely flagged. ───────
_TAG = re.compile(r"<[^>]+>")
_NAMES = [a["spelling"] for a in sc.ATT]
_NAME_RE = "|".join(_NAMES)
# name, optional year, then >=1 (connector + name + optional year)
_RUN = re.compile(
    rf"(?:{_NAME_RE})(?:\s+1[89]\d{{2}})?"
    rf"(?:\s*(?:,|·|&middot;|/|&amp;|&)\s*(?:and\s+)?(?:{_NAME_RE})(?:\s+1[89]\d{{2}})?)+"
)


def check_order() -> None:
    for p in iter_targets():
        if p.suffix != ".html":
            continue
        for i, raw in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            line = _TAG.sub(" ", raw)
            for m in _RUN.finditer(line):
                toks = re.findall(_NAME_RE, m.group(0))
                # only judge near-full trail runs (bookended Gonnson … Conson);
                # shorter subset lists (e.g. the 5-name phonetic cluster) are fine.
                if len(toks) < 7 or toks[0] != "Gonnson" or toks[-1] != "Conson":
                    continue
                if toks != _NAMES:
                    err(f"{p.relative_to(ROOT)}:{i} — surname-trail list is not the "
                        f"canonical eight in order (got {' · '.join(toks)})")


# ── Guard 5: digit-form metric counts (e.g. SVG/metric boxes) must match canon.
#    Operates on tag-stripped text so markup-separated metrics like
#    <span class="num">7</span><span class="lbl">American spellings</span> are caught
#    (these evade every word-based "seven→eight" pass). ──────────────────────────
# digit restricted to 1–2 chars so 4-digit years (1866, 1896) can't be read as counts
_METRIC = [
    (re.compile(r"\b(\d{1,2})\+?\s+(?:distinct\s+)?American\s+(?:spellings|renderings)\b"),
     "n_spellings"),
    (re.compile(r"\b(\d{1,2})\+?\s+(?:independent\s+|different\s+)?attestations\b"),
     "n_attestations"),
]


def check_metric_counts() -> None:
    for p in iter_targets():
        if p.suffix != ".html":
            continue
        text = _TAG.sub(" ", p.read_text(encoding="utf-8", errors="ignore"))
        for rx, key in _METRIC:
            want = sc.CANON[key]
            for m in rx.finditer(text):
                if int(m.group(1)) != want:
                    err(f"{p.relative_to(ROOT)} — metric '{m.group(0).strip()}' "
                        f"disagrees with canon {key}={want}")


def main() -> int:
    print("surname-canon guard (data/surname-attestations.json)")
    print(f"  canon: {sc.CANON['n_attestations']} attestations · "
          f"{sc.CANON['n_collapse']} collapse "
          f"({sc.CANON['n_kon']} [kɔn] / {sc.CANON['n_gon']} [ɡɔn]) · "
          f"{sc.CANON['n_outliers']} outliers · {sc.CANON['n_scribes']} scribes")
    check_freshness()
    check_stale()
    check_counts()
    check_order()
    check_metric_counts()
    if fail:
        print("✗ surname-canon guard FAILED — see above.")
    else:
        print("✓ surname-canon guard clean.")
    return fail


if __name__ == "__main__":
    raise SystemExit(main())
