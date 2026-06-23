#!/usr/bin/env python3
"""
Add stable anchor ids to every <dt> in glossary.html so other pages can
deep-link to specific glossary terms with glossary.html#term-id.

Idempotent: only touches dt elements that don't already have an id.
"""
from __future__ import annotations
import re
import unicodedata
from pathlib import Path

ROOT = Path("/sessions/great-friendly-turing/mnt/Charles Gannsen Research")
GLOSSARY = ROOT / "glossary.html"


def slugify(text: str) -> str:
    """Generate a stable URL slug from the term name."""
    # Strip HTML
    text = re.sub(r"<[^>]+>", "", text)
    # Take only the term (before " DE" / " EN" suffix), and only the first
    # canonical name before slashes / parentheses / spaces.
    text = re.sub(r"\s+(DE|EN|DE/EN|EN/DE)(?:\s|/).*", "", text)
    text = re.sub(r"\s+(DE|EN|DE/EN|EN/DE)$", "", text)
    # Take first variant before " / "
    text = text.split(" / ")[0].strip()
    # Remove pronunciation /.../ guides
    text = re.sub(r"/[^/]+/", "", text).strip()
    # Strip leading quotes/punctuation
    text = text.strip("\"' .")
    # Take first parenthetical-free token group
    text = re.sub(r"\s*\([^)]*\)\s*", " ", text).strip()
    # Normalize unicode and lowercase
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    # Replace any non-alphanumeric with hyphens
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text


def add_ids():
    html = GLOSSARY.read_text(encoding="utf-8")
    original = html
    seen = set()

    def repl(match):
        attrs = match.group(1) or ""
        inner = match.group(2)
        if 'id=' in attrs:
            return match.group(0)
        slug = slugify(inner)
        if not slug or slug in seen:
            # Disambiguate duplicates
            base = slug or "term"
            n = 2
            while f"{base}-{n}" in seen:
                n += 1
            slug = f"{base}-{n}"
        seen.add(slug)
        return f'<dt{attrs} id="g-{slug}">{inner}</dt>'

    html = re.sub(
        r"<dt([^>]*)>(.*?)</dt>",
        repl,
        html,
        flags=re.DOTALL,
    )

    if html == original:
        print("No changes (all dt elements already have ids, or pattern mismatch).")
    else:
        GLOSSARY.write_text(html, encoding="utf-8")
        print(f"Glossary updated: added ids to {len(seen)} unique dt elements.")
        for s in sorted(seen):
            print(f"  #g-{s}")


if __name__ == "__main__":
    add_ids()
