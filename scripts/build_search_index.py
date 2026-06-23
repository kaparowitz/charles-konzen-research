#!/usr/bin/env python3
"""
build_search_index.py — regenerate search-index.json from the standalone
HTML pages. The on-disk index was last hand-curated May 18, 2026; this
script makes it rebuildable on every deploy so new pages
(claims-dashboard.html, future research artifacts, etc.) become findable
through the site search without manual editing.

Schema, per existing assets/site-search.js consumer:
    [
      {
        "t": "<title text>",
        "h": "<first H1 / H2 / hero subtitle>",
        "u": "<relative URL from site root>",
        "d": "<meta description, ~200 chars>",
        "b": "<visible body text, capped at 2000 chars>",
        "k": "<kind: main|reference|person|family|source|town|child|civilwar|...>"
      },
      ...
    ]

Kind is assigned by directory:
    people/*       → person
    family_pages/* → family
    sources/*      → source
    towns/*        → town
    children/*     → child
    civilwar/*     → civilwar
    charles_america/* → charles
    immigration/*  → immigration
    germany/*      → germany
    correspondence/* → correspondence
    themes/*       → theme
    research_logs/* → research
    evidence/*     → evidence
    stories/*      → story
    Root pages — categorised individually below.

Usage:
    python3 scripts/build_search_index.py        # writes search-index.json at repo root
    python3 scripts/build_search_index.py --check # exit 1 if rebuild would change anything
"""
from __future__ import annotations
import argparse, json, os, re, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "search-index.json"

SKIP_DIRS = (
    "notes", "_archive", "_archive_pre_audit_fixes", "_backup_originals",
    "_deploy_netlify", "session_notes_docx", "scripts", ".git", ".netlify",
    "peter_charts", "nara_pages", "nara_ocr",
    "evidence_thumbs", "evidence_images", "family_photos",
    "assets",  # templates / non-page assets
)

# Root pages folded into the SPA (30 May 2026) — now redirect stubs, not indexed.
SKIP_FILES = (
    "overview.html", "charles-in-america.html", "civil-war.html",
    "immigration-journey.html", "people-in-the-story.html", "family-tree-spa.html",
    "key-evidence.html", "schrader-correspondence.html", "foundation.html",
    "latest-findings.html", "source-archive.html", "germany-and-origins.html",
)

# Root-level pages: explicit kind mapping. Anything not here defaults to "reference".
ROOT_KINDS = {
    "index.html": "main",
    "updates.html": "changelog",
    "changelog.html": "changelog",
    "errata.html": "reference",
    "abstract.html": "reference",
    "methodology.html": "reference",
    "bibliography.html": "reference",
    "glossary.html": "reference",
    "faq.html": "reference",
    "open-questions.html": "reference",
    "negative-results.html": "reference",
    "sponsor-reconciliation.html": "reference",
    "claims-dashboard.html": "reference",
    "source-archive.html": "reference",
    "evidence-index.html": "reference",
    "key-evidence.html": "main",
    "overview.html": "main",
    "stories.html": "main",
    "cast.html": "main",
    "charles-in-america.html": "main",
    "civil-war.html": "main",
    "germany-and-origins.html": "main",
    "immigration-journey.html": "main",
    "people-in-the-story.html": "main",
    "foundation.html": "main",
    "schrader-correspondence.html": "correspondence",
    "latest-findings.html": "changelog",
    "contribute.html": "reference",
    "about.html": "reference",
    "visualize.html": "reference",
    "family-poster.html": "reference",
    "family-tree-spa.html": "reference",
    "tree-interactive.html": "reference",
    "404.html": None,  # Excluded
}

DIR_KIND = {
    "people": "person",
    "family_pages": "family",
    "sources": "source",
    "towns": "town",
    "children": "child",
    "civilwar": "civilwar",
    "charles_america": "charles",
    "immigration": "immigration",
    "germany": "germany",
    "correspondence": "correspondence",
    "themes": "theme",
    "research_logs": "research",
    "evidence": "evidence",
    "stories": "story",
    "de": "reference",  # German translations
    "wikidata": "reference",
    "who": "reference",
    "well-known": None,
}


class PageExtractor(HTMLParser):
    """Pulls title, description, first heading, and visible body text."""
    def __init__(self):
        super().__init__()
        self.title_parts = []
        self.heading_parts = []
        self.body_parts = []
        self.description = ""
        self._in_title = False
        self._in_heading_tag = None
        self._heading_done = False
        # Skip text from these tags entirely
        self._skip_stack = 0
        self._skip_tags = {"script", "style", "nav", "footer", "noscript"}

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in self._skip_tags:
            self._skip_stack += 1
            return
        if tag == "title":
            self._in_title = True
            return
        if tag == "meta" and (d.get("name") == "description" or d.get("property") == "og:description"):
            if not self.description and d.get("content"):
                self.description = d["content"][:400]
            return
        # First H1, then H2, then H3 — whichever comes first
        if not self._heading_done and tag in ("h1", "h2", "h3"):
            self._in_heading_tag = tag

    def handle_endtag(self, tag):
        if tag in self._skip_tags and self._skip_stack > 0:
            self._skip_stack -= 1
            return
        if tag == "title":
            self._in_title = False
            return
        if tag == self._in_heading_tag:
            self._in_heading_tag = None
            self._heading_done = True

    def handle_data(self, data):
        if self._skip_stack > 0:
            return
        if self._in_title:
            self.title_parts.append(data)
        if self._in_heading_tag is not None:
            self.heading_parts.append(data)
        # Body text: collapse whitespace, only meaningful content
        text = data.strip()
        if text:
            self.body_parts.append(text)


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def relative_url(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace(os.sep, "/")


def kind_for(rel: str) -> str | None:
    """Return the kind string for this URL, or None if the page should be excluded."""
    if "/" in rel:
        first = rel.split("/", 1)[0]
        return DIR_KIND.get(first, "reference")
    return ROOT_KINDS.get(rel, "reference")


def should_skip(rel: str) -> bool:
    parts = rel.split("/")
    if any(p in SKIP_DIRS for p in parts[:-1]):
        return True
    if parts[-1] in SKIP_FILES:
        return True
    if kind_for(rel) is None:
        return True
    # Skip section index.html that duplicates the main page (e.g., people/index.html
    # is a directory listing, keep it; charles_america/index.html, keep it).
    return False


def extract_entry(path: Path) -> dict | None:
    rel = relative_url(path)
    if should_skip(rel):
        return None
    try:
        html = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        try:
            html = path.read_text(encoding="latin-1")
        except OSError:
            return None
    ex = PageExtractor()
    try:
        ex.feed(html)
    except Exception:
        return None
    title = normalize_ws("".join(ex.title_parts))
    heading = normalize_ws("".join(ex.heading_parts)) or title
    body = normalize_ws(" ".join(ex.body_parts))[:2000]
    # description: prefer meta description, fall back to first 250 chars of body
    desc = normalize_ws(ex.description) or body[:250]
    return {
        "t": title or rel,
        "h": heading,
        "u": rel,
        "d": desc[:400],
        "b": body,
        "k": kind_for(rel),
    }


def build() -> list[dict]:
    entries: list[dict] = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = relative_url(path)
        # Skip files inside excluded directories
        parts = rel.split("/")
        if any(p in SKIP_DIRS for p in parts[:-1]):
            continue
        # 404, hidden, archive
        if parts[-1] == "404.html":
            continue
        if any(p.startswith(".") for p in parts):
            continue
        # Skip stray files in `notes/` etc.
        if parts[0] in SKIP_DIRS:
            continue
        # Skip files explicitly tagged None
        if kind_for(rel) is None:
            continue
        entry = extract_entry(path)
        if entry is None:
            continue
        entries.append(entry)
    return entries


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="Exit 1 if rebuilding would change the on-disk index")
    args = ap.parse_args()
    entries = build()
    new_json = json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + "\n"
    if args.check:
        try:
            current = OUT.read_text(encoding="utf-8")
        except OSError:
            current = ""
        if current.strip() != new_json.strip():
            print(f"check: search-index.json would change ({len(entries)} entries)")
            return 1
        print(f"check: search-index.json up to date ({len(entries)} entries)")
        return 0
    OUT.write_text(new_json, encoding="utf-8")
    # Distribution
    from collections import Counter
    dist = Counter(e["k"] for e in entries)
    print(f"Wrote {OUT.name} — {len(entries)} entries")
    for k, n in sorted(dist.items(), key=lambda kv: -kv[1]):
        print(f"  {n:3d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
