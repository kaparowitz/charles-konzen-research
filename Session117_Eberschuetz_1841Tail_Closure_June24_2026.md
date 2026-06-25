# Session 117 — Eberschütz Confirmation Sweep: 1841-tail closure (24 June 2026)

## Goal
Close the one residual gap left by Session 115's Eberschütz confirmation sweep. That
session read the Konfirmationen register (reg. **218884**) class-by-class for 1847–1854
(births ~1833–1840) and found it negative, but flagged the **1855/1856 classes (births
~1841) as sampled, not read leaf-by-leaf**. This session reads them in full, per Jed's
"any Carl, 1833–1841 + Konze for Eberschütz" instruction, so the 1833–1841 birth window
is closed at the leaf level.

## Method
Live Archion in-browser viewer (subscription, Jed's login). Register 218884, calibration
**Seite(left) = 2 × image − 1731** (verified Session 115). Stale-canvas workaround: after
each page-jump click a zoom +/− to force a redraw, then read the written Jahr/Seite header
before trusting position. Read every Knaben (boys-first) entry for forename Carl/Karl and
any Konze / Kontze / Gansen / Gonsen / *n-s-n surname; scanned Mädchen surnames too.

## Leaves read (year confirmed by the written header, not arithmetic)
- **Bild 894** = Seite 57/58 = **Jahr 1854** (Nro 296–301) — 1854 class body.
- **Bild 895** = Seite 59/60 = **Jahr 1854** (Nro 303–308) — 1854 Mädchen tail, ends Nro 308.
- **Bild 896** = Seite 61/62 — left = 1854 tail (Nro 309 + Summa); **right = Jahr 1855 class
  START, Nro 314**. → permalink **p/99fab7d71a**.
- **Bild 897** = Seite 63/64 — left = 1855 girls tail + **Summa 14 = 7 Knaben/7 Mädchen** +
  Jahr 1856 header; right = Jahr 1856 class (Nro 326 ff.). → permalink **p/0b98119acc**.
- **Bild 898** = Seite 65/66 = Jahr 1856 (left) / Jahr 1857 (right) — confirms 1856 births
  are 1842 and 1857 births 1842–43.

## 1855 class — read in full (births 1840–41)
Nro 310–323; **Summa 14 = 7 Knaben + 7 Mädchen** (tally read on Bild 897, so the boys list
is provably complete). The **seven boys**:
1. **310 — Conrad Ludwig Vechel**, b. 1841, father Johann David Vechel (Leineweber), mother geb. Bohle; conf. 21 März 1855.
2. **311 — Conrad Lorenz Aschermann**, b. 1841, father Aschermann (Schneider).
3. **312 — Conrad Engelbrecht**, b. 1841, father Johannes Engelbrecht.
4. **313 — Friedrich Hattenbach zur Heide**, b. 1841, father Friedrich Hattenbach zur Heide, mother geb. Koch.
5. **314 — Conrad Bohle**, b. 13 Oct 1840, father Christian Bohle, mother Caroline Wiedemeier.
6. **315 — Friedrich Conrad Engelbrecht**, b. Nov 1840, father Bernd Georg Engelbrecht.
7. **316 — Daniel Scheele**, b. 1841, father Christian Scheele, mother (2nd wife) geb. Bohle.

Girls 317–323: Reppulier, Trottier, Jaeger, Heise, Wigge, Kahle, Krone.
**No Carl. No Konze / *n-s-n surname.**

## 1856 class — read into (births already 1842)
Nro 324 ff.: Ludwig Hempel (324), Ludwig Bohle (325), Conrad Ludwig Thöne (326), Friedrich
Kleppe (327), Conrad Ludwig Blum (328), Georg Wilhelm Theodor Gustav Schröder (329),
Heinrich Sasse (330), Conrad Ludwig Scheele (331), **Carl Scheele (332)** — all **b. 1842**.
Girls follow (Heinze, Aschermann, Thöne, …). The **only Carl is Carl Scheele, Nro 332,
b. 1842** (an Eberschütz Scheele — wrong surname, ~7 years too young). The only in-window
birth (1840) among the 1856 entries is a **girl** (Heinze).

## Result — NEGATIVE; 1833–1841 window now fully closed
- The 1841-born cohort lives in the **1855 class**, read in full: **no Carl, no Konze**.
- The **1856 class is already into 1842 births**, so 1841 is fully bracketed; its only Carl
  (Carl Scheele, b. 1842) is non-matching on both surname and age.
- Eberschütz stays **ELIMINATED**, now searched leaf-by-leaf on the confirmation track for
  the **entire 1847–1856 span** (births 1833–1841) plus the Jan–Feb 1835 baptism window.
- Two Carls total in the whole register, both non-matching: Carl Wilhelm Höbener (1854,
  b. Oct 1839, Schuhmacher's son) and Carl Scheele (1856, b. 1842).

## Permalinks minted
- 1855 class (Bild 896, Seite 61/62): https://www.archion.de/p/99fab7d71a/
- 1855 Summa + 1856 start incl. Carl Scheele (Bild 897, Seite 63/64): https://www.archion.de/p/0b98119acc/

## Files updated
- `germany/eberschuetz-research-log.html` — status box, sources row (two new permalinks +
  full 1855/1856 detail), calibration note (Bild 896/897 anchors), follow-ups now "None".
- `search-coverage.html` — Eberschütz wider-window entry rewritten (Höbener + Scheele, 1841
  closure); a live-Archion note added to the 24 Jun callout.
- `_MEMORY_Session_Conventions.md` — 218884 entry extended with 1855/1856 anchors, the
  1841-tail closure result, and the two permalinks.
