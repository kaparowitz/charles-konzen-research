# Charles Konzen Site — Round-2 Punch List · Content Debt (27 May 2026)

**Scope.** The remaining content-and-narrative debt the Round-1 review surfaced but didn't fix. Focus is on items that finish the binding between live claims and the rigor scaffolding, and that pull good standalone research into the narrative pages where readers will find it.

**Frame.** Round 1 closed the propagation cascade and bound four flagship narrative pages to the scaffolding. This round bites into items where the *page itself* is the problem — wrong frame, missing teaching moment, or audit trail flowing only one direction.

Ranked by leverage (brokenness × ease of fix). Brokenness scores from a fresh content audit; each item names file:line and the existing prose so the fix is a 1-tool-call substitution.

---

## 1. Add errata back-links from live claims — currently the audit trail flows only outward

Errata logs every promotion and recalibration, but the live claims don't link back to their errata entries. `overview.html` has **zero** errata-anchor links inline; `key-evidence.html` has only 4; Bertha's 1880 birth on `overview.html:928` carries no errata link at all despite being a flagship recalibration.

Fix: for each load-bearing claim that has a known errata entry, append a small `(see [errata · 2026-05-XX](errata.html#er-YYYY-MM-DD-ID))` link inline. Surnames, Bertha 1880, height 5'5"/5'10", Card 4/5 recalibration, Konsen→Konzen 1890, Heitzenberger→Hitzelberger, death-date Doc A/N — each gets a back-link. The errata entry IDs already exist; you just need to spot the live claim and add the anchor.

**Brokenness 4 · effort: low (sweep pattern).**

## 2. Walk the reader through the Andreas Konze / Andreas Kontze disentanglement on a narrative page

This is one of the project's hardest reads and an exemplary piece of identity-disentanglement methodology. It exists at length in `Andreas_Konze_Identity_Disentanglement.md` (root) and on `family_pages/fam-konze.html`. But on the narrative pages — `germany-and-origins.html` mentions Andreas Konze once in a tile sub (line 1283), `konzen-puzzle.html` chart labels three Andreas nodes "A / B / C" without explaining them, and `key-evidence.html:657` gives a list of Kontzen burials without disentanglement.

Fix: add a single `<details class="research-log"><summary>How we disentangled the two Andreas Konzes</summary>...</details>` block on `germany-and-origins.html` (after the surname-pool table, before the "verdict" section). Three paragraphs: the two-figure problem, the records that distinguish them, the resolution. The disentanglement is the kind of evidence-of-process a peer reviewer most wants to see.

**Brokenness 4 · effort: medium (one new section, ~400 words).**

## 3. Turn the children's lifespan figcaption into a teaching moment

`children/index.html:399` caption names every short-lived child but never says *why* any died — Maria Josephine and Auguste both died 1890 (cholera? puerperal? tuberculosis?), Friedrich Wilhelm at sixteen months, the mother Auguste in 1896. Charles's own 1903 death is dropped without context. The current caption is just a list of names.

Fix: rewrite to three sentences. (1) Three children died young; (2) cause of death where known (cholera epidemic, tuberculosis, the period's child-mortality landscape); (3) the four who survived crossed the 1900 line and lived into the radio era. The figure becomes pedagogy instead of a key.

**Brokenness 4 · effort: low (one figcaption rewrite + sourcing for any causes).**

## 4. Rewrite the Konzen Puzzle landing lede to answer the family reader's question first

`germany/konzen-puzzle.html` opens with an audit-trail card and an "At a Glance" summary whose lede *is* technically conclusion-first — but the conclusion is phrased for a connoisseur: *"the single American attestation of the full Hessian z-form Konzen, the documented Trendelburg parish spelling since 1773"* (line 885). A family reader following the home tile "Hessian origins → Trendelburg" needs to read "*Trendelburg*" as the first proper noun, not "the full Hessian z-form."

Fix: add a 2-sentence plain-language lede above the existing card. *"Charles's family surname is concluded as Konzen (with a z), the form documented in the Trendelburg parish register from 1773 onward. The 'puzzle' is the missing specific baptism record naming Charles himself — three archival threads remain open."* Then let the connoisseur card stand.

**Brokenness 3 · effort: low.**

## 5. Add the one-sentence "two sponsors recurred" explainer to the 15/17 framing

`sponsor-reconciliation.html:266` and `people-in-the-story.html:544` both quote *"15 named sponsors / 17 sponsorship slots"* with "(two recur)" in parentheses. A family reader reading 15/17 will count their fingers and assume they've miscounted; the parenthetical is too quiet to do the work.

Fix: replace each parenthetical with one explicit sentence — e.g., *"Two people stood up at more than one baptism — Erwin Spraul for both Friedrich Wilhelm 1866 and Catharina 1872; Henriette Kreichelt for Maria Josephine 1868, Auguste 1873, and Bertha 1880 — so 15 distinct individuals filled 17 slots."* The math snaps into focus.

**Brokenness 3 · effort: low (two sentences, after a fact-check against the sponsor list).**

## 6. Add audience-routing preambles to `stories.html` and `key-evidence.html`

Both landings open with format-or-content notes, not audience cues. A family reader who clicks "Key Evidence" expecting the story will get a researcher's card deck and bounce; a researcher who lands on Stories looking for the evidence chain will skim past the storytelling.

Fix: one italic preamble per page. On `stories.html`: *"This page is for the family-reader path — nine narrative moments, told as story. For the evidence chain that supports them, see [Key Evidence]."* On `key-evidence.html`: *"This page is for the researcher path — the documents and the inferences they support. For the same material as story, see [Stories]."*

**Brokenness 3 · effort: low (two sentences).**

## 7. Extend the glossary auto-link sweep beyond the four narrative pages

The Round-1 sweep covered `germany-and-origins.html`, `charles-in-america.html`, `civil-war.html`, `key-evidence.html`. Gaps: `stories.html` has **zero** glossary-links among the audited terms. `overview.html` misses HTR (2 mentions, 0 wrapped). `methodology.html` misses Kurrentschrift (2/0) and Kirchenbuch. `evidence-index.html` misses Stammrolle and Auswanderer-Beleg.

Fix: run the same first-occurrence sweep on `stories.html`, `overview.html`, `methodology.html`, `evidence-index.html`, `abstract.html`. Same `<a class="glossary-link" href="glossary.html#g-X">term</a>` pattern.

**Brokenness 3 · effort: low (one scripted pass).**

## 8. Bind `methodology.html` to the Doc A–O crosswalk; thicken abstract + overview binding

Round-1's binding sweep gave `methodology.html` 3 negative-results, 3 bibliography, 3 errata inline links — but **zero** to `source-archive.html#doc-crosswalk`, the page that holds the project's hardest-to-reconstruct reconciliation table. `abstract.html` and `overview.html` are also thin (2 each per scaffolding page).

Fix: on `methodology.html` §6 (Naming) and §confidence add `(see [Doc A–O crosswalk](source-archive.html#doc-crosswalk))` where the Doc-A/N source-rating reasoning is invoked. On `abstract.html` and `overview.html` add one link per scaffolding page wherever a quantified claim isn't already cited.

**Brokenness 2 · effort: low.**

## 9. Tighten Foundation 2020 cards to explicit "2020 said X / we now know Y" framing

The cards on `foundation.html` are substantive (not stubs, as Round 1 implied) but they do the contrast implicitly. Reframing each card with an explicit *"2020 said X — we now know Y because Z"* sentence makes the page didactic instead of summative.

Fix: rewrite each card's lead sentence in the contrast frame, preserving the existing bullet content underneath. ~5 cards × 1 sentence each.

**Brokenness 2 · effort: low.**

## 10. Soften residual Why-Charles absolutes on Theodore Gottlob, August Derr, Dr. Hess

The Round-1 sweep caught the worst over-claim (Auguste Kreichelt). A sample of 8 more people pages turned up these mild absolutes still standing:

- `people/theodore-gottlob.html:409` — *"Charles's identification witnesses are nearly always fellow veterans rather than civilian neighbors."*
- `people/august-derr.html:407` — *"the only witness whose chain-of-command position lets him swear, under oath..."*
- `people/dr-charles-hess.html:440` — *"Dr. Hess is the only treating physician Charles names directly in the pension file."*

Each is defensible but the absolutes invite challenge. Hedge to "most" / "the only one named in the file" / "in the surviving pension correspondence."

**Brokenness 2 · effort: low.**

---

## Cross-cutting note

The Round-1 review surfaced the "scaffolding > binding" failure mode. Round 2 adds a related pattern: **good standalone research → not on the narrative pages**. The Andreas Konze disentanglement, the children's-deaths context, the two-sponsors-recur math — all are documented at length somewhere on the site, but pulled into the narrative nowhere. Each fix above is structurally: *route a research output into the path a reader actually walks.*

---

*Generated 27 May 2026 from a fresh content audit. Builds on but does not duplicate `Site_Punch_List_May27_2026.md` (Round 1, same date). Verification cap: every item names a file and a line or section; sample-verified opens on Konzen Puzzle, Foundation, sponsor-reconciliation, children/index, and four people pages.*
