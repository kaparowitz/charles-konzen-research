# Charles Konzen Site — Top 10 Punch List (27 May 2026)

**Scope:** scholarly rigor + content/narrative only. UX, performance, and accessibility intentionally out of scope.
**Frame:** the site already ships world-class rigor *scaffolding* (errata, negative-results, sponsor-reconciliation, Mills-grade chips, transcription provenance). The recurring failure mode is that **canonical-claim updates don't propagate to every surface**, and **claims don't bind back to the scaffolding** that supports them. Both are fixable.

Ranked by leverage (credibility risk × ease of fix).

---

## 1. Close the surname-count cascade — three flagship instances are still stale

`SITE_HEALTH_May17_2026.md` declares this bug-class closed. It isn't. Three load-bearing surfaces still carry the old count:

- **`overview.html:987`** — surname-conclusion card lists *seven* American renderings (Gonnson · Gansen · Gonsen · Konsen · Jansen · Konzen · Conson — Gonson dropped) and "5 independent scribes." Same page at lines 433 and 534 correctly says eight. **Within-page contradiction on the keystone claim.**
- **`faq.html:389`** — "Of the **eight** American spellings... recorded across **seven** attestations 1866–1896." 8 spellings vs. 7 attestations; canon elsewhere is 8/8.
- **`children/index.html` lines 104, 108, 109, 155, 257** — meta description, og:description, twitter:description, JSON-LD `description`, and visible subtitle all say "**five** distinct parish-clerk renderings." This is the OG card that every Slack/Twitter/iMessage link preview will show; it undercuts the rigor frame *before a reader even opens the page.*

Why this matters: a single peer reviewer doing exactly the kind of count-the-spellings exercise the project invites will spot the contradictions in five minutes. Once they do, the rigor argument is on the defensive.

## 2. Reconcile Freundberg vs. Freundburg — the geographic linchpin disagrees with itself

The 1862 enlistment town reading is the foundation of the Trendelburg argument. Canon across **35 pages** is **"Freundburg"** (with -burg) — including `index.html`, `civil-war.html`, `key-evidence.html`, `abstract.html`, `evidence/card-2`, `source-archive.html`, `errata.html`, `methodology.html`.

But **`germany-and-origins.html`** — the very page that walks a reader through the phonetic decoding — gives it as **"Freundberg"** (with -berg) at lines 440, 454, 459, 469. And `index.html` itself contains both spellings mixed across its 31 instances. For a project whose argument hinges on what exactly a clerk wrote, this is a critical inconsistency. One global find-and-replace plus a re-render fixes it.

## 3. Bind claims to the rigor scaffolding — inline links from narrative → negative-results, bibliography, errata

This is the single highest-leverage rigor move available because **the scaffolding already exists; only the binding is missing.** Today:

- `germany-and-origins.html` asserts "ten surrounding parishes have been worked through" without linking to `negative-results.html`.
- `key-evidence.html` Card 2 cites "5'5", fair complexion" without an inline link to `bibliography.html#military`.
- Claim pages don't link *into* errata — errata logs the promotion but the live claim doesn't say "see errata #N for promotion history."

Fix: a one-pass sweep of the four flagship narrative pages (`germany-and-origins.html`, `charles-in-america.html`, `civil-war.html`, `key-evidence.html`) adding inline `(see [negative-results audit](negative-results.html))` and bibliography anchors at every quantified or sourced claim. Pattern: every "ten parishes," every transcription quote, every confidence chip gets a link.

## 4. Resolve "Hitzelberger" vs. "Heitzenberger" — bibliography prints a working hypothesis as fact

`bibliography.html:309` names pension affiant **"John Hitzelberger."** But `people-in-the-story.html:496` calls the same witness **"John Heitzenberger → a Hitzelberger"** and explicitly says *"Specific individual identity remains open."* The filename is `people/john-heitzenberger.html`. The bibliography is asserting the working reconstruction as the attestation — exactly the bug-class SITE_HEALTH flagged as the next-pass risk.

Fix: either (a) bibliography reads "John Heitzenberger (also read as Hitzelberger; identity open — see profile)" or (b) you accept the identity as resolved across the site and rename the profile. Pick one.

## 5. Build a single Load-Bearing Claims dashboard

Today the confidence taxonomy is defined in `methodology.html` and applied as chips on individual pages. A skeptical reviewer's first question is: *"Show me, on one screen, every claim this project is willing to defend as Confirmed vs. Working, with primary source and falsification condition."* That artifact doesn't exist.

Proposed page (`claims-dashboard.html`): one table — **Claim · Confidence · Primary source · What would change it**. Seven to twelve rows: the surname conclusion, Trendelburg parish, Deisel village, 1862 enlistment identity, the 1875 *Konsen* attestation, the 16 Dec 1903 death date, etc. This is the page a BCG-certified peer reviewer would ask for first, and it's a single afternoon of work because every row already exists across the site.

## 6. Audit people-page "Why-Charles" callouts for over-claiming

The Card 4 & 5 recalibration on 25 May (errata) tightened the direct-vs-indirect distinction at the top level. The same sweep hasn't been applied to people pages. Example:

- **`people/auguste-kreichelt.html:277`** — "the only direct documentary witness to Charles's surname spelling for thirty years — every rendering of the family name in St. Louis records appears alongside Auguste's first name." False as stated: 1862 enlistment (Gannsen), 1880 census (Gonson), 1890 daughter's death (Konzen) include Charles or a child *without* Auguste in the same field. The phrasing inflates Auguste's documentary role beyond what the records support.

Fix: re-read every Why-Charles callout on the 27 Cohort A people pages against the indirect-vs-direct framework. Down-grade phrasing where the role is corroborative rather than attestational.

## 7. Pick one register per people page — family-intro OR bottom-line, not both

The May 17 docx audit asked for one rewrite per page. What shipped was **both** — every Cohort A people page now stacks a plain-language family-intro paragraph *and* a dense bottom-line citation paragraph back-to-back saying largely the same things in two registers (`people/auguste-kreichelt.html` lines 275–276 is the type specimen). It reads as the residue of competing audits.

Fix: per page, decide whether this person serves family-reader curiosity (keep family-intro, demote bottom-line to a "Researcher view" disclosure) or peer-review (keep bottom-line, demote family-intro to a one-line summary).

## 8. Auto-link glossary terms on first occurrence per page

`glossary.html` is excellent, but only `overview.html` actually inline-links to it. `charles-in-america.html`, `civil-war.html`, `key-evidence.html` use **Stammrolle**, **Auswanderer-Beleg**, **Kirchenbuch**, **HTR**, **Kurrentschrift**, **Churhessen**, **Kirchenkreis** repeatedly without the `glossary-link` anchor. Family readers never find the glossary; researchers re-look-up terms they shouldn't have to.

Fix: one Python script pass — for each glossary term, wrap first occurrence per page in `<a class="glossary-link" href="glossary.html#g-X">term</a>`. The CSS class already exists.

## 9. Surface the 1-day Doc A/Doc N death-date discrepancy where it appears

`source-archive.html` honestly logs that the death certificate (Doc A) reads **17 Dec 1903** while the parish burial register (Doc N) reads **16 Dec**. Methodology says conflicts must be flagged "explicitly, not quietly overwritten." But `overview.html:982` and the home-card on `index.html` both give "16 December" without a footnote. Only `charles-in-america.html:428` surfaces the conflict inline.

Fix: every "16 December 1903" instance should carry a small `†` linking to `source-archive.html#doc-crosswalk`, with a one-line footer note that Doc A reads the next day. This costs nothing and converts a hidden reconciliation into visible rigor.

## 10. Reconcile the "78+ / 80+ / more than eighty research sessions" tri-count — and adopt a pre-commit grep checklist

`index.html` says "78+ sessions," `negative-results.html` says "80+," `methodology.html` says "more than eighty." Three counts for the same metric across three flagship pages.

The deeper fix is process, not content: **every time a canonical metric changes, the propagation cascade strikes.** Adopt a pre-commit checklist that greps the following surfaces for any canonical claim:

```
meta name="description"     og:description     twitter:description
JSON-LD "description"       <title>            H1
alt= attributes             figure captions    <text> inside <svg>
```

This is the same surface set that left "five distinct" alive in `children/index.html` meta tags and "Freundberg" alive in `germany-and-origins.html`. A 10-line shell script run before every deploy would catch 90% of the cascade residue this audit found.

---

## Cross-cutting themes (the *why* behind the punch list)

- **Scaffolding > binding.** World-class rigor pages (negative-results, errata, sponsor-reconciliation, bibliography, source-archive) exist but the narrative pages don't link into them. Closing this gap is what would move the site from "we did the work" to "you can verify it from any claim in two clicks."
- **Propagation cascade is the project's signature failure mode.** Every canon change (7→8 surnames, Konsen→Konzen 1890, 5'10"→5'5", Bertha 1879→1880) leaves 10–20 stale instances in meta-tags, OG cards, JSON-LD, alt text, and SVG `<text>`. A pre-commit grep harness costs hours to build and saves dozens of "we already fixed that" embarrassments.
- **Dual audience handled structurally, broken at the page level.** The Stories tab, the plain-language home lede, and the glossary work. But people pages now stack *both* registers instead of choosing, and the Konzen Puzzle landing still opens with the puzzle frame instead of the conclusion-first frame a family reader needs.

---

## What I'd do first (if I had two afternoons)

**Afternoon 1 (rigor):** fixes #1, #2, #4, #9 — all of them are find-and-replace scope, all of them close known correctness bugs on the flagship pages.

**Afternoon 2 (binding):** fix #3 + start #5 — one sweep of inline links from the four big narrative pages into negative-results / bibliography / errata, and a v1 of the claims dashboard with the seven most-load-bearing claims.

The rest are higher-effort but lower-risk; #7 in particular is a judgment call best made by you per page.

---

*Generated from a read of the local file tree on 27 May 2026. Findings spot-verified at: `overview.html:987`, `faq.html:389`, `germany-and-origins.html:440,454,459,469`, `children/index.html:104,108,109,155,257`. Builds on (and does not duplicate) `SITE_HEALTH_May17_2026.md`, `Charles_Konzen_Site_Audit_May17_2026.docx`, `Charles_Konzen_Genealogy_Rigor_Audit_May17_2026.docx`, `Site_Review_May1_2026.md`, `People_Pages_Audit_May10_2026.md`.*
