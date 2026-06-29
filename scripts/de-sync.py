#!/usr/bin/env python3
"""
de-sync.py — keep the German (/de/) mirror in sync with English sources.

Each translated German page embeds three marker meta tags recording WHICH
English page it was translated from and a SHA-256 of that English source at
translation time:

  <meta name="x-translated-from"       content="contribute.html">
  <meta name="x-translated-source-sha" content="<sha256>">
  <meta name="x-translated-date"       content="2026-06-28">

Subcommands
-----------
  stamp <page> [--date YYYY-MM-DD]
        (Re)write the marker tags in de/<page> using the CURRENT hash of the
        English source <page>. Run this right after translating/updating a page.

  check [--quiet]
        Compare every de/*.html marker against the current English source hash.
        Prints UP-TO-DATE / STALE / NO-SOURCE / UNSTAMPED per page, plus a list
        of public English pages that have NO German translation yet.
        Exit code 2 if any page is STALE (English changed since translation).

  list-stale
        Print only the English page paths whose German translation is stale
        (one per line) — convenient for feeding a re-translation loop.
"""
import os, re, sys, hashlib, argparse, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DE = os.path.join(ROOT, "de")

SKIP_DIRS = {"node_modules","_archive","_backup_originals","assets","de",
             "notes","notes_view","autoclusters_2026-06-07","peter_charts",
             "data","wikidata","evidence_images","evidence_thumbs","family_photos",
             "nara_ocr","nara_pages"}

def skip_dir(rel):
    parts = rel.split(os.sep)
    if any(p in SKIP_DIRS for p in parts): return True
    return any(p.startswith("_recovery") or p.startswith("_backup") for p in parts)

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def english_pages():
    """Public English content pages (exclude redirects, backups, internal notes)."""
    out = []
    for dp, dns, fns in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT); rel = "" if rel == "." else rel
        dns[:] = [d for d in dns if not skip_dir(os.path.join(rel, d))]
        if rel and skip_dir(rel): continue
        for fn in fns:
            if not fn.endswith(".html") or "backup" in fn.lower(): continue
            fp = os.path.join(dp, fn)
            low = open(fp, encoding="utf-8", errors="ignore").read(2000).lower()
            if 'http-equiv="refresh"' in low or 'redirecting' in low: continue
            out.append(os.path.relpath(fp, ROOT))
    return sorted(out)

MARK_RE = {
    "from": re.compile(r'<meta name="x-translated-from" content="([^"]*)">'),
    "sha":  re.compile(r'<meta name="x-translated-source-sha" content="([^"]*)">'),
    "date": re.compile(r'<meta name="x-translated-date" content="([^"]*)">'),
}

def read_markers(de_path):
    txt = open(de_path, encoding="utf-8").read()
    return {k: (m.group(1) if (m := r.search(txt)) else None) for k, r in MARK_RE.items()}

def stamp(page, date=None):
    src = os.path.join(ROOT, page)
    de_path = os.path.join(DE, page)
    if not os.path.exists(src): sys.exit(f"English source not found: {page}")
    if not os.path.exists(de_path): sys.exit(f"German page not found: de/{page}")
    date = date or datetime.date.today().isoformat()
    digest = sha(src)
    block = (f'<meta name="x-translated-from" content="{page}">\n'
             f'<meta name="x-translated-source-sha" content="{digest}">\n'
             f'<meta name="x-translated-date" content="{date}">\n')
    txt = open(de_path, encoding="utf-8").read()
    # remove any existing markers, then insert fresh block after <meta charset...>
    for r in MARK_RE.values():
        txt = re.sub(r.pattern + r"\s*", "", txt)
    m = re.search(r'(<meta charset="[^"]*">\s*)', txt, re.I)
    if m:
        txt = txt[:m.end()] + block + txt[m.end():]
    else:
        txt = txt.replace("</head>", block + "</head>", 1)
    open(de_path, "w", encoding="utf-8").write(txt)
    print(f"stamped de/{page}  sha={digest[:12]}…  date={date}")

def de_pages():
    out = []
    for dp, dns, fns in os.walk(DE):
        for fn in fns:
            if fn.endswith(".html") and "backup" not in fn.lower() and not fn.startswith("."):
                out.append(os.path.relpath(os.path.join(dp, fn), DE))
    return sorted(out)

def check(quiet=False, only_stale=False):
    stale = []
    rows = []
    for page in de_pages():
        de_path = os.path.join(DE, page)
        mk = read_markers(de_path)
        if not mk["from"]:
            rows.append(("UNSTAMPED", page, "manual/curated page — not auto-synced")); continue
        src = os.path.join(ROOT, mk["from"])
        if not os.path.exists(src):
            rows.append(("NO-SOURCE", page, f"english {mk['from']} missing")); continue
        cur = sha(src)
        if cur == mk["sha"]:
            rows.append(("UP-TO-DATE", page, mk["from"]))
        else:
            rows.append(("STALE", page, mk["from"]))
            stale.append(mk["from"])
    if only_stale:
        for s in stale: print(s)
        return 2 if stale else 0
    untranslated = [p for p in english_pages() if not os.path.exists(os.path.join(DE, p))]
    if not quiet:
        for status, page, info in rows:
            print(f"  [{status:10}] de/{page:32} ← {info}")
        print(f"\nSummary: {sum(1 for r in rows if r[0]=='UP-TO-DATE')} up-to-date, "
              f"{len(stale)} stale, "
              f"{sum(1 for r in rows if r[0]=='UNSTAMPED')} unstamped, "
              f"{len(untranslated)} English pages not yet translated.")
        if stale:
            print("\nSTALE (English changed since translation):")
            for s in stale: print("  -", s)
    return 2 if stale else 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("stamp"); sp.add_argument("page"); sp.add_argument("--date")
    sub.add_parser("check").add_argument("--quiet", action="store_true")
    sub.add_parser("list-stale")
    a = ap.parse_args()
    if a.cmd == "stamp": stamp(a.page, a.date)
    elif a.cmd == "check": sys.exit(check(quiet=a.quiet))
    elif a.cmd == "list-stale": sys.exit(check(only_stale=True))
