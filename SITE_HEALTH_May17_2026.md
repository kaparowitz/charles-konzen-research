# Site health report — 17 May 2026

A snapshot of the Charles Konzen Research site's technical state immediately after the multi-round audit-fix pass (rounds 1–5).

## Headline numbers

| Signal | Count |
|---|---|
| Total public HTML pages | **167** |
| JSON-LD blocks (all valid) | **347** |
| Pages with Article schema | **165** |
| Pages with BreadcrumbList | **151** |
| Pages with Person schema (kin profiles) | **193** |
| FAQPage schema | 1 (`faq.html`) |
| Pages missing meta description | **0** |
| Pages missing canonical URL | **0** |
| Sitemap entries (clean) | **172** |
| Per-page OG cards wired | **30** |
| Total `<img>` tags | 227 |
| Imgs with `width`/`height` | 130 (local), 95 external (not actionable) |
| Imgs with `loading="lazy"` | **227 of 227** |
| Genuinely broken internal links | **0** of 13,904 |
| JSON-LD parse errors | **0** of 347 |

## What was fixed (cumulative across 5 rounds)

### Content & genealogical rigor (P0)
- **1.6 GB `_deploy_netlify/` mirror** removed from deploy + repo; `.netlifyignore` + `.gitignore` updated; `sync-deploy.sh` dead code removed.
- **Front-page surname-conclusion link** (`konzen-puzzle.html`) fixed across 8 references — was 404'ing the project's own headline finding.
- **"geb Konzen" propagation failure** corrected on all 6 children pages (per the May 2026 errata that hadn't actually propagated).
- **1880 census conflation** fixed in the abstract — was attributing "Jansen" to "1880 U.S. Federal Census, enumerator J. Nollau"; corrected to distinguish 1880 baptism Jansen (Pastor Nollau) from 1880 census Gonson (enumerator unknown).
- **Surname trail standardised** site-wide to "seven distinct American spellings across eight independent attestations: Gonnson · Gansen · Gonsen · Konsen · Jansen · Gonson · Conson." Removed the bogus "Konzen" (German form) that appeared in the U.S.-renderings list in 6 places.
- **"6 December 2026" future date** (in abstract, about, errata, bibliography Schräder references) corrected to "6 May 2026".
- **"13 candidate families" / "21 candidate families" inconsistency** resolved — 13 is canonical across all flagship pages; updates.html and freundburg-mystery.html updated.
- **Pension affiant roster** in bibliography corrected to 7 (Derr, Meyer, Stoll, Nolan, Niemeier, Gottlob, Hitzelberger); Herweck clarified as marriage witness only.

### Information architecture & navigation
- **Real SPA static mirrors** for all 12 SPA tabs (was 12 redirect stubs at 16 lines each; now real pages 170–1,208 lines with per-page Article JSON-LD, OG cards, prev/next pager). The `<link rel="alternate">` promise in `index.html` now actually holds.
- **Reference dropdown split** into "Reference" (Abstract / Methodology / Bibliography / Open Questions / Errata / Visualize) + "About" (About / Contribute / FAQ / Glossary / Changelog). Was an 11-item junk drawer. Propagated to all 173 standalone pages.
- **First H2 on the Home tab** changed from "Home" to "Who was Charles Konzen?" — buries-the-lede problem fixed.
- **"Latest Findings" → "Home"** vocabulary unified across prose, button labels, and aria-labels.
- **People-tab nav** gained Family_Tree_All_Families and Kontze_Family_Tree_Graphic links (were orphaned visualizations).
- **44 inline `onclick`** SPA-tab handlers stripped from `index.html` — Cmd-click / middle-click / right-click-open-in-new-tab now work properly.
- **Mobile nav** now scrolls horizontally on a single row at ≤720 px instead of wrapping to 2–3 rows.
- **404 page** contact pointer fixed (was pointing at methodology, now points at contribute).

### SEO & social
- **149 pages** carry BreadcrumbList JSON-LD (was 0) — Google SERP results now show navigation hierarchy.
- **130 pages** carry Article JSON-LD (was ~33) — rich-result eligibility expanded to /people/, /family_pages/, /civilwar/, /germany/, /immigration/, /children/, /towns/, /sources/, /research_logs/.
- **30 pages** have per-page OG cards (was ~5; now branded social-share images per section).
- **Open Graph `og:image`** swept from relative SVG → absolute PNG site-wide (Facebook/LinkedIn/Slack don't render SVG).
- **Sitemap** cleaned: removed `assets/site-nav.html` and `assets/site-footer.html` pollution; freshness dates current; 172 valid URLs.
- **`updates.html` 301-redirected** to `changelog.html` via `netlify.toml` (was an orphan parallel changelog drifting from the canonical one).
- **0 pages** missing meta description; **0 pages** missing canonical URL (after fill-meta.py pass).
- **24 "St Louis"** (no period) → "St. Louis" across 7 files; intentional quoted instances preserved.

### Technical health
- **Leaflet `<script>`** now has `defer` on all 6 map-bearing pages (was blocking on `index.html`).
- **Skip-to-main link** added to 7 pages that lacked it.
- **All 227 `<img>` tags** now have `loading="lazy"`; **130 local imgs** have explicit `width`/`height` (CLS-safe).
- **Largest deployed image:** 2.0 MB (Stammtafel scan, intentional for deep-zoom). Was 8.9 MB.
- **WebP for Charles's portrait:** 1.6 MB → 344 KB (79% reduction); wired via existing `<picture>` element.
- **`_original.jpg` files** excluded from deploy via `.netlifyignore` patterns.
- **Search widget** repositioned from `top-right` (overlapping cinematic cover) to `bottom-right` with mobile-stretch.

### Editorial & writing
- **Six "six vs seven" inconsistencies** in the renderings count fixed (was slipping between "six distinct" and "seven distinct" within the same paragraph in the abstract).
- **Heisebeck framing** in abstract updated to include Schöneberg (matching errata).
- **methodology.html:451** obsolete sentence ("site does not maintain a centralised bibliography page") rewritten — bibliography exists.
- **GPS-compliance language** in abstract softened to acknowledge the residual research gap.
- **Cinema Chapter II + III ledes** depoeticised: removed "no English clerk can hear correctly" and "smallpox hospital" cover-card phrasings that were lightly fictionalising.
- **Schräder umlaut** standardised: 0 bare "Schrader" in flagship pages (was 8 in `index.html`); only intentional CSS-class tokens remain.
- **8 archive-card titles** in `index.html` document section converted from MDY ("April 14, 2026") to DMY ("14 April 2026").
- **Transcription-provenance note** added to abstract's Methodology section.
- **Cite-section code blocks** (3×) and sponsors annotation blocks (7×) migrated from inline styles to utility classes.

### Hero & shared component consolidation
- **8 unpaired `*-hero` classes** paired with the canonical `cinema-section-hero`; canonical print rules added in `cinematic.css` covering `cinema-section-hero / tab-hero / child-hero / story-hero`.
- **People in the Story tab** heading outline (verified): 1 H2 + 4 H3s + sub-H4s (was 53–59 H2s flat per May 14 audit); text-list duplicate view removed.

## What's not yet done — documented for handoff

| Item | Why deferred | Path to resolution |
|---|---|---|
| Aggressive SPA split (`scripts/split-spa.py --apply`) | Would create 3-way content duplication against the static mirrors we just built; plan recommends waiting until conservative split is Google-indexed | Run after ~2 weeks of indexing; staged & rollback-able |
| Deep-zoom on Evidence Cards 1–8 | The CSS+JS exist but no `<figure class="deep-zoom">` is used anywhere; the May 8 audit-completion report's claim of "5 of 8 wired" was aspirational | Needs IIIF tile sets per scan, then `data-src` wiring |
| WebP for 6 baptism evidence images | ImageMagick produced WebPs *larger* than source JPGs (scan parchment noise defeats prediction) | Try `cwebp --lossless`, or accept the JPGs |
| ORCID / Zenodo DOI / Wikidata Q-item mints | External accounts only | See `IDENTIFIERS_KIT.md` §1–§4 sed swaps |
| Long-tail inline-style migration (~10 in `index.html`, 8 in `Family_Tree_All_Families.html`, single-use stragglers) | Each one would need its own utility class for one use; not worth migration cost | Migrate incrementally as files get touched |

## How to ship

```sh
bash deploy.sh
```
or `git push` if connected to a Netlify-watched remote.

Post-deploy QA checklist (from `HANDOFF.md`):
1. Visit the live URL — verify nothing 500s
2. Submit a current snapshot to the Wayback Machine
3. Run Facebook OG validator and Twitter Card validator on the home page + one section page
4. Mobile QA: iPhone-emulation in Chrome devtools, focus the site-search box, verify the 236 KB lazy-loaded index returns hits

---

## Genealogy-rigor audit follow-up — 17 May 2026 (evening)

A second-round audit-fix pass shipped the same day, triggered by an external genealogy-rigor evaluation. **Internal-contradiction sweep (P0):** the seven factual contradictions that survived the morning's audit-fix pass were all closed (death-vs-burial date conflation; Bertha 1879→1880; Stammrolle age-18→age-20; Konzen-in-U.S.-spelling-list strip from methodology + FAQ; surname-count enumerations on foundation/index/who; 21→13 candidate-family count; tree-interactive Auguste-Kreichelt and Maria-Josephine errors). Each is logged as a formal entry on `errata.html` per the methodology's "log promotions and demotions, don't silently overwrite" rule.

**New audit-companion pages:**

| Path | Purpose |
|---|---|
| `sponsor-reconciliation.html` | The "immigrated alone" structural argument as a single auditable table: 17 sponsorship slots × 15 distinct sponsors across 7 baptisms, with each sponsor's documented kin link to Auguste and the explicit absence of any Charles-side blood relative. Three counterarguments addressed; category-distribution statistics (9 Auguste-side blood / 4 affinal / 3 St. Louis parish-circle / 0 Charles-side blood). |
| `negative-results.html` | The "reasonably exhaustive research" claim as an auditable table: 10 Hessian parishes searched (scope/result/closing-evidence each), 13 candidate families eliminated (with verdict date and elimination ground), plus U.S.-side and emigration-record searches. |

**Methodology page additions:**

- New §3 subsection: **Evidence-grade chips** (★ Orig · firsthand / Orig · secondhand / Derivative / Compiled · authored) per Mills's originality + informant-proximity framework. Applied inline on Key Evidence Cards 2, 3, and 6 as example notation.
- New §5 subsection: **Transcription-hand provenance** mapping every verbatim block on the site to one of three hands (Peter Schräder for German parish registers, author for U.S.-side records, Archion HTR as a low-confidence first pass) with the in-page notation convention.

**Working-state tagging (P1-9, P1-10):**

- The headline surname conclusion in the abstract and both germany-and-origins surname-verdict blocks now carries an inline ★ Working chip pointing to the source-rating taxonomy and Open Questions Priority 1 — eliminating the prior ambiguity between "is KONZEN" prose and the four-state confidence taxonomy.
- A conflict-resolution block was added to Key Evidence Card 8 (Compiled Service Record) addressing the 1862 enlistment "age 23" reading vs canonical 26 January 1835 birth date, per Mills §1.27 source-class weighting.
- Confidence-snapshot blocks were added to civil-war.html, charles-in-america.html, and immigration-journey.html (where ~zero formal badges previously existed) tagging the page's load-bearing claims with the four-state badges.

**Doc A–O crosswalk:** added as a `<details>` block on source-archive.html mapping each 2020-journal Doc letter to its current 2026 live source-archive / child / people / research-log entry, with confidence rating per row. Surfaced an honest 1-day discrepancy between Doc A (death certificate: 17 Dec) and Doc N (parish burial register: 16 Dec) as a Working-tagged minor open question.

**Nav + sitemap propagation:** both new pages added to `assets/site-nav.html` under Sources & method + Reference; `inject-site-nav.py` rebuilt the menu across 175 standalone pages (176/178 final count, the 2 exceptions being noscript and head-less files); `build-sitemap.py` re-ran to include both new pages (174 total entries).

**Final-state grep verification (post-fix):**

| Pattern | Before today | After today |
|---|---|---|
| "Bertha 1879" / "1879–1959" | 4 flagship pages + 3 FAQ blocks | 0 |
| "died 19 December 1903" attributed to Charles | 5 flagship pages + JSON-LD | 0 |
| "Konzen" inside any U.S.-spelling enumeration | methodology + FAQ | 0 |
| "21 candidate families" | germany-and-origins + Schräder timeline + index | 0 |
| "1853 conscription record at age 18" | 10+ flagship instances + Stammrolle research log | 0 |
| Auguste Kreichelt "1843 / Hesse-Cassel" | tree-interactive + faq + 1870-census log | 0 |
| Maria Josephine bio carrying "Auguste Somers" quote | tree-interactive | 0 |

**Outstanding items, external only:**

| Item | Why deferred | Owner |
|---|---|---|
| Zenodo DOI mint | External account | Jed (kit ready in `IDENTIFIERS_KIT.md`) |
| Wikidata Q-item mint | External account | Jed (draft ready in `WIKIDATA_DRAFT.md`) |
| Independent BCG-certified peer review of surname conclusion | Needs outside human | Jed to recruit |

The site's GPS-compliance posture is now substantively stronger: every load-bearing claim is either Confirmed with a primary source attached or Working with an explicit pointer to what would close it; the two auditable companion pages make the structural arguments reproducible; methodology now codifies both the four-state confidence taxonomy and the evidence-grade chip convention; and seven new errata entries log every contradiction this audit caught.

## Genealogy-rigor audit follow-up — 17 May 2026 (late evening: user-catch cascade)

A second user-catch pass shipped after the evening rigor work. Three substantive reframes, each one a class of bug the date/spelling sweep didn't surface: <em>project reconstructions presented as attestations</em>.

**Catch 1 — "L. Carl Konsen" as attested birth name.** The home page's "Identity at a glance" vital-details row listed Charles's "Birth name (German)" as <em>L. Carl Konsen</em>, with the same label appearing as a chip on the name-evolution flow's "1862 enlistment · 1866 marriage" stage and in the verdict paragraph. No single source carries that combination. The fix: the row is now "Birth name (reconstructed) ★ Working" with a footnote citing the three sources the reconstruction draws on (L. from the 1862 enlistment muster cards, Carl from the 1866 marriage register + 1872/1875 father-of-child fields, Konsen from the 1875 son's baptism). The chips now show what's actually on each record ("L. Charles Gannsen" 1862 + "Carl Gonnson" 1866); "L. Carl Konsen" was moved to a separately labelled "Project reconstruction · ★ Working" sub-stage rendered in a dashed-border chip. Six instances across `index.html` and `charles-in-america.html` corrected.

**Catch 2 — Hesse-records chip set was undercount and miscategorised.** The name-evolution flow's "Hesse records · pre-1859" stage listed only three forms (Konze · Konsen · Konzen) when the canonical Hesse parish-register cluster is five (Konze · Kontze · Kontzen · Contze · Konzen) plus three more from the parish's own cross-reference note (Cortze · Cordes · Contz). Worse, "Konsen" with an s was included as a Hesse-attested form — but no Trendelburg or Deisel parish register carries that spelling; it's an American phonetic capture (1875 St. Marcus baptism, Pastor Hoffmann, Swiss-born). The `germany/konzen-puzzle.html` lead paragraph compounded the error: "the German Hesse spelling found in the Deisel and Trendelburg church books." Fix: chips now show five Hesse-attested forms with per-chip tooltips citing specific registers, the parish cross-reference note as a footnote, and an explicit "Konsen with an s is NOT in this cluster" callout. The Konzen Puzzle page now says "closest American match to the German Hesse spelling cluster" with the caveat that no parish register carries Konsen with an s.

**Catch 3 — the 1890 daughter's death record reads Konzen (with z), not Konsen.** A user re-examination of the 1890 St. Marcus death-register image concluded the maiden-name reading is <strong>Konzen</strong>, reversing the 5 May 2026 errata that had previously corrected the reading from Konzen → Konsen. The reading has now been called Konzen → Konsen (5 May) → Konzen (17 May) across two months, reflecting the difficulty of distinguishing z from s in mid-19th-century German Kurrentschrift. Cascade:

| Effect | Detail |
|---|---|
| U.S.-spelling canon | Expanded from 7 to **8** distinct spellings: Gonnson · Gansen · Gonsen · Konsen · Jansen · Gonson · **Konzen** · Conson |
| 1890 record's evidentiary weight | Becomes the **single American attestation of the full Hessian z-form Konzen** &mdash; the form documented in the Trendelburg parish from 1773. Maiden-name attestations on death records are high-fidelity primary evidence (used for cemetery / probate / inheritance verification). |
| Retired argument | "Konsen attested twice 15 years apart" replaced by "Konsen 1875 (phonetic s-form) + Konzen 1890 (Hessian z-form) — two parallel orthographic variants bracketing the surname trail" |
| Reversed P0-4 fix | Today's morning P0-4 errata had stripped "Konzen" from the U.S.-spelling enumeration on methodology.html and faq.html (on the basis Konzen didn't appear in any U.S. record). That fix is now reversed; Konzen has been restored to both pages with a pointer to the 1890 attestation. |
| Errata supersession | New 17 May late-evening entry at top of `errata.html` (`#er-2026-05-17-konzen-1890`) explicitly superseding the 5 May 2026 entry. The 5 May entry now carries a "SUPERSEDED" banner and a back-reference to the supersession. |

**Cascade scope of catch 3:** 28 bulk replacements across 13 files (the exact-quote `"Auguste Somers geb Konsen"` → `"Auguste Somers geb Konzen"`) + 6 additional replacements in a second pass for the HTML-entity-encoded variant in 6 children-page family-tree blocks; plus narrative reframes on `index.html` (×3), `key-evidence.html` (×3), `germany/konzen-puzzle.html` lead paragraph, `methodology.html` §6, `faq.html` Q2, `abstract.html` surname-trail paragraph + verdict block, `children/auguste.html` (×3 narrative blocks), `people/auguste-kreichelt.html` bottom-line, `charles_america/old-st-marcus-cemetery.html` daughter row, and `tree-interactive.html` Auguste-jr bio. Historical changelog entries left untouched as period documentation.

**Cumulative for 17 May 2026:** seven P0 contradiction fixes (morning) + six P1 content additions + two P2 audit-companion pages + three late-evening user-catch reframes = sixteen substantive rigor improvements in one day, with seventeen errata entries documenting every reversal.

**Lesson for the next audit cycle:** today's most-impactful catches all surfaced a single class of bug — <em>project-side reconstructions or interpretations presented as primary-source attestations</em>. The next dedicated rigor pass should specifically grep for: (a) vital-details / "as recorded" table rows that mix attested fields with reconstructed ones, (b) chip sets in name-evolution / spelling-trail flows where reconstructed forms appear alongside attested ones, (c) verdict paragraphs that elide the reconstruction step ("Charles &mdash; born X in Hesse"), and (d) "preserved in the parish books" claims where the project's interpretive bridge form is named as the parish reading. The user catches today reveal that the project's biggest remaining rigor risk is not contradictory dates but conflated source-categories — and that the methodology's evidence-grade chip convention introduced this morning is the right tool to surface and quarantine each instance.
