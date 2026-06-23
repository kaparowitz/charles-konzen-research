#!/usr/bin/env python3
"""
Archive superseded versioned drafts in /notes/.

Keep only the latest version of each artifact group. Move all earlier
versions to _archive/notes/ — preserving the file (recoverable) but
removing it from the live deploy. Session notes are LEFT IN PLACE
(they are unique sessions, not versioned drafts) but already have
robots noindex from a previous step.
"""
from __future__ import annotations
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
ARCHIVE = ROOT / "_archive" / "notes"

# Patterns whose latest version we keep, archive the rest.
GROUPS = [
    # Kontze_Konze_Complete_Family_Reconstruction_AprilDD_2026[_vNN].html
    re.compile(r"^Kontze_Konze_Complete_Family_Reconstruction_.*\.html$"),
    # Research_Paper_for_Peter_Schrader_AprilDD_2026[_vNN].html
    re.compile(r"^Research_Paper_for_Peter_Schrader_.*\.html$"),
    # Research_Paper_AprilDD_2026.html
    re.compile(r"^Research_Paper_.*_2026.*\.html$"),
    # Message_for_Peter_Schrader_*.html
    re.compile(r"^Message_for_Peter_Schrader_.*\.html$"),
]


def version_key(filename: str) -> tuple:
    """
    Sort key that puts the latest version last.
    Picks up dates like AprilNN_2026 and explicit _vNN suffix.
    """
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
        "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
        "November": 11, "December": 12,
    }
    m = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)(\d+)_(\d{4})",
        filename,
    )
    year = int(m.group(3)) if m else 0
    month = months.get(m.group(1), 0) if m else 0
    day = int(m.group(2)) if m else 0
    v = re.search(r"_v(\d+)", filename)
    vnum = int(v.group(1)) if v else 0
    # tiebreaker: _evening / _update / _v<n>
    has_evening = 1 if "_evening" in filename else 0
    has_update = 1 if "_update" in filename else 0
    return (year, month, day, vnum, has_evening, has_update, filename)


def main() -> int:
    ARCHIVE.mkdir(parents=True, exist_ok=True)

    # Group files by which pattern they match
    files = sorted(p for p in NOTES.iterdir() if p.is_file() and p.suffix == ".html")

    grouped: dict[int, list[Path]] = {}
    ungrouped: list[Path] = []
    for f in files:
        idx = None
        for i, pat in enumerate(GROUPS):
            if pat.match(f.name):
                idx = i
                break
        if idx is None:
            ungrouped.append(f)
        else:
            grouped.setdefault(idx, []).append(f)

    moved = 0
    kept = []

    for idx, group in grouped.items():
        # sort, keep last (latest), archive rest
        group.sort(key=lambda p: version_key(p.name))
        latest = group[-1]
        kept.append(latest)
        for f in group[:-1]:
            target = ARCHIVE / f.name
            shutil.move(str(f), str(target))
            moved += 1

    # Print summary
    print(f"Files in /notes/ before : {len(files)}")
    print(f"Moved to _archive/notes/: {moved}")
    print(f"Kept in /notes/         : {len(files) - moved}")
    print()
    print("Latest versions kept (one per group):")
    for f in sorted(kept):
        print(f"  {f.relative_to(ROOT).as_posix()}")
    print()
    print(f"Ungrouped (kept as-is) : {len(ungrouped)}  (Session notes etc.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
