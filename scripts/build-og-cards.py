#!/usr/bin/env python3
"""
Generate per-page Open Graph card SVGs for the major standalone pages.

Each card is a 1200×630 SVG using the project's cinematic palette,
with the page's title set as the dominant text and the project name as
an eyebrow. Cards are written to /assets/og/ and the script optionally
rewrites the og:image meta on each page to point at its dedicated card.

Run with --update-pages to apply the og:image rewrite. Default is
--cards-only (preview).
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OG_DIR = ROOT / "assets" / "og"

# (page_path, page_title, eyebrow_label, accent_color)
PAGES = [
    ("abstract.html",    "Charles Konzen Research",   "★ Abstract",       "#d8b366"),
    ("methodology.html", "Methodology",               "Research standards","#8a6420"),
    ("faq.html",         "Frequently asked questions","FAQ",              "#d8b366"),
    ("glossary.html",    "Glossary",                  "German terminology","#8a6420"),
    ("bibliography.html","Bibliography",              "Every cited source","#8a6420"),
    ("open-questions.html","Open Questions",          "What we haven't found","#c87a30"),
    ("visualize.html",   "Visualize",                 "Four signature diagrams","#d8b366"),
    ("changelog.html",   "Changelog",                 "Substantive updates","#8a6420"),
    ("about.html",       "About this project",        "Authors · contact · cite","#d8b366"),
    ("contribute.html",  "Contribute or correct",     "How to add to the research","#c87a30"),
    ("stories.html",     "Stories",                   "Nine narrative moments","#d8b366"),
    ("cast.html",        "Cast",                      "The people in the stories","#a04030"),
    ("evidence/index.html","Key Evidence",            "8 high-leverage documents","#d8b366"),
    ("germany/index.html","Germany & Origins",        "Hesse-Kassel · Trendelburg","#4a6e34"),
    ("germany/parish-map.html","Hessian Parish Map",  "Every parish investigated","#4a6e34"),
    ("germany/konzen-puzzle.html","The Konzen Puzzle","Linguistic time-capsule","#4a6e34"),
    ("civilwar/index.html","Civil War service",       "Battery B · 2nd Mo Light Artillery","#a04030"),
    ("immigration/index.html","Immigration Journey",  "1859 · The Atlantic crossing","#3a5a8c"),
    ("people/index.html","People in the Story",       "~80 named individuals","#8a6420"),
    ("sources/index.html","Source archive",           "Every primary-source viewer","#8a6420"),
    ("towns/index.html", "Towns & villages",          "The Hofgeismar parish complex","#4a6e34"),
    ("children/index.html","The seven children",      "1866–1880 · St. Marcus baptisms","#b06820"),
    ("charles_america/index.html","Charles in America","His U.S. life · 1859–1903","#b06820"),
    ("correspondence/index.html","Schräder Correspondence","The collaboration trail","#6e4818"),
]

# Per-evidence-card OG covers
EVIDENCE_CARDS = [
    (1, "Card 1 · Trendelburg Kontzen", "★ Project conclusion", "#a04030"),
    (2, "Card 2 · Civil War enlistment", "1st Kurhessen reference", "#a04030"),
    (3, "Card 3 · 1866 marriage register", "Charles's stated origin", "#d8b366"),
    (4, "Card 4 · Seven baptisms", "1866–1880 · St. Marcus", "#d8b366"),
    (5, "Card 5 · 1868 naturalization", "4th Kurhessen reference", "#d8b366"),
    (6, "Card 6 · Erwin Carl Konsen baptism", "Linguistic time capsule", "#d8b366"),
    (7, "Card 7 · Pension file F41-…", "Seven affidavits · 1890–1903", "#a04030"),
    (8, "Card 8 · 'Auguste Conson' 1896", "Charles-self-attestation", "#d8b366"),
]


SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1f1a14"/>
      <stop offset="100%" stop-color="#3a2f1e"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0.45"/>
    </linearGradient>
    <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#d8b366" fill-opacity="0.06"/>
    </pattern>
  </defs>

  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect width="1200" height="630" fill="url(#dots)"/>

  <!-- Top accent bar -->
  <rect x="0" y="0" width="1200" height="6" fill="url(#accent)"/>
  <rect x="0" y="6" width="1200" height="2" fill="#d8b366" fill-opacity="0.6"/>

  <!-- Bottom double-rule (matches the cinematic 4px-double brand-color borders) -->
  <rect x="0" y="618" width="1200" height="3" fill="#d8b366" fill-opacity="0.5"/>
  <rect x="0" y="624" width="1200" height="2" fill="#d8b366"/>

  <!-- Side accent column -->
  <rect x="0" y="0" width="6" height="630" fill="{accent}"/>

  <!-- Project mark (small caps eyebrow) -->
  <text x="80" y="138" fill="#d8b366" font-family="Cormorant Garamond, Georgia, serif" font-weight="600" font-size="22" letter-spacing="6">A GENEALOGICAL INVESTIGATION</text>

  <!-- Eyebrow label -->
  <text x="80" y="220" fill="{accent}" font-family="Cormorant Garamond, Georgia, serif" font-weight="700" font-size="28" letter-spacing="3" font-style="italic">{eyebrow}</text>

  <!-- Main title -->
  {title_lines}

  <!-- Project signature -->
  <text x="80" y="555" fill="#c8b896" font-family="Cormorant Garamond, Georgia, serif" font-size="22" font-style="italic">Charles Konzen Research</text>
  <text x="80" y="582" fill="#8a7858" font-family="Inter, Arial, sans-serif" font-size="18">charles-konzen-research.netlify.app</text>

  <!-- Decorative gilt seal (top-right) -->
  <g transform="translate(1050, 130)">
    <circle cx="0" cy="0" r="60" fill="none" stroke="#d8b366" stroke-width="1.5" stroke-opacity="0.75"/>
    <circle cx="0" cy="0" r="48" fill="none" stroke="#d8b366" stroke-width="0.6" stroke-opacity="0.5"/>
    <text x="0" y="6" fill="#d8b366" font-family="Cormorant Garamond, Georgia, serif" font-size="34" font-style="italic" text-anchor="middle">CK</text>
  </g>
</svg>
"""


def render_title(title: str) -> str:
    """Render a multi-line H1 title as <text> elements. Splits long titles."""
    # rough wrap at ~24 chars
    words = title.split(" ")
    lines = []
    cur = ""
    for w in words:
        candidate = (cur + " " + w).strip()
        if len(candidate) > 26 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = candidate
    if cur:
        lines.append(cur)
    if len(lines) > 3:
        # fall back to single line shrunk
        lines = [title]

    if len(lines) == 1:
        size = 88 if len(lines[0]) <= 16 else 72
        return f'<text x="80" y="380" fill="#f6f1e7" font-family="Cormorant Garamond, Georgia, serif" font-weight="700" font-size="{size}">{xml_escape(lines[0])}</text>'

    # multi-line
    size = 64 if max(len(l) for l in lines) <= 22 else 56
    line_height = int(size * 1.05)
    base_y = 360 - (len(lines) - 1) * line_height // 2
    out = []
    for i, l in enumerate(lines):
        y = base_y + i * line_height
        out.append(f'<text x="80" y="{y}" fill="#f6f1e7" font-family="Cormorant Garamond, Georgia, serif" font-weight="700" font-size="{size}">{xml_escape(l)}</text>')
    return "\n  ".join(out)


def xml_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def slugify_for_filename(rel: str) -> str:
    p = rel.replace("/index.html", "/").replace(".html", "").replace("/", "_").rstrip("_")
    return p or "home"


def main(argv: list[str]) -> int:
    OG_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    page_to_card: dict[str, str] = {}

    for rel, title, eyebrow, accent in PAGES:
        svg = SVG_TEMPLATE.format(
            accent=accent,
            eyebrow=xml_escape(eyebrow),
            title_lines=render_title(title),
        )
        slug = slugify_for_filename(rel)
        out = OG_DIR / f"{slug}.svg"
        out.write_text(svg, encoding="utf-8")
        page_to_card[rel] = f"assets/og/{slug}.svg"
        written += 1

    # Evidence-card covers
    for n, title, eyebrow, accent in EVIDENCE_CARDS:
        svg = SVG_TEMPLATE.format(
            accent=accent,
            eyebrow=xml_escape(eyebrow),
            title_lines=render_title(title),
        )
        out = OG_DIR / f"evidence_card_{n}.svg"
        out.write_text(svg, encoding="utf-8")
        written += 1

    print(f"Wrote {written} OG SVG covers to {OG_DIR.relative_to(ROOT)}/")

    if "--update-pages" in argv:
        updated = 0
        for rel, card_path in page_to_card.items():
            page = ROOT / rel
            if not page.exists():
                continue
            try:
                c = page.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                c = page.read_text(encoding="latin-1")
            depth = rel.count("/") - (1 if rel.endswith("/index.html") or rel.endswith("index.html") else 0)
            # Use absolute prefix from this page back to root
            rel_path = page.relative_to(ROOT)
            depth_back = len(rel_path.parts) - 1
            prefix = "../" * depth_back
            new_card_url = prefix + card_path
            new = re.sub(
                r'(<meta\s+property="og:image"\s+content=")[^"]+(")',
                lambda m: m.group(1) + new_card_url + m.group(2),
                c,
                count=1,
            )
            new = re.sub(
                r'(<meta\s+name="twitter:image"\s+content=")[^"]+(")',
                lambda m: m.group(1) + new_card_url + m.group(2),
                new,
                count=1,
            )
            if new != c:
                page.write_text(new, encoding="utf-8")
                updated += 1
        print(f"Updated og:image / twitter:image on {updated} pages.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
