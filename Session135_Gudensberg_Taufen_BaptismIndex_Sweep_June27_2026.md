# Session 135 — Gudensberg town Taufen 1830–1844, baptism name-index sweep (1833–1841 window)

**Date:** 27 June 2026
**Task (Jed):** "sweep the baptism index for 1833-1841 for gudensberg"
**Register:** Gudensberg TOWN **Taufen 1830–1844**, Archion churchRegister **244439**
(Kirchenkreis Fritzlar; 531 images; parish tagged *"komplett transkribiert"*).
Workflow: in-browser Archion viewer (Jed logged in), index leaves read by eye.

## Why this was worth doing
The Gudensberg research log had a standing caveat (23 Jun 2026): the parish's **own**
Taufen book had *not* been surname-scanned for the Konze/Gans pool — only the
confirmation register (244437) and the two filial baptism books (Dissen 253403,
Grifte 253444) had been read. This session closes that gap.

## Register structure & calibration
- **Baptism body:** one opening per Seite, **Seite = Bild − 248**
  (Bild 250 = Seite 2 / 1830 Aug; **Bild 267 = Seite 19 / 1831 Aug–Sept**).
  Register runs ~Seite 1–254 (1830–1844); Nro continuous, ~4 entries/Seite.
- **Alphabetical name-index** at the END of the reel, **Bild ~508–525**,
  columns Männlich | Seite | Weiblich | Seite, entries ordered **by Seite within
  each letter** (NOT sub-alphabetical); common letters span TWO leaves.
- ⚠️ Despite "komplett transkribiert", the **index leaves carry no usable OCR**
  (`get_page_text` + the "txt" overlay return nothing on the index) → read by eye.
  Stale-canvas after every page-number jump — force a redraw with a zoom +/− or
  step with the prev/next arrows.
- Letter→Bild map (verified live): A|B = 508; **B·C|D = 510** (`p/85f21c743c`);
  D|E = 509; E = 511; **F|G = 513** (`p/f41ff41983`); **G(cont) = 514**;
  **H|I·J = 515** (`p/0cae314e05`); **I|K = 516** (`p/d78fbe9f62`);
  **K|L = 517** (`p/a9b6fa22cf`). (Leaves 509/510 bound slightly out of image
  order; no separate C page — B² overflow + C share one leaf.)

## Result — clean NEGATIVE for the entire Konze/Gans pool
| Letter | Leaf(s) | Surnames present | Pool verdict |
|---|---|---|---|
| **K** | 516R + 517L | König, Korf, Köhler, Köhe, Knoll, Knauß, Kißmann, Kißler, Knoch, Kell, Käufer, Krieg, Kolbe, Kußmann, Kümpel, Kümpfer, Kurz, Kaufhünger, Kirchmann, Koch, Klugfelder, + illeg. compound "Kor[n]zügel" | **No Konze/Kontze/Konsen/Konzen** |
| **I·J** | 515R | Jungermann, Jungkurt/Jungcurt, Jacob | **No Jungkonze/Jungkontze** |
| **G** | 513R + 514 | Groß, Göppel, Gümbel, Göddel, Günther, Goestmann, Gerhard(t), Goebel, Güth, Gridel, Gleisner, Gippert | **No Gans/Ganß/Ganson** |
| **C** | 510L (combined B·C) | one B-overflow entry only ("Beier/Bäse…248") | **No Conson/Contze/Conze** |

## Rigor note — Ganß vs. Groß (a near-error caught)
The FIRST G-index entry, "…Carl…, Seite 19", read as **"Ganß"** at low zoom — which
would have been a genuine Gans-pool hit in a town that otherwise has none. Pulled the
actual baptism (Bild 267 = Seite 19, `p/9ac4dd7943`): it is **"Groß — Ferdinand Carl
Hermann"**, male, **bapt. 11 Sept 1831**, father the local **Amts-Schäfer (sheep-master)
Groß** × Caroline geb. Finckel/Vinckel, godfather **Ferdinand Borchmann zu Oberkirchen**.
→ **Groß, not Ganß** = NOT a pool surname (classic Kurrent Ganß/Groß confusion).
Lesson: always verify a "G…ß" index hit at the entry image before recording it.
The only other Carl in the G index is "Karl Goebel" (Seite 239, ~1844). So **Gudensberg
town has no Gans family at all** — unlike the Weser-corridor parishes (Oedelsheim,
Heisebeck, Bodenfelde).

## Bottom line
Gudensberg TOWN is now searched on the **baptism track** too (was already negative on
confirmations 244437 + the filial baptism books Dissen 253403 / Grifte 253444). No
Konze/Kontze/Konsen/Konzen, no Jungkonze, no Gans/Ganß/Ganson, no Conson in the entire
1830–1844 baptism index (which fully covers the requested 1833–1841 window). **Gudensberg
stays ELIMINATED.** Because the index is the register's own comprehensive alphabetical
listing and contains no pool surname at all, a leaf-by-leaf scan of the 1833–1841 window
would add nothing — there is no "Carl on a pool surname" to find.

## Permalinks minted (reg. 244439)
- K index leaf (Bild 517) — `https://www.archion.de/p/a9b6fa22cf/`
- I·J index leaf (Bild 515) — `https://www.archion.de/p/0cae314e05/`
- F·G index leaf (Bild 513) — `https://www.archion.de/p/f41ff41983/`
- B·C index leaf (Bild 510) — `https://www.archion.de/p/85f21c743c/`
- I·K index leaf (Bild 516) — `https://www.archion.de/p/d78fbe9f62/`
- Groß baptism, Seite 19 / 1831 (Bild 267) — `https://www.archion.de/p/9ac4dd7943/`

## Follow-up (28 Jun 2026) — marriage + burial indexes also swept ("scan the surnames")
Closed Gudensberg town on every rite. Both in-window vital registers carry built-in
alphabetical name-indexes; both = NEGATIVE for the whole pool.

**Trauungen 1830–1863 = reg 244449** (shared reel 2438 imgs; section title "Trau- und
Register" at Bild 2243; index at end of section ~Bild 2417–2424):
- C = Bild 2417 (empty) → no Conson/Contze
- G = Bild 2420–2421: Graewer, Gummerwald, Geiser, Gröde, Groß, Gleisner, Glaser, Gippert,
  Gümbel, Griesel, Güth, Gold, Goebel, Grunewald, Gerhard → no Gans/Ganß (`p/ca1b922804`)
- I·J = Bild 2422: Jungermann, Jacob, Fehler, Fulberger → no Jungkonze
- K = Bild 2424: Krug, Kurz, Krause, Kubnert, Kolbe, Kieser, Küchmann, Kalb, Keim, Kaiser,
  Klöffler, Kneppor, Kauffunger, Kruse, Kroll, Kranz, Korb, Knorbe → no Konze (`p/39dcd061fc`)

**Beerdigungen 1830–1851 = reg 244444** (shared reel 1121 imgs; section title "Tod- und
Register" at Bild 836; entries Seite = Bild − 839 [Seite 1 = Bild 840; Seite 248/1851 =
Bild 1087]; entries end ~1091, "blank pages NOT filmed" card 1095, X-divider 1096). ⚠️ The
alphabetical index is filmed at the **very END of the reel, AFTER the X-card, Bild
~1097–1106** (not at the section front/back):
- C ~Bild 1100 (only a B-straggler "Beier 251") → no Conson/Contze
- G = Bild 1103–1104: Gleisner, Grantler, Gippert, Girt, Grunewald, Groß, Gawer, Germeroth,
  Goebel, Gründer, Runte → no Gans/Ganß (`p/cee74ad45c`)
- I·J = Bild 1105 (+ empty "I" 1106L): Jungermann, Jacob, Jungkurt, Imberger → no Jungkonze
- K = Bild 1106: Knoll, Krieg, Kußmann, Krug, Kolbe, Kaufunger, Kaiser, Knödding, Kroll,
  Kranz, Korf, Kurz → no Konze (`p/62a07114c5`)

NB the **"Jungkurt / Jungcurt"** surname (a local Jung+Kurt family, NOT Jungkonze) recurs
in all three Gudensberg indexes. With baptisms (244439), marriages (244449) and burials
(244444) all swept and all negative — plus confirmations (244437) — the Konze/Gans pool is
absent from **every** Gudensberg vital register, well beyond the 1833–41 window. Gudensberg
town is comprehensively eliminated.

## Files updated
- `_MEMORY_Session_Conventions.md` — added the 244439 calibration + result entry; appended
  the 244449/244444 marriage+burial sweep results & permalinks.
- `germany/gudensberg-research-log.html` — new "Own baptism register 244439 — name-index
  swept" section + table; closed the residual-scan caveat; added a "Marriage & burial
  registers — name-indexes swept" section; updated Sources table & permalinks.
