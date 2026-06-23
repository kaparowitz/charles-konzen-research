#!/usr/bin/env python3
"""
build-surname-trail.py — render the surname-trail tables from the single source.

Reads data/surname-attestations.json (via surname_canon) and rewrites the two
AUTOGEN regions in germany/konzen-puzzle.html:
  - AUTOGEN:surname-chronology   (the 8-row chronology table)
  - AUTOGEN:surname-phonetic     (the cluster phonetic table)

Idempotent: running it with no JSON change produces no diff. To change the
trail, edit the JSON and re-run this script — never hand-edit between markers.

Usage:  python3 scripts/build-surname-trail.py [--check]
        --check : exit 1 if the file is out of date (for CI), make no changes.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import surname_canon as sc  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "germany" / "konzen-puzzle.html"

REGIONS = {
    "surname-chronology": sc.chronology_table_html,
    "surname-phonetic": sc.phonetic_table_html,
}


def render(text: str) -> str:
    for name, fn in REGIONS.items():
        pat = re.compile(
            r"(<!-- AUTOGEN:" + re.escape(name) + r" START.*?-->)(.*?)(<!-- AUTOGEN:"
            + re.escape(name) + r" END -->)",
            re.DOTALL,
        )
        if not pat.search(text):
            raise SystemExit(f"ERROR: AUTOGEN markers for '{name}' not found in {TARGET}")
        text = pat.sub(lambda m: m.group(1) + "\n" + fn() + "\n" + m.group(3), text)
    return text


def main() -> int:
    check = "--check" in sys.argv
    original = TARGET.read_text(encoding="utf-8")
    updated = render(original)
    if updated == original:
        print("✓ surname-trail up to date (no change).")
        return 0
    if check:
        print("✗ surname-trail OUT OF DATE — run: python3 scripts/build-surname-trail.py")
        return 1
    TARGET.write_text(updated, encoding="utf-8")
    print(f"✓ regenerated surname-trail tables in {TARGET.relative_to(ROOT)} "
          f"({sc.CANON['n_attestations']} attestations, "
          f"{sc.CANON['n_collapse']} cluster / {sc.CANON['n_outliers']} outliers).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
