# People-Pages Audit — May 10, 2026

**Goal.** Evaluate every `people/*.html` page on the Charles Konzen Research site against the gold-standard structure established by the seven children pages (`children/auguste.html`, `bertha.html`, `erwin-carl-konsen.html`, `friedrich-wilhelm.html`, `josephine-maria.html`, `katherine-carolina.html`, `louise.html`) and bring them all up to that standard.

## Gold-standard checklist

Each page should have, in order:

1. **Head boilerplate** — theme-toggle init, viewport, `_shared.css`, theme/cinematic/dark-mode CSS, schema/JSON-LD `Person` block.
2. **Per-page `<style>` block** with: hero `.pill` overrides (confirmed/open/died-young), section h2 inline `.badge-inline`, `details.research-log` styling, `prefers-reduced-motion` reset.
3. **`#dark-boxes-override` style block** — dark-mode background/border overrides for all card/box/timeline classes.
4. **`<header class="child-hero cinema-section-hero">`** — crumbs, h1, sub, lifespan.
5. **★ At a Glance summary card** — `card-pill`, FS profile id, `bottom-line` paragraph (≥2 sentences with **bold** name + key facts), `charles-link` "Why this matters for understanding Charles" callout, `quick-facts` grid.
6. **Vital details** — `kv` table with every standard field (name, born, baptized, died, parents, FS profile, etc.).
7. **Family tree** — `family-tree` block showing parents and siblings (where applicable).
8. **Key event evidence card** — baptism / marriage / death / pension page with embedded image, ★ KEY EVIDENCE pill where appropriate, sponsor/witness list.
9. **Sources & cross-references** — bulleted list of FamilySearch link, journal entries, register citations, evidence-card cross-links.
10. **Back-nav footer + Cite-this-page widget** (already present site-wide via injection).

## Gap matrix

| Page                            | At-Glance | Bottom-line | Why-Charles | Quick-facts | Vital tbl | Family tree | Evidence card | Sponsors | Sources | Research-log | Hero pills | Reduced-motion | Dark-mode override |
|---------------------------------|:---------:|:-----------:|:-----------:|:-----------:|:---------:|:-----------:|:-------------:|:--------:|:-------:|:------------:|:----------:|:--------------:|:------------------:|
| **CHILDREN — gold standard**    |           |             |             |             |           |             |               |          |         |              |            |                |                    |
| children/auguste.html           |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     ✅    |    ✅    |              |     ✅      |       ✅        |                    |
| children/bertha.html            |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     ✅    |    ✅    |      ✅       |     ✅      |       ✅        |                    |
| children/erwin-carl-konsen.html |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     ✅    |    ✅    |      ✅       |     ✅      |       ✅        |                    |
| children/friedrich-wilhelm.html |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     ✅    |    ✅    |              |     ✅      |       ✅        |                    |
| children/josephine-maria.html   |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     ✅    |    ✅    |              |     ✅      |       ✅        |                    |
| children/katherine-carolina    |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     ✅    |    ✅    |      ✅       |     ✅      |       ✅        |                    |
| children/louise.html            |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     ✅    |    ✅    |      ✅       |     ✅      |       ✅        |                    |
| **PEOPLE — needs upgrade**      |           |             |             |             |           |             |               |          |         |              |            |                |                    |
| adam-herweck.html               |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         ✅           |
| amalia-muenke.html              |     ✅     |      ✅      |      ✅      |      ✅      |     —     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| august-derr.html                |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| august-kreichelt.html           |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| auguste-kreichelt.html          |    (alt)  |     (alt)   |     (alt)   |     (alt)   |     —     |      ✅      |       ✅       |     —    |    ✅    |      —       |     —      |       —        |         ✅           |
| bertha-barbara-kreichelt.html   |     ✅     |      ✅      |      ✅      |      ✅      |     —     |      ✅      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| carl-kreichelt.html             |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      ✅      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| catharina-albrecht.html         |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| christian-meyer.html            |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| christina-hahl.html             |     —     |      —      |      —      |      —      |     —     |      ✅      |       —       |     —    |    ✅    |      —       |     —      |       —        |         —          |
| dr-charles-hess.html            |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| erwin-spraul.html               |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| frederick-pillmann.html         |     ✅     |      ✅      |      ✅      |      ✅      |     —     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| georg-kreichelt.html            |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         ✅           |
| henriette-kreichelt.html        |     ✅     |      ✅      |      ✅      |      ✅      |     ✅     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| henry-niemeier.html             |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| henry-stoll.html                |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| jacob-reck.html                 |     ✅     |      ✅      |      ✅      |      ✅      |     —     |      ✅      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| john-hebbeler.html              |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| john-heitzenberger.html         |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| john-thurbecker.html            |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| josephine-von-delian.html       |     ✅     |      ✅      |      ✅      |      ✅      |     —     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| katherine-misch.html            |     —     |      —      |      —      |      —      |     —     |      ✅      |       —       |     —    |    ✅    |      —       |     —      |       —        |         —          |
| maria-agnes-goetz.html          |     ✅     |      ✅      |      ✅      |      ✅      |     —     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |
| michael-nolan.html              |     —     |      —      |      —      |      —      |     ✅     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| theodore-gottlob.html           |     —     |      —      |      —      |      —      |     —     |      —      |       ✅       |     —    |    —    |      —       |     —      |       —        |         —          |
| wilhelmina-ebeling.html         |     ✅     |      ✅      |      ✅      |      ✅      |     —     |      —      |       ✅       |     —    |    ✅    |      ✅       |     ✅      |       ✅        |         —          |

> **Coverage on `people/*.html` (out of 27):** At-Glance 13/27 · Bottom-line 13/27 · Why-Charles 13/27 · Quick-facts 13/27 · Vital tbl 16/27 · Family tree 7/27 · Evidence card 25/27 · Sources 16/27 · Research-log 13/27 · Hero pills 13/27 · Reduced-motion 13/27 · Dark-mode override 3/27.
> **Universal across all pages:** schema JSON-LD Person 27/27 · cite-widget 27/27 · back-nav 27/27 · `_shared.css` 27/27 · `site-nav-shared` 27/27 · `child-hero` 27/27.

## Two cohorts

**Cohort A — already mostly aligned (13 pages):** amalia-muenke, august-kreichelt, bertha-barbara-kreichelt, carl-kreichelt, catharina-albrecht, erwin-spraul, frederick-pillmann, georg-kreichelt, henriette-kreichelt, jacob-reck, josephine-von-delian, maria-agnes-goetz, wilhelmina-ebeling. *Need:* dark-mode-boxes override; sometimes vital-details `kv` table; sometimes family tree.

**Cohort B — skeletal, full upgrade required (14 pages):** adam-herweck (rich but uses different conventions), auguste-kreichelt (rich but uses different conventions), august-derr, christian-meyer, christina-hahl, dr-charles-hess, henry-niemeier, henry-stoll, john-hebbeler, john-heitzenberger, john-thurbecker, katherine-misch, michael-nolan, theodore-gottlob. *Need:* full ★ At a Glance card, charles-link callout, quick-facts grid, sources block, all the CSS pieces.

## Action plan

1. **Universal CSS injection** — apply hero-pill overrides, research-log styling, prefers-reduced-motion block, and `#dark-boxes-override` to every page that lacks them. Pattern-based, scriptable.
2. **Per-page semantic upgrade** — for each Cohort B page (and the gaps in Cohort A), draft the bottom-line / Why-Charles / quick-facts content from the existing page evidence and the broader site research notes.
3. **Verification pass** — re-run the audit script; confirm every page now has the gold-standard markers.

---

## Post-upgrade state (after May 10 evening pass)

**Markers now at 27/27 across every people/*.html page:**

`at_a_glance` · `card_pill` · `bottom_line` · `why_charles_callout` · `quick_facts_grid` · `vital_details_table` · `evidence_card` · `sources_xrefs` · `hero_pill_overrides` · `research_log_styles` · `reduced_motion_block` · `darkmode_boxes_override` · `schema_jsonld_person` · `cite_widget` · `back_nav` · `shared_css` · `site_nav_shared` · `child_hero` — **18 of 21 metrics fully aligned with the seven-children gold standard.**

**Three metrics that legitimately remain partial — by design:**

- `family_tree_block` (11/27) — pension witnesses (Derr, Meyer, Niemeier, Stoll, Hebbeler, Heitzenberger, Thurbecker, Nolan, Hess, Spraul, Pillmann, Reck, von Delian, Goetz, Ebeling, Albrecht) have no documented Konzen-family connection that would justify a family tree on their bio page; family trees were added only where the in-family relationship makes one informative (georg-kreichelt, henriette-kreichelt, amalia-muenke, theodore-gottlob, plus the kreichelt siblings that already had them).
- `sponsor_list` (0/27) — `class="sponsors"` is the baptism-sponsor enumeration pattern from the children pages (where each child's three baptism sponsors are listed). It does not apply on the people pages, which are themselves the sponsors. No structural gap.
- `research_log_details` (13/27) — the optional research-log dropdown was added on a per-page basis where day-to-day investigation notes warrant one. Pages without one rely on the broader site's `research_logs/` directory and `Session*` markdown notes.

## Verification (May 10 evening)

- **HTML well-formedness:** 27/27 pages parse cleanly under Python's HTMLParser. Two pre-existing well-formedness defects were repaired in passing (`john-heitzenberger.html` had a stray `</p>` on line 401; `katherine-misch.html` had an extra `</div>` on line 451).
- **Internal-link integrity:** 0 broken `../` links across all 27 pages (URL-decoded paths). The earlier flagged `auguste-kreichelt.html → ../peter_charts/record-image_%2046.jpg` is a false positive — the file exists as `record-image_ 46.jpg` (the `%20` URL-decodes to a space, matching the actual filename).
- **At-a-Glance card injection bug:** the first batch of injected cards had a stray `</p></div>` closing pattern inside `<div class="charles-link">`. Fixed across all 14 pages with a sed-style sweep.

## Sequence of changes applied

1. Universal CSS injection — added the standard hero-pill / badge-inline / research-log details / prefers-reduced-motion `<style>` block to 14 pages that lacked it; added the `id="dark-boxes-override"` block to 24 pages that lacked it.
2. ★ At a Glance summary cards — drafted and injected on 14 pages (adam-herweck, august-derr, auguste-kreichelt, christian-meyer, christina-hahl, dr-charles-hess, henry-niemeier, henry-stoll, john-hebbeler, john-heitzenberger, john-thurbecker, katherine-misch, michael-nolan, theodore-gottlob).
3. Sources & cross-references — added on 11 pages that had no Sources block (the pension-witness cohort + adam-herweck + theodore-gottlob).
4. Vital details `kv` tables — added on 11 pages whose existing content lacked a formal `<table class="kv">` structure.
5. Family-tree blocks — added on georg-kreichelt, henriette-kreichelt, amalia-muenke, theodore-gottlob (the in-family figures whose family graph aids the broader narrative).
6. Documentary-chain evidence cards — added on christina-hahl and katherine-misch to wrap their Misch ⟷ Gottlob bridge findings in the canonical `evidence-card` styling.
7. HTML repair — fixed the two pre-existing well-formedness defects.
