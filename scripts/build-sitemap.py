#!/usr/bin/env python3
"""
Generate sitemap.xml from all canonical HTML pages, excluding archives,
notes, and other non-public directories.

Reads each HTML page's lastmod from filesystem mtime, picks priority by
URL depth and section, and writes sitemap.xml at the project root.
"""
from __future__ import annotations
import datetime
import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://charles-research.netlify.app"

SKIP_PREFIXES = (
    "notes/", "_archive", "_backup_originals/", "_deploy_netlify/",
    "scripts/", "nara_pages/", "nara_ocr/", "node_modules/",
    "_test-spec.html",
    # Recovery snapshot dir — excluded from deploy in .netlifyignore (8 Jun 2026).
    "_recovery_20260608/", "_recovery",
    # Exclude shared partials (sitemap pollution flagged 16 May 2026).
    "assets/",
    # Internal author-side pages — noindex'd and in .netlifyignore (17 May 2026 audit pass).
    "styleguide.html",
    "peter_charts_download_checklist.html",
    # Folded into the SPA (30 May 2026) — now redirect stubs.
    "overview.html", "charles-in-america.html", "civil-war.html",
    "immigration-journey.html", "people-in-the-story.html", "family-tree-spa.html",
    "key-evidence.html", "schrader-correspondence.html", "foundation.html",
    "latest-findings.html", "source-archive.html", "germany-and-origins.html",
)

# Priority hints by path-prefix
PRIORITY_HINTS = [
    ("index.html",      1.0),
    ("abstract.html",   0.95),
    ("methodology.html",0.9),
    ("faq.html",        0.85),
    ("evidence/",       0.85),
    ("germany/",        0.85),
    ("civilwar/",       0.8),
    ("immigration/",    0.8),
    ("people/",         0.8),
    ("sources/",        0.8),
    ("towns/",          0.8),
    ("children/",       0.8),
    ("about.html",      0.75),
    ("contribute.html", 0.7),
    ("open-questions.html", 0.7),
    ("bibliography.html", 0.7),
    ("glossary.html",   0.65),
    ("changelog.html",  0.55),
    ("visualize.html",  0.85),
    ("stories.html",    0.75),
    ("cast.html",       0.7),
    ("family-poster.html", 0.6),
    ("tree-interactive.html", 0.7),
    ("Family_Tree_All_Families.html", 0.6),
    ("Kontze_Family_Tree_Graphic.html", 0.5),
    ("404.html",        0.0),  # don't list
    ("styleguide.html", 0.3),
    ("evidence-index.html", 0.5),
    ("peter_charts_download_checklist.html", 0.0),
    ("updates.html", 0.5),
]


def priority_for(rel: str) -> float:
    for prefix, p in PRIORITY_HINTS:
        if rel == prefix or rel.startswith(prefix):
            return p
    # default
    return 0.5


def main() -> int:
    today = datetime.date.today().isoformat()
    entries: list[tuple[str, str, float]] = []  # (loc, lastmod, priority)
    seen = set()

    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if any(rel.startswith(p) for p in SKIP_PREFIXES):
            continue
        # Dated manual backups (e.g. *.backup_20260622_031621.html) — excluded
        # from deploy via .netlifyignore (**/*.backup_*); never list in sitemap.
        if ".backup_" in rel:
            continue
        if rel in seen:
            continue
        seen.add(rel)

        prio = priority_for(rel)
        if prio <= 0:
            continue

        # Pretty URLs: drop /index.html
        loc_path = rel
        if loc_path == "index.html":
            loc_path = ""
        elif loc_path.endswith("/index.html"):
            loc_path = loc_path[:-10]
        loc = f"{BASE}/{loc_path}" if loc_path else f"{BASE}/"

        try:
            mtime = datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()
        except Exception:
            mtime = today

        entries.append((loc, mtime, prio))

    # build XML
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, prio in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(loc)}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        if loc.endswith("/"):
            lines.append("    <changefreq>weekly</changefreq>")
        else:
            lines.append("    <changefreq>monthly</changefreq>")
        lines.append(f"    <priority>{prio:.2f}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")

    out = ROOT / "sitemap.xml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} with {len(entries)} URLs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
