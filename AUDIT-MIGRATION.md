# AUDIT-MIGRATION — inline-style purge + .tile/.callout consolidation

**Started:** 16 May 2026
**Owner:** design-system pass
**Goal:** Retire ~3,462 lines of `assets/dark-mode.css` overrides by deleting
the underlying inline `style="background:#…"` attributes and the per-section
`.tile` / `.callout` zoo that forced those overrides to exist in the first
place. Estimated reduction once migration completes: **~1,500 lines** off
dark-mode.css.

> Do **not** delete anything from `assets/dark-mode.css` in this pass.
> Each override block can only be removed *after* every page that depended on
> it has been migrated. Removing too early breaks pages still in the queue.

---

## 1. New canonical classes (added to `assets/theme.css`)

All classes read from CSS custom properties, so dark-mode.css re-binding the
tokens automatically inverts the surface. **No new dark-mode overrides should
ever be written for these classes** — fix the token, not the class.

### Background utilities

| Class | Token | Intent |
|---|---|---|
| `.bg-page` | `--bg-page` | Page-level neutral surface. |
| `.bg-card` | `--bg-card` | Default card / panel background + light border. |
| `.bg-card-tint` | `--bg-card-tint` | Cream-tinted variant of card (used inside heroes, hypothesis blocks). |
| `.bg-elevated` | `--bg-elevated` | Slightly higher elevation (modals, dropdowns). |
| `.bg-deep` | `--bg-deep` | Deep ink surface for hero strips, with `--text-on-dark`. |
| `.bg-gold-tint` | `--bg-card-tint` + `--brand` border | Brand-gold-cast highlight pill (e.g., the "KONZEN" inline pill). |
| `.bg-civilwar-tint` | `--section-civilwar-t` / `--section-civilwar` | Oxblood tint + accent. |
| `.bg-immigration-tint` | `--section-immigration-t` / `--section-immigration` | Prussian-blue tint. |
| `.bg-germany-tint` | `--section-germany-t` / `--section-germany` | Hessian green tint. |
| `.bg-charles-tint` | `--section-charles-t` / `--section-charles` | Copper tint. |
| `.bg-schrader-tint` | `--section-schrader-t` / `--section-schrader` | Sepia tint. |
| `.bg-confirmed-tint` | `--bg-card-tint` / `--status-confirmed` | Confirmed-status surface. |
| `.bg-open-tint` | `--status-open-t` / `--status-open` | Open-question surface. |
| `.bg-eliminated-tint` | `--status-eliminated-t` / `--status-eliminated` | Eliminated-candidate surface. |
| `.bg-active-tint` | `--status-active-t` / `--status-active` | Active-investigation surface. |

### `.tile` primitive

```html
<a class="tile" data-section="germany" href="…">
  <div class="tile__label">1 · Hessian origins</div>
  <div class="tile__title">Where Charles came from</div>
  <div class="tile__sub">Trendelburg, Deisel, Friedrichsfeld…</div>
</a>
```

- Flex column, `var(--bg-card)`, `var(--border-light)` outline, 4px
  `border-left` accent that defaults to `var(--brand)` and switches via the
  `[data-section]` attribute (`civilwar | immigration | germany | charles |
  schrader`).
- Hover: `translateY(-1px)` + `var(--hover-shadow)` + darkened accent.
- Inner BEM-style children: `.tile__label`, `.tile__title`, `.tile__sub`.
- Modifier `.tile.tile--keystone` — heavier 2px outline + status-open accent
  for "key evidence" tiles.

### `.callout` primitive

```html
<div class="callout callout--milestone">
  <span class="callout__label">★★★ Project conclusion</span>
  <h3 class="callout__title">Charles's surname is Konzen.</h3>
  <p class="callout__body">…</p>
</div>
```

- Block, `var(--bg-card-tint)` background, 4px `border-left` accent.
- Children: `.callout__label` (uppercase eyebrow), `.callout__title` (Iowan Old
  Style 1.05rem), `.callout__body` (line-height 1.6).
- Variants:
  - `.callout--confirmed` → `--status-confirmed` accent.
  - `.callout--open` → `--status-open` accent + status-open-tint background.
  - `.callout--milestone` → `--section-civilwar` (oxblood) accent + tint
    background. **This is the canonical replacement for `.whats-new`.**

---

## 2. Highest-leverage remaining inline-style sites

Each row is one or more inline `style="background:#…"` attributes that should
be deleted and replaced with the listed utility/primitive. Ordered by impact
(number of duplicate sites the migration kills, dark-mode breakage severity).

| # | File / Line | Inline pattern | Replace with |
|---|---|---|---|
| 1 | `index.html:1991` (charles-portrait-figure) | `style="…background:linear-gradient(140deg, #fffaee, #f6ebd2); border:1px solid #b48a3a; border-left:5px solid #b48a3a; …"` | `<figure class="callout bg-gold-tint">` + drop gradient. ✅ done |
| 2 | `index.html:2007-2015` (two-block punchline hero, "What we know" + "Where the search stands") | gradient + section-coloured border-left, repeated 2× | `<div class="callout bg-charles-tint">` and `<div class="callout bg-immigration-tint">`. ✅ done |
| 3 | `index.html:2019` (Browse People pill button) | `background:#fffaf0; border:1px solid #d8b366; border-left:4px solid #d8b366;…` | `<a class="pill" data-section="charles">` (new `.pill` primitive added to theme.css). ✅ done |
| 4 | `index.html:4409` (`.card`) | `style="background:#fffaf0; border:1px solid #d8c8a8;"` | Delete inline; `.card` already has these defaults — remove the redundant attribute. ✅ done |
| 5 | `index.html:8589, 8595, 8601` (three nav-grid cards in the Cast section) | `background:#fffaf0; border:1px solid #d8c8a8; border-left:4px solid …` | `<div class="tile" data-section="immigration|charles|germany">`. ✅ done (these are actually the citation cards at lines 8556/8562/8568 in the "How to cite" section; migrated to `.tile` with immigration/charles/germany section accents matching the original blue/gold/green) |
| 6 | `family_pages/fam-quentin.html:149` (`.ff-section` opening, eliminated-candidate frame) | `style="background:#fbeef3; border:2px solid #8a4a4a; border-radius:6px; padding:1.2rem 1.4rem; …"` | `<section class="callout bg-eliminated-tint">`. Same pattern repeats across all `fam-*.html` `.ff-section` blocks. |
| 7 | `family_pages/fam-quentin.html:230` (table thead) | `style="background:#e8d8a8; …"` | `<thead class="bg-card-tint">` — and consider a `.tbl thead` global rule so we never paint table headers inline again. |
| 8 | `people/josephine-von-delian.html:367, 430, 448, 460, 480, 504` (six evidence-card variants) | `background:#fff4e8 | #e8f0d6 | #fdf3d8 …` + section border-left | Standardize on `<div class="callout callout--confirmed|--open">` or `.callout bg-germany-tint` etc. Same pattern repeats across all `people/*.html`. |
| 9 | `immigration/bremen-reconstruction.html:476, 662, 693, 727, 778, 814, 853, 896` (eight `.log-entry` rows) | `background:#fef2f2 | #f0f8e8 | #fdfaf3` + matching border-left-color | Drop the inline styles; restyle `.log-entry` once in the page's `<style>` to use tokens, OR migrate each to `<div class="callout bg-eliminated-tint|bg-germany-tint|bg-card-tint">`. |
| 10 | `index.html:2035` (KONZEN highlight pill, `#fff2c2`) | inline `<span style="background:#fff2c2; …">` | `<span class="bg-gold-tint">` (the pill version added in this pass). ✅ done (migrated by the prior home-page rewrite; verified at line 2011 — span carries `class="bg-gold-tint"` with only layout `padding`/`border-radius` remaining inline) |

A grep against the whole repo (excluding `_deploy_netlify/`) shows **~83
inline `style="background:#…"` occurrences across 30 source files**. The 10
rows above account for roughly 60% of them; the rest are one-off cards in
`children/*.html` and `research_logs/*.html` that follow the same shapes as
rows 8–9.

To audit progress later:

```sh
grep -rn 'style="background:#' \
  --include='*.html' \
  --exclude-dir=_deploy_netlify \
  .
```

---

## 3. Legacy classes pending deprecation

These per-section component classes were the original sin: every section
invented its own variant and dark-mode.css had to write five overrides for
what should have been one rule. Each is replaced by the new canonical
component plus a `data-section` attribute or status modifier.

| Legacy class | Replacement |
|---|---|
| `.ge-tile` | `.tile[data-section="germany"]` |
| `.ca-tile` | `.tile[data-section="charles"]` |
| `.cw-tile` | `.tile[data-section="civilwar"]` |
| `.im-tile` | `.tile[data-section="immigration"]` |
| `.schrader-tile` | `.tile[data-section="schrader"]` |
| `.person-card` | `.tile[data-section="charles"]` (default) or `.tile` if person isn't section-scoped |
| `.whats-new` | `.callout.callout--milestone` |
| `.smoking-gun` | `.callout.callout--milestone` (oxblood accent reads as the same "big finding" semantic) |
| `.konsen-feature` | `.callout.callout--confirmed` + `.bg-charles-tint` |
| `.friedrich-callout` | `.callout` (default brand accent) |
| `.peter-quote` | `.callout.callout--open` |

**Migration order matters.** Leave the legacy class on the element during
transition (`<div class="callout callout--milestone whats-new">`) so the old
dark-mode override still applies until every instance is migrated. Only then
strip the legacy class and delete the matching block in `dark-mode.css`.

---

## 4. Progress checkpoint (16 May 2026)

Migrated this pass:

- `index.html` — four "Start here" tiles (lines 1965-1986). Old: 4× ~250-char
  inline gradient/border duplicate. New: `<a class="tile"
  data-section="…">` with `.tile__label / __title / __sub` children. Zero
  inline `style` on the four cards.
- `index.html` — both `.whats-new` boxes (lines 2031, 2041). Old: inline
  `background:#fce8d6; border:2px solid #c8714a; border-left:6px solid
  #a3441f;`. New: `<div class="callout callout--milestone whats-new">` —
  legacy `whats-new` class retained for the migration window.

Net inline-style attributes removed in pass 1: 6 elements × ~250 chars ≈
~1.5 KB of duplicate inline styling.

### Pass 2 (16 May 2026, evening) — rows 1–5 + 10

- **Row 1 — `index.html:1991` charles-portrait figure.** Old: inline
  `linear-gradient(140deg, #fffaee, #f6ebd2)` + dual `#b48a3a` borders.
  New: `<figure id="charles-portrait-figure" class="callout bg-gold-tint" style="display:grid; …">` —
  only the grid layout (auto · 1fr, gap, align-items) stays inline; all
  color / border / padding now flows through `.callout` + `.bg-gold-tint`
  via the token chain.
- **Row 2 — `index.html:2014-2024` punchline-hero pair.** Two side-by-side
  inline-gradient blocks ("What we know about Charles" / "Where the search
  stands today") replaced by `<div class="callout bg-charles-tint">` and
  `<div class="callout bg-immigration-tint">` with `.callout__label`
  eyebrow + `.callout__body` paragraph. Inline link colors on the
  "→ Key Evidence tab" anchor also dropped — the tinted callout body
  inherits the correct link colour.
- **Row 3 — `index.html:2161` Browse People pill.** Added a new
  `.pill` + `.pill[data-section="…"]` primitive to
  `assets/theme.css` (the `.bg-card` / `--brand` / section-token chain
  applies automatically; dark mode requires no new override). The button
  is now `<a class="pill" data-section="charles" href="#people" …>`.
- **Row 4 — `index.html:4360` `.card`.** Just deleted the redundant
  `style="background:#fffaf0; border:1px solid #d8c8a8;"` — `.card`
  already paints those tokens.
- **Row 5 — `index.html:8556 / 8562 / 8568` three "How to cite" cards.**
  Each migrated to `<div class="tile" data-section="…">` + `.tile__label`
  eyebrow; the inner `<code>` block keeps its monospace style inline (it
  is genuinely format-specific). Section accents: NGSQ → immigration
  (blue, matching the original `#4a76c8`), Chicago → charles (copper,
  replacing original brand-gold `#d8b366` per the migration spec), plain
  prose → germany (green, matching `#5a8a4a`). Note: the migration doc
  said line numbers 8589/8595/8601 and "Cast section"; the actual block
  is in the "How to cite" section (citations, not Cast nav cards).
- **Row 10 — `index.html:2011` KONZEN inline pill.** Already migrated by
  the pass-1 home-page rewrite: `<span class="bg-gold-tint" style="padding:0.05rem 0.4rem; border-radius:3px;">KONZEN</span>`.
  Verified only. Inline `padding` + `border-radius` left in — these are
  the pill-shape layout, not colour.

CSS additions this pass: `.pill` + 5 section variants in `assets/theme.css`
(roughly 26 lines).

Inline-style audit (strict `style="background:#"` prefix pattern) in
`index.html`:

- Baseline (`_deploy_netlify/index.html` mirror, untouched): 9 occurrences.
- After this pass (`index.html`): **5 occurrences** — all five are the
  consecutive `mt-tight` callout paragraphs at lines 2560-2568 in the
  sponsor-reconciliation block (May 2026 reconciliation, "Charles
  immigrated alone" thread). They form one visual unit and should be
  migrated together in a future row; the cleanest replacement is one
  `<div class="callout bg-eliminated-tint">` wrapping all five
  paragraphs, or a `.callout--multiline` variant.

`background:linear-gradient(` occurrences in `index.html`: baseline 18 →
after this pass **15**. The three killed were row 1 and row 2's two
gradients.

### Pass 3 (16 May 2026, late evening) — rows 6 + 8 sweep

Hit the three sub-directories called out in the previous pass as
next-leverage. File-by-file:

**people/ (15 files, ~40 inline-bg attrs removed):**

- `josephine-von-delian.html` — 6 evidence-card sites + 1 verbatim
  monospace `<p>`. Routed to `callout--confirmed` (sage-green evidence
  panels, 3 sites), `bg-charles-tint` (Charles-side keystone baptism +
  open-question, 2 sites), `bg-gold-tint` (deep-search panel, 1 site),
  `callout--open` (Detjen alternative, 1 site).
- `amalia-muenke.html`, `bertha-barbara-kreichelt.html`,
  `frederick-pillmann.html` — 1 site each: single-pattern
  `#fff4e8` / orange → `callout bg-charles-tint`.
- `adam-herweck.html` — 6 sites. Two Charles-tint find boxes,
  two schrader-tint child-baptism records, one `callout--milestone`
  for the smoking-gun CSR confirmation, one gold-tinted blockquote.
- `auguste-kreichelt.html` — 2 evidence cards + 2 inline pills.
  Marriage & death records → `callout bg-gold-tint`; pills →
  `bg-gold-tint` / `bg-civilwar-tint`.
- `christina-hahl.html`, `katherine-misch.html` — 1 evidence card + 1
  pill each, plus 1 outer section in katherine. Same gold-tint pattern.
- `jacob-reck.html` — 2 cards: obituary → `bg-gold-tint`,
  caveat-note → `callout--open`.
- `john-heitzenberger.html` — 2 outer sections: open-question + gold
  documentary-evidence panel.
- `theodore-gottlob.html` — 2 outer sections: `bg-charles-tint`
  (two-ancestor convergence) + `bg-gold-tint` (Civil War service).
- `maria-agnes-goetz.html` — 1 evidence card (Charles-tint) + 2
  default cards (`bg-card-tint`).
- `wilhelmina-ebeling.html` — 3 cards: 2× `callout--confirmed`,
  1× `callout--open` (superseded-hypotheses panel).
- `christian-meyer.html`, `dr-charles-hess.html`, `erwin-spraul.html`,
  `michael-nolan.html` — affidavit/obituary blockquotes →
  `callout bg-gold-tint` (recurring pattern across 4 pension-witness
  pages).

**children/ (7 files, ~12 inline-bg attrs removed):**

- `auguste.html`, `bertha.html`, `erwin-carl-konsen.html`,
  `friedrich-wilhelm.html`, `josephine-maria.html`,
  `katherine-carolina.html`, `louise.html` — uniform pattern:
  `evidence-card` + inline `#fffaf0 / #d8b366` →
  `callout bg-gold-tint`.
- `auguste.html` also: 1× `#fce8d6` death-record pill → `bg-civilwar-tint`.
- `katherine-carolina.html`, `auguste.html`, `bertha.html` —
  inline `#fff2c2` smoking-gun-pair pills → `bg-gold-tint`.
- `friedrich-wilhelm.html` — 2 outer sections (1866 timeline +
  competing-readings) → `callout--milestone` (oxblood) +
  `callout bg-gold-tint`.
- **Intentional remainders:** two `surname-pill` `#d8b366` brass-gold
  stamps on `erwin-carl-konsen.html` lines 170, 179. These are
  single-character emphasis stamps, not surface containers — left
  inline. A `.surname-pill--gold` modifier isn't worth adding for two
  sites.

**family_pages/fam-* (6 files, ~22 inline-bg attrs removed):**

- `fam-quentin.html` — 14 sites cleaned (all of §2 row 6 + row 7).
  Eliminated-frame opening (`#fbeef3` + `#8a4a4a`) →
  `callout bg-eliminated-tint`. The 13 `.ff-section` blocks routed
  by section accent: `bg-germany-tint` (Hessian content),
  `bg-charles-tint` (Charles candidates), `bg-eliminated-tint`,
  `bg-immigration-tint` (Cincinnati lead), `bg-gold-tint`,
  `bg-card-tint`. The `<thead style="background:#e8d8a8">` →
  `<thead class="bg-card-tint">` per row 7. Plus 5 verdict-paragraph
  mini-callouts + 2 blockquote variants migrated to the matching
  `bg-*-tint`.
- `fam-konze.html` — the Kontze-FS-family wrapper → `bg-card`.
- `fam-herwig.html` — outer email-card → `callout bg-gold-tint`; two
  net-of-finding paragraphs → `callout bg-charles-tint`. Remaining
  inline styles on lines 157, 171-178 are functional (display:block
  on `<a>`, display:none on fallback placeholders, dashed-border
  styling) and don't fit the utility-class shapes; left in place.
- `fam-grandjot.html` — 3 net-of-finding paragraphs →
  `callout bg-charles-tint`.
- `fam-branson.html` — 1 surname-change note → `callout bg-germany-tint`.
- `fam-person.html` — 1 candidate-eliminated note →
  `callout bg-charles-tint`.

**Patterns observed (not anticipated by the audit doc):**

1. The audit-doc grep `style="background:#'` misses any site where
   `border-left:` (or any other property) precedes `background:` in
   the inline style string. The more-inclusive regex
   `style="[^"]*background:#'` surfaces ~3× more occurrences. Two
   children/friedrich-wilhelm sections and most fam-quentin
   `.ff-section`s had this ordering and were initially missed.
2. Inline `<span>` "★ KEY EVIDENCE" / "★ BRASCHLER SMOKING-GUN PAIR"
   pills with `background:#fff2c2` (or `#fce8d6`) recur across 6+
   children/people files. They were partially migrated by swapping the
   background portion for a `bg-gold-tint` / `bg-civilwar-tint` class
   while keeping the padding/radius/font inline (the `.bg-*` utility
   doesn't cover pill geometry).
3. Affidavit-quote blockquote `<blockquote style="…border-left:3px
   solid #d8b366; background:#fffaf0; font-style:italic;">` is a
   recurring pattern across 5 people pages (pension-witness
   affidavits). All standardized to `callout bg-gold-tint`.
4. Two visually-similar `#fffaf0` shapes need different treatment:
   with `border:1px solid #d8c8a8` it's the neutral `.bg-card`;
   with `border:1px solid #d8b366; border-left:4px solid #d8b366` it's
   the gold-cast variant → `callout bg-gold-tint`.

### Global inline-style count

| Date | Count (strict `style="background:#`) | Files |
|---|---|---|
| Migration start (audit-doc baseline) | ~83 | ~30 |
| End of Pass 2 (early 16 May) | ~80 | ~30 |
| **End of Pass 3 (late 16 May)** | **~52 working-tree only** | **~22** |

The repo-wide count via the *inclusive* regex
`style="[^"]*background:#'` is **88 working-tree** (was 254 pre-sweep
including archive mirrors; the count above excludes
`_deploy_netlify/`, `_archive/`, and `_archive_pre_audit_fixes/`).

Pass 3 removed ~74 inline-style attributes across 28 files (people 15
+ children 7 + family_pages 6). Remaining ~88 sites are concentrated
in out-of-scope directories from this pass: `immigration/`,
`research_logs/`, `germany/`, `charles_america/`, `sources/`,
`correspondence/`, `notes/`, `towns/`, plus the still-open
`index.html` sponsor-reconciliation block (5 mt-tight paragraphs at
2560-2568), `Family_Tree_All_Families.html`, `errata.html`,
`peter_charts_download_checklist.html`,
`Kontze_Family_Tree_Graphic.html`.

Recommended next steps (descending leverage):

1. Convert the five consecutive `mt-tight` sponsor-reconciliation
   paragraphs in `index.html` (lines 2560-2568) into a single
   `bg-eliminated-tint` callout wrapper — clears the last five
   `style="background:#"` from index.html in one edit.
2. Sweep `immigration/bremen-reconstruction.html` (8 `.log-entry`
   rows, row 9 of §2).
3. Sweep `research_logs/*.html` and `charles_america/*.html` —
   the same affidavit-blockquote + evidence-card shapes recur.
4. `Family_Tree_All_Families.html` + `Kontze_Family_Tree_Graphic.html`
   each have 4-8 sites; both family-graphic pages.
5. Delete `.whats-new` from `assets/cinematic-spa.css` / `theme.css`
   after the last `.whats-new` instance is gone.
6. Delete the dark-mode override blocks for `.ge-tile / .ca-tile /
   .cw-tile / .im-tile / .schrader-tile / .person-card / .whats-new /
   .smoking-gun / .konsen-feature / .friedrich-callout / .peter-quote`
   — **only after** the people/children sweep is done (now true).
7. Retire the runtime DOM-sweep JS in `germany/konzen-puzzle.html`
   that walks the tree tagging light-bg elements — it becomes
   unnecessary the moment the inline backgrounds it's compensating
   for are gone.

When dark-mode.css drops below ~2,000 lines, do a second audit pass — many
remaining overrides will be load-bearing only because of one stubborn page.
