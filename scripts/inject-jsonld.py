#!/usr/bin/env python3
"""
Inject per-page JSON-LD into key standalone pages.

Idempotent — wraps the injected block in BEGIN/END markers so re-runs replace it.
"""
from __future__ import annotations
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://charles-konzen-research.netlify.app"

BEGIN = "<!-- BEGIN-INJECTED-JSONLD -->"
END = "<!-- END-INJECTED-JSONLD -->"

# ----- Article-style pages -----
ARTICLE_PAGES = {
    "abstract.html": {
        "headline": "Charles Konzen Research — Abstract",
        "description": "Formal one-page abstract of the Charles Konzen genealogical investigation: question, method, evidence, working conclusion, and gaps.",
        "datePublished": "2026-03-29",
    },
    "methodology.html": {
        "headline": "Methodology — Charles Konzen Research",
        "description": "Research standards, source-rating taxonomy, transcription conventions, citation style, and known limitations.",
        "datePublished": "2026-03-29",
    },
    "faq.html": {
        "headline": "FAQ — Charles Konzen Research",
        "description": "Frequently asked questions about Charles Konzen, the surname trail, the family, and the project.",
        "datePublished": "2026-04-15",
    },
    "glossary.html": {
        "headline": "Glossary — Charles Konzen Research",
        "description": "German genealogical terminology used throughout the Charles Konzen investigation.",
        "datePublished": "2026-04-01",
    },
    "bibliography.html": {
        "headline": "Bibliography — Charles Konzen Research",
        "description": "Every primary source, archive, and reference work cited across the investigation.",
        "datePublished": "2026-04-01",
    },
    "open-questions.html": {
        "headline": "Open Questions — Charles Konzen Research",
        "description": "What the investigation has not yet resolved, with the conditions under which each gap would close.",
        "datePublished": "2026-04-01",
    },
    "visualize.html": {
        "headline": "Visualize — Charles Konzen Research",
        "description": "The four signature diagrams: timeline, surname trail, candidate funnel, parish map.",
        "datePublished": "2026-04-15",
    },
    "changelog.html": {
        "headline": "Changelog — Charles Konzen Research",
        "description": "Chronological log of substantive updates to the Charles Konzen investigation.",
        "datePublished": "2026-03-29",
    },
    "stories.html": {
        "headline": "Stories — Charles Konzen Research",
        "description": "Nine narrative moments from the Charles Konzen investigation.",
        "datePublished": "2026-04-15",
    },
    "cast.html": {
        "headline": "Cast — Charles Konzen Research",
        "description": "The people in the stories — a unified index of the named individuals across the investigation.",
        "datePublished": "2026-04-15",
    },
    "contribute.html": {
        "headline": "Contribute or correct — Charles Konzen Research",
        "description": "How descendants, researchers, and archivists can contribute to the investigation.",
        "datePublished": "2026-05-08",
    },
    "about.html": {
        "headline": "About — Charles Konzen Research",
        "description": "Project authors, declared interests, citation guidance, and licence.",
        "datePublished": "2026-05-08",
    },
    # Germany subpages (added 12 May 2026 to close the audit gap)
    "germany/index.html": {
        "headline": "Germany & Origins — Charles Konzen Research",
        "description": "The German-side investigation: Hessian parish complex around Trendelburg, the Konzen / Kontzen / Konze surname pool, eliminated candidates, surviving open questions.",
        "datePublished": "2026-04-01",
    },
    "germany/contextual-reading.html": {
        "headline": "Contextual reading on Hesse-Kassel — Charles Konzen Research",
        "description": "Background reading on Churhessen, the 1850s emigration wave, and the parish-register landscape relevant to the Charles Konzen investigation.",
        "datePublished": "2026-04-01",
    },
    "germany/hesse-kassel-context.html": {
        "headline": "Hesse-Kassel political and demographic context — Charles Konzen Research",
        "description": "Political history of Hesse-Kassel (Churhessen) and demographic conditions in the 1830s–1850s that shaped Konzen-family emigration.",
        "datePublished": "2026-04-01",
    },
    "germany/konzen-puzzle.html": {
        "headline": "The Konsen / Konzen / Kontzen surname puzzle — Charles Konzen Research",
        "description": "The seven attested American renderings of Charles's surname and how they triangulate to Konzen in the Trendelburg parish complex.",
        "datePublished": "2026-04-15",
    },
    "germany/parish-map.html": {
        "headline": "Parish map — searched vs unsearched — Charles Konzen Research",
        "description": "Map of the Trendelburg / Friedrichsfeld / Helmarshausen / Hofgeismar parish complex with search status by parish.",
        "datePublished": "2026-04-15",
    },
    "germany/political-history.html": {
        "headline": "Political history of Churhessen — Charles Konzen Research",
        "description": "Political timeline of Hesse-Kassel from the early 19th century through the 1866 Prussian annexation, with bearings on emigration motives.",
        "datePublished": "2026-04-15",
    },
    "germany/visit-today.html": {
        "headline": "Visiting the Hessian parishes today — Charles Konzen Research",
        "description": "Practical notes for descendants visiting Trendelburg, Deisel, Friedrichsfeld, and Helmarshausen — archives, churches, and cemeteries.",
        "datePublished": "2026-04-15",
    },
    # Immigration subpages
    "immigration/index.html": {
        "headline": "Immigration Journey — Charles Konzen Research",
        "description": "The 1859 transatlantic crossing: Bremen embarkation candidates, U.S. arrival port hypotheses, name variants in passenger manifests.",
        "datePublished": "2026-04-01",
    },
    "immigration/adjacent-emigrations.html": {
        "headline": "Adjacent Konze-family emigrations — Charles Konzen Research",
        "description": "Other Konze / Kontze / Konzen-surname emigrants from the same parish complex in the same window, and what they imply for Charles's path.",
        "datePublished": "2026-04-15",
    },
    "immigration/bremen-reconstruction.html": {
        "headline": "Bremen passenger-list reconstruction — Charles Konzen Research",
        "description": "Roll-by-roll reconstruction of Bremen → New Orleans / New York sailings 1858–1862 looking for Charles's 1859 crossing.",
        "datePublished": "2026-04-15",
    },
    "immigration/session-notes.html": {
        "headline": "Immigration research-session notes — Charles Konzen Research",
        "description": "Working log of immigration-side research sessions: what was searched, what was found, what was ruled out.",
        "datePublished": "2026-04-15",
    },
    "immigration/sources-and-name-variants.html": {
        "headline": "Sources and name variants — Charles Konzen Research",
        "description": "The passenger-list sources searched and the full set of name variants used against each index.",
        "datePublished": "2026-04-15",
    },
}


def page_url(rel: str) -> str:
    if rel == "index.html":
        return f"{BASE}/"
    if rel.endswith("/index.html"):
        return f"{BASE}/{rel[:-10]}"
    return f"{BASE}/{rel}"


def article_jsonld(rel: str, meta: dict) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": page_url(rel) + "#article",
        "headline": meta["headline"],
        "description": meta["description"],
        "datePublished": meta["datePublished"],
        "dateModified": "2026-05-12",
        "url": page_url(rel),
        "isPartOf": {"@id": f"{BASE}/#website"},
        "author": [
            {"@type": "Person", "name": "Jed Johnson"},
            {"@type": "Person", "name": "Peter Schräder"},
        ],
        "publisher": {
            "@type": "Person",
            "name": "Jed Johnson",
            "url": f"{BASE}/about.html",
        },
        "inLanguage": "en-US",
        "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


# ----- Per-person pages -----
def person_jsonld_for(path: Path) -> str | None:
    """Build minimal Person JSON-LD from <title> + meta description if present."""
    rel = path.relative_to(ROOT).as_posix()
    if not rel.startswith("people/") or rel == "people/index.html":
        return None
    try:
        c = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        c = path.read_text(encoding="latin-1")
    title_m = re.search(r"<title>([^<]+)</title>", c)
    desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', c)
    if not title_m:
        return None
    title = title_m.group(1).strip()
    # title is like "Auguste Kreichelt (1840–1896) — Charles Konzen Research"
    name_m = re.match(r"^(.*?)\s*[—|]\s*Charles Konzen", title)
    name = name_m.group(1).strip() if name_m else title
    desc = desc_m.group(1).strip() if desc_m else None
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": page_url(rel) + "#person",
        "name": re.sub(r"\s*\([^)]*\)\s*$", "", name),
        "url": page_url(rel),
        "isPartOf": {"@id": f"{BASE}/#website"},
    }
    if desc:
        data["description"] = desc
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2, ensure_ascii=False)}\n</script>'


def inject(content: str, jsonld_str: str) -> str:
    block = BEGIN + "\n" + jsonld_str + "\n" + END
    if BEGIN in content:
        return re.sub(
            re.escape(BEGIN) + r".*?" + re.escape(END),
            block.replace("\\", "\\\\"),
            content,
            count=1,
            flags=re.DOTALL,
        )
    if "</head>" not in content:
        return content
    return content.replace("</head>", block + "\n</head>", 1)


def already_has_jsonld(content: str) -> bool:
    return 'application/ld+json' in content


def main() -> int:
    updated = 0
    skipped_existing = 0

    # Article pages
    for rel, meta in ARTICLE_PAGES.items():
        path = ROOT / rel
        if not path.exists():
            continue
        try:
            c = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            c = path.read_text(encoding="latin-1")
        # If page already has its own JSON-LD AND no marker, skip to avoid clashing.
        if already_has_jsonld(c) and BEGIN not in c:
            skipped_existing += 1
            continue
        jsonld = article_jsonld(rel, meta)
        new = inject(c, jsonld)
        if new != c:
            path.write_text(new, encoding="utf-8")
            updated += 1

    # Person pages
    person_done = 0
    person_skipped = 0
    for path in (ROOT / "people").glob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if rel == "people/index.html":
            continue
        try:
            c = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            c = path.read_text(encoding="latin-1")
        if already_has_jsonld(c) and BEGIN not in c:
            person_skipped += 1
            continue
        jsonld = person_jsonld_for(path)
        if not jsonld:
            continue
        new = inject(c, jsonld)
        if new != c:
            path.write_text(new, encoding="utf-8")
            person_done += 1

    print(f"Article pages updated: {updated}")
    print(f"Article pages skipped (already had JSON-LD): {skipped_existing}")
    print(f"Person pages updated : {person_done}")
    print(f"Person pages skipped (already had JSON-LD): {person_skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
