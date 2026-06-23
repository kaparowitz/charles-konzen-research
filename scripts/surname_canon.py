#!/usr/bin/env python3
"""
surname_canon.py — shared loader + renderers for the American surname trail.

Single source of truth: data/surname-attestations.json
Consumers:
  - scripts/build-surname-trail.py   (renders the konzen-puzzle tables)
  - scripts/build-evidence-cards.py  (surname-list string + 1890 reading)
  - scripts/check_surname_canon.py    (deploy-gate consistency check)

Nothing here hard-codes a count. Every number is derived from the JSON, so
adding/removing an attestation in the JSON updates the tables, the counts,
and the checks together — the propagation-cascade bug cannot recur.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "surname-attestations.json"


def load() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


_d = load()
ATT = _d["attestations"]
CANON_RAW = _d["canon"]
READINGS = _d["readings"]


def _is_kon(a: dict) -> bool:
    return a["ipa"].lstrip().startswith("[ˈk")


# ── Derived counts (never hard-coded) ────────────────────────────────────────
CLUSTER = [a for a in ATT if a["cluster"]]
OUTLIERS = [a for a in ATT if not a["cluster"]]

CANON = {
    "n_spellings": len({a["spelling"] for a in ATT}),
    "n_attestations": len(ATT),
    "n_scribes": CANON_RAW["scribes_min"],
    "n_collapse": len(CLUSTER),
    "n_kon": sum(1 for a in CLUSTER if _is_kon(a)),
    "n_gon": sum(1 for a in CLUSTER if not _is_kon(a)),
    "n_outliers": len(OUTLIERS),
    "year_first": CANON_RAW["year_first"],
    "year_last": CANON_RAW["year_last"],
    "span_years": CANON_RAW["span_years"],
}


# ── Canonical strings ────────────────────────────────────────────────────────
def spelling_list_dotsep() -> str:
    """'Gonnson 1866 · Gansen 1870 · … · Conson 1896'"""
    return " · ".join(f"{a['spelling']} {a['year']}" for a in ATT)


def spelling_names_comma() -> str:
    """'Gonnson, Gansen, …, Conson'"""
    return ", ".join(a["spelling"] for a in ATT)


# ── Table renderers (output matches germany/konzen-puzzle.html structure) ─────
def chronology_table_html() -> str:
    rows = []
    for a in ATT:
        tr_cls = f' class="{a["row_class"]}"' if a["row_class"] else ""
        sur_cls = "surname cluster" if a["cluster"] else "surname"
        name = a["spelling"]
        if a["row_class"] == "konzen-keystone":
            name = f"<strong>{name}</strong>"
        name += a["spelling_suffix_html"]
        speaks = a["speaks_html"]
        speaks = f'<span class="speaker-flag">{speaks}</span>' if a["speaks_emph"] else speaks
        rows.append(
            f'      <tr{tr_cls}>\n'
            f'        <td>{a["year"]}</td>\n'
            f'        <td>{a["record_html"]}</td>\n'
            f'        <td class="{sur_cls}">{name}</td>\n'
            f'        <td>{a["scribe_html"]}</td>\n'
            f'        <td>{speaks}</td>\n'
            f'      </tr>'
        )
    body = "\n".join(rows)
    return (
        '<div class="surname-chronology">\n'
        '  <table>\n'
        '    <thead>\n'
        '      <tr>\n'
        '        <th>Year</th>\n'
        '        <th>Record</th>\n'
        '        <th>Surname recorded</th>\n'
        '        <th>Scribe</th>\n'
        '        <th>Charles speaks?</th>\n'
        '      </tr>\n'
        '    </thead>\n'
        '    <tbody>\n'
        f'{body}\n'
        '    </tbody>\n'
        '  </table>\n'
        '</div>'
    )


def phonetic_table_html() -> str:
    rows = ['    <tr><th>Year</th><th>Rendering</th><th>IPA</th><th>Charles informant?</th></tr>']
    for a in CLUSTER:
        bold = _is_kon(a) or a["phonetic_informant_yes"]
        name = f"<strong>{a['spelling']}</strong>" if bold else a["spelling"]
        name += a["spelling_suffix_html"]
        cls = "speaker-yes" if a["phonetic_informant_yes"] else "speaker-no"
        rows.append(
            f'    <tr><td>{a["year"]}</td><td>{name}</td>'
            f'<td><span class="ipa">{a["ipa"]}</span></td>'
            f'<td><span class="{cls}">{a["phonetic_informant_html"]}</span></td></tr>'
        )
    return "  <table>\n" + "\n".join(rows) + "\n  </table>"


if __name__ == "__main__":
    import sys
    print("CANON:", CANON, file=sys.stderr)
    print(spelling_list_dotsep())
