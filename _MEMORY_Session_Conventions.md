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
- 219049 (Gottsbüren **Taufen** 1830-1867; 1078 imgs; **calibrated + window-swept 26 Jun 2026, Session-this**):
  WELL-ORDERED, chronological, ONE written Seite per image at **Seite = Bild − 793** (verified: Bild814=S21 1832 Sept;
  Bild818=S25 1833 Jan; Bild842=S49 Dec1834/Jan1835; Bild843=S50 Jan1835; Bild844=S51 Feb1835; Bild850=S57 1835 Jun).
  Taufen section title card = **Bild 791**; entries open ~Bild794 (1830). Nro CONTINUOUS (not reset yearly); ~3-5
  entries/Seite, ≈45-55 baptisms/yr (parish covers filial hamlets — long Aschener/Gerland/Dettmar clans). Image↔year
  drifts (NOT a clean 13 leaves/yr) — always read the written "Jahr 18XX / Monat" header, don't extrapolate.
  VIEWER QUIRKS: inline viewer maxes at a low-res 812px thumbnail — **must use "Vollbild"/full-screen** for hi-res
  tiles. Zoom +/- buttons JUMP between fit and one high level (no smooth steps) and are erratic after a page-number
  jump (stale-canvas + lands at max zoom, panned to gutter); **the reliable rhythm = navigate with the prev/next
  ARROWS (top ~58,34 / ~223,34), which preserve zoom AND redraw cleanly**, then read. At "+3 from fit" (slider ~472)
  one Seite's header-row + 4-5 entries fit; at fit, a screenshot-zoom of the child-name column [~640-1010 px] is just
  legible. ⚠️ fit-view CUTS the bottom 1-2 entries of dense leaves (causes small Nro gaps) — pan/scroll for the tail.
  ALPHABETICAL "mit Register" INDEX = **Bild 1053 (A) → 1076 (Z)** (preceded by an "X" divider card at Bild 1052).
  ⚠️ **RE-READ A–Z 26 Jun 2026 (Session 127): the index is BOUND OUT OF ORDER, with DUPLICATE + one BLANK leaf** —
  the letters do NOT advance cleanly per spread (e.g. Bild 1062 is a **D | K** spread; G repeats at 1067; S repeats at
  1074; blank ruled leaf at 1068). The old "K = Bild 1062R / index 1053-1062 / G=1057-59" note was only coincidentally
  right for K. Read each leaf via the viewer's AI **"Erkannter Text"** panel (transcribes these index leaves well),
  scan for kon[sz]/kont/gans/gons/gann/conso/con[tz]e/jung, verify hits vs image. Letter→Bild map (verified live):
  A=1053-54, B=1055-56, D=1057, E/F=1058, **G=1059 + 1060L (dup 1067)**, H=1060R-1061, **K=1062R + 1063**, M=1064,
  N=1065-66, R=1069-70, S=1071-72+1074(dup), U/V=1073, W=1075, Z=1076. **NO own page for C, I, J, L, O, P, Q, T, X, Y.**
  ⭐ RESULT (Charles search): **NO Konze/Kontze/Konsen/Konzen** (K = Köster, Kurth, King, Köhler, Kaufmann, Kirschknecht,
  Kämpfe, Kümmel, Kümpel, König, Kunst, Kraft, Kluthe, Kindbe, Bury); **NO Gansen/Gonsen/Gonson/Gannsen/Gans/Ganß**
  (G = Gerland-native, Götze, Grabe, Gante, Gödchen, Gemmern, Garte, Grek, Gödecke); **NO Jungkonze** (there is NO I/J
  leaf at all — alphabet runs H→K→M); C-variants (Conson) would file under K (B→D jump, no C page) — cleared. Only
  regex false-positive = "Blankenberg, *Kons.*" (B, an abbreviation, NOT a surname). ⇒ no Konze-pool surname in
  Gottsbüren baptisms 1830-1867 (corroborates the parish's other Kontze-free books). **Index permalinks (reg.219049):
  A-start Bild1053 p/bd8ea39bc5; G Bild1059 p/7c7f01d0ca; G/H Bild1060 p/e60d78dc37; K Bild1062 p/00940fbb92; K-cont
  Bild1063 p/04f2eea26d.** Detail: Session127 log + germany/gottsbueren-research-log.html.
  Chronological reads (Charles b. 26 Jan 1835): **1833 Jan-~Aug (S25-36) read leaf-by-leaf = NEG** (Carls all local:
  Carl Friedr. Wilh. Gerland Nro129; Carl Friedr. August Gerland Nro134; illeg. Carl Heinrich Wiechard Nro139).
  **Jan 1835 (S49-50, Nro196-201) FULLY read = NEG** — the only Jan-1835 males are Heinrich Ludwig Baumann (b.21) &
  Johann Ludwig Wiegand (both solid local families); NO male b.26 Jan, NO Carl, NO Konze. **1835 Feb-Dec scanned**
  (S51-64): only Carl-child = **illeg. "Johann Carl," b. 15 Feb 1835, bapt. 22 Feb, mother Gertrude Elisabeth Schröder**
  (S52 Nro205) — a NEAR-MISS (illegitimate Carl, early 1835) but wrong date (15 Feb≠26 Jan), Schröder = common local
  family, no Konze link ⇒ NOT Charles. 1834 (autumn) + Jan 1836 sampled = same local pattern, no rufname-Carl/Konze.
  Verdict: Gottsbüren ELIMINATED on the BAPTISM track too (it was already eliminated on conf./marriage/burial).
  Full entry-by-entry of 1836-1841 left as optional follow-up (index already rules out the Konze surname there).
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
- 244439 (Gudensberg TOWN Taufen 1830-1844, Kirchenkreis Fritzlar; 531 imgs; "komplett transkribiert"; **baptism
  name-INDEX swept 27 Jun 2026, Session 135**): closes the old "Gudensberg own Taufen not surname-scanned" caveat.
  Baptism body = ONE opening per Seite at **Seite = Bild − 248** (Bild 250 = Seite 2 / 1830 Aug; **Bild 267 = Seite 19 /
  1831 Aug-Sept**); register runs ~Seite 1-254 (1830-1844), Nro continuous (~4/Seite). ⚠️ Despite the "komplett
  transkribiert" tag, the **alphabetical name-index leaves are NOT served with usable AI/OCR text** (get_page_text +
  the txt overlay return nothing on the index) → index read BY EYE; stale-canvas after every page-number jump (force a
  redraw with a zoom +/−, OR step with the next/prev arrows). The **A-Z name-index sits at the END of the reel,
  Bild ~508-525**, columns Männlich|Seite|Weiblich|Seite, entries ordered BY SEITE within each letter (NOT
  sub-alphabetical), and common letters span TWO leaves. Letter→Bild map (verified live): **A|B = 508; B·C|D = 510**
  (p/85f21c743c); **D|E = 509; E = 511; F|G = 513** (p/f41ff41983, G first page); **G(cont) = 514; H|I·J = 515**
  (p/0cae314e05); **I|K = 516** (p/d78fbe9f62); **K|L = 517** (p/a9b6fa22cf). (Leaves 509/510 are bound slightly out
  of image order; no separate C page — B² overflow + C share one leaf.) ⭐ **RESULT = clean NEGATIVE for the ENTIRE
  Konze/Gans pool.** • **K (516R+517L):** König, Korf, Köhler, Köhe, Knoll, Knauß, Kißmann, Kißler, Knoch, Kell,
  Käufer, Krieg, Kolbe, Kußmann, Kümpel, Kümpfer, Kurz, Kaufhünger, Kirchmann, Koch, Klugfelder + one illeg. compound
  "Kor[n]zügel" line — NO Konze/Kontze/Konsen/Konzen. • **I·J (515R):** Jungermann, Jungkurt/Jungcurt, Jacob — NO
  Jungkonze/Jungkontze. • **G (513R+514):** Groß, Göppel, Gümbel, Göddel, Günther, Goestmann, Gerhard(t), Goebel,
  Güth, Gridel, Gleisner, Gippert — NO Gans/Ganß/Ganson. • **C (510L, combined B·C leaf):** a single B-overflow entry
  only ("Beier/Bäse…248") — NO Conson/Contze/Conze. ⚠️ **CORRECTION-IN-THE-ACT (rigor note):** the FIRST G entry,
  "…Carl…, Seite 19", read as "Ganß" at low zoom, was VERIFIED at the baptism page (**Bild 267 = Seite 19**,
  p/9ac4dd7943) to be **"Groß — Ferdinand Carl Hermann"**, male, bapt. **11 Sept 1831**, father the local Amts-Schäfer
  Groß × Caroline geb. Finckel/Vinckel, godfather Ferdinand Borchmann zu Oberkirchen → **Groß, NOT Ganß** = NOT a pool
  surname (lesson: Kurrent Ganß/Groß confusion — always verify a "G…ß" index hit at the entry). Only other G-Carl =
  "Karl Goebel" S239 (~1844). So **NO Gans whatsoever in Gudensberg town** (unlike Oedelsheim/Heisebeck/Bodenfelde).
  ⇒ Gudensberg TOWN now negative on the BAPTISM track too (was already neg on Konf. 244437 + filials Dissen 253403 /
  Grifte 253444); **stays ELIMINATED.** Detail: Session135 log + germany/gudensberg-research-log.html.
  **MARRIAGE + BURIAL indexes ALSO swept (28 Jun 2026, per Jed "scan the surnames") = NEGATIVE:**
  • **Trauungen 1830-1863 = reg 244449** (shared reel 2438 imgs; Trau-section title "Trau- und Register" = Bild 2243;
    alphabetical index at END of section, Bild ~2417-2424): **C empty (2417L); G = 2420-2421L** (Graewer, Gummerwald,
    Geiser, Gröde, Groß, Gleisner, Glaser, Gippert, Gümbel, Griesel, Güth, Gold, Goebel, Grunewald, Gerhard; **p/ca1b922804**);
    **I·J = 2422R** (Jungermann, Jacob, Fehler, Fulberger); **K = 2424** (Krug, Kurz, Krause, Kubnert, Kolbe, Kieser,
    Küchmann, Kalb, Keim, Kaiser, Klöffler, Kneppor, Kauffunger, Kruse, Kroll, Kranz, Korb, Knorbe; **p/39dcd061fc**) →
    NO Konze/Kontze/Jungkonze/Gans/Ganß/Conson.
  • **Beerdigungen 1830-1851 = reg 244444** (shared reel 1121 imgs; burial-section title "Tod- und Register" = Bild 836;
    entries Seite = Bild − 839 [Seite1=840, Seite248/1851=1087], end ~1091 + "blank pages NOT filmed" card 1095 + X-divider
    1096; ⚠️ **the alphabetical index is filmed at the very END of the reel AFTER the X-card, Bild ~1097-1106**, NOT at the
    section front/back): **C ~1100 (only a B-straggler "Beier 251"); G = 1103-1104** (Gleisner, Grantler, Gippert, Girt,
    Grunewald, Groß, Gawer, Germeroth, Goebel, Gründer, Runte; **p/cee74ad45c**); **I·J = 1105R + empty "I" 1106L**
    (Jungermann, Jacob, Jungkurt, Imberger); **K = 1106R** (Knoll, Krieg, Kußmann, Krug, Kolbe, Kaufunger, Kaiser,
    Knödding, Kroll, Kranz, Korf, Kurz; **p/62a07114c5**) → NO Konze/Kontze/Jungkonze/Gans/Ganß/Conson.
  NB the **"Jungkurt/Jungcurt"** surname (Jung+Kurt, a real local family — NOT Jungkonze) recurs in all THREE Gudensberg
  indexes; do not mistake it for the Jungkonze pool surname. ⇒ ALL THREE Gudensberg vital registers (Taufen 244439,
  Trauungen 244449, Beerdigungen 244444) now swept = NO Konze/Gans pool surname anywhere; Gudensberg comprehensively
  ELIMINATED. (Trauungen reach to 1863 and burials to 1851, so the pool's absence is established well beyond the 1833-41
  birth window.)
- 168326 (Fulda Stadt ev. Taufen 1830-1863, Kirchenkreis Fulda; 1091 imgs; **baptism INDEX swept 27 Jun 2026,
  Session 130**): section title card = Bild 785; baptism body ~Bild 789-1069. **⚠️ The body reel is DUPLICATED/
  DISORDERED — Bild does NOT map linearly to Seite.** Live anchors: Bild 851=Seite63 (Dec1837); 852=Seite64
  (1838, Gastmann Nro298, p/bf75a813e2); 888=Seite66 (Apr1838); 925=Seite137 (1849); 1060=Seite272 (1863).
  (851→888 = +37 img for only +3 Seiten, but 888→925 = +37 img for +71 Seiten ⇒ heavy duplication.) **Read the
  printed "Seite N / Jahr 18XX" header, never extrapolate from Bild.** This reel HAS the AI "Erkannter Text"
  panel for most index leaves — **refresh it after a page jump by CLOSING (✕) and REOPENING (doc icon) the panel,
  then `get_page_text` returns the current leaf** (otherwise it shows the previous leaf). ALPHABETICAL baptism
  index: main A-Z **Bild 1071(A)→1082(W,Z)**, then "Fortsetzung"/overflow **1083-1088**, then end-of-reel TEST
  CARDS 1089-1091 (alphabet + mm-scale — NOT a 2nd index). Letter→Bild (main run): A=1071, B/C=1072, D/E=1073,
  F/G=1074, H/J=1075, K/L=1076, M/N=1077, O–V=1078-1081, W/Z=1082. Overflow: K-cont & S-cont=1083, H/W/B/S=1084,
  G/R/S/L=1085 (dup 1086), S=1088. **RESULT (Charles surname-pool sweep, 1833-41 window): NEGATIVE** — every pool
  letter read in BOTH main run + continuation: **C** (Claus, Clemann, Conradi, Clausius, Christiani, Chors,
  Cornelius — no Conson); **G** (Göppel, Göbel, Groß, Gilbert, Gieseler, Gerlach, Gasche, Gilsa, Günther, Gümpel,
  Giebel, Grünewald, Goller, Gutheil, Goßmann, Gud, Giet, Gies, Gauslandt, Gartlandt, Grau, Götze, Gutberlet — no
  Gansen/Gonsen/Gonson/Gannsen/Gans; Gastmann is here, already excluded); **I/J** (Juffland, Just, Jahn, Jüngling,
  Jahr, Immel, Jacobi, Jungermann, Jahre — no Jansen/Jungkonze); **K** (Klages, Kehl, Kietzell, Klostermann,
  Kersten, Kuhn, Kraus, Koch, Köhler, Kayser, Knoll, Kunst, Kraut, Kapp, Knoch, Klüppel, Katzung, Kersting,
  Kornemann, Kraft, Kurz, Kunze — no Konze/Kontze/Konsen/Konzen). Two near-tokens cleared: OCR stray "Komse 63"
  → Seite 63 = Dec1837, no such surname (artifact, military families Giebel/Lange); "Kunze, Wilhelmine… Seite 100"
  = female, ≈1843-44 (out of window). ⇒ NO Konze-pool baptism anywhere in Fulda EV 1830-1863. **Fulda EV stays
  ELIMINATED** on the baptism track (corroborates Session 127's Gastmann verdict + garrison sweep). Detail:
  Session130 log + germany/fulda-research-log.html.

- 219154 (Haueda Taufen 1830-1928, Kirchenkreis Hofgeismar; 495 imgs; **baptism window calibrated + permalink minted
  28 June 2026**): the Haueda Taufbuch section opens late in the reel — **section title card = Bild 258**, inner "Tauf
  Buch" title = Bild 259, entries open Bild 260. WELL-ORDERED, one written Seite per image at **Seite = Bild − 260**
  (verified live: Bild 264 = Seite 4 / 1831 Jan-März; Bild 272 = Seite 12 / 1834 Jan-Juni; Bild 273 = S13 / 1834
  Juni-Okt; Bild 274 = S14 / 1834 Okt-Dez; **Bild 275 = Seite 15 / 1835 Januar Februar und März**). Filial book =
  small parish, ~2-3 images/year. VIEWER QUIRKS: stale-canvas after a page-number jump (shows previous leaf until a
  zoom +/− forces a redraw) — navigate single steps with the prev/next ARROWS (top ~58/216,140), which redraw cleanly
  and preserve zoom; read the printed "Gemeinde Haueda · Jahr 18XX · Monat …" header, don't extrapolate from Bild.
  ⭐ **Jan–Feb 1835 baptism window = ONE leaf, Bild 275 (Seite 15)**, which carries all of Jan/Feb/März 1835. Read by
  eye = NEGATIVE: 1835 baptisms all legitimate on local surnames (Pille, Cramme, Pelte, Götte); no Konze/*n·s·n
  surname, no boy b.26 Jan 1835. **Permalink minted: Bild 275 = https://www.archion.de/p/0c535638ad/** (verified to
  resolve to pageId 19416172 / Bild 275). Minting flow on this viewer = chain icon (toolbar ~1123,140) → panel
  "Permalink erstellen" → click "Erstellen"; the FIRST click is swallowed by a DE→EN panel re-render (button becomes
  "Create"), so click again → wait ~3s → the p/<hash> URL renders with a "Permalink kopieren" button. (Leave the
  "Zoomstufe & Bildbereich einschließen" box UNCHECKED for a clean page-level permalink.) Haueda stays ELIMINATED on
  both tracks (baptism reg.219154 + confirmation reg.219151). Detail: germany/haueda-research-log.html.
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
  "Create"/"Erstellen"; FIRST click triggers DE→EN re-render so click again → p/<hash>. (Minting gotcha, verified
  28 Jun 2026: a Create click in the SAME browser_batch right after a page-jump gets swallowed by the panel
  re-render — navigate in one call, then click Create in a SEPARATE call; and a 2nd Create click RESETS the
  panel to the form, so click Create exactly ONCE per leaf.) ⭐ **PER-YEAR CONFIRMATION PERMALINKS minted live +
  each verified to resolve (28 Jun 2026):** 1847=Bild1981 p/a36d2f7fa0; 1848=Bild1982 p/9c413c25d3;
  **1849=Bild1983 p/0927f9755b (PRIME)**; **1850=Bild1984 p/5f2809a6dc (PRIME; older p/b4d6bfe1ba also valid)**;
  1851=Bild1985 p/2190a077fd; 1852=Bild1987 p/5216ede6f9; 1853=Bild1988 p/5dc83c310e; 1854=Bild1989 p/e513052fe9;
  1855=Bild1990 p/7e468e0689. RESULT (1847-1855
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

- 219214 (Helmarshausen Taufen 1830-1856 "mit Register", Kirchenkreis Hofgeismar; 598 imgs; **baptism index re-read
  26 June 2026, Session 124**): reel bundles other books — baptism title page = **Bild 312**; baptisms run ~Bild 313-410
  and are **LINEAR/chronological**, ~1 written Seite per image, ~13 imgs/yr. Year anchors: **1833 ≈ Bild 337** (Mai/Juni,
  Seite 25, Nro 111-116); **Jan 1835 ≈ Bild 356** (year header "1834-35", 1835 opens Nro 201 at Bild 356/Seite 42; late
  Jan 1835 = Bild 357/Seite 43). ⚠️ STALE-CANVAS after a page-number jump (shows the previous leaf until a zoom +/− forces
  a redraw — same fix as 219532); the prev/next **arrows keep zoom & redraw cleanly**, so single-step with arrows. The
  **alphabetical name-index sits at the END, Bild ~579-585**, two pages per opening, one letter per page (580 = G left / H
  right; 581 = I/J; 582 = H-tail left / **K** right; 583 = K-tail left / L right); within each letter, Männlich then
  Weiblich sub-columns with Seite numbers; **no separate C page** (alphabet jumps B→D, so C-variants would file under K).
  The on-screen `zoom`-region tool DRIFTS on this viewer (DPR mismatch) — to read tiny index text, instead DRAG the target
  column to center + click the in-viewer "+" 2-3× + take a normal screenshot. RESULT (re-read of the April index-only
  elimination, now at higher resolution + the newly-in-pool Gans/Ganson surname): **NEGATIVE on all of K, I/J and G** — no
  Konze/Kontze (K = Kraft, Köhler, Kayster, Kassmann, Kaß, Knipsfeld, Kolbe, Kothe, Klages, Kuhlmann, Klöckner, Kühnemann,
  Kayser, Kiethe, Kelle, Kuhle), no Jungkonze (I/J = Jungandreas, Jürgens, Jungmann), no Gans/Ganson (G = Gehre, Golf,
  Gronau, **Gauer**, Gofmannrecht, Gerland, Giller, Geyer, Gille; the only near-shape "Gauer, Friedrich Carl" sits at Seite
  19 ≈ 1832, pre-window, non-pool). The 1835 birth window read page-level (Bild 356-357): Gräßel/Dilling/Dietz/Heitz/Goda,
  **no Konze and no male Carl across the claimed 26 Jan 1835 date**. Permalinks: **K-index Bild 582 = p/61e1f2999b**; **Jan
  1835 leaf Bild 357 = p/c2e212421e**. The Helmarshausen OSB Konze (fam. 67/96/302/406) + Jungkontz (297/507/468) families
  therefore fall OUTSIDE this Taufen book (pre-1830 or in marriage/burial registers). Helmarshausen stays ELIMINATED on
  baptism (index + 1835 leaf), confirmation (219208), and OSB tracks. Detail in germany/helmarshausen-research-log.html +
  Session124 log.

- 219106 / 220213 / 219586 (**Grebenstein / Veckerhagen / Immenhausen baptism INDEXES swept full-window 27 Jun 2026,
  Session 133**): all three are "mit Register" Taufbücher whose **alphabetical name-index sits at the END of the Taufen
  section** (one or two letters per spread; for a given letter the dense column is on the page bearing its header, with a
  sparse "tail" on the next leaf). Calibrations: **Grebenstein 219106** (Taufen **1830-1839**, 1183 imgs; title card Bild 900):
  index Bild ~1160-1170 — **C** Bild 1161L (BLANK), **G** Bild 1164R, **I/J** Bild 1166R, **K** Bild 1167R+1168L; I|K leaf
  permalink **p/db1cc999b5** (verified). **Veckerhagen 220213** (Taufen **1830-1851**, 1068 imgs; title card Bild 777):
  index Bild ~1044-1051 — **C** Bild 1044R, **G** Bild 1048R, **I/J** Bild 1050R (one entry), **K** Bild 1051R; permalink
  **p/2ae59285f6**. **Immenhausen 219586** (Taufen **1830-1845**, 909 imgs; title card Bild 629): compact index Bild ~884-896 —
  **C** Bild 884R, **G** Bild 888R(+889L), **I/J** Bild 890R(+891L), **K** Bild 891R+892L; permalink **p/b762726f0f**.
  RESULT = **NEGATIVE in all three** for the entire Konze pool (Konze/Kontze/Konsen/Konzen · Conson/Contze · Gans/Gansen/
  Gonson/Gannsen · Jansen/Jungkonze). Surname pools are tight local Hofgeismar families: Grebenstein K=Knollführer/Klinger/
  Köster/Krum/Krieger/Kampfing/Knull/Korn/König/Kraus/Konrad, G=Groß/Gude/Gellner/Gerland/Gerlach; Veckerhagen K=König/Koß/
  Köhler/Köster/Knollführer, G=Graf/Gerlach/Günther/Gunkel, C=Cellmann/Söhre; Immenhausen K=Kobe/Köster/Kroll/Kraft/Kaufholz/
  Knierim/Krollshof/Koch/Krohne/Knauf/Kempf/Kayser/Kohl/Kurth, G=Gemmecke/Glänzer/Gläser/Gerlach/Goedecke/Geske, C="Carl"
  family only (the surname behind Immenhausen's 1849 confirmand "Friedrich Carl"), I/J=Iserloh/Jacob/Jäger/Junker. These
  upgrade the three from 1835-window-only to FULL-INDEX coverage; all stay ELIMINATED. ⚠️ Same viewer quirks as 219214:
  the on-screen `zoom`-region tool **drifts up-and-right** (DPR mismatch — shift the requested region DOWN, or use the
  in-viewer "+" then a plain screenshot); the page-number input is stale-canvas-prone and occasionally MIS-navigates in
  full-screen — the **thumbnail-strip click is the most reliable jump**, prev/next arrows redraw cleanly. Detail in
  Session133 log + the three germany/<parish>-research-log.html files.

- 220042 (Sielen Taufen 1830-1876, Kirchenkreis Hofgeismar; reel of 2112 imgs; **swept 1833-1841 on 26 Jun 2026,
  Session 125**): WELL-ORDERED, **one written Seite per image ⇒ image = Seite + 1828**. Title page = Bild 1826;
  column-header template = Bild 1828; 1830 begins Bild 1829 = Seite 1. Window map: 1833 = S9-12 (Bild 1837-1840);
  **1835 birth-core = Seite 16 = Bild 1844**; 1841 ends Seite 52 = Bild 1880 (year tally "Geboren im Jahr 1841: 21").
  Stale-canvas after a page-number jump (force a redraw with a zoom +/-); sequential next-arrow reads are clean.
  ⭐ **This reel exposes the viewer's AI "Erkannter Text" panel** (document icon in the toolbar) — lists each child as
  "Knabe/Mädchen, <name>" (switches to "Männlich/Weiblich" from Seite 52 / 1842). Fast workflow: read the panel per
  leaf, scan child names for Carl/Karl + the full panel text for Konze-type surnames, verify hits against the image.
  Extract the panel cleanly with JS (find the div containing /KI-basiert|AI-generated/ + /Jahr 18|Year 18/, smallest
  such node, slice after "einzublenden."/"transcription."). Permalink minting: chain icon (fullscreen toolbar ~1060,35)
  → "Erstellen"; FIRST click triggers a DE→EN re-render (button becomes "Create"), click again → p/<hash>.
  RESULT (1833-1841, **NEGATIVE for Charles**): the 1835 birth-core leaf (Seite 16, p/700c4c0c76) has ONE boy only =
  an **unnamed stillborn "Knabe —", b. 18 Jan 1835, Hausnr 101** (rest girls + Friedrich Wilhelm Blum); NO boy b. 26
  Jan 1835. **NO Konze/Kontze/Gansen/*n·s·n surname ANYWHERE** in 1833-1841 (child, parent, or godparent). FOUR
  Carl/Karl children, all non-matching: Karl Wilhelm Hofeditz b.2 Nov 1838 (S35/Bild1863, p/85edffbfa4); **Carl Ludwig
  Bößler b.19 Mar 1839, father Friedr. Wilhelm Bößler Leineweber (S38/Bild1866, p/f7d0dfe887) — = the 1853 confirmand
  from Session 112, cross-confirmed; the baptism AI mis-read the surname as "Köhler", image confirms Bößler**; Karl
  Wilhelm illegit. b.26 Oct 1839 (mother Wassermeier/father Baumann, S41/Bild1869 Nro188); Karl Ludwig Thöne bapt.9
  Aug 1840 (S46/Bild1874 Nro206). Sielen now negative on BOTH baptism (220042) and confirmation (220039) tracks plus
  early-KB burials (220033) → stays ELIMINATED. Detail: Session125 log + germany/sielen-research-log.html.
  **BAPTISM NAME-INDEX checked (26 Jun 2026):** 220042 is "mit Register" — alphabetical baptism name-index at END of reel,
  Bild ~2094-2100, two letters per opening, each page split Männlich/Seite/Weiblich/Seite, entries ordered BY Seite (so the
  1833-41 window = Seite 1-52 sits at the head of each letter). K spans TWO pages (early Bild2097-right covers the window
  Seiten 6,12,13,18…; later Bild2098-left runs S162-267). Read K/I·J/G for the Konze pool = NEGATIVE: **G index page is BLANK**
  (only G surname in the whole register = "Grunemann" S248 ~1875, on a late-overflow leaf) → no Gans/Ganß/Ganson; **I·J = Jordan
  & Jaeger only** (lone Carl = Carl Wilhelm Jordan S128 ~1857) → no Jungkonze; **K = Köster/Köste, Koch, Krause, Koßmann, Krome,
  Krone, Klein, Klöre** → no Konze/Kontze/Konsen. No separate C page (alphabet …G,H,I·J,K,L… → C-variants file under K, clear).
  Index independently corroborates the leaf sweep. Permalinks: G/H Bild2094 = p/8a6f4f25e0; I·J/H Bild2096 = p/0f16cc9960;
  K-early+overflow Bild2097 = p/8d9230dfde; K-late/L Bild2098 = p/e2c3dd800b. (Index hand read by eye — Konze-pool absence
  unambiguous.)

- 219265 + 219364 (**HOFGEISMAR TOWN baptisms — Altstädter + Neustädter; swept COMPLETE 27 June 2026, Session 126**):
  ⚠️ Naming caution — the older "219253/219256/219295/219382" numbers are the Altstadt KB/Trauungen + Neustadt Trauungen
  (marriage) books, NOT baptisms. The TOWN TAUFEN registers are: **Altstädter Taufen 1830-1843 = 219265**; **Neustädter
  Taufen 1830-1863 = 219364**. BOTH carry "Bem.: mit Register" → alphabetical baptism name-index at the END of the reel,
  spanning the whole register (so the K/G/I·J/C letter-sections settle 1833-1841 in one pass).
  • **219265 (Altstädter, reel 1000 imgs):** title page Bild 714; baptisms start Bild 717 = Seite 2 (Aug 1830);
    **Seite = Bild − 715** (Bild 820 = S105 = Oct 1835). Index at end: C=Bild977, G=981, H/I·J=983, **K=984**, M=986,
    N/O=988, Q/R=991, U/V=995. Jan 1835 birth-core = Seite 85-86 = Bild 800-801 (Nro 288-297). RESULT NEGATIVE: K-pool
    Köhler/Krome/Kratzenberg/Koth/Knüppel/Koppen/Kleinschmidt/Kuenne/Kühn/Klaus/Kroll/Kersting/König/Knauf/Kurre/Kraft/
    Kayser — no Konze; G-pool Gueth/Grau/Guempel/Grebe/Gante/Goldbeck/Gülke/Giese/Groese/George — no Gansen; C-pool
    Claus/Collmann/Carriere/Clobes/Croll — no Conson; local "Janson" family in I·J but J-boys at Seiten 21,33,46 then a
    GAP to 110 (no J-boy 1833-35). Jan 1835 leaf: no boy b.26 Jan (Koehler b.1Jan, Richter b.8Jan, Deichmann b.~5Jan,
    + girls Erdmann/Witzel/von Reinhardt).
  • **219364 (Neustädter, reel 1160 imgs):** title page Bild 874; **Seite = Bild − 878** (Bild 920 = S42 = Aug 1838;
    Bild 927 = S49 = Juni/Juli 1839; ~5-9 Seiten/yr, grows over time). Index at end: B=Bild1138(L), C/D=1138(R)/1139,
    F=1141, G=1142, H/I·J=1143, **K/L=1145**, P/Q=1150. RESULT NEGATIVE: K-pool Köhler/Kloppmann/Kahler/Kessling/Koch/
    Kohlhepp/Knabel/Kümpel/Kreszweber/Knoche/Kohlstaedt/Krome/Kreis/Kratzenberg/Kraft/Kleinschmidt/Krampe — no Konze;
    G-pool Grasse/Gnecht/Goldbeck/Gemmecke/Grappe/Grau/Gundlach/Gümpel — no Gansen; C folded into K (B→D, no separate C
    page) = clean; I·J = Israel/Janson/Jung/Jordan/Jäger/Jeppe/Ilse — "Janson Johannes" S49 (~1839) + "Janson Carl
    Friedrich" S203 (~1860), NO Carl-Janson b.~1835.
  BOTTOM LINE: Hofgeismar TOWN now ELIMINATED on the baptism track too (was already out on marriage + confirmation).
  No Konze/Kontze/Gansen/Gonsen/Conson in either town parish; the "Janson" burgher family is a distinct local line, not
  Charles. Index-leaf permalinks: Altst C p/0b3c5d4e22, G p/577f7942e0, I·J p/7753503cce, K p/9aa7751abd; Neust G
  p/5288df68a4, I·J p/cce1846251, K·L p/a703fdefff. Detail: Session126 log + germany/hofgeismar-research-log.html.

- **Four-parish baptism-INDEX checks (26 June 2026, Session 125)** — read the K / I-J / G index
  sections of each Taufen register for Konze/Kontze/Jungkonze/Gans/Ganson, 1833-1841 window. Register
  numbers (corrected): **Heisebeck Taufen = 219175** (219172 is the Konfirmationen); **Liebenau Taufen =
  219745** (219742 = Konf.); **Lamerden Taufen = 219676**; **Eberschütz Taufen = 218887**. Each has a
  built-in alphabetical Register at the END of the Taufen section (two letters per opening). RESULT =
  NO Konze/Kontze/Jungkonze in any; G pages empty at Liebenau (Bild 1702)/Lamerden (Bild 448)/Eberschütz
  (Bild 596). I/J = Jungheim (Liebenau Bild 1703), Jacobi/Jaspe/Jericke (Heisebeck Bild 1506),
  Jaeger/Jorden (Eberschütz Bild 597) — no Jungkonze. K sections = local K-names only (Heisebeck:
  Koch/Klinge/Küster/Klemme/Kassau, Bild 1507-08; Liebenau: Köster/Kümpel/Kniep/Plate, Bild 1706;
  Lamerden: Plate/Klage/Klö/Krote/Rückert, Bild 451-52; Eberschütz: Kraft/Küster/Klappe/Roß/Reichel,
  Bild 599) — no Konze. Liebenau/Lamerden indexes have hard Kurrent hands (K reads best-effort by eye;
  certify via Peter Schräder if ever needed). All four stay ELIMINATED on Konze/Kontze/Jungkonze.
  Detail in Session125 log + each parish research log.
- ⭐ **HEISEBECK GANS — corrected & upgraded (Session 127, 26 Jun 2026).** The Session-125 claim that
  Heisebeck Gans is "only from ~1866, out of window" was WRONG — it read only the LATE tail of the G
  index (Bild 1505, Seiten 145-253). The G section spans **Bild 1503-1505; the early Gans entries are
  on Bild 1504.** Calibration: **Seite ≈ Bild − 1237; Bild 1283 = Seite 46 = Jahr 1839** (verified).
  The **OSB Heisebeck-Arenborn** (klauskunze.com/heikun/hei/heisebeck_register.htm) lists **"Gans" ×~33
  family numbers** = major native multi-century Heisebeck surname. **Gans baptisms IN the 1833-1841
  window:** Christine Wilhelmine Gans (f, S.41 ~1838); **Eduard Gottlieb Gans (m, S.46, bapt. 16 Jun
  1839; father Heinrich Wilhelm Gans, Schneider × Dorothea; p/efb5066fa2)**; Johann Friedrich Gans
  (m, S.56 ~1840-41). TWO+ Gans households: Heinrich Wilhelm Gans (Schneider)×Dorothea, and Tagelöhner
  **Ernst Wilhelm Ganß** (his line = illeg. Wilhelm S.165/1866, Adolf S.196). For CHARLES: still no Gans
  son b.~26 Jan 1835 (first Gans = S.41 ~1838; Seite 19=1835 has no Gans) — not a direct match, but
  Heisebeck is now a STRONG Gans-pool locus (Diemel/Weser corridor; Gans≈Gannsen). Follow-ups: OSB
  family-page mining, Heisebeck Trauungen ~1836-38 (Gans marriages → fathers/origin), pre-1830 Heisebeck
  Taufen volume. Detail: Session127 log + germany/heisebeck-research-log.html.

- **Baptism-index checks: Lippoldsberg / Oedelsheim / Vernawahlshausen (Session 126, 26 Jun 2026).** Three
  Weser-valley parishes whose BAPTISMS were unsearched (confirmations done earlier). OSB Konze-pool surnames:
  Lippoldsberg=Kontze/Jungkontze/Gans/Ganß/Ganson; Oedelsheim=Kontze/Kontzen/Konzen/Jungkonz/Gans/Ganß;
  Vernawahlshausen=Gans only.
  • **219778 Lippoldsberg Taufen 1830-1870 — NEGATIVE (clean, via index).** Baptism **Seite = image − 1411**
    (Bild 1510 = S99 = 1846); window 1833-41 ≈ Seite 20-72. Alphabetical index A–Z ≈ Bild 1665-1695; **K=Bild
    1680-81, G=1678, H=1679** (legible + AI-transcribed). K section = NO Kontze/Konze/Jungkontze (only Käse,
    Kahle, Krapf, Koch, Knuth, Knipping, Kettler, Kramer, Kuhlmann, Kühne, Kraft, Kluges). **G section: a Gans
    family IS indexed but earliest Seite 99 = 1846 — ALL Gans baptisms postdate the window**; the two Carl/Karl
    Gans boys are Seite 152 (~1854) & 162 (~1856). Only in-window Carl of note = Klages Karl Friedrich Wilhelm
    S55 (~1838, non-Konze). Lippoldsberg baptisms ELIMINATED for 1833-41.
  • **219946 Oedelsheim Taufen 1830-1877 — PARTIAL / NOT cleared (OPEN).** Title Bild 646; baptism pages legible
    & AI-transcribed BUT reel is **SHUFFLED** (year ≠ image order; e.g. Bild 705="1831" sits after 693≈1836/37)
    and OCR noisy. Index at end (~911-933): **K(ontze) leaf = Bild 918 is FADED — AI returns 0 K entries** (ink
    loss + bleed-through), so Kontze can't be confirmed/excluded from the index; G=Bild 915 (Gronemann, Gassmann
    — no "Gans" seen), H=916 transcribes. Sampled baptism leaves 664-678 & 693 (incl. **Charles's exact Jan-Feb
    1835 window**) = NO baptized Kontze/Konze/Gans child; Carls all local (Heinrich Carl Schraeder b.Oct1834;
    Friedrich Carl WESSEL Hausnr21 b.~25 Feb 1835 [rufname Friedrich]; Carl Dettmar a father). **⚠️ BUT the Gans
    surname is present locally as GODPARENTS in the 1830s ("Carl August Gans", "Andreas Gans"), children's fathers
    = Lindner/Schnadhorst/Süg/Koch.** So Oedelsheim is NOT a clean negative — FLAGGED FOLLOW-UP: shuffle-aware
    full-window leaf sweep + Kurrent read of the faded K-index leaf Bild 918 (or Kunze's printed Oedelsheim OSB).
  • **220261 Vernawahlshausen Taufen 1830-1869 — clean NEGATIVE (index fully read, Session 127).** **Seite =
    image − 1296** (title Bild 1296); roughly LINEAR/not shuffled. Reel is **"mit Register"**: legible
    alphabetical index at reel END (~Bild 1560-1567), two letters/opening, AND the index leaves DO AI-transcribe
    via `get_page_text` (the S126 "faint & out of order 1564=M/1568=L" was a STALE-CANVAS mis-read). Letter map:
    1560 B|C, 1561 C|D, 1563 E|F, **1564 F|G**, **1567 K**. **G (Gans) = Bild 1564 = p/a36232f645** → Gebrunner/
    Goerder/Giebert only, **NO Gans/Ganß/Ganson**; **K (Konze) = Bild 1567 = p/24fd3271ea** → Kummel/Klinge/
    Küchemann/Koch only, **NO Konze/Kontze**; C empty (no Conson). OSB-attested "Gans" does NOT appear in the
    Vernawahlshausen baptism index 1830-1869 at all. (Earlier S126 8-leaf window sweep Bild 1328-1351 also neg.)
  • **220258 Vernawahlshausen Konfirmationen 1831-1948 — NEGATIVE (newly searched, Session 127).** Parish page
    `…/vernawahlshausen/220258`. Reel 1318 imgs; section title **Bild 1127**, classes from 1128; NOT
    AI-transcribed (read by eye); well-ordered chronological, ≈1.6 img/class; each class "Confirmierte Jahr 18XX",
    **A.Söhne then B.Töchter** + year-end "Summa". Window map: 1847=1152-53, 1848=1154-56, **1849=Bild 1157 (PRIME,
    p/e4a98e1045), 1850=Bild 1158 (PRIME)**, 1851=1159, 1853=1161, 1855/56=1163; reel ends blank (~1309+), no
    end-index. **1849 prime class = ONLY 2 boys: Pfütz b.20 Nov 1834 + Funke b.26 MÄRZ 1835 — neither a Carl,
    neither Gans/Konze, 1835 boy born 26 Mar not 26 Jan.** 1850's only Carl = **Carl Wilhelm Wißmann b.1835
    (Wißmann Ackermann clan)** — wrong surname/date. No Gans/Konze confirmand 1847-1856; Carl recurs only on local
    surnames (Gnann, Grobold, Nolte, Hosenhaus) or as fathers. Vernawahlshausen ELIMINATED on BOTH tracks.
  RESULT: no Charles (Carl b.26 Jan 1835 on a Konze/Gans surname) in any of the three. Lippoldsberg clean negative;
  **Vernawahlshausen now clean NEGATIVE on baptism index + confirmations (Session 127)**; **Oedelsheim stays OPEN**
  (Gans present as godparents + faded K-index). Detail: Session126 + Session127 logs. NB Archion index leaves are
  inconsistently AI-transcribed — but 220261's index DID transcribe cleanly; faint leaves (Oedelsheim K) don't.

- **⭐ OEDELSHEIM UPDATE (Session 127, 26 Jun 2026) — ACTIVE GANS FAMILY FOUND; now a PRIORITY LEAD.** Did the full
  leaf-by-leaf 1834-1836 sweep of 219946. The reel is shuffled, so anchor on each leaf's written "Jahr" header; the
  **main chronological 1834-36 run = Bild 673-693** (670=1832, 671-72=1833, 673-77=1834, 678-86=1835, 687-93=1836,
  694=1837), read complete (displaced leaves seen were OLDER: Bild 689=1830, cf S126 705=1831 — not 1834-36). This
  **overturns the "pool left before the 1840s" idea:** a real Gans baptism exists — **Andreas August Gans, b. 25 Feb
  1835, bapt. 15 Mar 1835, Oedelsheim Hausnr 2** (Bild 679/Seite 28, **p/075cc0099a**, image-verified). Father
  **Georg Friedrich Gans, Drechslermeister** (turner) × Johanne Marie Elisabeth geb. Kohlschein; godfather **Carl
  August Gans**, son of the **Gastwirth (innkeeper) Andreas Gans**. ≥3 Gans men in town in the 1830s (Georg Friedrich
  the turner; Andreas the innkeeper; Carl August the innkeeper's grown son ~b.1810-18; + a George Andreas Gans
  Stellmacher as godparent); "Gans" recurs as godparents through 1834-36. **STILL no Carl Gans:** no boy rufname
  Carl/Karl on a Gans surname, no Gans child b.26 Jan 1835 (Jan 1835 read in full; closest = George Heinrich Westerman
  b.24 Jan 1835, non-Gans). So Charles ≠ the 1835 Oedelsheim Gans baptism on record — BUT a living Gans family in the
  right place/decade makes Oedelsheim the **top Gans→Gannsen lead**. NEXT: reconstruct BOTH Gans households across ALL
  years in 219946 (hunt a Carl Gans + emigration ~1850s); Oedelsheim marriages/burials; Kunze's printed OSB; re-try the
  faded K-index (Bild 918). Detail: Session127 log + germany/oedelsheim-research-log.html (status now ⭐ PRIORITY LEAD).

- **⭐⭐ OEDELSHEIM GANS = MULTI-HOUSEHOLD POPULATION (Session 128, 26 Jun 2026).** Extending the Gans baptism sweep
  (219946) to 1837-1839 shows the Gans family is SEVERAL households (weight comparable to the Hümme Kontze cluster):
  **(A) Georg Friedrich Gans, Drechslermeister (turner), Hausnr 2 × Johanne Marie Elisabeth Kohlschein** → Andreas
  August (b.25 Feb 1835, p/075cc0099a) + Sophie Rosine Charlotte (b.~Jun 1837, Bild 696); **(C) Friedrich Wilhelm Gans,
  Tagelöhner, Hausnr 11 × Anna Christine Herwig** → Friedrich Wilhelm Gans (b.~Jan 1839, Bild 707/Seite 56,
  image-verified); **(B) Andreas Gans, Gastwirth (innkeeper)** → son Carl August Gans (adult godparent b.~1810-18);
  + George Andreas Gans, Stellmacher (godparent). STILL no Carl Gans child (Gans sons = Andreas August, Friedrich
  Wilhelm; only "Carl Gans" is the ~1810s innkeeper's son, ~20 yrs too old) → Charles NOT a documented 1835 Oedelsheim
  Gans baptism, but this is the project's strongest Gans→Gannsen lead (a Gans son emigrating ~1850s, not an 1835
  baptism). 219946 SHUFFLE map: main 1830-38 run = Bild 670-699, displaced 1831 leaves 700-705, resumes 1838/39 at 706;
  index G/K leaves too faded to read → reconstruct by leaf-sweep on the "Jahr" header. FOLLOW-UP: finish Gans sweep
  1830-33 + 1840-77 (all 3 households, every son); Oedelsheim Trauungen (Gans marriages) + Beerdigungen 219952 (deaths/
  emigration gap); Carl August Gans bapt in KB 1810-1830 reg.219940; Bremen/Hamburg passenger lists ~1850-59. Full doc:
  Oedelsheim_Gans_Family_Reconstruction_June26_2026.md.
  • **More baptisms found (S128 cont.):** Sophie Rosine Charlotte Gans (b.~Jun 1837, Hausnr 2, Household A); Reinhard/
    Theodor Gans (b.~1839, Bild 709/entry 269, Hausnr 14). Gans sons = Andreas August, Friedrich Wilhelm, Reinhard —
    STILL no Carl child.
  • **⭐ BURIAL SIGNAL = EMIGRATION (Oedelsheim Beerdigungen 1830-1899, reg 219952):** the burial index IS legible
    (title "Todten- und Register"; G-section = Bild 2456, R = 2465, L = 2459). The G-section is DOMINATED by Gronemann;
    **Gans deaths are strikingly SPARSE — essentially "Gans, Martin" Seite 116 only.** A large 1830s-40s Gans baptism
    population leaving almost no Gans deaths across 69 years = the **emigration signature** (the young Gans sons survived
    & left). Strongly consistent with a Gans son → "Gannsen" emigrating ~1850s = Charles. NEXT: pull the "Gans Martin"
    S116 burial; list which Gans children have NO death record; find Gans marriages (Oedelsheim has NO standalone
    Trauungen reg — marriages are in the combined KB vols, e.g. Kirchenbuch 1840-1852 = reg 352562, + a pre-1840 vol);
    Bremen/Hamburg passenger lists. NB the 219952 burial INDEX is mostly legible (unlike the faded Taufen 219946 index).

- **⭐⭐⭐ BREAKTHROUGH (Session 128, 26 Jun 2026) — a GANS FAMILY EMIGRATED OEDELSHEIM → NORTH AMERICA in 1834.**
  Source: **LAGIS "Hessische Auswanderer"** DB (lagis.hessen.de/de/personen/hessische-auswanderer — searchable by
  name/place; free open web; client-rendered so use the BROWSER not web_fetch). Record: **"Gans, Georg Friedrich,
  Oedelsheim, 1834"** (ID 110864, permalink lagis.hessen.de/resolve/de/ha/110864): Ziel **Nordamerika**, **4
  Auswandernde** (family of four), Vermögen 110, **HStAM Best. 16 Nr. 3216 S. 199** (Marburg; Innenministerium
  emigration/Untertanenentlassung files). Part of a **Weser-valley Gans emigration cluster** (all Lkr. Kassel):
  Oedelsheim 1834, Heisebeck 1840 & 1846 ("Frau des Henrich Wilhelm Gans"), Gieselwerder 1846 (Christine Charlotte
  Gans; Georg Wilhelm Gans; "Frau des Henrich Ferdinand Gans"). **KEY:** the Oedelsheim TURNER Georg Friedrich Gans
  STAYED (baptised kids 1835-37), so the 1834 emigrant is a SEPARATE/namesake Gans household that LEFT. **WORKING
  HYPOTHESIS (strong, unproven):** Charles Gannsen (b.26 Jan 1835, surname→Gannsen, NO German baptism ever found) was a
  child of this emigrant Gans family, **born 1835 AFTER they left Germany** → explains the missing baptism (and fits
  the read evidence: ALL Jan-1835 Oedelsheim baptisms searched = no Carl Gans). NEXT: (1) order/scan **HStAM Best.16
  Nr.3216 S.199** — names the 4 + ages + exact date; (2) US side — a Georg Friedrich Gans/"Gannsen" family arriving
  ~1834-35 → Missouri, Charles as their next/American-born son; (3) reconcile Charles's US-stated birthplace (if
  "Germany", test a 1835 departure with 1834 permit date); (4) check Heisebeck/Gieselwerder Gans emigrant records.
  Full detail: Oedelsheim_Gans_Family_Reconstruction_June26_2026.md.
  • **US-SIDE CORROBORATION + SHARPENED HYPOTHESIS (S128, via Jed's Ancestry login).** A SECOND independent index
    confirms it: Ancestry **"U.S. and Canada, Passenger & Immigration Lists Index"** (coll. 7486, rec. 129797) =
    **Georg Friedrich Gans, arrival 1834 America, "Wife & 3 children"**, annotation "All from counties of the province
    Nether-Hesse, NE part of former Hesse-Cassel" (= the Oedelsheim/Weser zone). Source = **Kurt Günther, "Hessian
    Emigrants to America," Germanic Genealogist no.15 (1978) p.375** (1833-34). So the emigrant G.F. Gans (wife + 3
    children, left 1834) is a SEPARATE household from the Oedelsheim TURNER G.F. Gans (who stayed, kids from 1835).
    **SHARPENED HYPOTHESIS: Charles (Carl) was likely one of the emigrant family's 3 CHILDREN — born in Kurhessen
    ~1832-34, emigrated as a toddler 1834** (fits family belief "born in Kurhessen", death-cert "born 1834",
    Gans→Gannsen; the "26 Jan 1835" is one post-mortem family estimate, maybe a yr off). DECISIVE NEXT: (1) find the
    emigrant family's 3 children's BAPTISMS in Oedelsheim/Niederhessen ~1826-34 — a G.F. Gans father whose wife is NOT
    Kohlschein, hunt a son Carl (KB 1810-1830 reg 219940 + 1830-34 part of 219946; + nearby filial parishes if
    "Oedelsheim"=Amt); (2) get Günther's article (Germanic Genealogist no.15, 1978, pp.374-377) — may NAME the wife+3
    children; (3) US 1840/1850 census for this Gans family (Ohio? cf. "George W. Ganse, b.Hesse-Cassel, naturalised 1852
    Cleveland OH"; or Missouri) → find Charles among the children. NB the project's MAIN thesis was Konze (Trendelburg/
    Deisel); this literal-Gans-from-Oedelsheim thread is a strong COMPETING origin hypothesis. Detail: reconstruction doc.
  • **⚠️ CORRECTION (27 Jun 2026) — the "emigration" is most likely an UNUSED PERMIT; hypothesis WEAKENED.** Checked
    KB 1810-1830 (reg 219940): the LAGIS/Günther entries are PERMIT records (Entlassung aus dem Untertanenverband =
    release-from-subject-status APPLICATIONS, not verified US arrivals). The ONLY Georg Friedrich Gans documented in
    Oedelsheim = the TURNER × Kohlschein, and he STAYED: son Georg Friedrich Wilhelm Gans bapt. 28 Mar 1821 (Bild 536,
    †Oedelsheim 12 Feb 1845) + Andreas August (1835) + Sophie (1837). A man baptising kids in Oedelsheim 1835/1837 did
    NOT emigrate 1834 → the 1834 "emigration (wife+3 children)" was almost certainly his UNUSED permit. So there was
    probably NO actual 1834 Gans emigration, and the US-arrival lead is a spurious permit (1850 US census also found NO
    Gans family born Germany / no Charles Gans — consistent). NET: the "Gans family emigrated 1834 → Charles" story is
    substantially weakened / probably wrong. What survives: Oedelsheim has a real large Gans population (right place/era);
    only thin remaining route = a single Gans son named Carl emigrating ALONE — but no Carl Gans found 1834-41, and a
    staying family fits "no family found" poorly. LESSON: emigration-DB hits = PERMITS; always verify against parish
    records before believing. KB 1810-1830 (219940): combined vol, Taufen S.1-104 (~Bild 482-555) each section w/ its own
    family-name index after it; confirmations ~Bild 560; **NO AI "Erkannter Text" panel on this register — read by image.**
    TODO if pursued: read the Taufen family-name index for the COMPLETE Gans-children list (is there a 2nd G.F. Gans? a
    Carl Gans son?); the turner's pre-1834 children aren't fully listed. Status downgraded from "TOP LEAD" to OPEN/WEAK.
  • **INDEX-READ ATTEMPT (27 Jun 2026) — BLOCKED by legibility.** Tried to read the KB 1810-1830 (219940) Taufen
    family-name index for the complete Gans list. Found it (G/K/L columns ≈ Bild 542-545; baptism entries + index
    columns are INTERLEAVED/jumbled), but it's **faint iron-gall ink with NO AI panel + stale-canvas + confusable
    Kurrent G/K** → could NOT get a clean, reliable read of all "Gans" entries. The "Carl August" entries I could read
    are on NON-Gans surnames (a K-surname Seite 10; a B-surname) — no Gans+Carl confirmed, but not cleanly ruled out
    either. NB Bild 536 = the turner's son Georg Friedrich Wilhelm Gans bapt. 1821 (reinforces turner stayed). To
    DEFINITIVELY close/revive the lead, the full Gans-children list needs: a Kurrent specialist (Peter Schräder) reading
    of the KB 1810-1830 Taufen index/entries, OR Kunze's PRINTED Oedelsheim OSB (lists the Gans families w/ dates), OR a
    full-res download of the index leaf (Bild ~545) for offline enhancement. Automated viewer read = not feasible here.

## Klaus Kunze (HeiKun-Verlag) OSB online registers — Konze/Gans surname pool (Session 127, 27 Jun 2026)
Klaus Kunze (klauskunze.com/heikun) publishes Ortssippenbücher for many Weser/Diemel parishes, and puts the
**Namen-/Orts-/Sachregister ONLINE** (free, instantly searchable; family entries with DATES are book-only). Several
are project candidate parishes. **Swept the online registers for the pool** — surname→family-number index:
- **Helmarshausen** `hel/register.htm` (OSB 1521-1950, 4500 fam, €60, ISBN 978-3-933334-21-3): Konze 67,96,302,406;
  Contzen 450; Jungkontz 297,507; Jungkonze 468; Gans 67,199,302,453; Ganß 186,556. ⭐ **fam 67 & 302 are indexed under
  BOTH Konze AND Gans.**
- **Oedelsheim** `os/oedelsheim_register.htm`: Contze, Contzen, Kontze, Kontzen, Konzen, Jungkonz, Gans, Ganß (name-list,
  no nos.) — confirms the OPEN Oedelsheim Gans/Kontze pool is real & dense (reinforces the ⭐ PRIORITY LEAD + "get Kunze's
  printed Oedelsheim OSB" next-step).
- **Lippoldsberg** `os/lippoldsberg_register.htm`: Contze 53,119,261,384; Kontze 262; Jungkontze 226; huge Gans (~50)+
  Ganß (~30); **Ganson 186** (the literal Ganson spelling!).
- **Karlshafen** `kf/namenregister.htm` (OSB 1699-1945): Konze 37,61,68,285,287,342; Kontze 287; Conze 99; Consens 181;
  Jungkonze 308; Gans (8 fam). fam 287 = Konze AND Kontze.
- **Gieselwerder** `os_gi/register.htm`: Contze (11 fam) + Contzen (8) + Kontzen (6) + Conze 214; huge Gans+Ganß; several
  fams carry both Contze & Contzen.
- **Sielen** OSB *1714-1831* (Rolf Nowak data, ed. Kunze 2009): **FREE FULL-TEXT PDF** at
  `klauskunze.com/heikun/sielen/OSB Sielen.pdf` (NOT in FamilySearch catalogue). **FULLY MINED 27 Jun 2026** (PDF+txt
  archived: `sources/OSB_Sielen_1714-1831_Nowak-Kunze.pdf`, `notes/sielen_osb_1714-1831_fulltext.txt`). Stops 4 yrs
  before Charles b.1835. RESULT: **NO native Konze/Kontze household and NO Gans/Ganß/Ganson at all** in Sielen
  1714-1831 — the Konze name enters ONLY by in-marriage, from the project's two core Konze locales: **=973= Johann
  Heinrich Konze, Ackermann, *in Trendelburg** (daughter Maria Elisabeth Konze ∞ Lorentz Becker, Sielen, 5.3.1809,
  fam=133=) and **=974= Johann Christoph Konze, Richter (judge) zu Hümme** (∞ Anna Catharina Schüßler; daughter Anna
  Catharina Kontze *1748 †1800 Sielen) — the latter an early-1700s Hümme Konze, possible forebear of the 1830s Hümme
  Kontze cluster. Plus Wilhelmine Friederike Kontze ∞ Conrad Becker (fam=131=). Corroborates Sielen ELIMINATION; NEW
  LEADS = the Trendelburg Ackermann-Konze and the Hümme Richter-Konze lines.
  **CROSS-REF (27 Jun, folded into konze-trendelburg.html + konze-huemme.html):** =973= Trendelburg Konze **= the documented
  Johann Henrich Kontze, b.~1740 d.1804** (son of Arnold Philipp Kontze, Rathsverwandter); his daughter **Maria Elisabetha
  b.28 Apr 1779** is the 1809 Sielen bride — OSB supplies her previously-unknown marriage to Lorentz Becker. =974= **Joh.
  Christoph Konze, Richter zu Hümme** = a NEW earliest Hümme Konze (a generation+ above Joh. Christoph Kontze b.1763; name
  recurs → possible direct line). Sielen Becker bride **Wilhelmine Friederike Kontze (=131=) = the Hümme posthumous daughter**
  (b.~Sep 1834, of Johannes Kontze ×Uffelmann, m. Conrad Becker 1856) — confirms the Hümme→Sielen-Becker marriage. So the
  Nowak OSB ties into the project tree at THREE points (Trendelburg dau's fate + new Hümme progenitor + Hümme-Becker confirm).
  ⭐ **HÜMME EARLY BOOKS (newly catalogued 27 Jun — the project pages had ONLY listed 219526 KB 1765-1831):** Archion holds
  **Hümme KB 1640-1724 = 219520**, **KB 1720-1765 = 219523**, and an **alphabetical KB-Register 1720-1765 = 398631** (index),
  plus Beerd. 1830-74=219538, Trau. 1830-91=219547. Parish "komplett transkribiert" (AI text). ⇒ The OSB "Johann Christoph
  Konze, Richter zu Hümme" (daughter b.1748) + family fall INSIDE KB 1720-1765 and ARE verifiable. **NEXT: search index 398631 +
  KB 219523 (and 219520 for the prior generation) for Konze/Kontze — verify the Richter, find Anna Catharina's 1748 baptism,
  bridge down to Joh. Christoph Kontze b.1763 + the 1830s cluster.** (konze-huemme.html holdings line corrected.)
  ⭐⭐ **INDEX 398631 SEARCHED (27 Jun) — KEY RESULT:** the KB-Register 1720-1765 is a clean TYPED index (15 imgs); K-page =
  **Bild 5 = p/d461c3f04a**. It lists **"Jungkontze / Jungcuntze" on KB pp. 40, 56, 69, 145, 202, 205, 233, 289, 295, 310, 321**
  and **NO plain "Kontze/Konze" entry at all**. ⇒ In Hümme 1720-1765 the family is the COMPOUND **Jungkontze** form — so the OSB
  "Konze, Richter zu Hümme" = the Hümme **Jungkontze** line (Nowak simplified it). This (a) proves an early-18th-c HÜMME Jungkontze
  family — bears on the OPEN "Hümme-vs-Stammen" Jungkonze question (FS labels the line "Hümme"); (b) ties the new Richter into the
  konze-jungkonze branch. Folded into konze-huemme.html (Richter row) + konze-jungkonze.html (new Hümme-connection note).
  **NEXT (not yet done): read KB 1720-1765 (219523) at the Jungkontze pages** (need to calibrate 219523 image=Seite; handwritten
  Kurrent) to pin Anna Catharina's 1748 baptism + the Richter's name/household + sons, and test the bridge to Joh. Christoph
  Kontze b.1763 and the Trendelburg/Stammen Jungkonze.
  **KB 219523 OPENED (27 Jun) — structure + calibration for the handoff:** reel 802 imgs; "1720-1765" title page = **Bild 617**;
  it is a COMBINED book (Taufen + Konf + Trauungen + Todten, "ohne Register"). NOT AI-transcribed (text panel only offers
  "Texterkennung beauftragen" — the "komplett transkribiert" tag covers the 1830+ books, NOT this one). Anchors read live:
  **Bild 762 = baptisms year "A° 1726"**; burials section by **Bild 783-784** (entries give "alt X Jahr" death-ages) ⇒ the
  **1748 baptisms sit ~Bild 770-780**. Hand is difficult early-Kurrent + faded. ⚠️ Extracting Anna Catharina Jungkontze's exact
  1748 baptism + confirming father "Joh. Christoph (Jung)kontze" + sons (bridge to Joh. Christoph Kontze b.1763) is a **Kurrent-
  SPECIALIST read (→ Peter Schräder)** — do NOT trust a screenshot transcription for the tree. Hand him: index Seite refs
  (Jungkontze pp. 40,56,69,145,202,205,233,289,295,310,321 of 398631) + these Bild anchors. Index K-page permalink p/d461c3f04a.
⚠️ **RIGOR CAVEAT:** a family number under BOTH "Konze" and "Gans" in an index = EITHER a true spelling-variant family
(Konze gen./alias Gans) OR Konze-head married a née-Gans woman (intermarriage). The index can't tell them apart — the
**book's family entry** is needed to confirm the variant equivalence. Promising, NOT proof. Access full records via:
FamilySearch Library (Kunze's books are in the FHL catalog) · email heikun-verlag@klauskunze.com with family nos. · or buy.
Full table + next steps: `Session127_Kunze_OSB_Online_Registers_Konze-Gans_Crosslink_June27_2026.md`.

## Lippoldsberg's neighbours — Kunze registers + Bodenfelde re-verify (Session 130, 27 Jun 2026)
Jed: "for lippoldsberg do the neighbouring parishes and check klauskunze town registers as well."
Lippoldsberg already neg (Taufen 219778 + Konf 219775). Worked the **un-searched cross-Weser
(Hannover-province) neighbours** + mined Kunze OSB registers (both **JS-rendered** — render in
browser; `web_fetch` shows only a shell):
- **Bursfelde + Glashütte** (`os/bursfelderegister.htm`; Hann.-Münden/Hemeln, Lkr. Göttingen):
  **Gans = fams 110, 113, 125, 136** (+Ganz 136, Gaus 130); **NO Konze/Kontze/Contze.** ARCHION
  (Session 130): 1800s parish = **Fürstenhagen (Kirchenkreis Uslar)** — NOT a standalone
  "Bursfelde" book; place-search "Bursfelde" returns only KB 1639-1746 (under Fürstenhagen), but
  Fürstenhagen's later books carry an **"Ort" column and "Bursfelder Glashütte" appears there**.
  Registers: **KB 1832-1852 reg 359377** (Taufen tabulated + Ort col), **Namensregister 1793-1911
  reg 359381** (alpha index, forename-first/faint). **1835 Taufen read (reg 359377, Bild 11-13):
  Jan 1835 = Offensen children only (no Bursfelde child b.~26 Jan); the Bursfelder-Glashütte 1835
  baptisms (Nro 12-13, ~Apr) are NON-Gans (e.g. "Georg Ludwig", Wittler/Müller-type).** ⇒ no Carl
  Gans b.26 Jan 1835 in Bursfelde → the 4 Gans fams are historical OSB families, not an 1835
  cohort. STILL TO DO: Namensregister 359381 G-section (every Gans + years) / printed OSB for the
  Gans-family timing + emigration gap. NB this viewer's page-field concatenates digits — clear
  with triple-click; jumps misfire, so verify the on-image year header.
- **Wahmbeck** (Lkr. Northeim; own parish **Kirchenkreis Uslar**, 8 books, NO Namensregister, NO
  Kunze OSB, never flagged for the pool): ARCHION 1835 baptisms = **KB 1790-1845 reg 359497**
  (combined, sectioned by rite; tabular Geburts-Register with clean "Familien-Namen" column;
  ~2 img/yr in Taufen: 1833=Bild93, 1835=Bild94-95, 1836=Bild96; **bound out of order / Erst+
  Zweitschrift** — 94r=1836 while 95l=1835, so the Jan-Aug 1835 leaf Nro1-21 was NOT isolated).
  1835 Nro22-29 (Sept-Dec)+1834/1836 read = **EFFECTIVELY NEGATIVE: no Gans/Konze/Kontze**; whole
  local pool = Arnstmeier, Rammenstein, Niemeyer, Friese, Elend, Förtner, Morgenstern, Grote,
  König, Meister, Bremer, Brockhaus, Pape, Hesse, Grobe, Hauck, Krautmann, Schröder, Vömer.
  Only Carls = Carl H.W. Morgenstern (b.7 Dec 1835) + Carl …Brockhaus (b.25 Feb 1836), non-pool.
  **CONFIRMATION WINDOW + BAPTISM INDEX swept (28 Jun 2026, Session 136):** (1) **No baptism
  name-index exists** — reg 359497 opens straight into the chronological "Natorum Catalogus"
  (Bild 3); the marginal "Familien-Namen" column is the only finding aid (confirms the "NO
  Namensregister" note). (2) Confirmations: reg 359497's Confirmanden-Register is at the **end**
  and ENDS **1845** (Bild ~260-263; 1845 class read = local pool, no Konze/Gans), so the 1833-41
  birth window (conf ~1847-1855) is in **KB 1846-1852 = reg 359498** (89 img), whose confirmation
  section runs ~1846→~1864. ⚠️ reg 359498 confirmations are **SHUFFLED + DUPLICATED** (Bild 60=62,
  61=64), **no OCR** — identify leaves by entries, read in Vollbild + drag-pan to the confirmand
  column. Window classes read (~conf 1848-1851 in full, adjacent spot-read): boys/girls all
  **local Solling pool** — Brackhahn, Henne, Koenig, Husshebeck, Korps, Lücke, Otte, Engelhard,
  Eckhardt, Rammenstein, Wienecke, Burgendahl, Garbe, Marktler, Fricke, Drewmann, Bähre,
  Strackmann, Willich, Neuhaus, Pogge (+1845 class: Niemeier, Marlow, Arnstmann, Schrade,
  Mecklenburg, Sprenger, Schmidt, Roße, Claus). **NO Konze/Kontze/Gans confirmand anywhere.**
  ⇒ Wahmbeck NEGATIVE for Charles on BOTH tracks; stays ELIMINATED. Residual (minor): full
  per-year de-dup of the shuffled 359498 reel (births 1839-41 spot-read only) = Kurrent second
  eye. Detail: `Session136_Wahmbeck_Confirmation_Window_BaptismIndex_June28_2026.md`.
- **Bodenfelde** (`bf/register-osb-bodenfelde.htm`; Lkr. Northeim, Kirchenkreis Uslar): the OSB
  **IS published/online** (the `bodenfelde.htm` "in Arbeit nicht vor 2012" page is stale).
  **Gans = 15 fams: 13,95,118,141,155,170,171,196,197,229,256,453,456,480,538** (+Gansberg 170,
  Ganske 171, Gante 171/196) AND **Contze = fam 178** (only real Konze-pool surname; all other
  Kon/Con hits are occupations — Konditor/Konrektor/Konteradmiral/Kontoristin etc.). ⇒ **densest
  Gans pop. of the ring + one Contze** — UPGRADES/CORRECTS the older "Gans/Ganß only, Konze=false"
  note. Fam 178 (Contze) and the Gans fams share no number (not an obvious Gans=Contze variant link).
- **Bodenfelde on Archion** (Kirchenkreis Uslar; Taufen reg **359334**, Kartei Männer **359346**,
  Namensregister 1815-1836 **359342**, + Familienbuch 1797-1899, Konf 1848-1875, Taufen-Konf
  1837-1852): **1835 Taufen RE-VERIFIED NEGATIVE** (corroborates `bodenfelde-research-log`). My 1835
  read sits at **img ~320-324** (header "1835") — **~14 imgs earlier than the log's "334-340"** ⇒
  the combined vol almost certainly has an **Erst- AND Zweitschrift** of the 1830s Taufen (1835
  appears twice; both read the same — reconcile the image map). **Jan 1835 in full:** 8 Jan (Witte,
  Wasmuth, "Carl August Ferd. Gehringer") → 22 Jan (Husemann, f, Nr5) → 8 Feb (Brauns, f, Nr6) —
  **no 26-Jan birth, no Gans/Contze/Konze**; "Carl" pervasive but all local (Gehringer, Streitwolf,
  Biermeier, Spieß). **Kartei Männer 359346 G-section** = F(Fräter/Fleißner/Fröhlich)→**Gante/
  Gautier** (img184)→Geiler/Geers/Gerke — **no dense Gans card** at the F→G boundary (sparse/faint;
  not certifiable). Namensregister 359342 = thumb-indexed, **filmed out of order** (img21=E after
  img19=F), G/Contze leaf not cleanly isolated — follow-up.
- ⇒ Bodenfelde mirrors **Oedelsheim**: a real Weser Gans population whose **1835 cohort yields no
  Carl Gans** → keeps the corridor "Gans→Gannsen emigrated ~1850s, not an 1835 baptism" reading.
- **STILL TO DO (full sweep, one-at-a-time per Jed):** Wahmbeck DONE (effectively neg, above);
  finish **Bursfelde** Gans-timing (Fürstenhagen Namensregister 359381 G-section / printed OSB);
  optional: locate Wahmbeck's displaced Jan-Aug 1835 leaf to fully close the 26-Jan check;
  Bodenfelde Familienbuch/Kartei Gans + Contze-178 generations + Konf books. Niedersachsen
  emigration DB (not LAGIS-Hessen) for any Weser Gans leaving ~1850s. Detail:
  `Session130_Lippoldsberg_Neighbors_Bodenfelde_Bursfelde_June27_2026.md`.
- **⭐ ELIMINATION CRITERION WIDENED to the 1833-1841 birth window (27 Jun 2026, per Jed):** the
  neighbour test is now "ANY Carl/Karl on a pool surname (Gans/Konze/Kontze/Contze) born 1833-41",
  not just b.26 Jan 1835. **GRIND EXECUTED (27 Jun, per Jed "grind through it"):**
  • **Wahmbeck = VERIFIED NEG** (no pool surname in the parish at all).
  • **Bursfelde (Fürstenhagen reg 359377) = VERIFIED NEG for the FULL window.** Scanned 1833-41
    Taufen (clean tabular reg; Ort+Eltern+Pathen+Familien-Namen cols): Bild 5-10 sequential
    (1833-35) + 14/20/24/27 sampled (1836-41) + 30=1842 boundary. **Gans appears NOWHERE** (no
    parent, no godparent, no Bursfelder-Glashütte entry). Bursfelde/Glashütte baptising families =
    fixed non-Gans set (Grünewald, Pflug, Thön, Hesse, Engelke, Köhler, Wittler, Bödecker, Grote,
    Otte…); every Carl is local (Georg Carl Christoph Hoff; Heinrich Carl Thön Bursfeld 1833; Georg
    Friedr. Carl Otte 1842). ⇒ the 4 Kunze Gans fams produced no baptism 1833-41 → no Carl Gans.
  • **Bodenfelde (reg 359334) = 1835 VERIFIED NEG; off-years BLOCKED by the book.** Taufen vol is
    **Erstschrift+Zweitschrift** (divider "Neues Bodenfelder Kirchenbuch Anno 1794" at Bild 316),
    Kurrent year-headers ambiguous (1795 vs 1835 unreadable), entries dense prose w/ faint margin
    names → reliable year-nav + surname-scan of the off-years NOT achievable in the viewer. Solid:
    1835 read ×2 = no Gans/Contze; men's index 359346 G = Gante/Gautier, no Gans card. RESIDUAL =
    dated 1833-41 baptisms of the 15 Gans fams + Contze 178 → **Kunze's printed OSB Bodenfelde**
    (book-only) or a Kurrent specialist on 359334 / indexes 359342 + Taufen-Konf-1837-52.
  Net: **no documented Carl on a pool surname b.1833-41 found anywhere in the neighbour ring**
  (Wahmbeck+Bursfelde firm; Bodenfelde firm for 1835 + named OSB-family residual) → consistent
  with Charles having no recoverable German baptism (born-after-emigration).

## Gieselwerder / Kelze / Gewissenruh baptism-index + window sweep (Session 134, 27 Jun 2026)
Jed: "sweep the full baptism index window for gieselwerder, hofgeismar kelze and gewissenruh."
All three were previously baptism-searched ONLY at the Jan–Feb 1835 leaf; this swept the full
1833–1841 window (index where it exists, else leaf-by-leaf). Live Archion, Jed logged in.
- ⭐⭐ **GIESELWERDER REOPENED — reg 219016 Taufen 1830–1881 is "mit Register" and the index is
  NOT clean of the Konze pool.** Title card Bild 1244; **Seite = Bild − 1246** (Bild1263=S17=1834;
  1280=S34=1835; 1282=S36=1837; 1373=S127=1854; year-rate non-linear, read each Seite's year).
  ⭐ **BAPTISM-ANCHOR PERMALINKS minted live + each verified to resolve (28 Jun 2026):**
  Bild1263 (S17/1834, Kuntze×Warnecke stillborn — the lead) = p/9e4fae9479; Bild1280 (S34/1835 window)
  = p/73de5a3e1f; Bild1282 (S36/1837, Joh. Georg Wilhelm Kuntze×Reitz) = p/82fe471d11; K-index Bild1514
  = p/ca95e3d098 (re-verified resolves to K-index leaf).
  Index at reel end: C(primary,**empty**)=Bild1507R; C/B-overflow=1508L; E|F=1510; F|G=1511;
  G|H=1512; H|I·J=1513; **I·J|K=1514** (K-index permalink p/ca95e3d098 — ⚠️ stale canvas at mint,
  trust Bild 1514). FINDINGS: **C** empty (NO Contze/Conze — the living family spells with K);
  **G** = large Gans pop. (males S25,62,68,82,86,95) but **NO male Carl Gans**; **I·J** = 2 entries,
  **NO Jungkonze**; **K** = ⭐ **Kontze ×2 male — todtgeboren S17 (1834) + Johann Georg Wilhelm S36
  (1837)** + Kontze fem. Wilhelmine Friederike S256(late); a large **Kunze** clan (male S67–252,
  fem S7–245) whose ONLY Carl = **Kunze Carl Heinr. Albert S127 = 1854 (out of window)**.
  ⭐ **LEAD (image-verified): Heinrich Ernst Kuntze** ×(1) **Sophie Dorothea geb. Warnecke** →
  stillborn male März 1834 (S17/Bild1263); ×(2?) **Sophie Elisabeth geb. Reitz** → **Johann Georg
  Wilhelm Kuntze, b./bapt. Feb 1837** (S36/Bild1282) — apparent remarriage ⇒ child-GAP ~early 1835.
  No Kontze baptism between S17 and S36, i.e. no recorded 1835 Kuntze child → fits Charles (b.26 Jan
  1835, no German baptism) IF a son was born ~1835 and not baptised here. **No direct Carl-on-pool
  b.1833-41, so no proven match, BUT upgrade Gieselwerder from "eliminated" → ACTIVE Konze-pool
  locus.** Follow-ups: reconstruct the Heinrich Ernst Kuntze household (confirm Warnecke→Reitz, hunt
  a son b.~1835) + the Kunze clan; Gieselwerder marriages/burials; Kunze printed OSB (os_gi); 1846
  LAGIS Gieselwerder Gans emigrant cluster vs the G-index Gans households.
- **KELZE — reg 219634 combined KB; baptism window NEGATIVE; stays ELIMINATED.** Title card Bild
  364: "*(1830-1970) S.2-166 … Register jeweils nach den Amtshandlungen." Taufen **Seite = Bild −
  367** (Bild369=S2=1830; 375=S9=1833; 381=S15=1835; 390=S23=1837; 395=S28=1839; 401=S34=1841/42).
  ⚠️ **Taufen alphabetical index NOT online** — image numbering jumps **488→(gap 489–532)→533
  X-divider** (last Taufen leaf 488≈1909 then section card); index lost in the gap → did full-window
  leaf read. Window 1833–1841 (Bild 374–401) = uniformly **French-Huguenot-colony** pool (Bonnet/
  Benoit, Morell, Monard, Morin, Croll, Briede, Homburg, Weidemann, Saeger, Schöning, Müller,
  Stalknecht, Ehle, Rudolph, Fischer, Don, Martin, Paschal, Waldeck) — **NO Konze/Kontze/Gans**.
  Window Carls all non-pool: **Carl Wilhelm Homburg b.Dez 1835** (= the confirmation-sweep window
  Carl), Carl Croll (~Dez1835/Jan1836), Carl Heinrich Weidemann (illegit. Jan 1836), + fathers Carl
  Morell. Corroborates the existing confirmation+1835 elimination.
- **GEWISSENRUH — reg 219001 combined KB; full window read NEGATIVE; stays ELIMINATED.** Title card
  Bild 1844: "*(1830-1920) S.3-96 … Register jeweils nach den Amtshandlungen." Taufen **Seite = Bild
  − 1845** (Bild1848=S3=1830/31; 1850=S5=1832/33; 1852=S7=1835/36; 1857=S12=1840/41; 1858=S13=
  1841/42; 1937=S92=1914). ⚠️ **Taufen index NOT online** (same gap pattern: last Taufen leaf
  Bild1937=S92=1914; X-divider 1942; gap 1943–1955; Konf section 1956+/title 1957). Tiny Huguenot
  colony (1840=4, 1841=6 baptisms). Window 1833–1841 (Seiten 5–13, Bild 1850–1858, EVERY entry
  Nro~12–48) leaf-by-leaf = pool Heriot/Heritier, Jouquenal, Welle, Seguin, Frebel, Fischer, Martin,
  Götze, Lotz, Spieß, Vogt, Geist, Thöl, Och, Reumhof — **NO Konze/Kontze/Gans**, **NO Jan-1835
  birth**. Window Carls all non-pool: Carl Spieß (1833), Johann Carl Jouquenal (b.1 Aug 1834),
  Carl Och (~Dez 1835), Carl Philipp Frebel (b.6 Feb 1840). Corroborates the existing elimination.
- Detail: `Session134_Gieselwerder_Kelze_Gewissenruh_Baptism_Index_Window_Sweep_June27_2026.md` +
  the three parish research logs.

## Fulda / Gastmann garrison-parish sweep (Session 129, 27 Jun 2026)
Followed up the Fulda "Dassen" near-miss (Karl Friedrich **Gastmann**, b.26 Feb 1838 Fulda,
father Michael, Feldwebel 2.Inf-Rgt 1.Comp). Lead stays ELIMINATED as Charles; completeness pass.
- **Archion has NO name/full-text search** (place search only; advanced filter = record TYPE).
  Pre-1866 Kurhessen indexes are bound out-of-order + duplicated + X-card-separated → no shortcut;
  a literal exhaustive civilian-parish read across the 5 garrison towns is impractical.
- **Garrison soldiers' families = dedicated military congregations.** Only **Kassel
  (Garnisongemeinde)** covers the pre-1866 window (Taufen 1833-42/1843-51/1852-65 regs
  174005/174008/—; Trauungen 1833-65 reg 174029; Beerdigungen 1833-65). Marburg (Garnisonsgemeinde
  1896 / Soldaten 1939) and Bad Hersfeld (Militärgemeinde 1866) are all too late; Ziegenhain &
  Hanau have NO separate garrison congregation.
- **RESULT:** **Kassel Garn. Trauungen 1833-65 = NO Gastmann marriage** (complete A-Z thumb-tabbed
  index; G leaf Bild 568 blank; H leaf has a real "Hartmann Conrad", not our man). **Hanau
  Marienkirche (ref.) Taufen 1837-42 = NO Gastmann** (full G index Bild 1006-07).
  ⇒ Michael Gastmann did NOT marry/baptise-Karl at the Kassel garrison; the family tracked the
  company's station, not Kassel.
- **⭐ KASSEL GARN. BAPTISM INDEXES — ALL 3 SWEPT, G + K (Session 129 cont., per Jed "also look for
  Konze, Konzen"):** indexes shuffled+duplicated+X-card-separated. **Taufen 1833-42 (reg 174005):**
  G leaf=Bild 2060 (one non-match "Gi[ss]ert"); K leaf=Bild 2064-65 (Kuhl, Köhler, Knoche, Klobes,
  Kümmel, Korngiebel, Kaufmann, Köster…). **Taufen 1843-51 (reg 174008):** G=Bild 2251/2257
  (Glaese/Gerland/Greis/Geis…); K=Bild 2256 (Köster, Krämer, Kühl, Kerstan, Kraft, Köhler, König,
  Klein…); I/J=2255 (no Jungkonze); C=2249 (Cantz/Crell/Conrad, no Contze/Conze). **Taufen 1852-65
  (reg 174011, own film 234):** garrison winding down, sparse index — only B/H/W leaves populated,
  NO G or K leaf at all. **RESULT = NEGATIVE all three: no Gastmann/Gans (G) and NO Konze/Konzen/
  Kontze/Konsen (K) in the Kassel garrison baptisms 1833-1865.** (1833-42 is Charles's birth-year
  volume → clean for the Konze pool too.) H leaves carry genuine Hartmanns (not OCR-Gastmann).
- NEXT (low priority): localise the 1.Comp's station via Kurhessen military rolls (Hof-/Staats-
  Handbuch, Ranglisten, Stammrollen — ORKA Uni-Kassel, some OCR-searchable), then read only that
  town. Detail: `Session129_Fulda_Garrison_Parish_Sweep_June27_2026.md` +
  `germany/fulda-research-log.html`.

## Baptism-window sweep: Marzhausen · Bad Karlshafen (both) · Hombressen (Session 131, 27 Jun 2026)
Jed: "sweep the full baptism index window for marzhausen bad karlshafen, hombressen." Extended each
from the old "Jan–Feb 1835 only" read to the full **1833–1841** window. Detail:
`Session131_Marzhausen_Karlshafen_Hombressen_Baptism_Window_Sweep_June27_2026.md`.
- **181898 Marzhausen Taufen (Kr. Witzenhausen; reel 1786 imgs) — FULL 1833-41 ENTRY SWEEP = NEGATIVE.**
  Calibration: Taufbuch Band 1 title page = **Bild 1631; Seite = Bild − 1631** (S1/Nro1/Aug1830 = Bild1632).
  One Seite per opening; **Nro continuous** (Nro1 S1/1830 → Nro106 S15/1841). Entries fill Bild 1632-1786
  (to ~1910). NOT AI-transcribed; **no usable alphabetical Register leaf in the reel** despite "mit Register"
  → swept at entry level. Window = **Seiten 4-15 = Bild 1635-1646**, read leaf-by-leaf fully rendered
  (⚠️ stale-canvas clips dense leaves — use 3 s waits + read the written Jahr/Seite header each leaf).
  NO Konze/Kontze/Jungkonze/Gans/Ganß/Ganson. Tight local pool (Hahn, Kipp, Albrecht, Günther, Schmidt,
  Lambach, Apel, Becker, Grimm/Grün/Görtz, Grabbe, Dieterich, Uttermöhlen, Reineke, Schäfer, Kulp, Volland,
  Weideman, Mohr, Welcke, Thees, Hartung, von Drach, Löher…). Window rufname-Carls: **Carl Heinrich Wilhelm
  Grün** (1837, Heinrich Grün × geb. Görtz — local) + the **"+"-added Carl Heinrich August Wilhelm**
  (b. Jan, local Schäfer "Christoph Wilhelm" × geb. Albrecht, **†19 Oct 1842**) — neither pool, neither a
  26-Jan-1835 survivor; plus middle-name Carls (Günther 1834, Hahn 1834, Kulp 1838 illeg, Grabbe 1840).
  Permalink 1835 leaf Bild1638 = **p/827d1228f9**. Upgrades the "1835-only" elimination to the full window.
- **218677 Bad Karlshafen LUTHERAN Taufen (1830-1895; reel 799) — FULL NAME-INDEX swept = NEGATIVE.**
  Alphabetical "mit Register" index at reel END **Bild ~776-798** (X-divider card Bild 799); ~2 letters/opening,
  entries listed by Seite within each letter (window = low Seiten, present). **K** Bild782/784 = Köster/Kirchhain/
  Klingender/Klein/Kuhlmann/Kopp/Kümmel — no Konze; **G** Bild780 = Graff/Georges/Gebel/Grabe/Großmann/Gott/
  Gnatz(distinct, -tz)/Günther/Gerlach/Geyer/Gerland — no Gans; **I·J** Bild782 = Jacob/Jost/**Jansen**/Israel
  — no Jungkonze (local Jansen family, distinct); **C** Bild776-777 = **Crede** only (+misfiled Brandes) — no
  Conze/Consens. Permalink B/C leaf Bild776 = **p/c71ba16968**.
- **218713 Bad Karlshafen REFORMED Taufen (1830-1857; reel 653) — FULL NAME-INDEX swept = NEGATIVE.**
  Index at reel END **Bild ~629-649** (X-divider Bild653); populated letters on right pages. **K** Bild636 =
  Knote/Koch/Klebe/Köhler/Kuhn/Kasting/**Köth**(dom)/Klipper/Knöbel/Kirchmeyer/Köppel/Kaiser/Kropp/Klepper/
  Klipp/Kraft/Krieger/Klugkist/Knöthe — no Konze ("Knote, Georg Carl S1" = Knote, not Kontze); **G** Bild634 =
  only Günther/Göbel/Görmann — no Gans; **I·J** Bild635 = **Issartel**/Jagstetter/Tomski — no Jungkonze;
  **C** Bild629 = **Costabel**(dom)/Caletzhof/Casselmann/Clauß/Brücker — no Conze/Consens. Permalink C leaf
  Bild629 = **p/713ddbcefb**.
  ⭐ **OSB CROSS-CHECK:** Kunze Karlshafen OSB lists Konze 37/61/68/285/287/342, Kontze 287, Conze 99,
  Consens 181, Jungkonze 308, Gans 8 fam — **NONE appear in EITHER baptism register 1830-95/1830-57** ⇒
  those OSB Konze/Gans families are pre-1830 or in marriage/burial records, not 1830s-50s baptisms.
- **219487 Hombressen Taufen — FULL NAME-INDEX swept = NEGATIVE.** Reel 1764; **TWO** title cards
  "Hombressen 1830-1850 mit Register" (Bild 1479 + 1496; likely Erst+Zweitschrift). Register MUCH bigger than
  its label — verbose entries (~1 Seite/baptism) run Bild ~1481→1700 to Seite150+. **⭐ The alphabetical
  Register is at the REEL TAIL, Bild ~1742-1763** (after ALL entries; closing X-card Bild 1764), with **A-Z
  letter tabs on the right edge**; covers the whole register so the window is included. **C** = Bild1742
  **BLANK** (Hombressen has no C surname at all → no Conze/Consens/Conson/Contze). **G** = Bild1745-1746 =
  Gilbert, **Görmann**(dom), Greite/Grebe, Gärtner, Gerland, Geiger, Klinge — **no Gans/Ganß/Ganson**.
  **I·J** = Bild1749 left = blank/sparse — **no Jungkonze**. **K** = Bild1749-1751 (large; covers Seiten
  ~5-258) = Kracking(dom), Köster, Köhler, Kraft, Kollmann, Klinge, Kanngießer, Kammel, Kipper, Naumann,
  Kühlborn — **no Konze/Kontze**. Permalink I·J/K index leaf Bild1749 = **p/480b8e031d**. Hombressen now
  ELIMINATED on the full window (prior Jan-Feb 1835 entry read also stands). Anchors for any future entry
  work: Bild1490=1831/S9; 1535=1834/S54.
- **⭐ ARCHION PERMALINKS minted (Session 131, baptism sweeps)** — full table in the parish research logs.
  **Marzhausen Taufen 181898** (per year — FULL window now minted, 28 Jun 2026): 1833=Bild1635=p/5e8ba53dae;
  1834=Bild1637=p/26d6862541; 1835=Bild1638=p/827d1228f9; 1836=Bild1639=p/fc7030960a; 1837=Bild1641=p/46415dcaa4;
  1838=Bild1642=p/7799fc56ed; 1839=Bild1643=p/1716e4fd6e; 1840=Bild1644=p/02ed36628d; 1841=Bild1645=p/0ee30cbb1b.
  (Note Bild1636 = a Taufbuch Band title page, so 1834 entries sit at Bild1637.)
  **Lippoldsberg Taufen 219778** (per year — FULL window 1831–1841, each year-verified from its written
  "Jahr 18.." header, 28 Jun 2026): 1831=Bild1416=p/2715c68e0d; 1832=Bild1420=p/1d9947f43e;
  1833=Bild1425=p/cf614a3da4; 1834=Bild1429=p/388fed7852; **1835=Bild1435=p/22b146a0af** (★ Charles
  anchor, resolution re-verified to load Bild1435); 1836=Bild1443=p/e4c4cf4766; 1837=Bild1450=p/c014fbca98;
  1838=Bild1457=p/b7c25bc88b; 1839=Bild1464=p/9f378a58d5; 1840=Bild1469=p/bb0324ac19;
  1841=Bild1474=p/68c5c87b06. ⭐ **The reel is LINEAR — Seite = Bild − 1411 throughout 1830–1841** (NOT
  shuffled; the old log "displaced/interleaved tail" + its anchors 1838=1474/1841=1484 were year-misreads;
  1424 is END-of-1832 not start-1833, real 1833=1425). Full table in `germany/lippoldsberg-research-log.html`.
  **Karlshafen Luth 218677**: C/B Bild776=p/c71ba16968; G Bild780=p/cb1104170c; I·J+K Bild782=p/5e21b5dc99.
  **Karlshafen Ref 218713**: C Bild629=p/713ddbcefb; G Bild634=p/937561eb36; I·J Bild635=p/457f24fb3f; K
  Bild636=p/098d4e8781. **Hombressen 219487**: C Bild1742=p/5da8b932e9; G Bild1745=p/084e5f883c; I·J+K
  Bild1749=p/480b8e031d. **Confirmation prime-class permalinks** (per-year-leaf image numbers in logs;
  **Marzh.Konf 181895 — now FULL per class leaf, all year-verified (28 Jun 2026):**
  1846/47=Bild1887=p/c30c9a4cd1; 1848/49=Bild1897=p/dbb3c41e3d; 1850/51=Bild1898=p/06af58910f;
  1851/52=Bild1899=p/d1bd38401c; 1853/54=Bild1900=p/854e558d36; 1855/56=Bild1901=p/068fb09ea7.
  ⚠️ This Band is bound OUT OF CHRONOLOGICAL ORDER and interleaves a duplicate-copy "Konfirmations-Buch" title
  page at Bild1896 (NOT a class leaf); 1846/47 sits at Bild1887 (just after section title 1886), and Bild1895
  is actually 1857/58. Always year-verify a confirmation leaf from its written "Jahr 18.. Pfingsten" header or the
  birth-year+age columns before trusting a Bild→year guess.
  **Karlsh.Luth.Konf 218674 — now per-year for the whole 1847–1855 window (28 Jun 2026):**
  1847=Bild992=p/d4a8e232d9; 1848=Bild993=p/d8e4545182; 1849prime=Bild994=p/61b7bc6da8; 1849/50=Bild995=p/32d29a66fa;
  1851=Bild996=p/c0b0875ad1; 1853/54=Bild997=p/287763d93b; 1854/55=Bild998=p/23c365e665.
  **Karlsh.Ref.Konf 218707 — now year-verified across the window (28 Jun 2026):**
  1847=Bild980=p/820497f9b7; 1848=Bild981=p/493f798b17; 1849prime=Bild984=p/01cad7ff94; 1850=Bild988=p/362a887b61;
  1851=Bild991=p/d4ae7f6912; 1852=Bild994=p/35f039c203; 1854=Bild996=p/8698b183a8; 1855=Bild998=p/61f57334ba.
  ⚠️ **1853 is a binding gap** — Seiten 90–93 absent between Bild994 (Seite88/89=1852) and Bild995 (Seite94=1854);
  likely a no-confirmation year or filming gap. The 1854 class spans Bild995–997. Verify each leaf from its written
  "Jahr 18.. Pfingsten/Ostern" header (legible only at ~2× viewer zoom — click the + button twice first).
  **Hombressen Konf 219481 (Konfirmationen 1831–1901) — prime cohorts year-verified (28 Jun 2026):**
  section title Bild1143; window classes 1846–1856 run from Bild1188, ~2 leaves/class, each with a clear written
  "Jahr 18.. Pfingsten" header. Minted: 1846=Bild1188=p/909330e2a9; 1848=Bild1194=p/7158fa195f;
  **1849prime=Bild1196=p/62e42244b2** (births 1834–35); 1850=Bild1198=p/3cae1c05a4 (right page; left closes 1849).
  Prime 1849/1850 cohorts = local Hofgeismar surnames only, no Konze/Gans. Remaining tail (1847≈Bild1190–1191,
  1851–1856≈Bild1200–1210) still image-only, p/-links pending — locatable by the same "Jahr 18.." headers.
  **Lippoldsberg Konf 219775 — prime-class per year, each year-verified from its "Jahr 18.. — 1ter Pfingsttag"
  header (28 Jun 2026):** 1846=Bild152=p/35f65129a1; 1847=Bild153=p/b85ba8e925; 1848=Bild154=p/76be9ce0d0;
  **1849prime=Bild155=p/3b15604236** (★ the decisive Gans-in-window cohort — #5 Friedrich Wilhelm Gans b.24 Jun 1835;
  "21 Kinder,13 Söhne,8 Töchter" Summa; class spans Bild155–157L; resolution re-verified to load Bild155);
  1850=Bild157R=p/c25e35735a; 1851=Bild159=p/d20091302a; 1852=Bild161=p/399dcfda73; 1853=Bild163=p/35bd3e8c76;
  1854=Bild164=p/e9ec86f00b; 1855=Bild166=p/194db66826. ⭐ **FULL 1846–1855 window now minted (28 Jun 2026).**
  Reel is **in order, NO displaced leaf** — Session 19's "1849=Bild163" was a plain misread: **Bild 163 is genuinely
  1853** (Pfingsten 15 Mai 1853; resolution re-verified). NO Carl Gans confirmand in any class 1846–1855.
  Full table in `germany/lippoldsberg-research-log.html`.
  ⚠️ **Archion throttles after a long run of rapid permalink mints** — the viewer stopped reaching
  document_idle (all screenshots failed) after ~12 mints; finish the "pending" p/-links in a later session.
  Also: the permalink panel opens in DE or EN inconsistently — if it shows "Erstellen", click it (re-renders to
  "Create") then click "Create"; if it shows "Create", click once. Give the panel ~1.5s to render before the
  Create click or it misses. The page-number field sometimes ignores a typed Bild and reverts to the section-title
  Bild — verify the field value (zoom it) after navigating and re-type if needed.

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

---

## No-index baptism reads — Niedermeiser & Bad Karlshafen ×2 (Session 136, 28 Jun 2026)

Calibrations for the continuous (no-name-index) registers, page-read across the
decisive 1834–1836 sibling band. All NEGATIVE for the Konze pool.

- **Niedermeiser 219877** (Taufen 1830–1877): continuous, one baptism per 2-page
  spread, continuous Nro. **1834 begins ~Bild 1857**; band = Bild 1857–1875
  (Nro 87–175). Year-end tallies: 1834 closes Nro 117, 1835 Nro 145.
- **Bad Karlshafen Lutheran 218677** (Taufen 1830–1895): clean monotonic, ~5–6
  baptisms/spread. Band 1 (1830) title = Bild 530. **1834 = Bild 526–529
  (Seite 11–14), 1835 = Bild 529–533 (Seite 14–18), 1836 = Bild 533–534
  (Seite 18–19); 1838 = Bild 538.** Page-input jumps are stale-canvas prone —
  force a redraw with a thumbnail-strip click + a zoom +/- nudge.
- **Bad Karlshafen Reformed 218713** (Taufen 1830–1857): ⚠️ **pathological film —
  two irregularly interleaved copies** (identical Seiten recur at offset Bilder,
  e.g. 400≡403, 406≡410, 414≡419) AND **non-monotonic** (Seite jumps against Bild
  order; months filmed out of sequence; matches the old note "1857 at Bild 522,
  1843 at Bild 535"). **Navigate by the printed YEAR-HEADER per spread, not by
  Bild/Seite arithmetic.** Decisive-band anchors found: 1834 mid = Seite 29
  (Bild 397); 1834 Oct–Dec = Seite 31 (Bild 399); 1835 = Bild 405/410/416/418/
  419; 1836 = Bild 412/413/417/420. An exhaustive entry pass is impractical
  without reading all ~250 baptism images; band sampled by header instead.
- **Reading zoom regions (full-screen):** top banner = year/Monat/Seite header;
  child+father name columns ≈ [700,300,910,650]; godparents column to the right.
