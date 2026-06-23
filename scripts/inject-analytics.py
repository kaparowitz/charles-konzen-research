#!/usr/bin/env python3
"""
Inject a privacy-respecting Plausible analytics tag into every public HTML page.

Default state: COMMENTED OUT.  Once you sign up at https://plausible.io and add
the site, edit `PLAUSIBLE_DOMAIN` below to your tracking domain (e.g.
"charles-konzen-research.netlify.app") and re-run this script with
`--enable` to flip the tag live.

Rules:
  - Skip /notes/ (working drafts, noindex)
  - Skip /_archive*/, /_backup_originals/
  - Idempotent — replaces existing injection if rerun

Usage:
    python3 scripts/inject-analytics.py            # inject commented-out scaffold
    python3 scripts/inject-analytics.py --enable   # inject live tag
    python3 scripts/inject-analytics.py --remove   # strip the scaffold entirely
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# === Edit this once you have a Plausible account ============================
PLAUSIBLE_DOMAIN = "charles-konzen-research.netlify.app"
# ============================================================================

BEGIN = "<!-- BEGIN-INJECTED-ANALYTICS -->"
END = "<!-- END-INJECTED-ANALYTICS -->"

SKIP_PREFIXES = ("notes/", "_archive", "_backup_originals/", "scripts/")


def build_block(enabled: bool) -> str:
    tag = (
        f'<script defer data-domain="{PLAUSIBLE_DOMAIN}" '
        f'src="https://plausible.io/js/script.js"></script>'
    )
    if enabled:
        return f"{BEGIN}\n{tag}\n{END}"
    # Disabled by default — leave the tag in an HTML comment so flipping on
    # is a one-line edit.
    return (
        f"{BEGIN}\n"
        f"<!-- Plausible privacy-first analytics (no cookies, GDPR-clean).\n"
        f"     Sign up at https://plausible.io, add the site, then run\n"
        f"     `python3 scripts/inject-analytics.py --enable` to activate.\n"
        f"{tag}\n"
        f"-->\n"
        f"{END}"
    )


def head_inject(content: str, block: str) -> str:
    """Insert the analytics block before </head>, idempotently."""
    if BEGIN in content:
        return re.sub(
            re.escape(BEGIN) + r".*?" + re.escape(END),
            block,
            content,
            count=1,
            flags=re.DOTALL,
        )
    if "</head>" in content:
        return content.replace("</head>", f"  {block}\n</head>", 1)
    return content


def head_remove(content: str) -> str:
    if BEGIN not in content:
        return content
    return re.sub(
        r"\s*" + re.escape(BEGIN) + r".*?" + re.escape(END) + r"\s*",
        "\n",
        content,
        count=1,
        flags=re.DOTALL,
    )


def is_skipped(rel: Path) -> bool:
    s = str(rel).replace("\\", "/")
    return any(s.startswith(p) for p in SKIP_PREFIXES)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--enable", action="store_true", help="activate the live tag")
    ap.add_argument("--remove", action="store_true", help="strip the scaffold entirely")
    args = ap.parse_args(argv)

    block = build_block(enabled=args.enable)
    pages = [p for p in ROOT.rglob("*.html") if not is_skipped(p.relative_to(ROOT))]
    n_changed = 0
    for p in pages:
        try:
            content = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = head_remove(content) if args.remove else head_inject(content, block)
        if new != content:
            p.write_text(new, encoding="utf-8")
            n_changed += 1
    state = "enabled" if args.enable else ("removed" if args.remove else "scaffolded (commented-out)")
    print(f"Plausible analytics {state} on {n_changed} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
