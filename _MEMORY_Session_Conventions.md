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
