# Audit-fix handoff — Charles Konzen Research

**Date:** 8 May 2026 (initial pass + evening world-class pass) · **updated 17 May 2026** (genealogy-rigor audit follow-up) · **updated 27–29 May 2026** (five-round content-debt + maintenance-hardening pass)
**Pass:** Stage 1–4 of the audit recommendations from
`Charles_Konzen_Site_Audit_May8_2026.docx`, the world-class
additions from the evening continuation pass, the 17 May rigor follow-up,
and the 27–29 May five-round programme documented below.

## 27–29 May 2026 — five-round content-debt + maintenance-hardening pass

A new pair of punch lists (Round 1 + Round 2) plus three follow-up rounds (R3 loose-ends, R4 durability/scope-extension, R5 completeness sweeps). 45 individual fixes landed across 4 days. Full punch lists at `Site_Punch_List_May27_2026.md` and `Site_Punch_List_Round2_May27_2026.md`.

### Headline outcomes

| Theme | What |
|---|---|
| **Propagation-cascade bug class** | Five surviving 7-attestation / 7-rendering instances closed (`overview.html`, `faq.html`, `evidence-index.html`, `germany/index.html`, `germany/konzen-puzzle.html`, `who/index.html`, `children/index.html`, `children/katherine-carolina.html`, `latest-findings.html`, `sponsor-reconciliation.html`); Freundberg → Freundburg propagation completed on `germany-and-origins.html` and `index.html` (35-file canon now consistent); session-count reconciled at 78+ across `methodology.html`, `negative-results.html`, `sponsor-reconciliation.html`. |
| **Audit-trail loop closure** | Errata back-links from live claims now exist for: surname conclusion, Bertha 1880, height 5'5", Card 4/5 recalibration, Konsen→Konzen 1890, Heitzenberger→Hitzelberger, Doc A/N death-date discrepancy, Entry 195 retraction. New formal errata entry `er-2026-05-03-heitzenberger-surname-family` closes the previously dangling reference. |
| **Narrative ↔ scaffolding binding** | ~24 inline cites added Round 2 (germany-and-origins, charles-in-america, civil-war, key-evidence) plus 13 more Round 2-8 (methodology, abstract, overview). Methodology→Doc A–O crosswalk binding closed (was 0, now 3). |
| **Claims dashboard (new page)** | `claims-dashboard.html` — 15 load-bearing claims on one screen, confidence pill + primary source + falsification condition per row, responsive table/card layout, wired into nav + footer across all 188 standalone pages, indexed in sitemap + search-index. |
| **Andreas Konze disentanglement (new section)** | `germany-and-origins.html#andreas-disentanglement` — teaching block walking the reader through the five (probably six) distinct men named Andreas Kon(t)ze in the Trendelburg/Deisel records 1718–1830; cross-linked from `germany/konzen-puzzle.html` with a reader's note above the candidate-tree SVG. |
| **Death-date discrepancy** | New `id="doc-crosswalk"` anchor on `source-archive.html`; dagger `†` footnotes on 7 most-visible "16 December 1903" prose instances linking to the Doc A–O crosswalk and the corresponding errata entry. |
| **Dual-audience routing** | "This page is for the family-reader path / researcher path" preambles added to `stories.html` and `key-evidence.html`. Konzen Puzzle landing now opens with a plain-language Working-conclusion paragraph before the connoisseur "At a Glance" card. |
| **People pages (Cohort A, 27 pages)** | One register kept per page: 10 family-intro kept (bottom-line wrapped in `<details>` "Researcher view"); 17 bottom-line kept (family-intro reduced to one-sentence italic preamble). Why-Charles over-claims tightened on 15 pages across the five rounds. |
| **Sponsor 15/17 reconciliation** | Plain-language explainer added on `sponsor-reconciliation.html` and `people-in-the-story.html` naming the two recurring sponsors (Georg Kreichelt and Friedrich Pillmann). |
| **Children's lifespan caption** | Rewritten on `children/index.html` to surface the three young deaths explicitly (16-month Friedrich Wilhelm; Maria Josephine 22 and Auguste 18 both in 1890) and conservatively note that specific causes of death are not recorded on the project's surfaced records. Auguste's age corrected 17 → 18. |
| **Glossary auto-linking** | First-occurrence glossary anchors added across 9 pages: `germany-and-origins`, `charles-in-america`, `civil-war`, `key-evidence`, `abstract`, `overview`, `methodology`, `evidence-index`, plus subpage spot-coverage. |
| **Foundation 2020 reframing** | REFINED / RULED OUT / NEW SINCE 2020 cards rewritten as explicit "2020 said X — we now know Y because Z" pairs on `foundation.html`. |
| **Skip-link target** | `<a id="main">` injected on 280 pages so the shared nav's skip-to-main works site-wide; persisted in `scripts/inject-site-nav.py` (`body_inject_skip_anchor()`) so future builds don't regress it. |
| **SPA-tab pseudo-anchor fix** | 34 bare `href="#X"` → `href="../index.html#X"` rewrites across 14 standalone pages (overview, key-evidence, charles-in-america, civil-war, foundation, latest-findings, source-archive, immigration-journey, family-tree-spa, people-in-the-story, etc.) so SPA-tab handlers route correctly when JS is unavailable. |
| **Site-wide broken-link sweep** | Audited 297 pages, found and fixed 30 real bugs: `konsen-puzzle.html` → `konzen-puzzle.html` (file rename), `#evidence-card-1` → `#card1` (anchor mismatch), `stories.html#X` → `stories/N-X.html` (per-story files), 10 family-page back-links to missing `#fam-X` anchors → redirected to `germany-and-origins.html`, plus 7 singletons. Final: 0 broken internal links across all 297 pages. |
| **OG image coverage** | Patched 125 pages that were missing `og:image` (people/, family_pages/, civilwar/, sources/, towns/, children/, research_logs/, etc.); 8 evidence-card pages switched from relative SVG to absolute PNG. Per-page `og:image:width` / `og:image:height` / `twitter:image` added. |
| **Search index rebuilt** | `search-index.json` regenerated from 186 entries (was 101, last hand-curated May 18). New build script `scripts/build_search_index.py` makes this repeatable on every deploy. Claims dashboard, all Reference-tab pages, and the new Round-2/3 errata + narrative sections are now searchable. |

### New maintenance harness

Three new scripts now gate every deploy via `deploy.sh`:

- **`scripts/check_canon.sh`** — pre-commit grep for the propagation-cascade bug class (surname counts, Freundberg, session counts, bare Hitzelberger). Fail-class hits abort deploy; warn-class hits report but don't block.
- **`scripts/check_links.py`** — internal-link audit. Catches missing files, missing cross-page anchors, missing in-page anchors. Exit ≠ 0 aborts deploy.
- **`scripts/build_search_index.py`** — regenerates `search-index.json` from all standalone pages. Idempotent; supports `--check` mode for CI dry-runs.

Wiring is in `deploy.sh`'s `sanity_checks` (gates) and `build_artifacts` (regeneration). Both `--dry-run` and full deploys show all gates passing.

### Final canonical values (29 May 2026)

| Claim | Canon |
|---|---|
| Surname count | 8 distinct American spellings, 8 attestations, 5 scribes, 30 years |
| Freundberg / Freundburg | **Freundburg** (with -burg) — matches Trendelburg phonetic decoding |
| Session count | 78+ research sessions |
| Heitzenberger / Hitzelberger | Clerk reading "Heitzenberger" / surname-family identified as Hitzelberger / specific individual identity remains open |
| Charles's death | 16 December 1903 per parish burial register (Doc N) · 17 December per death certificate (Doc A) — 1-day discrepancy flagged via † footnotes |
| Children's-baptism subset | 5 distinct baptism-register renderings (the subset of the 8-attestation site-wide trail) |

### Open follow-ups (deliberately not done in this pass)

- UX / navigation / mobile information-architecture review (7 dropdowns wide; index.html SPA at 754KB)
- SEO / performance / accessibility full audit beyond OG images and the spot-check
- Zenodo DOI minting (placeholders exist in `.zenodo.json` and `IDENTIFIERS_KIT.md`)
- Topical OG cards for `family_pages/`, `research_logs/`, `themes/` (currently share project default)
- `summary` vs `summary_large_image` Twitter card normalization site-wide



## 17 May 2026 — genealogy-rigor audit follow-up

Triggered by an external genealogy-rigor evaluation; full details in `SITE_HEALTH_May17_2026.md` and the new errata entries.

| What | Where |
|------|-------|
| Sponsor reconciliation table (17 slots × 15 sponsors × 0 Charles-side) | `sponsor-reconciliation.html` — new page |
| Negative-results audit (10 parishes + 13 candidate families + U.S./emigration searches) | `negative-results.html` — new page |
| Methodology §3: evidence-grade chip convention (★ Orig·firsthand / Orig·secondhand / Derivative / Compiled) | `methodology.html` |
| Methodology §5: per-quote transcription-hand provenance (Peter / author / HTR) | `methodology.html` |
| Working chips on the surname-conclusion sentence | `abstract.html`, `germany-and-origins.html`, `index.html` mirror |
| Conflict-resolution block on Key Evidence Card 8 (1862 age 23 vs canonical 1835) | `key-evidence.html` |
| Confidence snapshots on narrative tabs | `civil-war.html`, `charles-in-america.html`, `immigration-journey.html` |
| Doc A–O crosswalk table | `source-archive.html` |
| 7 errata entries for today's P0 fixes | `errata.html` |
| Nav + sitemap propagation | `assets/site-nav.html` (re-injected to 175 pages), `sitemap.xml` rebuilt to 174 entries |

## 17 May 2026 — late-evening user-catch cascade

Three substantive reframes triggered by user review of specific claims; full detail in `SITE_HEALTH_May17_2026.md` ("late evening" section) and three new errata entries.

| Catch | Where | Effect |
|---|---|---|
| "L. Carl Konsen" presented as attested birth name | `index.html`, `charles-in-america.html` (×3 instances each) | Reframed as "Birth name (reconstructed) ★ Working" with three-source footnote; chips show what's actually on each record |
| Hesse-records chip set undercount + included Konsen (which isn't Hesse-attested) | `index.html`, `charles-in-america.html`, `germany/konzen-puzzle.html` | Chips now show 5 Hesse-attested forms (Konze · Kontze · Kontzen · Contze · Konzen) plus parish cross-reference; explicit "Konsen is not in this cluster" callout |
| 1890 daughter's death record reads Konzen (with z), not Konsen | 13-file bulk swap + narrative reframes on abstract, methodology, FAQ, Key Evidence, Konsen Puzzle, children/auguste, etc. | U.S.-spelling canon expands 7→8 (Konzen added); 5 May 2026 errata superseded; today's morning P0-4 Konzen-strip reversed |
| New errata entries logging each | `errata.html` (3 new entries at top of 2026 section) | 5 May entry now carries "SUPERSEDED 17 May 2026" banner |
| Static PDFs regenerated | `abstract.pdf`, `methodology.pdf`, `errata.pdf`, `bibliography.pdf` | All four reflect the rollback |



This file documents what changed during the audit-fix pass, what's
recoverable / reversible, and the small list of items that can only be
done by you (because they need an external account or DNS access).

**Deploy:** see `DEPLOY.md` for the one-time GitHub + Netlify connect
steps and the day-to-day workflow.

## Evening pass — what was added (8 May 2026, world-class continuation)

| What | Where |
|------|-------|
| Errata page (formal revisions log) | `errata.html`, linked from Reference nav and footer |
| "Cite this page" widget on every page | `assets/cite-widget.{css,js}`, in shared footer |
| Plausible analytics scaffold (commented-out by default) | `scripts/inject-analytics.py`, every page |
| ORCID placeholders | `index.html` JSON-LD; `about.html` bios; `.zenodo.json`; `CITATION.cff` |
| Wikidata QuickStatements file | `wikidata/quickstatements.txt`, plus README |
| Zenodo deposit metadata | `.zenodo.json` |
| Citation File Format metadata | `CITATION.cff` |
| German translations | `de/abstract.html`, `de/glossary.html`, with hreflang cross-links |
| Deep-zoom (OpenSeadragon) on Evidence cards | `assets/deep-zoom.{css,js}`; cards 2/3/4/6/8 have scans |
| 12 SPA tabs extracted to citable static URLs | `latest-findings.html`, `overview.html`, `foundation.html`, `charles-in-america.html`, `civil-war.html`, `people-in-the-story.html`, `immigration-journey.html`, `germany-and-origins.html`, `family-tree-spa.html`, `key-evidence.html`, `schrader-correspondence.html`, `source-archive.html` |
| Extracted SPA stylesheet | `assets/cinematic-spa.css` |
| Print-tightened stylesheets | `abstract.html`, `methodology.html` |
| Static PDFs | `abstract.pdf`, `methodology.pdf`, `errata.pdf`, `bibliography.pdf` |
| New build scripts | `scripts/inject-analytics.py`, `scripts/build-pdfs.py`, `scripts/extract-spa-tabs.py` |
| Hygiene fixes | `styleguide.html` (2-H1 → 1), `peter_charts_download_checklist.html` (added viewport meta) |
| Git repo + deploy doc | `.gitignore`, `DEPLOY.md`, initial commit `686125d` |

## What's still on you (external accounts / human steps)

These are blocking on identifiers or services I don't have access to from
the file tree. `DEPLOY.md` documents each in step-by-step form; the short
list:

1. **Mint ORCID iDs** — both authors, 5 minutes each, then run the
   sed sweep at the top of `DEPLOY.md` to swap `PLACEHOLDER-ORCID-*`.
2. **Push to GitHub + connect Netlify** — `DEPLOY.md` § 2 / 3.  This
   single step makes the audit-fix work and everything in the evening
   pass actually live on `charles-research.netlify.app`
   (currently stale — `abstract.html`, `methodology.html`,
   `sitemap.xml`, etc. all 404 in production).
3. **Mint Zenodo DOI** — `.zenodo.json` is ready to drop in.
4. **Run Wikidata QuickStatements** — file is ready in `wikidata/`.
5. **(Optional) Activate Plausible** — `scripts/inject-analytics.py --enable`.

---

## What changed in the file tree

### New files

| Path | What it is |
|------|------------|
| `about.html` | New About-the-authors page with bios, declared interests, citation guidance. |
| `contribute.html` | New "How to add to the research" page with four contribution pathways and `mailto:` intake. |
| `LICENSE` | CC BY-NC-SA 4.0 licence file for the project text and analysis. |
| `netlify.toml` | Explicit Netlify build config (publish dir = root, redirects from old hostname, cache headers). |
| `.netlifyignore` | Tells Netlify to skip archives and editor artefacts. |
| `robots.txt` | Updated to add `Disallow: /notes/` and `Disallow: /_archive*/`. |
| `sitemap.xml` | Auto-generated from canonical pages. |
| `assets/site-nav.html` | Shared navigation HTML fragment (with the new "Reference" group). |
| `assets/site-footer.html` | Shared footer HTML fragment. |
| `assets/site-nav.css` | CSS for the shared nav + footer. |
| `assets/site-nav.js` | JS that drives the dropdown menus on standalone pages. |
| `assets/dark-mode.css` | `prefers-color-scheme: dark` re-binding of the theme variables. |
| `assets/og/*.svg` | 32 per-page Open Graph card SVGs. |
| `charles_america/index.html` | New section landing page. |
| `correspondence/index.html` | New section landing for the Schr&auml;der correspondence. |
| `evidence/card-1-trendelburg-kontzen.html` … `evidence/card-8-1896-conson.html` | 8 per-card evidence pages with full per-page metadata + Article JSON-LD. |
| `scripts/*.py` | Eight maintenance scripts (see below). |
| `_archive_pre_audit_fixes/` | Snapshot of the pre-fix tree (see "What's reversible" below). |

### Modified files

| Type | Pages affected | What changed |
|------|----------------|--------------|
| Domain sweep | 89 HTML files | `charlesgannsen.netlify.app` → `charles-research.netlify.app`. |
| Heading hierarchy | `germany/parish-map.html` | H1 → H3 → H2 → H4 collapsed to a clean H1 → H2 → H3 outline. |
| Theme color | 147 pages | Added `<meta name="theme-color" content="#1F1A14">`. |
| `rel="noopener noreferrer"` | 1599 link-attribute additions across the tree | Every `target="_blank"` now has the security/perf rel. |
| Reduced motion | 45 pages | Inline `<style>` blocks now wrap animations in `@media (prefers-reduced-motion: reduce)`. |
| Shared nav + footer | 146 standalone pages | Inserted `<!-- BEGIN-INJECTED-NAV -->` and `<!-- BEGIN-INJECTED-FOOTER -->` blocks. |
| Dark-mode CSS link | 159 pages | Added `<link rel="stylesheet" href=".../assets/dark-mode.css">`. |
| Per-page JSON-LD | 10 article pages + 27 person pages | Article / Person JSON-LD with marker comments. |
| OG image rewrite | 17 pages | Per-page OG card under `assets/og/`. |
| Notes noindex | 158 files in `/notes/` | `<meta name="robots" content="noindex,nofollow">`. |
| Home nav | `index.html` | Added a 6th "Reference" group with Abstract / Methodology / FAQ / Glossary / Bibliography / Open Questions / Visualize / Changelog / About / Contribute. |
| Home page citation block | `index.html` | New `#cite` section just below the SPA sections. |
| Search lazy-loading | `assets/site-search.js` | Removed the eager 1.2s pre-warm; index now only loads on first focus / click / `/` shortcut. |

### Archived (moved to `_archive_pre_audit_fixes/`)

| What | Why |
|------|-----|
| `_deploy_netlify_mirror/` (493 MB) | Duplicate of the entire site tree — replaced by explicit `netlify.toml`. |
| 8 `.bak` files in `germany/` and `immigration/` | Editor backup files exposed at live URLs. |
| `index.html.snapshot` | Pre-fix copy of the home page in case any of the structural changes need to be reverted. |

### Archived (moved to `_archive/notes/`)

48 versioned drafts of `Kontze_Konze_Complete_Family_Reconstruction_*.html`,
`Research_Paper_for_Peter_Schrader_*.html`, and similar earlier-version
working artefacts. The latest version of each group remains in `/notes/`.

---

## What's reversible

Everything destructive was moved, not deleted, so the pass is fully
reversible until you choose to clean up.

- `_archive_pre_audit_fixes/_deploy_netlify_mirror/` — restore with
  `mv _archive_pre_audit_fixes/_deploy_netlify_mirror _deploy_netlify`
- Archived `.bak` files — `mv _archive_pre_audit_fixes/bak_files/*.bak germany/` etc.
- Archived `/notes/` versioned drafts — `mv _archive/notes/* notes/`
- Domain sweep / nav injection / theme-color / rel-noopener — re-run any
  of the relevant `scripts/*.py` files to recompute, or restore from
  `_archive_pre_audit_fixes/` snapshot.

Once you've verified a Netlify deploy looks right, you can safely
`rm -rf _archive_pre_audit_fixes/` to recover the disk space (~493 MB).

---

## Scripts (under `scripts/`)

| Script | What it does | Idempotent? |
|--------|--------------|-------------|
| `inject-site-nav.py` | Inserts the shared nav + footer + asset links on every standalone page. | Yes — replaces `BEGIN/END` markers in place. |
| `a11y-and-meta-sweep.py` | Adds theme-color, rel=noopener, prefers-reduced-motion. | Yes. |
| `archive-old-notes.py` | Moves superseded versioned drafts from `/notes/` to `_archive/notes/`. | Yes (only acts on what's still in `/notes/`). |
| `build-sitemap.py` | Regenerates `sitemap.xml` from current canonical pages. | Yes — overwrites. |
| `inject-jsonld.py` | Adds Article + Person JSON-LD to key pages. | Yes — replaces `BEGIN/END` markers. |
| `build-evidence-cards.py` | Regenerates the 8 per-card pages from a Python data dict. | Yes — overwrites. |
| `inject-dark-mode-css.py` | Adds the `dark-mode.css` link to every standalone page. | Yes. |
| `build-og-cards.py` | Generates 32 per-page OG card SVGs; with `--update-pages` rewrites `og:image` meta. | Yes. |

Re-run any of them after content changes; all are safe to invoke
repeatedly.

---

## What needs you (external accounts / DNS)

These are the items the audit recommended that I cannot do from the
file tree alone.

### 1 · Zenodo DOI

Mint a Zenodo DOI to make the project formally citable. Free, ~30
minutes one-time setup.

1. Sign in at <https://zenodo.org/> with your GitHub or ORCID identity.
2. Create a new "Software" or "Dataset" record. Use the title
   "Charles Konzen Research: A Genealogical Investigation."
3. Authors: Jed Johnson, Peter Schr&auml;der.
4. Description: copy the lede from `abstract.html`.
5. Keywords: copy from the `Keywords` paragraph at the bottom of
   `abstract.html`.
6. Licence: CC BY-NC-SA 4.0 (matches `LICENSE` here).
7. Version: 1.0.0.
8. Upload either a snapshot ZIP of this repo or a curated PDF (the
   docx audit report would also work for a first deposit).
9. After publishing, paste the DOI into the citation block on
   `index.html` (`#cite`) and on `about.html` (`#how-to-cite`). Replace
   the line "A persistent DOI through Zenodo is in progress" with the
   actual DOI string.

### 2 · DNS / domain redirect

The `netlify.toml` here includes a 301 redirect from
`charlesgannsen.netlify.app/*` → `charles-research.netlify.app/*`.
That redirect only fires if the old subdomain is still mapped to this
Netlify site. If you no longer own / control that subdomain, the
redirect is harmless dead code (delete the first `[[redirects]]` block
in `netlify.toml`). If you do, leave it — it picks up any inbound link
that still uses the old name.

If you eventually move to a custom domain (e.g. `konzenresearch.org`),
update three places:

1. The `og:url`, `canonical`, and JSON-LD `url` strings across the
   site — easiest with a one-line `find` + `sed`:
   ```
   find . -name "*.html" -not -path "./_archive*" -not -path "./_backup*" \
     -exec sed -i 's|charles-konzen-research\.netlify\.app|konzenresearch.org|g' {} +
   ```
2. The `Sitemap:` line in `robots.txt`.
3. The `BASE` constant in `scripts/build-sitemap.py`,
   `scripts/inject-jsonld.py`, and `scripts/build-evidence-cards.py`.

### 3 · Optional · email-list provider

Buttondown (or Substack, MailerLite, etc.) — sign up, paste the
embed code into `contribute.html` or a new `subscribe.html`, and add
the link to the shared footer's "Project" column in
`assets/site-footer.html`.

### 4 · Optional · OG card rendering

The OG card SVGs under `assets/og/` use Cormorant Garamond, which
renders fine in any browser unfurl previewer. If you want hard-rasterised
PNG versions for legacy social platforms (LinkedIn legacy, some Slack
clients), run any local SVG → PNG converter once on the directory and
update the og:image meta to the .png paths. Optional only.

### 5 · After-deploy verification

1. Visit `https://charles-research.netlify.app/sitemap.xml` and
   confirm 159 URLs.
2. Visit `https://charles-research.netlify.app/robots.txt`.
3. Run any unfurl previewer (twitter card validator, Facebook sharing
   debugger, OpenGraph.xyz) on `/abstract.html`, `/germany/parish-map.html`,
   and `/evidence/card-1-trendelburg-kontzen.html` to confirm the
   per-page OG cards render.
4. Run Google's Rich Results Test on the home page to confirm the
   JSON-LD is well-formed.
5. Open the home page on a phone to confirm the new mobile theme-color
   tints the address bar.

---

## What's left from the audit catalogue

The audit's Stage 3 item "Split SPA: move section content into static
pages" was implemented as the **incremental** version: per-section
landing pages are now in place at every section folder URL
(`/charles_america/`, `/correspondence/`, `/civilwar/`, `/germany/`,
`/immigration/`, `/people/`, `/sources/`, `/towns/`, `/children/`,
`/evidence/`), each with proper per-page title, description, canonical,
JSON-LD, and OG card. The 628 KB `index.html` SPA is **unchanged** —
splitting its 12 in-DOM tabs into separate static pages is a more
invasive refactor that the audit estimated at one week and was
deliberately deferred. The lazy-load alternative (the audit's "one-day
fix") would be the natural next step; the search-index lazy-load that
was just shipped is the proof-of-concept pattern.

The audit's stage 3 item "Migrate inline styles in `index.html` to
utility classes" was **not** done — it's a careful refactor that
deserves an interactive session rather than a sweeping script.

---

## Audit document

The full audit report this pass implements lives at:

```
Charles_Konzen_Site_Audit_May8_2026.docx
```

Each fix here cross-references the audit ID it implements (e.g. "FIX 3"
in commit messages refers to the audit's "Resolve project identity
drift" recommendation; "SEO-3" refers to the sitemap / robots
recommendation, etc.).
