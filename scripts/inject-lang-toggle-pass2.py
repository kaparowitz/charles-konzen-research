#!/usr/bin/env python3
"""Pass 2: add toggle to genuine public content pages that lack a
theme-toggle.js anchor. Insert before </head>. Skip redirect stubs,
internal notes/notes_view/autoclusters, backups, vendor dirs."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"node_modules","_archive","_backup_originals","assets",
             "notes","notes_view","autoclusters_2026-06-07","peter_charts","data","wikidata"}
def skip_dir(rel):
    parts = rel.split(os.sep)
    if any(p in SKIP_DIRS for p in parts): return True
    if any(p.startswith("_recovery") or p.startswith("_backup") for p in parts): return True
    return False

added, redirects, nohead = [], [], []
for dirpath, dirnames, filenames in os.walk(ROOT):
    rel = os.path.relpath(dirpath, ROOT); rel = "" if rel=="." else rel
    dirnames[:] = [d for d in dirnames if not skip_dir(os.path.join(rel,d))]
    if rel and skip_dir(rel): continue
    for fn in filenames:
        if not fn.endswith(".html") or "backup" in fn.lower(): continue
        fp = os.path.join(dirpath, fn)
        txt = open(fp, encoding="utf-8").read()
        if "lang-toggle.js" in txt: continue           # already done in pass 1
        low = txt.lower()
        if 'http-equiv="refresh"' in low or 'redirecting' in low:
            redirects.append(os.path.relpath(fp,ROOT)); continue
        if "</head>" not in txt:
            nohead.append(os.path.relpath(fp,ROOT)); continue
        depth = 0 if rel=="" else rel.count(os.sep)+1
        prefix = "../"*depth
        tags = (f'<script defer src="{prefix}assets/de-pages.js?v=20260628"></script>\n'
                f'<script defer src="{prefix}assets/lang-toggle.js?v=20260628"></script>\n')
        txt = txt.replace("</head>", tags + "</head>", 1)
        open(fp,"w",encoding="utf-8").write(txt)
        added.append(os.path.relpath(fp,ROOT))

print(f"Added to {len(added)} content pages:")
for p in sorted(added): print("  ", p)
print(f"Redirect stubs skipped: {len(redirects)}")
print(f"No </head> skipped: {len(nohead)}", *sorted(nohead), sep="\n  " if nohead else "")
