# Session 105 — Web-data plugin setup + Kassel archive holdings scan

**Date:** 21 June 2026
**Tools:** Bright Data CLI (newly authenticated), Nimble (authorized, tools pending)
**Scope:** Stand up the open-web research plugins; verify Bright Data with a live
pull on the Trendelburg/Deisel holding archive (Landeskirchliches Archiv Kassel).

---

## NEXT ACTIONS (prioritised — pick up here)

1. **Kassel-only records request** — order/scan **E 1 Trendelburg 177
   Eheprotokollbuch 1779-1830** and **178/179 Zivilstandsregister 1808/1811**
   (not on Archion; could corroborate a Konze/Gannsen marriage or birth).
2. **Archion full-text (in viewer)** — Trendelburg is "komplett transkribiert";
   name-search **Konze/Kontze/Gannsen** in the combined Kirchenbuch vols
   1773-1818 & 1819-1831 and in Trauungen/Beerdigungen for 1828-1835 events.
3. **Charles Jr. + 2407 DeKalb forward** — 1900/1910 St. Louis census sweeping
   variants (Gansen/Ganssen/Konze/**Johnson**); reconcile vs FS "Charles
   Johnson Sr." LZXC-6GB. (Indexed-census/tree work, not full-text.)
4. **Civil War detail** — pull remaining 2nd Missouri Light Artillery cards for a
   descriptive roll (birthplace?); tie the **Rolla 1865** detachment to the
   existing Fort Wyman/Rolla thread; note enlistment **2 Dec 1862, St. Louis**.
5. **US Konze branch** — mine FS Full-Text for the St. Louis Ernst H. Konze
   household (5617 Pennsylvania Ave) and the Baltimore Konze family; check any
   link to the Gannsen line (incl. Adolph Ludwig Gannsen of Baltimore).
6. **Nimble** — confirm tools come online in a fresh session; use for open-web
   portal sweeps (Archivportal-D / Archives Portal Europe).

### NEXT-ACTIONS execution status (21 Jun, end of session)

1. **NA1 Kassel-only records — DONE (as far as possible here).** Confirmed
   177/178/179 are catalog-only (not on Archion). Request email drafted (DE+EN):
   `Kassel_Archive_Request_Draft_June21_2026.md`. *Jed must send it — I can't
   submit external requests.*
2. **NA2 Archion transcription search — ATTEMPTED in-viewer (logged in); no
   register-wide name search exists.** Drove the viewer via JavaScript (register
   IDs: Kirchenbuch 1773-1818 = **220096**, 1819-1831 = **220099**, Taufen
   1830-1863 = **220108**, Trauungen 1830-1892 = **220120**). Findings:
   - Archion's HTR ("komplett transkribiert") is delivered **per page** — each
     image has an empty `div.ocrtext` placeholder filled on demand when you open
     that page; the "Texterkennung" menu item only links to a help page. There is
     **no cross-register name/full-text search box** in the UI to query "Konze"
     across the whole book.
   - So a name sweep = paging through every image's Texterkennung panel (100+
     pp.), or reverse-engineering Archion's private OCR AJAX endpoint (fragile,
     ToS-questionable; the viewer also won't reach a stable load state for the
     browser tools and froze the renderer on a heavier call).
   - **Conclusion:** an automated transcription name-sweep isn't achievable from
     this environment. **Hands-on recipe for Jed:** open 220099 (1819-1831) and
     220096 (1773-1818) in the viewer, turn on Texterkennung, and read/scan for
     Konze/Kontze/Gannsen around 1828-1835 (marriages, baptisms); same for
     Trauungen 220120 and Beerdigungen for the death side. (Note "Zugang kaufen"
     still showed — confirm an active access package is on the account.)
3. **NA3 Census forward-trace — NEEDS HANDS-ON.** No clean hits under Gannsen or
   fuzzy "Gansen~" + St. Louis + Germany. Variant census matching requires
   iterative work + tree confirmation (Charles Jr., 2407 DeKalb); best done in
   Ancestry / the FS tree directly.
4. **NA4 More CW cards — REDUNDANT / not pursued.** The two substantive cards
   (Muster Roll, Returns) are captured above; the rest are GENERAL INDEX /
   REFERENCE pointer cards. The project already holds the **full Compiled
   Service Record** and **pension file** PDFs, which supersede these index cards
   (incl. any descriptive/birthplace data).
5. **NA5 US Konze branch — CAPTURED; kinship needs tree.** Full-Text already
   yielded the St. Louis Ernst H. Konze household (5617 Pennsylvania Ave) and the
   Baltimore Konze family. Full-Text cannot establish a Konze↔Gannsen kin link;
   that requires census/tree reconciliation.
6. **NA6 Nimble — NOT ONLINE.** Re-probed; still only the auth tools. Needs a
   fresh Cowork session for the connector to finish wiring up.

---

## Setup outcomes

- **Bright Data** — CLI installed and authenticated (June 2026). Zones
  `cli_unlocker` and `cli_browser` auto-created. Search + scrape both verified
  live. Known limitation: the API key lacks `bdata budget` permission (harmless
  403 on balance checks); widen token scope in the BD control panel if balance
  visibility is wanted. Re-auth one-liner if a future sandbox resets:
  `bdata login --api-key <Jed's key>`.
- **Nimble** — OAuth authorized this session, but the data tools had not
  registered yet; expected to come online in a fresh chat. Use it for the
  everyday open-web pulls once live (more persistent than the sandbox CLI).
- **Project `CLAUDE.md`** — created in the project root, documents both plugins,
  the open-web-vs-gated-site boundary, and the re-auth note.

## Live test — Trendelburg/Deisel record-holding archive

Target chosen: background on the candidate parishes' holding archive.

### Verified findings (open-web, not original records)

- **Holding archive:** Landeskirchliches Archiv der Evangelischen Kirche von
  Kurhessen-Waldeck, Kassel (archiv-ekkw.de). Founded 1994; oversees the local
  parish archives across **4 regions, 20 districts (Kirchenkreise), 774
  congregations**. States holdings of **200,000+ documents and ~1.3 million
  digitizations spanning 800 AD–21st century**.
- **How the archive exposes holdings:** the Kassel archive does **not** serve a
  record catalog on its own site. It explicitly redirects researchers to:
  - **Archivportal-D** — https://www.archivportal-d.de (open catalog/finding aids)
  - **Archives Portal Europe** — https://www.archivesportaleurope.net (open)
  - **Archion** — https://www.archion.de (the digitized images; gated, needs login)
- **Archion structure for this archive:** Kurhessen-Waldeck records are filed by
  **Kirchenkreis** (church district). Trendelburg and Deisel sit in the
  Hofgeismar area — confirm the exact Kirchenkreis on Archion's "All Archives →
  Hessen → Kurhessen-Waldeck" tree before browsing registers.
- **Coverage caveat (from a genealogy Q&A source):** Archion's Kassel-area
  coverage can **stop around 1794** for some parishes; **LAGIS-Hessen** is the
  fallback for earlier material. Relevant if any pre-1794 gap-filling is needed.

### Next-step leads (open-web, good Bright Data / Nimble targets)

1. Query **Archivportal-D** and **Archives Portal Europe** for "Trendelburg"
   and "Deisel" Kirchenbuch finding aids — confirm exact register signatures and
   date ranges held in Kassel (cross-check against the register calibrations in
   `_MEMORY_Session_Conventions.md`).
2. Resolve the **Kirchenkreis** containing Trendelburg/Deisel on Archion to
   speed register navigation.

## Finding aids located — Trendelburg & Deisel (portal sweep)

Searched Archivportal-D, Deutsche Digitale Bibliothek (DDB), and Archion's
public archive tree. Results verified at the item level.

### Deisel — confirmed
- **Kirchenkreis:** Hofgeismar (today Hofgeismar-Wolfhagen). Deisel is part of
  **Kirchspiel Trendelburg** (per kirchenkreis-hofgeismar-wolfhagen.de).
- **Archion online holdings (Deisel):** Taufen 1830-1861 · Taufen 1861-1906 ·
  Taufen 1907-1979 · Trauungen 1830-1901 · Trauungen 1901-1966.
  URL: https://www.archion.de/de/alle-archive/hessen/landeskirchliches-archiv-der-evangelischen-kirche-von-kurhessen-waldeck/kirchenkreis-hofgeismar/deisel
  (Older pre-1830 Deisel volumes also exist — the project has already worked
  Deisel registers 218821/218824/218851; the list above is the post-1830 set
  surfaced by the portal snippet, not the complete shelf.)
- Secondary: "Dorfleben: Ein Blick in die Geschichte von Deisel" (village
  history, DDB item MUSF5GTV4S3IZQ5QT74OHECH7DD4Z3MW).

### Trendelburg — confirmed
- **Pfarrarchiv Trendelburg** catalogued on Archivportal-D (284 items).
- **Transcription finding aid:** "Kirchenbuch Trendelburg 1819-1831 — Abschrift,
  bearb. Karl Heinz Taenzer, Gernsheim, MS ca. 1990, 186 S." Held in the
  **Bibliothek des Landeskirchlichen Archivs**, Kassel. A typed transcription
  overlapping the start of register 220108 (Trendelburg Taufen 1830-1863) —
  potentially a fast cross-check for hard-to-read 1830-31 entries.
  DDB/Archivportal item: CGFB6EYNDYQPXL47G5DJPSTTU7JGHCPL

### Correction logged
- The DDB entry "Kirchenbuch: Taufen (1755-1830) und Trauungen (1756-1830)"
  (item 2MFEPZJK65BWEJHC2ZPDT4TRIVYW32GB) is **Pfarrarchiv Schweinsberg**
  (Bestand E 1 Schweinsberg), NOT Deisel — discarded as a false lead.

## Archion digitized register catalog (Kirchenkreis Hofgeismar)

The portal's full 284-item Pfarrarchiv Trendelburg list is JS-faceted and
randomly sorted — not reliably page-scrapable with the current tools (and most
of those 284 are administrative files, not registers). The signature prefix for
the parish holding is **"E 1 Trendelburg"**. The list that matters for record
viewing is Archion's digitized catalog:

**Trendelburg** (https://www.archion.de/de/.../kirchenkreis-hofgeismar/trendelburg, churchRegister 220108):
- Taufen 1830-1863  ← register 220108, the active Konze/Gannsen baptism register
- Taufen 1863-1938
- Trauungen 1830-1892
- Trauungen 1893-1999
- (No pre-1830 Taufen and no Begräbnisse shown in the public listing; confirm
  on Archion whether burials are filmed separately. Project has separately used
  Trendelburg 220099/220096 — verify those against this catalog.)

**Deisel** (.../kirchenkreis-hofgeismar/deisel):
- Taufen 1830-1861 · Taufen 1861-1906 · Taufen 1907-1979
- Trauungen 1830-1901 · Trauungen 1901-1966
- (Plus the pre-1830 Deisel volumes the project already works: 218821/218824/218851.)

**Implication for Charles Gannsen (b. 26 Jan 1835):** a Trendelburg baptism
falls in Taufen 1830-1863 (220108, already in progress); a Deisel baptism falls
in Taufen 1830-1861. Both are on Archion behind login.

## Pfarrarchiv Trendelburg full inventory (browser + Bright Data)

Drove the Archivportal-D faceted UI in Chrome to reach the stable collection
node **Pfarrarchiv Trendelburg = "E 1 Trendelburg"** (context
ZRSPBTFOSDGNDQU747ADLJ3SBFW45BA2), then compiled all items via Bright Data
(the portal randomizes sort per request, so collected by repeated sampling +
dedup). **283 of 284 captured** (the 284th is the Bestand header node itself).
Full list saved to `Trendelburg_Pfarrarchiv_Inventory_E1_June21_2026.md`.

**High-value leads — pre-1830 / Charles-era registers held at Kassel that are
NOT in the Archion online Trendelburg set (Archion starts 1830):**
- E 1 Trendelburg 117 — **Trauung 1800-1854** (marriage book covering the
  1828-1835 window directly)
- E 1 Trendelburg 120 — **Begräbnis 1709-1905** (burials spanning Charles's era)
- E 1 Trendelburg 177 — **Eheprotokollbuch 1779-1830** (marriage protocols)
- E 1 Trendelburg 178 / 179 — **Zivilstandsregister 1808 / 1811** (Napoleonic
  civil registers)
- E 1 Trendelburg 115 — Taufe und Abendmahl 1855-1898
- E 1 Trendelburg 70 / 71 — Memorialbuch 1822-1878 / 1878-1912
- E 1 Trendelburg 165 — **Register des Waisenrates Friedrichsfeld 1890-1923**
  (Friedrichsfeld = a candidate parish in the hypothesis tree)
- E 1 Trendelburg 163 / 164 — Register des Waisenrates Trendelburg 1890-1907 / -1920

These are physical files at the Landeskirchliches Archiv Kassel. Whether each is
also filmed on Archion needs checking item-by-item; the marriage/burial/civil
items above appear to extend earlier than the Archion digital coverage and may
require an archive request to Kassel. **Action:** prioritise sig 117 (Trauung
1800-1854) and 177 (Eheprotokollbuch 1779-1830) for a Konze/Gannsen marriage,
and 120 (Begräbnis 1709-1905) for deaths.

## Archion vs Kassel-only — corrected comparison (IMPORTANT)

Re-checked the **full** Archion Trendelburg catalog in-browser (earlier I worked
from a truncated Google snippet — correction below). Archion's Trendelburg
holding is **"komplett transkribiert"** (full-text HTR transcription available)
and far deeper than first stated:

Archion Trendelburg (churchRegister 220108), complete list:
- Kirchenbuch 1613-1655 · 1655-1659 · 1660-1707 · 1708-1772 · 1773-1818 ·
  1819-1831  (combined volumes — mixed Taufen/Trauungen/Begräbnisse, pre-1830)
- Taufen 1830-1863 · Taufen 1863-1938
- Trauungen 1830-1892 · Trauungen 1893-1999
- Beerdigungen 1830-1877 · Beerdigungen 1877-2013
- Konfirmationen 1831-1914 · Konfirmationen 1915-2011

**Correction to earlier in this log:** the "Archion starts 1830 / coverage may
stop ~1794" notes do NOT apply to Trendelburg — Archion covers it back to 1613,
and the whole holding is transcribed.

Comparison of the flagged Kassel files:
| Kassel file | On Archion? | Where |
|---|---|---|
| 117 Trauung 1800-1854 | **Yes (content)** | 1800-1831 in Kirchenbuch 1773-1818 / 1819-1831; 1831-1854 in Trauungen 1830-1892 |
| 120 Begräbnis 1709-1905 | **Yes (content)** | pre-1830 in the combined Kirchenbuch volumes; 1830+ in Beerdigungen 1830-1877 / 1877-2013 |
| 177 Eheprotokollbuch 1779-1830 | **Likely Kassel-only** | a marriage-protocol/banns book, distinct from the marriage register; not in the Archion register series |
| 178/179 Zivilstandsregister 1808/1811 | **Kassel-only** | Napoleonic civil registers, not church books — Archion holds church registers only |

**Net:** the marriage and burial *content* you wanted is already on Archion
(and transcribed) — view it there first. The genuinely Kassel-only items worth
an archive request are the **Eheprotokollbuch 1779-1830 (177)** and the
**Zivilstandsregister 1808 & 1811 (178/179)** — independent record types that
can corroborate or add detail the parish registers don't.

## Can the transcriptions be name-searched outside the Archion viewer?

**Archion:** No. The public Archion search (`/de/suche/`) is a place search
(Ortssuche) — it locates *books* and can filter to those *with* a transcription,
but does not search names *inside* them. The full-text/name search over the
transcription lives **inside the gated viewer** (open a transcribed register
while logged in → search its text), so it needs the Archion subscription and
is per-register, not portal-wide.

**FamilySearch Full-Text (tested in-browser, Jed logged in):**
- Searched surname **"Konze"** → 245 pages of hits, but **every hit is a US
  record** (St. Louis & Baltimore directories/probate/wills, Minnesota,
  North Dakota, Wisconsin, Texas, New York). **No German parish registers.**
- Conclusion: FamilySearch Full-Text does **NOT** index the Trendelburg/Deisel
  Kurhessen-Waldeck ev. church registers — those are **Archion-exclusive**.
  So there is no open/outside-viewer name search of the German side; name
  search of the transcribed German books must be done inside the Archion viewer.

**Unexpected bonus lead (US side):** FamilySearch Full-Text is rich for the
**American Konze family**, directly relevant to the St. Louis thread
(cf. Session 96 StLGS Konze/Gannsen search):
- **St. Louis directories 1902/1903** — a Konze household at **5617 Pennsylvania
  Ave** (Ernst H. Konze, paper/cutter; Elizabeth, nurse; Emma, dressmaker;
  Frederick W.; Ida; Louis, bookkeeper; Louise, steno).
- **St. Louis Carondelet News 1918/1921** — Ensign **Raymond A. Konze**, son of
  Ernest Konze of 616 Dover, died (ship sinking, WWI); American Legion post
  named for him.
- **Baltimore probate/wills 1875-1945** — a large Lewis/Louis Konze family.
- Also Konze entries in Minnesota (Faribault deeds, Waseca genealogies),
  North Dakota, Wisconsin (Milwaukee obits), Texas, Queens NY.
- **Action:** mine FamilySearch Full-Text for the US Konze branch (esp. St.
  Louis Ernst H. Konze family) — a genuine outside-viewer, free, name-searchable
  resource that complements the Archion-only German side.

## FamilySearch Full-Text — "Gannsen" hits (DIRECTLY on target)

Searching surname **"Gannsen"** in Full-Text (US records) returned material
directly about Charles Gannsen — all free, name-searchable, outside any viewer.
**AI-transcribed; verify each against the image before recording as confirmed.**

Highest value:
- **St. Louis Directory 1895 / 1895-1896:** "**Gannsen Charles**, watch[maker],
  r. rear **2407 DeKalb**" AND "**Gannsen Charles, jr.**, lab., r. rear 2407
  DeKalb." → Charles Sr. (watchmaker) and a **son Charles Jr.** (laborer) at the
  same address. New residential address + a Jr. lead to chase.
- **Missouri Military Records 1861-1865** (multiple cards): "**Charles Gannsen,
  1st Battery / Battery B, 2nd Reg't Missouri Light Artillery**" — Battery Muster
  Rolls, Regimental Descriptive Book, Returns. Confirms the unit and may carry
  physical-description / enlistment detail. One card cross-references
  "**Gunnsen, Chas. L.** or Gannsen, Chas." (spelling variant to watch).

Possible relatives (lower confidence — verify):
- **Adolph Ludwig Gannsen, of Baltimore** (Richmond Co., NC marriage register,
  1930s) — note the **Baltimore** tie alongside the large Baltimore Konze family
  found earlier; worth probing for a Konze/Gannsen link.
- **Joh(ann) Gannsen, age 59, New York 1859** (migration index) with relatives
  Antje/Anke — Frisian-sounding names; may be an unrelated North-German Gannsen.
- Scattered, likely unrelated: Emil Gannsen (Scott Co., Iowa), Daisy Gannsen
  (Albany NY), Gannsen (Moore Co., NC). Italian "Gannsen" hits = OCR noise.

**Assessment / connection to the Konze line:** the St. Louis directories show
**Gannsen** (Charles, 2407 DeKalb) and **Konze** (Ernst H. household, 5617
Pennsylvania Ave) as *separate* households in the 1890s-1900s — the directories
alone don't link them. But Full-Text now gives an outside-viewer, free way to
work the **American** Charles Gannsen (residence, occupation, a son Charles Jr.,
and CW unit detail) that complements the Archion-only German Konze records.
Next: open the 1895 directory image to confirm the DeKalb entries, and pull the
full set of Missouri Light Artillery cards for enlistment/description detail.

## Confirmed in-image (FamilySearch Full-Text viewer) — Charles Gannsen

Opened the actual records (Jed logged in) to confirm the transcript hits:

**St. Louis Directory — Gould's 1895 (ark 3QHV-V38V-568N, image 268 of 1056):**
printed entries confirm **"Gannsen Charles, watch[maker], r. rear 2407 DeKalb"**
and **"Gannsen Charles, jr., lab., r. rear 2407 DeKalb"** — Charles Sr.
(watchmaker) and son Charles Jr. (laborer), same address, 1895.

**Battery Muster Roll, Jan-Feb 1863 (ark 3QHJ-H3BV-K6RP, img 1579) — handwritten,
viewed:** "Charles Gannsen, [Pvt], 1st Batt'y B, 2 Reg't Missouri Art'y. ...
Present or absent: **absent**. Remarks: **on detached service at Small Pox
Hospital since Feb 20, 1863, by order of Maj Genl Curtis.**" (Book mark 258.)

**Company Returns card (ark 3QHJ-X3BK-RJW5, img 39) — handwritten, viewed —
service timeline:**
- **Dec 1862: "Gained Dec 2/62, St. Louis, Mo. Joined by enlistment."**
  → enlisted **2 Dec 1862 at St. Louis**.
- Jan 1863: absent sick, regimental/​smallpox hospital since 30 Jan 1863.
- Mar-July 1865: absent on detached service, **Rolla, Mo.** (S.O. 82, Hd Qrs
  Dept of the Mo., 27 Mar 1865).
- Aug-Sep 1865: absent on detached service, St. Louis / Dept HQ of Missouri.
- (Book mark 546, A. Knapp, copyist.)

The remaining "Gannsen" military hits are **GENERAL INDEX / REFERENCE pointer
cards** ("Original filed under Gannsen Charles") — cross-references, no new data.
No Regimental Descriptive Book (with a birthplace field) surfaced in this set.

**⚠ AI-transcription error caught:** the Returns card's machine transcript renders
"Died Jan 363," but the handwriting reads "absent sick ... since Jan 30/63," and
the same card shows continued service into Sept 1865 — he did **not** die in
1863. Classic reason to verify Full-Text transcripts against the image.

**New leads for the project:** (1) son **Charles Gannsen Jr.** (St. Louis, 1895);
(2) precise enlistment **2 Dec 1862, St. Louis**; (3) **Rolla, Mo.** detachment
1865 — note the project's existing Fort Wyman / Rolla thread; (4) smallpox-
hospital detached service early 1863.

## Forward-tracing the Gannsen household (census / death / name evolution)

Tried to follow Charles Sr. & Jr. (2407 DeKalb, St. Louis) forward in
FamilySearch:
- **Indexed Records search, surname "Gannsen," Missouri:** the only clean
  "Gannsen" hits are the **1895 city directory** and the **Civil War** records
  (Soldiers Index + Missouri Union Service Records, several cards; one indexed
  as "Charles L Gannsen," birth indexed variously 1839/1842 — vs project's
  1835). **No 1900/1910 census and no death record surfaces under the exact
  spelling "Gannsen."**
- **Full-Text phrase "2407 DeKalb":** 0 hits (address not phrase-indexed that way).

**Interpretation (not yet proof):** "Gannsen" looks like a *transitional*
spelling that appears in the 1862-1895 window (enlistment → 1895 directory) but
does not clearly persist into 20th-c. census/death indexes. That is consistent
with the project's documented name-flux pattern (Konze/Kontze → Gannsen → …),
and note the project's own **"Charles Johnson Sr." (FS LZXC-6GB)** thread —
i.e. the line may run toward **Johnson**, not back to Konze. The household is
most likely indexed in later census under a *variant* (Gansen, Ganssen, Gansten,
Konze, or Johnson), not "Gannsen."

**Recommended hands-on next step (better done in-tree / on Ancestry):** run the
1900 & 1910 St. Louis census for the 2407 DeKalb area and for "Charles" b. ~1835
Germany, sweeping spelling variants (Gansen/Ganssen/Konze/Johnson), and reconcile
Charles Jr. against the existing FS tree. Full-Text confirmed the 1862-1895
American spine; the 20th-century continuation needs the indexed-census + tree
work the project normally does directly.

## Boundaries / evidentiary note

These are **descriptions of holdings from open web pages**, not the church-record
images themselves. The actual register images remain behind the Archion login and
must be read via the in-viewer workflow (Archion zoom tricks in the memory file).
Treat any catalog date range as a pointer, verify against the original image
before recording as confirmed — same standard as the rest of the project.

- FamilySearch's parish wiki could not be scraped (Incapsula bot block); read it
  directly in-browser if its holdings table is needed.

## Sources (fetched live via Bright Data, 21 Jun 2026)

- Landeskirchliches Archiv Kassel — https://www.archiv-ekkw.de/?lang=en
- Archion, Kurhessen-Waldeck archive — https://www.archion.de/en/all-archives/hessen/landeskirchliches-archiv-der-evangelischen-kirche-von-kurhessen-waldeck
- BD SERP result set for "Trendelburg Deisel Kirchenbuch Archion Kurhessen"
  (FamilySearch wiki, Archion, Archivportal-D, genealogy.stackexchange)
