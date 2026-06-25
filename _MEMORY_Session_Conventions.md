# Charles Gannsen Research — Persistent Session Memory

**Read this file at the start of every new session.** Jed has asked that I not
need to be re-reminded of these conventions each session.

---

## Archion viewer conventions

- **Use JavaScript zoom via the in-page viewer when native screenshot zoom
  is insufficient.** The `javascript_tool` action lets you execute code in
  the page context; use it to set CSS transforms, call the viewer's internal
  zoom methods, or pull the underlying image URL for direct high-resolution
  inspection.
- When the `javascript_tool` output is `[BLOCKED: Cookie/query string data]`,
  the result contained sensitive strings. Return the value in a different
  shape (e.g., replace URL query strings with `…`, or count characters
  instead of returning them) to get the inspection you need.
- Archion's viewer renders the register page as an `<img>` whose `src` points
  to a tiled image resource; typical tricks:
  - Read the top-header "Seite" number by clicking the `+` zoom button several
    times then screenshotting the upper right corner of the right page.
  - Use the native computer `zoom` action on the captured screenshot to
    re-magnify small regions without losing text quality.
  - Use JavaScript to set `document.documentElement.style.zoom = '3'` or
    apply a CSS `transform: scale(3)` to the viewer container to force
    oversize rendering, then screenshot again.
- The image counter in the top-left input field is a **1-indexed image
  number**, not an "option". For Register 220108 the relationship is:
  **Seite = image − 1378** (one full table-Seite per image; verified Session 93
  — the older "image = 1375 + option" note mis-mapped several Seiten).
  Always confirm the written Seite/Jahr header before reading; the image-number
  input is flaky (stale canvas) — force a redraw via the zoom buttons.

## Seite-to-image map for Register 220108 (Trendelburg Taufen 1830-1863)

| Image | Option | Seite | Year/Month |
|---|---|---|---|
| 1397 | 22 | ~7  | 1831 early |
| 1448 | 73 | 70  | 1838 Apr/Mai |
| 1621 | 246 | 220 | 1856 Apr-Juni |
| 1647 | 272 | 242 | 1861 Feb/März |
| 1648 | 273 | — | alphabetical index (N/O section) |

Seite/image ratio over the whole register ≈ **1 Seite per 1.15 images**.
The register ends around Seite 245-250; the alphabetical index follows.

## Session-log and file-versioning conventions

- **Session logs** → `SessionNN_<topic>_<date>.md` in the workspace folder.
- **Word-doc versions** → `Kontze_Konze_Complete_Family_Reconstruction_<date>_v<NN>.docx`
  — always create a new `v<NN+1>`, never overwrite.
- Always save final outputs to the user-selected workspace folder
  `/sessions/<current-session>/mnt/Charles Gannsen Research/` and share them
  with `computer://` links.

## Site editing conventions — keep main pages clean

**Rule (added May 2026, per Jed's instruction):** Do NOT clutter the main
site pages (`index.html` Civil War / Germany / Immigration tabs, the per-tab
deep-dive landing pages like `civilwar/places-served.html`,
`towns/index.html`, etc.) with the latest research-in-progress.

- **Main pages** → only summaries, "At a glance" sections, and stable findings.
  When research updates the conclusion, update the summary; do NOT paste the
  granular forensic analysis onto the main page.
- **Research logs** → put granular hypothesis testing, source-by-source
  evidence diffs, eliminated candidates, and date-stamped investigation
  entries in a dedicated log file. Conventional locations:
  - `civilwar/<topic>-research-log.html` for Civil War threads
  - `germany/<topic>-research-log.html` for German-side threads
  - `notes/Session<NN>_<topic>_<date>.html` for one-off session notes
  Cross-link from the main page's summary to the log; never the reverse.
- **When folding a finding into the site**: the *summary* on the main page
  states the working answer in 2–3 sentences; the *log* contains the
  hypothesis tree, the eliminated candidates, the verbatim source quotes.
- **Existing example (May 2026)**: the Fort Wyman / 64th Illinois mystery —
  full investigation lives at `civilwar/fort-wyman-research-log.html`;
  Civil War tab on `index.html` carries only a 2–3 sentence summary linking
  to the log.

## Project facts (stable across sessions)

- **Target**: Charles Gannsen, Civil War pvt., b. 26 Jan 1835, of German origin.
- **Leading hypothesis**: Born in Kurhessen to a Konze/Kontze family, later
  anglicised "Gannsen". Parish candidates = Deisel, Trendelburg,
  Friedrichsfeld, Helmarshausen.
- **Confirmed**: Three "geb. Konzen" mothers in Deisel 1828-1829
  (Maria Elisabeth, Wilhelmina, Carlotta).
- **Breakthrough (Session 18)**: Register 220108 Trendelburg Taufen 1830-1863
  alphabetical index lists "Konze, Johann Friedrich Wilhelm — 243" — the
  first Konze father-surname baptism confirmed in post-1831 Trendelburg.
  The "243" is a Seite page number (not a Nro.); Session 20 is executing
  the Seite 243 transcription.
- **Jungkonze** (compound surname) is attested in Trendelburg 1829 baptisms
  as a separate father-surname variant.
- **Hümme Kontze cluster (complete 23 June 2026):** a substantial multi-household
  Kontze population, NOT extinct (earlier "no Kontze baptism 1830-58" finding
  overturned). All 10 indexed Kontze baptisms in Taufen 1830-1863 pulled & cited;
  FIVE father-households: (1) Johannes the Leineweber (×Lichtefeld → Heinrich
  b.1823; then ×Marie Magdalene Uffelmann → Conrad 1833, Wilh. Friederike 1834
  posth.; DIED ~mid-1834); (2) a SECOND Johannes (Leineweber/Tagelöhner) ×Marie
  Christine Hofedietz "von Naumann" → Friedrich 1841; (3) Georg Friedrich
  (Tagelöhner/Bauaufseher) ×Kuhlmann v.Eberschütz → Anne Rosine 1830, Heinrich
  Friedrich 1843, Wilhelm 1848; (4) Friedrich ×Wilhelmine Büngener → Conrad 1844,
  Christoph Heinrich 1847, Elise Amalie 1852; (5) Wilhelm (Leineweber) ×geb. Busch
  → Maria 1852; plus Heinrich ×Marie Elisabeth Büngener (confirmation reg).
  "Naumann" is confirmed a REAL place (S81 entry), reopening Naumann-vs-Stammen
  for Johannes-the-Leineweber's origin. Full table + permalinks in
  `germany/huemme-research-log.html` and `germany/219532_image-seite-map.md`.
- **Surname canon = nine distinct American spellings** (updated June 2026, was
  eight): Gonnson · Gansen · Gonsen · Konsen · Gonson · Jansen · Konzen ·
  **Gannsen** · Conson. The count is data-driven from
  `data/surname-attestations.json` (rendered by `scripts/surname_canon.py`) and
  is never hard-coded, so it updates with the JSON. Site pages should read
  "nine distinct"; older "eight distinct" / "seven distinct" strings are stale.
- **Candidate-families canon = 16** (per the `negative-results.html#families`
  roster, which lists 16 eliminated families). The home page was reconciled
  from a stale "13" to 16 in June 2026; documentary changelog/errata entries
  retain their period numbers.

## Priority queue (inherited from Session 19, now executing)

1. 220108 Seite 243 — Konze Johann Friedrich Wilhelm full transcription
   (parents, birth date, baptism date, witnesses, death marginalia).
2. 220108 Jan 1835 — Charles Gannsen phonetic-variant scan.
3. 220099 Nov-Dec 1829 — Justus Ernst Konze / Jungkonze scan.
4. 220099 1828 full page-by-page at max zoom.
5. 218842 K section max-zoom re-check.
6. Hamburg/Bremen passenger lists 1850-1859 (Ancestry, not Archion).

## Register calibrations (verified Sessions 93–94)
- 220108: Seite = image − 1378. 220099: identify pages by header.
- 220096: baptisms image = 984 + Seite/2; burials image = 1176 + (Seite−356)/2.
  Taufen alphabetical index at END of Taufen section (Session 97): imgs 1095/1097 (A–B),
  1098 (C–G; Contze under C with "s. auch K!"), 1099 (H–K start), 1100 (Q–T),
  1101/1102/1104 (U–Z); K(cont)–P leaf UNFILMED in both passes — Kontze-spelled
  baptisms (incl. Anton Wilhelm S.151) must be found directly. Konfirmationen start
  S.223 = img 1101 right / 1105 = S.224–225. Download endpoint can 503 under load —
  do evidence downloads at session START before heavy viewer use.
  Images 1043–1058 JUMBLED w/ duplicates: 1043=1049=S.118–19, 1044=120–21, 1045=122–23,
  1050=1052=136–37, 1051=134–35, 1053=1057=132–33, 1054=146–47, 1055=142–43, 1056=144–45,
  1058=148–49. S.138–141 (1804) NOT FOUND in this stretch — try imgs 1046–1048.
- 218824: image = 1827 + ceil((Seite−1)/2) for burials; alphabetical indexes at the end
  (Taufregister K imgs 1886–87, Begräbnisregister K img 1883).
- 218851: Seite = image − 1784; register ENDS 22 Apr 1876; index continuation pages hide
  on unused letter pages (K→img 2054/2055→C img 2048→Z imgs 2068–69); S.92–117 unindexed.
- 218842: image ≈ Seite+1 (drifts to +2 from ~S.210); index K img 272 → C img 265 → X img 284.
- 220093: baptisms start img ~709 (S.1=1708); own name-register at S.251 (img 835, letter K).
- 219532 (Hümme Taufen 1830-1863, 1492 imgs; **COMPLETE 23 June 2026**): register is WELL-ORDERED at
  **image = Seite + 1208** (title page img 1206; baptism Nro1/Seite1 = img 1209; alphabetical K index
  leaf = img 1476, p/695988191b). ⚠️ The "shuffle/duplicate chaos" logged on 22 June was a STALE-CANVAS
  ARTIFACT, NOT real: after typing an image number the viewer shows the PREVIOUS leaf until a zoom action
  forces a redraw, so immediate screenshots read the wrong page. **FIX: after every page-number jump,
  click a zoom +/− button to force a redraw, THEN read the Seite header.** With that, all targets sat
  exactly at image=Seite+1208. (Lesson: trust SEQUENTIAL next-page reads; always redraw after a jump.)
  ALL 10 indexed Kontze baptisms pulled & cited (full table in germany/219532_image-seite-map.md and the
  research log): S4 Anne Rosine 1830 (img1212 p/55c3f399a7); S20 Conrad 1833 (1228 p/0636506e1e); S32
  Wilhelmine Friederike 1834 posth. (1240 p/aac9a2afde); S81 Friedrich 1841 (1289 p/a94361a969); S96
  Heinrich Friedrich 1843 (1304 p/84af9a31f5); S101 Conrad 1844 (1309 p/ca6fea7790); S119 Christoph
  Heinrich 1847 (1327 p/2982e4389d); S127 Wilhelm 1848 (1335 p/0ca790f2cf); Maria 1852 + Elise Amalie
  1852 (both Seite ~175, img1386 p/1107ea6d56). FIVE father-households: (1) Johannes Kontze Leineweber
  ×Lichtefeld(son Heinrich b.1823) then ×Marie Magdalene Uffelmann (Conrad 1833, Wilh. Friederike 1834),
  DIED ~mid-1834; (2) a SECOND Johannes Kontze (Leineweber/Tagelöhner) ×Marie Christine Hofedietz "von
  Naumann" (Friedrich 1841 — alive then, distinct man); (3) Georg Friedrich Kontze (Tagelöhner/Bauaufseher)
  ×Marie Christine Kuhlmann v.Eberschütz (Anne Rosine 1830, Heinrich Friedrich 1843, Wilhelm 1848); (4)
  Friedrich Kontze ×Wilhelmine Büngener (Conrad 1844, Christoph Heinrich 1847, Elise Amalie 1852; prob.
  the Friedrich w/ 1843 marriage); (5) Wilhelm Kontze (Leineweber) ×geb. Busch (Maria 1852). NOTE: S81
  proves "Naumann" is a REAL place (Marie Christine Hofedietz "von Naumann") — reopens Naumann-vs-Stammen
  for the 1837 confirmation entry (219529 img16).
- 205541 (Nürnberg-St. Sebald Taufen 1770-1800, Bayern; 657 imgs, normal chronological order,
  ≈1.9 written pages/image): img 165 = pp.320/321 (1777 Aug); img 183 = pp.354/355 (June 1778);
  **img 184 = pp.356/357 (July 1778)**; img 226 = pp.438/439 (Aug 1780); img 249 = pp.480/481 (Apr 1781).
  Image-number input is STALE-CANVAS prone after a jump — click the viewer "+" once to force a tile
  redraw, then read the written page header before trusting position.
- 219046 (Gottsbüren Konfirmationen 1831-1932; 1946 imgs total, conf. section title page = img 1752;
  verified 22 June 2026): SHUFFLED *and* DUPLICATED like 219532 — image number does NOT track year/Seite.
  Verified year anchors (read live): img1774=1844, img1775=1845 (dup at img1788), img1777=1848-end/1849-start,
  img1778=1848 (full class), img1780=1849 (boys 7-24), img1781=1849-end/tally, img1782=1850, img1784=1851,
  img1785=1852 (boys 14-19), img1786=1851-tally/1852-mixed, img1776=1852 (boys 1-13, displaced into the
  1846/47 slot). Each class lists boys (Knaben) 1..N first, then "Mädchen". Permalink minting: chain icon →
  wait → single "Create" click (the first click after the panel opens often doesn't register — click again) →
  the short p/<hash> URL renders in the panel. Per-class permalinks in `germany/gottsbueren-research-log.html`.
  MORE anchors (residual pass 22 Jun): img1789=1853(boys), 1790-91=1853(girls), 1792=1853-tally/1854-header,
  1793=1854(full), 1794=1855, 1796=1856; dups 1773=1852, 1787=1852, 1788=1845. FULL SWEEP DONE: every class
  1844-1856 read. The book runs 1844,1845, then 1848…1856 — a clean 1845→1848 gap, NO 1846/47 class (parallels
  the 1831→1834 gap; likely a vacancy). So Gottsbüren Konfirmationen is saturated end-to-end for Charles's window;
  no boy b.1831-42 with a Konze-type surname exists in the book.
- 253444 (Grifte Taufen 1830-1883, "Amt Gudensberg", Kirchenkreis Fritzlar; 1239 imgs; verified 22 Jun 2026):
  baptism section title page = img 960; continuous Nro numbering (NOT reset yearly). Leaves partly out of
  Seite-order with DUPLICATE scans, so de-dup by the printed Jahr/Seite header. The 1833-1841 window is
  CHRONOLOGICAL across imgs 974-1007 (no displaced leaves in this stretch — unlike 219532/219046). Year
  anchors (img / printed Seite / Nro / permalink): 1833 img974-977 S10-15 Nro36-56 p/5e9fbb5e01; 1834
  img978-981 S16-19 Nro57-75 p/888da2375f; 1835 img982-985 S20-23 Nro76-93 p/7ad3b1e9f5; 1836 img986-988
  S24-26 Nro94-106 p/553344dd8f; 1837 img989-992 S27-30 Nro107-123 p/af7eb3c298; 1838 img993-997 S31-35
  Nro124-142 p/56065192a8; 1839 img997-1001 S35-39 Nro143-163 p/e4d6b02b7d; 1840 img1002-1004 S40-42
  Nro164-175 p/a69f63d652; 1841 img1004-1007 S42-45 Nro176-192 p/2f1f861858 (rolls into 1842 at Nro193).
  RESULT: full 1833-1841 window read leaf-by-leaf (every child-name column) = NEGATIVE for Charles — no boy
  named Carl as rufname, no Konze/*n-s-n surname, no 26-Jan-1835 birth (1835 opens mid-Feb). ONLY "Carl" in
  the window = Nro73 (1834, img981/S19), male "Ludwig Daniel Carl" (Carl = 3rd given name), father Tagelöhner
  on a local non-matching surname (best read Paul/Wilmes-type), mother geb. Grünewald. Grifte ELIMINATED;
  detail + permalinks in `germany/grifte-research-log.html`. Permalink minting on this viewer: chain icon →
  wait → ODD number of "Create" clicks (1 click mints; a 2nd click resets to the form) → p/<hash> renders.
  **CONFIRMATION-BOOK CHECK (24 Jun 2026):** Grifte Archion holdings inspected directly = NO Konfirmationen register
  (only Beerdigungen x2, Kirchenbuch 1649-1841 [4 vols, end 1841], Nebenkirchenbuch 1857-1876 [starts after window],
  Taufen 1830-1883 & 1884-1925, Trauungen x2) → nothing covers the 1847-55 window; label confirmed, confirmands at
  Gudensberg. WINDOW ALREADY ALIGNED: unlike Dissen, Grifte's sweep already opens at Jan 1833 (Nro36/S10/img974,
  verified) — NO extension needed; pre-1833 (Nro1-35, 1830-1832) is out of window and not read. Grifte stays ELIMINATED.
- 253403 (Dissen Taufen 1830-1924, "Amt Gudensberg", Kirchenkreis Fritzlar; 354 imgs; verified 22 Jun 2026):
  roughly CHRONOLOGICAL, ~1 written Seite per image (unlike the shuffled 219532/219046). Taufbuch title page
  = img 112; **1834 begins img 113 = Seite 8 ⇒ Seite = image − 105**. Year-leaf map (img / printed Seite /
  Nro / permalink): 1834 img113 S8 (~Nro32-39, May-Dec; no Jan-Apr births) p/a1a62dce79; 1835 img114-117
  S9-12 Nro40-55 p/548399c828 (Jan-Feb leaf img114; also p/13900adabc img115, p/b4da95f92e img117); 1836
  img118-121 S13-16 Nro56-68 p/7acbd9d4a3; 1837 img121-123 S16-18 Nro69-80 p/cd359cc57f; 1838 img124-127
  S19-22 Nro81-96 p/af7dcf9fe6; 1839 img127-130 S22-25 Nro97-113 p/9bb6d31274; 1840 img130-132 S25-27
  Nro114-124 p/f051347c8a; 1841 img132-136 S27-31 Nro125-146 p/d5032fc7c6; **1842 begins img137 S32**.
  STALE-CANVAS prone: typing a page number updates the thumbnail/index but the main canvas lags one image —
  navigate with the prev/next **arrows** (clean redraw, keeps zoom). Each leaf's top & bottom entries are
  clipped at readable zoom; drag the image to read them. Year-end tallies ("X Knaben, Y Mädchen, überhaupt
  Z Kinder") sit at each year's last entry — use to bound years (1837=12, 1838=16, 1839=17, 1840=11).
  Permalink minting: link/chain icon → wait ~2s → click "Create"; the 1st click is swallowed by a DE→EN panel
  re-render, so click "Create" again until the p/<hash> URL renders. RESULT: full 1834-1841 baptism window
  read leaf-by-leaf (~110 baptisms) = NEGATIVE — NO male Carl/Karl at all (closest = female "Maria Carolina"
  Nro125, 1841 twin); two unnamed/stillborn males (1839 Nro103, 1841 Nro142). Dissen ELIMINATED; per-year
  permalinks in `germany/dissen-research-log.html`.
  **PRE-1834 EXTENSION (24 Jun 2026):** window widened back to 1830 to match the confirmation window (births ~1833-1841),
  since Dissen keeps NO confirmation book (Archion holdings verified: only Beerdigungen 1830-1969, Kirchenbuch 1773-1841 [ends
  1841, before the 1847-55 window], Taufen 1830-1924, Trauungen 1831-1949). Calibration extends cleanly: **Seite 1 = img 106**
  (register opens Sept 1830). Year/Nro/img map: 1830 Nro1-6 imgs106-107 (p/8cf9a4f0b6); 1831 Nro7-10 img108 (p/dff2917b36);
  1832 Nro11-15 img109 (p/40187ddc2e); 1833 Nro16-32 imgs110-112 (p/281fd2b3d5 [S5, Carl August], p/193a1b8946, p/b3c5e238ff);
  1834 opens img113/S8/Nro33 ("Conrad Schmincke") — clean join to the prior sweep. RESULT: ONE in-window male Carl found =
  **"Carl August," b. 7 Jan 1833, ILLEGITIMATE (mother Mangold / father Rost), Nro16/S5/img110** — non-Konze surname, 1833 not
  1835, illegitimate → NOT Charles (near-miss like Liebenau's Carl August Büster). No Konze surname anywhere in 1830-1841.
  Full 1830-1841 window now read & cited; Dissen stays ELIMINATED.

- 219013 (Gieselwerder/Oberweser Konfirmationen 1830-1957; 2145 imgs; swept 24 June 2026): conf. section
  title page = img 1958; inner "Konfirmations-Buch … Gemeinde Gieselwerder … 1. Juli 1830" = img 1959; first
  class (1830) = img 1960. ⭐ **CLEANLY ORDERED** (NOT shuffled/duplicated like the other Hofgeismar reels
  219172/219742/219673) — two written Seiten per image at **Seite(left page) = 2 × image − 3914** (verified:
  img 1985 = S56/57 = 1850; 1984 = S54/55; 1983 = S52/53; 1982 = S50/51). Stale-canvas after a page-number
  jump (shows previous leaf until a zoom +/− forces redraw) — single-step prev/next arrows give clean redraws.
  Knaben first, then Mädchen; each class ends with a "Summa h.a. N Confirmirte, x Knaben, y Töchter". Window
  class→image map: 1847 img1981-82 (S49-50); 1848 img1982-83 (S50-52); **1849 img1983-84 (S52-55, 22=14M/8F,
  PRIME births Jan1835)**; **1850 img1984-85 (S55-57, 16=4M/12F, PRIME)**; 1851 img1985-87; 1852 img1987-88;
  1853 img1988-89; 1854 img1989-90; 1855 img1990. Permalink minting: chain icon (top toolbar ~1123,140) →
  "Create"/"Erstellen"; FIRST click triggers DE→EN re-render so click again → p/<hash>. Anchor permalink
  **Bild 1984 (1849 Summa + 1850 prime boys, births 1835) = p/b4d6bfe1ba** (verified). RESULT (1847-1855
  sweep, ~140+ entries): **NEGATIVE** — NO Konze/Kontze/Gansen/Gonsen/*n-s-n surname anywhere; surname pool is
  the local Oberweser families (Marunde, Roll, Reuß, Nickel, Hennur, Vella, Schölla, Grafmann, Grovenmann,
  Lindner, Otto, Daus, Reitz, Müller, Masserschmidt…). Exactly ONE Carl in the window = Carl Friedrich Wilhelm
  **Marunde**, b. 21 Mar 1839 (1853 class, img1988/S63) — local family, wrong surname & year. Prime 1849 + 1850
  boy cohorts hold NO Carl. Gieselwerder now searched on BOTH baptism (219016, Jan-Feb 1835) and confirmation
  (219013) tracks — still ELIMINATED. Detail in germany/gieselwerder-research-log.html + Session117 log.
- 219742 (Liebenau Konfirmationen 1831-2013; 2156 imgs; swept 23 June 2026): section title page = img 1960,
  inner "Konfirmations-Buch" title = img 1962, first class (1831) = img 1963 (both pages 1831). Spacing is
  roughly **2 images per year early on, ~1 spread/year near the target** and is NOT linear — calibrate by the
  written "Jahr 18XX" header / "Summa der Confirmanden im Jahr 18XX" tally, not arithmetic. Verified anchors:
  1837=img1975, 1847=1987, 1848=1988-89, **1849=1990 (Seite 55-56)**, **1850=1991-92 (Seite 59)**, 1851=1992-93,
  1852=1993-94, 1853=1994-95, 1854=1995-96, 1855=1997 (Seite 69-70). Each class lists **boys (Knaben) first,
  then Mädchen**; the boys are the low-numbered entries — scan those for "Carl/Karl". STALE-CANVAS prone after a
  page-number jump (shows previous leaf until a zoom +/- forces a redraw) — same fix as 219532/219046: after every
  jump click a zoom button, THEN read. Permalink minting: chain icon (top toolbar ~1085,135) → wait for panel →
  "Create"/"Erstellen"; the FIRST click triggers a DE→EN re-render, so click again, then wait ~3s for the p/<hash>
  to render. Minted: 1849 class img1990 = p/6bcd134c6b; 1849-tail/1850-start img1991 = p/0faedeb9d3.
  RESULT (confirmation sweep 1847-1855): forename Carl recurs ~9× but NEVER on a Konze/*n-s-n surname — all local
  (Büster, Krumpe, Lindorf, Lange, Schäfer, Pfennig, Reinhardt). Prime cohorts decisive: 1850 class = NO Carl at
  all; 1849 class = only Carl August Büster b.11 Jun 1835 (wrong surname & date). Liebenau confirmations now OFF
  the "undigitised/on-site" list. Detail in germany/liebenau-research-log.html.

- 218884 (Eberschütz Konfirmationen 1831-2013; 1052 imgs; swept 23 June 2026): confirmation section title page =
  **Bild 864**; first class (1831) = Bild 867 (left=1831 Seite1, right=1832). Register is WELL-ORDERED, two written
  Seiten per image at **Seite(left) = 2 × image − 1731**. Verified year anchors: Bild 884 = Seite 37/38 = 1847;
  885 = S39/40 = 1848; 886 = S41/42 = 1848-end/**1849** (1849 class starts Nro 215); 887 = S43/44 = 1849-end/1850;
  888 = S45/46 = 1850; 889 = S47/48 = 1851; 890 = S49/50 = 1851-end/1852; 891 = S51/52 = 1852-end/1853; 892 = S53/54
  = 1853; 893 = S55/56 = **1854** (Carl Höbener Nro290); 894 = S57/58 = 1854; 895 = S59/60 = 1854 (Mädchen tail);
  **896 = S61/62 = 1854-tail (left) + 1855 class START (right, Nro 314)**; **897 = S63/64 = 1855 Summa + 1856 class start**;
  898 = S65/66 = 1856 (left) / 1857 (right). STALE-CANVAS prone after a
  page-number jump (blank/previous leaf until a zoom +/- forces a redraw) — same fix as the other Kassel registers:
  after every jump click a zoom button, THEN read. Page-number INPUT is flaky (off-by-1/2 on type) — prefer the
  prev/next arrows for single steps. Each class = boys (Knaben) first then Mädchen, with name/parents/birth-date/age
  columns; the running Nro does NOT reset yearly. Class extents (Nro / Summa): 1847=188-198; 1848=200-214 (Summa15);
  **1849=215-224 (Summa 10 = 3 Knaben/7 Töchter)**; 1850=225-~241; 1851=~244-257 (Summa8); 1852=~261-275 (Summa18);
  1853=276-~288; 1854=289-308. Permalink minting: chain icon (top toolbar ~1123,140) → wait → "Create"/"Erstellen";
  FIRST click triggers DE→EN re-render so click again, then ~3s for p/<hash>. Minted: **1849 prime class Bild 886 =
  p/27e3438e7b**; **Carl Höbener Bild 893 = p/84cbde3c42**. RESULT (1847-1854 sweep, births 1833-1840): the prime
  **1849 class has NO Carl at all** (3 boys = Christian Ludwig Rode, Heinrich Wilhelm Pfingst, Heinrich Wilhelm
  Alborn); the ONLY Carl in the whole register is **Carl Wilhelm Höbener** (1854, b. Oct 1839, father Joh. Christoph
  Höbener Schuhmacher) — wrong surname (-ener), too young. NO Konze/Kontze/Gansen/Gonsen/*n-s-n surname anywhere;
  surnames are the recurring Eberschütz families (Schröder, Hoff, Thöne, Tebs, Klappe, Stein, Boß, Mengel, Vogt,
  Rode, Engelbrecht, Pfannkuche, Alborn, Jäger, Scheele, Sasse). Eberschütz now searched on BOTH baptism (Jan-Feb
  1835, reg.218887) AND confirmation tracks — negative on both; still ELIMINATED. Detail in
  germany/eberschuetz-research-log.html.
  **1841-TAIL CLOSURE (24 Jun 2026):** read the 1855 + 1856 classes leaf-by-leaf, closing the full 1833-1841 birth
  window. **1855 class = Nro 310-323, Summa 14 = 7 Knaben/7 Mädchen** (boys: Conrad Ludwig Vechel, Conrad Lorenz
  Aschermann, Conrad Engelbrecht, Friedrich Hattenbach zur Heide, Conrad Bohle, Friedrich Conrad Engelbrecht,
  Daniel Scheele — all b.1840-41; NO Carl, NO Konze; girls Reppulier/Trottier/Jaeger/Heise/Wigge/Kahle/Krone).
  **1856 class (Nro 324 ff.) is already into 1842 births** (Hempel, Bohle, Thöne, Kleppe, Blum, Schröder, Sasse,
  Scheele), so the 1841 birth-year is fully bracketed; its only Carl = **Carl Scheele Nro332, b.1842** (Scheele
  family — wrong surname, 7 yrs too young); the only in-window birth among 1856 entries is a girl (Heinze b.1840).
  Permalinks: 1855 class Bild896 = p/99fab7d71a; 1855 Summa + 1856 start Bild897 = p/0b98119acc.

- 219673 (Lamerden Konfirmationen 1831-2013; 852 imgs; **swept COMPLETE 24 June 2026, Session 118**):
  DUAL-FILMED. Filming 1 = sparse hand (~6 entries/spread, imgs ~676–695); filming 2 = "… mit Register"
  copy, denser hand (~5 entries/page, title page img 692, imgs 696–707+). Printed **Seiten are shuffled but
  the confirmation YEARS run ~linearly by image** 1846(img693)→1855(img705). Confirmation pages NOT
  AI-transcribed — read by eye. Image→year map (window block): 1846=img693 (S32/33, entries166-177);
  1848=img694-695 (entries178-189, Summa "1848: 12 Kinder, 6 Knaben 6 Mädchen"); 1849start=img695 (190+);
  filming-2 dup 1848=img696 (S28/29); 1849=img697 (S26, read S114); 1850=img698 (S42, read S114);
  **1851=img699 (S44/45, Summa "9 Kinder, 1 Knabe, 8 Mädchen" — class has a SINGLE boy)**; 1852=img700
  (S46/47); 1853 Summa=img701 (S52/53, "15 Kinder, 9 Knaben 6 Mädchen") + 1854 start; 1854=img701-704
  (S54/55); 1854tail/**1855=img705 (S56 left=1854, S57 right=1855, births 1841)**; 1855 girls=img706.
  **1847 = GAP year** (numbering runs 177→178 with no class). VIEWER QUIRKS: stale-canvas after every
  page jump — click a zoom +/− to redraw THEN read; the zoom **slider snaps back to min**, so after a jump
  click "+" ~4× to reach the readable fit-width level (digital-zoom of that screenshot reads names fine).
  RESULT: full birth-window 1833–1841 (classes 1846–1855, both filmings) = NEGATIVE. Carl recurs ~15× but
  NEVER on a Konze/*n-s-n surname; no Konze-type surname in any class. Verified N-words Nand (#183) and
  Naße (recurring) are NOT Konze. Lamerden ELIMINATED on BOTH baptism (219676, Jan–Feb 1835) and
  confirmation tracks. Detail: Session118 log + germany/lamerden-research-log.html.

- 219634 (Hofgeismar-**Kelze** KB 1830-1971, COMBINED volume — Taufen+Konf+Trauungen+Todten in one register;
  834 imgs; **swept COMPLETE 24 June 2026, Session 117**): filming title card = **Bild 364**; it lists the
  section map — `*`(Taufen) S2-166, **`Konf` S1-119 (1831-1970)**, `oo` S1-64, `+` S1-112. Konfirmationen are
  WELL-ORDERED (no shuffle): one OPENING per image, each Seite headed "Seite N — Jahr 18XX" with its own column
  set + year-end "Sa. der Confirmierten in 18XX: N. x Knaben, y Mädchen" tally; **surnames underlined**. NOT
  AI-transcribed — read by eye. Window map (confirmation classes 1847-1855 = births 1833-1841): **Bild 558 = Seiten
  14-15 (1845-1847); 559 = S16-17 (1847/1848/1849 start); 560 = S18-19 (1849 end + 1850 + 1851 start, PRIME);
  561 = S20-21 (1851/1852); 562 = S22-23 (1853/1854); 563 = S24-25 (1855 + 1856-57 out of window)**. STALE-CANVAS
  after a page jump (force redraw with a zoom +/-), AND note clicking zoom RECENTERS the view — so pan AFTER the
  redraw. Permalink minting: chain icon (full-screen toolbar ~1060,35) → Erstellen; FIRST click triggers DE→EN
  re-render, click again, ~3s for p/<hash>. Prime 1849/1850 opening Bild560 = **p/cf5d171aae**. RESULT (1847-1855,
  NEGATIVE): every confirmand bears a tight **French-Huguenot-colony** surname set (Bonnet, Benoit, Morell, Monard,
  Morin, Croll, Briede; maiden names Seguin/Paschal/Ruddenklau) + Homburg, Weidemann, Stalknecht, Siebert,
  Finis/Tinnes, Jäger, Martin, Schöning, Rudolph — **NO Konze/Kontze/Gansen/*n-s-n surname anywhere**; a German
  Diemel-valley Konze would be conspicuous in a Huguenot colony. Sole window Carl = **Carl Wilhelm Homburg, b. 4 Dec
  1835** (1850 class, Homburg surname — wrong surname, Dec not Jan). The **1849 class (exact cohort for b. 26 Jan
  1835) has NO Carl** (Summa 5 = 4 Knaben/1 Mädchen: F.W. Homburg, L. Finis, C. Benoit, M. Weidemann, C.E. Monard).
  Kelze now ELIMINATED on BOTH baptism (Jan-Feb 1835) and confirmation tracks. Detail: Session117 log +
  germany/kelze-research-log.html.

- 181895 (Marzhausen Konfirmationen 1831-2011, Kirchenkreis Witzenhausen; 1985 imgs; **swept 24 June 2026**):
  the reel bundles all Marzhausen books; the **Konfirmationen section title card = Bild 1886**, classes begin Bild 1888/1889.
  WELL-ORDERED (no shuffle): early on **one written Seite per year**, two Seiten per image — **Bild 1889 = Seite 2/3 =
  Jahr 1832/1833**. Once classes pass ~8 confirmands (from ~1848) a class spills across pages, so TRACK BY THE WRITTEN
  "Jahr 18XX" HEADER + year-end "Sa." tally, NOT arithmetic. Window anchors (verified live): 1846 S16/1847 S17 = Bild 1896;
  1848 S18/1849 S19 = Bild 1897 (p/dbb3c41e3d); 1850 S20/1851 S21-start = Bild 1898; 1851-tail S22/1852 S23 = Bild 1899
  (p/d1bd38401c); 1853 S24/1854 S25 = Bild 1900; 1855/1856 = Bild 1901. Stale-canvas after a page-number jump — after
  typing an image number click a zoom +/− to force a redraw THEN read; the redraw click also bumps zoom, so re-fit with "−"
  if it over-zooms. Permalink minting: chain icon (~1123,140) → "Erstellen"; FIRST click triggers a DE→EN re-render (button
  becomes "Create"), click "Create" again → p/<hash>. RESULT (classes 1846-1856, fully bracketing births 1833-1841):
  NEGATIVE. No boy with rufname Carl/Karl on a Konze/Kontze/Gansen/*n-s-n surname; the prime 1849 class had only 2 boys
  (Lambach b.1834, Andreas Wilhelm Adolf Wilhelm b.1835). Carls present, all non-matching: Carl Wilhelm Apel (1846, b.1832),
  Carl Ullrich (1847, b.1832), Karl Heinrich Wilhelm Grimme (1852, b.~Dec 1837 — only Carl-rufname in window, but local
  Friedland Grimme family); + middle-name Karls (Günther 1848, Jacob Carl Leube 1851, Friedrich Jakob Karl Lange 1852).
  Surname pool tight & local (Hafer, Grimme, Löhner, Apel, Decker, Ullrich, Niedermann, Albrecht, Leube, Lambach, Günther,
  Diedrich, Bischof, Maaß, Uttermöhlen). Marzhausen now ELIMINATED on BOTH baptism (1835) and confirmation tracks. Detail
  in germany/marzhausen-research-log.html.

- 218674 + 218707 (**Bad Karlshafen Konfirmationen, BOTH confessions; swept COMPLETE 24 June 2026**): Bad Karlshafen
  was a Huguenot/Reformed foundation with TWO congregations — Lutheran *Konfirmationen 1831-1928* (reg. **218674**,
  1107 imgs) and Reformed *Konfirmationen 1831-1919* (reg. **218707**, 1138 imgs). Both previously "Baptisms only"
  (Jan-Feb 1835 Taufen read on 218677 Luth. + 218713 Ref.); the confirmation tracks are now ALSO swept = NEGATIVE.
  • **LUTHERAN 218674**: conf. section title card = **Bild 977**; ~1 written Seite per class-half, two Seiten per opening;
  each class = Knaben then Töchter + "Im Jahr 18XX sind confirmirt: N Knaben und M Töchter" tally. Anchors: 1844/45 =
  Bild 990 (S21/22); window classes — **1847 Bild 992-993 (S25-27), 1848 Bild 993-994 (S28-29), 1849 Bild 994-995
  (S30-31, PRIME), 1850 Bild 995 (S32, PRIME), 1851 Bild 996, 1852 Bild 997, 1853 Bild 997-998, 1854 Bild 998-999,
  1855 Bild 999 (S40)**. Prime 1849 leaf Bild 994 = **p/61b7bc6da8**. Carls all on local burgher surnames, none Konze:
  Steckhein+Lagg (1847 b.1832), Müller (1848 b.1834), **Carl Schwabe b.10 Mar 1835** (father Heinrich Schwabe Schmied)
  + **Carl Schäfer b.14 Jul 1835** (1849 prime), Georg Carl Jellitt (1850), Carl Schölle+Carl Maaß (1851 middle-names),
  Carl Schwabe (1852), Carl Schmidt (1854), Carl Conrad + Carl Niedmann (1855).
  • **REFORMED 218707**: conf. section title card = **Bild 946**; LARGE classes (continuous Nro, ~2 imgs/year, Knaben then
  Töchter + "Summa aller im Jahr 18XX … confirmirten = N" tally). Anchors: 1835/36 = Bild 958 (S20/21), 1838/39 = Bild 964
  (S32/33); window — **1847 Bild 979-980, 1848 Bild 981-983, 1849 Bild 984-986 (PRIME, births 1834-35), 1850 Bild 987-988,
  1851 Bild 988-991, 1852 Bild 991-992, 1853 Bild 993-994, 1854 Bild 995-997, 1855 Bild 998**. Prime 1849 leaf Bild 984 =
  **p/01cad7ff94**. Forename Carl is VERY common (Huguenot congregation) but NEVER on a Konze-type surname: 1849 prime
  boys = Ahrend, Barre, Bödicker, **Carl Friedrich Wilhelm Costabel b.14 Dec 1834**, Jeppe, Eisenträger, **Ferdinand Carl
  Wilhelm Engelhard b.1835**, Tiege, Grothe, Carl Schlingloff, **Johann Heinrich Schlosshahn b.22 Feb 1835** (= the
  legitimized-Thielemann boy, confirms his prior elimination). Later Carls: Ahrend(1850), Görmann/Hartung/Issartel(1851),
  Lössel/Rüdiger/Zielberg(1851), Görmann/Methe/Claus(1853), Meier(1854), Blume(1855) — all non-Konze.
  • VIEWER QUIRKS (both): page-number input is stale-canvas + the canvas AUTO-PANS so the Seite/Jahr header sits above the
  viewport top — fastest reliable read is **zoom out to fit-page then ZOOM the region [280,230,1320,720]** to capture the whole
  two-page spread at once; anchor years off the legible **Geburtsjahr column** (1833,1834,1835…) not arithmetic. Permalink
  minting: chain icon ~(1122,140) → "Erstellen"; FIRST click triggers DE→EN re-render → click "Create" again → p/<hash>.
  Both confessions now ELIMINATED on baptism AND confirmation tracks; detail in germany/karlshafen-research-log.html.

## Downloaded sources log
- **13 Jun 2026 — Rabus baptism (FS KZFV-DRQ).** Johann Wolfgang Martin Rabus, bapt. **12 July 1778**,
  **Nürnberg-St. Sebald**, Taufen 1770-1800 (Archion churchRegister 205541, sig. 9.5.0001-601-014),
  **image 184 / page 357**, the d.12 entry. Father **Johann Adam Rabus** (Bierwirth), mother
  **Margaretha Dorothea** (née Rupprecht), godfather Johann Wolfgang Martin Jäger (Gold-/Silberdraht-
  Fabrikant). This is the ORIGINAL behind the FS "certified Abschrift 1957" and pushes the Rabus line
  back a generation from Georg Christoph Rabus (KHB2-5J5). Full-res page-spread PDF (pp.356-357) was
  downloaded via the in-viewer Download button → lands in the browser Downloads folder; needs to be
  moved into the project folder manually. Source note:
  `Archion_Nuernberg_StSebald_Rabus_KZFV-DRQ_Baptism_June13_2026.md`.
