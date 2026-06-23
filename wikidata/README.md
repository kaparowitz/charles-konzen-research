# Wikidata + Zenodo — externalising the project's identifiers

This folder holds the metadata that turns the site from "an interesting personal
research site" into a record that participates in the global scholarly graph.

## Files

- **`../.zenodo.json`** — Zenodo deposit metadata.  Drop into the upload form
  at <https://zenodo.org/uploads/new> and Zenodo will pre-fill the title,
  authors, license, keywords, and related identifiers.  After publication,
  paste the DOI back into:
  - `index.html` (`#cite` block, JSON-LD `identifier`)
  - `about.html` (`#how-to-cite` section, the `Last revised` line)
  - `CITATION.cff` (replace `10.5281/zenodo.PLACEHOLDER`)
  - the cite-widget can also surface the DOI automatically if you set
    `<html data-doi="10.5281/zenodo.XXXXXXX">` on each page (or just on the
    home page) — `assets/cite-widget.js` already reads `data-doi` and shows
    a fourth row when it's present.

- **`quickstatements.txt`** — paste-able batch for
  <https://quickstatements.toolforge.org/#/batch> that creates the Wikidata
  item for Charles Konzen and the project item.  Read the file for line-by-line
  notes; each `LAST` line edits the most recently-created item.  Some property
  values (e.g. `P19 Hesse-Kassel`) should be verified on QuickStatements'
  preview before submission — Wikidata occasionally splits or merges
  geographic items.

- **`../CITATION.cff`** — Citation File Format metadata, used by GitHub's
  *"Cite this repository"* widget and by Zenodo when it auto-mints a DOI on
  GitHub release.  The `cff-version: 1.2.0` and DOI placeholder mean the file
  is ready to be picked up by GitHub's parser as soon as the repo is pushed.

## Order of operations

1. Mint ORCID iDs for both authors (see `HANDOFF.md`, item *ORCID*).
   Search-replace `PLACEHOLDER-ORCID-JED` and `PLACEHOLDER-ORCID-PETER`
   throughout the tree once you have the IDs.
2. Push the repo to GitHub (see `DEPLOY.md`).
3. Publish on Zenodo using `.zenodo.json` (or, if you connected the GitHub
   repo to Zenodo, simply tag a release — Zenodo will mint the DOI
   automatically and populate from `.zenodo.json`).
4. Paste the new DOI into `index.html`, `about.html`, and `CITATION.cff`.
5. Run the QuickStatements batch in `quickstatements.txt`.
6. Replace `PLACEHOLDER-WIKIDATA-Q-ID` in `index.html` (and any people pages
   you wire up later) with the Q-number QuickStatements assigns.

## Why this matters

Once steps 3–6 are done, the project has:

- A persistent DOI (Zenodo) — citable in NGSQ, books, and other Zenodo
  deposits without depending on this Netlify URL surviving.
- A Wikidata item — Google Knowledge Graph and most modern search engines
  pick this up as the canonical reference for "Charles Konzen (1835–1903)",
  and Wikipedia editors can hang citations off it.
- An ORCID-linked author block — co-citation graphs (Scopus, Dimensions,
  OpenAlex) start counting this project under both authors.
- A CFF file — GitHub auto-renders a "Cite this repository" widget from it,
  giving casual visitors a one-click citation.
