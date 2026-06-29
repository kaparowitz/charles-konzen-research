# Session 131 — Live Archion: locating the Weser-neighbour registers (Wahmbeck, Bursfelde)

**Date:** 27 June 2026
**Mode:** live, logged-in Archion viewer (Cowork + Claude-in-Chrome), Jed present.
**Goal:** complete the Session-130 follow-ups — sweep Bursfelde + Glashütte and Wahmbeck
on Archion; advance Oedelsheim. This run is the **catalog-location** stage.

---

## Tooling note (for future live runs)
- Archion's **place search box is a React controlled input** — programmatic value-setting does
  NOT trigger a new search (it keeps searching the prior term). The **browse tree**
  (`Alle Archive → Bundesland → Archiv → Kirchenkreis → Ort`) is plain link/anchor navigation
  and DOES work under automation; use it instead of the search box.
- The **viewer page-jump field works** via triple-click + type + Return.
- **Screenshots are the reliable read** of viewer state; `get_page_text` returned stale/parent
  content on this SPA.

## 1. Wahmbeck (Kirchenkreis Uslar) — REGISTER LOCATED, covers the window
- Holdings: Beerdigungen 1853–1907; Kirchenbuch 1673–1704; 1705–1737; 1737–1789;
  **Kirchenbuch 1790–1845 = churchRegister `359497`** (Signatur lokal 03-08145); Kirchenbuch
  1846–1852; Taufen 1853–1899; Trauungen 1853–1907.
- The **1833–1841 window sits inside reg. 359497** (combined book: Taufen / Trauungen /
  Beerdigungen catalogs in separate runs).
- **Calibration started:** image 130 = **Seite 123 = "Mortuorum Catalogus de a^o 1804 / 1805"**
  (the deaths section). Baptisms (Natorum/Getauften Catalogus) for the window are in a
  different run of the book — still to be located by probing.
- **No AI text recognition** for this book ("Bisher keine Texterkennung" / "Order text
  recognition (queue)"). Read path = **by-eye Kurrent**, or order OCR and wait.
- Status: **located + reachable, window read OUTSTANDING.** (Upgrades Session 130, which had
  "Archion not swept" and no register ID.)

## 2. Bursfelde + Glashütte — NOT digitised for the window on Archion (Uslar)
- Archion's only Bursfelde book is the **Kirchenbuch 1639–1746** filed under **Fürstenhagen,
  Kirchenkreis Uslar** — entirely **before** the 1833–1841 window.
- No 1830s Bursfelde/Glashütte volume appears under Kirchenkreis Uslar. Per Session 130 the
  settlements are administratively **Hann.-Münden, Ortsteil Hemeln**, so any window register
  would sit under **Kirchenkreis Hannoversch-Münden / Hemeln** (not yet checked) — otherwise
  the window is **on-site / OSB-only** (Kunze OSB already mined: Gans ×4, no Konze).
- Status: **window register not available under Uslar; check Hann.-Münden/Hemeln next, else
  on-site.**

## 3. Oedelsheim
- Unchanged from Sessions 127/128/130: the faded K(ontze) index leaf (reg. 219946 Bild 918) +
  shuffled reel need a **shuffle-aware leaf sweep / Kurrent specialist** (Peter Schräder).
  Not advanced this run.

## 1a. Wahmbeck — PROVISIONAL by-eye scan of the window births (reg. 359497)
**OCR ordered** this run ("Texterkennung beauftragt — in Warteschlange") so a certifiable
machine read will follow. Pending that, a by-eye scan of the legible **Geburts-Register**
leaves was done (viewer note: high zoom triggers an overlapping-leaf render glitch on this
reel; read at fit/moderate zoom).

Leaves viewed (page-map being built):
- **img 97** = Geburts-Register **1835** (header) → 1836; **img 96** = **1835** births
  ~April–December (entries 3–17, dates 2 Apr → 3 Dec 1835); **img 100** = Geburts-Register
  **1838** (Seite 99); **img 235** = Copulations-Register **1839** (Seite 232).
- Window calibration: **Geburts-Register ~1835 ≈ img 96–97; 1838 ≈ img 100** (births section);
  deaths 1804/05 = img 130; marriages 1839 = img 235.

**Surname pool (all leaves viewed): entirely local Solling/Weser names** — König, Otte,
Kettler, Bücker, Wittrop, Hesse, Ahrens, Baase, Strohmann, Grote, Pape, Mareker, Meinecke,
Friese, Brand, Niemeyer, Henne, Rave, Buurmann, Schaack, Könnemund, Garbe, Böing, Kniestädt.
**No Gans / Ganß / Gansen / Konze / Kontze surname appeared on any leaf viewed.** The forename
**Carl/Karl recurs but always on a local surname** (e.g. Carl Friedrich Wilhelm Henne;
Christian Carl Friese; Carl Heinrich Garbe).

**PROVISIONAL VERDICT: NEGATIVE for the Konze/Gans pool in Wahmbeck's window births** — the
parish surname pool is local, consistent with Wahmbeck having **no Kunze OSB** (no attested
pool surname). **Caveats:** (1) the **January-1835 head of the 1835 section (entries 1–2,
incl. any 26-Jan birth) was on the glitch-prone leaf and not cleanly read** — left to the OCR;
(2) not a full leaf-by-leaf certification. Confirm against the **queued Archion OCR** or a
Kurrent reader before treating as final.

## Bottom line
Registers located/clarified; the actual window reads remain. Reliable completion needs either
(a) Archion **OCR ordered** for Wahmbeck 359497 then read, (b) the **daily scheduled task**
repointed onto these targets (one parish/run, in the logged-in browser), or (c) **Peter
Schräder** for the Kurrent-heavy / faded books (Oedelsheim; Wahmbeck if OCR not ordered).
A provisional by-eye scan of the Wahmbeck window is possible but would warrant a second eye.

---

## UPDATE — 27 June 2026 (Session 24): Wahmbeck 1835 January head now read

The OCR ordered above had **not processed** (panel still "Bisher keine Texterkennung"), so the
outstanding Jan-1835 head was read by eye. **Calibration correction:** the year map above was off by
one — **Bild 96 = 1836**; the 1835 Geburts-Register is **Bild 93 (Seite 92, entries 1–6 = Jan head) →
94 (7–21) → 95 (22–29)**. Stale-canvas glitch on jumps: toggle txt off + click a zoom button to redraw.

**1835 entries 1–6 (Bild 93 right):** 1 Elend (m, 7 Jan) · 2 König (f, 18 Jan) · 3 Böger (f, 24 Jan) ·
4 Bunzendahl (f, 27 Jan) · 5 **Caroline Charlotte _Gans_** (f, 8 Feb, illegitimate — mother Caroline
Bremer, alleged father **George Christian Gans** "aus Gestelwarder" [?Gieselwerder]; child d. 1836) ·
6 Friedrich Wilhelm **Carl** Schrader (m, 13 Feb).

**Result:** **no male born 26 Jan 1835** (late-Jan births all girls); **no Carl on a pool surname**
(the Gans is a girl, d. 1836; the only male Carl is a Schrader) → **NEGATIVE for Charles.** *But the
Gans pool surname IS present* at Wahmbeck in the window — this **overturns the provisional "no Gans"**
above and adds Wahmbeck to the Weser-ring Gans cluster. Full detail in `Tier1_Search_Log_June2026.md`
Session 24; coverage page updated (Wahmbeck → "Searched + Gans found").
