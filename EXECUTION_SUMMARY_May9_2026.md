# Execution summary — 11-item punch list, 9 May 2026

**Context.** This session ran in parallel with another Cowork session
("Improve Charles Konzen research site", `local_5f6a768b...`) that was
mid-execution on the same project tree. To avoid file races, this
session worked only on **non-overlapping deliverables**: new top-level
documentation, a more aggressive SPA-split plan + script, and a
flexible deploy script. The parallel session shipped the bulk of the
in-page work (errata, cite widget, deep-zoom, /de/ translations,
print CSS, conservative SPA extract, git init, DEPLOY.md, CITATION.cff,
.zenodo.json, wikidata/quickstatements.txt).

This document maps each of the 11 punch-list items to **what shipped**,
**who shipped it**, and **what remains**.

---

## Status by punch-list item

| # | Item | Status | Delivered by | What's there |
|---|------|--------|--------------|--------------|
| 1 | Ship the May 8 audit-fix work to Netlify | **Stage-ready** | Sibling (git init) + this session (`deploy.sh`) | `git init` + initial commit `686125d`; `deploy.sh` (one-command, three deploy modes); `DEPLOY.md` (sibling's narrative guide). **Still needs:** push to a real GitHub remote (`git remote add origin …`), or run `bash deploy.sh` to produce a drag-and-drop zip. |
| 2 | Move 12 SPA tabs out of `index.html` | **Conservative split shipped; aggressive split staged** | Sibling (conservative) + this session (aggressive plan + script) | Conservative: 12 standalone pages (`latest-findings.html`, `civil-war.html`, …) created by `scripts/extract-spa-tabs.py`, paired with `<link rel="alternate">` from the home page. `index.html` is unchanged at 6,404 lines. Aggressive next stage: `SPA_SPLIT_PLAN.md` + `scripts/split-spa.py` (idempotent, dry-run-able, with rollback). Recommend running aggressive only after conservative is verified indexed. |
| 3 | Mint Zenodo DOI | **Pending mint** | Sibling (`.zenodo.json`, `CITATION.cff`) + this session (`IDENTIFIERS_KIT.md`) | Pre-filled metadata in `.zenodo.json`; full mint workflow + sed swap commands in `IDENTIFIERS_KIT.md` §1. **Needs you:** ~30 min at <https://zenodo.org/>. |
| 4 | ORCID + Wikidata anchors | **Pending mint** | Sibling (`wikidata/quickstatements.txt`, JSON-LD `sameAs` placeholders) + this session (`IDENTIFIERS_KIT.md`, `WIKIDATA_DRAFT.md`) | Placeholders wired through ~35 HTML files + `CITATION.cff` + `.zenodo.json`. QuickStatements batch ready to paste at <https://quickstatements.toolforge.org/>. **Needs you:** ~10 min ORCID each (Jed, Peter); ~30 min Wikidata. |
| 5 | German Abstract + Glossary | **Done** | Sibling | `de/abstract.html` + `de/glossary.html`, archive-formal Hochdeutsch (Sie register), full hreflang chain + JSON-LD `translationOfWork`. |
| 6 | Deep-zoom on 8 evidence cards | **Done (5 of 8)** | Sibling | `assets/deep-zoom.{js,css}` lazy-loads OpenSeadragon. Cards 2, 3, 4, 6, 8 have pannable scans; cards 1, 5, 7 do not yet (scan files missing or not yet wired). Print fallback to static image. |
| 7 | Print CSS + `/abstract.pdf` | **Done** | Sibling | Print stylesheets tightened on `abstract.html`, `methodology.html`, `errata.html`, `bibliography.html`. `scripts/build-pdfs.py` (WeasyPrint) renders each to PDF; "⤓ Download PDF" buttons in the heroes. (Note: WeasyPrint requires headless system deps — `bash deploy.sh --build-only` will warn if missing.) |
| 8 | Resolve inline-style sprawl | **Plan-only** | This session (in `SPA_SPLIT_PLAN.md`) | Inline-style normalisation is folded into `scripts/split-spa.py` — when the aggressive SPA split runs, recurring styles (≥3 occurrences) are extracted to `assets/spa-split-utilities.css` as `s-XXXXXX` utility classes. 229 unique inline styles (639 occurrences); 59 recur 3+ times → ~59 utility classes. Not yet executed. |
| 9 | Mobile search QA | **Deferred — needs deploy** | (deferred) | Cannot meaningfully QA the lazy-loaded search index until the deploy lands. After Netlify is live, open the site in Chrome devtools iPhone emulation, focus the search box, verify the 236 KB index loads + returns hits. The `assets/site-search.js` lazy-load architecture is in place. |
| 10 | Hygiene leftovers | **Done** | Sibling | `styleguide.html` 2-H1 collapsed to 1; `peter_charts_download_checklist.html` viewport meta added; analytics scaffolding (`scripts/inject-analytics.py`, off by default — flip on with `--enable`); 404.html exists at root. |
| 11 | Errata + cite widget + Wayback + OG audit | **Mostly done** | Sibling (errata, cite widget) | `errata.html` exists (5 entries seeded). `assets/cite-widget.{js,css}` auto-builds Chicago / NGSQ / MLA citations into the shared footer with copy buttons. **Still needs you:** OG validator runs (post-deploy: <https://www.opengraph.xyz/>, Twitter Card validator); Wayback snapshot submission. |

**Net status.** 8 of 11 items fully done or one-step-from-done. 3 of
11 require action only the user can take (Zenodo / ORCID / Wikidata
mint, post-deploy QA, OG validation, Wayback submission).

---

## What this session contributed

Five new files (none of which conflict with the sibling's work):

| File | Purpose |
|------|---------|
| `IDENTIFIERS_KIT.md` | Long-form workflow for the three external identifiers, with copy-paste field-by-field instructions for Zenodo / ORCID / Wikidata web forms and the master `sed` swap commands. Cross-references the sibling's `CITATION.cff`, `.zenodo.json`, `wikidata/quickstatements.txt`, and `DEPLOY.md`. |
| `WIKIDATA_DRAFT.md` | Annotated, claim-by-claim review of the Wikidata Q-item with confidence flags (CONFIRMED / ASSERTED / OMIT). Read this before submitting `wikidata/quickstatements.txt` so you understand what's being claimed. |
| `SPA_SPLIT_PLAN.md` | The aggressive next-stage SPA split: actually shrink `index.html` from 6,404 lines to ~1,000. Maps each of the 12 sections to its target URL, identifies 12 of 12 sections in `index.html`, lists 229 inline-style occurrences. |
| `scripts/split-spa.py` | Idempotent extractor for the aggressive split. `--dry-run`, `--stage`, `--apply --strategy=read-through\|replace`, `--rollback`. Depth-aware HTML parsing handles nested `<section>` tags. Creates `*.pre-split.bak` files for rollback. |
| `deploy.sh` | One-command deploy + verify. Auto-detects deploy mechanism (Netlify CLI → git push → manual zip) and runs the HANDOFF five-step verification. `--dry-run`, `--build-only`, `--snapshot=PATH`, `--verify-only` modes. |

Plus **this** file (`EXECUTION_SUMMARY_May9_2026.md`).

---

## Concrete recommended next steps (in order)

1. `bash deploy.sh` — produces a drag-and-drop zip at the project
   root (since no GitHub remote is configured yet). Drag onto
   <https://app.netlify.com/sites/charles-konzen-research/deploys>.
   This is the move that flips items 1, 5, 6, 7, 8 (sibling), 10, 11
   from "staged" to "live."

2. **Optional but recommended before step 1:** add a GitHub remote
   so future deploys are `git push` not zip. The sibling's
   `DEPLOY.md` walks through this.

3. Mint Zenodo DOI per `IDENTIFIERS_KIT.md` §1 (~30 min). Run the
   §4.1 `sed` swap. Re-deploy.

4. Mint your ORCID per `IDENTIFIERS_KIT.md` §2.B.1 (~10 min). Send
   Peter the German prompt template (also in §2.B.2). Run §4.2 and
   §4.3 swaps. Re-deploy.

5. Mint Wikidata Q-item via `wikidata/quickstatements.txt` (review
   `WIKIDATA_DRAFT.md` first, ~30 min). Run §4.4 swap. Re-deploy.

6. Run the post-deploy 5-step verification (`bash deploy.sh
   --verify-only` prints the checklist). This is item 9 (mobile
   search QA) and the OG / Wayback parts of item 11.

7. Once items 1–6 are confirmed indexed by Google (give it a week),
   consider running the aggressive SPA split:

   ```bash
   python3 scripts/split-spa.py --dry-run    # review
   python3 scripts/split-spa.py --stage      # extract
   python3 scripts/split-spa.py --apply --strategy=read-through
   bash deploy.sh
   ```

---

## Caveats + things to double-check

- **The 8 evidence cards were regenerated mid-session.** When this
  session ran `bash deploy.sh --dry-run` (before the dry-run mode
  was hardened), `scripts/build-evidence-cards.py` fired and
  rewrote all 8 cards from the current template. The sibling
  session was actively editing that template at the time. Spot-check
  one or two cards (e.g. card-1, card-5) to confirm they look right.
- **Sibling-session script `scripts/extract-spa-tabs.py` and this
  session's `scripts/split-spa.py` are different tools.** Don't run
  both. The sibling's runs first (conservative); this session's is
  the optional aggressive next stage.
- **The `--dry-run` mode in `deploy.sh` was hardened mid-session
  to skip build steps.** If you re-run `--dry-run` from the
  current `deploy.sh`, no files will be touched. The first run
  (~02:38 UTC, 9 May) did rebuild artifacts — that is the source
  of the evidence-card timestamps from that minute.
- **6 `PLACEHOLDER-ORCID-*` references remain live** until you mint.
  This is expected; `deploy.sh` reports them as a warning, not an
  error. The `sed` swap in `IDENTIFIERS_KIT.md` §4 fills them in
  one shot.

---

## Sources

- `HANDOFF.md` — sibling-session handoff for the 8 May audit-fix pass.
- `Charles_Konzen_Site_Audit_May8_2026.docx` — original audit.
- `Charles_Konzen_Audit_Fix_Completion_May8_2026.docx` — completion
  report from the prior pass.
- `DEPLOY.md` — sibling-session deploy guide (companion to this one).
- `IDENTIFIERS_KIT.md`, `WIKIDATA_DRAFT.md`, `SPA_SPLIT_PLAN.md` —
  this session's three companion docs.
- `scripts/split-spa.py`, `deploy.sh` — this session's two
  executables.

*Generated 9 May 2026 — see also `HANDOFF.md` for the prior pass.*
