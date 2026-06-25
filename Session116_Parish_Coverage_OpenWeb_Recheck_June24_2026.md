# Session 116 — Parish Search Coverage: daily open-web recheck (all parishes)

**Date:** 24 June 2026
**Type:** Automated scheduled run (`update-parish-search-coverage`). No user present.
**Scope:** Refresh pass across **all 36 parishes** on `search-coverage.html` — the
Konze-pool cluster, the confirmation-register sweep (incl. Tier-3 "Deissen"), the
1835 baptism-window sweep, the Catholic Westphalia border, and the
toponym/family-trail tests. Priority on rows still "Not yet", "Partial",
"Queued", or "Candidate"; refresh pass across all rows.

## Tooling note
Per `CLAUDE.md` the preferred web-research tools are Nimble and Bright Data.
In this unattended sandbox neither CLI is installed (`nimble`/`bdata` not on
PATH) and the Nimble MCP needs an interactive auth flow that cannot complete
without the user. Substituted the available open-web tools (WebSearch +
web_fetch) for this pass, same as Sessions 111/113. Subscription sites
(Archion, Ancestry, FamilySearch gated, MyHeritage, Fold3) were **not** touched
— out of scope for an automated run, per the task and CLAUDE.md.

## What was searched (open web)
- Konze / Kontze / Gansen / Gonsen + Trendelburg / Deisel / Hofgeismar Kirchenbuch
  1835 — generic results only (LAGIS Ortslexikon, GenWiki Trendelburg, Hessische
  Familienkunde PDFs, a Deisel Ahnenreihe). No record-level Konze hit.
- GEDBAS Konze/Kontze Hofgeismar/Trendelburg 1834–36 Taufe — no record-level
  baptism hit; the only "Kontze + Hofgeismar" matches are a present-day
  gynecologist (Tatjana/Tatiana Kontze), irrelevant.
- Ortssippenbuch Helmarshausen name register (klauskunze.com) — **fetched and
  re-verified** (see finding).
- Ortsfamilienbuch Schöneberg / Hümme / Stammen — no online OFB name register
  for the window; the Schöneberg OFB (Desel) covers 1669–1779 (pre-window), as
  already known.
- Heisebeck "Candidate" Wehmann forward-trace (Carl/Charles Wehmann b. ~1835
  emigrant) — nothing new on the open web.
- FamilySearch open-tree Karl Konzen/Kontze b. 1835 Hessen/Kurhessen — surname
  pages only (WikiTree Konzen/Konze, konzengenealogy.com — a distinct Eifel/
  Aachen-origin Konzen line, not the Diemel-valley family). No individual match.
- Andreas Kontze / Mainz 1854 family-trail — no record-level hit.
- Matricula (Catholic border): Beverungen St. Johannes, Dalhausen St. Marien,
  Herstelle confirmed present on Matricula (already searched); no new open index.

## New / verifiable result (the only one)
**Helmarshausen — Ortssippenbuch name register re-verified (open web).**
Re-read `https://klauskunze.com/heikun/hel/register.htm` (the Klaus Kunze
*Ortssippenbuch Helmarshausen*, 4500 families 1521–1950). The register still
carries **Konze** (family nos. 67, 96, 302, 406) and **Jungkontz / Jungkonze**
(nos. 297, 507, 468); grep of the full page returned **no** Gansen / Gonsen /
Ganssen variant. This is the standing open-web corroboration that the Konze
surname is attested in Helmarshausen. Caveat unchanged — it is a secondary
compiled index, not the original register, so it corroborates context only and
does not move any status. (The Heisebeck OSB register data point from Session
113 also re-checked out: no Konze/Gansen surname there — carried, not re-fetched
this pass.)

## Changes made
- `search-coverage.html` — replaced the "Open-web recheck — 23 Jun 2026" callout
  with a **24 Jun 2026** version: states the pass ran clean (no new
  confirmation-class match, no parish status changed), leads with the
  re-verified Helmarshausen OSB register (now with the source link), and carries
  the Heisebeck OSB data point. JSON-LD `dateModified` → 2026-06-24.
  **No row, pill, or summary-strip count changed** (still 36 parishes searched ·
  20+ Carls in window · 0 with a Konze/*n-s-n surname · 1833–1841).
- `germany/helmarshausen-research-log.html` — added a "Sources checked" row
  recording the 24 Jun 2026 OSB-register re-verification (open web).

## Net result
Daily check ran clean. No confirmation-class match for a Konze-type Carl, and no
parish moved status. The standing open-web corroborations (Helmarshausen OSB has
Konze/Jungkonze; Heisebeck OSB has neither) were re-verified and folded into the
coverage callout and the Helmarshausen log.

## Still outstanding (unchanged from 23 Jun)
- Deisel core class (218836) — read via AI transcription, negative (no change).
- Not digitised / on-site Tier: Heisebeck pre-1845, Schöneberg pre-1822.
- Gated US forward-trace of the Wehmann candidate (FamilySearch/Ancestry login;
  NARA AAD "Germans to America") — not runnable unattended.
