# Identifiers Kit — Zenodo DOI · ORCID · Wikidata

**Purpose.** Three external identifiers are wired into the site as
placeholders. This document is the single source of truth for minting
each one and replacing the placeholders with the real values. Once you
have the three IDs, the swap is a single `sed` command per identifier.

**Companion files** (created by the parallel session and referenced
throughout):
- `CITATION.cff` — machine-readable citation metadata (the GitHub
  "Cite this repository" widget reads this).
- `.zenodo.json` — pre-filled Zenodo metadata; Zenodo reads this from
  the GitHub release tag automatically.
- `wikidata/quickstatements.txt` — paste-ready Wikidata QuickStatements
  batch.
- `wikidata/README.md` — sibling guide for the QuickStatements run.
- `DEPLOY.md` — the deploy walkthrough; section "5 — Mint identifiers"
  is the short version of this kit.

This kit is the **long-form** companion: it explains *why* each
identifier matters, walks through the Zenodo / ORCID web forms field
by field, and provides the exact `sed` commands that swap every
placeholder in one shot. If you only want the abbreviated version,
read `DEPLOY.md` §5.

**Status (May 2026):** all three are pending mint. The site links and
JSON-LD currently render with `PLACEHOLDER-ORCID-JED`,
`PLACEHOLDER-ORCID-PETER`, and a `"DOI (when minted)"` label.

---

## Why these three identifiers, in this order

| Identifier | What it does for the project | Time to mint |
|------------|------------------------------|--------------|
| **Zenodo DOI** | Makes the site formally citable in NGSQ, *Hessische Familienkunde*, and Stadtarchiv correspondence. Without a DOI, citations rot when the URL changes. | ~30 min |
| **ORCID (×2)** | Disambiguates "Jed Johnson" and "Peter Schräder" from other authors with the same name. Required for several genealogical journals. Wires into the site's `Person` JSON-LD as `sameAs`, which Google Knowledge Graph indexes. | ~10 min each |
| **Wikidata Q-item** | Makes Charles Konzen the canonical web reference for a man who otherwise has no fixed entry. P973 (described-at-URL) points the world's largest open knowledge graph at this site. Search engines read Wikidata heavily. | ~30 min |

Mint Zenodo first (it citation-anchors everything else); then both
ORCIDs (so they can be deposited *into* the Zenodo record); then the
Wikidata item (which can reference the DOI as P356).

---

## 1 · Zenodo DOI

### A. Where to mint

<https://zenodo.org/> — sign in with your GitHub or ORCID identity.
After you've minted your ORCID below, that's the recommended login.

### B. Exact metadata to paste

Use the form below as the canonical metadata for the deposit. Every
field is filled — no guessing.

```
Resource type:        Software / Other / Dataset  →  pick "Other" → "Project / outputs"
                      (Zenodo does not have a "research site" type;
                      "Other" is correct for a multi-format research project.)

Title:                Charles Konzen Research: A Genealogical Investigation

Authors:              1.  Johnson, Jed  (ORCID: __ORCID_JED__)  — affiliation: Independent researcher
                      2.  Schräder, Peter  (ORCID: __ORCID_PETER__)  — affiliation: Independent genealogist, Trendelburg, Hesse, Germany

Description:          (paste the lede from abstract.html — the first paragraph of the abstract.
                      Keep it under 5,000 chars. Zenodo renders Markdown.)

                      ---

                      A multi-month transatlantic genealogical investigation into Charles Konzen
                      (recorded in U.S. records as Gannsen / Johnson; 26 January 1835 – 19 December 1903),
                      Hessian-born sergeant of Battery B, 2nd Missouri Light Artillery (Union), and
                      his Trendelburg / Deisel family origins in the former Electorate of
                      Hesse-Kassel.

                      The project documents what is confirmed, what remains open, and what has been
                      eliminated — at the level of detail required for independent verification.
                      It uses the Genealogical Proof Standard methodology (BCG Genealogy Standards,
                      2nd ed., 2019) and treats every claim as auditable: each parish register,
                      NARA service record, and pension-file page is reproduced as a primary-source
                      image with provenance, transcription, and translation.

                      The Charles Konzen Research site (charles-research.netlify.app) is the
                      living record of the investigation. This Zenodo deposit is a versioned
                      snapshot. For the most current state, consult the live site.

Keywords:             Charles Konzen; Charles Gannsen; Charles Johnson Sr.; Trendelburg; Deisel;
                      Friedrichsfeld; Konze; Kontzen; Contzen; Hesse-Kassel; Churhessen; Kurhessen;
                      Battery B 2nd Missouri Light Artillery; St. Marcus Evangelical Church;
                      Old Saint Marcus Cemetery; German immigration 1859; Civil War pension;
                      Auswanderer-Beleg; Genealogical Proof Standard; Hessisches Staatsarchiv;
                      Archion; Stadtarchiv Trendelburg

Communities:          Search for and add: "Genealogy" ; "Open Genealogy"
                      (these may not exist; if not, skip — community membership is optional)

Funding:              (leave blank — declared interests on /about.html note this is unfunded)

Languages:            English (primary)
                      German (secondary — for the /de/ Abstract and Glossary)

Dates:                Created:  2025-11-01  (project start, per /about.html)
                      Updated:  YYYY-MM-DD  (today's date when you publish)

Version:              1.0.0    (first formal deposit; bump to 1.1.0 on next deposit, 2.0.0 if methodology changes)

Licence:              Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
                      (this matches the /LICENSE file)

Related identifiers:  After minting:
                      "is identical to" → https://charles-research.netlify.app/
                      "is supplement to" → (later) the published article, if one is written

References:           (leave blank — references live in the deposited material itself)

Conference / Event:   (skip)
```

### C. What to upload

For the **first** deposit (1.0.0), upload either of these:

1. **Recommended:** a snapshot ZIP of the public site tree.
   Build it from the project root with:

   ```bash
   bash deploy.sh --snapshot zenodo-1.0.0.zip
   ```

   The script excludes `_archive*/`, `_backup_originals/`, `notes/`,
   and `.DS_Store`. Result is roughly 80 MB and contains every public
   page, every primary-source image, and every PDF.

2. **Alternative for a smaller first deposit:** the formal abstract
   PDF + the audit completion docx. After you run
   `bash scripts/build-pdfs.py` (already in the tree), upload:

   - `abstract.pdf`
   - `Charles_Konzen_Audit_Fix_Completion_May8_2026.docx`

   The full site can be a separate deposit at 1.1.0.

### D. After Zenodo issues the DOI

Zenodo will give you a string of the form `10.5281/zenodo.NNNNNNN`.
Save it. Then run **section 4** below to wire it through the site.

---

## 2 · ORCID (×2)

### A. Where to mint

Both authors register at <https://orcid.org/register>. Free, ~5 min
each.

### B. Exact metadata to paste

#### B.1 — Jed Johnson

```
Given names:          Jed
Family name:          Johnson
Primary email:        jedsjohnson@gmail.com
Country:              United States
Affiliation:          Independent researcher
Biography:            (optional — paste the bio from /about.html#authors)
Visibility:           Trusted parties (recommended) — lets the Zenodo deposit auto-link
Other identifiers:    (skip for now)
Websites:             https://charles-research.netlify.app/about.html
                      (label: "Charles Konzen Research")
Keywords:             genealogy; transatlantic migration; Hesse-Kassel; Civil War; primary source verification
```

After mint, ORCID issues a 16-digit ID like `0000-0001-2345-6789`.
Save it. That is `__ORCID_JED__` for the swap below.

#### B.2 — Peter Schräder

Peter is a co-author and a paid collaborator. Mint his ORCID **only
with his explicit consent**, and only with him on the call to enter
his own credentials. Do not mint on his behalf.

Suggested prompt for Peter (German, formal):

```
Sehr geehrter Herr Schräder,

für die Zenodo-Hinterlegung der Charles-Konzen-Forschung benötigen
beide Autoren eine ORCID-Kennung. Die ORCID-Registrierung ist
kostenlos und dauert etwa fünf Minuten unter:

  https://orcid.org/register

Bei Bedarf können wir das gemeinsam in einem Zoom-Termin durchgehen.
Die folgenden Felder werden ausgefüllt:

  Vorname:         Peter
  Nachname:        Schräder
  E-Mail:          (Ihre bevorzugte Kontaktadresse)
  Land:            Deutschland
  Affiliation:     Unabhängiger Genealoge, Trendelburg, Hessen
  Webseite:        https://charles-research.netlify.app/about.html
  Schlüsselwörter: Genealogie; Hessen-Kassel; Auswanderer-Belege; Archion; Kirchenbücher

Die ID wird einmal vergeben und ist lebenslang gültig.

Herzliche Grüße,
Jed
```

After mint, save Peter's ORCID. That is `__ORCID_PETER__` for the
swap below.

### C. After both ORCIDs are minted

Run **section 4**.

---

## 3 · Wikidata item for Charles Konzen

### A. Why

A Wikidata Q-item gives Charles Konzen a permanent, multi-lingual,
cross-referenced node in the world's largest open knowledge graph.
Search engines (Google, Bing, DuckDuckGo) read Wikidata aggressively;
the German-language descendants who search for `Konze Trendelburg
1835` end up at our site through Wikidata far more than through raw
Google ranking.

### B. Two-step mint

1. **Mint the item.** See `WIKIDATA_DRAFT.md` (sibling to this file)
   for the full statement-by-statement payload. Paste each statement
   into Wikidata's web UI at
   <https://www.wikidata.org/wiki/Special:NewItem>.

2. **Capture the QID.** Wikidata will assign a Q-number like
   `Q123456789`. Save it. That is `__WIKIDATA_QID__` for the swap
   below.

### C. After mint

Run **section 4**, and in addition add an `inverse` reference: edit
the Wikidata item to add `P973 (described-at-URL):
https://charles-research.netlify.app/`.

---

## 4 · The swap — one command per identifier

After all three identifiers are minted, run these from the project
root.

> **Sanity check before running:** the sibling Cowork session may
> still be editing files. Wait for that session to be idle, then
> run.

```bash
# 4.1 — Zenodo DOI (replace 10.5281/zenodo.NNNNNNN with your real DOI)
DOI="10.5281/zenodo.NNNNNNN"

# Substitute the placeholder text wherever it appears.
# This catches:
#   - `<div class="cite-lbl">DOI (when minted)</div>` cite-block label
#   - the `A persistent DOI ... is in progress` prose blurb
#   - `10.5281/zenodo.PLACEHOLDER` in CITATION.cff
#   - the `<html data-doi="…">` attribute the cite-widget reads
find . -type f \( -name "*.html" -o -name "*.cff" -o -name "*.json" \) \
  -not -path "./_archive*" -not -path "./_backup_originals/*" \
  -not -path "./notes/*" -not -path "./_deploy_netlify*" \
  -exec sed -i.bak \
    -e "s|>DOI (when minted)<|>DOI<|g" \
    -e "s|10\\.5281/zenodo\\.PLACEHOLDER|${DOI}|g" \
    -e "s|A persistent DOI for the project is in progress (see Zenodo deposit, planned May 2026)\\.|A persistent DOI for the project is <a href=\"https://doi.org/${DOI}\">${DOI}</a> (Zenodo).|g" \
    -e "s|A persistent DOI through Zenodo is in progress|The persistent DOI is <a href=\"https://doi.org/${DOI}\">${DOI}</a> (Zenodo).|g" \
    {} +
# Sanity: drop the .bak files
find . -name "*.bak" -not -path "./_archive*" -delete

# 4.2 — ORCID (Jed) — also covers CITATION.cff and .zenodo.json
ORCID_JED="0000-0001-XXXX-XXXX"   # paste your real ORCID here
find . -type f \( -name "*.html" -o -name "*.cff" -o -name "*.json" \) \
  -not -path "./_archive*" -not -path "./_backup_originals/*" -not -path "./notes/*" \
  -exec sed -i.bak "s|PLACEHOLDER-ORCID-JED|${ORCID_JED}|g" {} +
find . -name "*.bak" -not -path "./_archive*" -delete

# 4.3 — ORCID (Peter) — same coverage
ORCID_PETER="0000-0002-XXXX-XXXX"   # paste Peter's real ORCID here
find . -type f \( -name "*.html" -o -name "*.cff" -o -name "*.json" \) \
  -not -path "./_archive*" -not -path "./_backup_originals/*" -not -path "./notes/*" \
  -exec sed -i.bak "s|PLACEHOLDER-ORCID-PETER|${ORCID_PETER}|g" {} +
find . -name "*.bak" -not -path "./_archive*" -delete

# 4.4 — Wikidata QID
# This adds the QID into the Person JSON-LD `sameAs` block on /about.html
# and, if you've added the Wikidata anchor to the cast.html / people pages,
# replaces those placeholders too.
WIKIDATA_QID="QXXXXXXXX"
find . -type f -name "*.html" \
  -not -path "./_archive*" -not -path "./_backup_originals/*" -not -path "./notes/*" \
  -exec sed -i.bak "s|PLACEHOLDER-WIKIDATA-Q-ID|${WIKIDATA_QID}|g" {} +
find . -name "*.html.bak" -delete

# 4.5 — Verify nothing was missed
echo "=== Remaining placeholders (should be 0) ==="
grep -rIn "PLACEHOLDER-ORCID\|DOI (when minted)\|PLACEHOLDER-WIKIDATA" *.html */*.html 2>/dev/null | wc -l

# 4.6 — Regenerate sitemap so Zenodo / Wikidata crawlers see the latest tree
python3 scripts/build-sitemap.py

# 4.7 — Commit / re-deploy
bash deploy.sh
```

---

## 5 · After the swap — a 5-minute QA

1. Open `/about.html` and confirm the bios show real ORCID links
   (the green ORCID logo, not the word "PLACEHOLDER").
2. Open `/abstract.html` and `/index.html#cite` and confirm the
   citation block shows a real DOI (and the link goes to
   `doi.org/...`).
3. Run any page through Google's Rich Results Test
   (<https://search.google.com/test/rich-results>) and confirm:
   - `Person` schema includes `sameAs` for both ORCIDs.
   - `WebSite` schema includes `identifier` of type
     `PropertyValue` with the DOI.
4. Update Zenodo: edit your record, add the live `sameAs` link to
   the Wikidata item under "Related identifiers".
5. Update Wikidata: edit Q-item, add `P356 (DOI): NNNNN` and
   `P973 (described-at-URL): https://charles-research.netlify.app/`.

The three identifiers now form a closed reference loop: site → DOI →
Wikidata → site, and ORCID → Zenodo author → site → ORCID.

---

## Appendix · Where each placeholder currently lives

35 HTML files reference one or more of these placeholders. The most
important ones:

| Placeholder | Files (highlights) |
|-------------|-------------------|
| `PLACEHOLDER-ORCID-JED` | `about.html` (bio + JSON-LD) |
| `PLACEHOLDER-ORCID-PETER` | `about.html` (bio + JSON-LD) |
| `DOI (when minted)` | the cite-block on every top-level page (35 files) — added by the cite-widget |
| `A persistent DOI ... is in progress` | `about.html` how-to-cite blurb |
| `PLACEHOLDER-WIKIDATA-Q-ID` | not yet present — the swap in §4.4 is forward-compatible. Add the `sameAs` line to `about.html`'s Person JSON-LD when you mint. |

---

*Last updated: 9 May 2026 — written by the assistant during the parallel
session that staged the live-site deploy. Companion file:
`WIKIDATA_DRAFT.md`.*
