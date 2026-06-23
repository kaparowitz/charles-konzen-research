#!/usr/bin/env python3
"""
Inject BreadcrumbList JSON-LD into every page that has Article JSON-LD.

Breadcrumbs help Google show the page's position in the site hierarchy in
SERP results, replacing the otherwise-shown raw URL path. Bracketed by
<!-- BEGIN-INJECTED-BREADCRUMB --> / <!-- END-INJECTED-BREADCRUMB -->
markers for idempotent re-runs.

Each breadcrumb is derived from the page's URL path: e.g.
/civilwar/fort-wyman-rolla.html → Home › Civil War › Fort Wyman, Rolla.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://charles-konzen-research.netlify.app"

# Section-name overrides (URL slug → human label) for the breadcrumb chain.
SECTION_LABELS = {
    "civilwar":           "Civil War",
    "charles_america":    "Charles in America",
    "germany":            "Germany & Origins",
    "immigration":        "Immigration Journey",
    "people":             "People in the Story",
    "children":           "The Seven Children",
    "evidence":           "Key Evidence",
    "sources":            "Source Archive",
    "correspondence":     "Schräder Correspondence",
    "towns":              "Towns & Villages",
    "family_pages":       "Family Pages",
    "who":                "Who's Who",
    "de":                 "Deutsch",
    "themes":             "Themes",
    "research_logs":      "Research Logs",
}

# Page-title overrides for the leaf breadcrumb.
PAGE_LABELS = {
    "index.html":         None,  # skip — we don't add breadcrumb to home
    "abstract.html":      "Abstract",
    "methodology.html":   "Methodology",
    "bibliography.html":  "Bibliography",
    "open-questions.html":"Open Questions",
    "errata.html":        "Errata",
    "visualize.html":     "Visualize",
    "faq.html":           "FAQ",
    "glossary.html":      "Glossary",
    "about.html":         "About this project",
    "contribute.html":    "Contribute",
    "changelog.html":     "Changelog",
    "stories.html":       "Stories",
    "cast.html":          "Cast",
    "404.html":           None,
    "styleguide.html":    None,  # noindex anyway
    "civil-war.html":              "Civil War",
    "charles-in-america.html":     "Charles in America",
    "germany-and-origins.html":    "Germany & Origins",
    "immigration-journey.html":    "Immigration Journey",
    "people-in-the-story.html":    "People in the Story",
    "key-evidence.html":           "Key Evidence",
    "schrader-correspondence.html":"Schräder Correspondence",
    "source-archive.html":         "Source Archive",
    "latest-findings.html":        "Latest Findings",
    "overview.html":               "Overview",
    "foundation.html":             "Foundation",
    "family-tree-spa.html":        "Family Tree",
}

MARKER_BEGIN = "<!-- BEGIN-INJECTED-BREADCRUMB -->"
MARKER_END = "<!-- END-INJECTED-BREADCRUMB -->"


def humanize(slug: str) -> str:
    """Convert a slug like 'fort-wyman-rolla' to 'Fort Wyman Rolla'."""
    s = slug.replace("-", " ").replace("_", " ")
    return s.title()


def build_breadcrumb(rel_path: str) -> dict | None:
    """Build BreadcrumbList JSON-LD for a page given its repo-relative path."""
    parts = rel_path.split("/")
    fname = parts[-1]

    # Home page gets no breadcrumb
    if rel_path == "index.html":
        return None
    if fname in PAGE_LABELS and PAGE_LABELS[fname] is None:
        return None

    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": f"{BASE}/",
    }]
    pos = 2

    # Section parts (intermediate directories)
    for i in range(len(parts) - 1):
        section_slug = parts[i]
        section_path = "/".join(parts[:i + 1])
        label = SECTION_LABELS.get(section_slug, humanize(section_slug))
        items.append({
            "@type": "ListItem",
            "position": pos,
            "name": label,
            "item": f"{BASE}/{section_path}/",
        })
        pos += 1

    # Leaf — current page (no item URL per schema.org best practice)
    if fname == "index.html":
        # Section's own index — already in the chain above; drop the redundant last item
        items.pop()
        # Make the last item have no item URL (current page)
        if items:
            items[-1] = {k: v for k, v in items[-1].items() if k != "item"}
        # But if only Home is left, add a section leaf
        if len(items) < 2 and len(parts) > 1:
            items.append({
                "@type": "ListItem",
                "position": pos,
                "name": SECTION_LABELS.get(parts[-2], humanize(parts[-2])),
            })
    else:
        leaf_label = PAGE_LABELS.get(fname)
        if leaf_label is None:
            # Derive from filename
            leaf_label = humanize(fname.replace(".html", ""))
        items.append({
            "@type": "ListItem",
            "position": pos,
            "name": leaf_label,
        })

    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def inject(path: Path) -> str | None:
    """Inject a breadcrumb JSON-LD block into the page. Returns 'updated' / 'skipped' / 'no-page'."""
    rel = path.relative_to(ROOT).as_posix()
    if any(rel.startswith(p) for p in ("notes/", "_archive", "_backup_originals/", "_deploy_netlify/")):
        return "skipped"
    s = path.read_text(encoding="utf-8")
    # Skip if too small to be a real content page, or is a redirect stub
    if len(s) < 1500 or '<meta http-equiv="refresh"' in s:
        return "skipped"
    # Need a <head> to inject into
    if "</head>" not in s:
        return "skipped"

    bc = build_breadcrumb(rel)
    if bc is None:
        return "skipped"

    block = MARKER_BEGIN + "\n<script type=\"application/ld+json\">\n" + json.dumps(bc, indent=2, ensure_ascii=False) + "\n</script>\n" + MARKER_END
    # Replace existing block or insert before </head>
    if MARKER_BEGIN in s:
        new = re.sub(
            re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END),
            block,
            s,
            count=1,
            flags=re.DOTALL,
        )
    else:
        new = s.replace("</head>", block + "\n</head>", 1)
    if new != s:
        path.write_text(new, encoding="utf-8")
        return "updated"
    return "skipped"


def main() -> int:
    counts = {"updated": 0, "skipped": 0}
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(("notes/", "_archive", "_backup_originals/", "_deploy_netlify/", "scripts/")):
            continue
        status = inject(p)
        if status:
            counts[status] = counts.get(status, 0) + 1
    print(f"Updated: {counts.get('updated', 0)}  Skipped: {counts.get('skipped', 0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
