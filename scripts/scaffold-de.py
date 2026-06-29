#!/usr/bin/env python3
"""
scaffold-de.py <english-page> [<english-page> ...]

Create de/<page> as a structurally-correct German scaffold of an English
page: sets <html lang="de">, rewrites every site-relative href/src/srcset to
the correct RELATIVE path from the de/ location (pointing to ../de/<p> when a
German version of that target exists, else to the English file), fixes the
page's own canonical/og:url/JSON-LD self-URL to the /de/ URL, installs the
en/de/x-default hreflang trio, and stamps the freshness marker.

It does NOT translate text — run a translation pass afterward on the de/ file
(title, meta description, og/twitter text, visible body, JSON-LD human fields).
Paths and markers are already correct, so the translator must not touch them.
"""
import os, re, sys, hashlib, datetime, posixpath

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DE = os.path.join(ROOT, "de")
SITE = "https://charles-research.netlify.app"

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(65536), b""): h.update(c)
    return h.hexdigest()

def existing_de_set(extra):
    s = set(extra)
    for dp, _, fns in os.walk(DE):
        for fn in fns:
            if fn.endswith(".html") and "backup" not in fn.lower() and not fn.startswith("."):
                s.add(os.path.relpath(os.path.join(dp, fn), DE).replace(os.sep, "/"))
    return s

SKIP_SCHEMES = ("http://","https://","//","#","mailto:","tel:","data:","javascript:")

def rewrite_url(url, eng_dir, de_dir, de_set):
    u = url.strip()
    if not u or u.startswith(SKIP_SCHEMES): return url
    frag = ""
    if "#" in u:
        u, frag = u.split("#", 1); frag = "#" + frag
    if u == "":
        return url  # pure fragment
    # root-relative target of the english link, resolved from the english dir
    target = posixpath.normpath(posixpath.join(eng_dir, u))
    # german version exists?  -> point into de/
    de_target = ("de/" + target) if target in de_set else target
    rel = posixpath.relpath(de_target, de_dir)
    return rel + frag

def rewrite_srcset(val, eng_dir, de_dir, de_set):
    out = []
    for part in val.split(","):
        seg = part.strip()
        if not seg: continue
        bits = seg.split()
        bits[0] = rewrite_url(bits[0], eng_dir, de_dir, de_set)
        out.append(" ".join(bits))
    return ", ".join(out)

def scaffold(page, de_set):
    src = os.path.join(ROOT, page)
    if not os.path.exists(src): sys.exit(f"missing english: {page}")
    txt = open(src, encoding="utf-8").read()
    eng_dir = posixpath.dirname(page)
    de_dir = posixpath.normpath("de/" + eng_dir) if eng_dir else "de"

    # 1) <html lang="de">  — set on the <html> tag specifically (not the
    #    <!DOCTYPE html> that precedes it). If the tag already has a lang,
    #    rewrite it; otherwise add one. (Avoids a duplicate lang attribute.)
    if re.search(r'<html\b[^>]*\blang="', txt, re.I):
        txt = re.sub(r'(<html\b[^>]*\blang=")[^"]*(")', r'\1de\2', txt, count=1, flags=re.I)
    else:
        txt = re.sub(r'<html\b', '<html lang="de"', txt, count=1, flags=re.I)

    # 1b) localise locale + JSON-LD language codes
    txt = txt.replace('content="en_US"', 'content="de_DE"')
    txt = re.sub(r'("inLanguage":\s*)"en[-_]US"', r'\1"de-DE"', txt)

    # 2) rewrite href/src
    def attr_sub(m):
        attr, q, val = m.group(1), m.group(2), m.group(3)
        return f'{attr}={q}{rewrite_url(val, eng_dir, de_dir, de_set)}{q}'
    txt = re.sub(r'\b(href|src)=(")([^"]*)(?:")', attr_sub, txt)
    # 3) rewrite srcset
    def srcset_sub(m):
        return f'srcset="{rewrite_srcset(m.group(1), eng_dir, de_dir, de_set)}"'
    txt = re.sub(r'srcset="([^"]*)"', srcset_sub, txt)

    # 4) self-URL → /de/ URL (canonical, og:url, JSON-LD)
    txt = txt.replace(f"{SITE}/{page}", f"{SITE}/de/{page}")

    # 5) hreflang trio (remove existing alternate hreflang, insert standard)
    txt = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*"[^>]*>', '', txt)
    href_block = (f'<link rel="alternate" hreflang="en" href="{SITE}/{page}">\n'
                  f'<link rel="alternate" hreflang="de" href="{SITE}/de/{page}">\n'
                  f'<link rel="alternate" hreflang="x-default" href="{SITE}/{page}">\n')

    # NOTE: the freshness marker is intentionally NOT written here. A page is
    # only "in sync" once its TEXT has actually been translated; run
    #   python3 scripts/de-sync.py stamp <page>
    # after translating, and regenerate the manifest only then. A scaffolded but
    # untranslated page therefore shows as UNSTAMPED and must not be added to
    # assets/de-pages.js until translation is complete.

    # insert hreflang right after <meta charset...>
    m = re.search(r'(<meta charset="[^"]*">\s*)', txt, re.I)
    ins = href_block
    txt = (txt[:m.end()] + ins + txt[m.end():]) if m else txt.replace("</head>", ins + "</head>", 1)

    out = os.path.join(DE, page)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(txt)
    print(f"scaffolded de/{page}")

if __name__ == "__main__":
    pages = [p.strip().lstrip("/") for p in sys.argv[1:]]
    if not pages: sys.exit("usage: scaffold-de.py <page> [<page> ...]")
    de_set = existing_de_set(pages)
    for p in pages: scaffold(p, de_set)
