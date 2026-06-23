#!/usr/bin/env python3
"""
Sweep all HTML pages (excluding /notes/, archives, deploy mirror) and:

  1. Add <meta name="theme-color" content="#1F1A14"> if missing
     (between charset/viewport and the rest of head — keeps mobile
     Chrome address bar tinted to brand color).

  2. Add rel="noopener noreferrer" to every <a target="_blank">
     that is missing it. Idempotent — leaves existing rel alone.

  3. Inject a small @media (prefers-reduced-motion: reduce) override
     into every page that has an animation rule and doesn't already
     declare a reduced-motion override.

Idempotent. Skips /notes/, /_archive*/, /_backup_originals/.
"""
from __future__ import annotations
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_PREFIXES = ("notes/", "_archive", "_backup_originals/")

THEME_COLOR_TAG = '<meta name="theme-color" content="#1F1A14">'

REDUCED_MOTION_BLOCK = (
    "/* Respect prefers-reduced-motion (audit-fix pass, 8 May 2026). */\n"
    "  @media (prefers-reduced-motion: reduce) {\n"
    "    *, *::before, *::after {\n"
    "      animation-duration: 0.001ms !important;\n"
    "      animation-iteration-count: 1 !important;\n"
    "      transition-duration: 0.001ms !important;\n"
    "      scroll-behavior: auto !important;\n"
    "    }\n"
    "  }"
)

REDUCED_MOTION_MARKER = "Respect prefers-reduced-motion"


def should_skip(rel: str) -> bool:
    return any(rel.startswith(p) for p in SKIP_PREFIXES)


def add_theme_color(content: str) -> tuple[str, bool]:
    if 'name="theme-color"' in content:
        return content, False
    if "<head>" not in content:
        return content, False
    # Insert after charset+viewport block (immediately after the viewport meta if present)
    m = re.search(r'(<meta\s+name="viewport"[^>]*>)', content)
    if m:
        return content[:m.end()] + "\n" + THEME_COLOR_TAG + content[m.end():], True
    # Otherwise insert after <head>
    return content.replace("<head>", "<head>\n" + THEME_COLOR_TAG, 1), True


def add_rel_noopener(content: str) -> tuple[str, int]:
    # find <a ... target="_blank" ...> tags missing rel
    count = [0]
    def repl(m: re.Match) -> str:
        tag = m.group(0)
        if re.search(r'\brel\s*=', tag):
            # already has a rel — make sure it includes noopener+noreferrer
            existing = re.search(r'rel\s*=\s*"([^"]*)"', tag)
            if existing:
                vals = set(existing.group(1).split())
                changed = False
                if "noopener" not in vals:
                    vals.add("noopener"); changed = True
                if "noreferrer" not in vals:
                    vals.add("noreferrer"); changed = True
                if changed:
                    new_rel = " ".join(sorted(vals))
                    new_tag = re.sub(r'rel\s*=\s*"[^"]*"', f'rel="{new_rel}"', tag)
                    count[0] += 1
                    return new_tag
            return tag
        # no rel attr at all — add one
        count[0] += 1
        return tag[:-1] + ' rel="noopener noreferrer">'

    new = re.sub(r'<a\b[^>]*\btarget\s*=\s*"_blank"[^>]*>', repl, content)
    return new, count[0]


def add_reduced_motion(content: str) -> tuple[str, bool]:
    if REDUCED_MOTION_MARKER in content:
        return content, False
    # only inject if the page has its own <style>...</style> block AND uses animations
    if "<style" not in content:
        return content, False
    if "animation" not in content and "transition" not in content:
        return content, False
    # Insert just before the first </style>
    return content.replace("</style>", "  " + REDUCED_MOTION_BLOCK + "\n  </style>", 1), True


def main() -> int:
    pages = []
    for path in ROOT.rglob("*.html"):
        rel = str(path.relative_to(ROOT)).replace(os.sep, "/")
        if should_skip(rel):
            continue
        pages.append(path)

    pages.sort()
    theme_added = 0
    rel_total = 0
    rm_added = 0

    for page in pages:
        try:
            content = page.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = page.read_text(encoding="latin-1")

        new = content
        new, t = add_theme_color(new); theme_added += int(t)
        new, n = add_rel_noopener(new); rel_total += n
        new, rm = add_reduced_motion(new); rm_added += int(rm)

        if new != content:
            page.write_text(new, encoding="utf-8")

    print(f"Pages scanned       : {len(pages)}")
    print(f"theme-color added   : {theme_added}")
    print(f"rel=noopener fixed  : {rel_total}")
    print(f"reduced-motion added: {rm_added}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
