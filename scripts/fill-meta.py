#!/usr/bin/env python3
"""
Fill in missing <meta name="description"> and <link rel="canonical">
on every public HTML page.

For meta description: extract the first 160 chars of meaningful body prose
(after stripping nav, header, scripts, styles) and use as default.

For canonical: derive from the page's repo-relative path.
"""
from __future__ import annotations
import os
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://charles-konzen-research.netlify.app"


def derive_canonical(rel: str) -> str:
    """Repo-relative path → absolute canonical URL."""
    # Pretty URLs: drop /index.html
    if rel == "index.html":
        loc = ""
    elif rel.endswith("/index.html"):
        loc = rel[:-10]
    else:
        loc = rel
    # URL-encode spaces but preserve slashes
    parts = loc.split("/")
    parts = [quote(p, safe="") for p in parts]
    loc = "/".join(parts)
    return f"{BASE}/{loc}" if loc else f"{BASE}/"


def derive_description(s: str) -> str | None:
    """Extract a sensible 160-char description from body prose."""
    # Drop scripts, styles, nav, header, footer, head
    clean = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.DOTALL)
    clean = re.sub(r'<style[^>]*>.*?</style>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<head[^>]*>.*?</head>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<nav[^>]*>.*?</nav>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<header[^>]*>.*?</header>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<footer[^>]*>.*?</footer>', '', clean, flags=re.DOTALL)
    # Try .lede first
    m = re.search(r'<p[^>]*class="[^"]*\blede\b[^"]*"[^>]*>(.*?)</p>', clean, re.DOTALL)
    if not m:
        # Try .bottom-line
        m = re.search(r'<p[^>]*class="[^"]*\bbottom-line\b[^"]*"[^>]*>(.*?)</p>', clean, re.DOTALL)
    if not m:
        # First <p> with substantial content (>120 chars)
        for cand in re.finditer(r'<p[^>]*>(.*?)</p>', clean, re.DOTALL):
            text = re.sub(r'<[^>]+>', '', cand.group(1)).strip()
            if len(text) > 120:
                m = cand
                break
    if not m:
        return None
    text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    text = re.sub(r'\s+', ' ', text)
    # Decode common HTML entities
    text = text.replace("&amp;", "&").replace("&nbsp;", " ").replace("&mdash;", "—").replace("&ndash;", "–")
    text = text.replace("&quot;", '"').replace("&apos;", "'").replace("&lt;", "<").replace("&gt;", ">")
    if len(text) > 200:
        text = text[:197].rsplit(' ', 1)[0] + "…"
    return text or None


def inject(p: Path) -> dict:
    rel = p.relative_to(ROOT).as_posix()
    if rel.startswith(("notes/", "_archive", "_backup_originals/", "_deploy_netlify/", "scripts/")):
        return {"skipped": 1}
    s = p.read_text(encoding="utf-8")
    if len(s) < 1500 or '<meta http-equiv="refresh"' in s:
        return {"skipped": 1}
    if "</head>" not in s:
        return {"skipped": 1}
    orig = s
    actions = {"updated": 0, "desc_added": 0, "canonical_added": 0, "dupe_fixed": 0}

    # 1. De-duplicate meta description if more than one
    desc_count = len(re.findall(r'<meta\s+name="description"\s+content="', s))
    if desc_count > 1:
        # Keep the first, remove subsequent
        seen = [False]
        def repl_desc(m):
            if seen[0]:
                return ""
            seen[0] = True
            return m.group(0)
        s = re.sub(r'<meta\s+name="description"\s+content="[^"]*">\s*\n?', repl_desc, s)
        actions["dupe_fixed"] = 1

    # 2. De-duplicate og:type if more than one
    ogt_count = len(re.findall(r'<meta\s+property="og:type"', s))
    if ogt_count > 1:
        seen = [False]
        def repl_ogt(m):
            if seen[0]:
                return ""
            seen[0] = True
            return m.group(0)
        s = re.sub(r'<meta\s+property="og:type"\s+content="[^"]*">\s*\n?', repl_ogt, s)
        # Also de-dupe og:title, og:description, og:url that often go together
        for prop in ("og:title", "og:description", "og:url", "twitter:title", "twitter:description"):
            cnt = len(re.findall(rf'<meta\s+(?:property|name)="{re.escape(prop)}"', s))
            if cnt > 1:
                seen2 = [False]
                def _r(m, seen2=seen2):
                    if seen2[0]:
                        return ""
                    seen2[0] = True
                    return m.group(0)
                s = re.sub(rf'<meta\s+(?:property|name)="{re.escape(prop)}"\s+content="[^"]*">\s*\n?', _r, s)
        actions["dupe_fixed"] = 1

    # 3. Add meta description if missing
    has_desc = '<meta name="description"' in s
    if not has_desc:
        desc = derive_description(orig)
        if desc:
            # Escape quotes for attribute value
            esc = desc.replace('"', '&quot;')
            tag = f'<meta name="description" content="{esc}">\n'
            # Insert right after <title> or before </head>
            if '<title>' in s:
                s = re.sub(r'(</title>\s*\n?)', r'\1' + tag, s, count=1)
            else:
                s = s.replace('</head>', tag + '</head>', 1)
            actions["desc_added"] = 1

    # 4. Add canonical if missing
    has_canon = '<link rel="canonical"' in s
    if not has_canon:
        canon = derive_canonical(rel)
        tag = f'<link rel="canonical" href="{canon}">\n'
        if '</title>' in s:
            s = re.sub(r'(</title>\s*\n?)', r'\1' + tag, s, count=1)
        else:
            s = s.replace('</head>', tag + '</head>', 1)
        actions["canonical_added"] = 1

    if s != orig:
        p.write_text(s, encoding="utf-8")
        actions["updated"] = 1
    return actions


def main() -> int:
    totals = {"updated": 0, "desc_added": 0, "canonical_added": 0, "dupe_fixed": 0, "skipped": 0}
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(("notes/", "_archive", "_backup_originals/", "_deploy_netlify/", "scripts/")):
            continue
        result = inject(p)
        for k, v in result.items():
            totals[k] = totals.get(k, 0) + v
    print(f"Pages updated: {totals['updated']}")
    print(f"  meta descriptions added: {totals['desc_added']}")
    print(f"  canonical URLs added:    {totals['canonical_added']}")
    print(f"  duplicate metas fixed:   {totals['dupe_fixed']}")
    print(f"  skipped:                 {totals['skipped']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
