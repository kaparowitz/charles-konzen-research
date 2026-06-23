#!/usr/bin/env python3
"""
Sync the home page's SPA sections to match their standalone-file counterparts.

The site has historically maintained two copies of every section's content:
  1. <section id="germany" class="page">...</section> inside index.html (SPA tab)
  2. germany-and-origins.html as a standalone file (direct-URL access)

These could drift apart, leaving visitors with two different versions of the
same tab depending on how they arrived. This script picks one direction —
**standalone files are canonical** — and copies the content of each
standalone <main>...</main> into its matching SPA section in index.html,
preserving the <section> wrapper and the <h2> heading.

Usage:
    python3 scripts/sync-spa-sections.py            # apply
    python3 scripts/sync-spa-sections.py --check    # diff only, no write
    python3 scripts/sync-spa-sections.py --only=germany,charles  # subset
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

# section id (SPA) → standalone html file
SECTION_TO_FILE = {
    "overview":    "latest-findings.html",
    "glance":      "overview.html",
    "foundation":  "foundation.html",
    "germany":     "germany-and-origins.html",
    "immigration": "immigration-journey.html",
    "charles":     "charles-in-america.html",
    "civilwar":    "civil-war.html",
    "people":      "people-in-the-story.html",
    "tree":        "family-tree-spa.html",
    "evidence":    "evidence-index.html",
    "schrader":    "schrader-correspondence.html",
}

# Per-section heading text (preserved on the <h2> inside the SPA section)
SECTION_TO_HEADING = {
    "overview":    "Home",
    "glance":      "Overview",
    "foundation":  "Foundation (2020)",
    "germany":     "Germany &amp; Origins",
    "immigration": "Immigration Journey",
    "charles":     "Charles in America",
    "civilwar":    "Civil War",
    "people":      "People in the Story",
    "tree":        "Family Tree",
    "evidence":    "Key Evidence",
    "schrader":    "Peter Schräder Correspondence",
}


def find_section(html: str, sec_id: str) -> tuple[int, int] | None:
    """Return (start, end) byte offsets of the full <section id="..."> ... </section>
    block, with proper nesting. None if the section isn't present."""
    pat = f'<section id="{sec_id}"'
    start = html.find(pat)
    if start == -1:
        return None
    depth = 0
    i = start
    while i < len(html):
        if html.startswith("<section", i):
            depth += 1
            i += 8
        elif html.startswith("</section>", i):
            depth -= 1
            if depth == 0:
                return start, i + len("</section>")
            i += len("</section>")
        else:
            i += 1
    return None


def extract_main_inner(standalone_html: str) -> str | None:
    """Return the inner content of <main ...>...</main> in a standalone page,
    or None if no <main> is found."""
    m = re.search(r'<main[^>]*>([\s\S]+?)</main>', standalone_html)
    if not m:
        return None
    return m.group(1).strip("\n")


def main() -> int:
    args = sys.argv[1:]
    check_only = "--check" in args
    only_arg = next((a for a in args if a.startswith("--only=")), None)
    only_set = set(only_arg.split("=", 1)[1].split(",")) if only_arg else None

    if not INDEX.exists():
        print(f"ERROR: {INDEX} not found", file=sys.stderr)
        return 1

    idx_html = INDEX.read_text(encoding="utf-8")
    original = idx_html
    changes = []

    # Iterate over a stable order so byte offsets stay sane (largest-offset-first
    # so earlier edits don't shift later ones).
    items = list(SECTION_TO_FILE.items())
    # Compute current offsets and sort descending to splice from end to start
    offsets = []
    for sec_id, fname in items:
        bounds = find_section(idx_html, sec_id)
        if bounds is None:
            continue
        offsets.append((bounds[0], bounds[1], sec_id, fname))
    offsets.sort(reverse=True)

    for start, end, sec_id, fname in offsets:
        if only_set and sec_id not in only_set:
            continue
        standalone_path = ROOT / fname
        if not standalone_path.exists():
            print(f"  ! {sec_id}: standalone file missing: {fname} — skipped")
            continue
        try:
            standalone = standalone_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            standalone = standalone_path.read_text(encoding="latin-1")
        main_inner = extract_main_inner(standalone)
        if main_inner is None:
            print(f"  ! {sec_id}: no <main> tag in {fname} — skipped")
            continue

        heading = SECTION_TO_HEADING.get(sec_id, sec_id.title())
        # Preserve the existing class on the <section> opener (active / page etc.)
        opening_match = re.match(r'<section id="[^"]+" class="([^"]*)"[^>]*>', idx_html[start:start+200])
        section_class = opening_match.group(1) if opening_match else "page"

        new_block = (
            f'<section id="{sec_id}" class="{section_class}">\n'
            f'  <h2>{heading}</h2>\n'
            f'{main_inner}\n'
            f'</section>'
        )
        old_block = idx_html[start:end]
        if old_block != new_block:
            idx_html = idx_html[:start] + new_block + idx_html[end:]
            changes.append((sec_id, len(old_block), len(new_block)))

    if not changes:
        print("No changes needed — every SPA section already matches its standalone file.")
        return 0

    for sec_id, oldn, newn in changes:
        delta = newn - oldn
        sign = "+" if delta >= 0 else ""
        print(f"  ✓ {sec_id}: {oldn:,} → {newn:,} chars ({sign}{delta:,})")

    if check_only:
        print(f"\n--check: {len(changes)} section(s) would be updated. No file written.")
        return 0

    INDEX.write_text(idx_html, encoding="utf-8")
    print(f"\nWrote {INDEX} ({len(idx_html):,} bytes).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
