#!/usr/bin/env python3
"""
Inject the shared site nav + footer into every standalone HTML page.

Rules:
  - Skip /notes/ (working drafts, noindex)
  - Skip /_archive*/ and /_backup_originals/
  - Skip index.html (it has its own SPA nav)
  - Idempotent — replaces existing injection if rerun

Usage:
    python3 scripts/inject-site-nav.py
"""
from __future__ import annotations
import hashlib
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAV_FRAG = (ROOT / "assets" / "site-nav.html").read_text(encoding="utf-8")
FOOTER_FRAG = (ROOT / "assets" / "site-footer.html").read_text(encoding="utf-8")

# Markers used to recognize and replace prior injections.
NAV_BEGIN = "<!-- BEGIN-INJECTED-NAV -->"
NAV_END = "<!-- END-INJECTED-NAV -->"
FOOT_BEGIN = "<!-- BEGIN-INJECTED-FOOTER -->"
FOOT_END = "<!-- END-INJECTED-FOOTER -->"

CSS_LINK_BEGIN = "<!-- BEGIN-INJECTED-NAV-ASSETS -->"
CSS_LINK_END = "<!-- END-INJECTED-NAV-ASSETS -->"

# ---- automatic cache-busting -------------------------------------------------
# The injected nav assets used to be referenced with no ?v= query, so browsers
# cached an old copy and every page kept serving stale CSS/JS (the sticky nav
# would "scroll away", dropdowns would mis-behave, etc.). We now stamp each
# injected asset with a short hash of its *content*, so the URL changes
# automatically whenever the file changes — and stays identical when it
# doesn't. Just rerun this script after editing any nav asset.
_VER_CACHE: dict[str, str] = {}


def asset_ver(rel_asset: str) -> str:
    """Return a short content hash (cache-buster) for an asset under ROOT.

    Degrades gracefully to '' if the file can't be read, so a missing file
    never breaks injection — the reference is just emitted without a query.
    """
    if rel_asset not in _VER_CACHE:
        try:
            _VER_CACHE[rel_asset] = hashlib.md5(
                (ROOT / rel_asset).read_bytes()
            ).hexdigest()[:10]
        except OSError:
            _VER_CACHE[rel_asset] = ""
    return _VER_CACHE[rel_asset]


def versioned(rel_asset: str) -> str:
    """'assets/site-nav.css' -> 'assets/site-nav.css?v=<hash>' (root-relative)."""
    v = asset_ver(rel_asset)
    return f"{rel_asset}?v={v}" if v else rel_asset

SKIP_PREFIXES = ("notes/", "_archive", "_backup_originals/", "de/")
SKIP_FILES = {"index.html"}  # the home page has its own SPA nav
# NOTE: "de/" is skipped because the German mirror has its own nav/footer,
# applied by scripts/inject-site-nav-de.py (German labels + /de/ links).
# Running this English injector over /de/ would overwrite the German nav.


def relative_root_for(page: Path) -> str:
    """Return relative path prefix from this page back to repo root, e.g. '../' or '../../' or ''. """
    rel = page.relative_to(ROOT)
    depth = len(rel.parts) - 1  # number of directories above the file
    if depth == 0:
        return ""
    return "../" * depth


def render_fragment(fragment: str, root_prefix: str) -> str:
    return fragment.replace("{{ROOT}}", root_prefix)


def head_inject_assets(content: str, root_prefix: str) -> str:
    """Insert <link> + <script> for the shared nav, cite-widget, and deep-zoom assets in <head>, idempotently."""
    block = (
        f"{CSS_LINK_BEGIN}\n"
        f'<link rel="stylesheet" href="{root_prefix}{versioned("assets/site-nav.css")}">\n'
        f'<script defer src="{root_prefix}{versioned("assets/site-nav.js")}"></script>\n'
        f'<link rel="stylesheet" href="{root_prefix}{versioned("assets/cite-widget.css")}">\n'
        f'<script defer src="{root_prefix}{versioned("assets/cite-widget.js")}"></script>\n'
        f'<link rel="stylesheet" href="{root_prefix}{versioned("assets/deep-zoom.css")}">\n'
        f'<script defer src="{root_prefix}{versioned("assets/deep-zoom.js")}"></script>\n'
        f"{CSS_LINK_END}"
    )
    # If markers already present, replace.
    if CSS_LINK_BEGIN in content:
        return re.sub(
            re.escape(CSS_LINK_BEGIN) + r".*?" + re.escape(CSS_LINK_END),
            block.replace("\\", "\\\\"),
            content,
            count=1,
            flags=re.DOTALL,
        )
    # Otherwise, insert right before </head>.
    if "</head>" not in content:
        return content
    return content.replace("</head>", block + "\n</head>", 1)


def body_inject_nav(content: str, root_prefix: str) -> str:
    block = NAV_BEGIN + "\n" + render_fragment(NAV_FRAG, root_prefix) + "\n" + NAV_END
    if NAV_BEGIN in content:
        return re.sub(
            re.escape(NAV_BEGIN) + r".*?" + re.escape(NAV_END),
            block.replace("\\", "\\\\"),
            content,
            count=1,
            flags=re.DOTALL,
        )
    # Insert immediately after the opening <body...> tag.
    m = re.search(r"<body[^>]*>", content)
    if not m:
        return content
    end = m.end()
    return content[:end] + "\n" + block + "\n" + content[end:]


SKIP_ANCHOR_BEGIN = "<!-- BEGIN-INJECTED-SKIP-ANCHOR -->"
SKIP_ANCHOR_END = "<!-- END-INJECTED-SKIP-ANCHOR -->"
SKIP_ANCHOR_HTML = (
    SKIP_ANCHOR_BEGIN
    + '<a id="main" tabindex="-1" aria-hidden="true" '
      'style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);"></a>'
    + SKIP_ANCHOR_END
)


def body_inject_skip_anchor(content: str) -> str:
    """Insert (or refresh) the #main skip-link target immediately before
    the first <main> tag. The shared nav fragment's skip-link points to
    #main; many standalone pages have <main> tags whose existing id is a
    SPA-tab data-target (e.g. 'evidence-static') rather than 'main', so
    an empty anchor element is the cheapest way to give the skip-link a
    landing without disturbing those ids.

    Idempotent — replaces an existing injection if rerun. No-op if the
    page already has an element with id="main" or doesn't have a <main>.
    """
    if SKIP_ANCHOR_BEGIN in content:
        # Already injected — refresh in case the markup changed.
        return re.sub(
            re.escape(SKIP_ANCHOR_BEGIN) + r".*?" + re.escape(SKIP_ANCHOR_END),
            SKIP_ANCHOR_HTML,
            content,
            count=1,
            flags=re.DOTALL,
        )
    # If the page already has an id="main" anywhere (e.g. a hand-authored
    # <main id="main">), don't add a second one — HTML forbids duplicate ids.
    if re.search(r'\bid\s*=\s*"main"', content):
        return content
    m = re.search(r"<main\b", content)
    if not m:
        return content
    return content[: m.start()] + SKIP_ANCHOR_HTML + "\n" + content[m.start() :]


def body_inject_footer(content: str, root_prefix: str) -> str:
    block = FOOT_BEGIN + "\n" + render_fragment(FOOTER_FRAG, root_prefix) + "\n" + FOOT_END
    if FOOT_BEGIN in content:
        return re.sub(
            re.escape(FOOT_BEGIN) + r".*?" + re.escape(FOOT_END),
            block.replace("\\", "\\\\"),
            content,
            count=1,
            flags=re.DOTALL,
        )
    # Insert immediately before the closing </body>.
    if "</body>" not in content:
        return content
    return content.replace("</body>", block + "\n</body>", 1)


def should_skip(rel_path: str) -> bool:
    if any(rel_path.startswith(p) for p in SKIP_PREFIXES):
        return True
    if rel_path in SKIP_FILES:
        return True
    return False


def main() -> int:
    pages: list[Path] = []
    for path in ROOT.rglob("*.html"):
        rel = str(path.relative_to(ROOT)).replace(os.sep, "/")
        if should_skip(rel):
            continue
        pages.append(path)

    pages.sort()
    updated = 0
    skipped = 0
    no_body = 0
    no_head = 0

    for page in pages:
        rel = page.relative_to(ROOT).as_posix()
        try:
            content = page.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = page.read_text(encoding="latin-1")

        original = content
        root_prefix = relative_root_for(page)

        if "<head>" not in content and "<head " not in content:
            no_head += 1
            continue
        if "<body" not in content:
            no_body += 1
            continue

        content = head_inject_assets(content, root_prefix)
        content = body_inject_nav(content, root_prefix)
        content = body_inject_skip_anchor(content)
        content = body_inject_footer(content, root_prefix)

        if content != original:
            page.write_text(content, encoding="utf-8")
            updated += 1
        else:
            skipped += 1

    print(f"Pages scanned : {len(pages)}")
    print(f"Updated       : {updated}")
    print(f"No-op         : {skipped}")
    print(f"No <head>     : {no_head}")
    print(f"No <body>     : {no_body}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
