#!/usr/bin/env python3
"""Insert de-pages.js + lang-toggle.js <script> tags into every content
HTML page, right after the existing theme-toggle.js reference (so the
relative prefix matches). Idempotent. Skips backups/vendor dirs."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"node_modules", "_archive", "_backup_originals", "assets"}
def skip_dir(rel):
    parts = rel.split(os.sep)
    if any(p in SKIP_DIRS for p in parts): return True
    if any(p.startswith("_recovery") or p.startswith("_backup") for p in parts): return True
    return False

TT_RE = re.compile(r'^(\s*)<script defer src="([^"]*?)assets/theme-toggle\.js[^"]*"></script>\s*$')
changed, skipped, notag = [], [], []

for dirpath, dirnames, filenames in os.walk(ROOT):
    rel = os.path.relpath(dirpath, ROOT)
    rel = "" if rel == "." else rel
    dirnames[:] = [d for d in dirnames if not skip_dir(os.path.join(rel, d))]
    if rel and skip_dir(rel): continue
    for fn in filenames:
        if not fn.endswith(".html"): continue
        if "backup" in fn.lower(): continue
        fp = os.path.join(dirpath, fn)
        with open(fp, encoding="utf-8") as f:
            lines = f.readlines()
        if any("lang-toggle.js" in ln for ln in lines):
            skipped.append(os.path.relpath(fp, ROOT)); continue
        out, done = [], False
        for ln in lines:
            out.append(ln)
            if not done:
                m = TT_RE.match(ln.rstrip("\n"))
                if m:
                    indent, prefix = m.group(1), m.group(2)
                    out.append(f'{indent}<script defer src="{prefix}assets/de-pages.js?v=20260628"></script>\n')
                    out.append(f'{indent}<script defer src="{prefix}assets/lang-toggle.js?v=20260628"></script>\n')
                    done = True
        if done:
            with open(fp, "w", encoding="utf-8") as f:
                f.writelines(out)
            changed.append(os.path.relpath(fp, ROOT))
        else:
            notag.append(os.path.relpath(fp, ROOT))

print(f"Injected into {len(changed)} files.")
print(f"Already had toggle: {len(skipped)}")
print(f"No theme-toggle.js tag (skipped): {len(notag)}")
if notag:
    print("---- files without theme-toggle.js ----")
    for p in sorted(notag): print("  ", p)
