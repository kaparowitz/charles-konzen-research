#!/usr/bin/env python3
"""
Swap the injected shared nav + footer on standalone /de/ pages with the
GERMAN fragments (assets/site-nav.de.html, assets/site-footer.de.html).

For every /de/*.html page that carries the BEGIN/END-INJECTED-NAV (and
-FOOTER) markers, the English injected block is replaced with the German
one, with:
  • {{ROOT}}   → correct relative prefix back to the site root for that page
  • {{ROOTEN}} → same prefix, but never re-routed to /de/ (forced English)
  • links whose target has a finished German translation (per
    assets/de-pages.js) are routed to the /de/ copy, so German users stay
    in German; everything else points at the English page.

Idempotent. Skips de/index.html (it has its own hand-built German nav).
Re-run after translating more pages so newly-available /de/ links light up.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DE = ROOT / "de"
NAV_DE = (ROOT / "assets" / "site-nav.de.html").read_text(encoding="utf-8").strip()
FOOT_DE = (ROOT / "assets" / "site-footer.de.html").read_text(encoding="utf-8").strip()

NAV_BEGIN, NAV_END = "<!-- BEGIN-INJECTED-NAV -->", "<!-- END-INJECTED-NAV -->"
FOOT_BEGIN, FOOT_END = "<!-- BEGIN-INJECTED-FOOTER -->", "<!-- END-INJECTED-FOOTER -->"

def manifest_paths():
    js = (ROOT / "assets" / "de-pages.js").read_text(encoding="utf-8")
    return set(re.findall(r'"([^"]+)"', js))

def render(fragment, root_prefix, de_set):
    out = fragment
    # route translated links into /de/  (plain links only — anchored links
    # like {{ROOT}}index.html#charles stay on the English SPA).
    for p in de_set:
        out = out.replace('{{ROOT}}' + p + '"', '{{ROOT}}de/' + p + '"')
    # forced-English placeholder first, then the normal one.
    out = out.replace('{{ROOTEN}}', root_prefix)
    out = out.replace('{{ROOT}}', root_prefix)
    return out

def replace_block(content, begin, end, new_inner):
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    if not pat.search(content):
        return content, False
    return pat.sub(begin + "\n" + new_inner + "\n" + end, content, count=1), True

def main():
    de_set = manifest_paths()
    changed = 0
    for fp in sorted(DE.rglob("*.html")):
        rel = fp.relative_to(DE).as_posix()
        if rel == "index.html" or "backup" in rel.lower() or fp.name.startswith("."):
            continue
        depth = len(fp.relative_to(ROOT).parts) - 1
        root_prefix = "../" * depth
        txt = fp.read_text(encoding="utf-8")
        if NAV_BEGIN not in txt:
            continue
        nav = render(NAV_DE, root_prefix, de_set)
        foot = render(FOOT_DE, root_prefix, de_set)
        txt, n1 = replace_block(txt, NAV_BEGIN, NAV_END, nav)
        txt, n2 = replace_block(txt, FOOT_BEGIN, FOOT_END, foot)
        fp.write_text(txt, encoding="utf-8")
        if n1 or n2:
            changed += 1
            print(f"localised nav/footer: de/{rel}  (nav={n1} footer={n2})")
    print(f"\nUpdated {changed} German page(s). Manifest had {len(de_set)} translated targets.")

if __name__ == "__main__":
    main()
