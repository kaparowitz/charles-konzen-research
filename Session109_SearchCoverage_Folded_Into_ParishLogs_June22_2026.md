# Session 109 — Folded the confirmation-register sweep into the individual parish logs

**Date:** 22 June 2026
**Scope:** Jed: "Combine the parish search coverage with the Hessian Parish Map so all
the parish info is in one place — keep the Hessian parish map and add all the info to the
individual parish pages, if you think that is wise."

---

## Decision (confirmed with Jed)

- **Keep `germany/parish-map.html` as the hub** (untouched) — its cards already link to the
  per-parish research logs.
- **Keep `search-coverage.html` as the cross-parish synthesis ledger** — it holds material
  that belongs to no single parish (boys-named-Carl list, method/reliability notes, the
  "reasonably exhaustive research" GPS overview, "what the sweep means").
- **Fold each parish's confirmation-sweep row into its own parish research log** as a new,
  visually distinct section — *not* merged into the existing Konze "Sources checked" table
  (the two are different searches: any-Carl confirmation sweep vs. Konze-surname citations).

## What changed

1. **12 parish logs** got a new `<h2 class="sec">Confirmation-register sweep — "any Carl,
   1833–1841"</h2>` section, inserted between the status box and the next section. One
   register/window/result row each, with a colored result label (Searched / Carl found /
   Partial / Queued / Not yet / Covered) matching the search-coverage legend, plus the
   per-parish detail (the Carl found, father's trade, classes still to read):
   helmarshausen, huemme, sielen, deisel, trendelburg, friedrichsfeld, schoeneberg,
   hofgeismar, schierstein (Freudenberg), gudensberg, dissen, grifte.
   Each section links back to `search-coverage.html` for the cross-parish picture.

2. **`search-coverage.html`** — added a "Parish research log →" link under every parish in
   the coverage table (12 links), a note under the *Coverage* heading explaining the row now
   also lives on each parish log, and bumped JSON-LD `dateModified` to 2026-06-22. All the
   synthesis content was retained.

## Verification

- `scripts/check_links.py`: **437 pages, 0 broken refs.**
- Python `HTMLParser` on all 13 edited files: parses clean; `<tbody>` balanced in each;
  exactly one sweep section per parish log.
- Section placement confirmed to sit after `.pl-status` and before the next `h2.sec`
  (including friedrichsfeld, whose first section is "Online lane" not "Sources checked").

## Backups

- Originals copied to `_backup_originals/sweep_merge_20260622/` (13 files) before editing.

## Not changed (deliberate)

- `germany/parish-map.html` — kept as the hub per Jed's instruction.
- search-coverage.html structure/synthesis — preserved; only links + a note + date added.
