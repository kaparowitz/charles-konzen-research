#!/usr/bin/env python3
"""
Generate per-parish town pages for the 27 parishes on the Hessian Parish Map
that lacked their own page. Each page matches the existing towns/*.html format
(hero, At a glance, Historical overview, Significance, Research resources,
Project session-notes [research log], External references) and reuses the exact
shared nav + footer extracted from an existing town page.

All factual content is drawn from germany/parish-map.html (status, register
numbers, coordinates, search findings) — no invented vital data.
"""
import os, re, urllib.parse

TOWNS = os.path.join(os.path.dirname(__file__), "..", "towns")
TOWNS = os.path.abspath(TOWNS)
TEMPLATE = os.path.join(TOWNS, "sielen.html")

with open(TEMPLATE, encoding="utf-8") as f:
    tpl = f.read()

def block(name):
    m = re.search(r"<!-- BEGIN-INJECTED-%s -->(.*?)<!-- END-INJECTED-%s -->" % (name, name), tpl, re.S)
    return m.group(0)

NAV_ASSETS = block("NAV-ASSETS")
NAV = block("NAV")
FOOTER = block("FOOTER")

SITE = "https://charles-research.netlify.app"

# Status -> (pill label, hero tone)
STATUS_PILL = {
    "eliminated": "ELIMINATED",
    "open": "OPEN · UNDIGITISED",
    "working": "WORKING HYPOTHESIS",
    "charles": "CHARLES'S VILLAGE",
}

# Each parish: documented facts only (from parish-map.html).
P = [
 dict(slug="stammen", name="Stammen", status="eliminated",
   sub="Diemel-valley village ~2 km east of Deisel · a distinct Stammen Kontze branch documented · 1835 baptisms searched",
   german="village ~2 km east of Deisel", konze="documented",
   coords="51.566 N · 9.446 E", dist="~2.0 km east of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="220069 (baptisms) · 220072 (burials)",
   overview="Stammen is a small Evangelical village in the Diemel valley, about two kilometres east of Deisel in the historic Kreis Hofgeismar. Like the rest of the cluster it passed from Kurhessen to Prussia in 1866. The parish is significant to this investigation because it holds a <em>distinct</em> Kontze branch — separate from the main Trendelburg/Deisel line — and because one of the two decisive offline tests for the leading candidate now rests on its burial register.",
   sig="The 1835 baptisms were searched live on Archion (reg. 220069). One Konze-pool entry was found — a <strong>stillborn male Kontze</strong>, born 14 March 1835 at Haus Nr. 21 (a first-pass reading of “Rudolph, b. 20 Mar” was corrected at full zoom — see <a href=\"../errata.html#er-2026-06-06-stammen-stillborn\">errata</a>), child of <em>Christian Ludwig Kontze</em> (Tagelöhner) × <em>Anne Gertrud née Temme</em>. This is a newly-documented, distinct Stammen branch, not the Trendelburg Carl-Ludwig line, and is <strong>not Charles</strong> (the child was stillborn). Kontze also appears in 1833 as a godparent (“der Schwager”), and two <em>Jungkontze</em> mothers appear in 1835. <strong>Open offline test:</strong> Justus Ernst Konze’s siblings Heinrich Wilhelm (†1858) and Elisa Melusine (†1865) both died at Stammen, so the decisive read for Justus Ernst’s own fate is the un-indexed <strong>Stammen burial register (Archion 220072, ~1843–1875)</strong>, page by page; a Konze death there would eliminate the leading hypothesis, its absence would harden it.",
   log=[("S88 · Konze distribution sweep · Stammen correction","../notes_view/Session88_Konze_Distribution_Sweep_Stammen_Correction_June6_2026.html"),
        ("S89 · Stammen marriage + burial · Gottsbüren Konze","../notes_view/Session89_Stammen_Marriage_Burial_Gottsbueren_Konze_June6_2026.html"),
        ("Konze family by town (germany)","../germany/konze-stammen.html")]),

 dict(slug="gottsbueren", name="Gottsbüren", status="eliminated",
   sub="Wallfahrt village ~4 km SE of Deisel · a claimed but unconfirmed Kontze tie · 1835 negative",
   german="village ~4 km southeast of Deisel", konze="claimed",
   coords="51.552 N · 9.468 E", dist="~3.9 km SE of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219049",
   overview="Gottsbüren is an Evangelical village southeast of Deisel, historically a medieval pilgrimage (Wallfahrt) site. It sits at the edge of the Konze surname cluster but, on the documentary evidence, only as a <em>claimed</em> origin — not a Kontze home parish.",
   sig="The January–February 1835 baptisms were searched live on Archion: no Konze-pool male, no illegitimate male. A Stammen 1833 marriage names <em>Christian Ludwig Kontze</em> as <em>born in Gottsbüren</em> — but Gottsbüren’s own books are <strong>entirely Kontze-free</strong>: no Kontze in baptisms (1804/06/08), marriages (1795–1806), or burials (1805–Jan 1825 read entry-by-entry; none 1827–33 either). Only the maternal <em>Garland</em> family is native here. Gottsbüren is therefore a <strong>claimed but unconfirmed</strong> Konze tie (Andreas/Christian Ludwig Kontze an in-migrant), not a documented Konze village. See <a href=\"../changelog.html#cl-2026-06-06-stammen-gottsbueren\">changelog</a>.",
   log=[("S89 · Stammen marriage + burial · Gottsbüren Konze","../notes_view/Session89_Stammen_Marriage_Burial_Gottsbueren_Konze_June6_2026.html"),
        ("S88 · Konze distribution sweep","../notes_view/Session88_Konze_Distribution_Sweep_Stammen_Correction_June6_2026.html"),
        ("Konze family by town (germany)","../germany/konze-gottsbueren.html")]),

 dict(slug="lamerden", name="Lamerden", status="eliminated",
   sub="Diemel village ~5 km NW of Deisel · Jan–Feb 1835 baptisms read by eye · negative",
   german="village ~5 km northwest of Deisel", konze=None,
   coords="51.610 N · 9.392 E", dist="~5.0 km NW of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219676",
   overview="Lamerden is a small Evangelical village northwest of Deisel in the Diemel valley, within the historic Kreis Hofgeismar and the same Kirchenkreis as the rest of the search ring.",
   sig="The January–February 1835 baptisms were read by eye (the register is not AI-transcribed): <strong>no Konze-pool male and no illegitimate male</strong> in the window. Eliminated June 2026.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="eberschuetz", name="Eberschütz", status="eliminated",
   sub="Diemel village ~5 km NNE of Deisel · one illegitimate male verified not a match",
   german="village ~5 km north-northeast of Deisel", konze=None,
   coords="51.613 N · 9.441 E", dist="~5.2 km NNE of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="218887",
   overview="Eberschütz is an Evangelical village north-northeast of Deisel on the Diemel, within the historic Kreis Hofgeismar.",
   sig="The January–February 1835 baptisms were searched. One illegitimate male was found — <em>Heinrich Wilhelm Albore</em>, b. 22 Jan 1835, mother an unmarried woman from Bischhausen (Königreich Hannover) — verified at full zoom and judged <strong>not a match</strong> (surname, given name, and place all unrelated to Charles).",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="gieselwerder", name="Oberweser / Gieselwerder", status="eliminated",
   sub="Weser-valley parish ~7 km east of Deisel · Oberweser records held under Gieselwerder · negative",
   german="Weser-valley parish ~7 km east of Deisel", konze=None,
   coords="51.581 N · 9.522 E", dist="~7.3 km east of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219016",
   overview="Gieselwerder is an Evangelical parish in the Weser valley east of Deisel; the Oberweser-area Evangelical records are held under Gieselwerder. It marks the eastern edge of the close search ring.",
   sig="The January–February 1835 baptisms (reg. 219016) were searched: <strong>all males legitimate, no Konze-pool surname, and no illegitimate male</strong>. Eliminated June 2026.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="kelze", name="Hofgeismar-Kelze", status="eliminated",
   sub="Small Huguenot colony parish ~11 km SW of Deisel · only window baptism female",
   german="Huguenot colony parish ~11 km southwest of Deisel", konze=None,
   coords="51.483 N · 9.347 E", dist="~10.7 km SW of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Reformed (Huguenot colony)",
   portal="archion", reg="219634",
   overview="Kelze is a small Huguenot colony parish near Hofgeismar, southwest of Deisel — one of several refugee-foundation congregations in the district.",
   sig="The only January–February 1835 baptism is <strong>female</strong>; there is no Konze-pool surname and no in-window illegitimate male. Eliminated June 2026.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="gewissenruh", name="Gewissenruh", status="eliminated",
   sub="Tiny Huguenot parish ~12 km NE of Deisel · ~3 births/yr · no January 1835 baptism",
   german="tiny Huguenot parish ~12 km northeast of Deisel", konze=None,
   coords="51.623 N · 9.562 E", dist="~11.7 km NE of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Reformed (Huguenot colony)",
   portal="archion", reg="219001",
   overview="Gewissenruh is a very small Huguenot foundation parish northeast of Deisel, near the Weser — only a few births a year in this period.",
   sig="There is <strong>no January 1835 baptism at all</strong> (reg. 219001); the only window entry is female. Eliminated June 2026.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="grebenstein", name="Grebenstein", status="eliminated",
   sub="Small town ~14 km south of Deisel · one illegitimate January birth, female",
   german="small town ~14 km south of Deisel", konze=None,
   coords="51.447 N · 9.411 E", dist="~13.5 km south of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219106",
   overview="Grebenstein is a small Evangelical town south of Deisel toward Hofgeismar, within the historic Kreis Hofgeismar.",
   sig="The January–February 1835 baptisms were searched: one illegitimate January birth, but <em>female</em>; <strong>no Konze-pool male</strong>. Eliminated June 2026.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="veckerhagen", name="Veckerhagen", status="eliminated",
   sub="Weser ironworks village ~15 km SE of Deisel · one out-of-window illegitimate male, unrelated",
   german="Weser village ~15 km southeast of Deisel", konze=None,
   coords="51.493 N · 9.593 E", dist="~14.7 km SE of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="220213",
   overview="Veckerhagen is an Evangelical village on the Weser southeast of Deisel, historically known for its ducal ironworks (Eisenhammer).",
   sig="The January–March 1835 baptisms were searched. One illegitimate male — <em>Wilhelm Walter</em>, baptized ~March 1835 (mother Anna Martha Johanne Schäfer) — falls outside the window and is unrelated; <strong>not a match</strong>. No Konze-pool surname.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="immenhausen", name="Immenhausen", status="eliminated",
   sub="Small town ~16 km south of Deisel · all 1835 males legitimate",
   german="small town ~16 km south of Deisel", konze=None,
   coords="51.426 N · 9.478 E", dist="~16.3 km south of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219586",
   overview="Immenhausen is a small Evangelical town south of Deisel on the road toward Kassel, at the southern edge of the close search ring.",
   sig="The 1835 baptisms were searched: <strong>all males legitimate with named fathers</strong>; no Konze-pool surname and no illegitimate male. Eliminated June 2026.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="marzhausen", name="Marzhausen", status="eliminated",
   sub="Witzenhausen-district village ~40 km SE · checked for completeness · negative",
   german="village ~40 km southeast, Kirchenkreis Witzenhausen", konze=None,
   coords="51.376 N · 9.918 E", dist="~40 km SE — outside the rim",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kirchenkreis Witzenhausen", confession="Evangelical/Lutheran",
   portal="archion", reg="181898",
   overview="Marzhausen lies in the neighbouring Kirchenkreis Witzenhausen, far southeast of the Deisel cluster. It was checked only for completeness, well outside the walking-distance rim.",
   sig="The 1835 entries are all married couples; <strong>no Konze/Köster surname, no illegitimate male</strong>. Eliminated June 2026.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="karlshafen", name="Bad Karlshafen", status="eliminated",
   sub="Diemel/Weser harbour town ~9 km north · both confessions searched · one legitimized illegitimate, not Charles",
   german="harbour town ~9 km north of Deisel", konze=None,
   coords="51.645 N · 9.450 E", dist="~8.8 km north of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Lutheran + Reformed (French & German)",
   portal="archion", reg="218677 (Luth.) · 218713 (Ref.)",
   overview="Bad Karlshafen is a baroque harbour town where the Diemel meets the Weser, north of Deisel — a Huguenot/Waldensian foundation with both a Lutheran and a Reformed (French and German) congregation, the latter merged from 1830.",
   sig="Both confessions were searched. The Lutheran book (218677) is clean; the Reformed book (218713) holds the region’s one window-compatible illegitimate male, <em>Johann Heinrich Thielemann</em>, b. 8 Feb 1835 — but he was <strong>legitimized in 1838</strong> by a documented father (Schlosshahn) and stayed locally recorded; <strong>not Charles</strong>. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="hombressen", name="Hombressen", status="eliminated",
   sub="Village ~7 km SW of Deisel · legitimate males only · the one illegitimate birth female",
   german="village ~7 km southwest of Deisel", konze=None,
   coords="51.520 N · 9.348 E", dist="~7.2 km SW of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219487",
   overview="Hombressen is an Evangelical village southwest of Deisel toward Hofgeismar, within the historic Kreis Hofgeismar.",
   sig="January–February 1835 (reg. 219487): <strong>legitimate males only</strong> (21 Jan, 25 Feb); the single illegitimate birth in the window is female. No Konze-pool surname. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="haueda", name="Haueda", status="eliminated",
   sub="Filial village ~6 km WNW of Deisel · own Taufbuch from 1830 · negative",
   german="filial village ~6 km west-northwest of Deisel", konze=None,
   coords="51.597 N · 9.353 E", dist="~5.5 km WNW of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219154",
   overview="Haueda is a small Evangelical filial village west-northwest of Deisel that kept its own Taufbuch from 1830, within the historic Kreis Hofgeismar.",
   sig="The January–February 1835 males are all legitimate; <strong>no unehelich entry and no Konze-pool surname</strong>. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="ostheim", name="Ostheim", status="eliminated",
   sub="Village ~9 km WSW of Deisel · one stillborn male (not a candidate) · negative",
   german="village ~9 km west-southwest of Deisel", konze=None,
   coords="51.529 N · 9.300 E", dist="~9.2 km WSW of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219970",
   overview="Ostheim is an Evangelical village west-southwest of Deisel, within the historic Kreis Hofgeismar.",
   sig="January–February 1835 (reg. 219970): one stillborn male (unnamed, unbaptized — not a candidate by definition) and legitimate males only; <strong>no Konze-pool surname, no illegitimate male</strong>. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="niedermeiser", name="Niedermeiser", status="eliminated",
   sub="Village ~10 km SW of Deisel · no male baptism in the 1835 window at all",
   german="village ~10 km southwest of Deisel", konze=None,
   coords="51.503 N · 9.318 E", dist="~10.0 km SW of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="archion", reg="219877",
   overview="Niedermeiser is an Evangelical village southwest of Deisel, within the historic Kreis Hofgeismar.",
   sig="There is <strong>no male baptism at all between 11 January and 1 March 1835</strong> (reg. 219877) — the window entries are all female. No Konze-pool surname. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="herstelle", name="Herstelle / Würgassen", status="eliminated",
   sub="Catholic Westphalian parish ~8 km NNW · first cross-border search · via Matricula · negative",
   german="Catholic Westphalian parish ~8 km north-northwest of Deisel", konze=None,
   coords="51.633 N · 9.380 E", dist="~7.7 km NNW of Deisel",
   juris="Königreich Preußen · Provinz Westfalen · Erzbistum Paderborn", confession="Roman Catholic",
   portal="matricula", reg="DE_EBAP_10608",
   overview="Herstelle is a Roman Catholic parish across the Prussian border in Westphalia (Erzbistum Paderborn), just north-northwest of Deisel on the Weser; its register also covers the residents of neighbouring Würgassen. It was the first cross-border parish searched, via the Catholic Matricula portal rather than Archion.",
   sig="The January–February 1835 entries are every one marked <em>ehelich</em>; <strong>no pool-like surname and no illegitimate male</strong>. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="liebenau", name="Liebenau (+ Grimelsheim)", status="open",
   sub="Town ~13 km SW of Deisel · coverage hole: Archion holds only to 1777 · 1835 books not online",
   german="town ~13 km southwest of Deisel", konze=None,
   coords="51.496 N · 9.276 E", dist="~12.7 km SW of Deisel",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kreis Hofgeismar", confession="Evangelical/Lutheran",
   portal="open", reg="Archion holds only to 1777",
   overview="Liebenau is a small Evangelical town southwest of Deisel, with the filial village of Grimelsheim attached. It is one of two priority <strong>open</strong> gaps in the candidate pool because its 1835 registers are not digitised anywhere.",
   sig="<strong>Coverage hole found June 2026:</strong> Archion holds the Liebenau (Hesse) registers only to 1777 — the 1835 books (likely also covering filial Grimelsheim) are not online at all. Resolving this parish needs the Landeskirchliches Archiv Kassel or a FamilySearch microfilm. Logged as an open gap in <a href=\"../open-questions.html\">Open Questions</a>.",
   log=[("S85 · FamilySearch full-text adjacent parishes","../notes_view/Session85_FamilySearch_FullText_Adjacent_Parishes_June4_2026.html")]),

 dict(slug="beverungen", name="Beverungen", status="eliminated",
   sub="Catholic Westphalian town ~11 km north · five window males, all ehelich, each accounted for in Germany",
   german="Catholic Westphalian town ~11 km north of Deisel", konze=None,
   coords="51.663 N · 9.373 E", dist="~11.0 km north of Deisel",
   juris="Königreich Preußen · Provinz Westfalen · Erzbistum Paderborn", confession="Roman Catholic",
   portal="matricula", reg="DE_EBAP_10601",
   overview="Beverungen is a Roman Catholic town across the Prussian border in Westphalia (Erzbistum Paderborn), on the Weser north of Deisel. Searched via the Catholic Matricula portal.",
   sig="January–February 1835 (Taufen 1803–1835, image T_0108): five window males, <strong>every one <em>ehelich</em> and none in the surname pool</strong> — and each carries a later margin note placing him dead or married in Germany, so all five are independently eliminated as emigrant candidates. No illegitimate entry. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="dalhausen", name="Dalhausen", status="eliminated",
   sub="Catholic Westphalian village ~10 km NW · a striking 26 Jan 1835 near-miss, positively eliminated",
   german="Catholic Westphalian village ~10 km northwest of Deisel", konze=None,
   coords="51.626 N · 9.305 E", dist="~10.1 km NW of Deisel",
   juris="Königreich Preußen · Provinz Westfalen · Erzbistum Paderborn", confession="Roman Catholic",
   portal="matricula", reg="DE_EBAP_10605",
   overview="Dalhausen is a Roman Catholic village across the Prussian border in Westphalia (Erzbistum Paderborn), northwest of Deisel. Searched via the Catholic Matricula portal.",
   sig="The register’s own name index (Taufen 1822–1838) holds <strong>no pool-resembling surname for the entire 1822–1838 span</strong>; the January–February 1835 pages confirm all males <em>ehelich</em>. A striking near-miss: entry 6, <em>Friedrich Wilhelm Sievers</em>, was born exactly <strong>26 January 1835</strong> — but legitimate (Sievers × Spindeler), and his margin note (†23.2.1908) shows he <strong>died in Germany</strong>; positively eliminated. Eliminated June 2026.",
   log=[("S87 · Western / northern border parishes","../notes_view/Session87_Western_Northern_Border_Parishes_June6_2026.html")]),

 dict(slug="gudensberg", name="Gudensberg", status="eliminated",
   sub='Tier-3 "Deissen" place-name candidate ~42 km S near Kassel · 1850 confirmation class read · negative',
   german='Tier-3 "Deissen" candidate ~42 km south, near Kassel', konze=None,
   coords="51.180 N · 9.450 E", dist="~42 km south — far outside the rim",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Kirchenkreis Fritzlar", confession="Evangelical/Lutheran",
   portal="archion", reg="—",
   overview="Gudensberg is a small Evangelical town near Kassel in the Kirchenkreis Fritzlar, far south of the Deisel cluster. It was investigated as a Tier-3 place-name candidate for the “Deissen” / “Deisse” reading of Charles’s stated origin.",
   sig="Place-name candidate for “Deissen” / “Deisse.” The 1850 confirmation class was read (partial coverage); <strong>no Konze-pool surname and no window male</strong>. First flagged as an on-site Tier-3 target, then found on Archion and cleared. Eliminated June 2026.",
   log=[("Parish search coverage","../search-coverage.html")]),

 dict(slug="dissen", name="Dissen", status="eliminated",
   sub='Tier-3 "Deissen" place-name candidate ~40 km S near Gudensberg · negative',
   german='Tier-3 "Deissen" candidate ~40 km south, near Gudensberg', konze=None,
   coords="51.198 N · 9.421 E", dist="~40 km south — far outside the rim",
   juris="Kurfürstentum Hessen-Kassel until 1866 · near Gudensberg", confession="Evangelical/Lutheran",
   portal="archion", reg="—",
   overview="Dissen is a small place near Gudensberg, far south of the Deisel cluster, tested as a Tier-3 place-name candidate for the “Deissen” reading of “Deisse.”",
   sig="Tier-3 “Deissen” place-name candidate (from James’s reading of “Deisse”). Searched — <strong>negative; no Konze pool</strong>. Eliminated June 2026.",
   log=[("Parish search coverage","../search-coverage.html")]),

 dict(slug="grifte", name="Grifte", status="eliminated",
   sub='Tier-3 "Deissen" place-name candidate ~37 km S, Edermünde · negative',
   german='Tier-3 "Deissen" candidate ~37 km south, Edermünde', konze=None,
   coords="51.223 N · 9.426 E", dist="~37 km south — far outside the rim",
   juris="Kurfürstentum Hessen-Kassel until 1866 · Edermünde", confession="Evangelical/Lutheran",
   portal="archion", reg="—",
   overview="Grifte is a village in Eedermünde near Kassel, far south of the Deisel cluster, tested as a Tier-3 place-name candidate for the “Deissen” reading of “Deisse.”",
   sig="Tier-3 “Deissen” place-name candidate. Searched — <strong>negative; no Konze pool</strong>. Eliminated June 2026.",
   log=[("Parish search coverage","../search-coverage.html")]),

 dict(slug="diez", name="Diez", status="eliminated",
   sub="Hessen-Nassau toponym alternative ~135 km S (Lahn) · negative",
   german="Hessen-Nassau toponym alternative ~135 km south (Lahn)", konze=None,
   coords="50.369 N · 8.016 E", dist="~135 km south — far outside the rim",
   juris="Herzogtum Nassau → Provinz Hessen-Nassau (Prussia) · Lahn", confession="Evangelical",
   portal="hhstaw", reg="—",
   overview="Diez is a town on the Lahn in former Hessen-Nassau, far south of the Deisel cluster. It was tested only as a place-name alternative for the “Deisse, Kreis Cassel” reading.",
   sig="Hessen-Nassau place-name alternative tested against the “Deisse, Kreis Cassel” reading. <strong>No Konze pool; negative.</strong> Outside Churhessen and the surname cluster. Eliminated.",
   log=[("Parish search coverage","../search-coverage.html")]),

 dict(slug="dies", name="Dies", status="eliminated",
   sub="Hessen-Nassau toponym alternative ~135 km S (Rhein-Lahn) · negative",
   german="Hessen-Nassau toponym alternative ~135 km south (Rhein-Lahn)", konze=None,
   coords="50.345 N · 8.025 E", dist="~135 km south — far outside the rim",
   juris="Herzogtum Nassau → Provinz Hessen-Nassau (Prussia) · Rhein-Lahn", confession="Evangelical",
   portal="hhstaw", reg="—",
   overview="Dies is a very small place in the Rhein-Lahn area of former Hessen-Nassau, about 3 km from Diez (the two overlap on the parish map until you zoom in). Tested only as a place-name alternative for “Deisse.”",
   sig="Hessen-Nassau place-name alternative for “Deisse.” <strong>Outside Churhessen and with no surname pool; negative.</strong> Eliminated.",
   log=[("Parish search coverage","../search-coverage.html")]),

 dict(slug="schierstein", name="Schierstein", status="eliminated",
   sub='Rhine toponym alternative ~170 km S (Wiesbaden) · tested "Freudenberg / Schierstein" reading · negative',
   german="Rhine toponym alternative ~170 km south (Wiesbaden)", konze=None,
   coords="50.042 N · 8.192 E", dist="~170 km south — far outside the rim",
   juris="Provinz Hessen-Nassau (Prussia) · Wiesbaden · Rhine", confession="Evangelical",
   portal="hhstaw", reg="—",
   overview="Schierstein is a Rhine-side district of Wiesbaden in former Hessen-Nassau, far south of the Deisel cluster. It was tested only as a place-name alternative — the “Freudenberg / Schierstein” reading of the stated origin.",
   sig="Tested the “Freudenberg / Schierstein” reading of the place name. A Rhine parish with <strong>no Konze pool; negative.</strong> Eliminated.",
   log=[("Parish search coverage","../search-coverage.html")]),

 dict(slug="mainz", name="Mainz", status="eliminated",
   sub="Rheinhessen city ~175 km S · where Andreas Kontze died 1854 · the Konze family's southern settlement · no Charles-line birth ~1835",
   german="Rheinhessen city ~175 km south", konze="documented",
   coords="50.000 N · 8.271 E", dist="~175 km south — far outside the rim",
   juris="Großherzogtum Hessen (Hessen-Darmstadt) · Rheinhessen", confession="mixed (Catholic & Evangelical)",
   portal="other", reg="—",
   overview="Mainz, the Rheinhessen city on the Rhine, is far south of the Deisel cluster but enters the investigation as the place where the documented Friedrichsfeld Kontze branch settled — <em>Andreas Kontze</em> (b. 1 Oct 1795 Trendelburg) died here in 1854.",
   sig="Checked as the Konze family’s <strong>southern settlement</strong>, following Andreas Kontze’s line. There is <strong>no Charles-line male birth ~1835</strong> here; the branch settled south only after the 1840s. The Mainz trail documents where the family went, not where Charles was born. Eliminated as a birth parish (family trail).",
   log=[("Kontze family tree & research paths","../notes_view/Kontze_Family_Tree_and_Research_Paths.html")]),
]

def esc_attr(s):
    return s.replace('&','&amp;').replace('"','&quot;')

def og_desc(p):
    return esc_attr(p["sub"])

def wiki_name(name):
    # primary German place name for external link
    base = name.split(" / ")[0].split(" (")[0].split(" + ")[0].strip()
    return base

def register_card(p):
    if p["portal"] == "archion":
        reg = p["reg"]
        return f'''  <h3>Parish registers</h3>
  <div class="resource-grid">
    <div class="resource-card archion">
      <span class="source-label archion">Parish records</span>
      <h4>Archion — Kirchenkreis Hofgeismar</h4>
      <p>The Evangelical Church’s parish-register portal (subscription). Register holdings for this parish: <strong>KB {reg}</strong>. Searched for a male birth on/near 26 January 1835 in the Konze surname pool, or as an illegitimate birth.</p>
      <a href="https://www.archion.de/" target="_blank" rel="noopener noreferrer">archion.de ↗</a>
      <div class="archion-path"><strong>Archion path:</strong> <em>Browse → Hessen-Nassau → <a class="glossary-link" href="../glossary.html#g-kirchenkreis" title="Glossary: Kirchenkreis">Kirchenkreis</a> Hofgeismar → {p["name"]}</em></div>
    </div>
  </div>'''
    if p["portal"] == "matricula":
        return f'''  <h3>Parish registers</h3>
  <div class="resource-grid">
    <div class="resource-card archion">
      <span class="source-label archion">Catholic records</span>
      <h4>Matricula — Erzbistum Paderborn</h4>
      <p>Cross-border Catholic parish (Prussian Westphalia). Registers are on the free <strong>Matricula</strong> portal, not Archion. Parish identifier: <strong>{p["reg"]}</strong>. The January–February 1835 baptisms were read directly.</p>
      <a href="https://data.matricula-online.eu/en/deutschland/paderborn/" target="_blank" rel="noopener noreferrer">Matricula · Erzbistum Paderborn ↗</a>
    </div>
  </div>'''
    if p["portal"] == "open":
        return f'''  <h3>Parish registers</h3>
  <div class="resource-grid">
    <div class="resource-card archion">
      <span class="source-label archion">Coverage gap</span>
      <h4>Not digitised for 1835</h4>
      <p>{p["reg"]}. The 1835 volume is held on-site at the Landeskirchliches Archiv Kassel and is not available on Archion or FamilySearch online. This is an <strong>open</strong> gap in the candidate pool.</p>
      <a href="https://www.archion.de/" target="_blank" rel="noopener noreferrer">archion.de ↗</a>
    </div>
  </div>'''
    if p["portal"] == "hhstaw":
        return f'''  <h3>Parish registers</h3>
  <div class="resource-grid">
    <div class="resource-card archion">
      <span class="source-label archion">Toponym check</span>
      <h4>Hessen-Nassau — place-name reading test</h4>
      <p>This parish was tested only as a place-name alternative for the “Deisse, Kreis Cassel” reading, not as a candidate within the Konze surname cluster. Hessen-Nassau church records fall under the HHStAW (Wiesbaden) jurisdiction; no Konze pool exists here.</p>
      <a href="https://www.archion.de/" target="_blank" rel="noopener noreferrer">archion.de ↗</a>
    </div>
  </div>'''
    # other (Mainz)
    return f'''  <h3>Parish registers</h3>
  <div class="resource-grid">
    <div class="resource-card archion">
      <span class="source-label archion">Family-trail check</span>
      <h4>Großherzogtum Hessen — Rheinhessen</h4>
      <p>Mainz enters the investigation as the Friedrichsfeld Kontze branch’s southern settlement (Andreas Kontze d. 1854), not as a birth parish. Rheinhessen civil and church records fall under the Hessen-Darmstadt / Mainz jurisdictions.</p>
      <a href="https://www.familysearch.org/en/wiki/Mainz,_Hesse,_Germany_Genealogy" target="_blank" rel="noopener noreferrer">FamilySearch wiki ↗</a>
    </div>
  </div>'''

def konze_note(p):
    if p["konze"] == "documented":
        return '<div class="meta-row" style="margin-top:0.4rem;"><span class="pill" style="background:#caa23a;color:#1f1a14;">✦ Konze family documented here</span></div>'
    if p["konze"] == "claimed":
        return '<div class="meta-row" style="margin-top:0.4rem;"><span class="pill" style="background:transparent;border:1px dashed #caa23a;color:inherit;">✦ Konze claimed · unconfirmed</span></div>'
    return ""

def build(p):
    slug = p["slug"]; name = p["name"]
    canonical = f"{SITE}/towns/{slug}.html"
    ogdesc = og_desc(p)
    pill = STATUS_PILL[p["status"]]
    wname = wiki_name(name)
    wenc = urllib.parse.quote(wname.replace(" ", "_"))

    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<script id="theme-toggle-init">(function(){{try{{var t=localStorage.getItem("theme");document.documentElement.classList.add(t==="light"?"theme-light":"theme-dark");}}catch(e){{document.documentElement.classList.add("theme-dark");}}}})();</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1F1A14">
<title>{name} — Charles Research</title>
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="_shared.css?v=20260517-darkfix">
<link rel="stylesheet" href="../assets/theme.css?v=20260530c">
<link rel="stylesheet" href="../assets/cinematic.css?v=20260530c">
<link rel="stylesheet" href="../assets/dark-mode.css?v=20260530c">
<script defer src="../assets/theme-toggle.js?v=20260509-2330"></script>
<script defer src="../assets/site-search.js?v=20260529-mobilesearch"></script>
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Charles Research">
  <meta property="og:title" content="{esc_attr(name)} — Charles Research">
  <meta property="og:description" content="{ogdesc}">
  <meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og/towns.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:image" content="{SITE}/assets/og/towns.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc_attr(name)} — Charles Research">
  <meta name="twitter:description" content="{ogdesc}">
  <meta name="description" content="{ogdesc}">
<script defer src="../assets/cinematic.js"></script>
{NAV_ASSETS}
<!-- BEGIN-INJECTED-BREADCRUMB -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Towns & Villages", "item": "{SITE}/towns/" }},
    {{ "@type": "ListItem", "position": 3, "name": "{esc_attr(name)}" }}
  ]
}}
</script>
<!-- END-INJECTED-BREADCRUMB -->
<!-- BEGIN-INJECTED-ARTICLE -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "{canonical}#article",
  "headline": "{esc_attr(name)}",
  "url": "{canonical}",
  "isPartOf": {{ "@id": "{SITE}/#website" }},
  "author": [
    {{ "@type": "Person", "name": "Jed Johnson" }},
    {{ "@type": "Person", "name": "Peter Schräder" }}
  ],
  "publisher": {{ "@type": "Person", "name": "Jed Johnson", "url": "{SITE}/about.html" }},
  "inLanguage": "en-US",
  "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
  "dateModified": "2026-06-21",
  "description": "{ogdesc}"
}}
</script>
<!-- END-INJECTED-ARTICLE -->
</head>
<body class="cine-typography">
{NAV}


<header class="town-hero cinema-section-hero" data-tone="default">
  <div class="crumbs"><a href="../index.html">← Charles Research</a> &nbsp;/&nbsp; <a href="index.html">Towns</a> &nbsp;/&nbsp; {name}</div>
  <h1>{name} <span class="german">— {p["german"]}</span></h1>
  <div class="sub">{p["sub"]}</div>
  <div class="meta-row">
    <span class="pill">{pill}</span><span class="pill">{p["confession"]}</span><span class="pill">{esc_attr(p["dist"])}</span>
  </div>
  {konze_note(p)}
</header>

<a id="main" tabindex="-1" aria-hidden="true" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);"></a>
<main>

<section class="section">
  <h2>At a glance</h2>
  <table class="kv">
    <tr><td>Name</td><td><strong>{name}</strong></td></tr>
    <tr><td>Coordinates</td><td>{p["coords"]} · {esc_attr(p["dist"])}</td></tr>
    <tr><td>Jurisdiction (period)</td><td>{p["juris"]}</td></tr>
    <tr><td>Confession</td><td>{p["confession"]}</td></tr>
    <tr><td>Register holdings</td><td>{p["reg"]}</td></tr>
    <tr><td>Project status</td><td>{status_sentence(p)}</td></tr>
  </table>
</section>

<section class="section">
  <h2>Historical overview</h2>
  <p>{p["overview"]}</p>
</section>

<section class="section">
  <h2>Significance to the investigation</h2>
  <p>{p["sig"]}</p>
</section>

<section class="section">
  <h2>Research resources</h2>
{register_card(p)}

  <h3>Emigration &amp; civil records</h3>
  <div class="resource-grid">
    <div class="resource-card immigration">
      <span class="source-label immigration">Emigration register</span>
      <h4>LAGIS Hessen Auswanderer</h4>
      <p>Search this place in the Hessian state’s catalogue of documented emigrants (Kurhessen &amp; Hessen-Darmstadt, ~1830–1900).</p>
      <a href="https://www.lagis-hessen.de/de/subjects/index/sn/auswanderer" target="_blank" rel="noopener noreferrer">LAGIS Auswanderer ↗</a>
    </div>
    <div class="resource-card civil">
      <span class="source-label civil">State archive</span>
      <h4>{archive_card(p)}</h4>
      <p>{archive_blurb(p)}</p>
      <a href="{archive_url(p)}" target="_blank" rel="noopener noreferrer">{archive_link_label(p)} ↗</a>
    </div>
  </div>
</section>

<section class="section">
  <h2>Project session-notes</h2>
  <p class="small">The per-parish research log — what was searched, what was found, and the conclusion, with links to the full project session notes.</p>
  <ul>
{log_items(p)}
  </ul>
  <p class="small">See also the <a href="../germany/parish-map.html">Hessian Parish Map</a> · <a href="../search-coverage.html">Parish search coverage</a> · <a href="../negative-results.html">Negative-results audit</a>.</p>
</section>

<section class="section">
  <h2>External references</h2>
  <ul>
    <li><a href="https://de.wikipedia.org/wiki/{wenc}" target="_blank" rel="noopener noreferrer">Wikipedia (DE) · {esc_attr(wname)} ↗</a></li>
    <li><a href="https://www.lagis-hessen.de/de/subjects/index/sn/ol" target="_blank" rel="noopener noreferrer">LAGIS Ortslexikon (search) ↗</a></li>
  </ul>
</section>

<footer class="back-nav">
  <a href="../germany/parish-map.html">← Parish map</a>
  <a href="index.html">All towns</a>
  <a href="../germany/konze-family-by-town.html">Konze family by town →</a>
</footer>

</main>

{FOOTER}
</body>
</html>'''
    return head

def status_sentence(p):
    s = p["status"]
    if s == "open":
        return "<strong>Open · undigitised.</strong> A priority gap; the 1835 register is not online."
    if s == "working":
        return "<strong>Working hypothesis</strong> within the Konze surname pool."
    if s == "charles":
        return "<strong>Charles’s stated origin.</strong>"
    return "<strong>Eliminated.</strong> Searched for a 26 January 1835 male birth in the Konze pool (or as an illegitimate birth) — negative."

def archive_card(p):
    if p["portal"] == "matricula":
        return "LWL / Bistumsarchiv Paderborn"
    if p["portal"] == "hhstaw":
        return "HHStAW Wiesbaden"
    if p["portal"] == "other":
        return "Stadtarchiv / HHStAW (Rheinhessen)"
    return "HStAM Marburg"

def archive_blurb(p):
    if p["portal"] == "matricula":
        return "Prussian Westphalia civil and church administration; Catholic registers via Matricula, civil records via the North-Rhine-Westphalia state archives."
    if p["portal"] in ("hhstaw","other"):
        return "Hessen-Nassau / Hessen-Darmstadt records fall under the Wiesbaden state archive jurisdiction rather than Marburg."
    return "The Hessian state archive holds Kurhessen administrative files (1815–1866) — emigration permits, conscription rolls, tax registers — including the HStAM Bestand 180 Hofgeismar files."

def archive_url(p):
    return "https://arcinsys.hessen.de/"

def archive_link_label(p):
    return "arcinsys.hessen.de"

def log_items(p):
    out = []
    for label, href in p["log"]:
        out.append(f'    <li><a href="{href}">{label}</a></li>')
    return "\n".join(out)

count = 0
for p in P:
    html = build(p)
    path = os.path.join(TOWNS, p["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    count += 1
    print("wrote", path)
print(f"\nGenerated {count} parish pages.")
