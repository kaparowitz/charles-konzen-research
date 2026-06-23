#!/usr/bin/env python3
"""
Add a <link rel="stylesheet" href="…assets/dark-mode.css"> immediately
after the existing theme.css link on every standalone HTML page.
Idempotent.
"""
from __future__ import annotations
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = ("notes/", "_archive", "_backup_originals/", "scripts/")


def relative_root_for(page: Path) -> str:
    rel = page.relative_to(ROOT)
    depth = len(rel.parts) - 1
    return "../" * depth


pages = []
for p in ROOT.rglob("*.html"):
    rel = str(p.relative_to(ROOT)).replace(os.sep, "/")
    if any(rel.startswith(s) for s in SKIP):
        continue
    pages.append(p)

added = 0
already = 0
for p in pages:
    try:
        c = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        c = p.read_text(encoding="latin-1")
    if "dark-mode.css" in c:
        already += 1
        continue
    prefix = relative_root_for(p)
    # Insert after the LAST theme.css or cinematic.css link in <head>
    m = list(re.finditer(r'<link[^>]*href="[^"]*(?:cinematic|theme)\.css"[^>]*>', c))
    if not m:
        # fallback — insert before </head>
        if "</head>" in c:
            new = c.replace("</head>", f'<link rel="stylesheet" href="{prefix}assets/dark-mode.css">\n</head>', 1)
        else:
            continue
    else:
        last = m[-1]
        new = c[: last.end()] + f'\n<link rel="stylesheet" href="{prefix}assets/dark-mode.css">' + c[last.end():]
    if new != c:
        p.write_text(new, encoding="utf-8")
        added += 1

print(f"Pages scanned : {len(pages)}")
print(f"dark-mode.css added: {added}")
print(f"Already had it     : {already}")
