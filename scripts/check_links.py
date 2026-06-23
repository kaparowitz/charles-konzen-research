#!/usr/bin/env python3
"""
check_links.py — internal broken-link audit for the Charles Konzen Research site.

Catches:
  - href="path/to/file.html"       → file missing on disk
  - href="path/to/file.html#anchor" → file ok, anchor doesn't exist there
  - href="#anchor"                  → in-page anchor missing

Skips:
  - External hrefs (http/https/mailto/tel/javascript/data)
  - Template files under assets/ that contain {{ROOT}} placeholders
  - Backup, archive, and notes directories
  - The skip-link target #main (injected by inject-site-nav.py; see
    body_inject_skip_anchor() in that script)

Usage:
  python3 scripts/check_links.py
  python3 scripts/check_links.py --quiet   # only prints the totals
  python3 scripts/check_links.py --strict  # exit ≠ 0 on ANY hit (warn-class too)

Default exit code is 0 if no broken refs found, 1 otherwise. Suitable as a
pre-deploy gate (see deploy.sh sanity_checks).
"""
from __future__ import annotations
import argparse, os, re, sys, urllib.parse
from html.parser import HTMLParser
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = (
    "./notes/", "./_archive", "./_backup_originals/", "./_deploy_netlify/",
    "./_recovery_20260608",
    "./session_notes_docx/", "./scripts/", "./.netlify", "./.git",
    "./peter_charts/", "./nara_pages/", "./nara_ocr/",
    "./evidence_thumbs/", "./evidence_images/", "./family_photos/",
)
TEMPLATES = {"./assets/site-nav.html", "./assets/site-footer.html"}

class HrefCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs: list[str] = []
        self.ids: set[str] = set()
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "href" in d:
            self.hrefs.append(d["href"])
        if "id" in d:
            self.ids.add(d["id"])

_anchor_cache: dict[str, set[str] | None] = {}
def anchors_for(path: str) -> set[str] | None:
    if path in _anchor_cache:
        return _anchor_cache[path]
    if not os.path.exists(path):
        _anchor_cache[path] = None
        return None
    try:
        text = open(path, encoding="utf-8", errors="ignore").read()
    except Exception:
        _anchor_cache[path] = None
        return None
    ids = set(re.findall(r'\bid="([^"]+)"', text))
    ids |= set(re.findall(r'\bname="([^"]+)"', text))
    _anchor_cache[path] = ids
    return ids


def audit(strict: bool = False, quiet: bool = False) -> int:
    os.chdir(ROOT)
    pages: list[str] = []
    for root, dirs, files in os.walk("."):
        if any(root.startswith(s) for s in SKIP_DIRS) or root.startswith("./."):
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            p = os.path.join(root, f)
            if p in TEMPLATES:
                continue
            pages.append(p)

    by_cat: dict[str, list] = defaultdict(list)
    for page in pages:
        try:
            text = open(page, encoding="utf-8").read()
        except Exception:
            continue
        p = HrefCollector(); p.feed(text)
        page_dir = os.path.dirname(page) or "."
        for h in sorted(set(p.hrefs)):
            if not h:
                continue
            if h.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "data:")):
                continue
            if h.startswith("#main"):
                continue
            if h.startswith("#"):
                anchor = h[1:]
                if anchor and anchor not in p.ids:
                    by_cat["in-page-anchor-missing"].append((page, h))
                continue
            file_part, _, anchor = h.partition("#")
            file_part = file_part.split("?", 1)[0]
            if file_part.startswith("/"):
                target = "." + file_part
            else:
                target = os.path.normpath(os.path.join(page_dir, urllib.parse.unquote(file_part)))
            if os.path.isdir(target):
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                by_cat["missing-file"].append((page, h, target))
                continue
            # PDF fragments (#page=N, #nameddest=…) are viewer open-parameters, not HTML
            # id/name anchors, so they can't be validated against the file's ids — skip them.
            if anchor and not target.lower().endswith(".pdf"):
                ids = anchors_for(target)
                if ids and anchor not in ids:
                    by_cat["cross-page-anchor-missing"].append((page, h, target, anchor))

    total = sum(len(v) for v in by_cat.values())
    if not quiet:
        print(f"check_links: {len(pages)} pages audited, {total} broken refs")
        for cat in ("missing-file", "cross-page-anchor-missing", "in-page-anchor-missing"):
            items = by_cat[cat]
            if not items:
                continue
            print(f"\n  {cat} ({len(items)}):")
            seen: dict = {}
            for row in items:
                key = row[1:]
                seen.setdefault(key, []).append(row[0])
            for key, srcs in sorted(seen.items(), key=lambda kv: -len(kv[1]))[:30]:
                if cat == "missing-file":
                    href, target = key
                    print(f"    [{len(srcs)}×]  {href!r}  →  no file at {target}")
                elif cat == "cross-page-anchor-missing":
                    href, target, anchor = key
                    print(f"    [{len(srcs)}×]  {href!r}  →  #{anchor} missing in {target}")
                else:
                    print(f"    [{len(srcs)}×]  {key[0]!r}")
                for s in srcs[:2]:
                    print(f"              ← {s}")

    if total == 0:
        if not quiet:
            print("✓ no broken internal links")
        return 0
    return 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="Reserved — currently identical to default (no warn-class yet)")
    args = ap.parse_args()
    return audit(strict=args.strict, quiet=args.quiet)

if __name__ == "__main__":
    sys.exit(main())
