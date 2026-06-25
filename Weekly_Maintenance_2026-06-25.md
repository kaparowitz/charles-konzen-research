# Weekly Maintenance — 2026-06-25

*Automated weekly maintenance + deploy pass for the Charles Gannsen Research project.
Covers research-log activity in the last 7 days (18–25 June 2026) plus a site-hygiene
audit of the deployed files. Conventions read first: `CLAUDE.md`,
`_MEMORY_Session_Conventions.md`. This run follows the 22 June and 23 June digests, so
Part 1 foregrounds the work that postdates the 23 June report (Sessions 116–121,
24–25 June) and avoids re-narrating what those digests already covered.*

---

## Part 1 — Digest of new research activity

The headline of the week is that the **German-side confirmation-register sweep was driven
to completion**. Every remaining digitised Hofgeismar/Fritzlar confirmation register that
had only ever been read on its baptism track now has its 1847–1855 confirmation classes
(the boys born 1833–1841, bracketing Charles's 26 Jan 1835 birth) read leaf-by-leaf — all
negative for a Konze-pool *Carl*. With this, the digitised confirmation corpus for Charles's
birth window is saturated-negative, and the live search is correctly pointed at the
emigration side and the offline/undigitised parish gaps. A daily open-web recheck across all
36 parishes (Sessions 116, 121) surfaced no new digitisations.

### German-side (confirmation-register completion wave, Sessions 116–121)

- **Five parishes closed on the confirmation track on 24 June (Session 117 batch):**
  Eberschütz (reg. 218884 — 1841-tail / 1855–56 classes read in full, window now closed
  leaf-by-leaf; `Session117_Eberschuetz_1841Tail_Closure_June24_2026.md`), Gieselwerder /
  Oberweser (reg. 219013, 1847–1855 swept; `Session117_Gieselwerder_219013_…md`),
  Hofgeismar-Kelze (reg. 219634, combined volume — a tight French-Huguenot-colony surname
  pool, no Konze; `Session117_Kelze_219634_…md`), Liebenau (reg. 219742 — prime 1849/1850
  leaves re-read and certified; `Session117_Liebenau_…md`), and Helmarshausen (reg. 219208 —
  documentation reconciliation: the substantive 1848–1855 read was already done in Session
  109; the per-parish log was simply brought up to date; `Session117_Helmarshausen_…Reconciled_…md`).
- **Lamerden CONFIRMED complete (Session 118).** Reg. 219673 (dual-filmed) read 1846–1855
  across both filmings = negative; 1847 is a genuine gap-year (no class). Now eliminated on
  both baptism and confirmation tracks. `Session118_Lamerden_Confirmation_Sweep_Complete_June24_2026.md`.
- **Two genuinely unswept parishes read and eliminated (Sessions 119–120):** Grebenstein
  (reg. 219097 — the single most probative 1849 class holds *no Carl at all and no Konze-pool
  surname*; decisive negative) and Immenhausen (reg. 219580, 1847–1855 negative on the
  confirmation track to match the negative 1835 baptisms).
  `Session119_Grebenstein_219097_…md`, `Session120_Immenhausen_219580_…md`.
- **Marzhausen and Bad Karlshafen (both confessions)** were also closed on the confirmation
  track in this window per the memory-file register notes (181895; 218674 Lutheran + 218707
  Reformed) — surname pools tight and local, no Konze anywhere.
- **All-parish open-web recheck (Sessions 116, 121).** Scheduled open-web passes across all 36
  parishes found no new Archion digitisations or open-web records; subscription sites remain
  the gating workflow. Tooling note carried in both logs: in the unattended sandbox the Nimble
  and Bright Data CLIs are not on PATH, so these passes used WebSearch + web_fetch.

### US-side / emigration

- **Deisel Konze emigration thread (traced 22 June; `Konze_Deisel_Emigrants_Trace_June22_2026.md`).**
  Following Lüdicke's "KONZE, 2 Brüder" note, a FamilySearch Tree + records sweep documents
  ≥4 Konze men born in Deisel who emigrated to America in the 1880s–1900s (best fit for the
  "2 Brüder" = an NYC pair; others to Milwaukee/Chicago). They are collateral kin a generation
  younger than Charles and none went to St. Louis — so not his household, but direct
  documentation that the Deisel Konze clan demonstrably emigrated. *(Flagged in the 23 June
  report as well; see "fold into site" below.)*

### DNA / correspondence

- No new DNA logs this week. Correspondence: standing First-Families application and Kassel /
  Marburg archive-request drafts (`Archive_Letters_To_Send_June21_2026.md`,
  `Kassel_Archive_Request_Draft_June21_2026.md`) remain queued — these are offline/by-mail
  actions awaiting Jed.

### Should be folded into the public summary pages (not yet, or worth a refresh)

- **Confirmation-track completion.** The milestone — *all digitised Hofgeismar/Fritzlar
  confirmation registers in Charles's birth window are now read and negative* — lives only in
  the session logs and the per-parish research logs. `search-coverage.html` already gained
  Confirmations / Open-task columns (commit `e8b87d9`), but a 2–3 sentence stable summary on
  `negative-results.html` (and/or the Germany overview) stating the confirmation track is
  saturated-negative would capture the milestone per the "main pages carry stable summaries"
  convention. **Flagged for Jed — this is a conclusion edit, not a safe auto-fix.**
- **Deisel Konze emigration.** The documented emigration of the Deisel Konze clan is a
  substantive finding that may warrant a short stable note on the immigration / emigration
  summary page if not already reflected there. **Flagged for Jed.**

---

## Part 2 — Site-hygiene & rigor checks

Run against the deployed file set (excluding `node_modules/`, `_archive*`, `_backup*`,
`_recovery*`, `notes/`, and the patterns in `.netlifyignore`).

| # | Check | Result | Count |
|---|-------|--------|-------|
| 1 | Broken internal links (every deployed `.html`) | **PASS** | 438 pages audited, **0** broken refs (`scripts/check_links.py`) |
| 2 | Links into non-deployed dirs (`notes/`, `_archive/`, …) | **PASS** | 0 (covered by check_links + sitemap scan) |
| 3 | Sitemap hygiene (no missing / non-deployed entries) | **PASS** | 272 `<loc>` entries; 0 missing on disk; 0 into excluded dirs |
| 4 | Stale / future dates on flagship pages | **PASS** | 0 real hits (5 apparent in `index.html`, 1 in `errata.html` — all false positives: URL-encoded filenames `%2046`, Archion image no. `2063`) |
| 5 | Rigor regression — `geb Konsen` → `geb Konzen` | **PASS** | 0 on content pages (all hits are documentary descriptions of the *past* fix in `changelog.html`/`errata.html`) |
| 6 | Rigor regression — candidate-families count | **PASS\*** | 0 on flagship pages; `13`/`21` appear only in documentary `changelog/errata/updates` (period numbers, kept). \*See Needs-review re: 13 vs 16. |
| 7 | Rigor regression — surname count "eight/seven distinct" | **PASS\*** | 0 surname-count regressions on content; only documentary hits. One content hit `germany/konzen-puzzle.html` "eight distinct **candidates**" = candidate-men metric, not surname spellings. |
| 8 | Old brand "Charles Konzen Research" on deployed pages | **PASS** | 0 in deployed `.html` (only in working `.md` notes, scripts, LICENSE/CITATION — none deployed as content) |
| 9 | Oversized deploy assets (>3 MB, not `.netlifyignore`-excluded) | **PASS** | 0 *newly added* this week. Standing large assets (pension PDF, New Madrid tour PDFs, coat-of-arms SVGs, peter_charts source PDFs) are pre-existing and legitimately referenced. |
| 10 | Feed freshness (`feed.xml`) | **N/A** | No feed generator exists in `scripts/` → skipped per task. |

**Totals: 9 PASS, 1 N/A, 0 FAIL.**

---

## Part 3 — What I fixed this run

- **Regenerated `sitemap.xml`** via `scripts/build-sitemap.py` (the project's canonical
  generator). The 272 `<loc>` set is unchanged and already hygienic (0 missing/non-deployed
  entries); the regeneration refreshes the mtime-based `<lastmod>` values (263 lines). Safe,
  mechanical refresh.

No other changes were required — links, dates, branding, and rigor-canon were all clean on
the deployed content pages, so there was nothing unambiguous-and-safe left to fix. (Per the
task's safe-fixes-only rule, I made no judgment-call or genealogical-conclusion edits.)

Note: the commit also captured the week's already-staged research work that was sitting
uncommitted in the working tree — 11 new session logs (Sessions 115–121) and ~26 modified
research-log / town / per-parish pages plus the updated `_MEMORY_Session_Conventions.md` and
`Tier1_Search_Log_June2026.md`. These are Jed's research outputs, not maintenance edits.

---

## Deploy status — ✅ LIVE on `main` (merge commit `24b901d`)

**Published.** The run is committed and deployed to `main`; Netlify will rebuild
https://charles-research.netlify.app/ (HTTP 200 at hand-off).

What happened along the way, for the record:

- **My commit:** `9272423` — "Weekly maintenance + site hygiene — 2026-06-25" (38 files).
- **Divergence:** while this run was working, a parallel session advanced `origin/main` to
  `4a73962` ("search-coverage: publish confirmation-sweep reconciliation"), changing exactly
  one file — `search-coverage.html` — to a *newer, more polished* version (16 registers + the
  At-a-glance callout) than the in-progress copy in my working tree. So `main` had diverged and
  a plain push was correctly rejected (non-fast-forward — **not** an auth problem; token is fine).
- **Environment hazard:** this sandbox's working folder is a FUSE mount that **cannot delete
  files** (only rename) and was intermittently **corrupting working-tree files** (stripping
  lines) during git's lock-heavy merge machinery. The committed objects and the remote were
  never affected.
- **How it was resolved safely:** rather than risk a working-tree merge, I built the merge
  **entirely from the intact object store** using git plumbing with a temporary index on the
  sandbox-local `/tmp` (never touching the corrupted working tree): loaded `9272423`'s tree,
  swapped in `origin/main`'s authoritative `search-coverage.html` blob, and wrote merge commit
  **`24b901d`** with both parents (`9272423` + `4a73962`). Integrity was verified from the
  object store (all files full length; `search-coverage.html` = remote's version; report and
  session logs present) **before** pushing. The push was a clean fast-forward
  `4a73962..24b901d`. The temporary `auto/weekly-maintenance-2026-06-25` side branch (a
  belt-and-braces backup) was deleted after the merge landed.

**Two housekeeping notes for Jed (do these from a healthy git environment / a fresh session):**

1. **This session's local working tree is corrupted** by the FUSE environment (many files lost
   a few lines). The git *history* and the *remote* are clean. Before doing any local work,
   refresh the tree: `git fetch origin && git reset --hard origin/main`.
2. **Leftover junk in `.git/`** (files named `zz_*`, `*.zzlk_*`, `*.moved.*`, `probe_*`,
   `index.lock.stale`) couldn't be deleted from the sandbox (FUSE blocks unlink). They sit
   outside `refs/` and `objects/` so git ignores them, but you can `rm` them from a normal shell.

---

## Part 4 — Needs Jed's review

1. **Canon number drift between the task spec and the memory file.** This maintenance task's
   built-in rigor list names the canonical candidate-family count as **13** and the surname
   count as **"eight distinct."** But `_MEMORY_Session_Conventions.md` (updated 24 June) now
   states the canon is **16 candidate families** and **"nine distinct" American spellings**
   (Gould's 1895 "Gannsen" added the 9th). I treated the **memory file as authoritative** for
   this run. Flagging so the two can be reconciled — and so a guard can be added (see #2).
2. **No guard for the 16-families canon.** `scripts/check_canon.sh` guards surname-count
   regressions (and currently encodes the 9-spelling canon) but has **no check** for a stale
   "13 candidate families" appearing as current fact. None do today, but a guard line would
   prevent future drift. (Also: `check_canon.sh` timed out in this sandbox on the full tree —
   worth a look at its scan scope.)
3. **`germany/konzen-puzzle.html` — "eight distinct candidates."** Confirm this is the
   candidate-*men* metric (8 candidates, 6 eliminated, 2 inconclusive) and not an out-of-date
   surname-spelling count. It reads as the former and was left untouched.
4. **Fold-into-site items (Part 1):** (a) a stable 2–3 sentence "confirmation track now
   saturated-negative" summary on `negative-results.html` / Germany overview; (b) a short note
   on the documented Deisel Konze emigration on the immigration summary page. Both are
   conclusion edits and were left for Jed per the main-pages-carry-summaries convention.
5. **Standing oversized assets (informational).** `peter_charts/` holds several 3–8 MB source
   PDFs and a 7.6 MB combined-register PDF that ship to production. None are new this week and
   all are legitimate source documents, but if page-weight matters they could be candidates for
   a future compression pass.
