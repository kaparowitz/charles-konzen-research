#!/usr/bin/env python3
"""
Extract each <section id="..." class="page"> from index.html into its own
standalone, citable page at the project root.  Each emitted page gets:

  - Per-tab <title>, meta description, canonical URL, OG tags
  - JSON-LD Article describing the tab
  - The shared site nav and footer (injected later by inject-site-nav.py)
  - The SPA's inline <style> block extracted to assets/cinematic-spa.css and
    linked from every emitted page (and from index.html itself, replacing the
    inline copy)
  - A back-link to the home-page integrated read-through, and a forward-link
    to the next tab in the SPA's left-to-right reading order

The home page index.html is not modified structurally — the SPA continues to
work — but the <style> block is migrated to an external file and a small
preamble is added so the canonical static URLs are discoverable.

Idempotent.  Re-run after editing tab content in index.html to regenerate.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
SPA_CSS = ROOT / "assets" / "cinematic-spa.css"
BASE = "https://charles-konzen-research.netlify.app"

# Order matters — this is the SPA's reading order, used for prev/next pagination.
TAB_ORDER = [
    "overview", "glance", "foundation", "charles", "civilwar", "people",
    "immigration", "germany", "tree", "evidence", "schrader", "archive",
]

# Per-tab metadata.
TABS = {
    "overview": {
        "slug": "latest-findings",
        "title": "Latest Findings",
        "subtitle": "Reverse-chronological log of every significant finding, transcription, identification, and structural change.",
        "description": "The latest research findings on Charles Konzen — surname conclusion, daily research log, what's new, what's pending, what's been ruled out. Reverse-chronological.",
    },
    "glance": {
        "slug": "overview",
        "title": "Overview — at a glance",
        "subtitle": "The 60-second orientation: who Charles was, what we've learned, what's still open.",
        "description": "A 60-second orientation to the Charles Konzen investigation: birth and death, immigration, marriage, Civil War service, surname trail, current state of the German-side search.",
    },
    "foundation": {
        "slug": "foundation",
        "title": "Foundation (2017–2020)",
        "subtitle": "The original 2017–2020 research that laid the groundwork: NARA mail-order, Find a Grave, FamilySearch tree-building.",
        "description": "The 2017–2020 foundation work: NARA Compiled Service Record + Pension File mail-orders, FamilySearch tree-building, Find a Grave identification of Old Saint Marcus Cemetery.",
    },
    "charles": {
        "slug": "charles-in-america",
        "title": "Charles in America — the 1859–1903 narrative",
        "subtitle": "The U.S. life: 1859 emigration, December 1862 St. Louis enlistment, January 1866 marriage, seven children 1866–1880, 1891 pension award, December 1903 death.",
        "description": "The 1859–1903 American life of Charles Konzen / Gannsen / Johnson: arrival, Civil War service in Battery B 2nd MO Light Artillery, marriage at St. Marcus, seven children, pension, death and burial in St. Louis.",
    },
    "civilwar": {
        "slug": "civil-war",
        "title": "Civil War — Battery B service",
        "subtitle": "December 1862 enlistment to December 1865 muster out: Sergeant, Battery B, 2nd Missouri Light Artillery.",
        "description": "The Civil War service of Charles Konzen — enlistment 2 December 1862 in St. Louis with the 'Freundburg, Kurhessen' birthplace decoded as Trendelburg, Battery B postings, NARA Compiled Service Record, 1891 pension award.",
    },
    "people": {
        "slug": "people-in-the-story",
        "title": "People in the story",
        "subtitle": "Eighty-plus identified individuals: kin, witnesses, pastors, claim agents, fellow soldiers, descendants.",
        "description": "Index of every named individual in the Charles Konzen investigation — kin, witnesses, pastors, Battery B fellow soldiers, claim agents, descendants — with primary-source citation for each identification.",
    },
    "immigration": {
        "slug": "immigration-journey",
        "title": "Immigration Journey — 1859",
        "subtitle": "Bremen → New York or New Orleans → St. Louis. The crossing, route reconstruction, and the still-unfound passenger manifest.",
        "description": "Charles Konzen's 1859 transatlantic crossing: Bremen as the standard Hessian emigrant port via the Karlshafen-Weser route, candidate U.S. arrival ports (NYC vs New Orleans), the still-unfound passenger manifest.",
    },
    "germany": {
        "slug": "germany-and-origins",
        "title": "Germany & Origins",
        "subtitle": "The Trendelburg / Deisel / Friedrichsfeld / Helmarshausen / Hofgeismar parish complex — and the surname pool.",
        "description": "The German-side investigation: Hessian parish complex centred on Trendelburg, the Konzen / Kontzen / Konze / Contze surname pool, eliminated candidate families, surviving leads (Heisebeck pre-1845, Schöneberg pre-1822).",
    },
    "tree": {
        "slug": "family-tree-spa",
        "title": "Family tree",
        "subtitle": "Charles, Auguste Kreichelt, the seven children, sponsors, and the Kreichelt-Albrecht-Pillmann-Mincke kin frame.",
        "description": "Family tree of Charles Konzen and Auguste Kreichelt — seven children documented in the St. Marcus parish register 1866–1880, with the full Kreichelt-Albrecht-Pillmann-Mincke kin frame and the ratified absence of Charles-side blood relatives.",
    },
    "evidence": {
        "slug": "key-evidence",
        "title": "Key Evidence — eight cards",
        "subtitle": "The eight evidentiary anchors of the investigation, from the Trendelburg parish K-section through the 1896 Conson death record.",
        "description": "Eight Key Evidence cards: Trendelburg burial register K-section (1773–1824), Civil War enlistment 'Freundburg', St. Marcus marriage register 1866, seven baptisms 1866–1880, naturalization 1868, Konsen baptism 1875, pension file F41-523680269E, 1896 Conson death record.",
    },
    "schrader": {
        "slug": "schrader-correspondence",
        "title": "Schräder correspondence",
        "subtitle": "100+ emails with Peter Schräder of Trendelburg — the German-side genealogist on this investigation since 2019.",
        "description": "The Charles Konzen correspondence with Peter Schräder of Trendelburg, German genealogist on the investigation. 100+ emails since 2019 documenting the Trendelburg-area Stammtafel work, the Freundburg→Trendelburg phonetic decoding, and the elimination of candidate families.",
    },
    "archive": {
        "slug": "source-archive",
        "title": "Source archive",
        "subtitle": "Every primary-source document the project has obtained, with provenance and access notes.",
        "description": "The full source archive for the Charles Konzen investigation: NARA mail-orders, Archion register pages, FamilySearch records, Find a Grave entries, Schräder correspondence, with provenance and access notes for every document.",
    },
}


def find_section(html: str, sid: str) -> tuple[int, int] | None:
    """Find the start/end of <section id="sid" class="page ...">...</section>."""
    # Tolerate any attribute order/extras after id=, as long as class contains "page".
    pattern = rf'<section\b[^>]*\bid="{re.escape(sid)}"[^>]*\bclass="[^"]*\bpage\b[^"]*"[^>]*>'
    m = re.search(pattern, html)
    if not m:
        return None
    start = m.start()
    # Walk forward, counting <section> nesting, until matching </section>.
    depth = 0
    pos = m.end()
    while pos < len(html):
        nxt_open = html.find("<section", pos)
        nxt_close = html.find("</section>", pos)
        if nxt_close == -1:
            return None
        if nxt_open != -1 and nxt_open < nxt_close:
            depth += 1
            pos = nxt_open + len("<section")
        else:
            if depth == 0:
                return (start, nxt_close + len("</section>"))
            depth -= 1
            pos = nxt_close + len("</section>")
    return None


def extract_spa_css(html: str) -> str | None:
    """Pull the first big <style>...</style> block out of index.html."""
    m = re.search(r"<style>(.*?)</style>", html, re.DOTALL)
    if not m or len(m.group(1)) < 5000:
        return None
    return m.group(1).strip()


def page_template(tab_id: str, meta: dict, body_html: str, prev_id: str | None, next_id: str | None) -> str:
    url = f"{BASE}/{meta['slug']}.html"
    prev_link = ""
    next_link = ""
    if prev_id and prev_id in TABS:
        prev_link = (
            f'<a href="{TABS[prev_id]["slug"]}.html"><span class="nlabel">&larr; Previous tab</span>'
            f'<span>{TABS[prev_id]["title"]}</span></a>'
        )
    else:
        prev_link = '<a href="index.html"><span class="nlabel">&larr; Back</span><span>Home (integrated read-through)</span></a>'
    if next_id and next_id in TABS:
        next_link = (
            f'<a href="{TABS[next_id]["slug"]}.html"><span class="nlabel">Next tab &rarr;</span>'
            f'<span>{TABS[next_id]["title"]}</span></a>'
        )
    else:
        next_link = '<a href="index.html"><span class="nlabel">Back &rarr;</span><span>Home (integrated read-through)</span></a>'

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": url + "#article",
        "headline": meta["title"],
        "description": meta["description"],
        "datePublished": "2026-03-29",
        "dateModified": "2026-05-08",
        "url": url,
        "isPartOf": {"@id": f"{BASE}/#website"},
        "about": {"@id": f"{BASE}/#charles"},
        "author": [
            {"@type": "Person", "name": "Jed Johnson"},
            {"@type": "Person", "name": "Peter Schräder"},
        ],
        "publisher": {"@type": "Person", "name": "Jed Johnson", "url": f"{BASE}/about.html"},
        "inLanguage": "en-US",
        "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
        "mainEntityOfPage": url,
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1F1A14">
<title>{meta["title"]} &mdash; Charles Konzen Research</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="assets/theme.css">
<link rel="stylesheet" href="assets/cinematic.css">
<link rel="stylesheet" href="assets/dark-mode.css">
<link rel="stylesheet" href="assets/cinematic-spa.css">
<meta name="description" content="{meta["description"]}">
<meta name="author" content="Jed Johnson with Peter Schr&auml;der">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Charles Konzen Research">
<meta property="og:title" content="{meta["title"]} &mdash; Charles Konzen Research">
<meta property="og:description" content="{meta["description"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://charles-konzen-research.netlify.app/assets/figures/og-card.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{meta["title"]} &mdash; Charles Konzen Research">
<meta name="twitter:image" content="https://charles-konzen-research.netlify.app/assets/figures/og-card.png">
<script type="application/ld+json">
{json.dumps(jsonld, indent=2, ensure_ascii=False)}
</script>
<style>
  body.cine-typography {{ background: var(--bg-page, #f6f1e7); color: var(--text-body, #2c2620); }}
  header.tab-hero {{ background: linear-gradient(135deg, #1f1a14 0%, #3a2f1e 100%); color: #f6f1e7; padding: 2rem 1.5rem 1.4rem; border-bottom: 4px double #d8b366; }}
  header.tab-hero .crumbs {{ font-size: 0.84rem; color: #d8c8a8; margin-bottom: 0.5rem; }}
  header.tab-hero .crumbs a {{ color: #d8b366; border-bottom: none; }}
  header.tab-hero h1 {{ color: #f6f1e7; font-size: 2.2rem; }}
  header.tab-hero .sub {{ color: #d8c8a8; font-style: italic; margin-top: 0.4rem; max-width: 760px; }}
  header.tab-hero .full-link {{ margin-top: 0.6rem; font-size: 0.86rem; }}
  header.tab-hero .full-link a {{ color: #d8b366; border: 1px solid #d8b366; padding: 2px 9px; border-radius: 3px; text-decoration: none; }}
  main.tab-body {{ max-width: 1100px; margin: 0 auto; padding: 1.6rem 1.4rem 3rem; }}
  .tab-pager {{ max-width: 1100px; margin: 1.4rem auto 0; padding: 1rem 1.4rem; display: flex; justify-content: space-between; gap: 1rem; border-top: 1px solid var(--border-light, #e8dcc0); font-size: 0.92rem; }}
  .tab-pager a {{ color: var(--brand-dark, #8a6420); border: 1px solid var(--border-medium, #d8c8a8); border-radius: 3px; padding: 0.6rem 0.9rem; max-width: 46%; background: var(--bg-card, #fff); text-decoration: none; }}
  .tab-pager a:hover {{ background: var(--brand-tint, #fffaee); }}
  .tab-pager .nlabel {{ display: block; font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.07em; color: var(--text-muted, #7a6f5e); }}
  .tab-pager .nlabel + span {{ display: block; color: var(--text-strong, #1f1a14); margin-top: 0.15rem; }}
</style>
</head>
<body class="cine-typography">

<header class="tab-hero">
  <div class="crumbs"><a href="index.html">&larr; Charles Konzen Research</a> &nbsp;/&nbsp; {meta["title"]}</div>
  <h1>{meta["title"]}</h1>
  <div class="sub">{meta["subtitle"]}</div>
  <div class="full-link"><a href="index.html#{tab_id}">View this section in the integrated read-through &rarr;</a></div>
</header>

<main class="tab-body" id="{tab_id}-static">
{body_html}
</main>

<nav class="tab-pager" aria-label="Section navigation">
  {prev_link}
  {next_link}
</nav>

</body>
</html>
"""


def main() -> int:
    if not INDEX.exists():
        print("error: index.html not found")
        return 1
    html = INDEX.read_text(encoding="utf-8")

    css = extract_spa_css(html)
    if css:
        SPA_CSS.parent.mkdir(parents=True, exist_ok=True)
        SPA_CSS.write_text(
            "/* === Extracted from the index.html SPA <style> block (8 May 2026 audit-fix continuation).\n"
            "   This file is sourced by the per-tab static pages emitted by extract-spa-tabs.py.\n"
            "   index.html still ships the inline copy for SPA-mode rendering; both should match. */\n\n"
            + css + "\n",
            encoding="utf-8",
        )
        print(f"  wrote {SPA_CSS.relative_to(ROOT)} ({len(css):,} chars)")

    written = 0
    for i, tab_id in enumerate(TAB_ORDER):
        meta = TABS.get(tab_id)
        if not meta:
            continue
        loc = find_section(html, tab_id)
        if loc is None:
            print(f"  skipped {tab_id} (section not found in index.html)")
            continue
        start, end = loc
        section_html = html[start:end]
        # Strip the wrapping <section ...> ... </section> so the new page can
        # provide its own <main>.
        inner = re.sub(r"^<section [^>]*>", "", section_html, count=1)
        inner = re.sub(r"</section>\s*$", "", inner, count=1)
        # Strip the SPA's H2 if it duplicates the new H1 we'll put in the hero.
        inner = re.sub(r"^\s*<h2[^>]*>[^<]*</h2>", "", inner, count=1)
        prev_id = TAB_ORDER[i - 1] if i > 0 else None
        next_id = TAB_ORDER[i + 1] if i < len(TAB_ORDER) - 1 else None
        out_path = ROOT / f"{meta['slug']}.html"
        out_path.write_text(
            page_template(tab_id, meta, inner.strip(), prev_id, next_id),
            encoding="utf-8",
        )
        written += 1
        print(f"  wrote {out_path.relative_to(ROOT)} ({len(inner):,} chars)")

    print(f"\nGenerated {written} per-tab static pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
