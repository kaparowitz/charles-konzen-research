# Session 108 — 36 per-parish research logs + live Archion: Heisebeck candidate, Liebenau eliminated

**Date:** 21 June 2026
**Scope:** Jed: "On the Hessian parish map, complete all the research for each parish
listed — 36 in total" + "list the Archion permalink and image number for the sources
checked" + "update the parish-map html and the individual parish log files." Deliverable
choice: update `germany/parish-map.html` **and** create per-parish log files; go live in
Archion for the open parishes **and** compile from logs + open web.

---

## Headline — both "undigitised" priority gaps are in fact ON ARCHION (read live)

The map's two "Priority open leads" were both recorded as undigitised (on-site only at
the Landeskirchliches Archiv Kassel). Signed in to Archion as Jed, **both volumes were
found already digitised** (Archion adds records continuously; these post-date the
April/June 2026 sweeps) and were read live for the January 1835 window.

### Heisebeck — CANDIDATE FOUND ★
- **Register 219175 — Heisebeck Taufen 1830–1887** (title page img 1236; 1526 images).
- **Image 1256, entry 76** — permalink **https://www.archion.de/p/34e1ddfe6e/**
  - **Carl Friedrich August**, *male*, **illegitimate** ("geb. Wehmann" — mother's surname),
    **born 29 January 1835, 7 p.m.**, Heisebeck Oberdorf No. 33, **baptized 8 Feb 1835**.
  - Mother: **Dorothea Henriette Charlotte Wehmann**, the *unverehelichte* (unmarried)
    daughter of the Wehmann (Köster/sexton) family; **no father named**.
  - **Remarks column EMPTY** — no confirmation/death/marriage note, unlike his neighbours
    (entry 75 Georg Müller "confirmed 1849"; entry 79 "confirmiert 1849"). The empty column
    is consistent with a child who **left Heisebeck before confirmation age (~1849)** — the
    emigrant pattern.
  - **Assessment:** the strongest single match the project has surfaced for the
    illegitimate-birth scenario the Y-DNA keeps live — *male, given name Carl, born late
    January 1835, illegitimate, in the #1 priority-gap parish*. **A candidate, NOT a
    confirmed identity:** recorded birth 29 Jan (Charles 26 Jan — 3 days off); surname
    Wehmann, not Gannsen/Konze. Neighbouring window males (entry 75 b. 25 Nov 1834;
    entry 77 Johann Wilhelm Wenkel b. 23 Feb 1835) are legitimate, non-matching.
- Calibration images cited in the log: img 1250 (Jahr 1833 Seite 12), img 1257 (entry 77+).

### Liebenau (+ Grimelsheim) — ELIMINATED (from the image)
- **Register 219745 — Liebenau Taufen 1830–1890** (title page img 1433; 1722 images).
- **Image 1462** — permalink **https://www.archion.de/p/b3bae9fefa/** — *Jahr 1835,
  Januar–März, Seite 27, entries 87–90*: all **legitimate males with named fathers** —
  Justus Klüte (b. Oct 1834, bapt. Jan 1835), **Ludwig Wilhelm Winnefeld (b. 12 Jan 1835)**,
  Carl [Ackermann] (b. 15 Mar 1835), Johann Heinrich Taubel (b. Mar 1835). **No Konze-pool
  surname, no illegitimate male, no birth on/near 26 January.** Filial Grimelsheim falls
  within this same Taufbuch. Positively eliminated.
- Calibration: img 1448 (Jahr 1832), img 1465 (Jahr 1835 Juni–Aug) bracket the window.

Login confirmed via the viewer logout link; permalinks minted with Archion's "Permalink
erstellen" function while signed in.

---

## Deliverables produced

1. **36 new per-parish research-log files** — `germany/<slug>-research-log.html`, one per
   parish on the map (deisel, trendelburg, friedrichsfeld, heisebeck, liebenau, stammen,
   huemme, gottsbueren, schoeneberg, lamerden, eberschuetz, haueda, helmarshausen, sielen,
   hombressen, gieselwerder, herstelle, hofgeismar, karlshafen, ostheim, niedermeiser,
   dalhausen, kelze, beverungen, gewissenruh, grebenstein, veckerhagen, immenhausen,
   marzhausen, gudensberg, dissen, grifte, diez, dies, schierstein, mainz).
   - Each has: status banner + verdict; a **"Sources checked"** table listing the Archion
     **register, image number, and one-click permalink** for every minted citation (138
     permalinks across 18 registers, from the 21 June Citation Audit, plus the 2 new live
     finds); and a **"Remaining follow-ups"** list tagged by lane (open-web vs offline-blocked).
   - Parishes searched by eye / via FamilySearch full-text / Matricula (no per-image
     permalink minted) list the register number + search method instead, with a note that
     permalinks can be minted on request.

2. **`germany/parish-map.html` updated:**
   - All 36 cards' "Research log →" links re-pointed from shared session notes to the new
     per-parish logs (Leaflet popups for Heisebeck/Liebenau too).
   - **Heisebeck** card + marker: "Open · candidate found"; desc rewritten (now-digitised,
     Carl Wehmann candidate). Stays a priority open lead (candidate, not confirmed).
   - **Liebenau** card + marker: moved from Priority open leads → **Eliminated** ("now
     digitised"); desc rewritten.
   - Counts updated everywhere: Priority open leads **2→1**, Eliminated **31→32**; status
     strip "1 open lead / 32 eliminated"; OG description "thirty-two eliminated; one new
     candidate." Section totals still sum to 36.
   - Search-history strip: added a 21 June live-Archion entry; rewrote the "Open" line.
   - `check_links.py`: **437 pages, 0 broken refs.**

3. Open-web follow-ups: nothing new actionable beyond Session 107's recorded results (NARA
   AAD *Germans to America* negative; Arcinsys Gottlieb Konze reconciled as a known man).
   New leads logged instead: trace **Carl Friedrich August Wehmann** forward (Heisebeck
   confirmations 219172 = absence ⇒ left young; US records for a Carl/Charles ~1835).

---

## Open / next
- **Verify** the Heisebeck entry-76 birth-month reading (Januar) and trace the child
  forward — Heisebeck Konfirmationen 219172 (Archion) + US side (gated logins).
- Reconcile the Wehmann illegitimate-birth lead with the **Konze Y-DNA** (unknown father).
- Unchanged decisive offline tests still lead on Justus Ernst Konze: Stammen burials
  220072 (blind read) and HStAM Best. 180 Hofgeismar emigration file.
- Site pages not touched this session (per the "keep main pages clean" convention):
  `open-questions.html#heisebeck`, `errata.html`, `negative-results.html` could be updated
  next to fold in the Heisebeck-digitised / Liebenau-eliminated findings.
