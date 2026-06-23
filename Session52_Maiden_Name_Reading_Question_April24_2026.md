# Session 52 — April 24, 2026
## Entry 152 Maiden Name Re-Read Casts Doubt on Thilin Hypothesis; KB 218824 Section Structure Discovered

---

## Headline

Session 52 made two findings that complicate Session 51's clean Identity-6-equals-Klaus-Andreas-Kontze conclusion:

1. **Entry 152's mother's maiden name does not clearly read as "Thilin."** A re-read at zoom level 12 of Image 1814 in burial register 218851 shows a 5-letter Kurrent word that looks more like **"Thinka"** or **"Thirla"** than "Thilin" — and definitely not "Gräfe" (Session 49's reading). Whether this is the same name as Klaus Andreas Kontze's wife "Catharina Elisabeth née Thilin" (1799/1800 baptism entries) or a different woman remains uncertain. **A Jed-side Kurrent expert reading is now the bottleneck.**

2. **KB 218824 has a complex multi-section structure that explains the apparent non-monotonic image-year sequence noted in Session 51.** A title page on Image 1697 reads: "Deisel KB 1796-1831 — Bem.: * (1796-1830) S. 1-194; Konf (1796-1830); oo (1796-1831) S. 1-56; * (1831) S. 60-65; + (1796-1831) S. 1-95; totgeborene Kinder (1823-1830); mit Register für Trauungen und Begräbnisse nach den Amtshandlungen." This means the register is organized **by record type** (baptisms, confirmations, marriages, late baptisms, burials, stillbirths) rather than chronologically — and the 1660–1696 image range (where Session 51 found the 1799 Catharine and 1800 Wilhelmine Kontze baptisms) appears to belong to an **earlier separate register** filmed adjacent to the 1796–1831 register on the same microfilm.

The October 1810 Johannes Konze baptism was not located in this session due to the section-navigation complexity. P3 (Marie Elisabeth Konze baptism), P4 (Ludwig Köster death), P5 (Joh. Heinrich Konze search), and P8 (Klaus Andreas marriage record) were deferred to Session 53.

---

## Priority 2 (P2) — COMPLETED with caveat: Entry 152 maiden name re-read inconclusive

### Method

Burial register 218851 was opened, navigated to Image 1814 (where Entry 152 — Johannes Konze, lediger Sohn des Andreas Konze, b. 26 Oct 1810 d. 1835 — was originally read in Session 49). The viewer was driven to zoom level 12 via the `jquery.tilezoom` API, and the mother's maiden-name field was captured at two progressively tighter zoom regions.

### Reading

The mother's full text reads approximately:

> "[Catharina/Catharine] Elisabeth gb. **[Thinka? Thirla?]**, [Schümeischer? Schornsteinfeger?] [continuation]"

Letter-by-letter analysis of the maiden name (5–6 lowercase letters after "gb."):

| Position | Glyph | Possible reading |
|----------|-------|------------------|
| 1 | Capital T with crossbar | T (clear) |
| 2 | h with descender | h (clear) |
| 3 | small i with dot | i |
| 4 | medium up-stroke with curve | n, l, r, or k |
| 5 | small letter | k or l |
| 6 | terminal a | a |

Best transliteration candidates:
- **"Thinka"** — does not match any documented Konze maternal lineage
- **"Thirla"** — does not match
- **"Thilin"** — Klaus Andreas Kontze's wife per 1799/1800 baptisms — **possible only with strong glyph reinterpretation** (positions 4 and 5 would need to be "li" not "nk/rl," and position 6 would need to be "n" not "a")

### Implication

The maiden-name reading does NOT cleanly support the Session 51 conclusion that Identity 6 = Klaus Andreas Kontze. The match is now weaker than Session 51 implied. Three reconciliations remain on the table:

1. **Same woman, different scribe.** The 1810 burial scribe may have spelled "Thilin" in a way that visually resembles "Thinka." Kurrent variation across decades is real. Klaus Andreas's wife Catharina Elisabeth née Thilin remains the same person across all entries.
2. **Klaus Andreas remarried.** Catharina Elisabeth Thilin died between 1800 (Wilhelmine's birth) and 1810 (Johannes's birth). Klaus Andreas remarried a different Catharina. This second wife's maiden name is what Entry 152 records.
3. **Different Andreas.** Entry 152's Andreas is NOT Klaus Andreas Kontze but a sixth, genuinely distinct Andreas Konze whose wife is also named Catharina but with a different maiden name. The matching House Nr. 29 is then either coincidence or reflects two different households at the same address across decades.

**Recommended next step:** Jed-side Kurrent reading of Image 1814 at maximum zoom is the tiebreaker. If Jed reads "Thilin," Hypothesis 1 wins. If a clearly different name, Hypothesis 2 or 3.

---

## Priority 1 (P1) — DEFERRED: Register section structure discovered

### Discovery — KB 218824 sectional title page (Image 1697)

The title page on Image 1697 reveals the register's organization:

| Section | Years | Pages |
|---------|-------|-------|
| **\\* Baptisms (Taufen)** | 1796–1830 | S. 1–194 |
| Konfirmationen | 1796–1830 | (page count not noted) |
| **oo Marriages (Trauungen)** | 1796–1831 | S. 1–56 |
| **\\* Late Baptisms** | 1831 | S. 60–65 |
| **+ Burials (Beerdigungen)** | 1796–1831 | S. 1–95 |
| Stillbirths | 1823–1830 | (page count not noted) |
| Index for marriages and burials | — | — |

### What this explains

Session 51 noted apparent non-monotonic year sequences:
- Image 1660 → 1800
- Image 1670 → 1803–1804
- Image 1690 → 1804
- Image 1697 → title page
- Image 1700 → "1821" (re-read recommended)
- Image 1715 → "1815"
- Image 1722 → 1825
- Image 1730 → 1814–1815

**Resolution:** The 1660–1696 range likely belongs to an **earlier register** filmed on the same reel as the 1796–1831 register. The Catharine 1799 and Wilhelmine 1800 baptism entries on Image 1660 are in this earlier register. After the title page (1697), the 1796–1831 register's baptism section begins at Image 1698 and runs through ~Image 1791 (covering 194 pages of 1796–1830 baptisms), followed by other sections (confirmations, marriages, burials).

The confusing year jumps observed (1815 at 1715, 1821 at 1700, 1825 at 1722) likely reflect:
- The actual baptism section pages
- Year annotations added later in margins (death cross-references)
- Possibly some interleaving between sub-sections

### What this means for finding 1810 Johannes Konze

The October 1810 baptism — if recorded in this register — should be in the **baptism section** somewhere between Image 1698 and ~Image 1791. Given that 1796 is at the start (page 1) and 1830 is at the end (page 194), 1810 would be ~14/35 of the way through the 194-page section, i.e., page ~78 ≈ Image ~1698 + 39 ≈ **Image 1737**.

Alternatively, the 1810 baptism may be in the **earlier register** (1660–1696 range) if Klaus Andreas Kontze's children continued to be baptized there. This needs verification.

**Recommended Session 53 navigation targets:**
- Image **1737 ± 5** (estimated 1810 baptism location in the 1796–1831 register's baptism section)
- Images **1690–1696** (last pages of the older register, if still in use 1810)

---

## Priorities 3, 4, 5, 8 — DEFERRED to Session 53

| Priority | Subject | Why deferred |
|----------|---------|--------------|
| P3 | Marie Elisabeth Konze baptism | Same register-navigation challenge as P1 |
| P4 | Ludwig Köster death 1828–1832 | Distinct register; not opened this session |
| P5 | Joh. Heinrich Konze, Kaufmann (Entry 195's father) | Critical gap — extensive search required |
| P8 | Klaus Andreas Kontze × Catharina Elisabeth Thilin marriage | In KB 218824 marriages section (S. 1–56), location TBD; depends on P2 maiden-name resolution |

---

## Summary of Session 52

| Priority | Status | Outcome |
|----------|--------|---------|
| P1 — Johannes Konze 1810 baptism | **Deferred** | Register section structure now understood; navigation target estimated at ~Image 1737 |
| P2 — Entry 152 mother's maiden name | **Completed with caveat** | High-zoom reading inconclusive — Kurrent letters fit "Thinka" or "Thirla" better than "Thilin" or "Gräfe"; Jed-side reading needed |
| P3 — Marie Elisabeth Konze baptism | **Deferred** | — |
| P4 — Ludwig Köster death | **Deferred** | — |
| P5 — Joh. Heinrich Konze, Kaufmann | **Deferred** | — |
| P8 — Klaus Andreas marriage | **Deferred** | — |

### Key takeaways

1. **Identity 6 = Klaus Andreas Kontze is now LESS certain.** Session 51's bridge between the 1799/1800 baptisms and Entry 152's 1810 burial relied on the maiden name match. That match is now in question.
2. **The KB 218824 register has a documented multi-section structure** — important navigational reference for all future searches in this register.
3. **Two screenshots of the maiden name in Entry 152** were captured (zoom regions [400,540,780,580] and [170,530,800,600] on Image 1814) and saved to disk by the browser tool for Jed's review.

---

## Session 53 Priority Queue (recommended)

1. **(JED EXPERT READING)** Jed reads the maiden name in Entry 152 of register 218851 Image 1814. Verify whether it is Thilin, Thinka, Thirla, or another name. This single decision unlocks the Identity 6 question.
2. **(CARRIED FROM S52-P1)** Open KB 218824 at Image 1737 ± 5 (estimated 1810 baptism location in the post-title-page baptism section) and search for Johannes Konze son of Andreas Konze.
3. **(CARRIED FROM S52-P3)** Search the same image range for Marie Elisabeth Konze baptism (~1805–1812).
4. **(CARRIED FROM S52-P4)** Open burial register 218851 and search 1828–1832 burials for Ludwig Köster.
5. **(CARRIED FROM S52-P5)** Begin systematic Joh. Heinrich Konze, Kaufmann search across all Deisel registers (baptisms 1830-1861 [218842], baptisms 1796-1830 [218824 baptisms section], marriages, burials).
6. **(CARRIED FROM S52-P8)** Once the maiden-name question is resolved, search KB 218824 marriages section (estimated to follow the baptism section) for the marriage of Klaus Andreas Kontze × [whoever the maiden-name resolves to].
7. **(CARRIED, DEFERRED)** P6 (1930+ burial scan), P7 (1918 burial recheck) remain extensive scans for a dedicated session.

---

*Compiled April 24, 2026. Data sources: Live Archion read of Deisel KB 218824 (Image 1697 title page, Image 1730) and Deisel Beerdigungen 218851 (Image 1814). Key open question: maiden name reading on Entry 152.*
