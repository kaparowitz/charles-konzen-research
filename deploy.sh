#!/usr/bin/env bash
# ============================================================
# deploy.sh — one-command deploy + verification for the
# Charles Research site.
#
# Replaces sync-deploy.sh, which assumed the legacy
# _deploy_netlify/ mirror that was archived in the May 8 audit
# pass. This script is the canonical deploy entry point.
#
# USAGE
#   bash deploy.sh                  # build + deploy + verify
#   bash deploy.sh --dry-run        # show what would happen, don't push
#   bash deploy.sh --build-only     # rebuild generated artifacts, don't push
#   bash deploy.sh --snapshot=PATH  # write a Zenodo-ready zip to PATH
#   bash deploy.sh --verify-only    # just run the post-deploy checks
#
# It auto-detects which deploy mechanism applies, in this order:
#   1. Netlify CLI present + linked         → `netlify deploy --prod`
#   2. .git directory + remote configured   → git add/commit/push
#   3. Neither                              → write a zip you can
#                                             drag-and-drop into the
#                                             Netlify dashboard
# ============================================================

set -euo pipefail

# ---- args ----
MODE="full"
SNAPSHOT_PATH=""
for arg in "$@"; do
  case "$arg" in
    --dry-run)        MODE="dry-run" ;;
    --build-only)     MODE="build-only" ;;
    --verify-only)    MODE="verify-only" ;;
    --snapshot=*)     SNAPSHOT_PATH="${arg#*=}" ; MODE="snapshot" ;;
    -h|--help)
      sed -n '2,30p' "$0" | sed 's|^# \?||'
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2 ; exit 1 ;;
  esac
done

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(pwd)"

# ---- styling ----
if [ -t 1 ] ; then
  C_BOLD=$'\033[1m' ; C_DIM=$'\033[2m' ; C_OK=$'\033[32m' ; C_WARN=$'\033[33m' ; C_ERR=$'\033[31m' ; C_RESET=$'\033[0m'
else
  C_BOLD="" ; C_DIM="" ; C_OK="" ; C_WARN="" ; C_ERR="" ; C_RESET=""
fi
say()    { printf "%s%s%s\n" "$C_BOLD" "$1" "$C_RESET" ; }
ok()     { printf "  %s✓%s %s\n" "$C_OK"   "$C_RESET" "$1" ; }
warn()   { printf "  %s!%s %s\n" "$C_WARN" "$C_RESET" "$1" ; }
err()    { printf "  %s✗%s %s\n" "$C_ERR"  "$C_RESET" "$1" ; }

# ---- 1 · build generated artifacts ----
# In --dry-run mode, lists what *would* run but doesn't actually execute
# build steps (some of which mutate the file tree). Only --build-only
# and the default 'full' mode actually rebuild.
build_artifacts() {
  say "1 · Rebuilding generated artifacts"
  if [ "$MODE" = "dry-run" ] ; then
    for s in scripts/build-sitemap.py scripts/inject-jsonld.py scripts/build-og-cards.py scripts/build-evidence-cards.py scripts/build_search_index.py scripts/build-pdfs.py ; do
      [ -f "$s" ] && ok "would run: python3 $s"
    done
    return
  fi
  if command -v python3 >/dev/null 2>&1 ; then
    [ -f scripts/build-sitemap.py ]    && python3 scripts/build-sitemap.py    > /dev/null && ok "sitemap.xml regenerated"
    [ -f scripts/inject-jsonld.py ]    && python3 scripts/inject-jsonld.py    > /dev/null && ok "JSON-LD refreshed"
    [ -f scripts/build-og-cards.py ]   && python3 scripts/build-og-cards.py   > /dev/null && ok "OG cards regenerated"
    [ -f scripts/build-evidence-cards.py ] && python3 scripts/build-evidence-cards.py > /dev/null && ok "evidence cards regenerated"
    [ -f scripts/build_search_index.py ] && python3 scripts/build_search_index.py > /dev/null && ok "search-index.json regenerated"
    if [ -f scripts/build-pdfs.py ] ; then
      python3 scripts/build-pdfs.py > /dev/null 2>&1 && ok "PDFs regenerated" || warn "build-pdfs.py exists but failed (likely missing headless Chrome)"
    fi
  else
    warn "python3 not found — skipping artifact rebuild"
  fi
}

# ---- 2 · sanity checks before deploy ----
sanity_checks() {
  say "2 · Sanity checks"
  local fail=0
  # 2a. No leftover .bak files
  local n_bak ; n_bak=$(find . -name "*.bak" -not -path "./_archive*" -not -path "./_backup_originals/*" 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n_bak" -gt 0 ] ; then
    warn "$n_bak .bak files present — run 'find . -name \"*.bak\" -delete' or move into _archive*"
  else
    ok "no stray .bak files"
  fi
  # 2b. Reachability: every page in sitemap.xml exists
  if [ -f sitemap.xml ] ; then
    local missing ; missing=$(python3 - <<'PY'
import re, os, sys
text = open("sitemap.xml").read()
miss = 0
for m in re.finditer(r"<loc>https://charles-konzen-research\.netlify\.app(/[^<]*)</loc>", text):
    p = m.group(1)
    if p == "/": p = "/index.html"
    if p.endswith("/"): p = p + "index.html"
    if not os.path.exists("." + p):
        miss += 1
print(miss)
PY
)
    if [ "$missing" -gt 0 ] ; then
      err "$missing URLs in sitemap.xml have no matching file"
      fail=1
    else
      ok "every sitemap URL resolves to a local file"
    fi
  fi
  # 2c. No live PLACEHOLDER-ORCID strings in production-facing copy
  local n_orcid ; n_orcid=$(grep -rIn "PLACEHOLDER-ORCID" --include="*.html" \
    --exclude-dir=_archive --exclude-dir=_archive_pre_audit_fixes --exclude-dir=_backup_originals \
    --exclude-dir=notes --exclude-dir=_deploy_netlify 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n_orcid" -gt 0 ] ; then
    warn "$n_orcid PLACEHOLDER-ORCID references still live (mint via IDENTIFIERS_KIT.md when ready)"
  fi
  # 2d. 404 page must exist
  [ -f 404.html ] && ok "404.html present" || { err "404.html missing" ; fail=1 ; }
  # 2e. netlify.toml present
  [ -f netlify.toml ] && ok "netlify.toml present" || { err "netlify.toml missing" ; fail=1 ; }
  # 2f. No broken <link rel="stylesheet" href="..."> to missing CSS
  python3 - <<'PY' || true
import re, os
fails = 0
for path in ["index.html","abstract.html","about.html","404.html"]:
    if not os.path.exists(path): continue
    text = open(path,"r",encoding="utf-8").read()
    for m in re.finditer(r'<link rel="stylesheet" href="([^"]+)"', text):
        href = m.group(1).split("?")[0]
        if href.startswith("http"): continue
        if not os.path.exists(href.lstrip("/")):
            print(f"  ! {path}  →  missing stylesheet: {href}")
            fails += 1
import sys; sys.exit(fails > 0)
PY
  if [ $? -eq 0 ] ; then ok "stylesheet refs resolve on key pages" ; fi
  # 2g. Internal-link audit — block broken file paths, missing cross-page
  #     anchors, and dead in-page anchors from reaching production.
  if [ -f scripts/check_links.py ] ; then
    local links_out links_rc
    links_out=$(python3 scripts/check_links.py --quiet 2>&1) ; links_rc=$?
    if [ "$links_rc" -eq 0 ] ; then
      ok "internal-link audit clean"
    else
      err "internal-link audit found broken references — deploy ABORTED. Run 'python3 scripts/check_links.py' to review."
      python3 scripts/check_links.py 2>&1 | head -25
      fail=1
    fi
  else
    warn "scripts/check_links.py not found — skipping link audit"
  fi
  # 2h. Canonical-claim guard — block stale surname/Freundberg/session/Hitzelberger
  #     counts from reaching production. The propagation cascade is the project's
  #     signature failure mode; check_canon.sh is the pre-deploy gate. Fail-class
  #     hits abort the deploy; warn-class hits are reported but do not block.
  if [ -x scripts/check_canon.sh ] || [ -f scripts/check_canon.sh ] ; then
    local canon_out canon_rc
    canon_out=$(bash scripts/check_canon.sh 2>&1) ; canon_rc=$?
    if [ "$canon_rc" -eq 0 ] ; then
      local n_warn ; n_warn=$(printf "%s\n" "$canon_out" | grep -c '\[warn:' || true)
      if [ "$n_warn" -gt 0 ] ; then
        warn "canon-guard clean (0 fail-class hits, $n_warn warn-class advisories — review with 'bash scripts/check_canon.sh')"
      else
        ok "canon-guard clean"
      fi
    else
      err "canon-guard found stale canonical phrases — deploy ABORTED. Run 'bash scripts/check_canon.sh' to review."
      printf "%s\n" "$canon_out" | grep -E '^\./|^\s+\[fail:' | head -20
      fail=1
    fi
  else
    warn "scripts/check_canon.sh not found — skipping canon guard"
  fi
  return $fail
}

# ---- 3 · choose deploy mechanism ----
detect_deploy() {
  if command -v netlify >/dev/null 2>&1 && [ -f .netlify/state.json ] ; then
    echo "netlify-cli"
  elif [ -d .git ] && git remote -v >/dev/null 2>&1 && [ -n "$(git remote -v)" ] ; then
    echo "git-push"
  else
    echo "manual-zip"
  fi
}

deploy_via_netlify_cli() {
  say "3 · Deploy via Netlify CLI"
  if [ "$MODE" = "dry-run" ] ; then
    ok "dry-run: would run 'netlify deploy --prod --dir=.'"
    return 0
  fi
  netlify deploy --prod --dir=. --message "deploy.sh — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
}

deploy_via_git() {
  say "3 · Deploy via git push (Netlify is connected to the repo)"
  if [ -z "$(git status --porcelain)" ] ; then
    warn "no local changes to commit"
    return 0
  fi
  git status --short
  if [ "$MODE" = "dry-run" ] ; then
    ok "dry-run: would run 'git add -A && git commit && git push'"
    return 0
  fi
  printf "  Continue with commit + push? [y/N] " ; read -r yn
  if [ "$yn" != "y" ] && [ "$yn" != "Y" ] ; then warn "aborted by user" ; return 1 ; fi
  git add -A
  git commit -m "$(commit_message)"
  git push
  ok "pushed; Netlify will pick up the build automatically"
}

deploy_via_zip() {
  say "3 · No CLI / git remote found — building a manual deploy zip"
  # IMPORTANT: write the zip OUTSIDE the publish directory. Earlier
  # versions wrote ./deploy-*.zip into the repo root; on the next
  # `netlify deploy --dir=.` that 100+ MB artifact got uploaded with
  # the site and broke the deploy (per the 9 May 2026 audit).
  local zip_path="${SNAPSHOT_PATH:-${TMPDIR:-/tmp}/charles-konzen-deploy-$(date -u +%Y%m%d-%H%M%S).zip}"
  if [ "$MODE" = "dry-run" ] ; then
    ok "dry-run: would write $zip_path"
    return 0
  fi
  build_zip "$zip_path"
  ok "wrote $zip_path"
  printf "\n%sNext step:%s drag and drop %s onto\n  https://app.netlify.com/sites/charles-konzen-research/deploys\n" "$C_BOLD" "$C_RESET" "$zip_path"
}

build_zip() {
  local out="$1"
  python3 - "$out" <<'PY'
import zipfile, os, sys
out = sys.argv[1]
EXCL = ("_archive","_archive_pre_audit_fixes","_backup_originals","notes/_archive",
        "_deploy_netlify",".git",".DS_Store",".netlifyignore")
def excluded(p):
    p = p.replace("\\","/")
    return any(("/"+e+"/" in "/"+p+"/") or p.endswith(e) for e in EXCL)
n = 0
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if not excluded(os.path.join(root,d))]
        for f in files:
            full = os.path.join(root, f)
            arc = os.path.relpath(full, ".")  # safe path stripping
            if excluded(arc): continue
            if f.endswith(".bak") or f.endswith(".swp"): continue
            try:
                zf.write(full, arc)
                n += 1
            except FileNotFoundError:
                pass  # skip broken symlinks / vanished files
print(f"  ✓ {n} files in {out} ({os.path.getsize(out)//(1024*1024)} MB)")
PY
}

commit_message() {
  cat <<EOF
deploy: $(date -u +%Y-%m-%dT%H:%M:%SZ) — $(find . -name "*.html" -mmin -1440 -not -path "./_archive*" -not -path "./_backup*" 2>/dev/null | wc -l | tr -d ' ') files modified in last 24h
EOF
}

# ---- 4 · post-deploy verification (the HANDOFF five-step) ----
verify() {
  say "4 · Post-deploy verification (HANDOFF.md five-step)"
  cat <<'EOF'
  1. Visit https://charles-research.netlify.app/sitemap.xml
     and confirm ~174 URLs.
  2. Visit https://charles-research.netlify.app/robots.txt
     and confirm Disallow: /notes/ and /_archive*/ lines.
  3. Run an unfurl previewer on:
       /abstract.html
       /germany/parish-map.html
       /evidence/card-1-trendelburg-kontzen.html
     using https://www.opengraph.xyz/ — confirm per-page OG cards.
  4. Run https://search.google.com/test/rich-results
     on the home page; confirm Person + Article JSON-LD parses.
  5. Open the home page on a phone; confirm the address bar tints
     to #1F1A14 (the theme-color meta).

  After all five pass, you can safely:
     rm -rf _archive_pre_audit_fixes/    # ~493 MB recovered
EOF
  ok "checklist printed; complete each manually"
}

# ---- main ----
case "$MODE" in
  build-only)
    build_artifacts ; sanity_checks
    ;;
  verify-only)
    verify
    ;;
  snapshot)
    build_artifacts
    sanity_checks || warn "sanity checks failed; snapshot may include errors"
    build_zip "$SNAPSHOT_PATH"
    ;;
  dry-run|full)
    build_artifacts
    sanity_checks || { err "sanity checks failed; aborting"; [ "$MODE" = "dry-run" ] || exit 1; }
    case "$(detect_deploy)" in
      netlify-cli) deploy_via_netlify_cli ;;
      git-push)    deploy_via_git ;;
      manual-zip)  deploy_via_zip ;;
    esac
    [ "$MODE" = "full" ] && verify
    ;;
esac

say "deploy.sh complete"
