# Session 113 — Parish Search Coverage: daily open-web recheck (all parishes)

**Date:** 23 June 2026
**Type:** Automated scheduled run (`update-parish-search-coverage`). No user present.
**Scope:** Refresh pass across **all 36 parishes** on `search-coverage.html` — the
Konze-pool cluster, the confirmation-register sweep (incl. Tier-3 "Deissen"),
the 1835 baptism-window sweep, the Catholic Westphalia border, and the
toponym/family-trail tests. Priority on rows still "Not yet", "Partial",
"Queued", or "Candidate".

## Tooling note
Per `CLAUDE.md` the preferred web-research tools are Nimble and Bright Data.
In this unattended sandbox neither CLI is installed (`nimble`/`bdata` not on
PATH) and the Nimble MCP needs an interactive auth flow that cannot complete
without the user. Substituted the available open-web tools (WebSearch +
web_fetch) for this pass and noted it here. Subscription sites (Archion,
Ancestry, FamilySearch gated, MyHeritage, Fold3) were **not** touched — out of
scope for an automated run, per the task and CLAUDE.md.

## What was searched
Open-web queries run this pass:
- Konze / Konzen / Kontze / Gansen surname + Trendelburg / Deisel / Hofgeismar
  Kirchenbuch — generic results only (GenWiki, GEDBAS landing, OFB catalogs).
- Charles Gannsen / Konzen + Battery B, 2nd Missouri Light Artillery — no
  individual-level hits beyond the unit history already known.
- GEDBAS Konze/Kontze Hofgeismar 1835 — GEDBAS now behind Anubis bot-wall
  (`Access Denied`); no record-level read possible via open web.
- Ortsfamilienbuch / Ortssippenbuch for Schöneberg, Heisebeck, Liebenau —
  located the Heisebeck OFB online register (see finding below); Schöneberg OFB
  covers 1702–1798 only (pre-window).
- Heisebeck "Candidate" forward-trace: Carl/Charles **Wehmann** b. ~1835
  emigrant — nothing new (one unrelated Heisebeck→Kentucky emigrant
  "Heinrich Wilhelm", 1865 naturalization).
- Schöneberg ("Not yet") confirmations — confirmed still gated on Archion
  (reg. 220012); no open-web access.

## New, verifiable result (the only one)
**Heisebeck — Ortssippenbuch surname register is online and lists no Konze line.**
The published *Ortssippenbuch Heisebeck und Arenborn* (Klaus Kunze, Uslar 2000,
ISBN 978-3-933334-08-4 — a full evaluation of the parish church books) has its
complete name/place/subject register on the open web:
`https://klauskunze.com/heikun/hei/heisebeck_register.htm`. Fetched and grepped:
**no** Konze / Konzen / Kontze / Gansen / Gonsen / Jansen / Jungkonze surname
appears. The index is genuine — established Heisebeck families (Schulze, Klinge,
Thiele, Wienecke, Helwig, Schäfer) are all present. Reading: the Konze surname
was **not native** to Heisebeck, consistent with the standing Heisebeck
candidate being the illegitimate *Wehmann* child (mother's surname), not a Konze.
Caveat — a compiled secondary index, not the original register; corroborating
context only, no status change. (Same evidence class as the Helmarshausen OSB
surname-register lead carried from 22 June.)

## Changes made
- `search-coverage.html` — replaced the dated "Open-web recheck — 22 Jun 2026"
  callout with a **23 Jun 2026** version: states the pass ran clean (no new
  confirmation-class match, no parish status changed), adds the new Heisebeck
  OFB-register data point, and carries the Helmarshausen OSB lead. JSON-LD
  `dateModified` → 2026-06-23. **No row, pill, or summary-strip count changed**
  (still 36 parishes searched · 20+ Carls in window · 0 with a Konze/*n-s-n
  surname · 1833–1841).
- `germany/heisebeck-research-log.html` — appended a follow-up entry recording
  the OFB-register check (DONE, open web, 23 Jun 2026).

## Net result
Daily check ran clean. No confirmation-class match for a Konze-type Carl, and no
parish moved status. One new open-web corroboration (Heisebeck OFB register has
no Konze surname) folded into the coverage callout and the Heisebeck log.

## Still outstanding (unchanged from 22 Jun)
- Deisel core class (218836) queued for AI transcription.
- Schöneberg 1849–50 confirmations (220012) — scan-jumble-blocked leaf; Archion-gated.
- Not digitised / on-site Tier: Heisebeck pre-1845 marriages context, Liebenau 1835,
  Schöneberg pre-1822.
- Gated US forward-trace of the Wehmann candidate (FamilySearch/Ancestry login;
  NARA AAD "Germans to America" interactive form — neither runnable unattended).
