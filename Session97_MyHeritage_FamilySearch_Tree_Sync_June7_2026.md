# Session 97 — MyHeritage ↔ FamilySearch Tree Sync (GEDCOM rebuild)
**Date:** 7 June 2026
**Goal:** Replace the outdated 813-person MyHeritage tree with a full export of the
FamilySearch tree, to maximize Smart Matches / Theories of Family Relativity and the
chances of unknown relatives (esp. the German Lipphardt–Eickenberg cluster, Session 96)
reaching out. Executes step 2 of Session 96's action list ("attach the DNA kit to a
real tree").

---

## 1. What was built

**`Johnson_FamilySearch_Sync_June2026.ged`** (in this folder; 697 KB, GEDCOM 5.5.1, UTF-8):

| Metric | Value |
|---|---|
| Individuals | 3,187 |
| Families | 1,275 |
| Direct ancestors | ~2,300 (every documented FS generation, to ~1386) |
| Siblings of ancestors | ~890 (generations 1–8, i.e. back to ~1700s couples) |
| Full vitals (dates + places, christening/burial included) | generations 0–12 (~1550 onward) |
| Year-only vitals | generations 13–16 (pre-1550; FS data there largely unsourced) |
| FS person IDs | preserved on every person as `REFN` (e.g. Charles = `LZXC-6GB`) |

Charles Johnson Sr. (LZXC-6GB, b. 26 Jan 1835 Trendelburg, d. 16 Dec 1903 St. Louis,
bur. Old St. Marcus) carries **alternate names "Charles /Gannsen/" and "Charles
/Gannson/" (TYPE aka)** so German relatives searching the documented military-era
spellings can Smart-Match. Konzen was deliberately NOT added (unproven hypothesis;
avoids polluting matches). Auguste Kreichelt and all five Kreichelt siblings
(incl. Bertha Barbara, the Session-96 test-candidate line) are present with vitals.

Wife's (Saavedra) deep ancestry excluded by design — no DNA relevance to the Johnson kits.

## 2. How it was extracted (reusable recipe)

FamilySearch internal JSON endpoints, queried from a logged-in browser tab
(no API token needed; ~1,400 requests, ~3 min with 6-way concurrency):

- Pedigree skeleton: `/service/tree/tree-data/r9/portrait-pedigree/{pid}?includeMarriages=true&numGenerations=8`
  (recursable from gen-8 frontier persons; blood-side couples are index `i < 2^(g-1)`)
- Siblings: `/service/tree/tree-data/r9/family-members/couple/{p1}_{p2}/children?focusPersonId={pid}`
- Full vitals: `/service/tree/tree-data/v8/person/{pid}/details`

GEDCOM assembled in-page (JS), downloaded, moved to this folder via Finder.
**Pitfall:** crawl state lives in the tab's JS context — do NOT navigate that tab.
(Lost the dataset twice this way; third run was scripted end-to-end.)

## 3. MyHeritage import — blocked by repeated session invalidation, handed to Jed

- Account: **Complete plan** (unlimited tree size, expires Sep 2028) → no size cap issue.
- Existing site: "Johnson Family Tree (FamilySearch)", 813 people / 742 photos /
  6,896 DNA matches. Old tree left untouched; new tree imported alongside
  (MyHeritage cannot merge GEDCOM into an existing tree). Jed opted to delete the
  old tree himself after checking photos.
- **Anomaly:** every visit to `/import-gedcom/{siteId}` (clicked or direct URL,
  3 attempts) instantly invalidated the MyHeritage login and bounced to a SECOND
  site ID ending `...CRTQ` shown in guest view — possibly a stale duplicate site
  on the account. Import therefore handed to Jed to run manually in his own window.
- 20-minute wait reported by Jed (import processing / rate limit), then verification.

## 4. Outcome (completed this session)

1. ✅ **Import succeeded** after a wait-out of the session-invalidation issue:
   "Your family tree with 3,187 individuals was imported successfully" — new tree
   **"Johnson_FamilySearch_Sync_June2026" (familyTreeID=3)** in the same site,
   alongside the old 813-person tree (familyTreeID=2).
2. ✅ **2,635 Smart Matches found immediately** on import ("Review matches" queue).
3. ✅ Charles Johnson 1835–1903 verified present; Jed's person carries REFN KWCS-KB2.
4. ✅ **DNA kit AN-92FA83 re-assigned** to Jedediah Smith Johnson in the NEW tree
   (person id 3000001, confirmed via the re-assign dialog) — this is the unlock for
   Theories of Family Relativity (recomputed periodically, not instantly; check in
   coming days/weeks).
5. Only one kit appears under Manage DNA kits — Gary's/Sandy's/Sarah's kits are not
   managed from this account and did not need re-pointing.

## 4a. Closeout (end of session)

- ✅ New tree **set as default tree** on the site.
- ✅ Old 813-person tree: **deletion initiated by Jed** (MyHeritage reported
  "deletion will take some time" — verify it disappears from Manage trees later).
- Photo backup: Jed opted to skip. Partial backup exists:
  `myheritage_photos_backup_part1.zip` (first 120 of 742 originals) in Chrome's
  download folder. Photos are site-level on MyHeritage and the full-size originals
  remain fetchable via the photo-world GraphQL endpoint (recipe: capture
  `photo_world_fetch_site_media` body, rewrite `limit/offset`, fetch `url` field).
- Chrome quirk discovered: automatic downloads from myheritage.com were silently
  blocked after the first; required allowing the site under
  chrome://settings/content/automaticDownloads.

## 4b. Watch next

- Review the 2,635 Smart Matches; prioritize any touching the Kreichelt siblings,
  Charles's Gannsen/Gannson aka names, or the Lipphardt–Eickenberg cluster's surnames.
- Theories of Family Relativity recompute over days/weeks now that the kit sits in
  a 3,187-person default tree.
- The `...CRTQ` second site ID seen during the logout loop may be a stale duplicate
  site on the account — worth a look someday.

## 5. Cross-references

- Session 96 — MyHeritage DNA match analysis (Lipphardt–Eickenberg paternal cluster,
  chr-17 triangulated segment; the reason this tree-sync matters)
- dna.html § next steps
- FamilySearch_Data_Entry_and_Corrections.xlsx (older FS-side fixes)
