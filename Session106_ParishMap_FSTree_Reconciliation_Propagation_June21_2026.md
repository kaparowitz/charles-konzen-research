# Session 106 — Propagating the FS-tree reconciliation onto the Hessian parish map

**Date:** 21 June 2026
**Scope:** Mirror the 21 June FamilySearch shared-tree candidate reconciliation
(already folded into `abstract.html`, `claims-dashboard.html`, and `errata.html`
earlier that evening) onto `germany/parish-map.html`, which had last been touched
~2 hours before the batch and so was missing it.

---

## Why

The June 21 edit batch (errata, index, germany/index, abstract, claims-dashboard,
~01:5x UTC) added the FS-tree reconciliation finding but the parish map (last
modified 23:50 the prior evening) did not receive it. Jed asked to "update the
hessian parish map as well." This is a **mirror task** — propagate the same finding
in the map's own idiom (cards + Leaflet popups + search-history), not new research.

## The finding being propagated (recap)

A cross-read against the collaborative FamilySearch shared Family Tree corroborated
the project's hand-built Trendelburg/Deisel Konze framework and narrowed the
candidate field by **negative evidence**:

- **Carl Wilhelm Konze** (FS 99Z3-DFK, b. 15 Sep 1831 Trendelburg; son of Ludwig
  Karl Konze 1804 × Wilhelmine Marie Albrecht; first cousin of Justus Ernst) —
  briefly surfaced as a same-named candidate, then **ELIMINATED**: he stayed,
  married Marie Lauterbach, and **died at Trendelburg 30 Oct 1869**.
- **Justus Ernst Konze** (FS P87Z-ZDC, b. 14 Nov 1829 Friedrichsfeld; son of
  Andreas Kontze 1795 × Maria Sophia Hofeditz) — the **sole** Konze male of his
  generation absent from every searchable German death and emigration index;
  untraced after his 1843 Trendelburg confirmation. A **lead, not a confirmed
  identity**.
- Two decisive tests remain, both **offline**: page-by-page read of the un-indexed
  **Stammen burial register (Archion 220072, ~1843–1875)** and an individual
  emigration / release-from-citizenship file in **HStAM Bestand 180 Hofgeismar**.

Source detail: `FS_Tree_Konze_Reconciliation_June21_2026.md`;
errata `#er-2026-06-21-fs-tree-reconciliation`.

## Edits made to `germany/parish-map.html`

1. **New callout box** — "Which Konze son left — June 2026 FamilySearch-tree
   reconciliation," placed directly after the existing distribution-sweep callout;
   links to errata (21 Jun) and the negative-results audit.
2. **Trendelburg card + Leaflet popup** — added Carl Wilhelm Konze (1831), surfaced
   then eliminated (d. 30 Oct 1869 Trendelburg).
3. **Friedrichsfeld card + Leaflet popup** — Justus Ernst now flagged as the sole
   Konze male of his generation with no adult German death/marriage/emigration
   record; lead, not confirmed.
4. **Stammen card** — noted the decisive offline burial test (220072), since
   Justus Ernst's siblings Heinrich Wilhelm (†1858) and Elisa Melusine (†1865)
   both died at Stammen.
5. **Search-history strip** — new 21 June 2026 entry (FS-tree reconciliation +
   Archion citation audit + StLGS sweep); rewrote the "Open" line to lead with
   the two offline tests.
6. **JSON-LD** — `dateModified` bumped 2026-05-12 → 2026-06-21.

## What did NOT change (deliberate)

- **Parish counts unchanged**: still 29 investigated (1 stated origin · 2 working
  · 2 open · 24 eliminated). This was a *candidate-level* update inside
  Trendelburg/Friedrichsfeld — no parish moved category, no parish added.
- Status pills, map markers, coordinates, distance bars — untouched.

## Verification

- Counts intact (grep): 29 / 1 / 2 / 2 / 24.
- `<article class="parish-card">` open/close balanced at 29/29; 2 callouts.
- Fact spot-check: Carl Wilhelm 30 Oct 1869 / 99Z3-DFK / b. 15 Sep 1831;
  Justus Ernst P87Z-ZDC / b. 14 Nov 1829 — all consistent with the reconciliation
  log and the abstract/claims-dashboard wording.
- Cross-links resolve: errata `#er-2026-06-21-fs-tree-reconciliation` (present),
  negative-results `#families` (present).

## Convention note

Per the site-editing convention, the parish map is a *status/summary* surface, so
this folds the working answer in 2–3 sentences per card and pushes the full
hypothesis tree to the existing logs (`FS_Tree_Konze_Reconciliation_June21_2026.md`,
errata). No new conclusion was created; no Word-doc version bump needed.
