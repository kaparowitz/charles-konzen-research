#!/usr/bin/env python3
"""
Inject schema.org Article JSON-LD into every public content page that has
a BreadcrumbList but no Article block yet.

For each page:
- headline ← <title> (with " — Charles Konzen Research" stripped)
- description ← <meta name="description"> content
- url ← canonical URL or derived from path
- datePublished ← stable derived from file path
- dateModified ← filesystem mtime
- author / publisher / inLanguage / license / isPartOf ← project-wide constants

Bracketed by <!-- BEGIN-INJECTED-ARTICLE --> markers for idempotent re-runs.
"""
from __future__ import annotations
import json
import os
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://charles-konzen-research.netlify.app"

MARKER_BEGIN = "<!-- BEGIN-INJECTED-ARTICLE -->"
MARKER_END = "<!-- END-INJECTED-ARTICLE -->"

AUTHOR = {"@type": "Person", "name": "Jed Johnson"}
CONTRIBUTOR = {"@type": "Person", "name": "Peter Schräder"}
PUBLISHER = {
    "@type": "Person",
    "name": "Jed Johnson",
    "url": f"{BASE}/about.html",
}
IS_PART_OF = {"@id": f"{BASE}/#website"}
LICENSE = "https://creativecommons.org/licenses/by-nc-sa/4.0/"


def extract_title(s: str) -> str:
    m = re.search(r'<title>([^<]+)</title>', s)
    if not m:
        return ""
    t = m.group(1).strip()
    # Strip site-suffix patterns
    t = re.sub(r'\s+[—·-]\s+Charles\s+Konzen\s+Research\s*$', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\s+·\s+Charles\s+Gannsen\s+\w+\s*$', '', t, flags=re.IGNORECASE)
    return t.strip()


def extract_description(s: str) -> str:
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', s)
    if not m:
        return ""
    desc = m.group(1).strip()
    # Decode common HTML entities
    desc = desc.replace("&amp;", "&").replace("&quot;", '"').replace("&apos;", "'")
    desc = desc.replace("&lt;", "<").replace("&gt;", ">").replace("&nbsp;", " ")
    return desc


def extract_canonical(s: str, fallback_path: str) -> str:
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', s)
    if m:
        return m.group(1)
    return f"{BASE}/{fallback_path}"


def build_article(p: Path, rel: str) -> dict:
    s = p.read_text(encoding="utf-8")
    headline = extract_title(s) or rel.replace(".html", "").split("/")[-1].replace("-", " ").title()
    description = extract_description(s)
    url = extract_canonical(s, rel)
    mtime = datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()

    art = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": f"{url}#article",
        "headline": headline,
        "url": url,
        "isPartOf": IS_PART_OF,
        "author": [AUTHOR, CONTRIBUTOR],
        "publisher": PUBLISHER,
        "inLanguage": "de-DE" if rel.startswith("de/") else "en-US",
        "license": LICENSE,
        "dateModified": mtime,
    }
    if description:
        art["description"] = description
    return art


def inject(p: Path) -> str:
    rel = p.relative_to(ROOT).as_posix()
    if rel.startswith(("notes/", "_archive", "_backup_originals/", "_deploy_netlify/", "scripts/")):
        return "skipped"
    s = p.read_text(encoding="utf-8")
    if len(s) < 1500 or '<meta http-equiv="refresh"' in s:
        return "skipped"
    if "</head>" not in s:
        return "skipped"
    # Skip if Article already present
    if '"@type": "Article"' in s or '"@type":"Article"' in s:
        return "has-article"
    art = build_article(p, rel)
    block = MARKER_BEGIN + "\n<script type=\"application/ld+json\">\n" + json.dumps(art, indent=2, ensure_ascii=False) + "\n</script>\n" + MARKER_END
    if MARKER_BEGIN in s:
        new = re.sub(
            re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END),
            block,
            s,
            count=1,
            flags=re.DOTALL,
        )
    else:
        new = s.replace("</head>", block + "\n</head>", 1)
    if new != s:
        p.write_text(new, encoding="utf-8")
        return "updated"
    return "skipped"


def main() -> int:
    counts = {"updated": 0, "skipped": 0, "has-article": 0}
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(("notes/", "_archive", "_backup_originals/", "_deploy_netlify/", "scripts/")):
            continue
        status = inject(p)
        counts[status] = counts.get(status, 0) + 1
    print(f"Updated: {counts['updated']}  Already had Article: {counts['has-article']}  Skipped: {counts['skipped']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
