# Wikidata item draft — Charles Konzen (1835–1903)

**Purpose.** Annotated, statement-by-statement reference for the
Wikidata item, including which claims are confirmed vs asserted vs
to-be-omitted. Cross-references against the project's working /
confirmed / open / eliminated taxonomy.

**For the actual mint, use the sibling file** —
[`wikidata/quickstatements.txt`](wikidata/quickstatements.txt) is
paste-ready for the QuickStatements bot at
<https://quickstatements.toolforge.org/>. **This file is the
human-readable review of *what* is in that batch and *why*.** Read
this before submitting; submit through QuickStatements for speed.

Once Wikidata assigns a Q-number, drop it into
`PLACEHOLDER-WIKIDATA-Q-ID` per `IDENTIFIERS_KIT.md` §4.4.

**Status:** draft, May 2026. Cross-checked against the project's
working/confirmed/open/eliminated taxonomy. Statements marked
**[CONFIRMED]** have multiple-source attestation; statements marked
**[ASSERTED]** have one strong source; **[OMIT]** flags claims that
should not be added until the underlying evidence is closed.

---

## Item header

```
Label (English):       Charles Konzen
Label (German):        Charles Konzen
Description (English): Hessian-American Civil War sergeant of Battery B,
                       2nd Missouri Light Artillery (1835–1903),
                       recorded in U.S. records as Gannsen / Johnson
Description (German):  Hessischer Auswanderer, Sergeant der Battery B,
                       2nd Missouri Light Artillery (Unionsarmee, US-Bürgerkrieg),
                       in US-Quellen als Gannsen oder Johnson geführt (1835–1903)

Aliases (English):     Charles Gannsen ; Charles Johnson Sr. ; Karl Konzen ; Carl Konzen ;
                       Karl Konze ; Charles Konsen ; Charles Conson
Aliases (German):      Karl Konzen ; Carl Konzen ; Karl Konze ; Karl Contzen
```

> Note. Aliases follow the surname variants attested in primary
> sources; the project's `Andreas_Konze_Identity_Disentanglement.md`
> file documents which spelling appears on which document.

---

## Statements

Format below: `property — value — qualifiers — source`. Wikidata
property numbers are given so you can paste directly into the
"add statement" field.

### Identity

```
P31  (instance of)         →  Q5  (human)                              [CONFIRMED]
P21  (sex or gender)        →  Q6581097  (male)                         [CONFIRMED]
P735 (given name)           →  Q1124013  (Charles)                      [ASSERTED — anglicized form on every U.S. record]
P734 (family name)          →  (search "Konzen" — accept the existing surname item if one exists,
                                or skip this statement if not; aliases above carry the variants)
```

### Vital dates

```
P569 (date of birth)        →  26 January 1835                          [CONFIRMED]
   qualifier P1480 (sourcing circumstances) → Q71536040 (multiple sources concur)
   reference P248 (stated in) → Civil War enlistment register, 1862;
                                St. Marcus marriage register, 1866;
                                1880 U.S. Census; 1900 U.S. Census;
                                1891 pension declaration

P19  (place of birth)       →  Q-item for Deisel, Hofgeismar  (search Wikidata; if missing, omit)   [ASSERTED]
   qualifier P518 (applies to part) → "village of Deisel, Kreis Hofgeismar, former Electorate of Hesse-Kassel"
   reference: 1866 St. Marcus marriage register lists "Deisse, Kreis Cassel, Churhessen" — phonetic Deisel.
   **Note:** the specific German baptismal entry has not been recovered, so
   the place-of-birth statement is asserted, not confirmed.
   If you'd rather hold this open, mark with P5102 (nature of statement) → "claimed".

P570 (date of death)        →  19 December 1903                         [CONFIRMED]
   reference P248 (stated in) → St. Marcus burial #3393

P20  (place of death)       →  Q38022  (St. Louis)                      [CONFIRMED]
   reference P248 (stated in) → St. Marcus burial register

P119 (place of burial)      →  Q-item for Old Saint Marcus Cemetery, St. Louis  [CONFIRMED]
   qualifier P5436 (number of records) → "burial #3393"
```

### Citizenship & ethnicity

```
P27  (country of citizenship) → Q183  (Germany — at birth, via Hesse-Kassel)   [CONFIRMED]
P27  (country of citizenship) → Q30   (United States — naturalised)             [CONFIRMED]
   qualifier P580 (start time) → 1865-04-29 (naturalisation date — verify against /civilwar/ naturalisation card)
   reference P248 → naturalisation card #5 in /evidence/

P172 (ethnic group)         →  Q42884  (Germans)                                [CONFIRMED]
```

### Family

```
P22  (father)               →  Andreas Konze  (only add if Andreas has his own Q-item)  [ASSERTED]
   reference: 1866 St. Marcus marriage register names father; cross-checked
              against Trendelburg parish register Session18 finding.

P25  (mother)               →  (open — name on marriage register transcribes as "Margaretha";
                                no parish-confirmed mother yet. OMIT until closed.)

P26  (spouse)               →  Q-item for Friederike (Frederica) "Conson" / Konzen, née ?    [CONFIRMED — marriage]
   qualifier P580 (start time) → 1866-MM-DD (St. Marcus marriage)
   qualifier P1545 (series ordinal) → "1" (only marriage)
   reference P248 → St. Marcus Evangelical Church marriage register, 1866

P40  (child) ×7             →  one statement per child, only after each child has a Q-item or
                                a redirect target. The seven children are documented at
                                /charles_america/seven-children.html — most have their own
                                /children/ subpage on the site. OMIT for first deposit; create
                                items for the children later if there's appetite.
```

### Career

```
P106 (occupation)           →  Q1734662  (military personnel)                    [CONFIRMED]
P106 (occupation)           →  Q190551   (artilleryman)                          [CONFIRMED]
P106 (occupation)           →  (post-war occupation from St. Louis directories — labourer,
                                 cooper, depending on year. Add statement(s) per directory year if you
                                 want this granular.)

P241 (military branch)      →  Q9212  (Union Army)                              [CONFIRMED]
P410 (military rank)        →  Q97171474  (sergeant — U.S. Army, Civil War)     [CONFIRMED]
   qualifier P580 (start time) → date of promotion (verify in service record)

P607 (conflict)             →  Q8676   (American Civil War)                     [CONFIRMED]

P39  (position held)        →  member of Battery B, 2nd Missouri Light Artillery    [CONFIRMED]
   qualifier P580 / P582 → enlistment / muster-out dates from compiled service record
   reference P248 → NARA compiled service record G11-422819443E
```

### Cross-references (the sameAs network)

Add these **last**, after the QID is minted, so the references link
back here.

```
P973 (described at URL)     →  https://charles-research.netlify.app/         [REQUIRED]
P973 (described at URL)     →  https://charles-research.netlify.app/de/      (German entry point)
P356 (DOI)                  →  __DOI__   (after Zenodo deposit — see IDENTIFIERS_KIT.md §1)
P2671 (Google Knowledge Graph ID) → (skip; auto-populated by Google after item indexing)
P3430 (SNAC ID)             →  (skip — SNAC is for archival creators with significant published work)
P9747 (Find a Grave memorial ID) → if the project has linked one for the Old Saint Marcus burial; otherwise OMIT
```

---

## Sister items to consider creating

Useful but not required for the first deposit. Each is a 5-minute
mint and meaningfully improves the cross-reference graph.

| Sister item | What it would represent | Priority |
|-------------|------------------------|----------|
| Battery B, 2nd Missouri Light Artillery | The unit | **High** — links Civil War historians directly to the project |
| Andreas Konze (1789–?) | Charles's confirmed father | Medium — supports the Trendelburg / Hofgeismar identity work |
| St. Marcus Evangelical Church (St. Louis, demolished) | The wedding-and-burial church | Medium — connects with St. Louis history items |
| Old Saint Marcus Cemetery, St. Louis | Burial site | Low — already indexed by Find a Grave |
| Trendelburg parish register #220108 | The Taufen volume that holds the candidate baptism | High for genealogists — Archion catalogues these |

---

## Things to **omit** from the first deposit

The Wikidata "no original research" policy is loosely enforced for
biographical items, but the project's reputation will benefit from
strict adherence. Hold these back until they have a published source
behind them:

- **Specific Trendelburg baptism entry as Charles's birth.** The
  candidate is identified but the parish entry has not been
  reconciled against Trendelburg KB 220108 with certainty. Use
  `place of birth = Deisel` cautiously, qualified as "according to
  marriage register".
- **The "Konze → Konzen → Gannsen → Johnson" surname chain.** It is
  documented on the site but not yet in print; cite the site as
  the source via `P973`.
- **The 64th Illinois mystery.** Listed as an open research log
  on the site; add nothing about it to Wikidata.
- **Any photograph.** Photos in `family_photos/` are reproduced
  under family-private rights; do not upload to Commons or link as
  `image (P18)` until rights are explicitly cleared.

---

## After mint — wire-up checklist

```
[ ] QID captured and saved in IDENTIFIERS_KIT.md §4.4 sed command
[ ] DOI added to Wikidata as P356 (after Zenodo mint)
[ ] P973 (described at URL) → /  (English entry point)
[ ] P973 (described at URL) → /de/  (German entry point)
[ ] Sitelink added: en.wikipedia.org / de.wikipedia.org — only if
    a Wikipedia article is ever written. Currently neither exists.
[ ] In /about.html Person JSON-LD for the *site*, add a
    `sameAs: https://www.wikidata.org/wiki/{QID}` for Charles in
    the article's `mainEntity` block (separate from the author
    Person blocks).
[ ] In /cast.html (Charles's people-page), add a "Wikidata: {QID}"
    line under the dossier header.
```

---

*Last updated: 9 May 2026. See `IDENTIFIERS_KIT.md` for the master
mint workflow and the sed commands that wire the resulting IDs into
the site.*
