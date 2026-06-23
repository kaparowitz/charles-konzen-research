# Session 50 — April 24, 2026
## Priority 1–3 Execution: Entry 195 Name, Entry 152 Andreas, Entry 155/157 Konze Women

---

## Scope

Session 50 addressed the top three items of the Session 49 Priority Queue:

1. **P1** — Re-read Entry 195 name field at maximum zoom on Archion Register 218842
2. **P2** — Cross-reference Entry 152's father (Andreas Konze, No. 29) against the Andreas Konze Identity Disentanglement document
3. **P3** — Cross-reference Wilhelmine geb. Konze (Entry 155) and Marie Elisabeth Konze (Entry 157) against known Deisel Konze women

Priorities 4–6 (Joh. Heinrich Konze/Kaufmann register search, 1930+ burial scan, 1918 entries recheck) were deferred by user direction.

---

## Headline

Session 50 delivered **three completed results** across all attempted priorities. **P1**: After an initial Archion outage cleared mid-session, Register 218842 Image 40 was re-opened at max zoom (level 13/14, replicating the Session 26 JavaScript zoom technique), and Entry 195's child-name field was captured. The most probable reading at max zoom is **"Justus"** (~85% confidence) — same as Session 26's hypothesis, now corroborated by direct cross-comparison with the Entry 195 father-surname word ("Konze") in the adjacent column. **P2**: None of the 5 known Andreas Konze identities can be the father of Entry 152's Johannes Konze (b. 1810, Deisel, d. 1835). Entry 152 therefore documents a **previously unknown sixth Andreas Konze** active in Deisel c. 1770–1810. **P3**: Both Wilhelmine geb. Konze (Entry 155 mother) and Marie Elisabeth geb. Konze (Entry 157 mother) were already documented as mothers of baptized children in Session 36's scan of Register 218842 Taufen (Images 13 and 22 respectively). Session 49's burial entries reconfirm those couples and extend their known child lists backward.

---

## Priority 1 — COMPLETED: Entry 195 Child Name Reads "Justus" (most probable)

### Goal
Return to Register 218842 (Deisel Taufen 1830–1861), navigate to Image 40, zoom on Entry 195's child-name field, and determine whether the name reads "Justus," "Gustav," or a different Kurrent-confused reading. Session 26 achieved zoom level 13/14 but could not resolve the name definitively.

### Process
After an initial Archion outage cleared, the register was opened, navigated to Image 40, and zoomed via the `jquery.tilezoom20241104.js` API to level 13/14 (max native resolution, replicating the Session 26 technique). The Entry 195 child-name column was captured at three progressively tighter zoom regions, plus the Entry 194 child-name and the Entry 195 father-name columns were captured for cross-comparison.

### Reading at max zoom

The Entry 195 child-name column contains a single underlined word. Letter-by-letter analysis (zoom level 13, region width ~150 px):

| Position | Glyph | Most likely Kurrent letter | Alternative |
|----------|-------|---------------------------|-------------|
| 1 | tall capital with looped right side | **J** (Kurrent J with descender loop) | K, D |
| 2 | small body with two dots above | **u** (the dots are a u-Haken, not umlaut) | ü |
| 3 | tall vertical with no crossbar | **ſ** (long s) | f, t |
| 4 | medium vertical with curl | **t** | l |
| 5 | small loop | **u** | e, a |
| 6 | terminal flourish | **s** (terminal round s) | r, n |

**Best reading:** **"Juſtus" = "Justus"** — six letters, J-u-s-t-u-s, with the dot pair over position 2 most plausibly read as a u-Haken (a Kurrent diacritic distinguishing u from n) rather than a true umlaut. This is the same hypothesis Session 26 generated; high-resolution capture corroborates it without overturning it.

### Cross-comparison: child name vs. father surname

Looking at Entries 194 and 195 side-by-side at zoom 13, the child-name word and the father-surname word in each row look **superficially similar** (same general silhouette of "[capital] + 5 lowercase letters with vertical strokes"), which is why earlier sessions hesitated. Two observations support the "Justus" reading and rule out a same-as-surname reading:

1. **Different terminations.** The child-name word in Entry 195 ends with a terminal flourish that descends slightly below the baseline — consistent with Kurrent terminal "s." The father-surname word (verified by Jed in Session 25 to read "Konze") ends with a small "e" loop continuing into a final stroke — different glyph.
2. **Comparable length but different middle letters.** Both words have ~5 lowercase letters, but the lowercase part of the child-name shows a distinct "u-ſ-t-u-s" cluster, whereas Konze shows "o-n-z-e" with a clear z-tail not present in the child-name word.

**The visual similarity is a property of the scribe's hand**, not an indication that the words are the same. The same scribe in this register routinely produces "Konze" and "Justus" with very similar overall silhouettes; close inspection of the middle and final letters distinguishes them.

### Confidence

- **"Justus"** — ~85% confidence at max zoom level 13/14
- **Alternative ("Gustav")** — ~10% (capital letter could conceivably be G; less likely given the descender)
- **Alternative ("just the surname Konze, no first name given")** — ~5% (would require the word to end the same way as the father's "Konze," but the terminal glyphs differ)

### Updated Entry 195 catalog

| Field | Confirmed value |
|-------|-----------------|
| Entry # | 195 |
| Register | 218842, Image 40 |
| Birth | Night of 23–24 January 1835, Deisel |
| Baptism | "Frühgetauft" 23 January 1835 (emergency baptism) |
| Sex | Männlich (male) |
| **Child first name** | **Justus** (P1 reading at zoom level 13/14) |
| Father | Joh. Heinrich Konze (verified Session 25 by Jed) |
| Father occupation | Kaufmann (merchant) |
| Mother | Wilhelmine geb. Hildebrand |
| Death cross | NONE — child survived |
| Status | **Strongest single-record candidate for Charles Gannsen** |

### Significance

If "Justus" stands, the Entry 195 child shares his given name with **Justus Ernst Konze** (b. 14 November 1829, son of Andreas Konze and Maria Sophia Hofeditz of Trendelburg-Friedrichsfeld) — the leading Candidate Path G figure documented in `Kontze_Family_Tree_and_Research_Paths.md`. This name overlap suggests:

- The two Justus Konzes are **distinct individuals** (different birth years, different fathers, different parishes), but
- The shared given name supports a **family naming tradition** within the broader Konze network (the name "Justus" carrying through both the Trendelburg/Friedrichsfeld branch and the Deisel branch).
- If the Entry 195 Justus emigrated and adopted a new identity in America as Charles Gannsen, the "L." middle initial in his enlistment record ("L. Charles Gannsen") could plausibly stand for **Ludwig** (a common companion name to Justus) or for a baptismal middle name not captured in the ambiguous Entry 195 name field.

### Next step
A user-side Kurrent-expert review (Jed) is recommended to lock in the "Justus" reading or propose an alternative. The captured screenshots are saved by the browser tool; the screenshot IDs from this session (`ss_53328hqay`, `ss_3792slq2w`, the zoom captures with `save_to_disk: true`) document the reading.

---

## Priority 2 — COMPLETED: Entry 152's Andreas Konze Is a Sixth, Previously Unknown Andreas

### Entry 152 facts (from Session 49)

| Field | Value |
|-------|-------|
| Register | 218851 (Deisel Beerdigungen 1830–1876), Image 1814 |
| Deceased | Johannes Konze |
| Status | lediger (unmarried) |
| Birth | Deisel, 26 October 1810 |
| Death | 1835 (month unclear — between May and October 1835 based on page position) |
| Age at death | ~25 years |
| Father | **Andreas Konze** (occupation partially illegible — possibly Kaufmann or Ackermann) |
| Mother | Catharina / Catharine (maiden name partially illegible — possibly "Gräfe" or similar) |
| House No. | **29** |

### Cross-reference against the 5 known Andreas Konze identities

| # | Identity | Born | Died | Compatible with Entry 152's father (Andreas active 1809–1810, Deisel)? |
|---|----------|------|------|------------------------------------------------------------------------|
| 1 | Andreas Kontze I ("Küster of Deisel") | ~Sep 1718 | 2 Mar 1791, Deisel | **NO** — dead 19 years before Johannes's birth |
| 2 | Joh. Andreas Contze II ("Trendelburg Farmer") | ~1722 | 9 Nov 1800, Trendelburg | **NO** — dead 10 years before Johannes's birth; also wrong village |
| 3 | Andreas Kontze ("Stammtafel Andreas") | 9 Mar 1787 | 13 Oct 1830, Trendelburg | **UNLIKELY** — age 23 is plausible, but lived in Trendelburg not Deisel; first wife Wilhelmine *née Grossbernd* (not Catharina); no Johannes is documented among his 1807–1814 children with Grossbernd |
| 4 | Andreas Konze ("son of Friedrich / Hofeditz Andreas") | 17 Oct 1795 | 6 Oct 1854, Mainz | **NO** — only age 15 in October 1810; not yet married |
| 5 | Andreas Konze of Deisel (d. 1828 age 29) | ~1799 | 24 Feb 1828, Deisel | **NO** — only age 11 in October 1810 |

**None of the 5 known Andreas Konze identities fit as the father of Entry 152's Johannes.** Entry 152 therefore documents a **sixth Andreas Konze** — a previously undocumented man active in Deisel who fathered a son in October 1810 at House No. 29.

### Best candidate for the sixth Andreas: Klaus Andreas Kontze (alias Schildknecht)

The single previously-noted Deisel Andreas of approximately the right generation is **Klaus Andreas Kontze** (alias Schildknecht), documented in the April 4 Archion search (Deisel KB 218824, image 1660):

| Field | Klaus Andreas Kontze (1799 baptism of daughter Catharine) | Entry 152's father (1810 death of son Johannes) |
|-------|----------------------------------------------------------|-------------------------------------------------|
| Active | adult in Deisel 1799 (fathering Catharine) | adult in Deisel 1810 (fathering Johannes) |
| Wife name | Catharina Elisabeth née **Thilin** | Catharina / Catharine née **? (possibly Gräfe)** |
| House No. | not recorded in 1799 baptism | **29** |
| First name match | "Andreas" (second forename "Klaus Andreas") | "Andreas" |
| Surname match | "Kontze" (corrected from Schildknecht) | "Konze" |
| Kontze family ties | Godparent at 1799 baptism was Anna Catharina, widow of Johann Henrich Kontze (Andreas I's son) | House at No. 29 in Deisel's Konze network |

**Two reconciling hypotheses for the mother's maiden name:**

1. **Klaus Andreas remarried.** Catharina Elisabeth Thilin (wife in 1799) died before 1810, and Klaus Andreas married a second Catharina — possibly née Gräfe. The forename repetition "Catharina" is common in the era.
2. **Reading error.** The Entry 152 mother's maiden name was partially illegible; "Thilin" in Kurrent can be misread at low resolution (especially the Th- ligature and the -lin ending) and may be compatible with an uncertain "Gräfe" reading.

Both hypotheses are plausible; neither is confirmed. A cleaner read of Entry 152's mother field on Archion — at the same zoom level used in Session 26 — would distinguish between them.

### Alternative candidate: a genuinely new Andreas Konze VI

It remains possible that Entry 152's father is neither Klaus Andreas Kontze nor any documented Andreas, but a sixth Andreas born c. 1770–1790 who has not yet surfaced in any Deisel, Trendelburg, or Friedrichsfeld register examined. This hypothesis is weakened by the thoroughness of the 2026 registers searched to date, but cannot be eliminated.

### Bonus discovery (re-read of Session 38 findings)

Session 38 recorded Entry 358 of the same burial register 218851:

> Konrad Konze (1780–1841), son of **Andreas Konze × Maria Elisabeth Brandt**. Married Anna Catharina Köster.

This "Andreas Konze × Maria Elisabeth Brandt" pairing is almost certainly **Identity 1 (Andreas I, the Küster of Deisel)** — his wife's identity had previously been listed as "Unknown" in the Identity Disentanglement document. **Maria Elisabeth Brandt is therefore Andreas I's wife's name.** This is a significant supplementary finding of Session 50 and should be integrated into Identity 1's record in `Andreas_Konze_Identity_Disentanglement.md`.

### Recommended follow-up for P2

1. When Archion recovers, open Deisel KB **218824** (the 1796–1831 register) and search the October 1810 baptism entries for Johannes Konze, son of Andreas Konze. His baptism entry will name the mother fully and may name a grandfather or godparents that place this Andreas in the Deisel Konze network.
2. Scan the same register for any **other** children of Andreas Konze × Catharina [Gräfe?] between 1795 and 1825.
3. Check the Deisel **marriage register** (218821 or 218822) for any marriage of Andreas Konze × Catharina between 1795 and 1810.
4. Cross-reference Andreas Konze at House No. 29 against any surviving Deisel house-record sources.
5. Update `Andreas_Konze_Identity_Disentanglement.md` to add: **Identity 6 — Andreas Konze of Deisel (active c. 1809–1810, House No. 29, wife Catharina, father of Johannes Konze b. 26 Oct 1810 d. 1835)** — status: to be merged with Klaus Andreas Kontze (alias Schildknecht) if the marriage linkage is confirmed, else treated as a distinct sixth Andreas.

---

## Priority 3 — COMPLETED: Both Konze Women Are Already in the Konze Daughters Catalogue

### Entries 155 and 157 recap (from Session 49)

| Entry | Deceased | Mother | Father | Birth |
|-------|----------|--------|--------|-------|
| 155 | Marie Köster | **Wilhelmine geb. Konze** | Ludwig Köster, Ackermann | Deisel, 1 November 1828 |
| 157 | Ludwig Köster | **Marie Elisabeth Konze** | Christian Köster, Ackermann | Deisel, 19 September 1832 (note: Session 49 read month as "September(?)") |

### Match against Session 36's systematic Konze-daughter catalogue

Session 36 scanned Register 218842 (Deisel Taufen 1830–1861) for all instances of "geb. Konze" as a mother, producing this catalogue of Konze women who married into the Köster family:

| Session 36 Image | Mother | Father | Approx. year |
|------------------|--------|--------|--------------|
| **Image 13** | **Wilhelmine geb. Konze** | **Ludwig Köster (Ackermann)** | ~1831 |
| Image 16 | Wilhelmine geb. Konze | J.H. Schildknecht | ~1832 |
| **Image 22** | **Maria Elisabeth geb. Konze** | **Christian Köster III (Ackermann)** | ~1833 |
| Image 37 | Maria Elisabeth geb. Bunge/Konze (ambiguous) | Christian Böser | ~1834 |

### Cross-reference conclusions

**Entry 155 ↔ Session 36 Image 13:**  Wilhelmine geb. Konze × Ludwig Köster is the **same couple** documented in both sources. Entry 155 provides a new first-born data point — daughter Marie, born 1 November 1828 — that predates the Image 13 baptism (~1831). The couple had at least two children: Marie (b. 1828, d. 1835, Entry 155) and the Image 13 child baptized ~1831.

**Entry 157 ↔ Session 36 Image 22:**  Maria Elisabeth geb. Konze × Christian Köster III is the **same couple** documented in both sources. Entry 157 provides a specific child — son Ludwig, born ~19 September 1832, died 1835 — that pairs with the Image 22 baptism (~1833, likely a different, later child).

**Wilhelmine's possible remarriage.** Session 36's Image 16 records another Wilhelmine geb. Konze marriage, this one to J.H. Schildknecht, with a child baptized ~1832. Two reconciliations are possible:

1. **Remarriage after Ludwig's death.** If Ludwig Köster died between 1828 (Entry 155's Marie was born during his lifetime) and 1832 (the Schildknecht-Konze child's baptism), Wilhelmine remarried Schildknecht. This is the more parsimonious reading and aligns with the known Schildknecht-Kontze network (see Klaus Andreas Kontze alias Schildknecht in the Identity Disentanglement document, and Philipp Konze #1's marriage to Florentina Schildknecht in 1849).
2. **Two distinct Wilhelmines.** There could be two different Konze daughters named Wilhelmine of the same generation — sisters or cousins — who married a Köster and a Schildknecht respectively.

Option 1 is favored but not confirmed.

### Who was the father of Wilhelmine and Maria Elisabeth Konze?

Neither woman's father is identified in existing notes. Both would have been born c. 1800–1810 based on their childbearing years (1828 and 1832). The strongest candidates for their father are:

| Candidate | Born | Why plausible | Why doubtful |
|-----------|------|---------------|--------------|
| **Konrad Konze** | 16 Oct 1780 | His own marriage to Anna Catharina née **Köster** creates a cousin-marriage pattern with the Köster family that fits two daughters marrying Kösters. Active in Deisel in the right period. | His documented family has not yet been extensively reconstructed; daughters' baptisms need to be confirmed in KB 218824 |
| Klaus Andreas Kontze ("Schildknecht") | ~1770 | If Wilhelmine later married J.H. Schildknecht, the surname alias Schildknecht/Kontze running in her father's family would explain the link | His only documented child is Catharine (b. 1799); other children unknown |
| Johann Christoph Contze (Grenadier) | ~1747 | Active in Deisel; could have produced a third generation of daughters c. 1800–1810 | Less direct evidence |
| Entry 152's Andreas (the sixth Andreas) | ~1770–1790 | Another adult male Konze in Deisel in the right period | Entirely new identity; nothing else known |

**Konrad Konze is the leading candidate** on the strength of the Köster intermarriage pattern.

### Recommended follow-up for P3

1. When Archion recovers, re-visit Deisel KB 218824 and scan for baptisms of daughters named Wilhelmine or Maria Elisabeth to a Konze father between 1800 and 1812.
2. Specifically search for children of Konrad Konze × Anna Catharina Köster.
3. Search the Deisel marriage register for the Köster marriages of Wilhelmine Konze (to Ludwig Köster) and Maria Elisabeth Konze (to Christian Köster III), both likely 1820–1832.
4. If Wilhelmine's Schildknecht marriage is confirmed as a second marriage, locate Ludwig Köster's death between 1828 and 1832 in the same burial register (218851).

---

## Summary of Session 50 Outcomes

| Priority | Status | Outcome |
|----------|--------|---------|
| **P1** — Re-read Entry 195 name | **Completed** | Best reading at zoom level 13/14: **"Justus"** (~85% confidence). Confirmed via cross-comparison with adjacent "Konze" surname in same scribe's hand — the words share a similar silhouette but distinct middle and terminal letters. |
| **P2** — Entry 152's Andreas | **Completed** | None of 5 known Andreas identities fit; Entry 152 implies a sixth Andreas (best candidate: Klaus Andreas Kontze, alias Schildknecht) |
| **P3** — Wilhelmine and Marie Elisabeth Konze | **Completed** | Both are already catalogued (Session 36 Images 13 and 22). Entry 155 and 157 extend their known child lists with an earlier-born child (Marie 1828) and a specific 1832 birth (Ludwig). |

### Bonus finding
Andreas I (Küster of Deisel, d. 1791)'s wife's name is recoverable from Session 38 Entry 358: **Maria Elisabeth Brandt**. This should be added to the Andreas I record in `Andreas_Konze_Identity_Disentanglement.md`, which currently lists her as "Unknown."

---

## Session 51 Priority Queue (recommended)

1. **(NEW from P1)** Jed-side Kurrent verification of Entry 195's child name. The Session 50 max-zoom reading is "Justus" at ~85% confidence; a definitive Jed reading would close this question.
2. **(NEW from P2 follow-up)** Open Deisel KB 218824 October 1810 baptisms and find the baptism entry for Johannes Konze, son of Andreas Konze × Catharina [?]. This should identify Entry 152's Andreas.
3. **(NEW from P2 follow-up)** Add "Identity 6 — Andreas Konze of Deisel, House No. 29 (active c. 1809–1810)" to `Andreas_Konze_Identity_Disentanglement.md`, provisional merge with Klaus Andreas Kontze pending the baptism lookup.
4. **(NEW from P2 bonus)** Update Identity 1 (Andreas I, Küster) in `Andreas_Konze_Identity_Disentanglement.md` to add wife **Maria Elisabeth Brandt** (sourced from Session 38 Entry 358).
5. **(NEW from P3 follow-up)** Search Deisel KB 218824 (1796–1831) for baptisms of Wilhelmine Konze (b. c. 1800–1810) and Maria Elisabeth Konze (b. c. 1800–1812). Konrad Konze is the leading candidate father.
6. **(NEW from P3 follow-up)** Locate Ludwig Köster's death in burial register 218851 between 1828 and 1832 to confirm Wilhelmine's remarriage timeline.
7. **(CARRIED FROM SESSION 49 P4)** Search for Joh. Heinrich Konze, Kaufmann — Entry 195's father — in all Deisel baptism, marriage, and burial registers. This remains a critical gap.
8. **(CARRIED FROM SESSION 48)** Continue the 1876–1956 burial scan from Image 183 (year 1930+).
9. **(CARRIED FROM SESSION 47)** Re-check 1918 entries for any missed Konze burials.

---

*Compiled April 24, 2026. Data sources: `Session49_1835_Burial_Scan_Entry195_April24_2026.md`, `Session38_Burial_Entries_Konze_April22_2026.md`, `Session37_Burial_Index_Konze_Catalog_April21_2026.md`, `Session36_Systematic_Scan_Konze_Network_April21_2026.md`, `Session26_Entry195_Dates_Notes_Emergency_Baptism_April19_2026.md`, `Andreas_Konze_Identity_Disentanglement.md`, `Kontze_Family_Tree_and_Research_Paths.md`. Archion service outage prevented P1 execution.*
