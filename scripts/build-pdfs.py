#!/usr/bin/env python3
"""
Render the citable static pages (abstract, methodology, errata) to PDF using
the page's own print stylesheet, so the output matches what a researcher would
get from Cmd+P.  PDFs land at the project root next to their HTML source,
linkable from the Abstract / Methodology pages.

Dependencies:
    pip install weasyprint

Usage:
    python3 scripts/build-pdfs.py            # render the default set
    python3 scripts/build-pdfs.py page.html  # render a specific page
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DEFAULTS = [
    ROOT / "abstract.html",
    ROOT / "methodology.html",
    ROOT / "errata.html",
    ROOT / "bibliography.html",
]


def render(src: Path) -> Path:
    try:
        from weasyprint import HTML
    except ImportError:
        print("error: weasyprint not installed.  pip install weasyprint", file=sys.stderr)
        sys.exit(2)
    out = src.with_suffix(".pdf")
    print(f"  rendering {src.name} -> {out.name}")
    HTML(filename=str(src), base_url=str(ROOT)).write_pdf(str(out), presentational_hints=True)
    return out


def main(argv: list[str]) -> int:
    if argv:
        targets = [Path(a) if Path(a).is_absolute() else (ROOT / a) for a in argv]
    else:
        targets = DEFAULTS
    for t in targets:
        if not t.exists():
            print(f"  skipping {t.name} (not found)")
            continue
        render(t)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
