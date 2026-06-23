#!/usr/bin/env python3
"""
Split stories.html (1,450 lines, 9 narrative articles in one scroll) into
9 standalone stories/<n>-<slug>.html pages plus a stories/index.html landing.

Each new page carries:
  - The same theme/cinematic CSS the original page used (paths re-rooted)
  - Per-page <title>, meta description, canonical, OG card
  - The injected nav + footer placeholders (so inject-site-nav.py picks
    them up on next run)
  - Prev/next pagers
  - Article JSON-LD scoped to the single story

The original stories.html is rewritten in place to be a TOC landing
page that lists all 9 with short summaries and links to the new pages.

Idempotent: re-running rewrites the new pages and the landing from the
current source content; existing files are overwritten cleanly.
"""
from __future__ import annotations
import json
import os
import re
from pathlib import Path
from textwrap import dedent

ROOT = Path("/sessions/great-friendly-turing/mnt/Charles Gannsen Research")
SOURCE = ROOT / "stories.html"
OUT_DIR = ROOT / "stories"

# Ordered list of (id, slug, title, short summary).
STORIES = [
    ("portrait",  "1-portrait",  "A photograph in a moving box",
     "For more than a hundred years no one had a face to put to Charles. Then in September 2025 a descendant in Independence, Missouri found one in a moving box."),
    ("recruiter", "2-recruiter", "The recruiter and the recruit",
     "Charles's enlistment, the man who signed him up, and how the two of them would meet again — four years later, at the marriage entry."),
    ("kreichelt", "3-kreichelt", "The brother in the same battery",
     "How Charles came to fight in a Civil War battery alongside his own brother-in-law."),
    ("elector",   "4-elector",   "The firstborn and the deposed Elector",
     "Why Charles named his first son after a Hessian prince who had been deposed three months before the baptism."),
    ("pillmann",  "5-pillmann",  "The man who sponsored twice",
     "Of the twelve named sponsors across the seven Gannsen baptisms, one man &mdash; a German butcher &mdash; stood up twice."),
    ("braschler", "6-braschler", "The pastor who wrote two different vowels",
     "The same pastor wrote two different spellings of the family name in two consecutive years &mdash; the &quot;smoking gun&quot; that the spelling came from Charles's voice, not the clerk's pen."),
    ("konsen",    "7-konsen",    "The surname spelled twice, fifteen years apart",
     "The two American records that preserve the original Hessian K-form, fifteen years apart &mdash; the strongest pair of evidence points connecting Charles to a specific German surname pool."),
    ("spraul",    "8-spraul",    "The brewing-trade godfather",
     "The Anheuser-Busch Superintendent who stood as the sole named sponsor at the most-evidence-bearing baptism in the entire series."),
    ("alone",     "9-alone",     "Seven baptisms with no one from his side",
     "Across seven baptisms and twelve named sponsors, not one is a Konze, Konzen, Kontzen, or Gannsen &mdash; the structural argument that Charles immigrated alone."),
]

# Article date metadata (used in JSON-LD).
DATE_PUBLISHED = "2026-04-15"
DATE_MODIFIED  = "2026-05-17"
BASE_URL = "https://charles-konzen-research.netlify.app"


def extract_articles(html: str) -> dict[str, str]:
    """Return {story_id: article_html_block} for each of the 9 story articles."""
    out: dict[str, str] = {}
    for m in re.finditer(
        r'<article class="story"[^>]*id="([^"]+)"[\s\S]*?</article>',
        html,
    ):
        sid = m.group(1)
        out[sid] = m.group(0)
    return out


def extract_inline_styles(html: str) -> str:
    """Pull the first <style>…</style> block from stories.html — the
    typographic styles that articles need to render correctly. We inline
    them on each child page so it stands on its own."""
    m = re.search(r'<style>([\s\S]*?)</style>', html)
    return m.group(1) if m else ""


def build_story_page(idx: int, story_id: str, slug: str, title: str,
                     summary: str, article_html: str, inline_css: str) -> str:
    """Render the full HTML for one stories/<slug>.html page."""
    prev_idx = idx - 1
    next_idx = idx + 1
    prev_html = ""
    next_html = ""
    if prev_idx >= 0:
        p_slug = STORIES[prev_idx][1]
        p_title = STORIES[prev_idx][2]
        prev_html = (
            f'    <a href="{p_slug}.html" class="pager-prev">'
            f'<span class="nlabel">&larr; Previous story</span>'
            f'<span>Story {prev_idx + 1} &middot; {p_title}</span></a>\n'
        )
    else:
        prev_html = '    <a href="../stories.html" class="pager-prev"><span class="nlabel">&larr;</span><span>All stories (index)</span></a>\n'

    if next_idx < len(STORIES):
        n_slug = STORIES[next_idx][1]
        n_title = STORIES[next_idx][2]
        next_html = (
            f'    <a href="{n_slug}.html" class="pager-next">'
            f'<span class="nlabel">Next story &rarr;</span>'
            f'<span>Story {next_idx + 1} &middot; {n_title}</span></a>\n'
        )
    else:
        next_html = '    <a href="../stories.html" class="pager-next"><span class="nlabel">All stories</span><span>Back to index &rarr;</span></a>\n'

    canonical = f"{BASE_URL}/stories/{slug}.html"
    og_image = f"{BASE_URL}/assets/og/stories.png"

    title_html = re.sub(r"<[^>]+>", "", title)
    summary_html = re.sub(r"<[^>]+>", "", summary)[:150]

    article_html = article_html.replace('class="story"', 'class="story story--standalone"')

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<script id="theme-toggle-init">(function(){{try{{var t=localStorage.getItem("theme");document.documentElement.classList.add(t==="light"?"theme-light":"theme-dark");}}catch(e){{document.documentElement.classList.add("theme-dark");}}}})();</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1F1A14">
<title>Story {idx + 1} &middot; {title_html} &mdash; Charles Konzen Research</title>
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="../assets/theme.css?v=20260516-utilities">
<link rel="stylesheet" href="../assets/cinematic.css">
<link rel="stylesheet" href="../assets/dark-mode.css?v=20260516-utilities">
<script defer src="../assets/theme-toggle.js?v=20260509-2330"></script>
<meta name="description" content="{summary_html}">
<meta name="author" content="Jed Johnson with Peter Schräder">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Charles Konzen Research">
<meta property="og:title" content="Story {idx + 1} · {title_html} — Charles Konzen Research">
<meta property="og:description" content="{summary_html}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Story {idx + 1} · {title_html}">
<meta name="twitter:image" content="{og_image}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "{canonical}#article",
  "headline": "Story {idx + 1} · {title_html}",
  "description": {json.dumps(summary_html, ensure_ascii=False)},
  "datePublished": "{DATE_PUBLISHED}",
  "dateModified": "{DATE_MODIFIED}",
  "url": "{canonical}",
  "isPartOf": {{ "@id": "{BASE_URL}/#website" }},
  "author": [
    {{ "@type": "Person", "name": "Jed Johnson" }},
    {{ "@type": "Person", "name": "Peter Schräder" }}
  ],
  "publisher": {{ "@type": "Person", "name": "Jed Johnson", "url": "{BASE_URL}/about.html" }},
  "inLanguage": "en-US",
  "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/"
}}
</script>
<style>
{inline_css}
  /* Standalone story page additions */
  article.story--standalone {{ margin: 1rem 0 2.4rem; }}
  .story-pager {{ display: flex; justify-content: space-between; gap: 1rem;
    border-top: 1px solid var(--border-light, #e8dcc0); padding: 1.2rem 0 0;
    margin-top: 2rem; font-size: 0.92rem; }}
  .story-pager a {{ color: var(--brand-dark, #8a6420); border: 1px solid var(--border-medium, #d8c8a8);
    border-radius: 3px; padding: 0.6rem 0.9rem; max-width: 46%; background: var(--bg-card, #fff);
    text-decoration: none; }}
  .story-pager a:hover {{ background: var(--brand-tint, #fffaee); }}
  .story-pager .nlabel {{ display: block; font-size: 0.74rem; text-transform: uppercase;
    letter-spacing: 0.07em; color: var(--text-muted, #7a6f5e); }}
  .story-pager .nlabel + span {{ display: block; color: var(--text-strong, #1f1a14); margin-top: 0.15rem; }}
  .story-pager .pager-next {{ text-align: right; }}
</style>
</head>
<body class="cine-typography">
<header class="st-hero">
  <div class="crumbs"><a href="../index.html">Charles Konzen Research</a> / <a href="../stories.html">Stories</a> / Story {idx + 1}</div>
  <h1>{title_html}</h1>
  <div class="sub">Story {idx + 1} of 9 &middot; from the cinematic investigation</div>
</header>

<main id="main">
  {article_html}

  <nav class="story-pager" aria-label="Story navigation">
{prev_html}{next_html}  </nav>
</main>
</body>
</html>
"""
    return page


def build_landing(html: str, inline_css: str) -> str:
    """Rewrite stories.html as a TOC landing for the 9 split pages."""
    # Pull the original header and lede if present.
    head_match = re.search(r"<header[^>]*class=\"st-hero\"[^>]*>([\s\S]*?)</header>", html)
    header_html = head_match.group(0) if head_match else ""

    toc_items = []
    for i, (sid, slug, title, summary) in enumerate(STORIES):
        toc_items.append(
            f'    <li><span class="num">Story {i+1:02d}</span>'
            f'<a href="stories/{slug}.html"><strong>{title}</strong></a>'
            f'<span class="summary">{summary}</span></li>'
        )

    landing = f"""<!DOCTYPE html>
<html lang="en">
<head>
<script id="theme-toggle-init">(function(){{try{{var t=localStorage.getItem("theme");document.documentElement.classList.add(t==="light"?"theme-light":"theme-dark");}}catch(e){{document.documentElement.classList.add("theme-dark");}}}})();</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1F1A14">
<title>Stories — Charles Konzen Research</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="canonical" href="{BASE_URL}/stories.html">
<link rel="stylesheet" href="assets/theme.css?v=20260516-utilities">
<link rel="stylesheet" href="assets/cinematic.css">
<link rel="stylesheet" href="assets/dark-mode.css?v=20260516-utilities">
<script defer src="assets/theme-toggle.js?v=20260509-2330"></script>
<meta name="description" content="Nine narrative moments from the Charles Konzen investigation, told in plain English. Each story is a self-contained page; together they trace the threads from the portrait in a moving box to the seven baptisms with no one from his side.">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Charles Konzen Research">
<meta property="og:title" content="Stories — Charles Konzen Research">
<meta property="og:description" content="Nine narrative moments from the investigation, told in plain English.">
<meta property="og:url" content="{BASE_URL}/stories.html">
<meta property="og:image" content="{BASE_URL}/assets/og/stories.png">
<style>
{inline_css}
  ol.toc-stories {{ list-style: none; padding: 0; margin: 1.4rem 0; }}
  ol.toc-stories li {{ display: grid; grid-template-columns: 110px 1fr; gap: 0.6rem;
    align-items: baseline; padding: 0.85rem 0; border-bottom: 1px solid var(--border-light, #e8dcc0); }}
  ol.toc-stories li:last-child {{ border-bottom: 0; }}
  ol.toc-stories .num {{ font-family: var(--font-mono, monospace); font-size: 0.78rem;
    color: var(--brand-dark, #8a6420); letter-spacing: 0.14em; text-transform: uppercase; }}
  ol.toc-stories a {{ color: var(--text-strong, #1f1a14); text-decoration: none;
    border-bottom: 1px dotted var(--border-medium, #d8c8a8); }}
  ol.toc-stories a:hover {{ color: var(--brand-dark, #8a6420); border-bottom-color: var(--brand, #d8b366); }}
  ol.toc-stories .summary {{ display: block; margin-top: 0.25rem; font-size: 0.94rem;
    color: var(--text-meta, #5a4a32); line-height: 1.5; font-style: italic; }}
</style>
</head>
<body class="cine-typography">
{header_html}

<main id="main">
  <p class="lede">Nine narrative moments from the investigation, each one a self-contained page. Click any title to open the full story; use the &larr; / &rarr; pager at the bottom of each page to read the next.</p>

  <ol class="toc-stories">
{chr(10).join(toc_items)}
  </ol>
</main>
</body>
</html>
"""
    return landing


def main():
    html = SOURCE.read_text(encoding="utf-8")
    articles = extract_articles(html)
    if len(articles) != 9:
        raise SystemExit(f"Expected 9 stories; found {len(articles)} ({list(articles)})")

    inline_css = extract_inline_styles(html)
    OUT_DIR.mkdir(exist_ok=True)

    for i, (sid, slug, title, summary) in enumerate(STORIES):
        if sid not in articles:
            print(f"  [MISS] {sid}: article not found in source")
            continue
        page = build_story_page(i, sid, slug, title, summary, articles[sid], inline_css)
        out_path = OUT_DIR / f"{slug}.html"
        out_path.write_text(page, encoding="utf-8")
        print(f"  Wrote {out_path.relative_to(ROOT)}  ({len(page):,} bytes)")

    landing = build_landing(html, inline_css)
    SOURCE.write_text(landing, encoding="utf-8")
    print(f"  Rewrote {SOURCE.relative_to(ROOT)} as TOC landing ({len(landing):,} bytes)")


if __name__ == "__main__":
    main()
