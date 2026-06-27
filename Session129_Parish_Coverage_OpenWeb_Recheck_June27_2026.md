# Session 129 — Parish Search Coverage: daily open-web recheck (all parishes)

**Date:** 27 June 2026
**Type:** Automated scheduled run (`update-parish-search-coverage`). No user present.
**Scope:** Refresh pass across **all parishes** on `search-coverage.html` — the
Konze-pool cluster (Deisel, Trendelburg, Friedrichsfeld, Stammen, Hümme,
Gottsbüren); the confirmation-register sweep incl. Tier-3 "Deissen"
(Helmarshausen, Sielen, Schöneberg, Hofgeismar town, Gudensberg, Dissen, Grifte,
Fulda); the surrounding Kreis Hofgeismar ring (Heisebeck, Liebenau, Lamerden,
Eberschütz, Gieselwerder, Kelze, Gewissenruh, Grebenstein, Veckerhagen,
Immenhausen, Marzhausen, Bad Karlshafen, Hombressen, Haueda, Ostheim,
Niedermeiser); the wider Kreis Kassel / Weser ring (Lippoldsberg, Oedelsheim,
Vernawahlshausen); the Catholic Westphalia border (Herstelle, Beverungen,
Dalhausen); and the toponym/family-trail tests (Freudenberg, Diez, Dies, Mainz).
Priority on rows still "Not yet", "Partial", "Queued", or "Candidate" — i.e. the
Heisebeck "Wehmann" candidate, the Fulda "Gastmann" flag, and the **Oedelsheim
Gans-family priority lead** — plus a refresh pass across all rows.

## Step 0 — repo sync
`git fetch origin` ran clean (nothing new on the remote); `HEAD` already equals
`origin/main` (`dc48ca3`), so the rebase would have been a no-op. `git pull
--rebase` could not run only because the working tree carries **pre-existing,
uncommitted work from earlier sessions/runs** (23 modified files incl.
`search-coverage.html`, plus the untracked Session 124–128 logs and several
parish research-log edits). Per the task's safety rules nothing was reset,
checked out, cleaned, stashed, or force-pushed. **No `git reset --hard`,
`git checkout -- .`, `git clean -fd`, `git stash drop`, or `git push --force`
was run anywhere.**

## ⚠️ Environment blocker — FUSE `index.lock` (persisted git is at risk)
The mounted working tree (`/sessions/.../mnt/Charles Gannsen Research`) is on a
FUSE filesystem that **intermittently refuses to `unlink` `.git/index.lock`**
("Operation not permitted", confirmed via both `rm -f` and Python `os.unlink`).
Read-only git (`status`, `fetch`, `log`, `diff`) works, but every write
operation (`add`, `commit`, `reset`) leaves a stale `index.lock` the mount then
won't delete, which blocks the next git write. This is almost certainly **why
the working tree has accumulated days of uncommitted work** (the page is well
ahead of the last commit `dc48ca3` — e.g. summary strip now reads 25 confirmation
registers swept / 5 full baptism reads / 10 baptism-index reads vs. the committed
24-swept state). Action taken this run is recorded under "Commit/push" below.

## Tooling note
Per `CLAUDE.md` the preferred web-research tool is the **Nimble Cowork
connector**, and this run it was **live and worked** (MCP `nimble_search` /
`nimble_extract`) — a change from the WebSearch-fallback runs (Sessions 121/123),
where the CLI was unavailable. Bright Data not needed this run. Subscription
sites (Archion, Ancestry, FamilySearch gated records, MyHeritage, Fold3) were
**not** touched — out of scope for an automated run, per the task and `CLAUDE.md`.

## What was searched (open web, via Nimble)
The high-value open-web target this run was **LAGIS "Hessische Auswanderer"**
(the Hessian Landesarchiv emigrant database, `lagis.hessen.de` / legacy
`lagis-hessen.de`) — the one open source that holds individual-level data on the
Weser/Hofgeismar Gans pool, and the corroborating thread behind the Oedelsheim
priority lead. Queried the emigrant index directly (legacy URL-param interface,
which still works; the new SPA ignores `?q=`):

- **`q=Gans` → 105 emigrants Hesse-wide.** Full alphabetical list pulled. The
  only entries from the **Landkreis Kassel / Weser zone** (the parishes in play)
  are exactly those already logged: **Gans, Georg Friedrich — Oedelsheim, 1834
  (id 110864)**; **Frau des Henrich Wilhelm — Heisebeck, 1840 (82731) & 1846
  (82733/93011)**; **Georg Wilhelm — Gieselwerder, 1846 (85732/108718)**;
  **Christine / Christine Charlotte / Frau des Henrich Ferdinand — Gieselwerder,
  1846 (108726/92405/92404)**. Every other "Gans" hit is a Jewish Gans family
  from Hersfeld-Rotenburg / Fulda / Schwalm-Eder / Darmstadt-Dieburg / Frankfurt
  — unrelated. **No new Weser-zone Gans emigrant surfaced.**
- **Clean verifiable NEGATIVE — no "Carl/Karl Gans" emigrant anywhere in LAGIS.**
  Alphabetically a "Gans, Carl" would fall between "Gans, Balthasar" (#6–7) and
  "Gans, Christine" (#8); the list goes straight from Balthasar to Christine with
  no Carl/Karl. This reinforces the read-evidence finding that there is no
  documented Carl Gans baptism in the window — there is likewise no Carl Gans in
  the emigration record.
- **`q=Kontze` → 0 · `q=Konze`/`q=Konzen` → 0 · `q=Gansen` → 0.** The Konze /
  Kontze / Konzen / Gansen surname pool produces **zero** Hessian emigrant
  records — consistent with every prior pass. No emigrant under the project's
  core surname.
- **Charles Gannsen / Konzen + Battery B, 2nd Missouri Light Artillery** — only
  the standard regimental references already known (NPS, Wikipedia, WikiTree,
  Civil War Archive). No individual-level open-web hit.
- **Oedelsheim Gans → North America 1834 + Günther "Hessian emigrants"
  (Niederhessen) article** — only generic German-genealogy guides; nothing online
  names the emigrant G. F. Gans's wife or three children (the competing
  "literal-Gans-from-Oedelsheim" origin thread still needs the printed Günther
  article + HStAM Best. 16 file, both offline/on-site).

## New / verifiable result
**None.** The LAGIS sweep **re-confirmed** the known Weser-zone Gans emigrant
cluster and added a clean negative (no Carl/Karl Gans; zero Kontze/Konze/Konzen/
Gansen emigrants) — but produced **no new data point that moves any parish
status**. Every live lead (Oedelsheim faded K-index + Gans-household
reconstruction; the Wehmann US forward-trace; residual/partial confirmation
leaves) sits behind Archion or gated US logins — out of scope for an unattended
run.

## Changes made
- **`search-coverage.html` — content unchanged by this run.** Per the task's
  "nothing new" rule, no row, pill, or summary-strip count was altered and the
  JSON-LD `dateModified` was left as-is. (The page already carries substantial
  uncommitted edits from the Session 124–128 runs; those were left exactly as
  found — not authored or modified here.)
- No parish research log edited (no new verifiable data point to record).
- This session log added.

## Commit / push
Attempted the safe sequence (`pull --rebase` → `add` → `commit` → `push`). See
the run summary for the exact outcome and the `index.lock` blocker status. No
destructive git command was used at any point.

## Coverage check — every grouping reviewed, none missing
All table groupings were reviewed (Konze-pool cluster · confirmation-register
sweep incl. Tier-3 · surrounding Kreis Hofgeismar ring · wider Kreis Kassel/Weser
ring · Catholic Westphalia border · toponym/family-trail tests). No additional
Kirchenkreis Hofgeismar parish was identified that should be added. The roster
remains complete for the widened sweep.

## Still outstanding (unchanged)
- **Oedelsheim (priority lead):** shuffle-aware full-window leaf sweep + Kurrent
  read of the faded K-index leaf (Bild 918); reconstruct the Gans households
  across all years in reg. 219946; Oedelsheim marriages/burials; Kunze's printed
  OSB; the HStAM Best. 16 emigration file + Günther article for the 1834
  emigrant family. All Archion-/offline-gated.
- **Heisebeck "Wehmann" candidate:** gated US forward-trace (FamilySearch/
  Ancestry login; NARA AAD "Germans to America") — not runnable unattended.
- **Fulda "Gastmann":** already resolved as **not Charles**; low-priority EV
  garrison-parish tail only.
- Residual/partial confirmation leaves (Grebenstein 1851–55; Veckerhagen tail)
  and not-digitised/on-site Tier (Heisebeck pre-1845, Schöneberg pre-1822) —
  Archion-gated, not runnable unattended.

## Net result
Daily check ran **clean** — no parish moved status. The LAGIS emigrant database
re-confirmed the Weser-zone Gans cluster and yielded a clean negative on a Carl
Gans / any Konze-pool emigrant. The standing picture is unchanged. The one item
needing Jed's attention is the **FUSE `index.lock` git blocker**, which is
leaving the accumulated daily work uncommitted and unpushed.
