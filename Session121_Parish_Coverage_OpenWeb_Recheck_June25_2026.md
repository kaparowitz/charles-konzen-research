# Session 121 — Parish Search Coverage: daily open-web recheck (all parishes)

**Date:** 25 June 2026
**Type:** Automated scheduled run (`update-parish-search-coverage`). No user present.
**Scope:** Refresh pass across **all 36 parishes** on `search-coverage.html` — the
Konze-pool cluster (Deisel, Trendelburg, Friedrichsfeld, Stammen, Hümme,
Gottsbüren), the confirmation-register sweep incl. Tier-3 "Deissen"
(Helmarshausen, Sielen, Schöneberg, Hofgeismar town, Gudensberg, Dissen, Grifte),
the 1835 baptism-window sweep (Heisebeck, Liebenau, Lamerden, Eberschütz,
Gieselwerder, Kelze, Gewissenruh, Grebenstein, Veckerhagen, Immenhausen,
Marzhausen, Bad Karlshafen, Hombressen, Haueda, Ostheim, Niedermeiser), the
Catholic Westphalia border (Herstelle, Beverungen, Dalhausen), and the
toponym/family-trail tests (Freudenberg, Diez, Dies, Mainz). Priority on rows
still "Not yet", "Partial", "Queued", or "Candidate"; refresh pass across all rows.

## Tooling note
Per `CLAUDE.md` the preferred web-research tools are Nimble and Bright Data. In
this unattended sandbox neither CLI is installed (`nimble` / `bdata` not on PATH)
and the Nimble MCP needs an interactive auth flow that cannot complete without
the user. Substituted the available open-web tools (WebSearch + web_fetch) for
this pass, same as Sessions 111 / 113 / 116. Subscription sites (Archion,
Ancestry, FamilySearch gated records, MyHeritage, Fold3) were **not** touched —
out of scope for an automated run, per the task and `CLAUDE.md`.

## What was searched (open web)
- Konze / Kontze / Gansen / Gonsen + Trendelburg / Deisel / Hofgeismar
  Kirchenbuch 1835 Taufe — generic results only (LAGIS Deisel Ortslexikon,
  GenWiki "Hessische Kirchenbuchbearbeitungen", Kirchspiel Trendelburg page,
  Hessische Familienkunde PDFs). The only "Kontze + Hofgeismar" hit remains a
  present-day gynaecologist (Tatiana/Tatjana Kontze), irrelevant.
- Konze / Kontze / Gonsen baptism 1834–1836 Kreis Hofgeismar GEDBAS — no
  record-level baptism hit; surname-database and OFB landing pages only. (Beuleke,
  *Die Hugenottenkolonie Kelze*, ZHG 69, surfaced again — context for Kelze's
  Huguenot surname pool, already reflected in the Kelze log; no Konze.)
- Ortssippenbuch / Ortsfamilienbuch Schöneberg / Hümme / Stammen / Helmarshausen
  + Konze/Kontze — the standing Helmarshausen OSB register (klauskunze.com) and
  the Taenzer Hümme/Stammen KB compilations re-surfaced; no new window-covering
  OFB name register. Schöneberg OFB still covers only pre-window decades.
- Charles Gannsen / Konzen + Battery B, 2nd Missouri Light Artillery + immigrant /
  naturalization — no individual-level open-web hit beyond the unit history
  already known.
- Heisebeck "Candidate" Carl/Charles **Wehmann** b. ~1835 emigrant forward-trace
  (Germans-to-America / Hamburg lists landing pages) — nothing new; the trace
  remains gated (US records / NARA AAD), not runnable unattended.
- FamilySearch open-tree Karl/Carl Konzen/Kontze b. 1835 Hessen/Kurhessen /
  Auswanderer — surname-collection pages only; no matching individual.
- Andreas Kontze / Mainz 1854 family-trail — no record-level hit.
- Matricula (Catholic border): Beverungen St. Johannes Bapt., Dalhausen,
  Herstelle confirmed still present in the Paderborn holdings on Matricula
  Online (already searched on prior passes); no new open index, no Konze/Gansen.

## Standing corroborations re-checked
- **Helmarshausen OSB** (`klauskunze.com/heikun/hel/register.htm`) — register
  page still live and unchanged (re-surfaced in search; full page is ~523 KB).
  It carries **Konze** and **Jungkontz/Jungkonze** family numbers and **no**
  Gansen/Gonsen variant — the standing open-web corroboration that the Konze
  surname is attested in Helmarshausen. Secondary compiled index → corroborates
  context only; no status change.
- **Heisebeck OSB** (`klauskunze.com/heikun/hei/heisebeck_register.htm`) — carried
  from Session 113 (lists **no** Konze/Gansen line; Heisebeck candidate is the
  illegitimate *Wehmann* child). Not re-fetched this pass (provenance-gated this
  run); data point unchanged.

## New / verifiable result
**None.** No record-level Konze-type baptism, no confirmation-class match for a
Konze-type Carl, and no open-web source that moves any parish status. Every
remaining lead (confirmation registers for the residual/partial parishes; the
Wehmann US forward-trace) sits behind Archion or gated US logins — out of scope
for an unattended run.

## Changes made
- **`search-coverage.html` — unchanged.** Per the task's "nothing new" rule the
  page content was left exactly as-is (still 36 parishes searched · 20
  confirmation registers swept · 2 substantive on-site open tasks · 0 Carls with
  a Konze/*n-s-n surname · window 1833–1841; JSON-LD `dateModified` left at
  2026-06-24, the date of the last substantive content change). No row, pill, or
  summary-strip count changed.
- No parish research log edited (no new verifiable data point to record).

## Net result
Daily check ran clean. No confirmation-class match for a Konze-type Carl, no
record-level Konze baptism on the open web, and no parish moved status. The
standing corroborations (Helmarshausen OSB has Konze/Jungkonze; Heisebeck OSB has
neither) still hold.

## Coverage check — every grouping reviewed, none missing
All five table groupings were swept. No additional Kirchenkreis Hofgeismar parish
was identified that should be added to the table — the 36-parish roster remains
complete for the widened sweep.

## Still outstanding (unchanged from 24 Jun)
- Deisel core class (218836) — read via AI transcription, negative (no change).
- Partial/residual confirmation leaves: Grebenstein 1854–55 (births 1840–41);
  Veckerhagen 1847/1849–54; Hombressen / Haueda / Ostheim / Niedermeiser
  confirmation classes not yet read — all Archion-gated, not runnable unattended.
- Not digitised / on-site Tier: Heisebeck pre-1845, Schöneberg pre-1822.
- Gated US forward-trace of the Wehmann candidate (FamilySearch/Ancestry login;
  NARA AAD "Germans to America") — not runnable unattended.
