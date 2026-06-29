# Session 140 — Parish Research-Log Standardization (4-column Sources table)

**Date:** 28 June 2026
**Scope:** Bring every `germany/<parish>-research-log.html` up to the
Heisebeck/Liebenau standard — the canonical **4-column "Sources checked"
table** (Register · Image · Archion permalink · Record at this image) plus a
**"Remaining follow-ups"** list — without fabricating any data.

## What the standard is

Exemplars: `heisebeck-research-log.html`, `liebenau-research-log.html`
(also Deisel, Trendelburg, Stammen, Hümme, Diez, Schierstein). Each has:

- `<table class="src">` with `<thead>` = **Register | Image | Archion permalink
  | Record at this image**, and per-row `<td class="img">` image numbers.
- Minted permalinks `https://www.archion.de/p/<10-hex>/` where they exist;
  the honest fallback `img NNNN (no permalink minted)` (linked to the register
  viewer) for by-eye leaves — the standard itself uses this (e.g. Liebenau
  img 1448/1465).
- A `<p class="note">` on method/reliability, then `<ul class="fu">` follow-ups
  with `<span class="lane">` tags.

## Audit result (41 logs)

- **8 already at standard** — untouched: Heisebeck, Liebenau, Deisel,
  Trendelburg, Stammen, Hümme, Diez, Schierstein.
- **32 converted** from the old 2-column "Source · What was checked" format.
- **1 left as-is — Friedrichsfeld**: it kept **no register of its own**
  (colonist filial; confirmands fold into the Deisel/Trendelburg mother-church
  books, which are already at standard). Its content is the Justus-Ernst-Konze
  emigration/US-record trail — no Archion images to permalink, so a 4-column
  register table does not apply.

## Data sourcing — no fabrication

Most prime-leaf permalinks already existed, minted during the original live
sweeps and recorded in the session logs / page prose. Image→year maps were
mined from the session files (e.g. Lamerden Session118, Eberschütz Session115,
Immenhausen Session120, Kelze Session117, Grebenstein Session119, Karlshafen
Session131, Gudensberg Session135, Hofgeismar Session126). Every permalink and
Bild written into the tables is a **real, pre-existing value** copied from those
sources.

## Live Archion minting — viewer blocker

Per Jed's instruction the plan was to mint missing permalinks live. **Finding:
the Archion deep-zoom viewer never returns to a `document_idle` state after an
in-viewer image change** (combobox jump *or* next-arrow), so screenshots /
DOM reads hang (45 s+); the URL does not encode the image, so a specific leaf
can't be reloaded cleanly. Reliable mint/read is therefore only possible on a
register's **default landing image**.

- **1 new permalink minted live & verified:** Lamerden Konfirmationen 219673,
  **section title img 675 = `https://www.archion.de/p/fece6afbf4/`**.
- For all other gaps: used the recorded data + the standard
  `img NNNN (no permalink minted)` convention (Jed's chosen path).

## Open tasks — preserved & flagged (⚑ / ★)

| Parish | Open thread |
|---|---|
| Grebenstein | 1852–1855 confirmation tail (Bild ~1911–1920) + 1847 head-entries 1–4 (Bild 1896) — youngest years, low priority |
| Veckerhagen | two displaced leaves Seite 80–81 (1847) & 102–103 (1853) unlocated in the duplicate-exposure reel |
| Lippoldsberg | 1851–1855 reads (Bild 159–165) to re-confirm on the ordered leaves |
| Marzhausen | mint the "pending" per-year/leaf permalinks (viewer throttled) |
| Schöneberg | pre-1822 Kirchenbuch — undigitised, on-site / Kassel archive |
| Gieselwerder | **active Warnecke lead** — burial reg. 219022 (shuffled/unindexed) + marriage 219028; Warnecke death ~1834–36 unread → Schräder / archive trip |
| Hofgeismar | HStAM Best. 180 Hofgeismar emigration file (offline) |
| Mainz | possible Mainz civil death record for Justus Ernst Konze |
| Oedelsheim | faded K-index leaf (219946 Bild 918) — specialist / image-processing |
| Bodenfelde | finding aids not yet mined (Taufen-Konf 1837–52, Kartei Männer Gans/Contze-178) |

## Verification

- 0 row/cell mismatches (every Sources-table row has the right cell count).
- All `<table>` tags balanced in all 41 logs.
- No `Source | What was checked` 2-column tables remain.
- Follow-ups present in every converted log; open-task flags intact.

## Residual (for a stable viewer session)

**19 logs** carry at least one `img NNNN (no permalink minted)` leaf — cited by
register + Bild (an exact Archion citation) but without a `/p/` short-link.
Highest-value to mint when the viewer cooperates: the prime-cohort confirmation
leaves (e.g. Lamerden img 695/699, Karlshafen non-prime years, Marzhausen's
"pending" set, Helmarshausen confirmations 219208).

## Phase 2 — distinct breakout sections (same session)

The gold standard isn't only the consolidated *Sources checked* table — Liebenau
(and the richer logs) also break the work into **distinct sections**: a
year-by-year **Confirmation-register sweep** table (Class · Bild · permalink ·
Carls/verdict) and a separate **Baptism index/sweep** section, each with their
own image numbers/permalinks. The first pass had folded everything into the one
table for the thinner logs. Added the breakout sections to the 12 substantive
Lutheran parishes that were still at "Sources + follow-ups only":

**Immenhausen, Karlshafen** (both confessions), **Veckerhagen, Oedelsheim,
Grebenstein, Ostheim, Niedermeiser, Haueda, Hombressen, Eberschütz, Lamerden,
Lippoldsberg** — each now has a year-by-year confirmation table (with Bild +
permalinks where minted, else register+Bild) and a baptism index/sweep section,
built from the session-log per-class data (Immenhausen S120, Grebenstein S119,
village sweeps S122, Eberschütz S115, Lamerden S118, etc.).

Granularity is honest: Haueda/Hombressen pin the prime 1849 leaf and note the
flanking years at forename level (their Session 122 per-year transcript was lost
to a context compaction); Veckerhagen/Oedelsheim/Lamerden/Grebenstein carry the
full year→Bild map read by eye (no per-year permalink minted).

Left appropriately lighter: Heisebeck (reference exemplar — its confirmation read
sits in the Sources table + a follow-up), Grifte/Dissen (no separate
Konfirmationen register — combined book ends 1841), Beverungen/Dalhausen/Herstelle
(Catholic, baptism-only), Mainz/Dies/Friedrichsfeld (no own register).

Re-verified: all `<table>` balanced; all Sources/sweep rows have the correct cell
count (the one Trendelburg flag is a legitimate `colspan` sub-header).

## Files touched

All under `germany/`: lamerden, immenhausen, eberschuetz, kelze, grebenstein,
karlshafen, gudensberg, hofgeismar, haueda, hombressen, niedermeiser, ostheim,
veckerhagen, dies, marzhausen, oedelsheim, helmarshausen, beverungen, dalhausen,
herstelle, mainz, bodenfelde, gewissenruh, gieselwerder, dissen, gottsbueren,
grifte, lippoldsberg, schoeneberg, fulda, sielen, vernawahlshausen
(+ friedrichsfeld reviewed, intentionally left as a no-own-register filial).
