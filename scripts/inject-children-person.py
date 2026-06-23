#!/usr/bin/env python3
"""
Inject subject-Person schema.org JSON-LD for each of the 7 children of
Charles & Auguste, on their individual /children/ profile pages.

Parses each child page for birth/death dates, birth place, and FamilySearch
PID. Builds a Person block with:
- name, alternateName
- birthDate, birthPlace, deathDate (where known)
- parent → Charles, Auguste
- sameAs → FamilySearch URL

Bracketed by <!-- BEGIN-INJECTED-CHILD-PERSON --> markers.
"""
from __future__ import annotations
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://charles-konzen-research.netlify.app"

MARKER_BEGIN = "<!-- BEGIN-INJECTED-CHILD-PERSON -->"
MARKER_END = "<!-- END-INJECTED-CHILD-PERSON -->"

# Parents (referenced by @id)
CHARLES_ID = f"{BASE}/#charles"
AUGUSTE_ID = f"{BASE}/people/auguste-kreichelt.html#person"

# Per-child overrides (where extraction would be ambiguous)
CHILD_OVERRIDES = {
    "auguste.html":               {"name": "Auguste Gonsen", "alternate": ["Auguste Johnson"], "fs_pid": "L5N2-M8Y"},
    "bertha.html":                {"name": "Bertha Jansen", "alternate": ["Bertha Johnson"]},
    "erwin-carl-konsen.html":     {"name": "Erwin Carl Konsen", "alternate": ["Charles Johnson Jr."], "fs_pid": "KL18-V2Y"},
    "friedrich-wilhelm.html":     {"name": "Friedrich Wilhelm Gonnson", "alternate": ["Frederick Johnson"]},
    "josephine-maria.html":       {"name": "Josephine Maria"},
    "katherine-carolina.html":    {"name": "Katherine Carolina Gansen", "alternate": ["Katherine Johnson"]},
    "louise.html":                {"name": "Louise Jansen", "alternate": ["Louise Foster"]},
}


def parse_dates(s: str) -> dict:
    """Extract birth and death dates from various page patterns."""
    out = {}
    # Look for "Born <date>" or "<date> · Born"
    m = re.search(r'Born[:\s]+(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})', s)
    if m:
        out['birthDate_raw'] = m.group(1)
        # Parse to ISO if possible
        try:
            from datetime import datetime
            dt = datetime.strptime(m.group(1), "%d %B %Y")
            out['birthDate'] = dt.date().isoformat()
        except Exception:
            pass
    # Death date
    m = re.search(r'Died[:\s]+(\d{4})', s)
    if m:
        out['deathYear'] = m.group(1)
    m = re.search(r'Died[:\s]+(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})', s)
    if m:
        try:
            from datetime import datetime
            dt = datetime.strptime(m.group(1), "%d %B %Y")
            out['deathDate'] = dt.date().isoformat()
        except Exception:
            pass
    # Birth place
    m = re.search(r'Born[^<]*?,?\s*((?:St\.\s+Louis|Trendelburg)[^<]*?)(?:<|\.)', s)
    if m:
        out['birthPlace'] = m.group(1).strip().rstrip(',. ')
    return out


def parse_fs_pid(s: str, page_name: str) -> str | None:
    override = CHILD_OVERRIDES.get(page_name, {}).get("fs_pid")
    if override:
        return override
    m = re.search(r'familysearch\.org/tree/person/details/([A-Z0-9]{4}-[A-Z0-9]{3,4})', s)
    if m:
        return m.group(1)
    return None


def build_person(p: Path) -> dict:
    s = p.read_text(encoding="utf-8")
    name = p.stem
    over = CHILD_OVERRIDES.get(p.name, {})
    display_name = over.get("name", name.replace("-", " ").title())
    page_url = f"{BASE}/children/{p.name}"

    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": f"{page_url}#person",
        "name": display_name,
        "url": page_url,
        "parent": [
            {"@id": CHARLES_ID, "@type": "Person", "name": "Charles Konzen"},
            {"@id": AUGUSTE_ID, "@type": "Person", "name": "Auguste Kreichelt"},
        ],
        "nationality": "American",
    }
    if "alternate" in over:
        person["alternateName"] = over["alternate"]

    dates = parse_dates(s)
    if "birthDate" in dates:
        person["birthDate"] = dates["birthDate"]
    elif "birthDate_raw" in dates:
        person["birthDate"] = dates["birthDate_raw"]
    if "deathDate" in dates:
        person["deathDate"] = dates["deathDate"]
    elif "deathYear" in dates:
        person["deathDate"] = dates["deathYear"]
    if "birthPlace" in dates:
        person["birthPlace"] = {
            "@type": "Place",
            "name": dates["birthPlace"],
        }
    pid = parse_fs_pid(s, p.name)
    if pid:
        person["sameAs"] = [f"https://www.familysearch.org/tree/person/details/{pid}"]
    return person


def inject(p: Path) -> str:
    if p.name == "index.html":
        return "skipped"
    s = p.read_text(encoding="utf-8")
    person = build_person(p)
    block = MARKER_BEGIN + "\n<script type=\"application/ld+json\">\n" + json.dumps(person, indent=2, ensure_ascii=False) + "\n</script>\n" + MARKER_END
    if MARKER_BEGIN in s:
        new = re.sub(
            re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END),
            block,
            s,
            count=1,
            flags=re.DOTALL,
        )
    else:
        new = s.replace("</head>", block + "\n</head>", 1)
    if new != s:
        p.write_text(new, encoding="utf-8")
        return "updated"
    return "no-change"


def main() -> int:
    children_dir = ROOT / "children"
    counts = {"updated": 0, "no-change": 0, "skipped": 0}
    for p in sorted(children_dir.glob("*.html")):
        status = inject(p)
        counts[status] = counts.get(status, 0) + 1
        if status == "updated":
            print(f"  ✓ {p.relative_to(ROOT)}")
    print(f"\nUpdated: {counts['updated']}  No-change: {counts['no-change']}  Skipped: {counts['skipped']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
