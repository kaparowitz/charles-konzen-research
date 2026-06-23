# Charles Gannsen Research Site — Review & Recommendations

**Reviewer:** Claude · **Date:** 1 May 2026 · **Audience reference:** family/personal use
**Site reviewed:** `Charles_Gannsen_Research_Site.html` (4,766 lines · 455 KB) plus 206 sub-pages across `people/`, `sources/`, `family_pages/`, `notes/`, `civilwar/`, `children/`, `peter_charts/`, `evidence_images/`, `session_notes_docx/`.

---

## TL;DR — what to do first

The site is **already very good** for what it is — better than 95% of family genealogy sites I've seen. The aesthetic is period-appropriate and pleasing, the evidentiary discipline is unusually strong, and the IA is coherent. If you stopped here it would still be a meaningful gift to your family.

The five highest-leverage upgrades, in priority order:

1. **Add a "What's new" banner on the Overview tab** — a single dated paragraph at the top: "Latest finding (1 May 2026): Quentin Pass 6 confirmed Eliza Quentin in 1860 Cincinnati census." This single change does more than anything else to make the site feel alive each time a relative revisits it.
2. **Consolidate sub-page CSS** — `family_pages/` (15 pages) and `notes/` (158 pages) have inline-duplicated styles instead of using a shared stylesheet. One `_shared.css` extraction makes future styling tweaks a 1-file edit instead of a 173-file edit.
3. **Compress and lazy-load images** — 30 MB of images, five of them over 1 MB. A 30-min ImageMagick / `cwebp` pass plus `loading="lazy"` on `<img>` tags will cut page weight ~75%.
4. **Add `<meta description>`, favicon, and `og:image`** — links shared in iMessage/email currently render as bare URLs. A 10-line head-tag addition makes shared links look professional.
5. **Add a unified "Everyone in the story" index** — one page that lists every named person across `people/`, `family_pages/`, and `children/` with a one-line role description and a link to the canonical profile. With 207 HTML files, navigation is the limiting factor.

The remainder of this document expands on these and adds 15 secondary recommendations grouped by dimension.

---

## What the site does well

Before listing problems, let me flag what should not be touched:

- **Period-appropriate visual identity.** The warm parchment palette (`#f6f1e7` base, `#d4a017` gold accents, `#2c2620` ink-dark headers) plus the Iowan Old Style serif make the site read like a 19th-century document on the screen — exactly right for a Civil War / Hessian-emigration story. Many genealogy sites default to either bland Bootstrap or aggressive Victorian pastiche; this hits a balanced middle.
- **The Overview SVG infographic.** The clickable "Hesse → Atlantic → United States" map at the top of Tab I is the strongest single piece of design on the site. It teaches the structure of the investigation in one glance and doubles as nav. Don't change it.
- **Evidentiary discipline.** Every factual claim links back to its primary source by page number — e.g. "→ See Pension Page 22," with the pension viewer providing a page-numbered transcription. This is rare on family sites and approaches the standard of professional genealogical journals.
- **The pension file viewer.** Page-by-page collapsible blocks with both image and transcription, plus a sticky page-number toolbar, is a near-ideal pattern for primary-source presentation.
- **Hash-routed tabs with smart deep-linking.** The JS that intercepts `#fam-*` anchors and switches into the Schrader tab before scrolling is genuinely thoughtful. Most tab implementations break on direct links; this one doesn't.
- **The `.fsn` FamilySearch person-ID inline link style.** Tiny detail — the gold-tinted nowrap badge for FamilySearch PIDs — but it makes those IDs scannable and tactically clickable. Worth keeping.

---

## Findings by dimension

### 1. Information architecture & navigation

**Strengths.** Thirteen-tab top nav now covers the topic space cleanly. Sub-pages use consistent breadcrumb patterns (`← Charles Gannsen Research / People who knew Charles / August Derr`). Cross-tab links inside the main file use the `#tab` hash + JS click handler, which both updates the URL and highlights the destination — that's the right pattern.

**Weaknesses & recommendations:**

- **Civil War tab is overgrown.** It runs ~220 lines of dense HTML with at-a-glance facts, the Kreichelt/Herweck card, a vertical timeline, the Freundburg analysis, and cross-references — all on one scrolling page. Add an in-page mini-TOC at the top of the long tabs (Civil War, Charles in America, Schrader, Family Tree). A simple `<nav class="page-toc">` with anchor links to each H3 would let visitors jump.
- **No site-wide search.** With 207 HTML files, ⌘-F on a single page no longer covers it. Two options: (a) a tiny client-side search using [Pagefind](https://pagefind.app/) — it generates a static index and adds a search box for ~30 KB of JS; or (b) a manually curated "Index of names" page (cheaper, also useful). Given the audience is family, the curated index is the higher-leverage move. Pagefind is a "do this if you ever want it public" upgrade.
- **No "everyone in the story" index.** `people/index.html` covers the 11 pension witnesses + 1 physician. But `family_pages/` has 15 family lines, `children/` has the seven Gannsen children, and `peter_charts/` has the 13 candidate-family charts. There's no single page that lists *every named individual* with a one-line role + link. Recommended: a `/who/index.html` that's just a sortable/filterable table.
- **The "open Tab X" inline-link pattern is inconsistent.** Some links use `<a href="#charles" onclick="...click()">`, others use plain `<a href="#charles">`. The hashchange handler picks both up, but the inline `onclick` versions are strictly redundant after the existing `handleHash()` listener. Cleanup would shave ~20 KB of HTML and remove an inline-script smell.
- **Footer is minimal.** Just a back-to-tab strip. A "site map" footer (small links to all 13 tabs + the major sub-page indexes) gives keyboard/scroll-tired visitors a quick teleport.
- **No "last updated" date per page.** With ongoing research this matters: a relative who reads the site in July won't know whether the Schrader hypothesis is still live. Add a small `<time datetime="...">` near each tab's `<h2>` showing the last-edit date of that tab's content.

### 2. Visual design & typography

**Strengths.** Color, typography, and spacing are consistent and considered. The shared CSS (in `people/_shared.css` and `sources/_shared.css`, which look identical) defines a tight component vocabulary: `.section`, `.kv` table, `.evidence-card`, `.page-block`, `.pill`. The palette holds together across `embed-wrap`, hero gradients, and link styles.

**Weaknesses & recommendations:**

- **Sub-page CSS is duplicated, not centralized.** `sources/_shared.css` and `people/_shared.css` are both 130 lines and substantively identical (the sources version has extras for `.embed-wrap`). Recommend: hoist a single root-level `_site.css` that both directories link via `../_site.css`, and let each directory have a tiny supplementary file only for genuinely-local rules.
- **The 158 pages in `notes/` and 15 pages in `family_pages/` don't link to either shared CSS.** They have inline-duplicated rules. This is the single largest maintainability problem on the site. Future you (or someone editing these in 2030) will thank you for the consolidation.
- **335 inline `style="..."` attributes in the main HTML.** Most are one-offs ("margin-top:0.6rem;" "color:#8a5a14;"), but several patterns recur enough to be classes (`.small-link`, `.muted-meta`, `.tab-cross-ref`). Consolidating shaves both bytes and visual inconsistency.
- **Period-aesthetic accent — mixed metaphors.** The double gold `border-bottom` on the site header is great. The blue (`#4a76c8`) `transcription` border-left and the purple (`#8a7ac0`) `.badge.active` feel like they came from a different design system. Recommend: stay inside the warm-Hesse palette (umber, gold, parchment, ink-dark) and reserve sparing red (`#c84a4a`) and blue only for genuinely semantic distinctions (e.g. transcription vs. original).
- **Headings 4–6 are over-used.** 76 H5s and 15 H6s in one HTML file is a sign that some H4/H5 lists could be re-cast as `<dl>` definition lists or `.kv` tables. Visual hierarchy gets muddier each time you go past H4.
- **Body line-length is fine for desktop (max-width:1100px) but the long-form prose in tabs like Foundation and Schrader could go narrower.** A 1100px column at 16px font is ~95 characters per line — past the 60–75 char optimum for reading. A `.lede`-class paragraph that maxes out around 720px would help, or a `prose` wrapper for long paragraphs.

### 3. Content & evidentiary rigor

**Strengths.** Confidence calibration is unusually honest. Statements like "plausibly named after Charles Gannsen, but the documentary record points the other way" and "the working hypothesis" appear throughout — much better than the typical genealogy site, where speculation hardens into "fact" within two clicks. The verdict tags (`<p class="verdict">`) and the explicit "Doc N / Doc M / Doc O" indexing tying back to the 2020 AncestryProGenealogists journal show research rigor.

**Weaknesses & recommendations:**

- **Confidence levels aren't visually marked.** "Working hypothesis," "confirmed," "eliminated," and "candidate" are scattered through prose. Add a small badge component (you already have `.badge.eliminated`, `.badge.open`, `.badge.active` on family pages — extend it site-wide) that tags every claim card. Three colors only: green = sourced/confirmed, yellow = working hypothesis, red = eliminated.
- **Source-density gradient.** Some statements are densely sourced (the pension-file claims), others are bare ("the chain-migration mechanism"). For family-use this is fine; if you ever publish, every paragraph should end with at least one source link.
- **The "Doc A–O" indexing system from the 2020 journal is mentioned but not consolidated.** Add an `evidence-index.html` page that lists all 15 docs with one row each: doc letter, type, date, who collected it, where the file lives, link to the rendered viewer page if any. This is the kind of artifact a professional-genealogy reviewer would expect.
- **Person-profile depth is inconsistent.** Adam Herweck's profile is 324 lines and reads like a mini-biography; August Derr is 67 lines (good); Henry Stoll is 61 lines (thin); John Heitzenberger is 53 lines (very thin). Either bring the thin ones up to a baseline (a "Quick facts" `.kv` table + "What he swore to" + "Why he matters" trio, even if some sections are a sentence each), or add an explicit "Limited record — what we know" header so the reader knows the brevity is informational, not editorial laziness.
- **No "open questions" inventory at the bottom of each tab.** You have a top-level Open Questions tab (X), but each thematic tab should also end with a small "What's still unanswered in this section" block. This makes the site feel like a living investigation rather than a frozen monograph.
- **Versioned drafts in the root.** 28 versions of `Kontze_Konze_Complete_Family_Reconstruction_*.docx` clutter the working directory. Move them to `notes/_archive/` (or a similar dated folder); keep only the latest visible at root.

### 4. Technical & accessibility

**Strengths.** Semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`). The tab JS is clean and small. ARIA attributes (`aria-label`, `aria-expanded`) appear on the SVG region links and the stat tiles. `lang="en"` is set. Mobile media query at 720px hides Roman numerals and tightens padding.

**Weaknesses & recommendations:**

- **30 MB of images, no compression pass.** `Quentin2.jpg` is 2.5 MB; `neu.jpg` 2.4 MB; `Kontze.jpg` 2.0 MB; civilwar page scans 700–1100 KB each. Run a one-time `cwebp -q 85` (or `mozjpeg -quality 82`) over `peter_charts/`, `civilwar/page_images/`, and the root JPGs. Expect 60–80% size reduction with no visible quality loss. For pages that embed many of these (Schrader tab, Civil War tab), this single change is the largest perceived-performance improvement available.
- **No `loading="lazy"` on `<img>` tags.** Adding `loading="lazy"` to the 31 main-page images and the dozens in sub-pages defers off-screen image loads. Single-line edit per image; large win.
- **No `srcset` / responsive images.** On mobile, the same 2.5 MB `Quentin2.jpg` is served as on desktop. Either pre-generate `-medium` and `-thumb` variants or ship one well-compressed master. (The simpler fix is just to compress; `srcset` is the next step.)
- **Image alt text is filename-equivalent.** "Stammtafel Johann Friedrich Kontze.jpg" is technically alt text but isn't useful to a screen reader or for accessibility. Replace with descriptive: "Stammtafel chart for the Johann Friedrich Kontze family, prepared by Peter Schräder, showing nine children with birth and death dates."
- **No favicon.** Browser tabs show the default globe icon. Add a 32×32 favicon (any of the gold-on-dark accent could work — even a stylized "CG" monogram).
- **No `<meta name="description">`.** On the main file and 200+ sub-pages. This impacts how links render in iMessage, Slack, email previews, and search. One sentence per page.
- **No Open Graph / Twitter card tags.** A 4-line `<meta property="og:title" / og:description / og:image / og:type>` block makes shared links render with a preview image and summary card.
- **No `<title>` updates on tab change.** Clicking through to "Civil War" doesn't update the document title — which means browser history and bookmarks all read "Charles Gannsen Research — A Genealogical Investigation". Five lines of JS in the existing `showTab()` function fixes this.
- **Tab nav at 13 tabs will overflow on phones.** The 720px media query hides Roman numerals but the labels stay long. "People who knew Charles" alone is 22 characters. On a 360px iPhone the tab row will horizontal-scroll. Either (a) use shorter labels on mobile (`People`, `Sources`, `Schrader`), (b) collapse into a hamburger / `<select>` dropdown below 600px, or (c) wrap to two rows.
- **Keyboard nav.** The tab buttons have `:focus` styling, but the SVG region-link `<a>`s don't. Add `:focus-visible` styling so keyboard users can see what's focused.
- **`_deploy_netlify` doubles the working tree.** Currently 67 MB mirrored from the 158 MB source. Two options: (a) delete the mirror and let Netlify build directly from the root with a build step that just copies the served files, or (b) gitignore-equivalent the heavy non-served files (the 27 MB `peter_charts/*.zip` files probably don't need to ship). Deploy weight matters less now than it did, but cleaner is cleaner.

---

## The 20-recommendation backlog, prioritized

| # | Recommendation | Effort | Impact | Priority |
|---|----------------|:--:|:--:|:--:|
| 1 | "What's new" dated banner on Overview tab | XS | High | 🟢 Do first |
| 2 | Hoist shared CSS for `family_pages/` and `notes/` | M | Med | 🟢 Do first |
| 3 | Compress images + add `loading="lazy"` | S | High | 🟢 Do first |
| 4 | Add favicon, `<meta description>`, og:image | S | Med | 🟢 Do first |
| 5 | Unified "Everyone in the story" index page | M | High | 🟢 Do first |
| 6 | Per-tab mini-TOC on long tabs | S | Med | 🟡 Next |
| 7 | Site-wide confidence-badge taxonomy | M | Med | 🟡 Next |
| 8 | Update `<title>` on tab change | XS | Low | 🟡 Next |
| 9 | Mobile tab row — wrap or collapse | S | Med | 🟡 Next |
| 10 | "Last updated" timestamp per tab | S | Low | 🟡 Next |
| 11 | Improve image alt text (31 images) | S | Low | 🟡 Next |
| 12 | Move v1–v27 docx drafts to `notes/_archive/` | XS | Low | 🟡 Next |
| 13 | Add per-tab "Open questions" footer block | M | Med | 🔵 Later |
| 14 | Consolidate inline `style=""` into classes | M | Low | 🔵 Later |
| 15 | Evidence-index page (Doc A–O reference) | M | Med | 🔵 Later |
| 16 | Even out person-profile depth | M | Low | 🔵 Later |
| 17 | Trim the `_deploy_netlify` mirror | S | Low | 🔵 Later |
| 18 | Add `:focus-visible` styling for keyboard users | XS | Low | 🔵 Later |
| 19 | Footer site-map | S | Low | 🔵 Later |
| 20 | Pagefind static search (only if going public) | S | Low | ⚪ Optional |

**Effort key:** XS = under 30 min · S = 1–2 hr · M = half-day

---

## Comparison reference points

For the things the site already does well — the Overview infographic, the per-tab evidence cards, the pension-file page-by-page viewer — the closest comparators are professional one-name studies (e.g. the [Gentle One-Name Study](http://gentle.one-name.net/) school) and academic digital exhibits. For the things to improve, the reference set is more pedestrian: standard web hygiene (favicon, og tags, image compression) and modern long-form journalism patterns ("what's new" rails, in-page TOCs, mobile-first nav).

The site is closer in quality to a digital-humanities exhibit than to a hobbyist family-history wiki — that's a real achievement, and the recommendations above are about closing the last 15% of the gap, not about a redesign.

---

*If you want, I can implement any of items #1–5 directly — say which and I'll go.*
