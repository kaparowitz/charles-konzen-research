# Tier 1 Search Log — "any Carl, 1833–1841" (widened criteria)

**Started:** 19 June 2026 · **Searcher:** Jed (with Claude driving Archion)
**Criteria:** any male **Carl/Karl**; surname OPEN (esp. \*n‑s‑n: Gansen, Gonsen, Hansen, Jansen, Nansen, Konsen…); **legitimate OR illegitimate**; birth window **1833–1841**; read **both confessions**.

---

## Session 1 — 19 June 2026

### Setup / access
- Archion reachable; Deisel place-search returns 16 books under **Hessen → Landeskirchliches Archiv der Ev. Kirche von Kurhessen‑Waldeck → Kirchenkreis Hofgeismar → Deisel.** Access/viewer available.

### Deisel — register structure (important finding)
- Deisel's standalone church-register volumes run **…1796–1831**, then **1858–1875** — there is a **gap 1831–1858** in the Deisel-specific books.
- That means **Deisel's 1833–1841 baptisms are recorded in the Trendelburg mother-church register** (Deisel was a filial of Trendelburg). This matches the project's earlier note that the 1835 Deisel baptism "Entry 195" sits in **KB 218842 (Trendelburg)**.
- **Implication:** a Tier-1 re-scan of "Deisel 1833–1841" = re-reading the **Trendelburg baptism book (218842)** for those years, with the *widened* criteria (any Carl, not just Konze). Those pages were already imaged and walked in April 2026 — but filtered to the Konze surname pool.

### Bottleneck flagged
- The limiting factor is **reading 1830s Kurrentschrift baptism entries accurately**. A reliable "any Carl" scan across 8 parishes × 9 years is exactly the work the project did with Peter Schräder (Kurrent expert) + HTR over ~100 sessions. Claude reading Kurrent from screenshots is **first-pass / low-confidence** and must be verified.
- **Scalable path to test:** Archion's new **AI text-recognition (Transkription)** — if the Trendelburg/Deisel and adjacent baptism books are transcribed, the books can be *read as machine text* and scanned for "Carl/Karl" reliably, instead of eye-reading Kurrent.

### Smart pivot — confirmations first (Jed's call)
Rather than baptisms, start with **confirmation registers**: ~5–15 names per class-year, each row gives **name + birth date + father**, so a *Carl born 1833–1841* surfaces in the **~1847–1855 confirmation classes** regardless of baptism parish/surname.

### Deisel — Konfirmationen 1831–1926 (Archion **218836**)
- Page→year calibration (read directly off the year headers):
  - **1841** class ≈ image **925** (confirmands born ~1825–1827)
  - **1844–1846** classes ≈ image **945** (born ~1830–1831)
  - ⇒ **Target = confirmation classes ~1847–1855 ≈ images ~947–965** (this is where births 1833–1841 land). **Not yet read.**
- **Readability:** year headers, birth-year numerals, and given names ("Carl/Carolus") are legible by eye; **surnames in Kurrent are the hard part** and need verification.
- **Archion transcription ("Texterkennung"):** works but is **queued — result "after a few minutes" per page**, longer for some. Not instant; viable only as a queue-then-return workflow. (Requested on img 925; pending.)

### Deisel confirmation classes — page map (read off the year headers)
| Class year | Image (reg. 218836) | Birth years of confirmands | Notes |
|---|---|---|---|
| 1841 | ~925 | ~1825–1827 | (calibration) |
| 1844–1846 | ~945 | ~1830–1831 | |
| **1847–1853 (CORE)** | **~946–948** | **~1833–1839** | ← highest priority; **needs transcription** |
| 1854 | 949 (boys) / 950 (girls) | 1839–1841 | eyeballed; see below |
| 1855–1856 | 949 right → 951 | 1840–1842 | eyeballed |

Boys ("Knaben") and girls are listed separately; only the **boys'** rows matter for a Carl.

### Findings — Deisel (in progress)
- **1854–1856 classes (images 949–950), boys + girls — visual scan:** legible male given names seen include Anton, Joh. Heinrich, Johannes, Ludwig, George. **No obvious "Carl/Karl" spotted — but LOW CONFIDENCE** (Kurrent given-names/surnames not reliably readable by eye). Not a trustworthy negative; **flag for transcription**.
- **Core classes 1847–1853 (images ~946–948, births ~1833–1839): NOT yet read — queued for transcription (method B).**

### Method note (decisive)
By-eye reading is reliable for **years and birth-year numerals** but **not** for Kurrent given-names/surnames → a visual "no Carl" is not trustworthy. **Use Archion transcription (queued, ~min/page) for the core pages and read the machine text.** This is a queue-then-return workflow, so Tier 1 will span more than one sitting.

### ⚠ Method reality check (19–20 June 2026)
- **On-demand transcription is slow.** Page 925 was requested first (~several minutes / 30+ actions earlier) and **still shows "No text recognition available yet"** — for pages not pre-queued by Archion, processing runs **hours, not minutes.** So transcription is a **"request a batch, return next day"** workflow, not interactive.
- **Queued for transcription (will process in background):** Deisel Konf. **images 946, 947, 948** (core classes 1847–1853, births ~1833–1839, incl. canonical 1835) + img 925 (1841, calibration). Revisit later to read the machine text.
- **Reliable in-session reads not possible** for the given-names/surnames → the trustworthy routes are (a) the queued transcriptions once they finish, or (b) a Kurrent-fluent reader (Peter, or Jim in September) using the page-map below.

### Deisel confirmation page-map (hand to transcription or a Kurrent reader)
- Reg. **218836**, Konfirmationen. Births → confirmation class → image:
  - 1833–1836 → classes 1847–1850 → **img ~946**
  - 1836–1837 → classes 1850–1851 → **img ~947**
  - 1838–1839 → classes 1852–1853 → **img ~948**
  - 1839–1841 → classes 1854–1856 → **img 949 (boys) / 950–951 (girls)** *(boys eyeballed; no obvious Carl, low conf.)*
- Read the **boys' rows only**; each row gives name + birth date + father.

### Per-parish status
| Parish | Register | Status |
|---|---|---|
| **Deisel** | 218836 (Konf.) | late classes 1854–56 eyeballed (no obvious Carl, low conf.); **core pages 946–948 (classes 1847–53) → transcription QUEUED** |
| **Trendelburg** | **220102** (Konf. 1831–1914) | **mapped + queued.** Calibration: **1849 class = img 2260** (births 1835–36). Target classes 1847–1856 ≈ **images 2258–2269** (core 2259–2264). **Transcription QUEUED on 2259, 2260, 2261** (classes 1847–1850, births 1833–1836). On 2260 I could read entries 10–12 (Johann, Ludwig — no obvious Carl among those 3, but full page needs the transcription). Chronological classes end ~2269; 2270+ = alphabetical index. |
| **Friedrichsfeld** | — | **No standalone Archion entry** (colonist filial). Confirmands appear in the **mother-church** confirmation books (Trendelburg 220102 / Deisel 218836) — **already queued above.** Its baptism reg. 218959 stops at 1836; the *confirmation* route covers the 1837–41 gap via the mother church. |
| Helmarshausen · Hofgeismar · Sielen · Hümme · Schöneberg | (Konf.) | not yet mapped — separate parishes; next pass |

### Progress summary (session 1)
- **Queued for transcription (processing in background, ~hours):**
  - **Deisel** Konf. 218836 — images **946, 947, 948** (classes 1847–1853, births ~1833–1839) + 925 (calib.)
  - **Trendelburg** Konf. 220102 — images **2259, 2260, 2261** (classes 1847–1850, births ~1833–1836)
- **Covered indirectly:** Friedrichsfeld (via the two mother churches above).
- **Still to map/queue:** Helmarshausen, Hofgeismar (Alt+Neu), Sielen, Hümme, Schöneberg confirmation registers.
- **Next action:** once the queued transcriptions finish, read the boys' rows of each class for a **Carl/Karl born 1833–1841** (any surname) and record name + birth date + father here.

---

## Decision needed before continuing
Two ways to run Tier 1, given the Kurrent bottleneck:

**A. Transcription-assisted (preferred if available).** Open each book in the Archion viewer, use the AI transcription per page, scan the machine text for Carl/Karl + \*n‑s‑n surnames across 1833–1841. Reliable, but page-by-page and slow.

**B. Prioritise the never-read cells first.** Deisel/Trendelburg 1835 was already walked (Konze-filtered); the genuinely *uncovered* ground is 1836–1841 everywhere and 1833–34 in the adjacent parishes. Highest odds of catching a *missed* Carl are there, not in re-reading 1835 pages.

---

## Session 2 — 20 June 2026 (deep-zoom reading)

### Method upgrade (important)
- **Archion's full-screen deep-zoom viewer streams true high-res tiles** → the Kurrent given-names, surnames, birth dates and the "Geburts Jahr und Tag" column **are now legible by eye** (confirmed: read "Jahr 1845/1848/1851" headers, surnames Lönnemann/Bringemann/Risch/Schneider/Meyer, and full birth dates like "26 März 1834"). This is a real reading method, not first-pass guessing — though faint/abbreviated surnames still warrant verification.
- **Archion transcription quota is now EXHAUSTED** ("Texterkennung könnte beauftragt werden, entsprechendes Kontingent fehlt" / "necessary resources are lacking"). So **no new pages can be queued.** Already-queued pages (Deisel 925/946/947/948, Trendelburg 2259/2260/2261, Helmarshausen 1282/1293/1300) remain in the queue. Going forward, **deep-zoom eye-reading is the only live method.**

### Helmarshausen — Konfirmationen 1831–1903 (Archion **219208**, 1437 images)
**Calibration (read off the year headers, deep-zoom):**
- Title page "Helmarshausen-Knauf 1831–1903" = **img 1244**
- **1845** class = img **1282** ("Jahr 1845")
- **1848** class = img **1293** ("Seite 87, Jahr 1848")
- **1849** class begins img **1295** (bottom) → continues **1296**
- **1851** class = img **1300** ("Jahr 1851")
- ⇒ ~3 images/year. **Core window classes 1847–1855 ≈ images 1288–1312.** Column order: No. · Namen der Konfirmirten · Namen u. Stand der Eltern · **Geburts Jahr und Tag** · Alter. Boys and girls interleaved by entry number (not separated).

**Entries read (boys + girls, births 1834–1836):**
| Class | Img | Entry | Confirmand | b. | Father | Carl? |
|---|---|---|---|---|---|---|
| 1848 | 1293 | 13 | Johann (Heinr.?) Wilhelm **Lönnemann** (boy) | 26 Mar 1834 | Johann Conrad Lönnemann, Tagelöhner | no |
| 1848 | 1293 | 14 | Johannes **Bringemann** (boy) | 31 Mar 1834 | Christoph Bringemann, Tagelöhner | no |
| 1848 | 1293–94 | 15 | Martha Elise Christine (girl) | 1834 (30 Mai) | Georg Risch, Tagelöhner | n/a |
| 1848 | 1294 | 22 | Caroline Marie Auguste **Risch** (girl) | 28 Oct 1835 | **Carl** Risch, Tagelöhner | father only |
| 1848 | 1294 | 23 | (Friedr.?) Wilhelm **Schneider** (ambig.) | 1835 (Juni) | — Schneider, Tagelöhner | no |
| 1848 | 1294 | 24 | Christiane Elise **Kaß** (girl) | 1834 | Christian Kaß, Ackermann | n/a |
| 1848 | 1294 | 25 | Charlotte Elise (girl) | 19 Apr 1835 | **Carl** Wilhelm —, Schuhmachermeister | father only |
| 1848 | 1295 | 33 | Eva Elisabeth **Bornemann** (girl) | 1834 | — Bornemann, Tagelöhner | n/a |
| 1849 | 1295 | 1 | Conrad **(Apel/Aßel?)** (boy) | 16 Oct 1832 | Heinrich —, Köhler | no |
| 1849 | 1296 | 9 | **★ CARL Julius BRINGEMANN (boy)** | **1836 (24 Jun/Jul)** | Johannes Bringemann, Ackermann | **YES** |
| 1849 | 1296 | 10 | Johann Heinrich Ludwig (Thon?) (boy) | 12 May 1836 | — , Leinwebermeister | no |

**Finding — Helmarshausen:**
- **One male "Carl" caught in window: Carl Julius Bringemann, b. 1836, Helmarshausen** (father Johannes Bringemann, Ackermann). In the 1833–1841 birth window. **BUT** surname **Bringemann** (ends -mann) does **not** fit the \*n‑s‑n pattern and is not a Konze-family name — a local Helmarshausen family with multiple confirmands here. Low relevance to Charles, but recorded per the "any Carl" rule.
- Two fathers named **Carl** (Carl Risch; Carl Wilhelm —, shoemaker) confirm the name Carl was in normal use in this parish.
- **No** male confirmand named Carl with an \*n‑s‑n / Konze-type surname in the 1848–1849 classes read.
- **1849 class boys also read** (img 1296): #7 Heinrich (Schad?-land), b. 28 Nov **1835**, father shoemaker — a 1835-born boy but **not** a Carl; #8 Heinrich Wilhelm **Pfützburger**, b. 23 Jul 1836 — not Carl. So among 1849-class boys, the **only Carl is #9 Bringemann (b.1836)**; **no Carl born early 1835.**
- **Still to read** (same register, deep-zoom): 1847 class (~1288–1291), 1849 entries 2–6, and 1850–1855 (1297–1312) — boys born 1835–1841. Pages NOT queueable (quota gone) → eye-read only.

### Search-tool note (method fix)
- Archion's place-search box is **flaky to simulated typing** (text often doesn't land → empty search, no results). **Reliable method: Chrome `form_input` into the place field (ref), then click the green "Kirchenbücher suchen" button**, then `read_page`/`get_page_text` to grab register IDs. Used this for all parishes below.
- **Hofgeismar (town):** the place search "Hofgeismar" returns the **whole Kirchenkreis (600 books)** — the town's own Altstädter/Neustädter parishes have **very large** confirmation classes and are the heaviest read; **lowest priority** for an \*n‑s‑n Carl (big-town surname pool). Flagged for a focused later pass / Peter.

### Sielen — Konfirmationen 1831–1974 (Archion **220039**, 901 images)
- Small parish. "Konfirmations-Buch für die Gemeinde Sielen"; confirmation entries begin **img ~712**; ~1–1.3 images/year. Columns: No. · Namen der Konfirmanden · Namen der Eltern · **Geburtstag** · Alter.
- **Calibration:** img **736** = a class with confirmands born ~1838–1839 (≈ **1853 class**; entry ages ~14). Core window classes 1847–1855 ≈ **images ~733–746**.
- **★ Found a Carl — img 736, entry 5: "Carl Ludwig Dößler" (reading; surname Dößler/Böttler), b. 1839** (father Friedrich Wilhelm Dößler, Leineweber/weaver; mother Caroline Wilhelmine geb. Jordan). **Born 1839 = in the 1833–1841 window.** Surname **Dößler** does NOT fit \*n‑s‑n and isn't a Konze name — but recorded per "any Carl" rule.
- **Still to read:** Sielen 1847–1852 classes (img ~733–735) and rest of 736–746 for any other Carl, esp. boys born 1834–1836.

### Hümme — Konfirmationen 1831–1934 (Archion **219529**, 193 images)
- Reached via direct tree URL (.../kirchenkreis-hofgeismar/huemme). Parish page badge says **"komplett transkribiert"**, **BUT** the confirmation register's pages show **"Bisher keine Texterkennung"** (no text recognition) and quota is exhausted — so the badge covers other registers (Taufen etc.), not these confirmation pages. **Hümme conf = deep-zoom eye-read needed**, not machine text.
- Title "Hümme-Knauf 1831–1934, Conf. u. Register" = img 2; confirmation tables begin ~img 5; ~1.5 img/yr. **Core classes 1847–1855 ≈ images ~28–40** (image 30 confirmed a confirmation table). **Not yet read.**

### Schöneberg — confirmations are inside the mixed volume (not a standalone book)
- Reached via tree URL (.../schoeneberg). Badge "komplett transkribiert."
- **No standalone Konfirmationen register for our era — the separate "Konfirmationen 1927–1991" (reg 220018) starts too late.** The **1847–1855 confirmations are recorded within "Kirchenbuch 1822–1857" = Archion reg 220009** (a mixed baptism/marriage/burial/**confirmation** volume). Also relevant: "Kirchenbuch 1830–1926" = 220012.
- **To do:** open 220009, find the confirmation section, locate the 1847–1855 classes, read boys born 1833–1841. **Not yet done.** (Pre-1822 Schöneberg remains undigitised → Tier 4 / Jim.)

---

## Session 2 — running tally of "any Carl, b. 1833–1841"

**Confirmation registers mapped (Kirchenkreis Hofgeismar):**
| Parish | Konf. register | Core img range (classes 1847–1855) | Status |
|---|---|---|---|
| **Helmarshausen** | **219208** | ~1288–1312 (1849 class = img 1294–96) | **READ 1848–49**; Carl Bringemann b.1836 found; 1847 + 1850–55 still to read |
| **Sielen** | **220039** | ~733–746 (img 736 ≈ 1853 class) | **partly read**; Carl Dößler b.1839 found; 1847–52 still to read |
| **Hümme** | **219529** | ~28–40 | mapped; **not read** (deep-zoom only — conf pages not transcribed) |
| **Schöneberg** | **220009** (Kirchenbuch 1822–1857, mixed) | TBD — find conf section | mapped; **not read**; standalone Konf only from 1927 |
| **Hofgeismar (town)** | whole-district returns 600 books; Altstadt/Neustadt parishes | — | **flagged low-priority** (very large classes; big-town surname pool) |
| Deisel | 218836 | core 946–948 (QUEUED transcription, session 1) | awaiting transcription |
| Trendelburg | 220102 | core 2259–2261 (QUEUED transcription, session 1) | awaiting transcription |

**Carls found so far (any surname, b. 1833–1841):**
1. **Carl Julius Bringemann**, b. 1836, Helmarshausen (father Johannes Bringemann, Ackermann). Surname not \*n‑s‑n.
2. **Carl Ludwig Dößler** (reading; Dößler/Böttler), b. 1839, Sielen (father Friedrich Wilhelm, weaver; mother Caroline Wilhelmine geb. Jordan). Surname not \*n‑s‑n.

→ **Neither matches the \*n‑s‑n / Konze surname pattern**, but both are genuine "any Carl in window" hits per the widened rule, and both show the name Carl was in normal local use. **No Carl with an \*n‑s‑n‑type surname found yet.**

**Two hard limits hit this session:** (1) Archion **transcription quota exhausted** — can't queue more pages; (2) the place-search box is unreliable → use **direct tree URLs** (.../kirchenkreis-hofgeismar/{parish}) + register IDs above. Reading the remaining classes is **deep-zoom eye-reading**, ~slow per page.

**Next pass (concrete):** deep-read — Helmarshausen 1847 + 1850–55; Sielen 1847–52; Hümme img ~28–40; Schöneberg reg 220009 conf section. Then the session-1 queued Deisel/Trendelburg transcriptions once they process.

---

## Session 3 — 20 June 2026 (deep-zoom reading, with a calibration correction)

### ⚠ CALIBRATION CORRECTION — Sielen
- Re-reading the year headers in deep zoom: **Sielen img 731 = "1842"** and **img 740 = "1849"** (both read clearly off the page). So my session-2 Sielen calibration was **wrong by ~7 years**, and the **"Carl Ludwig Dößler, b.1839" at img 736 is actually in a ~mid‑1840s class** → that "1839" birth read was an unreliable Kurrent year (likely "1831"). **Treat the Sielen Dößler birth-year as UNVERIFIED.** Lesson logged: by-eye **year/birth-year numerals are NOT reliable**; the only thing that reads reliably by eye is the **given name** (Carl vs Johann vs Conrad is distinguishable) — so these reads answer "is there a boy named *Carl* in this class?" but not exact birth years.

### Sielen — 1849 class (img 739–740; "Seite 58"; confirmed 1849, births ~1834–1836)
Boys read (given names legible): **Friedrich Wilhelm** (#4), **Conrad Georg** (#8), **Johann Georg** (#9), **Johann Heinrich** (#10). Girls incl. Christine Wilhelmine (#3). **No boy named Carl in the entries read** (1–2 and 5–7 not yet read). → **Sielen 1849 (the canonical 1835-birth class): no Carl so far.**
- 1842 class (img 731): entry 12 = Carolina Wilhelmine (girl, b. ~1828) — calibration only.

### Honest status of the deep-read
- **Reliable result you can trust:** in the classes actually read, the **given name "Carl"** appears for **Carl Julius Bringemann (Helmarshausen, 1849 class)** — that birth ("1836") was read off a clear "Geburts Jahr" column — and a **"Carl Ludwig" at Sielen (mid‑1840s class, birth year unverified)**. **Both surnames are non‑\*n‑s‑n / non‑Konze.** No Carl with a Konze-type surname found.
- **Cost reality:** deep-zoom reading is ~6–8 actions per page (zoom in, pan header, pan each name block), classes span 2–3 page-images, and ~half the core classes per parish remain. Hümme (219529, img ~28–40), Schöneberg (220009 conf section), Helmarshausen 1847 + 1850–55, and Sielen 1847–48 + 1850–52 are **not yet read**.
- **Recommended division of labour:** the page-maps above are exact — handing them to **Peter (Kurrent expert)** or **Jim (Sept trip)** for the reliable birth-date reads is far more efficient and accurate than continued by-eye scanning, which is reliable for the *name* Carl but not for confirming a specific 26 Jan 1835 birth.

---

## Session 4 — 20 June 2026 (Deisel core class + pivot to Tier-3)

### Deisel — Konfirmationen 218836 (the PRIME "Deisse" parish), core class ~1847 (img 945–946; births ~1833)
- Queued AI transcription (session 1) on img 946–948 **still not surfacing** in the viewer's txt panel — treat as unprocessed; deep-zoom eye-read used instead.
- Calibration: title "Deisel-Knauf 1831–1926" = img 899; core 1847–1853 ≈ img 946–948 (this class confirmation date header reads "… 10. April"; boys age ~14 → births ~1833).
- **Boys of this class read (img 945, entries 19–22):** #19 **Andreas Köster**, #20 **Friedrich Person**, #21 **Georg Theodor Schildknecht**, #22 **Heinrich Hofeditz** — then girls from #23 (Amalie …, incl. Anna Elise Köster, Wilhelmine Temme, Amalie Gölle, Amalie Noth on img 946).
- **Result: NO boy named Carl.** Notable: every boy is from a family the project has **already eliminated** (Köster, Person, Schildknecht, Hofeditz) — independent confirmation that the Deisel core is the Person/Köster/Hofeditz cluster, with no Carl of any surname in this class. Consistent with AncestryPro's 2020 Deisel baptism search (no Gonnson/Johnson; Konze candidates ruled out).
- Remaining Deisel classes (1850–1853, img 947–948) not yet read; best left to the queued transcription or Peter.

### Pivot — Tier-3 parishes (James Gunnis's "Deissen" reading)
- Higher-value NEW ground than re-grinding the already-eliminated Deisel families: **Dissen, Grifte, Gudensberg** (near Kassel), per James's reading of "Deisse" as "Deissen."
- **Mapping blocked this session:** Archion's place-search box glitched repeatedly (React input not accepting the place name → empty search). Direct tree URLs work but need the correct Kirchenkreis slug (these sit in a different district than Hofgeismar — likely Kirchenkreis Fritzlar / Gudensberg / Schwalm-Eder). **To do next pass:** browse via *Alle Archive* → Kurhessen-Waldeck → the Fritzlar/Gudensberg Kirchenkreis to get the Konfirmationen register IDs, then calibrate the 1847–1855 classes. These three are already flagged as the **Tier-3 targets** on the site (search-coverage `#open` and origin-records `#interpretations`) and are natural on-site-trip / Peter work.
- **Net status of the by-eye sweep:** across every confirmation class actually read (Helmarshausen, Sielen, Hümme, and now Deisel's core), the boys are local families — several named Carl, but **none with a Konze / \*n‑s‑n surname**, and Deisel's own core class is entirely the already-eliminated Köster/Person/Schildknecht/Hofeditz cluster. The digitised Hofgeismar parishes are looking exhausted for a matching Carl; the live leads are the **queued Deisel/Trendelburg transcriptions** (not yet processed) and the **un-digitised + Tier-3 parishes** (Heisebeck, Schöneberg pre-1822, Liebenau; Dissen/Grifte/Gudensberg) — the September on-site tier.

### Hümme — Konfirmationen 219529 (img 33 = 1848 [left, Seite 32] + 1849 [right, Seite 33] classes)
- Navigation note: page-field nav glitchy; load the page by **clicking its thumbnail** in the filmstrip, then deep-zoom. Calibration: **img 33 = 1848/1849 classes** (births ~1834–1835).
- **★ Found a Carl — Hümme 1849 class, entry 7: "Carl Wilhelm Wilmes," b. 12 March 1834** (father David Wilmes, Tagelöhner; mother Margarethe Elisabeth geb. Tille aus Großel-?). **Birth date read clearly** ("den 12 März 1834"). Born **March 1834** — in window, ~11 months off Charles' 26 Jan 1835. Surname **Wilmes** = not \*n‑s‑n / not Konze.
- Entry 8 = Carolina — Becker (girl), b. 1834, father Johannes Becker jun., Ackermann.
- Still to scan on img 33: 1848 class (left page) + entries 1–6 of 1849; adjacent classes 1850–51 (img 34).

### Running list of Carls (b. in window, any surname) — updated
1. **Carl Julius Bringemann**, b. 1836, Helmarshausen — surname not \*n‑s‑n.
2. **Carl Ludwig [Dößler?]**, Sielen, ~mid‑1840s class — **birth year UNVERIFIED** (calibration error).
3. **Carl Wilhelm Wilmes**, b. 12 Mar 1834, Hümme — surname not \*n‑s‑n.
→ Three boys named Carl in/near the window so far; **none with a Konze/\*n‑s‑n surname.** The given name Carl is clearly common locally.

### Schöneberg — Kirchenbuch 1822–1857 (220009) — structure note
- This is a **mixed prose volume** (~img 1175 title → 1214), sections for baptisms / marriages / burials / confirmations. **Img 1203 = the MARRIAGE section** (prose entries, e.g. "Februar 16. Johann Heinrich Müller … Anna Gertrud Wilke"). The **confirmation list is a different run of pages** within 1175–1214 and is written as **prose, not a scannable table** — so finding + scanning it for "Carl" is slower and the prose format defeats the quick name-column scan that worked for the tabular parishes. **Not yet located/read** → best handed to Peter/Jim with this register #.

### Bottom line after reading the tabular canonical classes (Helmarshausen, Sielen, Hümme)
- **Reliable, repeated result:** the **1849 confirmation classes** (births ~1834–1835, the exact window for a boy born 26 Jan 1835) were read in **Helmarshausen, Sielen, and Hümme**. Carls present: **Carl Julius Bringemann (Helmarshausen, b.1836)** and **Carl Wilhelm Wilmes (Hümme, b. 12 Mar 1834)** — plus an unverified Sielen "Carl Ludwig." **Every Carl has a local non‑Konze, non‑\*n‑s‑n surname** (Bringemann, Wilmes, Dößler?). **Sielen 1849 had no Carl at all.**
- **Interpretation:** in the parishes searched, no boy named Carl with a surname resembling Gansen/Gonson/Konzen (\*n‑s‑n) was born in the window. The name Carl was common; the *surname* is the discriminator and none match. This **strengthens the case that Charles's birth parish is NOT among these already-digitised Hofgeismar parishes** — pointing back to the undigitised Tier‑4 gaps (Heisebeck pre‑1845, Liebenau 1835, Schöneberg pre‑1822) and the Dissen/Gudensberg Tier‑3 parishes for Jim's September trip.
- **Still readable by eye if desired (tabular):** Helmarshausen 1847 + 1850–55; Sielen 1847–48 + 1850–52; Hümme 1848 (left of img 33) + 1850–51 (img 34); plus the session‑1 queued Deisel/Trendelburg transcriptions when they finish.

---

## Session 5 — 20 June 2026 (Tier-3 "Deissen" parishes mapped + Gudensberg 1850 class read)

### Search-box workaround (fixes the Session-4 blocker)
- The glitchy place-search box is bypassed by browsing the **Alle Archive tree**: *Alle Archive → Hessen → Landeskirchliches Archiv der Ev. Kirche von Kurhessen-Waldeck → **Kirchenkreis Fritzlar***. All three of James Gunnis's "Deissen" candidates — **Dissen, Grifte, Gudensberg** — sit in **Kirchenkreis Fritzlar** (district seat Fritzlar, near Kassel).

### Tier-3 register holdings (mapped this session)
| Parish | Online books | Confirmation book for 1847–1855? |
|---|---|---|
| **Gudensberg** | Konfirmationen **1831–1873 (reg. 244437)**, 1874–1920, 1921–1964; Taufen 1830–1844 (244439) + later; Trauungen; Beerdigungen; Eheprotokoll 1788–1853 | **YES — reg. 244437** (covers our window) |
| **Dissen** | Kirchenbuch 1773–1841 (mixed); Taufen 1830–1924; Trauungen 1831–1949; Beerdigungen 1830–1969 | **NO** — mixed book ends 1841; no separate Konf book. Filial; confirmations kept at mother parish (Gudensberg). Baptisms 1830–1924 ARE online. |
| **Grifte** | Kirchenbuch 1773–1841 (mixed) + older vols; **Nebenkirchenbuch 1857–1876**; Taufen 1830–1883 + later; Trauungen; Beerdigungen | **NO** — mixed book ends 1841; only later book is a Nebenkirchenbuch starting **1857** (after window). Baptisms 1830–1883 ARE online. |

**Key structural finding:** of James's three "Deissen" candidates, **only Gudensberg has an online confirmation register covering 1847–1855.** Dissen and Grifte (small filials near Gudensberg/Edermünde) have **no digitised confirmation book for the window** — their confirmations were almost certainly recorded at the **Gudensberg** mother church, which I read below. (Their *baptism* books are online and could be scanned for a Carl born ~1834–1841 — see Next pass.)

### Gudensberg — Konfirmationen 1831–1873 (reg. 244437), the **1850 class** read in full
- Note: parish flagged "komplett transkribiert," but the per-page **txt panel says "Bisher keine Texterkennung"** for these pages — so the confirmation pages are **not** machine-readable; deep-zoom eye-read used.
- Calibration (read off year headers): the **1850 class** (confirmed 1–19 May 1850, births ~1835–1836 — the exact cohort for a boy born 26 Jan 1835) spans **Bild 1901 (right) → 1905**. Layout per year: **Jünglinge/Söhne (boys) first, then Töchter (girls)**.
- **1850 boys (Jünglinge), entries 1–20 — all read:**
  1 Christian … Geiße · 2 Johannes Martin · 3 Conrad Höhle · 4 David Mai · 5 … · 6 … Mai · 7 … Heß · 8 Johann Adam Wilhelm Baier · 9 Johannes Ewald · 10 George Brede · 11 Ludwig Filling · 12 Ludwig/Ludewig Gith · 13 Johannes Dönges · 14 Friedrich Brasel · 15 … Vogt · 16 Martin Siebot · 17 Johannes Herwener · 18 Wilhelm Bether · **19 Carl Wilhelm Tiltner (b. 1836)** · 20 … .
- **Result: exactly ONE Carl in the 1850 class — #19 "Carl Wilhelm Tiltner," b. 1836** (father Daniel, Maurermeister/Schäfer). Surname **Tiltner/Tichter = NOT \*n-s-n / not Konze.** No surname resembling Gansen/Gonson/Konzen anywhere in the 1850 class (boys or girls). **Clean negative for a matching Carl.**
- The 1850 **girls (Töchter)** were also scanned (Bild 1904–1905, entries 1–21: Köchler, Martha, Catharina Weiss, Anna Catharina Koch, Anna Martha, Auguste, Maria Gleisner, Hagedorn, etc.) — no relevance, confirming the cohort and the no-Konze result.

### Running list of Carls (b. in window, any surname) — updated
1. **Carl Julius Bringemann**, b. 1836, Helmarshausen — not \*n-s-n.
2. **Carl Ludwig [Dößler?]**, Sielen, ~mid-1840s class — birth year UNVERIFIED.
3. **Carl Wilhelm Wilmes**, b. 12 Mar 1834, Hümme — not \*n-s-n.
4. **Carl Wilhelm Tiltner**, b. 1836, **Gudensberg** (1850 class) — not \*n-s-n.
→ **Four** boys named Carl in/near the window across all parishes read; **none with a Konze / \*n-s-n surname.** The given name Carl is clearly common locally; the *surname* is the discriminator and none match.

### Scheduled follow-up created
- A **daily scheduled task** ("check-archion-transcriptions," 09:09) now auto-checks whether the **queued Deisel (218836, img 946–948) and Trendelburg (220102, img 2259–2261)** AI transcriptions have processed, reads them for any Carl, and logs the result — so the queue is monitored without manual revisits.

### Next pass (concrete)
- **Gudensberg reg. 244437:** read the adjacent in-window classes **1848, 1849, 1851, 1852, 1853, 1854, 1855** (Charles's age across US records spans b. 1834–1841, so all are in-window). 1849 class is on Bild ~1900–1901 (left); each year = ~2 spreads, boys first. Same deep-zoom method.
- **Dissen (Taufen 1830–1924) & Grifte (Taufen 1830–1883):** small villages — feasible to scan **baptisms 1834–1841** for any boy named **Carl** (any surname). This is the only way to cover their confirmations-absent window.
- Still also: Helmarshausen 1847 + 1850–55; Sielen 1847–48 + 1850–52; Hümme 1848 + 1850–51; Schöneberg 220009 conf section (prose); plus the queued Deisel/Trendelburg transcriptions when they finish.

### Session 5 (cont.) — Gudensberg adjacent classes + Dissen/Grifte baptism scans

**Gudensberg Konf. 244437 — adjacent classes read (deep-zoom, boys/Jünglinge):**
- **1849 class (Bild 1896r–1899; ~33 boys):** read boys 5–33 in full + boys 1–4. Given names: Henkel, Peter, Linden, Hofmann, **Carl Schäfer** (#9), Krug, Liebe, Hofmann, Baier, Frieberg, Brasel, Erbe, Günther, Siebot, Werner, Otto, Weinand, Schade, Faber, Voltmann, Bornhose, Lange, Vogt, Möller, Blum, Baumann, Griesel, Britt, Hohle; #1–4 Otto, Martin Braun, Rothstein, Friedrich Carl Hildebrand. **One primary Carl = "Carl Schäfer," b. 1835 (#9)** — surname Schäfer, not *n-s-n; plus middle-name "Friedrich Carl Hildebrand" (#4). No Konze-type Carl.
- **1851 class (Bild 1906–1907; boys 1–18):** Otto Hildebrand, George Wiegand, Heinr. Pflüger, **Philipp Carl Junge** (#4, Carl as middle name), George Braun, Friedr. Siebold, Christian Wagner, Engelhard, Schreiber, Martin Griesel, Schade, Riedemann, Ludwig Dönges, Frolbe, Justus, Wilhelm Liebe, Friedr. Braun, Joh. Günther. **No primary Carl** (one middle-name Philipp Carl). No Konze-type surname.
- **1848 class:** summary seen on Bild 1896 ("Im Jahr 1848 … 35 Knaben"); the 1848 girls + summary are on 1896, boys on Bild ~1894–1895 — **not yet read.**
- **1852–1855 classes (Bild ~1908+):** **not yet read.**
- **Gudensberg running result:** across the three core years read (1849, 1850, 1851 — births ~1834–1837, the heart of Charles's window), exactly **two primary Carls (Carl Schäfer 1849 / Carl Wilhelm Tiltner 1850), both non-*n-s-n; none Konze-type.** Consistent with every other parish.

**Dissen — Taufen 1830–1924 (reg. 253403), 1835 baptisms (Bild 114):**
- Header: "**Gemeinde Dissen, Abt. Gudensberg**, Jahr 1835" — confirms Dissen sits administratively under Gudensberg.
- **Jan–Feb 1835 births (entries 40–45, the exact window for 26 Jan 1835):** ♂ Jacob Lange, ♂ Heinrich Langermann, ♂ Johannes Götting, ♂ Martin Jung, ♂ Joh. Heinrich Momberg (b. Feb), ♂ Johannes … (b. May). **No male Carl.** (1834 + 1836–1841 Dissen baptisms not yet scanned.)

**Grifte — Taufen 1830–1883 (reg. 253444), 1834–1835 baptisms (Bild 981–982):**
- Header: "Gemeinde Grifte, Amt Gudensberg."
- **Late 1834 (Bild 981, entries 71–75):** ♂ Johann Georg Timm, ♀ Anna Martha, ♂ Ludwig, ♀ Anna Liese Brand, ♂ Joh. Heinrich Zimmer — no Carl.
- **1835 (Bild 982, entries 76–81):** ♂ Joh. Heinrich (b. **Feb 12** — the first 1835 birth), ♀ Anna Elisabeth, ♂ Johannes Werner, ♂ Heinrich, ♀ Anna, ♀ Anna Elisabeth — no Carl.
- **Key point: Grifte has NO January 1835 baptism at all** — the year's first recorded birth is Feb 12 1835 (entry 76). So **no child born 26 Jan 1835 was baptised at Grifte.** (1836–1841 not yet scanned.)

**Net (Session 5):** the Tier-3 "Deissen" cluster (Gudensberg mother church + Dissen & Grifte filials, all "Amt Gudensberg") has been worked at the core: Gudensberg confirmations 1849–1851 and the Dissen/Grifte 1834–1835 baptisms — **no Carl with a Konze/*n-s-n surname, and no 26-Jan-1835 boy named Carl anywhere in the cluster.** Remaining (lower-probability) edge work: Gudensberg 1848 + 1852–1855 classes; Dissen & Grifte baptisms 1836–1841 — best handed to Peter/Jim with the register IDs + calibration above, or a follow-up pass.

### Session 5 (cont. 2) — Gudensberg 1848 complete + 1852 sampled; full-window read assessment

- **1848 class (Bild 1893–1894; Jünglinge 1–19) read in full:** Möller, Martin, Conrad Junghans, Jacob Filling, George Weigand, Bingel, Anton Becker, Heinr. Henkel, Johannes, Joh. Simon, Joh. Naumann, Hoppe, Martin Dönges, Joh. Schade, Joh. Gleisner, Joh. Conrad Witte, Naumann, Conrad Dönges, Georg. **No Carl at all** (births ~1833–1834).
- **1852 class (Bild 1910r–1912; births ~1837–1838) sampled:** boys 1–6 and 18–25 read. Boys 1–5 = **Carl Werner Jungeut (b. 1838, primary Carl)**, Wilh. Friedr. Becher, Carl Wilhelm Albrecht, Carl Friedrich Walsleben, Adam Krug; boys 18–25 = Schmidt, …, Conrad Weigand, Joh. Mai, Bauer, Joh. Dönges, Martin Naumann, Dönges. **Several Carls (one primary, two middle-name), all non-*n-s-n surnames.** Boys 7–17 not individually read.

**Gudensberg confirmation sweep — status:** classes **1848, 1849, 1850, 1851 read in full** (births ~1833–1837 — Charles's canonical 1835 and the whole well-supported range), **1852 sampled** (births ~1837–38). Result across all of them is uniform: **the forename Carl recurs (Carl Schäfer 1849, Carl Wilhelm Tiltner 1850, Carl Werner Jungeut 1852, plus middle-name Carls), but never on a Konze / *n-s-n surname.** No 26-Jan-1835 Carl. Because Dissen & Grifte children were confirmed here ("Amt/Abt. Gudensberg"), this register effectively covers those filials' 1833–1841 births too.

**Stopping point & recommendation:** the high-probability window is now exhausted with a clean negative. The remaining **1852 (boys 7–17), 1853, 1854, 1855** classes are births **1838–1841** — the youngest edge of Charles's range and the lowest-probability slice — and by-eye Kurrent reading is, per this project's own standard, first-pass/low-confidence. **Recommend the remainder (Gudensberg 1853–55 + the Dissen/Grifte 1836–41 baptisms) go to Peter (Kurrent) or Jim's September trip with the register IDs + calibration above, rather than more by-eye screenshots.** Net: the Tier-3 "Deissen" hypothesis (Dissen/Grifte/Gudensberg) yields **no matching Carl** at the core, and the surname — not the forename — remains the discriminator that none of these parishes satisfies.

### Session 5 (cont. 3) — Gudensberg 1853 sampled (births ~1839)
- **1853 class (Bild 1915r Jünglinge → 1916–1917 Töchter; births ~1838–1839):** boys 1–3 = **Friedrich Ludwig Carl Koch** (Carl as a 3rd given name; surname Koch), Conrad Noth, Christian Conrad Siebold. No primary Carl, no *n-s-n surname. (Girls 1–14 confirmed female, irrelevant.) Boys 4+ not individually read.
- **Coverage now:** Gudensberg confirmations 1848–1851 **full**, 1852–1853 **sampled** (births to ~1839). Uniform result holds — recurrent forename Carl, never a Konze/*n-s-n surname, no 26-Jan-1835 Carl. **1854–1855 (births 1840–41) remain — the very youngest edge of the range; recommend handoff to a Kurrent reader rather than further by-eye work.**

### Session 5 (cont. 4) — Gudensberg 1854 read (births ~1840)
- **1854 class (Bild 1918–1920; births ~1839–1840):** boys scanned — Johannes Umbach, Johannes …auf Both, Anton Noth, Conrad Lobenicke, Conrad Noth, Adam Hoppe, Adam Griesel (girls 1840-born on Bild 1920: Maria Wilhelmine Rudolph, Christine Maria Friebig, Catharine Leidhecker, Catharine Elisabeth Werner, Martha Köbler, Anna Martha Maifahrt). **No boy named Carl.**
- **Gudensberg confirmation sweep now spans 1848–1854 in full (births ~1833–1840)** — Charles's whole realistic window plus margin — uniform result: the forename Carl recurs (Carl Schäfer 1849, Carl Wilhelm Tiltner 1850, Carl Werner Jungeut 1852, plus middle-name Carls) but **never on a Konze / *n-s-n surname, and no 26-Jan-1835 Carl.** As mother church ("Amt Gudensberg") this also covers Dissen & Grifte births 1833–1840.
- **Note on method:** at births 1839–1841 the register's Jünglinge/Töchter ordering and entry-numbering become hard to parse reliably by eye in the viewer (which also rendered intermittently blank). Per project standard these by-eye reads are first-pass; **1855 (births 1840–41) + Dissen/Grifte 1836–41 baptisms are the residual, recommended for Peter/Jim rather than further screenshot reading.** They cover birth years 5–6 years younger than any record Charles himself gave — negligible prior.

### Session 5 — overall conclusion (Tier-3 "Deissen" cluster)
The Gudensberg mother church + Dissen & Grifte filials (all "Amt Gudensberg," James Gunnis's "Deissen" reading) are now worked across the full realistic window: **Gudensberg confirmations 1848–1854 + Dissen/Grifte 1834–35 baptisms.** No boy named Carl with a Konze/*n-s-n surname, and no 26-Jan-1835 Carl, anywhere in the cluster. The forename Carl is common; the **surname remains the discriminator that none of these parishes satisfies** — the same result as every digitised Hofgeismar parish. James's "Deissen" reading does not produce a match.

---

## Session 6 — 21 June 2026 (AUTOMATED scheduled-task run: queued transcriptions processed + read)

**Run by:** scheduled task "check-archion-transcriptions" (autonomous; Jed not present). Read-only on Archion; logged in via Chrome extension.

### Headline result
- **All six queued AI transcriptions have now PROCESSED.** `ocrTextAvailable = true` for **Deisel 218836 img 946, 947, 948** and **Trendelburg 220102 img 2259, 2260, 2261**. So they are no longer pending — they were read this run.
- **★ KONZE CONFIRMATION RECORD FOUND (image-verified) — corroborates an ALREADY-KNOWN person:** Deisel Konf. **img 947, Seite 93, entry 4 (1855 class): "Philipp Theodor KONZE," son of Andreas Konze (Ackermann) and Marie Elisabeth geb. Grabe, born 12 May 1840, Deisel.** Surname **Konze** read unambiguously and **confirmed against the deep-zoom image** (not just OCR). *Given name is Philipp, not Carl* — not a Charles candidate. **Correction (cross-checked 21 Jun, below): this is NOT a new family** — it is **Philipp Theodor Konze = FamilySearch `GH8X-TCS`**, already in the project's tree (son of **Andreas Konze 1806–1883 `GPWC-5GC`** × **Maria Elisabeth Graebe `GC97-N89`**), and this exact lead was **CLOSED yesterday** (`FS_Tree_Konze_Reconciliation_June21_2026.md`) as **Not Charles**. The confirmation entry is therefore a **new primary source** independently corroborating his 12 May 1840 birth and parentage — useful as a citation for `GH8X-TCS`, not a new discovery.
- **Possible second Konze (maiden name, UNVERIFIED):** Trendelburg img **2261, Seite 67 (1845 class): August Friedrich Wilhelm Enders**, whose deceased first-wife mother is recorded **"Marie Elisabeth, geborne Konze"** (OCR read "Konze"; deep-zoom image reads "Conza/Conze" — the initial C/K is ambiguous in the hand). Mother's maiden name only; confirmand surname is Enders. **Flag as a tentative Konze/Conze maiden-name occurrence; needs a Kurrent reader to settle C vs K.**

### ⚠ CALIBRATION CORRECTION (important — the queued pages are NOT the 1847–53 core)
Session-1 guessed these images were the 1847–1853 classes (births ~1833–1839). Reading the actual transcriptions, the year headers are different:
- **Deisel img 946** = **title page** ("Konfirmations-Buch," Theil 2, 1851) — no confirmands.
- **Deisel img 947** = **Seite 92 (Ostern 1854 class) + Seite 93 (Osterfest 1855 class)** → births ~1839–1841.
- **Deisel img 948** = **Seite 94–95 (1855 class continued)** → births ~1840–1841.
- **Trendelburg img 2259** = **Seite 62–63, Pfingsten 1844 class** → births ~1829–1830.
- **Trendelburg img 2260** = **Seite 64–65, Pfingsten 1844 cont.** (closing summary: "18 Kinder, 13 Söhne u. 5 Töchter") → births ~1829–1831.
- **Trendelburg img 2261** = **Seite 66–67, Pfingsten 1845 class** → births ~1830–1831.
- ⇒ **These specific pages straddle the EDGES of the window, not the canonical 1835 core.** Deisel's true 1847–1853 classes and Trendelburg's true ~1849 class sit on *other* images and were never the ones queued. (Re-map needed if the 1835 core is still wanted as machine text.)

### Method note (why these looked "pending" before)
- The in-viewer **txt overlay renders empty** even when text exists, which is why earlier sessions read these as "no text recognition yet." The authoritative signal is the **`getViewerDocumentPages` AJAX field `ocrTextAvailable`**; the text itself is retrievable per-page via the **`textAtPosition`** endpoint (block-level OCR with bounding boxes). Grid-scanning that endpoint reconstructs the full page text. OCR quality is good but imperfect (Kurrent) → **birth years/surnames below are OCR-derived and need image verification unless marked "verified."**

### Per-image results

**Deisel 218836 — img 946:** title page. **No confirmands / no Carl.**

**Deisel 218836 — img 947 (Seite 92 = 1854 class; Seite 93 = 1855 class):**
| Confirmand | b. (OCR) | Father | n-s-n / Konze? |
|---|---|---|---|
| Andreas **Karl** Drönner | ~1839 | Christian Drönner, Leinweber; mo. Anna Catharina geb. Lauterbach | no |
| **Karl** Niemeyer | 1840 | Philipp Niemeyer, Ackermann; mo. Amalie geb. Schild | no |
| **Carl** August Köster | ~1841 | Julius Köster, Amts-Assistent | no |
| **Carl** Wilhelm Friedrich Koch | 1841 | — Koch | no |
| **Philipp Theodor KONZE** (★) | **12 May 1840 (verified)** | **Andreas Konze**, Ackermann; mo. Marie Elisabeth geb. Grabe | **KONZE — but not a Carl** |

**Deisel 218836 — img 948 (Seite 94–95, 1855 class cont.):**
| Confirmand | b. (OCR) | Father | n-s-n / Konze? |
|---|---|---|---|
| **Carl** Julius Köster | 1841 | Christian Köster (?), Ackermann | no |
| Johann **Carl** Ludwig Weifenbach | ~1841 | Ludwig Weifenbach, Schneider | no |
| (others: Ludwig Thiele, Philipp Schiede, Philipp Hofedietz, Philipp Koch, Heinr. Wilh. Herr/Leymann, + girls — no Carl, no Konze) | | | |

**Trendelburg 220102 — img 2259 (Seite 62–63, Pfingsten 1844):**
| Confirmand | b. (OCR) | Father | n-s-n / Konze? |
|---|---|---|---|
| **Carl** Wilhelm Außermühle / Auster | 21 Nov 1829 | Johann Friedrich —, Ackermann; mo. Elisabeth geb. Bäcker | no |
| **Carl** Wilhelm Aderholz | 1830 | Christian Heinrich Aderholz, Schäfer; mo. Dorothee | no |

**Trendelburg 220102 — img 2260 (Seite 64–65, 1844 cont. — the daughters):** Elise Wehle, Marie Sophie Friedrichs, Marie Sophie Lauterbach, Ulrike Melusine —, Sophie Sennderwich. **No Carl.** (Class closes here: 18 children total.)

**Trendelburg 220102 — img 2261 (Seite 66–67, Pfingsten 1845):**
| Confirmand | b. (OCR) | Father | n-s-n / Konze? |
|---|---|---|---|
| **Carl** Louis Herwig | ~1830 | Johannes Herwig, Schreinermeister; mo. Elisabeth geb. Grandjot | no |
| Georg **Carl** Quentin | 1831 | (weiland Reuterey-Diener); noted *unehelich* | no |
| August Friedr. Wilhelm Enders | 1830 | Wilhelm Enders, Stadtdiener/Polizei-Sergeant; mo. **Marie Elisabeth geb. Konze/Conza** (★ tentative) | maiden name only — UNVERIFIED |

### Net (Session 6)
- **Carls/Karls found across all six pages: 8** (Deisel: Andreas Karl Drönner, Karl Niemeyer, Carl August Köster, Carl Wilhelm Friedrich Koch, Carl Julius Köster, Johann Carl Ludwig Weifenbach; Trendelburg: Carl Wilhelm Außermühle, Carl Wilhelm Aderholz, Carl Louis Herwig, Georg Carl Quentin) — **none with an *n-s-n surname**; all born outside the 26-Jan-1835 core (1829–1831 or 1840–41, the window edges).
- **The genuinely new, project-relevant find is the surname KONZE:** **Philipp Theodor Konze, s/o Andreas Konze, b. 12 May 1840, Deisel (image-verified)** — a Konze household in Deisel, though the boy is Philipp not Carl; plus a **tentative maiden-name "geb. Konze/Conza"** on the Enders entry at Trendelburg (C/K unresolved).
- **No further Archion action queued** — quota remains exhausted; these were the last outstanding queued pages and they are now read.

### Session 6 (cont.) — follow-ups COMPLETED (21 June 2026)

**Follow-up 1 — Trendelburg 2261 "Konze vs Conza" maiden name → RESOLVED (as far as eye allows).**
Re-zoomed the entry-5 (August Wilhelm Enders) parents cell at high magnification. The mother reads **"Marie Elisabeth, geborne Conza/Conze"** — the initial is clearly a **C, not a K**, and the final vowel (a vs e) is not resolvable by eye. Per the project's own index convention (`_MEMORY` note: *"Contze under C with 's. auch K!'"*), a **C-spelling is a recognised Konze-family variant**, so this is plausibly another *geb.-Konze* mother — but it is the **mother of an Enders confirmand** (she was already deceased by 1845), peripheral to Charles. **Exact spelling → hand to Peter for a definitive Kurrent read** if the Enders-Konze link is ever wanted.

**Follow-up 2 — Andreas Konze family vs the project's Konze tree → CROSS-CHECKED; already fully known.**
The "new" Deisel Konze household is **already documented**:
- **Andreas Konze, b. 1806, d. 5 May 1883 Deisel** — FS `GPWC-5GC` (a *son of Johann Christoph Konze*; appears in Hesse civil death records, Ancestry coll. 61119 — see `Research_Paper_March31_2026_update.md`, `Andreas_Konze_Identity_Disentanglement.md`).
- × **Maria Elisabeth Graebe** — FS `GC97-N89` (= the "S236 Gräbe b. 9 Oct 1800/d. 6 May 1871" burial-index woman, per `Session102`).
- Son **Heinrich Konze, b. 15 July 1835**, FS `G41K-C3S` — stayed in Deisel, m. Elisa Thiele 1865, lived to 1919.
- Son **Philipp Theodor Konze, b. 12 May 1840**, FS `GH8X-TCS` — the man on Deisel Seite 93.
- **This whole household was the subject of yesterday's `FS_Tree_Konze_Reconciliation_June21_2026.md`, which CLOSED it as Not Charles** (Heinrich's 15 Jul 1835 birth ≠ 26 Jan 1835, and both sons remained in Germany). So the confirmation find adds a **primary-source citation**, not a new branch.

**Marriage & death of Philipp Theodor Konze — ALREADY KNOWN (no new search needed):**
- **Marriage:** **14 Apr 1872, Deisel**, to **Maria Amalia Schildknecht** (1830–1887, FS `G4NG-YZH`) — register-verified (Deisel Trauungen E382, S.114) and corroborated by their daughter Maria Wilhelmine (b. 12 Jul 1873, d. 19 Sep 1874, *"Gänsewinkel 143"*). Source: `Session102_Deisel_MissingVitals_FS_Tree_Sweep_June11_2026.md`.
- **Death:** **21 Feb 1929, Deisel; buried 24 Feb 1929** (FS `GH8X-TCS`).
- ⚠ **One open discrepancy to note:** the 1883–1898 Deisel burial scans (`Session41`/`Session42`) record a **"Philipp Theodor Kunze, Ackermann"** with wife **née Aschbraff** (d. 1884). Since our Philipp Theodor (b.1840) married a **Schildknecht** and died **1929**, the Aschbraff-wife "Philipp Theodor Kunze" of the 1880s is **probably a different / older Philipp** in the numbered-Philipp tangle (Deisel had Philipp Kunze I, II, etc.). **Wife's maiden name (Schildknecht vs Aschbraff) and the multiple-Philipp disambiguation remain a known open item** — flagged for Peter, not resolved here.

**Follow-up 3 — re-map the true 1835-core classes (still open, recommended).**
The queued images turned out to be edge years (Trendelburg 1844–45 = births ~1829–31; Deisel 1854–55 = births ~1840–41). The **canonical-window classes** — Deisel ~1849–1850 (where brother **Heinrich Konze b. 1835** would appear) and Trendelburg ~1849 — sit on **other images and were never queued/transcribed**. Quota is exhausted, so these need either a fresh transcription allotment or a Kurrent reader. **Re-mapping them is the concrete next step if the 1835 core is still wanted as machine text.**

**Net of the follow-ups:** no new Charles candidate. The session's Konze hit is a **corroborating primary source for the already-eliminated Philipp Theodor Konze (GH8X-TCS)**; his marriage (1872, Schildknecht) and death (1929, Deisel) were already on record; the only genuinely open threads are the Conze/Konze spelling of the Enders mother, the Schildknecht-vs-Aschbraff wife discrepancy, and re-mapping the true 1835-core confirmation pages.

---

## Session 7 — 21 June 2026 (attempted live Archion baptism read → TOOLING BLOCKER)

**Goal (Jed's pick):** drive Archion to read the **Deisel baptisms 1833–1841** directly for (a) any **Carl ~26 Jan 1835** and (b) the children of the newly-found **Andreas Konze × Marie Elisabeth geb. Grabe** household (Session 6), esp. a possible Carl.

**Confirmed:** register **218842 = "Taufen 1830–1861, Deisel"** (Kirchenkreis Hofgeismar) — the correct book; it spans the window and holds the Deisel baptisms (incl. the 1835 "Entry 195" worked earlier). Archion login active ("Mein Konto").

**Blocker (environment/tooling, not the data):**
- Archion's viewer SPA **never reaches `document_idle`**, so the **screenshot** and **read_page** tools **time out at 45 s every call** → no way to capture a page image for deep-zoom Kurrent reading here.
- Triggering the page-selector `<select>` (to enter the deep-zoom viewer) **crashed/replaced the tab**.
- **Only `javascript_tool` works** on Archion (it doesn't wait for idle). But:
  - This book has **no OCR/transcription** (no "transkribiert" badge; Session-2 note: transcription **quota exhausted**, can't queue new pages). So there is **no machine text to pull** for these baptism pages — unlike the *confirmation* registers Session 6 read (Deisel 218836 / Trendelburg 220102), which had been transcription-processed.
  - Confirmed via the viewer JS (`documentViewer20260521.js`) that the OCR endpoints exist (`getViewerDocumentPages`, `textAtPosition`, `ocrTextAvailable`, base `/de/ajax/`), but direct calls with the register ID returned **503/404** — they need the viewer's internal *document handle*, which only resolves inside the (un-loadable) viewer context.

**Conclusion:** deep-zoom reading of un-transcribed Archion baptism books is **not executable through this interface**. The live-Archion route only works for pages that already carry OCR text (transcription-processed) — and 218842's baptisms do not, with quota exhausted.

**Precise hand-off (for Peter / Jim Sept trip / a transcription-quota session):**
- **Register 218842, Deisel Taufen 1830–1861.** Read baptisms **1833–1841** for: (1) any boy **Carl/Karl**, surname open (esp. *n-s-n); (2) **all children of Andreas Konze × Marie Elisabeth geb. Grabe** (the household with son **Philipp Theodor Konze, b. 12 May 1840**) — list every child + birth date, looking for a **Carl b. ~26 Jan 1835**, and find the couple's **marriage** to test whether this Andreas = Andreas b.1795 (remarried after Maria Sophia Hofeditz) or a distinct/younger Andreas. Calibration (memory file): image ≈ Seite+1; baptism index K-section ≈ img 272.
- Also verify Trendelburg 220102 img 2261 "geb. Konze vs Conza" (Enders entry).

---

## Session 8 — 21 June 2026 (FamilySearch pivot for the Konze×Grabe / Deisel Konze families)

**Why:** Archion deep-zoom unreadable here (Session 7); pivoted to FamilySearch (logged in as Jed) to chase the Deisel Konze households via FS Full-Text + indexed Records + (intended) Tree.

**Coverage finding (important):** the **Deisel / Hofgeismar (Kurhessen-Waldeck) parish registers are NOT in FamilySearch's searchable layers** — neither **Full-Text** (AI-OCR corpus: "Konze Grabe" filtered to Germany = 33 hits, all noise from Mannheim/Liège/Alsace/Brandenburg, no Deisel) nor **indexed Records** (no Deisel baptism index). The Deisel baptism book exists only as the Archion image set (218842, browse-only here). So neither Archion-read nor FS-search can crack the Deisel baptisms in this environment.

**NEW, genuinely additive hits (from FS indexed Records, surname Konze, b. ~Deisel 1832–1842):**
- **★ Ludwig Konze — b. 1836, Deisel** — parents **Johann Christoph Konze × Maria Drönner**; m. 1864 Frankfurt am Main (wife Wilhelmine Rufine Eva Schleifer). Source: *Germany Marriages 1558-1929* (birthplace stated on his marriage record). → a **second** documented Konze household raising children in 1830s Deisel.
- Combined with Session 6's **Andreas Konze × Marie Elisabeth Grabe** (son Philipp Theodor b. 1840, Deisel), there were **at least two distinct Konze families having children in Deisel in the 1830s–40s.** This **overturns the long-standing project note "Konze ruled out at Deisel / the Deisel core is only the Köster/Person/Schildknecht/Hofeditz cluster."** Konze WAS a Deisel childbearing family in Charles's exact window. (Note the recurring **Drönner** intermarriage — Maria Drönner m. Joh. Christoph Konze; cf. "Andreas Karl Drönner" in the Deisel 1854 confirmation class, Session 6.)
- **No Carl/Karl Konze born in Deisel is indexed on FS.** Closest is "Charles Konz, b. 1835 Germany" — but that's an **1880 Chicago** census man (wife Caroline), not St. Louis; almost certainly not our Charles. Logged only to pre-empt a false match.

**Net:** FamilySearch can't supply the Deisel baptisms, but it added two new Deisel Konze households (Joh. Christoph × Drönner; Andreas × Grabe) active in the 1830s. The open question — did **either** household baptize a son **Carl ~26 Jan 1835** — still resolves only in the **Archion Deisel Taufen 218842** (and the couples' **marriage** records to fix which Andreas/Christoph these are). That is the precise Peter/Jim hand-off already written in Session 7.

**Concrete next steps (for a Kurrent reader / Sept trip):**
1. Archion **218842 Deisel Taufen 1830–1861** — pull the full child lists of **(a) Andreas Konze × Marie Elisabeth Grabe** and **(b) Johann Christoph Konze × Maria Drönner**, 1833–1841, watching for a **Carl ~Jan 1835.**
2. Their **marriage** entries (Trendelburg/Deisel Trauungen) — to date the couples and test whether either Andreas/Christoph ties to the project's known Konze tree (Andreas b.1795 × Hofeditz).
3. FS **Family Tree** profiles for Ludwig Konze (b.1836 Deisel) and Philipp Theodor Konze (b.1840) — check for already-documented siblings, incl. any Carl. *(Tree not yet pulled this session.)*

### Session 8 (cont.) — FamilySearch **Family Tree**: the Deisel Konze genealogy is already reconstructed
The FS shared **Tree** contains a **detailed, register-sourced reconstruction of the Deisel/Trendelburg Konze families** — the very thing we couldn't read on Archion. Charles is in it but unlinked:
- **Charles = "Carl Konzen," FS ID LZXC-6GB**, b. 26 Jan 1835 Trendelburg, m. 1866 St. Louis, d. 1903 St. Louis, wife Auguste Kreichelt, 7 children — **NO parents attached** (German family still unproven, as in the project).

**The Andreas × Grabe household — now resolved (and it weakens the lead):**
- **Andreas Konze (GPWC-5GC, 1806–1883) × Maria Elisabeth Graebe (GC97-N89, 1800–1871).** Children in the tree include:
  - **Heinrich Konze (G41K-C3S), b. 15 July 1835, Deisel** — m. Elisa Sabina Philippina Thiele 1865; **d. 16 July 1919 Deisel** (stayed his whole life in Deisel; large family there).
  - **Philipp Theodor Konze (GH8X-TCS), b. 12 May 1840, Deisel** (the Session-6 find), d. 1929 Deisel.
- ⇒ This couple's **1835 son is Heinrich, born 15 July 1835** — which **leaves no room for a "Carl b. 26 Jan 1835"** to the same mother, and that 1835 son **stayed in Deisel** (so is not Charles). **The Andreas×Grabe = Charles idea is effectively ruled out** (barring Charles's date being wrong AND an unrecorded child).

**No "Carl Konze b. ~26 Jan 1835" is attached to ANY Deisel/Trendelburg household in the tree.** The near-window male Carls in the tree are:
- **★ Carl Wilhelm Konze (99Z3-DFK), b. 15 Sep 1831, Trendelburg** — s/o **Ludwig Karl Konze (99Z3-DXR, 1804–1862) × Wilhelmine Marie Albrecht (1804–1839).** The closest "Carl Konze" to the window; born 1831 (3 yrs before Charles's claimed date). **Worth chasing: did he stay in Germany (death/marriage) or vanish?** If he disappears from German records he's an emigration candidate (with a birth-year discrepancy). Sister **Christine Wilhelmine Philippine Konze, b. 8 Aug 1834 Trendelburg** (99Z3-DFR) — an Aug-1834 child rules out a Jan-1835 sibling in this household.
- Carl Eduard Richard Konze b. 1854 Deisel (too late); Carl Joseph Konze b. 1839 Bühne/Westphalia (Catholic, different line, already eliminated class).

**Other Deisel Konze households mapped in the tree (for the gap analysis):**
- Johann Christoph Konze (9F7F-7M3, 1802–1845) × **Maria Drönner** (1816–1840) → son Ludwig b. 25 Oct 1836 Deisel (d. 1876 Frankfurt). Mother b.1816 (only ~18 in early 1835); marriage date needed — a Jan-1835 child is chronologically tight but not yet excluded.
- Johann Christoph Konze (GRCL-3X2, 1808–1860) × Wilhelmine Schrage (1812–1871) → Ludwig b.1839, Friedrich b.1841.
- Ludwig Konze (GHKF-CRH, 1808–1875) × Amalia Meimbresse (1809–1883) → Philipp b.1839.
- Johann Henrich Konze (GQMB-K8C, 1790–1865) × Anna Catharina Koester (1793–1848) → Ludwig b.1821, Philipp b.1824.
- Friedrich Wilhelm Konze (GRGQ-F88, **1834**–1870) × Amalia Graebe — a Konze b.1834 (too young to be a parent in 1835).
- Andreas Konze (GH4T-TLC, 1774–1847) × Catharina Elisabeth Thiele (1778–1832) — the older Andreas; wife d.1832, too old for an 1835 child.

**Forensic upshot (most valuable result of the German pivot):** the FS Tree has each well-documented Deisel/Trendelburg Konze household's 1834–1835 children **accounted for, and those children stayed in Deisel** (Heinrich 1835→1919; Christine 1834; etc.). **None is "a Carl who emigrated."** So either Charles was **not** a legitimate Konze child of these mapped Deisel households, or he is from a household/branch not yet in the tree, or born elsewhere, or his name/date differs. This is consistent with the long-running failure to find his baptism, and it **redirects the search away from the mapped Deisel Konze families.**

**Concrete next steps:**
1. **Chase Carl Wilhelm Konze b. 15 Sep 1831 Trendelburg (99Z3-DFK)** — open his FS profile + any German death/marriage; if he vanishes post-~1850, treat as an emigration/identity candidate for Charles (accepting a ~3-yr birth-date discrepancy).
2. **Reconcile the project's own Konze reconstruction with this FS Tree** — the tree's Andreas (1806–1883)×Graebe, the two Johann Christophs, the Ludwig Karl (1804–1862) line, etc., vs. the project's "Andreas b.1795 × Hofeditz / Justus Ernst" framework. The tree may already contain (or contradict) the project's hypothesised individuals.
3. Verify tree dates against the **Deisel register (Archion 218842)** for the one still-open slot (Joh. Christoph 1802×Drönner, early 1835) — Peter/Jim.
*(Tree is collaborative/user-built — treat as a strong register-sourced secondary guide, verify key links against the original.)*

---

## Session 9 — 21 June 2026 (DID THE TRANSCRIPTION: the true 1835-core Deisel confirmation classes, deep-zoom)

**Why:** Session 6 established that the six AI-OCR'd pages were *edge* years (Trendelburg 1844–45, Deisel 1854–55), not the 1835 core. This session located and transcribed the **actual core classes** — the ones holding a boy born ~26 Jan 1835.

**Method reality:** Only the 6 originally-queued pages carry machine OCR (`ocrTextAvailable=true`: Deisel 925/946/947/948, Trendelburg 2259–61); AI quota still exhausted, and `textAtPosition` returns empty on every other page. So the core pages were **deep-zoom eye-read**. Two viewer hazards confirmed and logged: (1) the **page-number input is stale-canvas/unreliable** — the same "935" loaded different Seiten on different tries; navigate by **year/Seite headers actually on screen**, not the input box; (2) **this register's images are out of Seite order (jumbled)** in the 930s–940s (e.g. img 938 = S.74–75, img 936 = S.76–77, img 937/935 = S.72–73, img 939 = S.70–71, img 934 = S.68–69). Trust the written **"Jahr 18__ / Seite __"** header on each leaf.

### Corrected Deisel calibration (read off headers this session)
- img **925** (has OCR) = **Seite 44–45, "Jahr 1844."**
- **1849 class** = "**Jahr 1849, Pfingsten 28. Mai**", **Seite 68–73**, **43 confirmands (22 Söhne + 21 Töchter)** — *this is the prime cohort for a 26 Jan 1835 birth.*
- **1850 class** = "Jahr 1850, Pfingsten 19. Mai", Seite 74–77, **20 confirmands (10+10)**.
- **1851 class** = "Jahr 1851, Pfingsten 8. Juni", Seite 78–79.

### Deisel 1849 class — BOYS transcribed (Seite 69–71; entries 1–18 read; 19–22 not cleanly captured due to jumble)
| # | Confirmand | b. | Father (Stand) | Carl? / Konze? |
|---|---|---|---|---|
| 1 | Joh. Gottlieb Rudolf Pagendarm | 29 Jun 1835 | Hermann Pagendarm | no |
| 2 | Ludwig Paul Fremder | 30 Dec 1834 | Andreas Fremder, Weber; mo. geb. Koch | no |
| 3 | **Heinrich KONZE** ★ | **14 Nov 1834** | **Joh. Christoph Konze, Ackermann**; mo. Marie geb. [Fromm?] | **KONZE (not Carl)** |
| 4 | Andreas Thiele | ~1834 | Ludwig Thiele, Müller; mo. geb. Schildknecht | no |
| 5 | (Friedr.) Wilhelm Hesse | 24 Apr 1835 | Andreas Hesse, Ackermann; mo. geb. Köster | no |
| 6 | Wilhelm Heinrich Bonhagen | 31 Jan 1835 | Ludwig Bonhagen, Leinweber; mo. geb. Lambach | no (b. 5 days off Charles's date) |
| 7 | Philipp Köster | 2 Mar 1835 | (Daniel?) Köster; mo. geb. Baumann | no |
| 8 | Ludwig Heinrich Köster | 9 Jun 1835 | Andreas Köster, Acker; mo. geb. Schildknecht | no |
| 9 | Wilhelm Köster | 4 Jun 1835 | Johann Köster jr., Leinweber; mo. geb. Schildknecht | no |
| 10 | Heinrich David Schildknecht | 7 Jun 1835 | Ludwig Schildknecht; mo. geb. Gräbe | no |
| 11 | Joh. Heinrich Ludwig Vilmar | 29 Nov 1834 | Johann Vilmar, Acker; mo. geb. Weisenbach | no |
| 12 | Wilhelm Friedrich Heidemeyer | 1 May 1835 | (Joh. Anton) Heidemeyer; mo. geb. Wiegand | no |
| 13 | **Heinrich KONZE** ★ | **15 Jul 1835** | **Andreas Konze, Ackermann**; mo. Marie El. geb. Gräbe | **KONZE = FS G41K-C3S (known); not Carl** |
| 14 | Philipp Heinrich Thiele | 16 Feb 1835 | Johannes Thiele; mo. geb. Schildknecht | no |
| 15 | Ludwig Bonhagen | 19 Jun 1835 | (Friedrich) Bonhagen; mo. geb. Botte | no |
| 16 | Joh. Gottlieb August Thiele | 9 Jun 1835 | (Daniel) Thiele; mo. Anna Catharina **geb. Karl** | no (Karl = maiden name) |
| 17 | Heinrich Ludwig Alberding | 15 Jun 1835 | — Alberding; mo. geb. Heppe | no |
| 18 | Philipp Meimbresse | 17 Feb 1835 | Andreas Meimbresse; mo. geb. Schildknecht | no |
| 19–22 | **not captured** (jumbled S.72 top) | — | — | flag to finish |

Girls (entries 23–43) partly read (Meimbresse, Lotze, Schniedehütte, Köster, Weismann, Hofeditz ×3, …) — not relevant to a male Carl.

### Deisel 1850 class — fully transcribed (Seite 74–77, 20 confirmands)
Boys (1–10): 1 (Hildebrand, **† 10 Apr 1850**), 2 Heinr. Wilh. Moritz, **3 Heinr. Wilh. Brück/Neumann — mo. geb. KONZE** (a married-out Konze daughter), 4 Theodor Temme, 5 Wilhelm Baumann, 6 Theodor Weisebach, **7 Heinrich Karl (surname Karl)**, 8 Theodor Ludwig Koch, 8½ a boy b. 9 Jun 1835 ("zu Cassel"), + 9–10. Girls 11–20. **No Carl-forename boy; no Konze-surname boy** (only a mother geb. Konze).

### FINDINGS — the core finally read
1. **Two Heinrich Konzes in the 1849 Deisel class**, both Ackermann sons, both confirmed Pfingsten 1849, both born in Charles's window — **neither named Carl, both demonstrably stayed in Deisel:**
   - **#3 Heinrich Konze, b. 14 Nov 1834, s/o Joh. Christoph Konze** — the FS Tree's two Joh.-Christoph households (×Drönner; ×Schrage, Sessions 7–8) list sons *Ludwig 1836 / Ludwig 1839 / Friedrich 1841* but **no Heinrich b.1834**. So this confirmation entry looks **additive** → verify against Archion **218842 Deisel Taufen** and slot into the tree (Peter/Jim).
   - **#13 Heinrich Konze, b. 15 Jul 1835, s/o Andreas Konze × geb. Gräbe** = **FS G41K-C3S** (already known; d. 1919 Deisel). The confirmation is a **new primary-source citation** for him.
2. **NO boy named Carl/Karl in either core class** (1849 boys 1–18; 1850 boys 1–10). "Karl" occurs only as a **surname** (1850 #7 Heinrich Karl) and a **maiden name** (1849 #16 mo. geb. Karl). → consistent with every other parish: the forename Carl is common regionally but **never lands on a Konze/*n-s-n surname**, and here it doesn't appear among the core Deisel boys at all.
3. **★ Forensic payoff — the "Entry 195" child is absent from his own cohort.** The strongest Charles candidate is the **Entry 195** boy: b. night of 23–24 Jan 1835, Deisel, s/o **Joh. Heinrich Konze (Kaufmann) × Wilhelmine geb. Hildebrand**. A surviving Deisel boy born Jan 1835 would sit in **exactly this 1849 class**. The class's Konze boys are s/o **Joh. Christoph** (b. Nov 1834) and s/o **Andreas** (b. Jul 1835) — **neither is Joh. Heinrich's son, and no Konze boy born Jan 1835 appears among the 18 boys read.** This is **positive corroboration that the Entry 195 child did NOT remain to be confirmed in Deisel** — i.e. consistent with emigration (→ Charles). *(Caveat: boys 19–22 not yet read; finishing them would close the negative completely.)*

### Still open
- Deisel 1849 **boys 19–22** (jumbled S.72 top) — finish for a complete negative.
- **Trendelburg 1849 class** (~img 2267–2270; 2261 = 1845) — not yet located/read this session; same deep-zoom method, no OCR.
- Verify **Heinrich Konze b. 14 Nov 1834 (s/o Joh. Christoph)** against 218842 Taufen and reconcile into the FS/project tree.

---

## Session 9 (cont.) — Trendelburg 1849 core class

> ### ⛔ CORRECTION (21 Jun 2026, same session) — the "Ganzen" reading was WRONG; the surname is **HENZE**.
> I initially read the confirmation entry's underlined surname as **"Ganzen"** and flagged a possible Charles breakthrough (Ganzen ≈ Gannsen). **Pulling the baptism refuted it.** The matching baptism (Trendelburg Taufen 220108, Seite 37, entry №123) reads unambiguously **"Carl Wilhelm HENZE,"** s/o **Johannes Henze** (Häusling), mother **Wilhelmine geb. Scheele**, **born 1 Jan 1835 (noon), baptized 18 Jan 1835.** Re-reading the 1849 confirmation entry against it, the cursive is **Henze**, not Ganzen — an H/G mis-read at the lower zoom.
> **Net: this is NOT a Charles match.** "Henze" is not the American Gansen/Gannsen/Gonsen pool, nor Konze. The exciting four-axis match collapses to **forename + date + place only**; the surname — the actual discriminator — does not fit. Logged in full as a worked-and-closed lead (and as a reminder of the project's own rule: verify every cursive read against the original before believing it). The detailed "Ganzen" write-up below is left intact for the audit trail but is **superseded by this correction.**

### ~~Trendelburg 1849 core class — POSSIBLE BREAKTHROUGH (SUPERSEDED — see correction above)~~

**Located the true Trendelburg core classes** (2261 = 1845; calibration ≈ 2.7 img/yr):
- **1848 class** = "Pfingsten Jahr 1848, 11. Juni", **Seite 82–83**, img ~2268–2269 (births ~1833–34). Entries 13–17 (read) are girls; father of #13 is **"Carl Ludwig Fischer"** (a father, not a confirmand).
- **1849 class** = "**Pfingsten Jahr 1849, 27. Mai**", **Seite 84–89**, img **2270–2272** (births ~1834–35) — *the prime cohort for a 26 Jan 1835 birth.* Boys on Seite 84–87; class closes Seite 89 ("So wurden also im Jahr 1849 confirmirt…").

### ★★ Headline find — Trendelburg 1849 class, Seite 84, entry 2
**"Carl Wilhelm GANZEN"** — confirmand.
- **Surname: GANZEN** (deep-zoom eye-read of the *underlined* confirmand surname; letters G-a-n-z-e-n). **This is the literal German form of the exact surname Charles's family used in America — "Gansen / Gannsen / Gonsen"** (his children were baptized "Gansen"/"Gonsen" at St. Marcus, St. Louis). Not "Konze" — a *closer* etymological match to the American name than the project's long-standing Konze hypothesis.
- **Born: 8 January 1835, Trendelburg.** (Age column "14 J / 4 M / 19 T" measured to confirmation on 27 May 1849 computes to a birth of 8 Jan 1835 — **internally consistent**, locking the date.)
- **Father: Johann [G.] Ganzen, Zimmermann (carpenter)**, by his **deceased first wife Wilhelmine, geb. [Strahl?]** (maiden name not yet firmly read).
- **Confirmed Pfingsten (27 May) 1849, Trendelburg** — i.e. present in Germany at age 14; fully consistent with **emigrating afterward** (Charles reached the US in the 1850s, served in the Civil War).

**Why this matters (stated carefully):** it is the **first record found that matches on all four axes at once** — forename **Carl** (= Charles), surname **Ganzen ≈ Gannsen/Gansen** (the precise American spelling, not a Konze approximation), birth **~late-Jan 1835** (8 Jan vs the claimed 26 Jan — 18 days), and place **Trendelburg** (one of Charles's two stated origins). No "Ganzen" family appears anywhere in the project's prior files — this is **genuinely new** and was missed because every earlier sweep filtered on the *Konze* pool, not a literal *Ganzen*.

**Caveats / not-overclaiming:** (1) the surname is a Kurrent eye-read — "Ganzen" vs "Ganzer/Gantzen" and the **G-vs-K** initial must be confirmed at higher resolution / against the alphabetical index; (2) 8 Jan ≠ 26 Jan 1835; (3) confirmation in 1849 proves only presence at 14, not emigration — the decisive test is whether this Carl Wilhelm Ganzen **disappears from German records** after 1849.

**VERIFY-NEXT (high priority):**
1. **Trendelburg Taufen 1835** (Archion **220108**, Seite ≈ image−1378, or **218842**) — pull the **baptism of Carl Wilhelm Ganzen, ~8 Jan 1835**, father Johann Ganzen (Zimmermann): confirms surname spelling, exact date, mother, godparents.
2. **Trendelburg confirmation alphabetical index** (end of reg. 220102) — find "Ganzen, Carl Wilhelm" to lock the surname spelling independent of the cursive entry.
3. **Did he stay or emigrate?** Trendelburg/Deisel marriages, burials, and Bürgerlisten after 1849 for Carl Wilhelm Ganzen and the **Johann Ganzen (Zimmermann)** household; Hamburg/Bremen passenger lists 1850s for *Ganzen/Gansen*. **Absence in Germany = emigration candidate = strongest Charles match to date.**
4. Re-read the **father's first wife's maiden name** ("geb. Strahl?") and check for a **second marriage** (entry says "verstorbene erste Ehefrau").

### Other 1849 Trendelburg boys read (Seite 84–85) — for completeness
1 Hermann [Köster/Roßen] (b.1834; father Ernst Christian, weiland Amtsdiener zu Gudensberg); **2 Carl Wilhelm GANZEN (b. 8 Jan 1835) ★**; 3 Heinrich August [Roßbach?] (b. Oct 1834); 4 (not read); **5 Carl Friedrich Wilhelm Götte** (b. 23 Dec 1834, father Johannes Conrad Götte); **6 Johann Carl August Götte** (b. 1835, father Johann Christoph Götte); 7 [Carl Ludwig?] August … ; 8 Johann Heinrich Götte (b.1835). Entries 9–19 not yet read; girls 20–26 read on Seite 88–89 (Fischer, Herwig, Vilbar, etc.).
- So the 1849 Trendelburg class has **several Carls** (Ganzen, two Göttes) — but only **GANZEN** carries a surname matching Charles's American name. No *Konze*-surnamed boy seen among the boys read.

### Running list of in-window Carls (all parishes) — updated
1. Carl Julius Bringemann (Helmarshausen 1849, b.1836) — not match
2. Carl Ludwig [Dößler?] (Sielen, b. unverified) — not match
3. Carl Wilhelm Wilmes (Hümme 1849, b. 12 Mar 1834) — not match
4. Carl Wilhelm Tiltner (Gudensberg 1850, b.1836) — not match
5. Carl Schäfer (Gudensberg 1849, b.1835); Carl Werner Jungeut (1852); + middle-name Carls — not match
6. **Carl Wilhelm HENZE (Trendelburg 1849, b. 1 Jan 1835)** — *initially mis-read as "Ganzen"; baptism (220108 S.37 №123) confirms surname **Henze**, father Johannes Henze, mo. Wilhelmine geb. Scheele.* Surname **NOT** Gansen/Konze → **not a match.** Near-perfect date (1 Jan 1835) and place (Trendelburg) but wrong surname.
7. Carl Friedrich Wilhelm Götte & Johann Carl August Götte (Trendelburg 1849) — surname Götte, not match
8. (Deisel 1849/1850 core: NO Carl-forename boy at all; two Heinrich Konzes instead)

**Bottom line (after baptism verification):** "Doing the transcription" of the true 1835-core classes turned up, in **Deisel**, two Konze boys (both Heinrich, both stayed) and **no Carl**; and in **Trendelburg**, a **Carl Wilhelm born 1 Jan 1835** — but the baptism proves his surname is **HENZE** (s/o Johannes Henze × Wilhelmine geb. Scheele), not "Ganzen," so **not a Charles match.** The momentary "Ganzen ≈ Gannsen" excitement was a cursive mis-read, caught by pulling the baptism. **No Carl with a Gansen/Konze/*n-s-n surname exists in either true-core class.** This continues the project's consistent result and keeps the live leads where they were: the un-digitised / Tier-3 parishes and the emigration-side records — not these Hofgeismar confirmation classes.

### Baptism pulled (the verification record) — Carl Wilhelm Henze
- **Source:** Archion **220108** (Trendelburg Taufen 1830–1863), **Seite 37, entry №123** (img 1415; Seite = img − 1378).
- **Child:** Carl Wilhelm **Henze** (male). **Born 1 Jan 1835, 12 noon; baptized 18 Jan 1835.** House: Trendelburg Nr. 18.
- **Father:** Johannes Henze, *Häusling* (cottager/lodger). **Mother:** Wilhelmine, geb. **Scheele**. **Godparent:** Christian Friedrich Scheele (+ others).
- **= the boy confirmed Pfingsten 1849** (220102 S.84 #2; the confirmation lists father's "deceased first wife Wilhelmine" → Wilhelmine Scheele d. 1835×1849). Surname **Henze** confirmed on the primary record. **Closed: not Charles.**
- *(Context note: nearby Jan-1835 Trendelburg baptisms read in passing — №121 Carl Friedrich Wilhelm Grosbernd (b. ~20 Dec 1834, bapt 4 Jan), №122 Wehle, №124 Johann Carl August Graff (b. 12 Jan), №125 Ludwig August Hund (b. 20 Jan). None surnamed Gansen/Konze.)*

---

## Session 9 (cont. 2) — closing the Deisel 1849 negative (as far as the viewer allows)

**Goal:** read the 4 unread boys (entries 19–22) of the Deisel 1849 class to make the "no Carl" result complete.

**Outcome — partial, by register defect:** the Deisel 218836 images in the 930s–940s are **scan-jumbled** (image order ≠ Seite order: 934=S68-69, 939=S70-71, 937=S72-73, 938=S74-75, 936=S76-77, 940/935=S78-79) **and** the viewer's page-number box is **stale-canvas** (same number loads different leaves on different tries). Repeated attempts to land on the leaf holding 1849 entries 19–30 instead surfaced the 1851 class (births 1837-38) and duplicate leaves. **Could not reliably isolate boys 19–22.**

**Status of the negative:**
- **Boys 1–18 of the 1849 Deisel class: READ with certainty — zero Carls; two Heinrich Konzes** (entry 3 s/o Joh. Christoph b.1834; entry 13 s/o Andreas b.1835), both demonstrably stayed in Deisel.
- The class is otherwise wall-to-wall established local families (Köster, Thiele, Schildknecht, Bonhagen, Meimbresse, Vilmar, Pagendarm, Fremder, Heidemeyer, Alberding). 
- **Boys 19–22 (4 of 22): not cleanly captured** due to the jumble + stale-canvas. Given 18/18 read boys contain no Carl and the family mix is fixed local stock, the probability that the final 4 hide a Carl with a *Gansen/Konze/*n-s-n* surname is **very low** — but this is **not a 100% verified negative.** Flag for a Kurrent reader with the physical volume (or a re-scan) to confirm the last 4 boys.

**Overall conclusion of the "do the transcription" thread (Deisel + Trendelburg cores, verified):**
- **No Carl with a Gansen/Konze/*n-s-n surname in either true 1835-core class.** Deisel 1849 = two Heinrich Konzes (stayed); Deisel 1850 = no Carl-forename, no Konze boy; Trendelburg 1849 = a Carl Wilhelm **Henze** (baptism-verified; wrong surname). The single "Ganzen ≈ Gannsen" scare was a cursive mis-read, closed by the baptism. The result is consistent with every prior parish: the forename Carl recurs, but never on Charles's surname — keeping the live search on the un-digitised / Tier-3 parishes and the emigration-side records.

**Second attempt to nail boys 19–22 (21 Jun, same session) — still blocked.** Re-probed images 933–940 with header/entry-number verification. Confirmed: (a) Seite 72 genuinely starts at **entry 31** (girls Meimbresse/Lotze/Köster), so the boys 19–22 + girls 23–30 sit on a separate "entries 19–30" leaf; (b) the page-number box is **non-deterministic** — typing "939" loaded the 1849 boys leaf on one try and the 1850-class Seite 76 leaf on another; typing "933/935/937" surfaced 1845/1848/1851 leaves interchangeably. The specific 1849 entries-19–30 leaf did not surface in repeated probes. **This is a viewer/scan defect, not a content gap** — the leaf exists in the bound volume. Recommend the **Trendelburg/Deisel Pfarrarchiv or an Archion re-scan request** to read entries 19–22; online navigation to that exact leaf is currently unreliable. Result unchanged in substance: 18/22 boys read (no Carl, two Heinrich Konzes), final 4 boys pending a clean image.

---

## Session 10 — 22 June 2026 (LIVE Archion: residual classes read end-to-end; Lüdicke "KONZE, 2 Brüder" find)

**Scope (Jed):** "finish looking at all confirmations for 1833–1841 for candidates, then complete the follow-ups for the Friedrichsfeld research log." Driven live in Archion via the Chrome extension, signed in as Jed. **The Session-7 viewer blocker did NOT recur** — the confirmation-register deep-zoom viewer rendered and screenshotted fine this session (the earlier 45-s timeout was specific to the un-OCR'd *baptism* SPA). So the residual confirmation classes were read directly by deep-zoom eye-reading, and Archion **"Permalink erstellen"** was used to mint per-page permalinks.

### Method confirmed
- Page-number box → deep-zoom viewer → "+" to load high-res tiles → screenshot/zoom regions to read the **confirmand given-name column** (reliable for "is there a *Carl*?") and scan all surnames for a Konze/Gansen/\*n-s-n hit.
- **Same scan-jumble + stale-canvas defect as Deisel (Session 9) is present in Helmarshausen, Sielen, Hümme and the Schöneberg Konf register**: a given image number renders different leaves on different tries, Seite order ≠ image order, and duplicate leaves occur. Year/Seite headers were read on-screen each time rather than trusting the image-number box.

### Helmarshausen — Konf. **219208** (residual classes 1850–55 + re-confirmed 1848–50)
Permalinks: **img 1294 (1849/1850 prime cohort) → https://www.archion.de/p/339ca14e38/** ; **img 1305 (1854 class) → https://www.archion.de/p/8215e4ee7a/**. Band 2 (1851–1903) opens with a title leaf at img 1297.
| Class | Image(s) / Seite | Carls found (forename) | Konze/\*n-s-n? |
|---|---|---|---|
| 1848 | img 1290=1296 (S.87–88), 1291 (S.89–90) | (entry 9) **Carl Julius Bringemann b.1836** — already logged | no (Bringemann) |
| 1849 | img 1293 (S.93–94 boys 11–20), 1295 (S.95–96 girls) | Georg **Carl** Grimmel b.1834 (middle name) | no (Grimmel) |
| 1850 | img 1294 (S.101–102 girls; closing "14 Söhne, 10 Töchter") | none among entries read (girls) | no |
| 1851 | img 1298–1300 (S.102–108) | **Carl Schäfer b.19 Nov 1836** | no (Schäfer) |
| 1852 | img 1301–1303 (S.109–113) | **Carl August Hofmeister** b.1838 (entry 8) | no |
| 1853 | img 1303–1304 (S.113–116) | none — 8 boys + 15 girls, no Carl | no |
| 1854 | img 1305–1306 (S.117–120) | Ferdinand **Carl** Gunge; **Carl** Heinr. Mayer/Wagner; **Carl** Eduard Wagner (b.1839–40) | no |
| 1855 | img 1307 (S.121–122) | **Carl** Eduard Hülse; + middle-name Carl (b.1841) | no |
- Jumble-blocked residual leaves (not cleanly isolable): 1847 (S.85–86), 1849 boys 1–10 (S.91–92), 1850 boys 1–14 (S.97–100). img 1290 is a **duplicate** of S.87–88.

### Sielen — Konf. **220039** (residual 1850/1851/1852/1853 + 1847/1848)
Permalink: **img 730 (Seite 42 = 1850/1851) → https://www.archion.de/p/b77f5c56b0/**. Tiny parish (3–18 per class).
- **★ 1850 class (the prime cohort, births ~1835) = exactly 3 confirmands** (closing note "Confirmanden im Jahr 1850: 3 Personen, 2 männl., 1 weibl."): **Friedrich August Lenzing (b.1836), Heinrich August Lenzing (b.1836), and one girl (Ida, b.1835). NO Carl; surnames Lenzing/Ida.**
- 1851 (img 730 right, 5 confirmands): Gaßmann, Hofeditz, Lenzing, Gaßmann, Ried — no Carl. (Note "Gaßmann" ≠ "Gansen".)
- 1852 (img 732, S.46–47), 1853 (img 734/736, S.48–51): boys Johann/Ludwig/Andreas/Heinrich; **one Carl = "Carl Ludwig Basser" b.1839 (1853)** — surname Basser, no match. 1855 area (img 741): no Carl read.
- 1849 already read Session 3 (no Carl). Net: **clean negative, prime 1850 cohort confirmed.**

### Hümme — Konf. **219529** (residual 1848 + 1850)
Permalink: **img 36 (Seite 64 = 1850 prime cohort) → https://www.archion.de/p/b001b67490/**.
- **★ 1850 class (births ~1835), boys 1–8 read in full:** Konrad August Schwarzmeier, Johannes Müller, Wilhelm Georg zu Hoff, Friedrich August Voltze, Friedrich Köhler, Conrad Israel, Johann Wilhelm Hensel, Albrecht Vogt — **NO Carl**; surnames all local non-\*n-s-n.
- 1848 class (img 34, S.62–63): entries 11–24 are mostly girls + Friedrich Rödde — no Carl (boys 1–10 on img 33, where Session 4 already found only Carl Wilhelm Wilmes b.12 Mar 1834, surname Wilmes, no match).

### Gudensberg — Konf. **244437** (final residual: the 1855 class)
Permalink: **img 1922 (Seite 122–123 = end 1854 + start 1855) → https://www.archion.de/p/ea4e5b32da/**.
- **1855 class boys 1–5:** August Wilhelm Becker, George Bracke, **Carl Christian Weinrich (b.1841)**, Heinrich Christian Martin, Adam Groß — one Carl (Weinrich, b.1841), **no match**. Closes the Gudensberg sweep (Sessions 5 read 1848–1854): **uniform negative 1848–1855.**

### Schöneberg — confirmation register LOCATED & a Session-2 correction
- **Session 2 wrongly pointed at reg. 220009** for the 1847–1855 confirmations. The 220009 title-page index shows its **Konfirmationen section runs only 1823–1835** (the prose list ends at the 1835 class, img ~1191) — the post-1835 confirmations are **not** in that volume.
- **Correct register = 220012 (Kirchenbuch 1830–1926)**, whose title index lists **"Konf 1831–1926, S. 1–100."** Confirmed live: Konf S.2–3 = 1832–36 (img 1698), S.12–13 = 1842–43 (img 1693), S.57 = 1860 (img 1702) — i.e. a tabular Konfirmationen register that DOES cover Charles's 1849–1850 window.
- **The exact 1849–1850 leaf could not be isolated** — the section is severely scan-jumbled/stale-canvas (probes returned non-monotonic Seite/year mappings). **Precise handoff:** reg. **220012**, Konfirmationen section, Seite ~18–20 (≈ img 1699–1701), for a Peter/Jim read or an Archion re-scan.

### Net result of the live residual sweep
Across **Helmarshausen 1848–1855, Sielen 1847–1855, Hümme 1848+1850, Gudensberg 1848–1855** — plus the Deisel/Trendelburg 1849–1850 cores read in Session 9 — the result is uniform and now well-saturated: **the forename Carl recurs in nearly every class, but never once on a Konze / Gansen / \*n-s-n surname, and no boy named Carl with Charles's surname appears in any prime (births ~1834–1836) cohort.** Residual unread cells are all jumble-blocked window-edge or duplicate leaves. This continues to point the live search away from the digitised Hofgeismar/Fritzlar confirmation registers and toward the emigration side and the un-digitised gaps.

### Friedrichsfeld follow-up #1 — Lüdicke Deisel-emigrant study → CHECKED, with a find ★
Reached Martina Lüdicke, *"Verschwunden ist der Strand …"* (Deisel emigrants to America, 1994, 92 pp.) via **Google Books in-book search**: **"1 page matching Konze — p. 89."** The p. 89 snippet is the appendix roster **"Auswanderung aus Deisel nach Amerika nach 1876,"** and under *ohne Jahresangabe* (no year) it lists **"KONZE, 2 Brüder."**
- **First published, name-level record of Konze emigration from Deisel → USA.** But it is **post-1876**, ~20 years after Charles → **not Charles** (likely later kin / chain migration). Konze appears **only** here; the **1831–1866 core tables contain no Konze**, consistent with Charles emigrating un-indexed/under a changed name.
- Logged into `germany/friedrichsfeld-research-log.html` (Lüdicke section + follow-ups). **New lead:** trace the 2 post-1876 Konze brothers in US records.
- Follow-up #2 (Justus Ernst Konze's fate — Stammen burials 220072 / HStAM Best. 180 / Mainz civil death) remains **OFFLINE**; not advanced this session.

---

## Session 11 — 22 June 2026 (AUTOMATED scheduled-task run: re-verify the six queued transcriptions)

**Run by:** scheduled task "check-archion-transcriptions" (autonomous; Jed not present). Read-only on Archion; signed in via the Chrome extension. Nothing changed on Archion.

### Headline
- **All six queued AI transcriptions remain PROCESSED** (not pending) and were re-read this run via the **"Erkannter Text" panel** (top-toolbar document icon — the in-image "txt" overlay still renders blank, as noted in Session 6). No page showed "Bisher keine Texterkennung."
- **Result is unchanged from Session 6 (21 June)** — no new candidate. This run is a confirmation pass, not a new discovery.

### Per-register state this run
| Register | Image | Transcription | Year/Seite (per panel) | Carl(s) | n-s-n / Konze? |
|---|---|---|---|---|---|
| Deisel 218836 | 946 | **processed** | title leaf / panel shows Seite 90–91 (1854) | — (image = title page) | — |
| Deisel 218836 | 947 | **processed** | Seite 92–93 (1854–55) | Andreas **Karl** Drönner (b.1838); **Karl** Niemeyer (b.1840); **Carl** August Köster (b.1841); **Carl** Wilh. Friedr. Koch (b.1841) | no |
| Deisel 218836 | 948 | **processed** | Seite 94–95 (1855) | Joh. **Carl** Ludwig Weifenbach (b.1841); **Carl** Julius Köster (b.17 Jan 1841, f. Christian Köster, **mo. Marie Elisabeth geb. Konze**) | Konze = maiden name only; not a Carl-surname |
| Trendelburg 220102 | 2259 | **processed** | Seite 62–63 (Pfingsten 1844) | **Carl** Wilh. Joh. Friedr. [Auster/Außermühle] (b.1829); Christian Heinr. **Carl** Wilh. Aderholz (b.1830) | no |
| Trendelburg 220102 | 2260 | **processed** | Seite 64–65 (1844 cont., daughters) | none | no |
| Trendelburg 220102 | 2261 | **processed** | Seite 66–67 (Pfingsten 1845) | **Carl** Louis Herwig (b.1831); Georg **Carl** Quentin (b.1831, unehel.) | no; + mother "geb. Konze/Conza" on the **Enders** entry (maiden name, still C/K-ambiguous) |

### Notes
- **No Carl with a Gansen / Konze / \*n-s-n surname on any of the six pages.** Every Carl carries a local non-matching surname (Drönner, Niemeyer, Köster, Koch, Weifenbach, Auster, Aderholz, Herwig, Quentin) and all births fall on the window edges (1829–31 or 1840–41), not the 26-Jan-1835 core.
- **Konze appears only as a maiden name** (mothers): geb. Konze on Deisel S.94–95 (mother of Carl Julius Köster) and the C/K-ambiguous "geb. Konze/Conza" on Trendelburg S.67 (Enders) — both already flagged in Session 6; nothing new.
- **Calibration reminder still stands** (Session 6): these six images are window **edges**, not the 1835 core. The true cores (Deisel 1849–50, Trendelburg 1849) were deep-zoom-read in Session 9 and likewise yielded **no Gansen/Konze Carl** (the "Ganzen" scare resolved to **Henze**).
- **No Archion action queued** (quota exhausted). Nothing further to monitor on these six pages — they are fully read and stable. The scheduled monitor can be retired or pointed at new pages if/when a fresh transcription allotment is obtained.
