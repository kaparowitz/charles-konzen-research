# Session 112 — Sielen Confirmation-Register Sweep (Archion 220039)
## Date: June 22, 2026

## Objective
Live re-sweep of the **Sielen Konfirmationen** register (Archion churchRegister
**220039**, "Konfirmationen 1831–1974", Band I, 901 images) for the widened
June-2026 question: **any boy named Carl/Karl, born 1833–1841, surname open**,
who would surface in the **1847–1855** confirmation classes. Mint per-image
Archion permalinks (the parish log previously had none) and reconcile the stale
`germany/sielen-research-log.html` against `search-coverage.html`.

Driven live in Archion via the logged-in browser (subscription content — handled
in-viewer per project convention, not via the web-data plugins).

## Register structure & calibration (the important methodological finding)

- Title page (Konfirmations-Buch, Gemeinde Sielen, Band I, "vom 1. Jan 1830 bis
  5. Mai 1974") = **image 711**. First tabular entries (1831 class) begin ~713.
- The page-number dropdown **skips images 829–874** (a gap in the viewable run).
- **The viewer's page-input field is unreliable on this register** (the
  documented "stale canvas / page reverts" behaviour). A bare `type page → Return`
  frequently leaves the *previous* leaf's tiles on screen, which produced several
  false "Seite/Jahr" reads early in the session (e.g. a phantom "image 735 =
  Seite 50/51" and a phantom "740 = Seite 108/1874"). **Forcing a redraw (click
  the viewer + then − after navigating) before reading the header fixes this.**
- With forced redraws, the candidate window is **clean and sequential**,
  2 Seiten per image (no shuffling in this stretch — the apparent shuffle was the
  stale-canvas artifact):

| Image | Seite | Confirmation year(s) |
|------:|------:|----------------------|
| 729 | 34 / 35 | 1846 / 1847 |
| 730 | 36 / 37 | 1847 (summary) / 1848 |
| 731 | 38 / 39 | 1848 |
| 732 | 40 / 41 | 1849 |
| 733 | 42 / 43 | 1850 / 1851 |
| 734 | 44 / 45 | 1851 |
| 735 | 46 / 47 | 1852 |
| 736 | 48 / 49 | 1852 (tail) / 1853 |
| 737 | 50 / 51 | 1853 (tail) / 1854 |

Confirmation dates read on the headers: 1847 "am 23ten Mai", 1848 "am 11ten Juni",
1849 "am 27ten Mai", 1850 "am 19ten Mai", 1851 "am 8ten Juni", 1852 "am 11ten
April", 1853 "am 27ten März". Ages run 13–15, consistent with the birth years.

## Carl/Karl sweep — results by class

Method: read the **"Namen der Confirmirten"** column (given name reads reliably in
Kurrent; surnames warrant a second eye). Males are listed first in each class,
females after; only male entries can carry "Carl/Karl".

| Class | Seite | Result | Male given names seen (best reading) |
|------:|------:|--------|--------------------------------------|
| 1846 | 34 | no Carl | — (tail of class) |
| 1847 | 34b–35 | **no Carl** | Heinrich August, Salomon (Wassmann), Christian August (Otte), Ludwig/Conrad-type |
| 1848 | 36–39 | **no Carl** | Joh. Conrad Lenzing, Joh. Heinrich Hof, Christian Ludwig, Georg Wilhelm, Friedr. Conrad, Friedr. Wilhelm Gefferich, Joh. Heinrich Gefferich, Heinrich |
| 1849 | 40–41 | **no Carl** | Johann, Friedr. Wilhelm Gefferich, Joh. Heinrich, Gottfried Hof, Friedr. Wilhelm |
| 1850 | 42 | **no Carl** | Friedr. August Lenzing, Heinrich Friedr. August Lenzing (small class) |
| 1851 | 43–45 | **no Carl** | Conrad Georg, Johann Conrad, Joseph-type |
| 1852 | 46–48 | **no Carl** | Joh. Heinrich Hof, Konrad Wilhelm, Konrad Wilhelm, Johann Wilhelm |
| **1853** | 48b–51 | **⭐ one Carl** | **Carl Ludwig Bößler** (entry 5, Seite 49) |
| **1854** | 51 → 52+ | **⭐⭐ two Carls** | **Heinrich Carl Storch** (entry 1); **Carl Ludwig [Stein]** (entry 2) |
| 1855 | 52+ | not separately read | Seite 52+ runs past the cleanly-read leaves; off-anchor (births ~1840–41) |

### The three Carls (all non-matching)

1. **Carl Ludwig Bößler** — Seite 49, 1853 class, **entry 5**.
   - Born **19 März 1839**; age 14 at confirmation (27 März 1853).
   - Father **Friedrich Wilhelm Bößler, Leineweber** (weaver), of Sielen; mother
     Johanna (geb. …, not fully read).
   - Surname read "Bößler"/"Büßler" (B-vowel-ßler), re-zoomed three times on a
     forced-redraw render. **This corrects the earlier tentative "Carl Ludwig
     Basser" record** logged before the Sielen calibration was fixed.
   - Verdict: born 1839 (4 yr after the 26 Jan 1835 anchor); surname is a B-form,
     not a *…n·s·n* / Gannsen variant. **Not a match.**

2. **Heinrich Carl Storch** — Seite 51, 1854 class, **entry 1**.
   - Born **1840**; age 14. Father Johann [Conrad/Eduard] Storch, Ackermann; mother
     Christine Marie Elisabeth (geb. Mein[er]).
   - Verdict: born 1840; surname Storch. **Not a match.**

3. **Carl Ludwig [Stein]** — Seite 51, 1854 class, **entry 2**.
   - Born **1840**; age 13. Father Johann Heinrich […]. Surname tentative ("Stein"/
     similar local name).
   - Verdict: born 1840; local surname. **Not a match.**

The 1853/1854 Carls were the "jumble-blocked window-edge" cells flagged on
`search-coverage.html`; reading them required the forced-redraw method. The two
1854 Carls were **not** in the prior record (which listed only the one 1853 Carl).

## Conclusion

The Sielen confirmation classes across the candidate window — **1846–1854,
covering births ~1831–1840** — contain **no boy named Carl who matches Charles**
(b. 26 Jan 1835; American surname → Gannsen / *…n·s·n*). Crucially, the
**anchor-core classes (births 1834–1836 = the 1848, 1849, 1850 classes) contain
no Carl at all.** Every Carl that does appear is born 1839–1840 with a local
Sielen surname (Bößler, Storch, Stein). This **confirms and strengthens the
ELIMINATED verdict** for Sielen and supersedes the single-Carl record with a
corrected reading plus two newly-found (non-matching) Carls.

Residual: the **1855 class (Seite 52+)** was not separately read; it is off-anchor
(births ~1840–41) and lies just past the cleanly-rendered leaves. The exact
page-map beyond Seite 51 is left for a Kurrent specialist (Peter Schräder) or the
September archive trip, per the standing method note.

## Archion permalinks minted (force-redraw verified)

The original 22 Jun sweep minted permalinks only for the window-edge leaves
(735–737, where the Carls appear). On **28 Jun 2026** the earlier candidate-window
leaves (729–734, the 1846–1851 classes — including the anchor-core 1848/1849/1850
classes) were re-opened live in the viewer, each Seite/Jahr header re-confirmed
against the table above, and per-image permalinks minted. Every class in the
1846–1854 candidate window now has a citable link.

| Permalink | Image | Seite | Content |
|-----------|------:|------:|---------|
| https://www.archion.de/p/23e492013b/ | 729 | 34 / 35 | 1846 (am 31 Mai) / 1847 (am 23 Mai) — no Carl |
| https://www.archion.de/p/37bf8ec0d1/ | 730 | 36 / 37 | 1847 summary / 1848 (am 11 Juni) — no Carl |
| https://www.archion.de/p/fdcca8212c/ | 731 | 38 / 39 | 1848 — no Carl |
| https://www.archion.de/p/8951455284/ | 732 | 40 / 41 | 1849 (am 27 Mai) — no Carl |
| https://www.archion.de/p/69740b182e/ | 733 | 42 / 43 | 1850 (am 19 Mai) / 1851 (am 8 Juni) — no Carl |
| https://www.archion.de/p/bd48148c76/ | 734 | 44 / 45 | 1851 — no Carl |
| https://www.archion.de/p/6436dc9d8d/ | 735 | 46 / 47 | 1852 class — no Carl |
| https://www.archion.de/p/edc4e8bcbe/ | 736 | 48 / 49 | 1852 tail / **1853 — Carl Ludwig Bößler (entry 5, S.49)** |
| https://www.archion.de/p/00ce7acdf9/ | 737 | 50 / 51 | 1853 tail / **1854 — Heinrich Carl Storch (1), Carl Ludwig [Stein] (2)** |

Register: Archion churchRegister **220039**, Sielen Konfirmationen 1831–1974,
Landeskirchliches Archiv der Ev. Kirche von Kurhessen-Waldeck, Kirchenkreis
Hofgeismar.

## Reliability notes
- Given names (Carl vs Johann/Conrad/Heinrich) read reliably; **surnames are
  best-readings, not certified transcriptions** (Bößler, Storch, Stein especially).
- Birth-year numerals are the weakest reads; confirmation-year headers + ages were
  cross-checked for internal consistency.
- The page-input field reverts/staled repeatedly; all cited image↔Seite pairs were
  re-verified with a forced redraw before reading.
