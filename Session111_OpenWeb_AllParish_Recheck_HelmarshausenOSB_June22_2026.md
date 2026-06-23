# Session 111 — Open-web all-parish recheck + Helmarshausen OSB lead

**Date:** 22 June 2026
**Trigger:** Manual "run now" of the new daily scheduled task
`update-parish-search-coverage` (runs 00:00 local), broadened this session to
cover **all parishes**, not just the Diemel-valley / Konze-pool cluster.

## Scope

Open-web pass across all 36 parishes on `search-coverage.html`, all five
groupings:
- Konze-pool cluster: Deisel, Trendelburg, Friedrichsfeld, Stammen, Hümme, Gottsbüren
- Confirmation-register sweep: Helmarshausen, Sielen, Schöneberg, Hofgeismar (town), Gudensberg, Dissen, Grifte
- 1835 baptism-window sweep: Heisebeck, Liebenau, Lamerden, Eberschütz, Gieselwerder, Hofgeismar-Kelze, Gewissenruh, Grebenstein, Veckerhagen, Immenhausen, Marzhausen, Bad Karlshafen, Hombressen, Haueda, Ostheim, Niedermeiser
- Catholic Westphalia border: Herstelle, Beverungen, Dalhausen
- Toponym / family-trail tests: Freudenberg, Diez, Dies, Mainz

## Method / boundary

Open sources only. Per project rules the gated subscription images
(Archion, Ancestry, FamilySearch records, MyHeritage, Fold3) stay on Jed's
in-browser workflow and were **not** touched in this automated run. Nimble and
Bright Data CLIs were not installed in this session's sandbox and the Nimble
MCP needed an OAuth sign-in, so this manual pass used the built-in web search;
the scheduled task itself is written to prefer Nimble / Bright Data per
`CLAUDE.md`.

## Result

No new confirmation-class match for a Konze-type Carl (b. 1833–1841) surfaced
on the open web. The surname discriminator still yields **zero** *n·s·n /
Konzen matches among the dozen-plus Carls already catalogued.

**One genuine new lead — Helmarshausen Ortssippenbuch.** The published OSB
surname register (klauskunze.com/heikun/hel/register.htm) lists:
- **Konze** — family nos. 67, 96, 302, 406
- **Jungkontz** — nos. 297, 507
- **Jungkonze** — no. 468

This is an open-web corroboration that the Konze / Jungkonze surname is present
in Helmarshausen (extends the Jungkonze attestation previously held only for
Trendelburg). It is a **secondary compiled index**, not a register image — per
the project evidentiary standard, OSB entries 67/96/302/406 (and the Jungkontz/
Jungkonze nos.) must be checked against the original Helmarshausen register
before any status pill changes. Logged as a follow-up for the Helmarshausen
research log.

Other near-hits were too early or out of scope: the DDB "Kirchspiel Grifte mit
Dissen … Confirmationen" volume (Habenicht, 1999) covers **1650–1772**, well
before the 1849–1855 window; Matricula confirms Beverungen and Dalhausen are
online (already searched).

## Page changes

- `search-coverage.html`: added a dated "Open-web recheck — 22 Jun 2026"
  callout under the summary strip recording the clean all-parish pass and the
  Helmarshausen OSB lead. No status pills changed (lead needs image
  verification). Layout/structure untouched.

## Follow-ups

1. Pull Helmarshausen OSB entries 67, 96, 302, 406 (Konze) and 297/507/468
   (Jungkontz/Jungkonze) — names, dates, any Carl in the 1833–1841 window —
   and verify against the Archion Helmarshausen register.
2. Re-run once Nimble / Bright Data are authenticated in-session for fuller
   open-web coverage than the built-in search gives.
