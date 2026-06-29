# Session 137 — Parish Search Coverage: daily open-web recheck (all parishes)

**Date:** 28 June 2026
**Type:** Automated scheduled run (`update-parish-search-coverage`). No user present.
**Scope:** Refresh pass across **all parishes** on `search-coverage.html` — the
Konze-pool cluster (Deisel, Trendelburg, Friedrichsfeld, Stammen, Hümme,
Gottsbüren); the confirmation-register sweep incl. Tier-3 "Deissen"
(Helmarshausen, Sielen, Schöneberg, Hofgeismar town, Gudensberg, Dissen, Grifte,
Fulda, Dassen); the surrounding Kreis Hofgeismar ring (Heisebeck, Liebenau,
Lamerden, Eberschütz, Gieselwerder, Kelze, Gewissenruh, Grebenstein, Veckerhagen,
Immenhausen, Marzhausen, Bad Karlshafen, Hombressen, Haueda, Ostheim,
Niedermeiser); the wider Kreis Kassel / Weser ring (Lippoldsberg, Oedelsheim,
Vernawahlshausen, Gottstreu, Bodenfelde, Bursfelde+Glashütte, Wahmbeck); the
Catholic Westphalia border (Herstelle, Beverungen, Dalhausen); and the
toponym/family-trail tests (Freudenberg, Diez, Dies, Mainz). Priority on rows
still "Partial"/"Candidate" — above all the **Gieselwerder Kuntze/Contze household
(reopened 27 Jun)** — plus a refresh pass across all rows.

## Step 0 — repo sync
`git fetch origin` ran clean; `origin/main...HEAD` reports `0  0`, i.e. local
**HEAD already equals `origin/main`** (`8d94383`), so the `--rebase` is a strict
no-op — there is nothing on the remote to reconcile and no conflict. `git pull
--rebase` would not start only because the working tree carries **pre-existing,
uncommitted work from earlier sessions/runs** (28 modified files incl.
`search-coverage.html`, plus ~10 untracked Session 124–136 logs). Per the task's
safety rules nothing was reset, checked out, cleaned, stashed, or force-pushed.
**No `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`,
or `git push --force` was run anywhere.**

## ⚠️ Environment blocker — FUSE `index.lock` (persisted git still at risk)
Unchanged from Sessions 123/129. The mounted working tree is on a FUSE
filesystem that **refuses to `unlink` `.git/index.lock`** ("Operation not
permitted", confirmed via `rm -f`). A stale 0-byte `.git/index.lock` (dated
06:10) is present and cannot be removed, and new files cannot be created inside
`.git/`, so every git **write** (`add`, `commit`, `push`) fails with
`fatal: Unable to create '.../.git/index.lock': File exists`. Read-only git
(`fetch`, `status`, `log`, `diff`, `rev-list`) works fine. This is why the
working tree has accumulated days of uncommitted Session-124–136 work well ahead
of the last commit `8d94383`. **Jed needs to clear the stale `.git/index.lock`
locally and commit the backlog** — the daily runs cannot persist their own work
until that lock is cleared. (Separate minor artefact: the mount also refuses
`unlink` on ordinary files, so a stray empty `_writetest` probe file in the
project root could not be deleted; it is harmless and can be removed locally.)

## Tooling note
Per `CLAUDE.md` the preferred web-research tool is the **Nimble Cowork
connector**. This run **Nimble was unreachable** — every `nimble_search` /
`nimble_extract` call returned "The connector's server isn't responding" across
repeated retries. Fell back to the built-in **WebSearch** plus direct
`web_fetch` of static open-web pages (same fallback posture as Sessions 121/123).
Bright Data not invoked. Subscription sites (Archion, Ancestry, FamilySearch
gated records, MyHeritage, Fold3) were **not** touched — out of scope for an
automated run, per the task and `CLAUDE.md`.

## What was searched (open web)
Focused this run's fresh effort on **two genuinely new checks** not run in prior
daily passes, both bearing on live rows, plus a breadth refresh:

1. **Gieselwerder Kuntze/Contze household (the one reopened locus).** Pulled
   Klaus Kunze's online Ortssippenbuch-Gieselwerder material:
   - **OSB Gieselwerder surname register** (`klauskunze.com/heikun/os_gi/register.htm`)
     — confirms the pool surnames **Contze, Kontze, Kuntze, Gans, Ganß** are all
     present as Gieselwerder families in the printed OSB. This corroborates the
     27 Jun "Kuntze family found" reopening, but the online register is a
     **name→page index only** (no dates), so it yields **no dated data point**
     that could move the row.
   - **"Genealogie Contze aus Gieselwerder"** (`.../familienforschung/as/contze.htm`)
     — the only Contze detail Kunze publishes online is a **1669 burial**
     (Catharina Contze, bur. 11 May 1669, ref. KB Gieselwerder) plus a 1585
     mention of an Andreas Kuntzen as a Bursfelde-cloister creditor. Confirms the
     family's deep Gieselwerder roots but is **three centuries** off the window.
     The 1830s Heinrich-Ernst-Kuntze household reconstruction still requires the
     **printed OSB pages** (book published by HeiKun-Verlag; current edition
     dated 4 May 2026) or Archion — both offline/gated.
2. **`konzengenealogy.com` rule-out (new).** Checked the dedicated "Konzen
   Genealogy" site. It traces a **different Konzen line** — Lellig (Luxembourg) /
   Herborn origins, US trees for Angela Susanna Konzen and Catherine Konzen — with
   **no Hessian Diemel-valley / Hofgeismar connection**. Eliminated on geography,
   consistent with the project's standing surname-pool conclusions. Logged as
   checked-and-unrelated.
3. **Breadth refresh** across the surname pool (Kontze/Konze/Konzen/Gansen
   emigrants), the core Deisel/Trendelburg cluster, and the **Charles Gannsen /
   Konzen + Battery B, 2nd Missouri Light Artillery** thread — only the standing
   resources surfaced (LAGIS Hessische Auswanderer, GenWiki Hofgeismar/Trendelburg,
   Hessische Familienkunde PDFs, the regimental references already known). A
   modern "Kontze" hit in Hofgeismar is a present-day physician — not relevant.
   **No new individual-level open-web record.**

LAGIS "Hessische Auswanderer" remains the one open source with individual-level
Weser/Hofgeismar Gans-pool data; Session 129 (27 Jun) did the exhaustive
`q=Gans / Kontze / Konze / Konzen / Gansen` pull and recorded a clean negative
(Weser-zone Gans cluster re-confirmed; **no Carl/Karl Gans**; zero Kontze/Konze/
Konzen/Gansen emigrants). That static result stands one day on; not re-pulled
this run as the database is unchanged and the legacy search interface adds no new
rows day-to-day.

## New / verifiable result
**None.** The Gieselwerder OSB register confirmed (but only re-confirmed) the
pool-surname presence already noted on the page; the online Contze page is a
1669 entry; konzengenealogy.com is a different family. **No data point moves any
parish status.**

## Changes made
- **`search-coverage.html` — content unchanged by this run.** Per the task's
  "nothing new" rule, no row, pill, summary-strip count, or the JSON-LD
  `dateModified` (2026-06-27) was altered. (The page already carries substantial
  uncommitted edits from the Session 124–136 runs; those were left exactly as
  found — not authored or modified here.)
- No parish research log edited (no new verifiable data point to record).
- This session log added.

## Coverage check — every grouping reviewed, none missing
All table groupings were reviewed (Konze-pool cluster · confirmation-register
sweep incl. Tier-3 · surrounding Kreis Hofgeismar ring · wider Kreis Kassel/Weser
ring incl. Gottstreu/Bodenfelde/Bursfelde/Wahmbeck · Catholic Westphalia border ·
toponym/family-trail tests). No additional Kirchenkreis Hofgeismar parish was
identified that should be added. The 40-parish roster remains complete for the
widened sweep.

## Still outstanding (unchanged)
- **Gieselwerder (one live locus):** reconstruct the Heinrich-Ernst-Kuntze
  household + cross-check Kunze's printed Gieselwerder OSB; Taufen name-index
  already shows the Kuntze/Kontze family but no Carl on a pool surname b.
  1833–41. OSB-print / Archion-gated.
- **Bursfelde+Glashütte:** register not on Archion (OSB-only / on-site); optional
  Hemeln KB 1822–1852 neighbour check.
- Minor residuals: Schöneberg Konze-vs-Ronze Kurrent read (pending Schräder),
  Oedelsheim faded K-index leaf (Bild 918), Wahmbeck other-year leaf-certs when
  OCR processes — all Archion-/offline-gated.
- Gated US forward-traces (Heisebeck "Wehmann"; the Oedelsheim 1834 Gans emigrant
  family via HStAM Best. 16 + Günther article) — not runnable unattended.

## Commit / push
Attempted the safe sequence. **Blocked** by the FUSE `.git/index.lock` (see
above) — `git add`/`commit` cannot create the index lock, so nothing could be
committed or pushed this run. **No destructive git command was used at any
point.** The new session log + the standing backlog remain uncommitted on the
working tree until Jed clears the lock locally.

## Net result
Daily check ran **clean** — no parish moved status, no new verifiable open-web
result. Two new checks this run (the Gieselwerder OSB register and the
konzengenealogy.com line) both came back corroborating-or-unrelated. The standing
picture is unchanged. Two items need Jed's attention: (1) the **FUSE
`index.lock` git blocker**, still leaving accumulated daily work uncommitted and
unpushed; (2) Nimble was down this run — if it stays down, the durable
connector may need re-authorising in Connectors.
