# Weekly Maintenance — 2026-06-23

*Automated weekly pass for the Charles Gannsen Research project. Covers research-log
activity in the last 7 days (16–23 June 2026) plus a site-hygiene audit of the deployed
files. Conventions read first: `CLAUDE.md`, `_MEMORY_Session_Conventions.md`. This run
falls shortly after the 22 June digest (UTC date rollover), so Part 1 foregrounds the
work that postdates that digest and avoids re-narrating what it already covered. The
site-hygiene fixes were **committed** (`2566a15`); the **push to GitHub could not be
completed in this run** — see the run summary at the end.*

---

## Part 1 — Digest of new research activity

The German-side confirmation-register sweep was pushed essentially to completion this week.
Three more parishes got dedicated confirmation reads (Gottsbüren, Sielen, and a verification
pass at Heisebeck), two more 1830s baptism registers were read leaf-by-leaf and eliminated
(Grifte, Dissen), an all-parish open-web recheck surfaced one new secondary lead
(Helmarshausen Ortssippenbuch), and the Friedrichsfeld "Lüdicke 2 Brüder" thread was traced
all the way into US records — documenting, with named and dated people, that the Deisel Konze
clan demonstrably emigrated to America. The week's strongest single candidate (the Heisebeck
illegitimate Carl, surfaced 21 June) had its reading verified and its non-confirmation
corroborated live. Net effect: the digitised Hofgeismar/Fritzlar confirmation registers are
now saturated-negative for a Konze-pool Carl, and the live search is correctly pointed at the
emigration side and the offline gaps.

### German-side

- **Heisebeck candidate — reading VERIFIED, non-confirmation CORROBORATED (Session 110,
  live Archion).** Register 219175 (Heisebeck Taufen 1830–1887), image 1256 entry 76,
  permalink `/p/34e1ddfe6e/`, re-read at high zoom signed in as Jed: **Carl Friedrich
  August, geb. Wehmann, born 29 Jan 1835** (baptized 8 Feb 1835), illegitimate, mother
  Dorothea Henriette Charlotte Wehmann, **remarks column confirmed BLANK** (the row above
  reads "confirmirt 1849", so a blank cell means no Heisebeck confirmation). The Heisebeck
  confirmation register 219172 b.1835–36 cohort was read in full — no Carl Friedrich August
  Wehmann — corroborating an early departure. US open-web forward-trace of a Carl/Charles
  Wehmann b. ~1835 was negative/inconclusive; the free **NARA AAD "Germans to America"
  index has never been run on the *Wehmann* surname** (recommended next step). Still a
  **candidate, not a confirmed identity** (29 Jan vs Charles's 26 Jan; surname Wehmann, not
  Gannsen/Konze). *(`Session110_Heisebeck_Followups_Entry76_Verified_Confirmation_Absence_June22_2026.md`)*
- **Gottsbüren confirmation sweep (Session 100, live Archion).** Gottsbüren keeps a separate
  Konfirmationen 1831–1932 book — register **219046** — distinct from the Taufen book the
  project had been citing. Classes 1848–1852 read with per-class Archion permalinks minted;
  the prime 1849 and 1850 classes (the cohort for a boy born Jan 1835) read in full. ~10
  Carls across the classes, **none on a Konze-pool / *n-s-n* surname**. Upgrades Gottsbüren
  from "cleared on BMD books alone" to "confirmation register also read, prime window
  saturated." Register 219046's shuffle/duplicate calibration + permalink recipe added to the
  memory file. *(`Session100_Gottsbueren_Confirmation_Sweep_June22_2026.md`)*
- **Sielen confirmation sweep (Session 112, live Archion).** Register **220039**, classes
  1846–1854 (births ~1831–1840) read with forced-redraw calibration (the apparent "shuffle"
  was a stale-canvas artifact; the candidate window is actually clean and sequential, 2 Seiten
  per image). **The anchor-core classes 1848/1849/1850 contain no Carl at all.** Three Carls
  appear in 1853–1854 — Carl Ludwig Bößler (b.1839), Heinrich Carl Storch (b.1840), Carl
  Ludwig [Stein] (b.1840) — all local surnames, none matching. This **corrects** the earlier
  tentative "Carl Ludwig Basser" record and adds two newly-found (non-matching) Carls;
  strengthens the ELIMINATED verdict. Three permalinks minted. *(`Session112_Sielen_220039_Confirmation_Sweep_June22_2026.md`)*
- **Two more baptism registers read leaf-by-leaf and ELIMINATED (memory-file calibrations,
  22 Jun).** **Grifte** (Taufen 1830–1883, reg. 253444): full 1833–1841 window read every
  child-name column — negative for Charles; the only "Carl" was a 3rd-given-name on a
  non-matching local surname. **Dissen** (Taufen 1830–1924, reg. 253403): full 1834–1841
  window (~110 baptisms) — no male Carl/Karl at all. Both have new chronology maps + permalink
  recipes in `_MEMORY_Session_Conventions.md`; detail in `germany/grifte-research-log.html`
  and `germany/dissen-research-log.html`.
- **All-parish open-web recheck (Session 111).** Manual run of the new daily
  `update-parish-search-coverage` task, broadened to all 36 parishes across all five groupings.
  No new confirmation-class match surfaced. **One genuine new lead:** the published
  **Helmarshausen Ortssippenbuch** surname register lists Konze (family nos. 67, 96, 302, 406),
  Jungkontz (297, 507) and Jungkonze (468) — open-web corroboration that the Konze/Jungkonze
  surname is present in Helmarshausen (extends the Jungkonze attestation beyond Trendelburg).
  It is a **secondary compiled index** — per the project standard, the OSB entries must be
  checked against the original Helmarshausen register before any status changes. *(Note: this
  manual run used the built-in web search; Nimble/Bright Data CLIs were not installed in-session
  and the Nimble MCP wanted an OAuth sign-in.)* *(`Session111_OpenWeb_AllParish_Recheck_HelmarshausenOSB_June22_2026.md`)*
- **★ Lüdicke "KONZE, 2 Brüder" traced into US records (Session 109 addendum +
  `Konze_Deisel_Emigrants_Trace_June22_2026.md`).** Following Lüdicke's *Verschwunden ist
  der Strand…* p. 89 roster line (two Konze brothers, Deisel → USA, post-1876, undated), a
  FamilySearch Tree + Historical-Records sweep (logged in as Jed) documents **≥4 Deisel-born
  Konze men who emigrated** in the 1880s–1900s:
  - **Best fit for the "2 Brüder":** Heinrich Philipp Konze (b. 1 Jul 1876 Deisel → Manhattan;
    m. 1898, naturalized 1906 Queens, d. ~1929 NYC) and **Friedrich Ludwig "Frederick" Konze**
    (b. 20 Jan 1887 Deisel → NYC; WWI draft, naturalizations 1919/1925, d. 1977) — both sons of
    Ludwig Theodor Konze × Maria Christiane Schaefer.
  - Plus **Philipp Ludwig Konze** (b.1871; ship *Trave*, Bremen, 14 Aug 1889 → Milwaukee →
    naturalized 1896 Jersey City → Chicago tailor 1900) and **Carl Konze** (b.1881 → m. 1923
    Manhattan).
  - **Relevance, stated carefully:** confirms the Deisel-Konze → America migration the whole
    Charles hypothesis rests on, now with named/dated individuals — **but none is Charles, his
    child, or his sibling** (born 1871–1887 vs Charles 1835; settled NYC/Milwaukee/Chicago, not
    St. Louis). Collateral kin; circumstantial reinforcement, **no direct documentary bridge**.
    A recurring emigrant **"Carl/Charles" forename** rode with the line. **Highest-value next
    step: targeted Y-DNA** between a living descendant of these emigrants and a Charles
    descendant. One data caveat flagged for an Archion check: the FS Tree gives father Ludwig
    Theodor Konze an internally impossible 1839–1870 lifespan against children born 1874–1889.
- **Tier-1 "any Carl, 1833–1841" widened re-scan** (`Tier1_Search_Log_June2026.md`, updated
  through 22 Jun): the residual live confirmation reads (Helmarshausen, Sielen, Hümme,
  Gudensberg, Gottsbüren) are appended as the Session 10 entry with per-class permalinks. The
  surname discriminator still yields **zero** *n·s·n / Konzen matches** among the dozen-plus
  Carls catalogued.

### US-side

- The US trail this week was driven almost entirely through the German-emigration lens (the
  Deisel-Konze emigrant chain above). The actionable untapped US leads are unchanged from the
  22 June digest: the **Missouri probate card index** (Charles d. 1903 estate; the
  low-confidence "Conson, James & Sophie" StLGS probate entry) and the **NARA AAD "Wehmann"**
  surname search newly identified in Session 110.

### DNA

- No new DNA pull this week (the AutoClusters export remains dated 7 June). The **Y-DNA result
  continues to keep the illegitimate-birth scenario live** — the reason the Heisebeck Wehmann
  Carl is treated as the strongest single candidate rather than dismissed, and the reason a
  **targeted Y-DNA test against the documented Deisel-Konze emigrant descendants** is now the
  single highest-value next step on the German side.

### Correspondence

- Unchanged from the 22 June digest and still **waiting on Jed to send**: the two finished
  archive letters (`Archive_Letters_To_Send_June21_2026.md` — Landeskirchliches Archiv Kassel
  for the Trendelburg E1 Eheprotokollbuch/Zivilstandsregister not on Archion, and the HStAM
  Marburg Stammrolle/Auswanderer inquiry), the **First Families of St. Louis** application
  draft, and the queued items for **Jim's September archive trip** (Schöneberg pre-1822
  registers; the jumble-blocked Schöneberg 1849–50 confirmation leaf, reg. 220012 S.18–20).

### Folding into the public summary pages (per the memory-file rule)

This week's work folded correctly into the detail layer: the Gottsbüren, Sielen, Heisebeck,
Grifte and Dissen findings reached their per-parish research logs, `search-coverage.html`
gained the dated open-web-recheck callout, and the Friedrichsfeld log gained the "2 Brüder
traced" section. The Heisebeck-candidate placement is unchanged from last week's note — it
sits on `open-questions.html`, `negative-results.html`, `errata.html`, and the parish map, but
**not on the home page, `abstract.html`, or `latest-findings.html`**. That remains a content
judgment call carried forward to "Needs your decision" (elevating a still-open candidate to
the home summary).

---

## Part 2 — Site-hygiene checks

Scope: deployed files only — excludes `node_modules/`, `_archive*`, `_backup*`, `_recovery*`,
`notes/`, and everything else in `.netlifyignore`. `notes_view/` (the deployed HTML mirror) is
treated as deployed.

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Broken internal links | **PASS** | `scripts/check_links.py`: 438 pages audited, 0 broken refs (re-run after all edits). |
| 2 | Sitemap hygiene | **FAIL → FIXED** | Two problems found and fixed (see below): the **generator script `build-sitemap.py` hard-coded a stale domain** (`charles-konzen-research.netlify.app`) — running it would have regressed the live sitemap's domain — and it **under-excluded**, so it pulled in non-deployed `_recovery_` and `*.backup_*` artifacts. After fixing both, the sitemap was regenerated: now `charles-research.netlify.app` throughout, **272 URLs** (64 net-new public pages incl. the 36 `germany/*-research-log.html` parish logs and the new `towns/*` pages), 0 junk entries, 0 removed pages, XML well-formed, every `<loc>` resolves on disk. |
| 3 | Feed freshness | **STALE → decision** | `feed.xml` `<updated>` is **2026-05-17** — over a month behind a very active June. **No feed-generator script exists** in `scripts/`, and adding a month of entries is a content task, so this is routed to "Needs your decision" rather than hand-edited. |
| 4 | Stale / future dates | **PASS** | No future ISO dates (2026-07+/2027) and no impossible months/days on flagship pages (`index.html`, `abstract.html`, `latest-findings.html`, `open-questions.html`, `errata.html`, `changelog.html`). |
| 5 | Count-canon consistency | **FAIL → FIXED** | Candidate-family count: canon is now **16** (per `_MEMORY_Session_Conventions.md`, the `negative-results.html` roster "Sixteen…", `candidate-funnel.svg` "16 families investigated", and `index.html`'s own funnel *caption*). Two stale **"13 families investigated"** funnel **titles** survived the June 13→16 reconciliation — `index.html` (contradicting its own caption and SVG in the same `<figure>`) and `visualize.html`. **Both corrected to 16.** Surname canon ("nine distinct American spellings") is consistent across flagship pages — no action. |
| 6 | Oversized new deploy assets | **PASS (1 → decision)** | One file >3 MB added in the last 7 days: `peter_charts/Rabus_JohannPhilipp_1736_Bergen_GeburtsTaufzeugnis.pdf` (3.5 MB), **not referenced by any deployed HTML** and `peter_charts/` is not blanket-ignored → routed to decision (link it, move it, or `.netlifyignore` it). md5 not checked for duplication. |

**Tally: 6 checks — 4 pass, 2 fixed in place; 3 items routed to "needs your decision".**

---

## What I fixed this run

1. **`scripts/build-sitemap.py` — stale generator domain.** Changed `BASE` from
   `https://charles-konzen-research.netlify.app` to `https://charles-research.netlify.app`
   (the live domain used by the deployed `sitemap.xml`, `robots.txt`, `feed.xml`, and every
   canonical/`og:`/JSON-LD URL on the site). This was a latent regression: the script would
   have rewritten the whole sitemap to the wrong domain on its next run.
2. **`scripts/build-sitemap.py` — exclusion gaps.** Added `_recovery_20260608/` / `_recovery`
   to `SKIP_PREFIXES` and a `.backup_` filename filter, mirroring `.netlifyignore`
   (`_recovery_20260608/`, `**/*.backup_*`). Without this, the regenerated sitemap listed
   non-deployed recovery/backup snapshots — URLs that 404 for crawlers.
3. **`sitemap.xml` — regenerated.** Correct domain, 272 URLs, +64 legitimate public pages
   (36 parish logs + town pages + `interactive-name-trail.html`), 0 junk, 0 removals,
   well-formed, all `<loc>` paths verified present on disk.
4. **`index.html` — stale count.** Funnel title "13 families investigated" → "16 families
   investigated" (it contradicted its own figcaption and the SVG it captions).
5. **`visualize.html` — stale count.** Funnel `<h2>` "13 families investigated" → "16 families
   investigated" (same `candidate-funnel.svg`, same canon).

All edits are site-hygiene only — no genealogical conclusions were changed. Both count fixes
align stale display strings to the already-documented canon (16) and to the authoritative
`negative-results.html` roster; nothing substantive was reinterpreted.

---

## Needs your decision

1. **Residual stale domain in 12 other build scripts.** Besides `build-sitemap.py` (fixed),
   twelve scripts still hard-code `charles-konzen-research.netlify.app` (`split-stories.py`,
   `build-evidence-cards.py`, `inject-analytics.py`, `extract-spa-tabs.py`,
   `inject-children-person.py`, `fill-meta.py`, `inject-article-jsonld.py`, `inject-jsonld.py`,
   `build-og-cards.py`, `inject-breadcrumbs.py`, `split-spa.py`, plus an og:image literal in
   `extract-spa-tabs.py`). These are **build-time only** (not run by `deploy.sh`), so they
   don't affect the current live site — but any of them would inject the wrong domain if
   re-run. I left them because `notes_view/HANDOFF.html` documents an intended migration to a
   **`konzenresearch.org`** custom domain, so the correct target (`charles-research.netlify.app`
   vs `konzenresearch.org`) is a call only you can make. **Decide the canonical domain, then I
   can sweep all twelve in one pass.**
2. **GitHub repo link on `claims-dashboard.html`** points to
   `github.com/jedjohnson/charles-konzen-research`. I couldn't verify the repo's actual name,
   so I left it — confirm whether that's the live repo URL or needs updating.
3. **`feed.xml` is stale** (`<updated>` 2026-05-17) and has **no generator script**. Decide
   whether you want a feed-builder added (so future weekly passes can refresh it) or whether the
   Atom feed is deprecated in favor of `changelog.html` / `updates.html`.
4. **`peter_charts/Rabus_JohannPhilipp_1736_Bergen_GeburtsTaufzeugnis.pdf` (3.5 MB, added this
   week)** — unreferenced by any deployed page. Link it from a source/evidence page, move it to
   a proper location, or add it to `.netlifyignore`.
5. **Fold the Heisebeck candidate into the public summary** (carried over from 22 June) — the
   Carl Friedrich August / Wehmann lead is on the detail pages but absent from `index.html`,
   `abstract.html`, and `latest-findings.html`. Decide whether a 2–3 sentence working-summary
   mention belongs at least on `latest-findings.html`.

---

## Run summary — committed, pushed, and deployed ✅

*(Footer updated 23 June 2026 during the manual "run now" that finished setting up
continuous deployment. The morning run's "push blocked" note below it is now resolved.)*

- **GitHub continuous deployment is now live.** The repo
  `github.com/kaparowitz/charles-konzen-research` (default branch `main`) holds the full
  site, and **Netlify auto-deploys on every push to `main`** — the CLI-only workflow is
  retired. The ~134 MB initial transfer that timed out in the morning run was completed by
  staging the large binaries to the remote in ~25 MB batches, then pointing `main` at them.
- **A repo-scoped fine-grained token** (Contents read/write, no expiry) is stored in the
  local git config so the weekly task can `git push` unattended. Revoke/rotate anytime at
  GitHub → Settings → Developer settings → Fine-grained tokens.
- **Privacy guard:** raw DNA match exports (`*Chromosome_Browser*`, Family Finder / Y-DNA /
  STR / shared-segment CSVs), the GEDCOM (`*.ged`), AutoClusters, and stray installers/
  backups are now `.gitignore`d so they are never published to the public repo.
- **This run published Jed's pending site edit** — the "Start here" dropdown was simplified
  in the shared nav source (`assets/site-nav.html`) and across all pages; that change had
  been sitting uncommitted and is now committed and deployed.
- **Hygiene audit re-confirmed clean:** sitemap has 0 entries pointing to missing files;
  the "eight distinct" / "13 candidate families" / "geb Konsen" grep hits are all legitimate
  in context (the Konze paternity-chart count, and documentary `changelog`/`errata`/`updates`
  entries that intentionally retain period numbers) — no unsafe auto-fixes were made.

*The genealogical "needs your decision" items above were left untouched.*
