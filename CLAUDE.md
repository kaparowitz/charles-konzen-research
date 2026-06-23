# Charles Gannsen Research — Project Instructions

**At the start of every session, also read `_MEMORY_Session_Conventions.md`.**
That file holds the stable project facts, Archion viewer tricks, register
calibrations, and the session-log / file-versioning conventions. This file
covers *how to do web research* for the project.

## Project in one line

Tracing **Charles Gannsen** (Civil War pvt., b. 26 Jan 1835, German origin)
and the Konze / Kontze / Gannsen family across German church records
(Archion), FamilySearch, Ancestry, and US records. See the memory file for
the current hypothesis tree and priority queue.

## Web research tooling

Two web-data plugins are installed for pulling records from sites that have no
dedicated connector (parish indexes, archive catalogs, census databases,
newspaper and immigration sites).

- **Nimble** — search, crawl, and extract structured data from web pages.
  Default for live record lookups and bulk page pulls. Skills:
  `nimble:nimble-web-expert` (fetch / scrape any URL),
  `nimble:nimble-crawl-reference` (multi-page collections),
  `nimble:nimble-extract-reference` (pull fields out of a record page),
  `nimble:local-places` (places / addresses).
- **Bright Data** — alternative web-data toolkit (search, scrape, scraper
  builder). *Authenticated June 2026.* Skills include `brightdata-plugin:search`,
  `brightdata-plugin:scrape`, `brightdata-plugin:scraper-builder`. The CLI runs
  in the sandbox; if a session reports it isn't logged in, re-auth with
  `bdata login --api-key <Jed's key>` (key lives in the Bright Data dashboard,
  not stored here). Note: the API key works for search/scrape but lacks
  `bdata budget` permission — ignore the 403 on balance checks.

When a task needs live web data, prefer these over generic fetching. Use the
narrowest skill: extract for a known record page, crawl for a paginated
register index, search when URLs must be discovered first.

### Important boundaries

- **Subscription sites (Ancestry, FamilySearch, Archion, MyHeritage, Fold3)**
  keep records behind Jed's personal login. The web-data plugins are best for
  the **open web**; for the gated sites, continue using the in-browser /
  viewer workflow documented in `_MEMORY_Session_Conventions.md` (Archion
  zoom tricks, downloads at session start, etc.).
- Always verify a scraped record against the original image before treating it
  as confirmed — same evidentiary standard as the rest of the project.

## Output conventions (see memory file for detail)

- Session logs → `SessionNN_<topic>_<date>.md` in this folder.
- Word-doc versions → new `v<NN+1>`, never overwrite.
- Keep main site pages to stable summaries; granular forensic work goes in
  research-log files. Save final outputs here and share with file links.
