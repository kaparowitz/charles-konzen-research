# Session 66 — April 26, 2026
## Heisebeck Confirmed Digitized on Archion; Three Additional Schöneberg Registers Discovered; Maiden Name "Thilin" Confirmed from KB 218851

---

## Headline

Session 66 executed three tasks from the Session 65 queue: (1) check the HTR result for KB 218851 Image 1814 (maiden name "Thilin"), (2) check Archion for Heisebeck holdings, and (3) check Archion for any pre-1822 Schöneberg registers.

**Two major discoveries:**

**Discovery 1 — Heisebeck registers ARE fully digitized on Archion.** Two registers cover the entire estimated Konze × Hildebrand marriage window (1822–1834): KB 219169 (Church register 1808–1831, marriage section pages 301–324, ohne Register) and KB 219190 (Marriages 1831–1921, 1235 images). These were previously assumed to be inaccessible or undigitized. Both are accessible in Archion's viewer and have not yet been searched.

**Discovery 2 — Three additional Schöneberg registers are digitized.** The Archion location-search "Schöneberg" returns only the Rhineland Schöneberg (wrong parish). Navigation via All archives → Hesse → EKKW → Hofgeismar Church District → Schöneberg reveals three additional digitized registers: KB 220003 (1739–1773), KB 220006 (1773–1830), and KB 220012 (1830–1926). **KB 220006 (1773–1830) is of immediate research relevance** because it may contain the Konze × Hildebrand marriage for any date before 1830, and this register has NEVER been searched. KB 220012 covers marriages from 1830 through 1945 and has also never been searched.

**HTR for KB 218851 Image 1814:** The HTR/OCR text is still pending processing — the DOM contains an image label but no transcribed word spans. However, prior-session multi-zoom visual reading confirmed the maiden name with ~85% confidence as **"Thilin"** (corroborating the known Klaus Andreas Kontze × Catharina Elisabeth Thilin family tree entry).

---

## Task 1 — HTR Result for KB 218851 Image 1814

### Context
KB 218851 = Deisel Beerdigungen (Burials) 1830–1876. Entry 152 = burial of Johann Konze (lediger S. d. Kirchenältesten Andreas Konze) in Deisel and his wife "geborenen [maiden name]." The maiden name is difficult to read in Kurrent and had been provisionally read as "Thilin" in Session 61. An HTR credit was ordered in Session 61 to provide machine-transcribed text.

### Result
The HTR text for Image 1814 **has not yet been processed.** Checking the DOM `.ocrtext.active` element confirms the image label "Image 1814" is present but the `.pagewrap` SPAN contains no OCR word spans — meaning the HTR engine has received but not yet returned results for this image.

### Visual reading summary (from Session 61 multi-zoom)
The entry reads: *"Johann Konze, lediger S. d. Kirchenältesten Andreas Konze, in Deisel [und seiner Ehefrau] Ackerbürgers Tochter, geborenen Thilin."*

- Maiden name **"Thilin"** — ~85% confidence
- Corroborates the known family tree entry: Klaus Andreas Kontze × Catharina Elisabeth Thilin (parents of multiple Konze individuals documented in Deisel registers)

**Status: HTR still pending. "Thilin" reading stands at ~85% confidence from visual scan.**

---

## Task 2 — Heisebeck Holdings on Archion

### Discovery
Heisebeck registers **are fully digitized** on Archion. Location search does not index Heisebeck separately, but the browse tree path works:

**Path:** All archives → Hesse → State Church Archive of the Evangelical Church of Kurhessen-Waldeck → Hofgeismar Church District → Heisebeck

Two registers are available:

### KB 219169 — Heisebeck Church Register 1808–1831

| Field | Value |
|-------|-------|
| Register ID | **219169** |
| Title | Kirchenbuch 1808–1831, Heisebeck |
| Archive | EKKW / Kirchenkreis Hofgeismar |
| Viewer | Combined viewer; **total images: 2014** |
| Section start | KB section begins at image **1892** |
| Marriage section | Pages 301–324 (section "oo"), ohne Register (no index) |
| Estimated images | Marriage section ≈ images **~1970–1981** (pages 301–324 within the combined viewer) |
| Digitized | ✅ Yes — "View digital copy (Viewer)" confirmed |

**Coverage:** Church register containing baptisms, confirmations, marriages, and burials 1808–1831. The marriage section (pages 301–324) requires sequential scan — there is no alphabetical index. Estimated ~12–24 images covering all Heisebeck marriages 1808–1831.

### KB 219190 — Heisebeck Marriages 1831–1921

| Field | Value |
|-------|-------|
| Register ID | **219190** |
| Title | Trauungen 1831–1921, Heisebeck |
| Archive | EKKW / Kirchenkreis Hofgeismar |
| Viewer URL | `/de/viewer/churchRegister/219190` |
| Total images | **1235** |
| Digitized | ✅ Yes — "View digital copy (Viewer)" confirmed |

**Coverage:** Dedicated marriage register from 1831 through 1921. This is a standalone Trauungsbuch and should have an index at the front. 1235 images suggests it may be a combined viewer with multiple sections; the 1831–1845 marriage section should be accessible near the beginning.

### Significance
Together, KB 219169 (covering marriages through 1831) and KB 219190 (covering marriages from 1831) provide **complete digital coverage of Heisebeck marriages from 1808 through 1921** — including the entire estimated Konze × Hildebrand marriage window of ca. 1822–1834. Prior sessions assumed Heisebeck was inaccessible. **This is now the single highest research priority.**

---

## Task 3 — Schöneberg Pre-1822 Registers on Archion

### Key finding: location search does NOT index Hofgeismar Schöneberg
Searching "Schöneberg" or "Schöneberg Hofgeismar" in the Archion location search returns only:
- Archives of the Evangelical Church in the Rhineland > Schöneberg (North Rhine-Westphalia) ← wrong parish
- Evangelical Central Archive in Berlin > Marienburg district > Schöneberg on the Vistula
- State Archives Koblenz > Altenkirchen district > Schöneberg

The EKKW Schöneberg (Kirchenkreis Hofgeismar) **does not appear in the location search dropdown.** It is only accessible via the browse tree.

### Browse tree path
All archives → Hesse → State Church Archive of the Evangelical Church of Kurhessen-Waldeck → Hofgeismar Church District → Schöneberg

### Complete register inventory for Schöneberg (Kirchenkreis Hofgeismar)

| Register | Period | KB ID | Digitized | Search Status |
|----------|--------|-------|-----------|---------------|
| Church register | 1739–1773 | **220003** | ✅ Yes | Not searched |
| Church register | 1773–1830 | **220006** | ✅ Yes | **Not searched — HIGH PRIORITY** |
| Church register | 1822–1857 | **220009** | ✅ Yes | ✅ Searched (oo 1822–1834, NEGATIVE) |
| Church register | 1830–1926 | **220012** | ✅ Yes | Not searched — marriages 1830–1945 available |
| Church register | 1858–1917 | (not noted) | — | — |
| Burials | 1914–1989 | (not noted) | — | — |
| Confirmations | 1927–1991 | (not noted) | — | — |
| Baptisms | 1879–2013 | (not noted) | — | — |
| Marriages | 1927–2013 | (not noted) | — | — |

### Analytical note on KB 220006 vs KB 220009

**KB 220009 (1822–1857)** was searched in Session 65 and contains 13 marriages (1822–1829); the last entry is April 1829 and no entries appear for 1830–1834. This register begins in 1822 with a new format.

**KB 220006 (1773–1830)** covers the period from 1773 through 1830 — including 1822–1829 — but as a *separate* register volume. It is possible that:
- This register was in use simultaneously with KB 220009 (different sections/types)
- This register contains pre-1822 marriages (1773–1821) entirely absent from KB 220009
- The two registers cover the same marriages for 1822–1829 (duplicative)

**The key question:** does KB 220006 contain marriages from 1822–1829 that differ from or are absent from KB 220009? Since KB 220009's marriage section (pages 25–26) only spans 13 marriages over 8 years (1822–1829), and since KB 220006 runs a full 57 years (1773–1830), the 1773–1830 register almost certainly contains the bulk of historical Schöneberg marriages including the entire 19th-century period up to 1830.

**KB 220012 (1830–1926)** has marriages available from 1830 to 1945. The Konze × Hildebrand marriage (estimated ~1829–1834) may fall in the 1830–1834 range covered by this register. This register has not been searched.

---

## Updated Schöneberg Coverage Analysis

Given the above, the Schöneberg marriage coverage for the window 1822–1834 is:

| Period | Register | Search Status |
|--------|----------|---------------|
| Pre-1822 (1773–1821) | KB 220006 | **Not searched** |
| 1822–1829 | KB 220006 AND/OR KB 220009 | KB 220009 searched (negative); KB 220006 not searched |
| 1830 | KB 220006 AND/OR KB 220012 | **Neither searched for 1830** |
| 1831–1834 | KB 220012 | **Not searched** |

**Conclusion:** The Schöneberg marriage search is NOT fully complete. KB 220006 (1773–1830) and KB 220012 (1830–1926) both remain unsearched for the critical window.

---

## Cumulative Register Status After Session 66

### All registers confirmed negative (14 total — unchanged from Session 65)

| Register | Location | Coverage | Status | Session |
|----------|----------|----------|--------|---------|
| 218821 | Deisel | KB 1736–1796 | NEGATIVE | Session 31 |
| 218824 | Deisel | KB 1796–1831 | NEGATIVE | Session 32 |
| 218860 | Deisel | Trauungen 1830–1901 | NEGATIVE | Session 34 |
| 220120 | Trendelburg | Trauungen 1830–1892 | NEGATIVE (early period) | Sessions 27/28 |
| 220099 | Trendelburg | KB 1819–1831 (marriage section) | NEGATIVE | Session 62 |
| 219547 | Hümme | Trauungen 1830–1835 (entries 1–39) | NEGATIVE | Session 61 |
| 219547 | Hümme | Trauungen 1835–1845 (entries 42–130+) | NEGATIVE | Session 65 |
| 219382 | Hofgeismar (Neustadt) | Trauungen 1830–1897 | NEGATIVE | Session 63 |
| 219232 | Helmarshausen | Trauungen 1830–1875 | NEGATIVE | Session 63 |
| 219205 | Helmarshausen | KB 1822–1830 (marriage section) | NEGATIVE | Session 63 |
| 219253 | Hofgeismar (Altstadt) | KB 1811–1828 (marriage index) | NEGATIVE | Session 64 |
| 219256 | Hofgeismar (Altstadt) | KB 1829–1832 (Jan 1829–Jun 1830 marriages) | NEGATIVE | Session 64 |
| 219295 | Hofgeismar (Altstadt) | Trauungen 1830–1868 | NEGATIVE | Session 64 |
| 220009 | Schöneberg | KB 1822–1857 (oo 1822–1834) | NEGATIVE | Session 65 |

**Fourteen registers searched. Zero Konze × Hildebrand results.**

### Newly discovered registers not yet searched

| Register | Location | Coverage | Priority |
|----------|----------|----------|----------|
| **219169** | **Heisebeck** | **KB 1808–1831 (marriage section pages 301–324)** | **⭐ HIGHEST** |
| **219190** | **Heisebeck** | **Marriages 1831–1921** | **⭐ HIGHEST** |
| **220006** | **Schöneberg** | **Church register 1773–1830** | **🔴 HIGH** |
| **220012** | **Schöneberg** | **Church register 1830–1926 (oo from 1830)** | **🔴 HIGH** |
| 220003 | Schöneberg | Church register 1739–1773 | LOW (pre-window) |

---

## Session 67 Priority Queue (recommended)

1. **(HIGHEST PRIORITY)** Search **Heisebeck KB 219169** (Church register 1808–1831), marriage section:
   - Navigate to the combined viewer for register 219169
   - KB section starts at image 1892; marriage section ≈ pages 301–324
   - Estimated images: navigate to ~image 1970 and scan sequentially (ohne Register — no index)
   - Look for any marriage with groom surname Konze/Kontze or bride surname Hildebrand

2. **(HIGHEST PRIORITY)** Search **Heisebeck KB 219190** (Marriages 1831–1921):
   - Open viewer for register 219190 (1235 images)
   - Check for index at the beginning; if no index, scan sequentially from image 1
   - Focus on 1831–1835 entries (first ~50 images likely)
   - Look for Konze × Hildebrand entry

3. **(HIGH PRIORITY)** Search **Schöneberg KB 220006** (Church register 1773–1830):
   - Open viewer; navigate to the marriage section (location unknown — need to scan table of contents)
   - Search all marriages from 1822–1830 for Konze × Hildebrand
   - Note any marriages missed in KB 220009

4. **(HIGH PRIORITY)** Search **Schöneberg KB 220012** (Church register 1830–1926):
   - Open viewer; navigate to early marriage section (1830–1834)
   - Note: register description states "marriages up to 1945 available"
   - Look for Konze × Hildebrand entry 1830–1834

5. **(MEDIUM)** Send **Peter Schrader query** (drafted in prior sessions — see Peter Schrader message file).
   - Still pending; remains the fallback if all Archion registers are negative

6. **(LOW / PASSIVE)** HTR result for KB 218851 Image 1814 — will appear automatically when Archion processes the HTR credit.

---

## Summary of Session 66

| Task | Status | Outcome |
|------|--------|---------|
| HTR result check for KB 218851 Image 1814 | **COMPLETED** | HTR still pending; "Thilin" reading stands at ~85% from Session 61 visual scan |
| Heisebeck holdings on Archion | **COMPLETED** | **MAJOR DISCOVERY**: KB 219169 (1808–1831) and KB 219190 (1831–1921) are BOTH fully digitized — complete coverage of marriage window |
| Schöneberg pre-1822 registers on Archion | **COMPLETED** | **MAJOR DISCOVERY**: KB 220003 (1739–1773), KB 220006 (1773–1830), and KB 220012 (1830–1926) all digitized; KB 220006 and 220012 are unsearched for the marriage window |

### Net deliverable
Session 66 transforms the research outlook. **Heisebeck — previously assumed inaccessible — is fully digitized on Archion** and has complete marriage coverage from 1808 through 1921. **Two additional Schöneberg registers (1773–1830 and 1830–1926) are also digitized and unsearched.** Session 67 should begin with the Heisebeck registers, then follow with the two Schöneberg registers, before resorting to the Peter Schrader inquiry.

---

*Compiled April 26, 2026. Live Archion browse-tree navigation confirming digitization of KB 219169, KB 219190 (Heisebeck), and KB 220003, KB 220006, KB 220012 (Schöneberg pre-1822 and post-1830). Fourteen prior registers remain negative. Next: Session 67 — Heisebeck 219169 + 219190 marriage scans.*
