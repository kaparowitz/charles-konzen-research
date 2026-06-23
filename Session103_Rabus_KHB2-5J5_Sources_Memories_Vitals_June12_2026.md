# Session 103 — Georg Christoph Rabus (FamilySearch KHB2-5J5): Sources, Memories, Vitals

**Date:** 12 June 2026
**Person:** Georg Christoph Rabus, 28 Apr 1805 Gotha – 9 Apr 1872 Gotha (FS ID **KHB2-5J5**)
**Line:** Rabus generation 10 (Gotha branch; see `Rabus_Line_Verification_Assessment_June11_2026.md`)

## Objective (per Jed)
Find birth/christening, death, and marriage records; attach as sources; add the
record downloads to the Memories section; update the Vitals section including burial.

## Starting state
KHB2-5J5 had **0 sources, 0 memories**. Birth (28 Apr 1805 Gotha) and Death
(9 Apr 1872 Gotha) were present; Christening and Burial were blank. Marriage to
Auguste Friedericke Therese Merbach (KZ39-L89) recorded as 17 Nov 1833, no place.

## Records located
FamilySearch **indexed** record search returned nothing for Gotha/Thuringia
(thin coverage). FamilySearch **Full-Text** search on "Georg Christoph Rabus"
returned three LDS *Family Group Records Collection, Archives Section* sheets,
all compiled from the Lutheran church-book records of Gotha (informant Franz
Lohse, Gotha, Leesenstr. 7). These are the primary documentary sources currently
digitized for this family.

| Record | ARK | Film / image | What it documents |
|---|---|---|---|
| His own family sheet (husband) | 3:1:3QS7-L97M-P9K8-4 | film 7000424, img 1196 | b. 28 Apr 1805, m. 17 Nov 1833, d. 9 Apr 1872 Gotha; parents; 7 children |
| Parents' family sheet (he = child 3, marked X) | 3:1:3QS7-L97M-P9KD-F | film 7000424, img 1212 | his birth; father Joh. Wolfgang Martin Rabus, mother Joh. Dorothee Starkloff |
| Merbach (wife's parents') sheet | 3:1:3QSQ-G97M-NPYZ | film 5895666, img 223 | marriage 17 Nov 1833 to Auguste Friedericke Therese Merbach (b. 3 Dec 1808 Gotha) |

Note: these sheets give **no separate burial date** and no standalone christening
date — only birth/marriage/death events. So burial was recorded as place-only.

## Actions completed
1. **Sources (3 attached)** — all three sheets attached to KHB2-5J5 with full
   titles (film + image), descriptive notes, and per-attachment "reason"
   statements. After attaching, corrected the Merbach sheet film number from a
   mistaken 7000426 to the correct **5895666** (img 223).
2. **Memories (3 uploaded)** — full-resolution JPEGs of all three sheets uploaded
   to the Memories tab (Make Public). Filenames:
   - `FGRC_GeorgChristophRabus_AugusteMerbach_FamilyGroupRecord_film7000424_img1196.jpg`
   - `FGRC_RabusParents_JohannWolfgangMartinRabus_Starkloff_film7000424_img1212.jpg`
   - `FGRC_MerbachFamily_Marriage_GeorgChristophRabus_17Nov1833_film5895666_img223.jpg`
3. **Vitals updated**
   - **Burial** added: place **Gotha, Sachsen-Coburg-Gotha, Thüringen, Germany**
     (standardized to Gotha, Saxe-Coburg and Gotha, 1871–1920). Date left blank —
     not documented in the sources. Reason statement cites the attached sheets.
   - **Marriage place** added to the couple relationship: **Gotha,
     Sachsen-Coburg-Gotha, Thüringen, Germany**, 17 Nov 1833, reason cites the two
     family-group sheets that record the marriage.
   - Birth and Death already correct; no christening date available to add.

## Image-capture technique (for future sessions)
The FGRC viewer's in-app download endpoint did save full-res JPEGs to
`peter_charts/` automatically (named by ARK, e.g. `3QS7-L97M-P9K8-4.jpg`,
3729×2201). When the endpoint is slow, the DeepZoom tiles can be reassembled:
full resolution is **level 12** (256-px tiles), base URL
`https://sg30p0.familysearch.org/.../<ARK>/image_files/12/<col>_<row>.jpg`.
Level 9–11 are lower-res; level 13 returns 404. Tiles can 503 under load — retry
with backoff.

## Result
KHB2-5J5 now shows **Sources (3)**, **Memories (3)**, Burial populated, Marriage
place populated. Quality score improved from the prior "no sources attached"
flag. Originals saved in `peter_charts/`.
