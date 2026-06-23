#!/usr/bin/env python3
"""
Auto-link the FIRST occurrence of selected glossary terms on every content
page (excluding the glossary, changelog, errata, archives, scripts, and other
high-density pages where auto-linking would create noise).

Each linked term renders as a subtle dotted underline (.glossary-link CSS class)
that goes to glossary.html#g-<term>.

Idempotent: re-running skips paragraphs that already have .glossary-link.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path("/sessions/great-friendly-turing/mnt/Charles Gannsen Research")

# Terms to auto-link. Each entry: (regex pattern, glossary anchor).
# Patterns use \b word boundaries and are case-sensitive on proper nouns.
TERMS = [
    # German technical terms — high confidence (won't appear in normal English)
    (r"\bKirchenb(?:ü|u)cher\b", "kirchenbuch"),
    (r"\bKirchenbuch\b", "kirchenbuch"),
    (r"\bStammrollen?\b", "g-stammrolle"),
    (r"\bStammtafel\b", "g-stammtafel"),
    (r"\bAuswanderer-Belege?\b", "g-auswanderer-beleg"),
    (r"\bAuswanderung\b", "g-auswanderung"),
    (r"\bKurrent\b", "g-kurrent"),
    (r"\bSütterlin\b", "g-kurrent"),
    (r"\bBestattungsregister\b", "g-bestattung"),
    (r"\bBestattung\b", "g-bestattung"),
    (r"\bTrauungen?\b", "g-trauung"),
    (r"\bTaufen?\b", "g-taufe"),
    (r"\bPfarramt\b", "g-pfarramt"),
    (r"\bKirchenkreis\b", "g-kirchenkreis"),
    # Place / region terms
    (r"\bChurhessen\b", "g-churhessen"),
    (r"\bKurhessen\b", "g-kurhessen"),
    (r"\bKreis Hofgeismar\b", "g-kreis"),
    # Acronyms / project-specific
    (r"\bHTR\b", "g-htr"),
    (r"\bLAGIS\b", "g-lagis"),
    (r"\bGenealogical Proof Standard\b", "g-genealogical-proof-standard"),
    (r"\bCompiled Service Record\b", "g-compiled-service-record"),
    (r"\bCSR\b", "g-compiled-service-record"),
]

# Pages where auto-linking would be noisy or counter-productive.
EXCLUDE_FILES = {
    "glossary.html",       # The glossary itself
    "changelog.html",      # Histories of references
    "errata.html",         # Many glossary terms mentioned in context
    "index.html",          # SPA; selectors would multi-match across tabs
    "404.html",
    "styleguide.html",
    "feed.xml",
    "sitemap.xml",
}
EXCLUDE_DIRS = {"_archive_pre_audit_fixes", "_backup_originals", "_archive", "notes",
                ".git", "assets", "scripts", ".netlify", ".well-known", "themes",
                "evidence_thumbs", "evidence_images", "nara_ocr", "nara_pages",
                "session_notes_docx", "family_photos", "peter_charts", "de",
                "wikidata"}

# Marker used to skip already-processed paragraphs.
LINK_MARKER = "glossary-link"


def relative_glossary_path(page: Path) -> str:
    """Return relative path from this page to glossary.html."""
    rel = page.relative_to(ROOT)
    depth = len(rel.parts) - 1
    if depth == 0:
        return "glossary.html"
    return "../" * depth + "glossary.html"


def process_file(page: Path) -> tuple[int, list[str]]:
    """Insert auto-glossary links into the page. Returns (count, hit_terms)."""
    html = page.read_text(encoding="utf-8")
    glossary_url = relative_glossary_path(page)

    seen_anchors: set[str] = set()
    hits: list[str] = []

    # Find each term's first occurrence in plain text outside of <a>, <script>,
    # <style>, <title>, <meta>, <head>, and outside of tag attributes.
    # Approach: walk the HTML linearly; skip excluded zones; only match in
    # paragraph-level text.
    def walk_and_replace(html: str) -> str:
        out = []
        i = 0
        n = len(html)
        depth_no_link = 0   # inside <a>, <script>, <style>, <title>, <head>
        while i < n:
            ch = html[i]
            if ch == "<":
                # Find tag end
                j = html.find(">", i)
                if j == -1:
                    out.append(html[i:])
                    break
                tag = html[i:j+1]
                tag_lower = tag.lower()
                # Track entry/exit of zones we mustn't touch
                if tag_lower.startswith(("<a ", "<a>", "<script", "<style", "<title", "<head", "<noscript")):
                    depth_no_link += 1
                elif tag_lower.startswith(("</a>", "</script", "</style", "</title", "</head", "</noscript")):
                    depth_no_link = max(0, depth_no_link - 1)
                out.append(tag)
                i = j + 1
            else:
                # Plain text segment — scan for next "<"
                j = html.find("<", i)
                if j == -1:
                    j = n
                segment = html[i:j]
                if depth_no_link == 0:
                    segment = inject_first_occurrences(segment)
                out.append(segment)
                i = j
        return "".join(out)

    def inject_first_occurrences(text: str) -> str:
        for pattern, anchor in TERMS:
            if anchor in seen_anchors:
                continue
            m = re.search(pattern, text)
            if not m:
                continue
            seen_anchors.add(anchor)
            hits.append(anchor)
            replacement = (
                f'<a class="{LINK_MARKER}" '
                f'href="{glossary_url}#{anchor}" '
                f'title="Glossary: {m.group(0)}">'
                f'{m.group(0)}</a>'
            )
            text = text[:m.start()] + replacement + text[m.end():]
        return text

    if f'class="{LINK_MARKER}"' in html:
        # Already processed once. Re-scan only for terms not yet linked.
        # We can't easily tell which terms have been linked, so:
        # parse existing href anchors and mark them as seen.
        for href in re.findall(r'class="' + LINK_MARKER + r'"[^>]+href="[^#]*#([^"]+)"', html):
            seen_anchors.add(href)

    new_html = walk_and_replace(html)
    if new_html != html:
        page.write_text(new_html, encoding="utf-8")
    return len(hits), hits


def main():
    processed = 0
    total_links = 0
    pages_touched = 0

    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT)
        parts = rel.parts
        if any(p in EXCLUDE_DIRS for p in parts):
            continue
        if rel.parts[-1] in EXCLUDE_FILES:
            continue
        # Skip the glossary itself just in case
        if "glossary.html" in str(rel):
            continue
        # Process
        count, hits = process_file(path)
        processed += 1
        if count > 0:
            total_links += count
            pages_touched += 1
            if pages_touched <= 12:
                print(f"  {rel}: linked {count}  ({', '.join(hits)})")

    print()
    print(f"Pages processed: {processed}")
    print(f"Pages with new links: {pages_touched}")
    print(f"Total auto-glossary links added: {total_links}")


if __name__ == "__main__":
    main()
