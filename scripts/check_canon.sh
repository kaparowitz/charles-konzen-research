#!/usr/bin/env bash
# check_canon.sh — Pre-commit guard against the propagation-cascade bug-class.
#
# Every time a canonical metric changes on Charles Konzen Research, stale instances
# of the old value tend to survive in the surfaces that are easy to forget:
#   - <meta name="description">      - <meta property="og:description">
#   - <meta name="twitter:description">  - JSON-LD "description" / "headline"
#   - <title>                            - <h1>
#   - alt="..." attributes               - <figcaption>
#   - <text> elements inside SVG figures
#
# This script greps the entire site for the *old, retracted* forms of canonical
# claims. A clean run prints nothing; a finding means a stale instance survived.
#
# Usage:  bash scripts/check_canon.sh
# Exit:   0 if clean, 1 if anything was found.

set -u

SITE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SITE_ROOT" || exit 2

# Files to scan: every .html plus selected static files
SCAN_GLOBS=(
  "*.html" "**/*.html"
  "feed.xml" "sitemap.xml"
)

FOUND=0

# ── Helper: grep that prints "[label] file:line:match" and updates FOUND ──────
# Pass a leading 'warn' or 'fail' as $1 to control whether the check affects
# the exit code. 'warn' checks print findings but do not fail CI.
flag() {
  local severity="fail"
  if [[ "$1" == "warn" || "$1" == "fail" ]]; then severity="$1"; shift; fi
  local label="$1" pattern="$2"
  # -n line numbers, -E regex, -I skip binary, -r recursive, --include=*.html
  # We scan all HTML + XML feed/sitemap. Skip _backup_originals and _archive.
  local hits
  hits=$(grep -rnE -I \
          --include='*.html' --include='feed.xml' --include='sitemap.xml' \
          --exclude-dir='_backup_originals' --exclude-dir='_archive' \
          --exclude-dir='.git' --exclude-dir='.netlify' \
          --exclude-dir='notes' --exclude-dir='notes_view' --exclude-dir='session_notes_docx' \
          --exclude='errata.html' --exclude='changelog.html' \
          -- "$pattern" . 2>/dev/null) || true
  # Also exclude the John Heitzenberger page itself (it legitimately discusses
  # "John Hitzelberger" as a candidate reading under hypothesis 2).
  hits=$(echo "$hits" | grep -vE 'people/john-heitzenberger\.html' || true)
  if [[ -n "$hits" ]]; then
    if [[ "$severity" == "fail" ]]; then FOUND=1; fi
    echo "──────────────────────────────────────────────────────────────────"
    echo "  [$severity: $label]"
    echo "──────────────────────────────────────────────────────────────────"
    echo "$hits"
    echo
  fi
}

echo "Charles Konzen Research — canon guard"
echo "site root: $SITE_ROOT"
echo

# ── #1 Surname-count cascade ──────────────────────────────────────────────────
# Canon: 9 American spellings · 9 attestations · 5 scribes · 30 years
#        (1895 Gould's St. Louis directory "Gannsen" added 21 Jun 2026)
flag "stale: 'seven attestations' (should be 'nine attestations')" \
     'seven attestations|7 attestations'
flag "stale: '7 American renderings' (should be 9) — exclude prose about ranks/sons" \
     '7 American (renderings|spellings|attestations)'
flag "stale: 'eight attestations' (should be 'nine attestations')" \
     'eight attestations|8 attestations'
flag "stale: '8 American renderings' (should be 9)" \
     '8 American (renderings|spellings|attestations)'
flag "stale: 'eight (distinct) American spellings/renderings' (should be nine)" \
     'eight (distinct )?American (renderings|spellings|captures)'
flag "stale: 'Six of (the) eight … collapse' (should be 'Six of nine')" \
     'Six of (the )?eight'
flag "stale: 'six different ways' for children's surnames (should be five)" \
     'six different ways across the seven baptisms'
flag "stale: 'five distinct parish-clerk renderings' without subset framing — should clarify it's the children's-baptism subset" \
     'five distinct parish-clerk renderings'

# ── #2 Freundberg vs Freundburg ───────────────────────────────────────────────
# Canon: Freundburg (with -burg)
flag "stale: 'Freundberg' (should be 'Freundburg')" \
     'Freundberg'

# ── #3 Hitzelberger / Heitzenberger framing ───────────────────────────────────
# Canon: clerk wrote 'Heitzenberger'; surname-family identified as Hitzelberger;
# the SPECIFIC INDIVIDUAL identity remains open. Bare 'John Hitzelberger'
# without that hedge asserts an open hypothesis as fact.
flag "stale: bare 'John Hitzelberger' without 'identity open' hedge — exclude bibliography (now fixed) and people page itself" \
     'John Hitzelberger[^—<]'

# ── #4 Session count ──────────────────────────────────────────────────────────
# Canon: 78+
flag "stale: '80+ sessions' (canon is '78+')" \
     '80\+ (research )?sessions'
flag "stale: 'more than eighty' sessions (canon is '78+')" \
     'more than eighty (research )?sessions|over eighty (research )?sessions'

# ── #5 Death-date sources ─────────────────────────────────────────────────────
# Canon: 16 December 1903 from parish register (Doc N); Doc A reads 17 December —
# the 1-day discrepancy must be FLAGGED, not silently flattened. This check
# finds prose 'died 16 ... 1903' lines that lack a sibling reference to the
# crosswalk/errata. It's heuristic; review the hits.
flag warn "a '16 [Dec|December] 1903' string — review whether it needs the Doc A/N discrepancy footnote (most timeline/SVG references do not)" \
     '16 (Dec|December) 1903'
# (this flag will likely have legitimate matches — e.g. timeline SVG labels.
#  The goal is to surface them for review, not to fail CI.)

# ── #6 Surname pool wording — '5 scribes' check ───────────────────────────────
# Canon phrasing: "5 independent scribes" or "five scribes"
# An old draft sometimes said "five+ independent scribes" — keep one form.
flag "stale: 'five+ independent scribes' (pick 'five independent scribes' or note 'five+ scribes — additional scribes possible')" \
     'five\+ independent scribes'

# ── #7 Phrases of canonical concern in OG/meta surfaces only ──────────────────
# This sub-check is stricter: anything matching the old surname trail '5 ...
# scribes' or '7 ... attestations' inside an OG/meta/JSON-LD line is high-cost.
flag "high-cost: stale count inside meta/og/jsonld description — usually rendered in link previews" \
     '(meta[^>]*description|"description"|og:description|twitter:description)[^>]*(seven attestations|7 attestations|six different ways across the seven baptisms|Freundberg|five distinct parish-clerk renderings)'

# ── Stories pages confidence-check ────────────────────────────────────────────
# The 9 stories/*.html pages were audited clean on 29 May 2026 (Round 6).
# This block re-verifies they haven't drifted: each story is grep'd for the
# canon-violating phrases as a fast smoke test. If a stories page picks up
# a stale canon phrase in a future edit, deploy aborts.
if [[ -d ./stories ]]; then
  story_hits=$(grep -rnE -I --include='*.html' \
    'Freundberg|seven attestations|7 attestations|eight attestations|8 attestations|five distinct parish-clerk renderings|John Hitzelberger[^—<]|80\+ (research )?sessions|Bertha[^a-zA-Z]+1879|six different ways across the seven baptisms' \
    ./stories/ 2>/dev/null) || true
  if [[ -n "$story_hits" ]]; then
    FOUND=1
    echo "──────────────────────────────────────────────────────────────────"
    echo "  [fail: stories pages picked up stale canon phrasing — fix before deploy]"
    echo "──────────────────────────────────────────────────────────────────"
    echo "$story_hits"
    echo
  fi
fi

# ── #8 Surname-trail single-source guard ─────────────────────────────────────
# Delegates to the JSON-driven checker. It verifies the AUTOGEN tables in
# germany/konzen-puzzle.html are freshly rendered from data/surname-attestations.json,
# and scans for retracted phrasings *including in scripts/build-evidence-cards.py*
# (the card generator's source data, which the HTML greps above cannot see).
if command -v python3 >/dev/null 2>&1; then
  echo "── running surname-canon guard (scripts/check_surname_canon.py) ──"
  if ! python3 "$SITE_ROOT/scripts/check_surname_canon.py"; then
    FOUND=1
  fi
  echo
else
  echo "  [skip: python3 not found — surname-canon guard not run]"
fi

# ── Summary ──────────────────────────────────────────────────────────────────
echo "──────────────────────────────────────────────────────────────────"
if [[ "$FOUND" -eq 0 ]]; then
  echo "✓ canon-guard clean — no stale canonical phrases found."
  exit 0
else
  echo "✗ canon-guard found stale instances. Review the matches above."
  echo "  Each section above is one check; some checks (like '16 Dec 1903')"
  echo "  warn rather than fail — review them in context."
  exit 1
fi
