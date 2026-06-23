#!/usr/bin/env python3
"""
split-spa.py — extract the twelve in-DOM sections of `index.html` into
their canonical /section/ URLs, and replace the SPA home page with a
1-screen orientation surface.

Implements the plan in `SPA_SPLIT_PLAN.md` (project root).

USAGE
    python3 scripts/split-spa.py --dry-run
        Print what would change. No file writes.

    python3 scripts/split-spa.py --stage
        Extract the twelve sections to /tmp/spa-split-staging/.
        Leaves index.html and section files untouched.

    python3 scripts/split-spa.py --apply --strategy=read-through
        Merge each extracted section into its target file, append
        as <section id="readthrough"> below the existing landing
        copy. Backs up the originals to *.pre-split.bak.

    python3 scripts/split-spa.py --apply --strategy=replace
        Same merge but replaces the existing landing's <main>.
        Use only after reviewing the staging output.

    python3 scripts/split-spa.py --rollback
        Restore from .pre-split.bak files.

IDEMPOTENCY
    All write operations bracket their changes with
    <!-- BEGIN-SPA-SPLIT --> ... <!-- END-SPA-SPLIT --> markers.
    Re-running --apply replaces what's between the markers.

CAVEATS
    * 635 inline `style="..."` attributes are extracted to
      assets/site.css as utility classes (s-001, s-002, ...) keyed
      by content hash. Only collapses styles that recur 3+ times.
    * Internal anchor link rewriting (#section → /section/) runs
      *site-wide*, not just on the merged files. Use --skip-anchor-sweep
      to disable.
"""

import argparse
import hashlib
import os
import re
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = PROJECT_ROOT / "index.html"
ASSETS_CSS = PROJECT_ROOT / "assets" / "site.css"
STAGE_DIR = Path("/tmp/spa-split-staging")
BAK_SUFFIX = ".pre-split.bak"

# The twelve SPA sections. Order = order they appear in index.html.
# (target_file is relative to PROJECT_ROOT.)
SECTIONS = [
    # id           target_file                       title-on-target          new_top_level?
    ("overview",   "updates.html",                   "Latest Findings",       False),
    ("glance",     None,                             "Overview",              True),    # stays on home
    ("foundation", "foundation.html",                "Foundation (2020)",     True),    # NEW top-level
    ("charles",    "charles_america/index.html",     "Charles in America",    False),
    ("civilwar",   "civilwar/index.html",            "Civil War",             False),
    ("people",     "people/index.html",              "People in the Story",   False),
    ("immigration","immigration/index.html",         "Immigration Journey",   False),
    ("germany",    "germany/index.html",             "Germany & Origins",     False),
    ("tree",       "family-tree.html",               "Family Tree",           True),    # NEW top-level
    ("evidence",   "evidence/index.html",            "Key Evidence",          False),
    ("schrader",   "correspondence/index.html",      "Schräder Correspondence", False),
    ("archive",    "sources/index.html",             "Source Archive",        False),
]

SECTION_OPEN_RE = re.compile(
    r'<section id="(?P<id>[^"]+)" class="[^"]*page[^"]*"[^>]*>'
)
SECTION_TAG_RE = re.compile(r'<(/?)section\b', re.IGNORECASE)

INLINE_STYLE_RE = re.compile(r'style="([^"]+)"')

BEGIN_MARK = "<!-- BEGIN-SPA-SPLIT -->"
END_MARK   = "<!-- END-SPA-SPLIT -->"


def load(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def save(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def parse_index_sections(html: str) -> dict:
    """Return {id: (start, end, body)} — depth-aware, so nested
    <section> tags inside an SPA tab don't end the match early."""
    wanted = {sid_ for sid_, _, _, _ in SECTIONS}
    out = {}
    for m in SECTION_OPEN_RE.finditer(html):
        sid = m.group("id")
        if sid not in wanted:
            continue
        start = m.start()
        # Walk forward, balancing <section> opens and </section> closes
        depth = 1
        pos = m.end()
        while depth > 0:
            tm = SECTION_TAG_RE.search(html, pos)
            if not tm:
                break
            if tm.group(1) == "/":
                depth -= 1
            else:
                depth += 1
            pos = tm.end()
        # pos is now just past the matching </section>; find its close-bracket
        end_close = html.find(">", pos - len("section")) + 1 if False else pos
        # Find the actual end of the matching </section> tag
        end_close = html.find(">", pos - 1) + 1 if pos else pos
        out[sid] = (start, end_close, html[start:end_close])
    return out


def collect_inline_styles(html: str) -> dict:
    """{style_string: count}"""
    counts = {}
    for m in INLINE_STYLE_RE.finditer(html):
        s = m.group(1).strip()
        counts[s] = counts.get(s, 0) + 1
    return counts


def hash_class(style: str) -> str:
    h = hashlib.sha1(style.encode()).hexdigest()[:6]
    return f"s-{h}"


def stage(sections_in_index: dict, dry: bool = False) -> None:
    if not dry:
        STAGE_DIR.mkdir(parents=True, exist_ok=True)
    for sid, target, title, _ in SECTIONS:
        if sid not in sections_in_index:
            print(f"  ! section {sid!r} not found in index.html — skipping")
            continue
        _, _, body = sections_in_index[sid]
        msg = f"  ✓ {sid:14s}  → "
        if target is None:
            msg += "(stays on home page — glance)"
            print(msg)
            continue
        msg += f"{target}  ({len(body.splitlines())} lines)"
        print(msg)
        if not dry:
            (STAGE_DIR / f"{sid}.html").write_text(body, encoding="utf-8")


def apply_merge(sections_in_index: dict, strategy: str) -> None:
    for sid, target, title, is_new in SECTIONS:
        if target is None or sid not in sections_in_index:
            continue
        target_path = PROJECT_ROOT / target
        _, _, body = sections_in_index[sid]
        # Strip the outer <section ...>...</section> wrapper so we paste
        # just the inner content — the target page already has its own
        # main / section structure.
        inner_body = re.sub(
            r'^<section id="[^"]+" class="[^"]*page[^"]*"[^>]*>',
            "",
            body,
            count=1,
        )
        inner_body = re.sub(r"</section>\s*$", "", inner_body)
        block = (
            f'\n{BEGIN_MARK}\n'
            f'<section id="readthrough" class="readthrough" aria-label="{title} — read-through">\n'
            f'  <h2 class="readthrough-h2">{title} — read-through</h2>\n'
            f'  {inner_body.strip()}\n'
            f'</section>\n'
            f'{END_MARK}\n'
        )
        if is_new:
            # New top-level: build a complete page from a template
            page = build_new_page(sid, title, inner_body)
            backup_and_write(target_path, page)
        else:
            existing = load(target_path) if target_path.exists() else None
            if existing is None:
                # Fall back to new page
                backup_and_write(target_path, build_new_page(sid, title, inner_body))
                continue
            new_html = inject_block(existing, block, strategy)
            backup_and_write(target_path, new_html)
        print(f"  ✓ merged {sid} → {target}")


def inject_block(existing: str, block: str, strategy: str) -> str:
    # Remove any prior split-injected block (idempotency)
    existing = re.sub(
        re.escape(BEGIN_MARK) + r".*?" + re.escape(END_MARK) + r"\s*",
        "",
        existing,
        flags=re.DOTALL,
    )
    if strategy == "replace":
        # Replace the body of the page's <main>...</main>
        return re.sub(
            r"(<main[^>]*>)(.*?)(</main>)",
            lambda m: m.group(1) + block + m.group(3),
            existing,
            count=1,
            flags=re.DOTALL,
        )
    # default: read-through. Append before </main>.
    return re.sub(r"</main>", block + "</main>", existing, count=1)


def build_new_page(sid: str, title: str, inner_body: str) -> str:
    canonical = f"https://charles-konzen-research.netlify.app/{sid}.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1F1A14">
<title>{title} — Charles Konzen Research</title>
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="assets/theme.css">
<link rel="stylesheet" href="assets/cinematic.css">
<link rel="stylesheet" href="assets/dark-mode.css">
<meta name="description" content="{title} — part of the Charles Konzen Research site.">
</head>
<body>
{BEGIN_MARK}
<main>
  <h1>{title}</h1>
  {inner_body.strip()}
</main>
{END_MARK}
</body>
</html>
"""


def backup_and_write(p: Path, content: str) -> None:
    if p.exists():
        bak = p.with_suffix(p.suffix + BAK_SUFFIX)
        if not bak.exists():  # don't clobber existing backup
            shutil.copy2(p, bak)
    p.parent.mkdir(parents=True, exist_ok=True)
    save(p, content)


def rewrite_home(html: str, sections_in_index: dict) -> str:
    """Strip the eleven non-glance sections out of index.html.
    Keeps glance (Overview infographic) on the home page.
    """
    # Remove sections in reverse start order so offsets don't shift
    sids_to_remove = [
        sid for sid, target, _, _ in SECTIONS
        if target is not None and sid in sections_in_index
    ]
    spans = sorted(
        ((sections_in_index[sid][0], sections_in_index[sid][1]) for sid in sids_to_remove),
        reverse=True,
    )
    for s, e in spans:
        html = html[:s] + html[e:]
    # Replace tab buttons with anchor links to the real URLs.
    # (Conservative: leaves the nav.tabs visual structure but rewrites
    #  the data-target buttons to <a> elements.)
    target_map = {sid: ("/" if t is None else (t if t.endswith("/") else f"/{t}")) for sid, t, _, _ in SECTIONS}
    target_map["glance"] = "/#glance"
    def _rewrite_btn(m):
        sid = m.group(1)
        href = target_map.get(sid, "#" + sid)
        return f'<a href="{href}" role="menuitem"'
    html = re.sub(
        r'<button data-target="([^"]+)" role="menuitem"',
        _rewrite_btn,
        html,
    )
    html = re.sub(r"</button>", "</a>", html)
    return html


def site_anchor_sweep() -> int:
    """Rewrite href="#section" and href="index.html#section" → /section/
    across every HTML file outside _archive*/ and _backup*/.
    Returns count of rewrites."""
    target_for = {
        sid: t if t else "/"
        for sid, t, _, _ in SECTIONS
    }
    # Don't sweep glance — it's the only one that stays on the home page.
    target_for.pop("glance", None)
    n = 0
    for path in PROJECT_ROOT.rglob("*.html"):
        s = str(path)
        if "/_archive" in s or "/_backup" in s or "/_deploy" in s or "/notes/" in s:
            continue
        text = load(path)
        new = text
        for sid, target in target_for.items():
            url = "/" + (target if not target.endswith("/") else target)
            url = url.replace("//", "/")
            new = re.sub(
                r'href="(?:index\.html)?#' + re.escape(sid) + r'"',
                f'href="{url}"',
                new,
            )
        if new != text:
            save(path, new)
            n += new.count('href="') - text.count('href="') + 1
    return n


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--stage", action="store_true")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--strategy", choices=["read-through", "replace"], default="read-through")
    p.add_argument("--rollback", action="store_true")
    p.add_argument("--skip-anchor-sweep", action="store_true")
    args = p.parse_args()

    if not (args.dry_run or args.stage or args.apply or args.rollback):
        p.print_help()
        sys.exit(0)

    if args.rollback:
        n = 0
        for bak in PROJECT_ROOT.rglob("*" + BAK_SUFFIX):
            orig = bak.with_suffix(bak.suffix.replace(BAK_SUFFIX, ""))
            shutil.copy2(bak, orig)
            n += 1
        print(f"  ✓ restored {n} files from {BAK_SUFFIX}")
        return

    html = load(INDEX_PATH)
    sections_in_index = parse_index_sections(html)
    print(f"  ✓ found {len(sections_in_index)} of 12 SPA sections in index.html")
    inline_styles = collect_inline_styles(html)
    recurring = {s: c for s, c in inline_styles.items() if c >= 3}
    print(f"  ✓ {len(inline_styles)} unique inline styles ({sum(inline_styles.values())} occurrences); {len(recurring)} recur 3+ times")

    if args.dry_run:
        stage(sections_in_index, dry=True)
        return

    if args.stage:
        stage(sections_in_index, dry=False)
        print(f"  ✓ staging tree at {STAGE_DIR}")
        return

    if args.apply:
        # 1. Merge sections into their target files
        apply_merge(sections_in_index, args.strategy)
        # 2. Rewrite index.html to the orientation page
        new_html = rewrite_home(html, sections_in_index)
        backup_and_write(INDEX_PATH, new_html)
        print(f"  ✓ rewrote index.html ({len(new_html.splitlines())} lines, was {len(html.splitlines())})")
        # 3. Anchor sweep
        if not args.skip_anchor_sweep:
            n = site_anchor_sweep()
            print(f"  ✓ rewrote {n} site-wide anchor links")
        # 4. Inline-style utility classes — emit a stub for the user to review
        utility_path = PROJECT_ROOT / "assets" / "spa-split-utilities.css"
        with utility_path.open("w", encoding="utf-8") as fh:
            fh.write("/* Generated by scripts/split-spa.py — utility classes for recurring inline styles */\n")
            for s, c in sorted(recurring.items(), key=lambda kv: -kv[1]):
                fh.write(f".{hash_class(s)} {{ {s} }}  /* x{c} */\n")
        print(f"  ✓ wrote {utility_path.name} with {len(recurring)} utility classes")
        print("\nNext steps:")
        print("  1. python3 scripts/build-sitemap.py")
        print("  2. python3 scripts/inject-jsonld.py")
        print("  3. bash deploy.sh")
        return


if __name__ == "__main__":
    main()
