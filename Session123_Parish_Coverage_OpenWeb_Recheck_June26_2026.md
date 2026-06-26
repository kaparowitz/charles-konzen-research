# Session 123 — Parish Search Coverage: daily open-web recheck (all parishes)

**Date:** 26 June 2026
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

## Step 0 — repo sync
`git fetch origin` + `git pull --rebase origin main`. Branch already up to date
with `origin/main` (fetch found nothing new), so the rebase would have been a
no-op; it reported "unstaged changes" only because the working tree carries
**pre-existing manual/other work** not committed by this task —
`Tier1_Search_Log_June2026.md`, `evidence/index.html`, `germany/konzen-puzzle.html`
(plus an untracked `germany/konzen-puzzle.backup_pre_cleanup_20260625.html`).
Per the task's safety rules those were **left untouched** (no reset/checkout/clean/
stash/force anywhere). Any commit this run is scoped to this session's own files
only, never `git add -A` of the whole tree.

## Tooling note
Per `CLAUDE.md` the preferred web-research tools are Nimble and Bright Data. In
this unattended sandbox neither CLI is installed (`nimble` / `bdata` not on PATH —
the sandbox resets between sessions) and the Nimble MCP only exposed its
interactive `authenticate` / `complete_authentication` step, which cannot complete
without the user. Substituted the available open-web tools (WebSearch) for this
pass, same as Sessions 111 / 113 / 116 / 121. Subscription sites (Archion,
Ancestry, FamilySearch gated records, MyHeritage, Fold3) were **not** touched —
out of scope for an automated run, per the task and `CLAUDE.md`.

## What was searched (open web)
- Konze / Kontze / Gansen / Gonsen baptism 1834–1835 + Trendelburg / Deisel /
  Hofgeismar Kirchenbuch — generic results only (GenWiki "Hessische
  Kirchenbuchbearbeitungen", Hessische Familienkunde PDFs, Trendelburg/Hofgeismar
  town & tourism pages, LAGIS). No record-level Konze-type baptism hit.
- Carl Konzen / Kontze geb. 1835 Kurhessen Auswanderer Amerika / Civil War —
  emigration-literature landing pages only (Hessisches Landesarchiv Auswanderer,
  Deutsche Auswanderer-Datenbank, LAGIS "Hessische Auswanderer"); no
  individual-level match.
- Ortsfamilienbuch / Ortssippenbuch Hofgeismar / Schöneberg / Hümme / Stammen +
  Konze/Kontze — the standing **Helmarshausen OSB** register (klauskunze.com)
  re-surfaced, plus the HFV Ortsfamilienbücher index and a klauskunze
  **Bodenfelde** OSB register. No new window-covering OFB name register; no
  Gansen/Gonsen variant.
- GEDBAS Konze/Kontze/Gansen + Hofgeismar/Trendelburg/Diemel 1830–1840 — only
  town/geography pages (Wikipedia Hofgeismar/Hümme, Trendelburg). No GEDBAS
  record-level baptism.
- Heisebeck "Candidate" **Carl Wehmann** b. ~1835 emigrant forward-trace
  (Germans-to-America / Hamburg-list landing pages) — nothing new; the trace
  remains gated (US records / NARA AAD), not runnable unattended.
- Charles Gannsen / Konzen + Battery B, 2nd Missouri Light Artillery + immigrant /
  naturalization — only the unit history already known (Wikipedia Battery B; the
  unrelated Capt. "Charles/Karl August Mann" of the same battery resurfaces, not
  our man). No individual-level open-web hit.

## Standing corroborations re-checked
- **Helmarshausen OSB** (`klauskunze.com/heikun/hel/register.htm`) — register page
  still live (re-surfaced in search). Carries **Konze** and **Jungkontz/Jungkonze**
  family numbers and **no** Gansen/Gonsen variant — the standing open-web
  corroboration that the Konze surname is attested in Helmarshausen. Secondary
  compiled index → context only; no status change.
- **Bodenfelde OSB** (`klauskunze.com/heikun/bf/…`) surfaced again as a klauskunze
  neighbour-parish register. Bodenfelde sits on the Weser just N of Gieselwerder
  but is in the Hannover church (Kirchenkreis Münden/Göttingen), **not** Kurhessen
  Kirchenkreis Hofgeismar, and produced no Konze/Gansen hit — does not warrant a
  new table row.

## New / verifiable result
**None.** No record-level Konze-type baptism, no confirmation-class match for a
Konze-type Carl, and no open-web source that moves any parish status. Every
remaining lead (confirmation registers for the residual/partial parishes; the
Wehmann US forward-trace) sits behind Archion or gated US logins — out of scope
for an unattended run.

## Changes made
- **`search-coverage.html` — unchanged.** Per the task's "nothing new" rule the
  page content was left exactly as-is (still **36** parishes searched · **24**
  confirmation registers swept · **2** substantive on-site open tasks · **0**
  Carls with a Konze/*n-s-n surname · window 1833–1841; JSON-LD `dateModified`
  left at **2026-06-25**, the date of the last substantive content change —
  the 25 Jun village-sweep update). No row, pill, or summary-strip count changed.
- No parish research log edited (no new verifiable data point to record).

## Net result
Daily check ran clean. No confirmation-class match for a Konze-type Carl, no
record-level Konze baptism on the open web, and no parish moved status. The
standing corroborations (Helmarshausen OSB has Konze/Jungkonze; Heisebeck OSB has
neither) still hold.

## Coverage check — every grouping reviewed, none missing
All five table groupings were swept. No additional Kirchenkreis Hofgeismar parish
was identified that should be added to the table — the 36-parish roster remains
complete for the widened sweep. (Bodenfelde considered and excluded: wrong
Landeskirche, no Konze hit.)

## Still outstanding (unchanged from 25 Jun)
- Deisel core class (218836) — read via AI transcription, negative (no change).
- Partial/residual confirmation leaves: Grebenstein 1851–55 (births 1840–41,
  prime 1848–50 cohort already read negative); Veckerhagen 1847/1849–54
  confirmation classes not yet read — Archion-gated, not runnable unattended.
- Not digitised / on-site Tier: Heisebeck pre-1845, Schöneberg pre-1822.
- Gated US forward-trace of the Wehmann candidate (FamilySearch/Ancestry login;
  NARA AAD "Germans to America") — not runnable unattended.
