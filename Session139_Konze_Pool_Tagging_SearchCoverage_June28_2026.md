# Session 139 — Konze-pool result tags on the Search-Coverage ledger (28 June 2026)

**What changed.** Added a new result-column tag to `search-coverage.html` marking
every searched parish in which a **Konze / Kontze / Jungkonze** surname (or spelling
variant) actually occurs — mirroring the existing *Gans family found* / *Kuntze family
found* candidate pills, but in a distinct muted slate-purple pill (`r-pool`,
"Konze pool present") so it is not confused with a live candidate.

**Meaning of the tag.** The Konze-pool surname occurs in that parish's records, **but
no Carl born 1833–41 on that surname matches Charles** — either because it is the
native home parish (surname present, no matching child), or because it appears only as
a burial, marriage, later child, or folded-in line, or only in the printed OSB register
rather than the searched baptism window. In short: *there, but not in the register that
would hold Charles.*

## Parishes tagged

**Native home parishes (Diemel cluster — attested in the Archion registers):**

- **Deisel** — "Konze — home parish." Native home of the surname; full 1833–41 baptisms read, no matching Carl.
- **Trendelburg** — "Konze — home parish." Konze/Kontze incl. Jungkonze native here; full window read, no match.
- **Hümme** — "Kontze present." Kontze strongly attested (100+ register mentions); the one Carl is a non-Kontze local.
- **Gottsbüren** — "Konze present." Surname present; full baptism index read, Carls all non-pool locals.

**Present, but not in a 1833–41 baptism (Archion):**

- **Stammen** — "Kontze — burial only" (14 Mar 1835 stillborn male, burial entry; no baptized siblings).
- **Friedrichsfeld** — "Kontze line" (Andreas Kontze line; no own register — baptisms/confirmands fold into Deisel/Trendelburg).
- **Schöneberg** — "Konze? — later daughters" (Konze/Ronze daughters b. 1862–70; final Kurrent reading still pending Schräder).
- **Bad Karlshafen** — "Konze/Jungkonze — marr./bur." (OSB Konze/Conze/Consens/Jungkonze pre-1830 or in marriage/burial records, not 1830s baptisms).

**Attested in Klaus Kunze's OSB registers, none in the searched window:**

- **Lippoldsberg** — "Kontze (OSB)" (OSB lists Kontze, Jungkontze + *Ganson*; baptisms 1831–41 line-read negative for Kontze).
- **Oedelsheim** — "Kontze (OSB)" (OSB lists Kontze, Kontzen, Konzen, Jungkonz; searched window negative).

**Not tagged (deliberately):** **Bodenfelde** — Kunze's OSB mining showed its sole
apparent "Konze" hit was *Konzertmeister* (a word, not a surname); Bodenfelde carries
Gans only, so it keeps its Gans tag and no Konze-pool tag. **Gieselwerder** already
carries the stronger red *Kuntze family found* candidate pill (active lead), so it was
left as-is.

## Reference — Klaus & Heike Kunze Ortssippenbücher (HeiKun-Verlag, Uslar)

Surname-distribution evidence for the Weser-ring parishes is drawn from Klaus Kunze's
online OSB *Registerseiten* (alphabetical surname indexes; they prove **presence of the
surname in that parish's book, 16th–19th c.**, not individual dates). Full mining note:
`KlausKunze_OSB_Konze_Distribution_June26_2026.md`.

- HeiKun OSB catalogue — https://klauskunze.com/heikun/index.htm
- Oedelsheim OSB register — https://klauskunze.com/heikun/os/oedelsheim_register.htm
- Lippoldsberg OSB register — https://klauskunze.com/heikun/os/lippoldsberg_register.htm
- Vernawahlshausen OSB register — https://klauskunze.com/heikun/ver/vernawahlshausen_register.htm
- Gieselwerder OSB register — https://klauskunze.com/heikun/os_gi/register.htm
- Bodenfelde OSB register — https://klauskunze.com/heikun/bf/register-osb-bodenfelde.htm

Publisher: HeiKun-Verlag (Klaus & Heike Kunze, Uslar), klauskunze.com.

## Page housekeeping

- New `.pill.r-pool` style + legend entry added to the Result-column key (legend links the Kunze OSB note).
- JSON-LD `dateModified` bumped to 2026-06-28.

**Standing caveat.** OSB registers confirm surname *presence*, not a baptism in our
window; Schöneberg's Konze/Ronze reading is still unconfirmed. All tags remain subject
to the project's verify-against-original standard before being treated as final.
