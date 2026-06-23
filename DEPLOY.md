# Deploy

This site lives at <https://charles-research.netlify.app/>.  The repo
is set up for **continuous deployment**: every push to `main` triggers a fresh
Netlify build.  This document is the one-time setup, plus the day-to-day workflow.

---

## Deploy configuration — resolved (publish from root)

The publish directory is the **project root**: `netlify.toml` declares
`publish = "."` and that is what the build uses.  The old dual-deploy conflict
is gone — the `_deploy_netlify/` mirror and `sync-deploy.sh` were both removed
(June 2026), so there is no longer a competing source of truth.  Just edit the
canonical files at the root and push; `.netlifyignore` controls what is excluded
from the upload.

---

## One-time setup (you do these once)

### 1 · Mint ORCID iDs

Both authors register at <https://orcid.org/register> (5 minutes each).  Then
run the search-replace pass that swaps the placeholders for the real iDs:

```sh
JED_ID="0000-0000-0000-XXXX"   # paste your real ORCID iD here
PETER_ID="0000-0000-0000-YYYY" # and Peter's

find . -name "*.html" -not -path "./_archive*" -not -path "./_backup*" \
  -exec sed -i '' "s|PLACEHOLDER-ORCID-JED|$JED_ID|g" {} +
find . -name "*.html" -not -path "./_archive*" -not -path "./_backup*" \
  -exec sed -i '' "s|PLACEHOLDER-ORCID-PETER|$PETER_ID|g" {} +
sed -i '' "s|PLACEHOLDER-ORCID-JED|$JED_ID|g" .zenodo.json CITATION.cff
sed -i '' "s|PLACEHOLDER-ORCID-PETER|$PETER_ID|g" .zenodo.json CITATION.cff
```

### 2 · Create the GitHub repo

```sh
cd "/Users/jedjohnson/Documents/Claude/Projects/Charles Gannsen Research"
git init
git add -A
git commit -m "Initial public commit — May 2026 audit-fix pass"
gh repo create charles-konzen-research --public --source=. --remote=origin --push
```

(Or skip the `gh` CLI step and do it through GitHub.com → New repository, then
`git remote add origin git@github.com:USER/charles-konzen-research.git && git push -u origin main`.)

### 3 · Connect Netlify to the GitHub repo

1. Log in at <https://app.netlify.com>.
2. **Site settings** → **Build & deploy** → **Continuous deployment** → **Link site to a Git repository**.
3. Pick GitHub → authorise → choose `charles-konzen-research`.
4. Build command: *(leave blank — it's a static site)*.
5. Publish directory: `.` (the project root, also pinned in `netlify.toml`).
6. Save.

Once connected, Netlify pulls every push.  The first auto-deploy will pick up
all the May 2026 audit-fix work that is currently sitting locally and not yet live.

### 4 · Mint the Zenodo DOI

Two paths, pick one:

- **Path A · One-time deposit**: log in at <https://zenodo.org/uploads/new>,
  drag in `.zenodo.json` to pre-fill, attach a curated PDF (the `abstract.pdf`
  and `methodology.pdf` together is a fine first deposit), publish.  Copy
  the DOI back into `index.html#cite`, `about.html#how-to-cite`, and
  `CITATION.cff`.

- **Path B · GitHub-linked auto-deposit** (recommended for ongoing work):
  follow <https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content>
  to link the repo to Zenodo.  Tag a release (`git tag v1.0.0 && git push --tags`)
  and Zenodo mints a DOI automatically and re-mints one for every future tag.
  Already-prepared `.zenodo.json` and `CITATION.cff` mean Zenodo and GitHub
  will populate from them with no further work.

### 5 · Wikidata entity

Once the DOI is in hand, paste `wikidata/quickstatements.txt` into
<https://quickstatements.toolforge.org/#/batch> (logged in to Wikidata).
After it runs, replace `PLACEHOLDER-WIKIDATA-Q-ID` in `index.html` with the
new Q-number.  See `wikidata/README.md` for full instructions.

### 6 · (Optional) Plausible analytics

Sign up at <https://plausible.io>, add `charles-research.netlify.app`
as a site, then run:

```sh
python3 scripts/inject-analytics.py --enable
```

That single command flips the (currently commented-out) Plausible tag live
on every page.  Re-run with `--remove` to strip it entirely.

---

## Day-to-day workflow

You edit content locally.  Every push to `main` deploys.

```sh
# After editing
python3 scripts/inject-site-nav.py    # if you added new HTML pages
python3 scripts/build-sitemap.py      # if you added or removed pages
python3 scripts/build-pdfs.py         # if you edited abstract/methodology/errata/bibliography
git add -A
git commit -m "<short message>"
git push
```

Netlify deploys in ~30 seconds.

---

## What's where

| Path | Purpose |
|---|---|
| `index.html` | Home page (the SPA + 12 in-DOM tabs) |
| `abstract.html`, `methodology.html`, `errata.html`, `bibliography.html`, etc. | Standalone reference pages |
| `latest-findings.html`, `overview.html`, `civil-war.html`, … (12 files) | Static mirrors of each SPA tab — citable URLs for SEO + bookmarking |
| `de/abstract.html`, `de/glossary.html` | German translations |
| `evidence/card-1-trendelburg-kontzen.html` … `card-8-1896-conson.html` | Per-card evidence pages with deep-zoom scans |
| `assets/site-nav.html`, `assets/site-footer.html`, `assets/site-nav.css`, `.js` | Shared nav + footer partials |
| `assets/cite-widget.css`, `.js` | "Cite this page" footer widget |
| `assets/deep-zoom.css`, `.js` | OpenSeadragon wrapper for primary-source scans |
| `assets/cinematic-spa.css` | Extracted SPA stylesheet (mirror of `index.html`'s inline `<style>`) |
| `assets/dark-mode.css` | `prefers-color-scheme: dark` re-binding |
| `scripts/*.py` | Maintenance scripts (all idempotent — see `HANDOFF.md`) |
| `.zenodo.json`, `CITATION.cff` | Citable-record metadata |
| `wikidata/` | QuickStatements + notes for the Wikidata entity |
| `netlify.toml`, `.netlifyignore`, `robots.txt`, `sitemap.xml`, `feed.xml` | Site infra |

---

## Troubleshooting deploys

- **Deploy succeeds but old pages still show**: hit Cmd+Shift+R; Netlify's
  CDN can also be force-refreshed via the *"Clear cache and deploy"* button
  in the Netlify UI.
- **Build fails on a missing file**: check `.netlifyignore` — the sweep
  excludes archives, notes, and editor artefacts; if a real file matches
  one of those globs, rename it.
- **404 on a section landing**: re-run `python3 scripts/build-sitemap.py`
  and re-deploy; the new URL must be in the sitemap before Google will
  consider it indexed.
