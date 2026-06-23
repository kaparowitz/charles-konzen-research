# Register 220093 — Session 6: CLUSTER G BREAKTHROUGH (April 13, 2026)

**Session Date:** April 13, 2026 (later in day, after session 5 blocker)
**Register:** Archion Register #220093 (Trendelburg Kirchenbuch 1708–1772)
**Major result:** Navigation unblocked; **page 48 read**; critical new Kontze family-structure evidence found.

---

## 1. Navigation Breakthrough

The Session 5 blocker is **solved**. The Archion viewer uses jQuery with delegated `change` handlers on its page `<select>`. Synthetic DOM events do not trigger them, but **jQuery's `.trigger('change')` does**. The reliable navigation recipe is:

```javascript
const $ = window.jQuery;
$('select').val(String(targetIndex)).trigger('change');  // targetIndex = imageNumber - 705
$('.zoom-in').trigger('click');   // zoom via jQuery handler
$('.zoom-out').trigger('click');
$('.btn.fullscreen:not(.d-none)').first().trigger('click'); // enter fullscreen
```

With this, any image in the register can be opened and zoomed end-to-end from Claude without manual user intervention.

---

## 2. CLUSTER G BREAKTHROUGH — Page 48 (Image 733)

### 2.1 The image

Image 733 is NOT a TOC separator (prior Session 4 assumption was wrong). It is a real manuscript spread:
- **Left page: page 48**, year **1722** (page number "48" clearly visible top-left; "1722" as header).
- **Right page: page 49**, year **1723** (header "1723" visible; page otherwise blank apart from that header — suggests 1722 fiscal year ended with few entries and scribe reserved a fresh page for 1723).

Page 48 contains only ~7–8 lines of entries (1722 had few Trendelburg baptisms).

### 2.2 What page 48 actually says (key transcription)

After a second pass with aggressive zoom + pan (jQuery `.zoom-holder` CSS `left`/`top` manipulation), the page reads with the following clear elements (approximate; Kurrent paleography, may need native-reader verification):

> **"48"** (page number, top-left)
> **"1722"** (year header, top-center)
>
> — Entry 1 (date: "16. Marty" = March 16, 1722): [child name?], ... Mutter Catharina [?]...
>
> — Entry 2: "... als Christian Ludwig Richards, uxor [wife] Henricus Richards, des Müllers, Margaretha **Kontzen**, der Gevatter H. Ludwig..."
>
> — Entry 3 (the critical Kontze entry):
>   **"... Andreas Kontze, des Nies Kontzen Sohn, die Mutter Catharina ..."**
>   Next line: **"Pate [possibly 'Flatte' — likely 'Pate'] Andreas Kontze"** = **"Godfather Andreas Kontze"**
>
> — Entry 4 (date: "31."): "... geboren [...], Eva Rosina, des Conrad Engels Tochter, die Mutter..."
> Continuation: "... Sophia Richards, geboren [...] 12. uhr [...]"
> "... ein [something] vater [ist] Petrus Rosenthal, gebetter"
> "... Henricus Schaub, [...] Vater gewesen"
>
> — Entry 5 (tail): "... Gertrand geb. Kotha, ein Gebatterin [name]"
> "... Hoff [...] uxor, die Mutter pfleg[ter] Kindes..."
> **"nach Elisabeth"** (closing — likely "named after Elisabeth")

### 2.3 Why this rewrites the family tree

The phrase **"Andreas Kontze, des Nies Kontzen Sohn"** translates literally as **"Andreas Kontze, son of Nies Kontze."** This is unambiguous genitive construction ("des X [genitive] Sohn" = "the son of X").

**Double-Andreas observation:** On the very next line the word **"Pate"** ("godfather") appears before a second reference to **"Andreas Kontze"**. This indicates two different Andreas Kontzes in the same entry: the father (Gen 1, son of Nies) and the godfather (almost certainly Gen 0 — Andreas Contze Sr., the patriarch). If this reading is correct, it **directly proves Andreas Sr. was still alive in March 1722** and attending his grandchild's baptism, while also distinguishing the two Andreases definitively.

**Implication:** Within Trendelburg, there is an Andreas Kontze who is the SON of Nies (Dionysius) Kontze Senior — i.e., a **Generation 1** Andreas Kontze (grandson of Andreas Contze Senior).

This potentially means the "Andreas Junior" who appeared in Session 3 on page 39 (1719, "Contzy" cluster) is actually **Nies's son, not Andreas Senior's son**. If that is right, the Generation 0 Kontze patriarchs are:

- **Andreas Contze Senior** (patriarch, b. pre-1680)
    - **Arnold Philipp Kontze** (b. 1708, confirmed son per image 709)
    - **Nies / Dionysius Kontze Sr.** (generation 0)
        - **Andreas Kontze** (Gen 1 — this new finding) — appears in 1722 entry, has wife Catharina
        - **Anna Gertrud Kontze** (Gen 1, b. ~1745 per baptism index) — still to be located
    - **Joan Henrif / Johann Henrich Kontze** (generation 0)
    - (possibly more)

The earlier assumption that Nies and "Andreas Junior" were brothers must now be **treated as unverified**. The 1719 "two Andreas" scene on page 39 might be Andreas Sr + his grandson Andreas (not Andreas Sr + a second son Andreas Jr).

### 2.4 Margaretha Kontze
"Margaretha Kontzen" also appears on page 48 line 2, described in connection with "des Müllers" (the miller). She may be:
- A wife of one of the Kontze men (the miller's wife), OR
- The miller's daughter who became a Kontze, OR
- A Kontze daughter married to the miller.

Needs clarification on next read; but she is a new Kontze female on record.

### 2.5 Catharina
"die Mutter Catharina" — Catharina is the mother of the child baptized in this entry. If "Andreas Kontze, des Nies Kontzen Sohn" is the father, then **Catharina is Gen-1 Andreas's wife**. Her maiden name is not given in the visible fragment — likely truncated by column width.

---

## 3. Cluster N Re-examination — Image 765 (November–December 1745, January 1746)

Session 4's tentative "Dreas Kontea von Zeylitz" is **confirmed and corrected**. Right page of image 765 clearly reads:

> **"[An]dreas Kontzen von Zeyhl"** — serving as godparent in a November 1745 baptism.

The place name is **Zeyhl** (not Zeylitz). Zeyhl is a separate village/hamlet — likely a nearby rural parish. This is a **new Kontze geographic branch outside Trendelburg proper**.

Andreas Kontzen *von Zeyhl* is potentially:
- The same Gen-1 Andreas Kontze (son of Nies) who had moved to Zeyhl by 1745, OR
- A cousin of the Trendelburg Kontzes whose family lived in Zeyhl from earlier.

The 1746 header "ANNUS 1746" appears lower on the right page; January 1746 entries begin immediately below.

Also visible on left page (late 1745): "Lucia Cornelgen von Körbeke" — Körbeke (another nearby village) also has a family link by marriage/godparent relation.

---

## 4. Images 764 & 766 — Anna Gertrud Kontze NOT found

Scanned both images at high zoom. Anna Gertrud Kontze baptism is **not visible on 764 or 766**. Either:
- The baptism-index page number (112) is inaccurate, OR
- She was baptized in a different village register, OR
- Her entry is on page 113 or another nearby image we haven't opened.

**Notable incidental find on image 766 (left page):** a godfather list including **"Philipp Uffelmann, Jonas Bauman, Christian Thiele, Jodar Henrich Temme"** — the Uffelmann family (godfathers of Arnold Philipp Kontze in 1708) remains socially intertwined with Kontze and allied Trendelburg families in the 1740s. Continuity over ~40 years.

---

## 5. Updated family-tree hypothesis

**Revised working hypothesis:**

```
Andreas Contze SR (b. pre-1680, Trendelburg)
├── Arnold Philipp Kontze (b. 1708 Mar — image 709)
├── Nies (Dionysius) Kontze SR (b. ? — baptism seen image 754, p.90, late 1737 ≠ his own)
│   ├── Andreas Kontze (Gen 1) — wife Catharina — family in 1722 Trendelburg (image 733, p.48)
│   │       └── possibly later moves to Zeyhl by ~1745 (image 765)
│   ├── Anna Gertrud Kontze (Gen 1, b. ~1745/46) — baptism still unlocated
│   └── (other children?)
├── Joan Henrif / Johann Henrich Kontze (Gen 0)
└── (additional Gen 0 siblings if any)
```

**Key open questions:**
1. Where did Andreas Sr come from (his own baptism — predates register; needs earlier Trendelburg register or a neighboring-parish register).
2. Is the Zeyhl Kontze the same man as Gen-1 Andreas?
3. Where is Anna Gertrud Kontze's actual baptism entry?
4. Is there a marriage record for Gen-1 Andreas × Catharina pre-1722 that would give Catharina's maiden name?

---

## 6. Priority Queue — Next Steps

| Priority | Action | Reason |
|----------|--------|--------|
| **1** | Re-read page 48 with higher zoom + pan | Confirm exact transcription of "Andreas Kontze, des Nies Kontzen Sohn" and identify the child's name + date |
| 2 | Cluster U (pages 185, 189) — images ~802/804 | Latest Andreas + Margaretha — may clarify Gen-1 Andreas's later life |
| 3 | Look for **marriage** register section of this kirchenbuch | Find Andreas Kontze (Gen 1) × Catharina marriage |
| 4 | Cluster H (page 68) earliest Philipp | Philipp line context |
| 5 | Search neighboring parish registers for **Zeyhl** (Zehl/Zeell/Zell?) | Locate the Zeyhl Kontze branch |
| 6 | Revisit prior "Andreas Junior" assumption on page 39 (image 728) | Determine if this is Gen-0 son or Gen-1 grandson |

---

## 7. Technical notes for future sessions

- **Navigation recipe confirmed** (§1). Any future session can jump directly to any image by index.
- **Image 733 = page 48 (1722)** — NOT a TOC separator. Earlier calibration note is corrected.
- Revised anchors:

| Image | Page | Year |
|-------|------|------|
| 709 | 1 | 1708 |
| 728 | 39 | 1719 |
| **733** | **48** | **1722** (left) / 1723 (right, mostly blank) |
| 734 | 50 | 1724 end / 1725 start |
| 735 | 52 | 1725 |
| 754 | 90 | late 1737 / 1738 |
| 765 | ~112 | 1745 Nov–Dec / 1746 Jan |

Formula: image ≈ 709 + floor(page/2) — holds without any separator correction now that image 733 is confirmed as a real page.

---

*Sibling docs:*
- `Register_220093_Baptism_Index_Findings_April12_2026.md`
- `Register_220093_Baptism_Page_Visits_April13_2026.md`
- `Register_220093_Baptism_Session3_Findings_April13_2026.md`
- `Register_220093_Baptism_Session4_Calibration_April13_2026.md`
- `Register_220093_Baptism_Session5_NavigationBlocker_April13_2026.md` (superseded)
- This file — **Session 6: Cluster G breakthrough**
