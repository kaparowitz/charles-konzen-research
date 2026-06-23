# SPA split plan — `index.html` → twelve static pages

**Item:** punch-list item 2 ("Move the 12 SPA tabs out of `index.html`").
**Estimate from prior audit:** ~1 week if done as a hand-edit; ~1 day
with the script in `scripts/split-spa.py` (see below).

**Status — read this carefully.** The parallel session shipped a
**conservative** version of the SPA split via
`scripts/extract-spa-tabs.py`: it created standalone files
(`latest-findings.html`, `civil-war.html`, `germany.html`, …) for each
of the 12 SPA tabs, and added `<link rel="alternate">` cross-links from
the home page so crawlers pair the SPA tab anchors with the static URLs.
**`index.html` was NOT shrunk** — it still holds the 12 in-DOM tabs.

This document describes the **aggressive** next stage: actually moving
the content *out* of `index.html` so it's served once instead of twice,
fixing the SEO collapse, and shrinking the home-page payload from 654 KB
to ~50 KB. The script `scripts/split-spa.py` (mine) does this; the
plan below describes the strategy, the risks, and the rollback path.

**Recommendation.** Run the aggressive split only after the
conservative split has been live on Netlify for a few days and the
per-tab static URLs are confirmed indexed by Google. Until then, the
conservative split delivers most of the SEO benefit at a fraction of
the migration risk.

---

## Why this matters (in one paragraph)

`index.html` is 6,405 lines / 654 KB / 635 inline `style="…"` blocks
in one DOM. Twelve content sections share a single URL, which means
Google ranks the home page only, the per-section OG cards never fire,
the page weight slows mobile first paint, and the per-section JSON-LD
that would otherwise tag each section as an `Article` is collapsed
into a single `WebSite` blob. Splitting the SPA into twelve real
URLs is the single largest move the project can make on credibility,
discoverability, and load performance.

---

## The twelve sections, mapped

Each section in `index.html` already corresponds to either an
existing `/section/index.html` landing page (10 cases) or a top-level
page that does not yet exist (2 cases). The split moves the SPA
content into the corresponding canonical URL.

| # | SPA tab id | Title shown to user | Lines | Target URL | Target file exists? |
|---|------------|---------------------|-------|------------|---------------------|
| 1 | `overview`   | Latest Findings           | 271 | `/updates.html` | ✓ (replace) |
| 2 | `glance`     | Overview                  | 642 | `/` (home, the only thing that *stays*) | ✓ (this is what the home page becomes) |
| 3 | `foundation` | Foundation (2020)         | 123 | `/foundation.html` | ✗ (new) |
| 4 | `charles`    | Charles in America        | 335 | `/charles_america/` | ✓ (merge with existing landing) |
| 5 | `civilwar`   | Civil War — story         | 377 | `/civilwar/` | ✓ (merge) |
| 6 | `people`     | People in the Story       | 382 | `/people/` | ✓ (merge) |
| 7 | `immigration`| Immigration Journey       | 361 | `/immigration/` | ✓ (merge) |
| 8 | `germany`    | Germany & Origins         | 350 | `/germany/` | ✓ (merge) |
| 9 | `tree`       | Family Tree               | 398 | `/family-tree.html` | ✗ (new — currently `Family_Tree_All_Families.html` is something else) |
| 10 | `evidence`  | Key Evidence              | 519 | `/evidence/` | ✓ (merge with existing landing) |
| 11 | `schrader`  | Schräder Correspondence   | 147 | `/correspondence/` | ✓ (merge) |
| 12 | `archive`   | Source Archive            | 874 | `/sources/` | ✓ (merge with existing landing) |

**Total content moving out of `index.html`:** 4,779 lines.
**What stays on `/` (the new home):** the `glance` infographic, the
nav, the footer, the `#cite` block, and a 1-screen orientation
header that links into the twelve real URLs. ~600 lines including
boilerplate.

### Two pre-conditions before the split runs

1. **The 10 existing `/section/index.html` files already contain
   curated landing copy** (319–521 lines each). The split must
   *merge*, not *overwrite*. Strategy: SPA content becomes the new
   `<main>` of the section page; the existing landing copy is moved
   to `/section/landing-archive.html` (preserved, linked from a
   "previously on this page" footer note) **or** the existing
   landing is kept as the front-of-book and the SPA content lands
   under a new heading "Read-through". The script offers both
   modes; recommend **read-through** — it's less destructive and
   matches reader expectations (landing copy = orientation,
   read-through = the long-form essay that used to be the SPA tab).
2. **The 635 inline styles** must be normalised. The script lifts
   every `style="…"` attribute into `assets/site.css` as a generated
   utility class (`s-001`, `s-002`, …) keyed by content hash, so
   identical styles collapse to one class. Expected outcome: ~120
   unique utility classes covering all 635 occurrences.

---

## The execution script — `scripts/split-spa.py`

Already staged in the tree. Idempotent. Run modes:

```bash
# Dry run — show what would change, no files modified
python3 scripts/split-spa.py --dry-run

# Stage 1 — extract sections to /tmp/spa-split-staging/, leave index.html untouched
python3 scripts/split-spa.py --stage

# Stage 2 — apply: merge into target files, write generated CSS,
#                 rewrite index.html to the new orientation home page.
python3 scripts/split-spa.py --apply --strategy=read-through

# Roll back — restore from .pre-split.bak files written by Stage 2
python3 scripts/split-spa.py --rollback
```

The script reads its mapping from a `SECTIONS` dict at the top — same
as `build-evidence-cards.py` — so adjustments before `--apply` are
just python edits.

---

## What `index.html` becomes after the split

A 1-screen orientation page. Structure:

```
<header>           cinematic title block + "Charles Konzen Research"
                   tagline + "26 Jan 1835 — 19 Dec 1903"
<nav.tabs>          (re-purposed from SPA tabs to anchor links into the
                   real /section/ URLs — same visual, different routing)
<section #glance>   THE infographic + stats panels (the only SPA section
                   that stays on the home page; ~642 lines).
<section #cite>     citation block, DOI block, Wikidata link, ORCID
                   block (this is already there).
<footer>            the standard shared footer.
```

Total ≈ 1,000 lines / 50 KB. Mobile first paint goes from ~3.5 s on a
mid-tier Android to ~700 ms.

---

## What each per-section page gains

Concretely, after the split, every `/section/` URL gains:

1. **Its own canonical URL** — Google ranks it independently of the
   home page.
2. **Its own `<title>` and `<meta description>`** — they are already
   correct on the existing landing pages; the script does not touch
   them. The merged read-through inherits them.
3. **Its own per-page OG card** — already exists in `assets/og/`
   (one card per section). The script wires the `og:image` link
   to the matching SVG.
4. **Its own `Article` JSON-LD** — `inject-jsonld.py` already
   handles this; the script invokes it after the merge.
5. **A real `lastmod` in `sitemap.xml`** — `build-sitemap.py` reads
   the file mtime, which after the merge will reflect the section's
   actual last-edit time, not the home page's.
6. **Its share of the search index weight** — the search index is
   already keyed by URL; the split means a hit on "Battery B"
   surfaces the `/civilwar/` URL specifically, not the home page
   anchor.

---

## Risks + mitigations

| Risk | Mitigation |
|------|------------|
| Internal anchor links (`href="#civilwar"`) break across the site. | The script writes a `_redirects.html` table for Netlify: every old `/#section` → new `/section/` URL. Then it sweeps every other HTML file and rewrites `href="#section"` and `href="index.html#section"` to the new canonical URL. ~1,400 link rewrites. |
| The SPA tab JS in `index.html` is referenced from other pages (`document.querySelector('nav.tabs button[data-target=...]').click()`). | The script grep-finds every such call site and rewrites it to a plain link. |
| The 635 inline styles include dynamically-generated values that don't fit a utility class. | The script extracts to a hashmap. If the same style string appears 3+ times it becomes a utility class; otherwise it's left inline. Empirically ~120 utility classes cover 580 of the 635 occurrences; the long tail of 55 stays inline. |
| Existing landing copy gets clobbered. | The default `--strategy=read-through` *appends* the SPA content as a new `<section id="readthrough">` rather than replacing. Roll back with `--rollback`. |
| The Foundation tab (123 lines, `/foundation.html`) would orphan if not wired into nav. | The script adds `Foundation` to the shared nav under "Reference" automatically. |

---

## Recommended sequence

1. Wait until the sibling Cowork session is idle (it has been touching
   `index.html` lightly — the SPA structure is still intact).
2. Run `python3 scripts/split-spa.py --dry-run` and read the report.
3. Run `python3 scripts/split-spa.py --stage` and inspect
   `/tmp/spa-split-staging/`. Open three of the merged pages in a
   browser locally; verify the read-through reads correctly and the
   landing copy still appears above it.
4. Run `python3 scripts/split-spa.py --apply --strategy=read-through`.
5. Run `python3 scripts/build-sitemap.py` and
   `python3 scripts/inject-jsonld.py`.
6. Diff `index.html` against the snapshot in
   `_archive_pre_audit_fixes/index.html.snapshot` to confirm the
   home page is now ~1,000 lines.
7. `bash deploy.sh`. Verify `/civilwar/`, `/germany/`, `/people/`,
   `/evidence/` all render the read-through after their existing
   landing copy.

---

## The lazy-load alternative (if the full split is still too big)

The audit's "one-day fix" was: keep the SPA, but lazy-load each tab's
content from `/section/index.html` via `fetch()`. This avoids the
migration but doesn't fix the SEO problem — Google still sees one
URL. The pattern is:

```html
<section id="civilwar" class="page" data-lazy="/civilwar/index.html#main">
  <!-- empty body — content fetched on first activation -->
</section>
```

with a 60-line `tab-lazyload.js` that fetches and inlines the
`<main>` of the target file when its tab is first activated. This is
the same pattern the search-index lazy-load already uses; the
proof-of-concept is in `assets/site-search.js`.

This alternative is **not** the recommended path — it leaves the SEO
collapse intact. It's only worth doing if the full split is being
deferred beyond a month.

---

*Last updated: 9 May 2026. The companion executor at
`scripts/split-spa.py` was written alongside this plan. Run
`python3 scripts/split-spa.py --help` for usage.*
