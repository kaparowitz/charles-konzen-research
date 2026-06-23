# Register 220093 Baptism — Session 4 Calibration & Partial Cluster N (April 13, 2026)

**Session Date:** April 13, 2026 (continuation)
**Register:** Archion Register #220093 (Trendelburg Kirchenbuch 1708–1772)
**Section:** Taufen (Baptisms), manuscript pages 1–245
**Researcher:** Jed Johnson (with Claude assistance)

---

## 1. Session Goal & Outcome

**Goal:** Visit Cluster G (page 48, earliest Andreas baptism) — the highest-priority remaining page, which may confirm whether all Generation 0 Kontze patriarchs are sons of Andreas Contze Senior.

**Outcome:** Cluster G could not be reliably located due to separator/TOC pages disrupting the page↔image calibration in the 730–734 image range. Instead, this session produced valuable **calibration data** and a **partial scan** of Cluster N (~page 112, image 765).

---

## 2. Calibration Discoveries

Prior anchor: page 1 = image 709 (March 1708 header confirmed).

| Image | Manuscript Page | Year Range | Notes |
|-------|-----------------|-----------|-------|
| 709 | p. 1 | 1708 | Arnold Philipp baptism (ANNO 1708 header) |
| 728 | p. 39 | 1719 | "Contzy" cluster — Andreas Sr. & Jr. |
| **733** | **(separator)** | — | **Table of Contents page** listing Getaufte 1708–72 pp.1–245, Konfirmierte, Geburten, etc. Not a manuscript page. |
| 735 | p. 52 | 1725 | Confirmed year/page anchor |
| 754 | p. 90 | late 1737 / early 1738 | Dionysius (Nies) Kontze baptism |
| **765** | **~p. 112** | **~1745/46** | Cluster N target — partial scan (see §4) |

**Revised formula:** Image ≈ 709 + (page ÷ 2) + separator offsets. At least ONE separator page occurs between images 728 and 735 (likely image 733 = TOC). This shifts later calibration by +1 image vs. the naive formula, explaining why page 48 is not at image 733 as the naive formula would suggest — it is likely at image 732 or 734, both of which appeared blank or ambiguous during this session.

---

## 3. Cluster G (Page 48) — DEFERRED

**Status:** Not successfully located this session.

**What happened:**
- Image 732 appeared blank/unreadable
- Image 733 is a section-divider TOC page (not page 48)
- Image 734 was ambiguous
- Without a clean year header to anchor against, page 48 cannot be confidently identified

**Recommended next approach:**
1. Navigate to image 735 (confirmed = p. 52, 1725) and page BACKWARDS through 734 → 733 → 732 → 731, looking for the 1722–1723 transition on a left-hand manuscript page.
2. Alternatively, search for page numbers written directly on the manuscript (where present) to triangulate.
3. If still blocked, skip G and return after Cluster H (p. 68 earliest Philipp), which should be near image 743 — a cleaner anchor.

---

## 4. Cluster N (Page 112, Image 765) — PARTIAL

**Year confirmed:** ~1745/46 (consistent with page 112 target).

**Entries read (non-Kontze fathers on this opening):**
- Conrad Ackmanns
- Andreas Weller
- Conrad Weikks (Ackermann)
- Joannes Beisleim (Schultheis)

**Potential Kontze signal — NEEDS RE-EXAMINATION:**

On the right-hand page of image 765, a godparent/witness position contained what appeared to read:

> "Dreas Kontea von Zeylitz"

**Tentative interpretation:** "[An]dreas Kontze von Zeylitz" — an Andreas Kontze from Zeylitz serving as godfather.

**Why this matters if confirmed:**
- Introduces a **new geographic branch** of the Kontze family: Zeylitz (likely Zeilitz / Zeitz area — needs geographic confirmation).
- Another Andreas Kontze, distinct from Trendelburg Senior and Junior.
- Could be a cousin-line that explains the surname's prevalence in the region.
- Dates (~1745/46) would make him contemporary with Andreas Contze Junior of Trendelburg (active 1719+).

**Still unfound on image 765:** the index-expected "Anna Gertrud Kontze" baptism. She may be on the facing leaf (image 764 or 766) or on pages 114 / 117 (subsequent openings in Cluster N).

---

## 5. Updated Priority Queue

| Priority | Cluster | Pages | Target Image | Status |
|----------|---------|-------|-------------|--------|
| **Next** | N (cont.) | 112, 114, 117 | 765 + adjacent | Partial — confirm "Kontea von Zeylitz" and find Anna Gertrud |
| 2 | G (retry) | 48 | ~732/734 | Deferred — needs backwards-walk from image 735 |
| 3 | U | 185, 189 | ~802 | Not started — latest Andreas + Margaretha |
| 4 | H | 68 | ~743 | Not started — earliest Philipp |
| 5 | V | 196, 197, 200 | ~808 | Not started |
| 6 | E | 27, 28 | ~722 | Not started |
| 7 | L | 95, 97 | ~757 | Not started |
| 8 | R | 159 | ~789 | Not started |

---

## 6. Key Open Questions Carried Forward

1. **"Kontea von Zeylitz" (image 765)** — Is this an Andreas Kontze from Zeylitz? Re-examine with fresh zoom. If confirmed, research the Zeylitz locality and check for other Zeylitz-Kontze signals in earlier pages.
2. **Anna Gertrud Kontze baptism** — not yet located; check images 764 and 766 next session.
3. **Andreas Contze Senior's baptism** — page 48 (Cluster G) remains the critical unknown. If he was born before 1708, his own baptism would predate this register and would need to be sought in a PRIOR Trendelburg register (pre-1708 Taufen).
4. Calibration: how many separator pages exist between images 709 and 802? Known: at least one (image 733). Likely more in the Konfirmierte/Geburten/Marriage transitions.

---

## 7. Technical Note — Viewer Navigation

The Archion viewer's reliable navigation method established this session:

```javascript
const sel = document.querySelector('select');
sel.selectedIndex = N;  // N = target image index
sel.dispatchEvent(new Event('change', { bubbles: true }));
```

URL-based navigation (`?img=N`) unreliably resets to title page. The `<select>` dropdown approach is the confirmed working path.

---

*Companion docs:*
- `Register_220093_Baptism_Index_Findings_April12_2026.md` — master index & priority queue
- `Register_220093_Baptism_Page_Visits_April13_2026.md` — Clusters K, S
- `Register_220093_Baptism_Session3_Findings_April13_2026.md` — Clusters A, F
- This file — Session 4 calibration + partial N
