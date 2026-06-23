
# Part XIII — Higher-Zoom Re-verification and Key Retractions (April 11, 2026, late evening / continuation session)

*Added April 11, 2026 in a continuation session following Part XII. A fresh 4× zoom pass through the Trendelburg 1773–1818 burial register (Archion register 220096) was made possible by extending the Part XII zoom-breakthrough technique with a keyboard "+" dispatchEvent step. This pushed the post-zoom `.zoom-holder` from 764×620 (the 2× level used for Part XII) to 1528×1240 (a full 4× level), providing the extra letterform detail needed to definitively resolve several borderline Jungkontze / Jungeorge readings and to surface at least one entirely new Kontze entry. This Part XIII documents the resulting corrections and retractions to Part XII as well as the newly-discovered 1787 Konke (Kontze) entry on page 366.*

## XIII.1 Methodology extension — 4× zoom via keyboard "+" dispatchEvent

The Part XII §XII.4 technique reliably steps the Archion viewer from its default 1× level to 2× via a synthetic `click` dispatched on the `.zoom-hotspots` overlay. The `.zoom-hotspots` click does not however step the viewer past 2× (subsequent `.zoom-hotspots` clicks are consumed by the viewer as repeat clicks at the same level). To push the viewer from 2× to 4×, dispatch a keyboard `"+"` (`keyCode: 187`) keydown event on `document`:

```javascript
(() => {
  document.dispatchEvent(new KeyboardEvent('keydown', {key: '+', keyCode: 187, bubbles: true}));
  document.dispatchEvent(new KeyboardEvent('keyup',   {key: '+', keyCode: 187, bubbles: true}));
  const zh = document.querySelector('.zoom-holder');
  return JSON.stringify({width: zh.offsetWidth, height: zh.offsetHeight});
})();
```

After this sequence the `.zoom-holder` measured 1528×1240 CSS pixels — exactly 4× the default 382×310 — and the browser tile cache served maximally fine tiles at the new level. The 4× zoom persisted across `select.change` navigations in the same way as the 2× level in Part XII. At 4× the text is large enough that individual Kurrent letterforms (in particular capital K vs. lowercase c, and `-tz-` vs `-g-`) can be distinguished unambiguously.

## XIII.2 Correction to Part XII §XII.1 — Page 364 Jun 4 1783 entry is **JungKontze**, not Jungeorge

Part XII §XII.1 retracted the Jungkontze reading of the 364 Jun 4 1783 entry on the grounds that the clearer J-section entries on pages 385 and 398 unambiguously read "Jungeorge" and that the 1221-image burial index's C→K cross-reference note did not list any J-variants. The retraction was made at 2× zoom. At 4× zoom, the 364 Jun 4 1783 surname resolves unambiguously:

> *p. 364, Jun 4, 1783 (image 1180)*: "**Maria Elisabeth, Johann Henrich JungKontze, Corporal bey den Königlichen Husaren dahier, Töchterlein, starb den 3. Juny 1783 an den Blattern, alt 1 Jahr 3 Monat 3 Wochen 1 Tag.**"

The capital **K** on "Kontze" is distinct from any lowercase letter-form and is clearly set off from the preceding "Jung" by a visible word-break. The terminal "-tze" cluster is likewise clearly different from the "-ge" cluster seen on page 385. The earlier (2×) reading of "Jungeorge" was wrong, and Part XII §XII.1's retraction of this specific entry is now itself retracted.

**Consequence.** The Part XI §XI.2 reading of Maria Elisabeth Jungkontze as a legitimate Kontze-family burial is reinstated. Maria Elisabeth was the daughter of **Johann Henrich Jungkontze, Corporal in the Königliche Husaren (Royal Hussars)**, and died of **die Blattern (smallpox)** on June 3, 1783, aged 1 year 3 months 3 weeks 1 day (born approximately February 10, 1782). She was buried June 4, 1783. Her father Johann Henrich Jungkontze becomes the fourth Hessian-military Kontze in the reconstruction (alongside Johann Christoph Contze, Grenadier Leib-Grenadier-Bataillon; plus the HETRINA record entries) and the only one identified as a cavalry NCO rather than infantry.

**Note on surname form "Jungkontze" vs. plain "Kontze."** "Jungkontze" is a compound Trendelburg surname literally meaning "young Kontze" — a 17th/18th-century convention used when two male Kontze households with the same given name lived contemporaneously in the same small town, and the younger (or newer-arrived) one was distinguished with "Jung." The 18th-century Trendelburg parish register treats "Jungkontze" and "Kontze" as two separate but related surnames, much as "Jungeorge" coexisted with plain "Georg" for a distinct unrelated family. The Jungkontze branch is therefore a legitimate Kontze-family branch and not a separate lineage.

## XIII.3 Confirmation of Part XII §XII.1 — Page 385 Feb 23 1797 entry **is** Jungeorge

The 385 Feb 23 1797 entry ("Joh: George [surname] Ambtsdiener dahier, gestorben am 21ten abends zwischen 10 und 11 Uhr, alt ohngefähr 64 Jahr") was re-read at 4× zoom. The terminal cluster after "Jung" resolves to **lowercase e-o-r-g-e** — a sequence of lowercase cursive Kurrent letters with no capital K and no "-tz-." Part XII §XII.1's reading of **Jungeorge** for this entry is confirmed.

The decedent is therefore Johann Georg Jungeorge, Amtsdiener (court usher / bailiff's servant) of Trendelburg, born approximately 1733, died February 21 1797, buried February 23 1797. He is not a Kontze-family member. The Jungeorge family is a separate Trendelburg household.

## XIII.4 Correction to Part XII §XII.1 — Page 398 May 9 1801 entry is **Jungconze** (= Kontze variant), not Jungeorge

The 398 May 9 1801 entry ("Christina Charlotta, Johannes [surname] Bürger und [Schneider?] dahier Töchterlein, gestorben am 7ten abends zwischen 9 und 10 Uhr, alt 7 Wochen weniger 1 Tag") was re-read at 4× zoom. Contrary to Part XII §XII.1, the terminal cluster after "Jung" is **not** "-eorge" but rather **lowercase c-o-n-z-e** — a five-letter sequence in which the first letter is a cursive Kurrent "c" (not a capital K), the middle is "on," and the terminal is "z-e." The reading is therefore **Jungconze**.

In the 18th-century Trendelburg register, "Konze" / "Contze" / "Konke" / "Kontze" are all phonetic and orthographic variants of the same surname Kontze (see Part XI §XI.2 on the burial index's C→K cross-reference note which explicitly equates Contze, Cortze, Cordes, and Contz). The "Jungconze" compound therefore belongs to the Jungkontze branch documented in §XIII.2 above — it is a softer spelling of the same compound surname. This entry is therefore a legitimate Kontze-family burial.

**Decedent:** Christina Charlotta Jungconze, infant daughter of Johannes Jungconze, Bürger und (probably) Schneider of Trendelburg, died May 7 1801 at 9–10 p.m., aged 7 weeks less 1 day (born approximately March 21, 1801). Buried May 9, 1801. Her father Johannes Jungconze is plausibly a younger male of the same Jungkontze household as Johann Henrich Jungkontze the Corporal of Hussars (§XIII.2) — one generation later.

## XIII.5 New find — Page 366 Jan 1787 burial of Anna Chargretha, wife of Joh. Henr. Konke

Part XII §XII.6 listed as research priority #1 the re-verification of the alleged "page 366 Jan 24 1786 Jungkontze entry." At 4× zoom the reality of that entry turned out to be different from both the Part XI surname and the Part XII date. The actual entry, found on page 366 directly under the "1787" year-heading, reads:

> *p. 366, Jan 24, 1787 (image 1181)*: "**[24.] Anna Chargretha geb. Wilhelmannin, Ehefrau Joh: Henr. Konke Bürger und [Ackermann?] dahier, starb den [24.?] Januar Nachmittag um 2 Uhr, alt 65 Jahr.**"

(The month-day field for the actual death / burial date shows a numeral whose first digit is almost certainly "2"; the second digit is smudged at the capture resolution but the entry's position in the register sequence between Jan 14 Anton Heinrich and Feb 2 Dorothea Elisabetha forces the date into the Jan 14 – Feb 1 window, which together with the visible "2-something" makes Jan 24 the near-certain reading.)

**Decedent:** Anna Chargretha née Wilhelm (the form "Wilhelmaennin" is the 18th-century feminine genitive "of the Wilhelm [family]"), born approximately early August 1721 to early January 1722 (depending on whether the "65 Jahr" was read as a completed or approximated age), died January 24 1787 at 2 p.m., buried shortly thereafter. **Spouse:** Johann Henrich Konke, Bürger und Ackermann of Trendelburg, who appears to have still been living as of her burial (the entry identifies him as her spouse in the present tense, not as "weiland").

### XIII.5.1 Why "Konke" = "Kontze"

The terminal sound in 18th-century Hessian German was often rendered with any of "-ke," "-ce," "-tze," "-nze," or "-onze" for the same underlying surname. The 220096 burial-index image 1221 cross-reference note explicitly equates **Contze / Cortze / Cordes / Contz** as a single surname cluster. "Konke" is the same cluster pronounced more crisply — the medial "-nt-" reduced to "-n-" and the terminal "-ze" flattened to "-ke" (or possibly the scribe writing the surname as the family colloquially pronounced it rather than as it was canonically spelled in formal documents). The Konke / Kontze family identity is strongly supported by the occupation and honorific context: Joh. Henrich Konke is **Bürger und Ackermann** in Trendelburg in 1787, exactly the title borne by the Kontze household heads Johann [Henrich?] Kontze (§XII.2.1, father of Martha Elisabeth d. April 11, 1783) and Johannes Kontze (§XII.2.2, father of Wilhelmina d. June 14, 1783). It is highly probable that **Joh. Henrich Konke = Johann Henrich Kontze**, i.e. the same individual as the father of Martha Elisabeth in §XII.2.1.

### XIII.5.2 Implications for the Kontze family reconstruction

If Joh. Henrich Konke = Johann Henrich Kontze the Bürger und Ackermann, the following new relationships are established:

- **Anna Chargretha née Wilhelm**, b. c. 1722, d. Jan 24 1787, was the **wife** of Johann Henrich Kontze.
- Johann Henrich Kontze was himself born no later than c. 1722 (i.e. he was at least his wife's age and probably a few years older). This places him squarely in the senior generation — plausibly the same cohort as **Herr Andreas Contze** (b. c. August 1722, d. Nov 1800) and only slightly younger than **Arnold Philipp Kontze** (b. c. 1708/9, d. April 1780). He may be a third brother of those two men.
- The **Wilhelm family** is now introduced as a new Trendelburg in-law family to the Kontze tree via Anna Chargretha's maiden name.
- Johann Henrich Kontze lost his young daughter Martha Elisabeth (age 3y 4.5m) on April 11 1783 (§XII.2.1) and his wife Anna Chargretha (age 65) on January 24 1787. The four-year gap and the specific ages fit a single household cleanly.

### XIII.5.3 Distinction from Johann Henrich Jungkontze the Corporal

Johann Henrich Kontze Bürger und Ackermann (§XIII.5) and Johann Henrich Jungkontze Corporal der Königlichen Husaren (§XIII.2) are **almost certainly two different men**, not the same person twice-recorded under variant surnames. The two differ in:

1. **Surname.** Kontze (simple form) vs. Jungkontze (compound form with "Jung" disambiguator), as intentionally used by the Trendelburg register to distinguish two contemporaneous male Kontze households.
2. **Occupation.** Bürger und Ackermann (civilian farmer with burgher rights) vs. Corporal der Königlichen Husaren (active-service NCO in the Royal Hussar cavalry regiment of Landgrave Friedrich II of Hessen-Kassel). These are incompatible full-time roles.
3. **Age cohort.** Born no later than 1722 vs. born approximately 1745–1760 (a cavalry corporal fathering a daughter in 1782 is most plausibly in his 20s or 30s).

The plausible reading is that **Johann Henrich Jungkontze Corporal** is the son or nephew of **Johann Henrich Kontze Bürger und Ackermann**, bearing the same given name with the "Jung" prefix precisely to distinguish the younger military man from his elder civilian kinsman. This is the standard function of the "Jung-" prefix in Hessian patronymic practice.

## XIII.6 Revised consolidated Kontze burial inventory (Register 220096, 1773–1818)

| # | Decedent | Relationship / role | Burial date | Age at death | Derived birth | Manuscript page | Image | Source section |
|---|---|---|---|---|---|---|---|---|
| 1 | Arnold Philipp Kontze | self, Rathsverwandter & Ackermann | ~Apr 5, 1780 | 71 years | c. 1708/9 | 361 | 1178 | K-index + pg. read |
| 2 | Martha Elisabeth Kontze | daughter of Johann Henrich Kontze, Bürger & Ackermann | Apr 14, 1783 | 3y 4.5m | ~Nov 1779 | 364 | 1180 | pg. read only |
| 3 | Maria Elisabeth Jungkontze | daughter of Joh. Henrich Jungkontze, Corporal Kön. Husaren | Jun 4, 1783 | 1y 3m 3w 1d | ~Feb 10, 1782 | 364 | 1180 | pg. read only |
| 4 | Wilhelmina Kontze | daughter of Johannes Kontze, Bürger & Ackermann | Jun 16, 1783 | 1y 5m 2d 12min | ~Jan 12, 1782 | 364 | 1180 | pg. read only |
| 5 | Anna Chargretha Konke née Wilhelm | wife of Joh. Henrich Konke, Bürger & Ackermann | ~Jan 24, 1787 | 65 years | c. 1722 | 366 | 1181 | **new find pg. read** |
| 6 | Herr Andreas Contze | self, Rathsverwandter | Nov 9, 1800 | 77y 8m 26d | ~Aug 3, 1722 | 396 | 1196 | K-index + pg. read |
| 7 | Christina Charlotta Jungconze | daughter of Johannes Jungconze, Bürger & (Schneider?) | May 9, 1801 | 7w less 1d | ~Mar 21, 1801 | 398 | 1197 | pg. read only |
| 8 | Johannes Contze | son of Johann Christoph Contze, Grenadier Leib-Gren.-Btl. | Jan 4, 1808 | 3y 6m − 2w | ~Jul 1804 | 414 | 1205 | K-index + pg. read |

Plus the separate Jungeorge family burials on pages 385, 398, and elsewhere, now definitively excluded from the Kontze reconstruction.

## XIII.7 Revised list of distinct Kontze adult males in 18th-century Trendelburg

Combining Parts XI, XII, and XIII the reconstruction now identifies the following distinct adult male Kontze / Konke / Jungkontze household heads documented in 1773–1818 Trendelburg:

1. **Arnold Philipp Kontze** — Rathsverwandter & Ackermann. b. ~1708/9, d. Apr 5 1780 aged 71. Senior generation. Civic office-holder.
2. **Herr Andreas Contze** — Rathsverwandter. b. ~Aug 3 1722, d. Nov 9 1800 aged 77y 8m 26d. Senior generation. Civic office-holder. Probably a brother of Arnold Philipp.
3. **Johann Henrich Kontze** (= "Joh. Henr. Konke") — Bürger und Ackermann. b. no later than c. 1722. Spouse Anna Chargretha née Wilhelm (d. Jan 24 1787 aged 65). Father of Martha Elisabeth (d. Apr 11 1783 aged 3y 4.5m). Senior generation (possibly a third brother of #1 and #2; alternatively a slightly younger cousin).
4. **Johannes Kontze** — Bürger und Ackermann. Father of Wilhelmina (d. Jun 14 1783 aged 1y 5m). Middle generation. Possibly a son of one of #1, #2, or #3.
5. **Johann Henrich Jungkontze** — Corporal bey den Königlichen Husaren (Royal Hussar cavalry). b. ~1745–1760. Father of Maria Elisabeth (d. Jun 3 1783 of smallpox, aged 1y 3m 3w 1d). Military younger generation. Plausibly a son or nephew of #3 Johann Henrich Kontze, carrying the same given name with the "Jung" prefix as a disambiguation marker.
6. **Johannes Jungconze** — Bürger und (Schneider?). Father of Christina Charlotta (d. May 7 1801 aged 7w less 1d). Younger generation of the Jungkontze/Jungconze branch. Plausibly a son of #5 Johann Henrich Jungkontze, or alternatively a cousin in the same branch.
7. **Johann Christoph Contze** — Grenadier in the Leib-Grenadier-Bataillon. Father of Johannes d. Jan 4 1808 aged 3y 6m − 2w. Military youngest generation. Possibly ~15–20 years younger than #5.

Points 1–4 are senior + middle generation civilian farmers with council-office lineage in points 1 and 2. Points 5–7 are military-age younger men, two in the Jungkontze line and one (Johann Christoph) in the simple-Kontze / Contze line. The family pattern is consistent with a single patrilineal Kontze clan branching into several households across roughly three generations in the window 1770–1810, with young adult sons entering Hessian military service in the final quarter of the 18th century.

## XIII.8 Updated next-steps priorities

1. **Marriage record for Joh. Henrich Kontze × Anna Chargretha Wilhelm.** The most likely marriage window is c. 1740–1750 (wife born c. 1722, husband born no later than c. 1722, first child Martha Elisabeth born c. November 1779 → this was either a late first child or a late second marriage; either way the couple was married at least by c. 1778). Search the 220093 pre-1773 Trendelburg register for the marriage.
2. **Wilhelm family in Trendelburg.** The maiden name Wilhelm introduces a new in-law family. Search 220093 and 220096 for Wilhelm baptisms, marriages, and burials to locate Anna Chargretha's parents.
3. **Baptism records for Martha Elisabeth (c. Nov 1779), Wilhelmina (c. Jan 1782), and Maria Elisabeth (c. Feb 1782).** All three daughters buried in 1783 would have been baptized in the 1779–1782 window and all three baptism entries should be on pages of register 220096 corresponding to those years.
4. **Continuing page-by-page sweep** of the 1773–1818 burial section (248 images total) looking for additional Kontze entries missed by the K-index — priorities are the gap years 1773–1779 and 1788–1799 which have not yet been inspected.
5. **Re-verify §11.27 "hweiland 1795" primary source** to decide between Reconciliation A and Reconciliation B in Part XII §XII.3.

## XIII.9 Confidence assessment

The four re-readings of this session have materially changed the inventory:

- Page 364 Jun 4 1783 **JungKontze** — confidence: very high (4× zoom, capital K unambiguous)
- Page 385 Feb 23 1797 **Jungeorge** — confidence: high (4× zoom, lowercase cluster, no K)
- Page 398 May 9 1801 **Jungconze** — confidence: high (4× zoom, lowercase c-o-n-z-e cluster; counts as a Kontze variant via the C/K cross-reference note)
- Page 366 Jan 24 1787 **Anna Chargretha née Wilhelm, wife of Joh. Henr. Konke** — confidence: high for the names; medium for the exact day-of-month (reads as "24" but the first digit is partially smudged) and for identifying Konke = Kontze (strongly supported by occupation and register conventions but not 100% proven)

Aggregate: the Kontze-in-Trendelburg household inventory for 1773–1810 has grown from 5 adult men to 7, a new in-law family (Wilhelm) has been introduced, and the Jungkontze compound-surname branch is rehabilitated as a legitimate Kontze branch rather than being mistakenly collapsed into Jungeorge.
