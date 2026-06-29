# Session 141 — Lippoldsberg baptism per-year Archion permalinks (28 Jun 2026)

**Jed:** "permalink the lippoldsberg research log as well."

Scope chosen (AskUserQuestion): **full per-year window 1831–1841** for the Lippoldsberg
baptism register (Archion reg. **219778**, Taufen 1830–1870). Live, logged-in Archion viewer
via the in-browser workflow.

## What was done
Navigated to each year's first leaf, **year-verified it from the written "Jahr 18.." header**
(zoomed each header — the calibration step the memory file warns about), then minted a permalink
(chain icon → DE "Erstellen" first click re-renders to EN "Create" → second click yields the
short URL). All 11 minted and each read back from the panel.

| Year | Bild (Seite) | Permalink |
|------|--------------|-----------|
| 1831 | 1416 (S5)  | p/2715c68e0d |
| 1832 | 1420 (S9)  | p/1d9947f43e |
| 1833 | 1425 (S14) | p/cf614a3da4 |
| 1834 | 1429 (S18) | p/388fed7852 |
| 1835 ★ | 1435 (S24) | p/22b146a0af |
| 1836 | 1443 (S32) | p/e4c4cf4766 |
| 1837 | 1450 (S39) | p/c014fbca98 |
| 1838 | 1457 (S46) | p/b7c25bc88b |
| 1839 | 1464 (S53) | p/9f378a58d5 |
| 1840 | 1469 (S58) | p/bb0324ac19 |
| 1841 | 1474 (S63) | p/68c5c87b06 |

Full URLs are `https://www.archion.de/p/<hash>/`. **Resolution spot-check:** opened
`p/22b146a0af` (the ★1835 leaf) — resolved correctly to reg. 219778 **Bild 1435**, showing the
1835 header and entries #111–113 (the two Pape girls + stillborn male). 12 mints total in the run
(11 kept + 1 swallowed re-render click); no throttle hit.

## Calibration corrections (important)
Reading every year header established that the baptism reel is **LINEAR, not shuffled**:
**Seite = Bild − 1411** holds across the whole window 1830–1841. This overturns the prior log's
"displaced/interleaved tail (1836 onward)" caveat, which had come from year-numeral misreads.
Specific anchor fixes vs. the old table:
- **1833 starts Bild 1425**, not 1424 — Bild **1424 is the END of 1832** (Oct–Dec + year-end Summa, S13).
- **1836 = Bild 1443** (not ~1444).
- **1837 = 1450, 1838 = 1457, 1839 = 1464, 1840 = 1469, 1841 = 1474.** The old table had
  1838=~1474 and 1841 "reached by Bild 1484" — both wrong; **Bild 1474 is 1841**.
- Corroboration: Bild 1457 (1838) entry #304 = **Carl August Gans** — matches the log's
  "Carl August Gans, bapt. 18 Mar 1838" line.

## Files updated
- `germany/lippoldsberg-research-log.html` — baptism year→Bild table rebuilt to a 4-column
  table (Year | Year-start Bild (Seite) | Archion permalink (year-verified) | Notes) with all 11
  permalinks + corrected anchors; intro paragraph and caveat note rewritten to state the reel is
  linear (Seite = Bild − 1411); pl-meta updated (Taufen reg. 219778; permalinks added 28 Jun 2026).
- `_MEMORY_Session_Conventions.md` — added the Lippoldsberg 219778 per-year permalink line + the
  Seite=Bild−1411 / "reel is linear" correction under the Session-131 permalink block.

## Confirmation prime-class permalinks (reg. 219775) — added same day
Per Jed's follow-up ("do the confirmation prime class leaves"), minted a year-verified permalink for
each confirmation class 1846–1850 (each read from its written "Jahr 18.. — 1ter Pfingsttag" header):

| Class | Bild (Seite) | Permalink |
|-------|--------------|-----------|
| 1846 | 152 (S40/41) | p/35f65129a1 |
| 1847 | 153 (S42/43) | p/b85ba8e925 |
| 1848 | 154 (S44/45) | p/76be9ce0d0 |
| 1849 ★ prime | 155 (S46/47) | p/3b15604236 |
| 1850 | 157R (S51)   | p/c25e35735a |

The ★1849 cohort is the decisive leaf (Pfingsten 27 May 1849; "21 Kinder, 13 Söhne, 8 Töchter"; #5
**Friedrich Wilhelm Gans, b. 24 Jun 1835** — a Gans in Charles's generation but not a Carl and not
26 Jan). **Resolution spot-check:** `p/3b15604236` resolves to reg. 219775 **Bild 155**. The reel runs
in order for this window (Seite ≈ Bild − 111; 1846 class on Bild 152). Confirmation table in the research
log updated with all five links + the "Jahr/Pfingsten" verification.

## 1851–1855 confirmations re-read & minted (same day)
Per Jed's follow-up ("re-read and mint"), the 1851–1855 classes were re-read leaf by leaf and minted:

| Class | Bild (Seite) | Permalink |
|-------|--------------|-----------|
| 1851 | 159 (S54/55) | p/d20091302a |
| 1852 | 161 (S58/59) | p/399dcfda73 |
| 1853 | 163 (S62/63) | p/35bd3e8c76 |
| 1854 | 164 (S64/65) | p/e9ec86f00b |
| 1855 | 166 (S68/69) | p/194db66826 |

**Resolved the old open item:** the reel is **in order — there is no displaced/duplicate leaf**. Session 19's
"1849 = Bild 163" was simply a misread; **Bild 163 is genuinely the 1853 class** (Pfingsten 15 May 1853;
resolution re-verified to load Bild 163). The confirmation window 1846–1855 is now fully permalinked
(10 classes). No confirmand named Carl Gans in any class.

## Conclusion unchanged
The genealogical verdict stands: **no Carl Gans b. 26 Jan 1835 in Lippoldsberg** (baptisms or
confirmations); nearest is Carl August Gans b. 26 Feb 1838 (not Charles).
