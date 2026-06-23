# Color & Contrast Audit — Charles Konzen Research

*Audit date: 8 May 2026. WCAG 2.1 AA threshold: **4.5:1** for body, **3:1** for large headings. Ratios computed from the actual hex values in `assets/theme.css`, `assets/cinematic.css`, `assets/dark-mode.css`, `assets/site-nav.css`, and the per-section `_shared.css` files.*

The site has a coherent palette — a single "gilt" gold (#d8b366 / brand), warm paper background (#f6f1e7), and walnut darks for heroes. Most body text is well above AA. The contrast problems cluster around **one specific color**: the brand gilt #d8b366, which is too light to use against the cream paper background or with white text on top. Five distinct patterns are causing the readability complaints.

## Palette inventory

| Token | Light | Dark | Role |
|---|---|---|---|
| `--bg-page` | #f6f1e7 (paper) | #1a1612 (deep walnut) | page background |
| `--bg-card` | #fffaf0 | #24201a | cards |
| `--text-body` | #2c2620 | #e8dfc8 | body copy |
| `--text-strong` | #3a2f1e | #f4ead0 | strong / headings |
| `--text-meta` | #4a3a22 | #c8b896 | small meta |
| `--text-muted` | #6a5a42 | #9c8a6e | italic captions |
| `--brand` (gilt) | #d8b366 | #e6c47a | accents, hover |
| `--brand-dark` | #8a6420 | #d8b366 | default link |
| `--ink-night` (cinema) | — | #14110c | hero/cover backdrop |
| `--ink-paper` (cinema) | — | #ece2cc | hero text |
| `--gilt-deep` | #8a6420 | — | accent on dark |

Section accents (oxblood #a04030, Prussian #3a5a8c, Hessian green #4a6e34, copper #b06820, sepia #6e4818) all pass AA on cream paper — those aren't the problem.

## Findings: what fails

### 1. `a:hover { color: #d8b366 }` — body links become unreadable on hover  ⚠️ critical

Gilt #d8b366 on paper #f6f1e7 = **1.77:1 (FAIL)**. Hovering any body link makes the text nearly invisible against the cream background. This is the single biggest cause of the "hard to read" feeling — every page has body links and every one of them does this.

The pattern is repeated in almost every per-section stylesheet:

- `family_pages/_shared.css:12`
- `research_logs/_shared.css:9`
- `sources/_shared.css:9`
- `children/_shared.css:9` and `:44`
- `people/_shared.css:9`
- `charles_america/_shared.css:9`
- `towns/_shared.css:10`
- `notes/_shared.css:40`
- `assets/cinematic.css:124` (`.map-link:hover`)

### 2. `color: #fff` on `background: #d8b366` — pills, hover-fills  ⚠️ critical

White text on gilt #d8b366 = **1.99:1 (FAIL)**. Affects the "open" status pills, the back-nav button hover, the FamilySearch link hover, and several other "fill on hover" treatments.

Where it lives:

- `.badge.open` and `.summary-card .card-pill.open` — `family_pages/_shared.css:22, :73`, `people/_shared.css:306`, `children/_shared.css:205`
- `a.fsn:hover` — `family_pages/_shared.css:46`, `sources/_shared.css:133`, `research_logs/_shared.css:119`, `people/_shared.css:119`, `children/_shared.css:37`
- `footer.back-nav a:hover` — every section stylesheet (charles_america, family_pages, people, towns, sources, research_logs, children, notes, civilwar, germany, immigration)
- `.page-toolbar a:hover` — `sources/_shared.css:108`, `people/_shared.css:94`, `research_logs/_shared.css:94`

Note: `theme.css` already defines `--status-open: #c87a30` (an amber that does work better with white — 3.34:1, AA-large) and overrides `.badge.open` and `.card-pill.open` to use it later in the same files. But the *earlier* hardcoded `#d8b366` rules are still in cascade order and still apply to many elements (the `.fsn:hover` background fill is the most conspicuous one).

### 3. Cinematic breadcrumb separator — `rgba(216, 179, 102, 0.4)` on `#14110c` = **2.48:1 (FAIL)**

`assets/cinematic.css:1195` — the "›" separator chip in `header.cinema-section-hero .csh__crumbs span`. Small, but technically below AA and visibly faint.

### 4. Cinematic body link hover — `--gilt-deep` (#8a6420) on `#14110c` = **3.52:1 (AA-large only)**

`assets/cinematic.css:1134` — `body.cine-typography main a:hover` sets `color: var(--gilt-deep)`. On the dark hero/cover backgrounds (`#14110c`), this passes AA-large but not AA for body text. The default (non-hover) `border-bottom-color: rgba(216,179,102,0.5)` is fine; it's specifically the hover *text color* swap that's too dim.

### 5. Borderline (passes AA-large only — felt soft, not technically broken)

| Selector / file | Pair | Ratio |
|---|---|---|
| `.site-nav-shared .group-btn::after` (caret arrow) — `assets/site-nav.css:44` | #8a7858 on #2c2620 | 3.49:1 |
| `.site-foot-shared .foot-meta` — `assets/site-nav.css:144` | #8a7858 on #3a2f1e | 3.06:1 |
| `header.site-header.cinema-banner .banner-byline` — `assets/cinematic.css:1521` | rgba(236,226,204,0.5) on #14110c | 4.41:1 |
| `.kfs-pid` (FamilySearch ID badge), `.ft-pid` — `family_pages/_shared.css:198, :316` | #4a76c8 / #c84a76 on #fffaf0 | 4.28–4.30:1 |
| **Dark mode** `--text-muted: #9c8a6e` on `--bg-card-tint: #2c261d` | | 4.47:1 |

These are below AA only by tenths and only on small/decorative text, but if the user is scanning by eye they'll feel washed-out.

## Things that already pass

For completeness — these were checked and are fine, no action needed:

- All body text on paper / card (10:1+, AAA)
- The dark cinematic heroes — H1, lede, sub, eyebrows all 8–14:1
- Site nav top-level buttons (#c8b896 on #2c2620 = 7.65:1)
- Section-accent badges (battery / context) with white text on oxblood/Prussian/Hessian — all AA
- The default link color #8a6420 on paper = 4.75:1 (just over AA)

## Recommended fixes

### Pattern A — replace `a:hover { color: #d8b366 }` with `--brand-dark` (gilt-deep #8a6420)

`#8a6420` on paper = 4.75:1, passes AA. Or for stronger contrast, use `#74420f` (deep copper, 7.38:1 AAA). Same change in 11 files. Keep the dotted underline color as-is so the visual hover signal remains.

```css
/* before */
a:hover { color: #d8b366; }
/* after */
a:hover { color: var(--brand-dark); }   /* or: color: #74420f */
```

### Pattern B — fix `color:#fff` on gilt fills

Two equally good options:

- **Keep gilt background, switch text to ink** — `color: #1f1a14` on `#d8b366` = 8.68:1 AAA. Best preserves the visual identity.
- **Darken the background to match `--status-open` (#c87a30)** for status pills, or to `--brand-dark` (#8a6420 = 5.35:1 AA) for hover fills. Use this if you want to keep white text.

Recommended: ink text on gilt fills (Pattern B-1). One line per file, and the gilt remains the brand color.

```css
/* family_pages/_shared.css:22 */
.badge.open { background:#d8b366; color:#1f1a14; }   /* was color:#fff */

/* family_pages/_shared.css:46 — same idea for fsn link hover */
a.fsn:hover { background:#d8b366; color:#1f1a14; border-bottom-color:#d8b366; }

/* footer.back-nav a:hover everywhere */
footer.back-nav a:hover { background:#d8b366; color:#1f1a14; }
```

### Pattern C — bump cinema breadcrumb separator alpha

```css
/* assets/cinematic.css:1195 */
header.cinema-section-hero .csh__crumbs span {
  color: rgba(216, 179, 102, 0.65);   /* was 0.4 → 4.58:1 AA */
}
```

### Pattern D — lift cinema body link hover toward gilt, not gilt-deep

```css
/* assets/cinematic.css:1134 */
body.cine-typography main a:hover,
body.cine-typography section.page p a:hover,
body.cine-typography section.page li a:hover {
  color: var(--gilt);                  /* was var(--gilt-deep) → 9.47:1 AAA */
  border-bottom-color: var(--gilt);
}
```

This actually reads as "gilt brightens on hover," which matches the visual metaphor of the cinematic theme better than the current "gilt darkens to bronze."

### Pattern E — small bumps for the "borderline" group

```css
/* assets/site-nav.css:44 (caret) */
.site-nav-shared .group-btn::after { color: #a89878; }   /* 5.29:1 AA */

/* assets/site-nav.css:144 (footer meta) */
.site-foot-shared .foot-meta { color: #a89878; }         /* 4.63:1 AA */

/* assets/cinematic.css:1521 (banner byline) */
header.site-header.cinema-banner .banner-byline {
  color: rgba(236, 226, 204, 0.6);                       /* was 0.5 → 5.80:1 AA */
}

/* assets/dark-mode.css:27 (dark-mode muted) */
--text-muted: #b89c70;                                    /* was #9c8a6e → 5.73:1 AA on tint */
```

### Pattern F — PID badges (optional, nice-to-have)

`.kfs-pid` and `.ft-pid` are tiny monospace IDs that are decorative more than they are content. They pass AA-large which is technically the correct threshold for ≥18.66px non-bold or ≥14px bold — but `.ft-pid` is 0.68rem (~10.9px) so should hit 4.5:1.

```css
.kfs-pid { color: #2c4a72; }                /* was #4a76c8 → 8.66:1 AAA */
.kfs-card.female .kfs-pid { color: #933154; } /* was #c84a76 → 7.19:1 AAA */
```

## Priority for fixing

1. **Pattern A** (link hover gilt → gilt-deep) — affects every single page; biggest visible improvement; 9 one-line edits across the section stylesheets plus one in `cinematic.css`.
2. **Pattern B** (white-on-gilt pills/hovers) — globally visible; ~20 small edits across the per-section stylesheets.
3. **Pattern C & D** (cinema crumbs separator + cinema link hover) — only on cinema-styled pages; 2 edits in `cinematic.css`.
4. **Pattern E & F** (caret, footer meta, banner byline, dark-mode muted, PIDs) — polish; can be batched later.

If you want to push the whole fix through, the changes are mechanical and span ~15 files — happy to apply them next.
