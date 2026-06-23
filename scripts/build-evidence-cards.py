#!/usr/bin/env python3
"""
Generate per-card evidence pages from a small data dict.
Each page has full per-page metadata (title, description, OG, JSON-LD,
canonical) so the eight Key Evidence cards become citable URLs of their own.

Cross-links the cards together (prev / next) and back to /evidence/.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = ROOT / "evidence"
BASE = "https://charles-konzen-research.netlify.app"

CARDS = [
    {
        "n": 1, "slug": "card-1-trendelburg-kontzen",
        "title": "Card 1 — Trendelburg burial register 220096 · K-section",
        "subtitle": "1773–1824 · Trendelburg, Churhessen",
        "category": "★ Project conclusion",
        "tone": "major",  # darker tone for the lynchpin
        "abstract": "The convergent-evidence basis for the May 2026 surname conclusion: KONZEN. Trendelburg parish surname-pool documented continuously from 1773; the parish-internal cross-reference note 'siehe auch K. Contze, Cortze, Cordes, Contz' establishes orthographic interchangeability across K- and C-initial forms. The nine distinct American Charles-family renderings all converge on this German source.",
        "body_html": """
<p>The Trendelburg parish burial register <em>Kirchenbuch 220096</em> (1773–1824), accessed via Archion.de, contains the K-section family pool from which Charles Konzen most likely descends. Six specific <em>Kontzen</em> burials are documented (Philipp Kontzen 1773; Johann Henrich Kontzen 1773; Johann Friedrich Kontzen 1795; Andreas Kontzen I and II in the 1795 marriage / baptism on the same register image; Ludwig Kontzen 1824). Three <em>Kontze</em> burials add weight (Arnold Philipp 1780, Andreas 1800, child Johannes 1808). Two <em>Contze</em> primary entries (Andreas Contze 1800; Johann Christoph Contze 1808) document the C-initial variant.</p>
<p>The parish&rsquo;s own clerk, in the burial-index alphabetical apparatus, wrote the cross-reference note <em>&ldquo;siehe auch K. Contze, Cortze, Cordes, Contz&rdquo;</em> — establishing that the parish itself treated the K-, C-, and -en variants as orthographically interchangeable. <strong>This is what makes the nine American Charles-family renderings (Gonnson, Gansen, Gonsen, Konsen, Gonson, Jansen, Konzen, Gannsen, Conson) all readable as descendants of one German surname.</strong></p>
<p>Convergent-evidence reading: the 1875 St. Marcus baptism of Erwin Carl <em>Konsen</em> (Card 6) preserves the Hessian -en form; the 1890 death record of his sister Auguste reads &ldquo;Auguste Somers geb <em>Konzen</em>&rdquo; — the full Hessian z-form, fifteen years later, by a different scribe. The 1896 St. Marcus death record of wife Auguste at Charles&rsquo;s direct dictation (Card 8) reads <em>Conson</em> — the C-initial form that ties straight to the Trendelburg parish&rsquo;s own Contze entries.</p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full convergent-evidence card on the homepage", "../index.html#evidence"),
            ("The Konzen puzzle (linguistic analysis)", "../germany/konzen-puzzle.html"),
            ("Trendelburg town page", "../towns/trendelburg.html"),
            ("Project Abstract", "../abstract.html"),
        ],
        "scan": None,
    },
    {
        "n": 2, "slug": "card-2-civil-war-enlistment",
        "title": "Card 2 — Civil War enlistment record · 'Freundburg, Kurhessen'",
        "subtitle": "2 December 1862 · St. Louis",
        "category": "1st Kurhessen reference",
        "tone": "default",
        "abstract": "The first mention of a town and state anywhere in Charles's documentary record. Peter Schräder's 26 February 2026 phonetic re-reading decoded 'Freundburg' as a clerk's mishearing of Trendelburg. The working geographic anchor of the entire investigation.",
        "body_html": """
<p>On 2 December 1862, Charles enlisted in St. Louis with Battery B of the 2nd Missouri Light Artillery (Union). The enlistment register names his birthplace as <em>&ldquo;Freundburg, Kurhessen&rdquo;</em> — a town that does not exist on any Hessian map.</p>
<p>The phonetic decoding originally proposed by Peter Schr&auml;der in his 26 February 2026 letter reads the entry as a clerk&rsquo;s mishearing of <strong>Trendelburg</strong>. The German <em>Tr-</em> cluster (an unfamiliar onset to an English-speaking American clerk) heard as <em>Fr-</em>; the meaningless syllable <em>-endel-</em> normalised to the familiar German word <em>Freund-</em> (&ldquo;friend&rdquo;); the trailing <em>-burg</em> preserved exactly. This decoding has been reaffirmed by Schr&auml;der in subsequent correspondence (6 December 2026).</p>
<p>The political designation <strong>&ldquo;Kurhessen&rdquo;</strong> on this record is the first of four explicit Kurhessen / Hesse-Kassel references across Charles&rsquo;s U.S. documentary record (the other three: 1866 marriage register &ldquo;Churhessen&rdquo; on Card 3; 1866 firstborn naming on Card 4; 1868 naturalization renouncing the King of Prussia on Card 5). The cumulative pattern across six years and four independent documents is one of the strongest identity signals the project has assembled.</p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full card on the homepage", "../index.html#evidence"),
            ("Research log: Freundburg, Kurhessen", "../research_logs/freundburg-kurhessen.html"),
            ("Civil War section", "../civilwar/"),
            ("Compiled Service Record (NARA)", "../sources/nara-service-record-packet.html"),
        ],
        "scan": {
            "src": "../evidence_images/evidence_1_civil_war.jpg",
            "alt": "Battery B, 2nd Missouri Light Artillery enlistment register entry, 2 December 1862, naming Charles's birthplace as 'Freundburg, Kurhessen' — decoded by Peter Schräder as Trendelburg.",
            "title": "Enlistment register · 2 Dec 1862",
            "source": "NARA Compiled Service Record (M405, file G11-422819443E)",
            "height": "tall",
        },
    },
    {
        "n": 3, "slug": "card-3-marriage-register",
        "title": "Card 3 — St. Marcus marriage register · Pastor Wall",
        "subtitle": "7 January 1866 · St. Louis",
        "category": "Marriage register",
        "tone": "default",
        "abstract": "Charles's own statement of origin: 'aus Deisse, Kreis Cassel, Churhessen' — the village of Deisel inside the Electorate of Hesse-Kassel. Surname recorded as Gonnson. With Card 2's Freundburg decoding, this triangulates the answer to a 5×5 km square inside the Kreis Hofgeismar.",
        "body_html": """
<p>St. Marcus Evangelical Church marriage register, A.D. 1866 — page 134-135, entry No. 676 (running entry &numero;4): the marriage of <strong>Carl Gonnson</strong> &amp; <strong>Auguste Kreichelt</strong>, recorded 7 January 1866 by Pastor <strong>Georg Wendelin Wall</strong> (W&uuml;rttemberger; St. Marcus 1850–1866). Charles&rsquo;s stated origin: <em>&ldquo;aus Deisse, Kreis Cassel, Churhessen&rdquo;</em> — the village of <strong>Deisel</strong> in the Trendelburg parish complex, inside the Electorate of Hesse-Kassel.</p>
<p>This is the entry that ties the May 2026 Konzen surname conclusion to a specific Hessian territorial reference. Triangulated with Card 2&rsquo;s &ldquo;Freundburg&rdquo; (= Trendelburg) decoding, the answer is bounded to a 5&nbsp;km &times; 5&nbsp;km square inside the Kreis Hofgeismar.</p>
<p>The surname rendering &ldquo;Gonnson&rdquo; here is the first of nine distinct American captures of Charles&rsquo;s German surname (Gonnson 1866 · Gansen 1870 · Gonsen 1872 · Konsen 1875 · Gonson 1880 · Jansen 1881 · Konzen 1890 · Gannsen 1895 · Conson 1896). All nine converge on the Trendelburg Kontzen / Contzen pool.</p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full card on the homepage", "../index.html#evidence"),
            ("Auguste Kreichelt biography", "../people/auguste-kreichelt.html"),
            ("Deisel village page", "../towns/deisel.html"),
        ],
        "scan": {
            "src": "../evidence_images/evidence_3_marriage.webp",
            "alt": "St. Marcus Evangelical Church marriage register, 7 January 1866, recording 'Carl Gonnson' aus Deisse, Kreis Cassel, Churhessen, marrying Auguste Kreichelt — Pastor Wendelin Wall officiating.",
            "title": "St. Marcus marriage register · 7 Jan 1866",
            "source": "St. Marcus Evangelical Church marriage register, page 134–135, entry No. 676",
            "height": "tall",
        },
    },
    {
        "n": 4, "slug": "card-4-seven-baptisms",
        "title": "Card 4 — Seven St. Marcus baptisms · 1866–1880",
        "subtitle": "1866–1880 · St. Louis",
        "category": "Baptisms · sponsor pattern",
        "tone": "default",
        "abstract": "Charles & Auguste's seven children. The baptismal records carry the surname trail (Gonnson, Gansen, Gonsen, Konsen, Jansen) and the Pastor Braschler 'smoking gun' pair (1870 vs 1872). Sponsor reconciliation across all seven baptisms reveals not a single Charles-side blood relative — the structural support for the 'immigrated alone' hypothesis.",
        "body_html": """
<p>Seven children, every baptism recorded at <strong>St. Marcus German Evangelical Church</strong>, the German-Evangelical congregation on DeKalb Street descended from the Reformed-Lutheran tradition of Kurhessen / Hesse-Kassel: Friedrich Wilhelm (1866-1867) · Maria Josephine (1868-1890) · Katherine Carolina (1870-1949) · Auguste (1872-1890) · Louise (1873-1947) · Erwin Carl <em>Konsen</em> (1875-1950) · Bertha (1880-1959).</p>
<p>The seven baptismal entries collectively yield <strong>five</strong> of the nine distinct surname renderings: <em>Gonnson</em> (Wall) · <em>Gansen</em> (Braschler) · <em>Gonsen</em> (Braschler again, two years later, different vowel — the &ldquo;Pastor Braschler smoking gun&rdquo; that proves the spelling came from Charles&rsquo;s mouth, not the pastor&rsquo;s pen) · <em>Konsen</em> (Hoffmann) · <em>Jansen</em> (Nollau).</p>
<p><strong>The sponsorship pattern is structurally diagnostic.</strong> Across all seven baptisms — fifteen named sponsors across seventeen sponsorship slots — <em>not a single sponsor traces to Charles&rsquo;s side of the family</em>. Every kin sponsor is from Auguste&rsquo;s Kreichelt-Albrecht-Pillmann-Mincke side. German-Lutheran baptismal sponsorship in this period was structurally a kin-default convention; the asymmetry across Charles&rsquo;s seven baptisms is consistent with Charles having no German blood family accessible by mail or in person between 1866 and 1880, corroborating the working hypothesis that he immigrated alone in 1859.</p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full card on the homepage", "../index.html#evidence"),
            ("The seven children", "../charles_america/seven-children.html"),
            ("Story · Seven baptisms", "../stories/9-alone.html"),
            ("Children index", "../children/"),
        ],
        "scan": {
            "src": "../evidence_images/baptism_1866_friedrich_wilhelm_gonnson.webp",
            "alt": "1866 St. Marcus baptism register entry for Friedrich Wilhelm Gonnson — first of Charles & Auguste's seven children. Pastor Wendelin Wall.",
            "title": "St. Marcus baptism · Friedrich Wilhelm Gonnson · 1866",
            "source": "St. Marcus Evangelical Church baptism register",
            "height": "default",
        },
    },
    {
        "n": 5, "slug": "card-5-naturalization",
        "title": "Card 5 — U.S. Naturalization record",
        "subtitle": "21 October 1868 · St. Louis",
        "category": "4th Kurhessen reference",
        "tone": "default",
        "abstract": "Charles's formal U.S. citizenship grant. The renunciation language is politically loaded: he formally renounces 'the King of Prussia', not the Elector of Hesse — confirming that he both knew his homeland of Kurhessen had been absorbed by Prussia in 1866 and made the formal civic acknowledgment of that fact.",
        "body_html": """
<p>Charles&rsquo;s definitive U.S. naturalization is recorded on 21 October 1868 in St. Louis — three years after his discharge from Battery&nbsp;B, nine years after his 1859 immigration. The document records him as <strong>Charles Gannsen</strong> (the Anglicised form he kept under the Civil War clerk&rsquo;s hand) and contains the standard renunciation language.</p>
<p><strong>The renunciation is politically loaded.</strong> Charles formally renounces <em>&ldquo;the King of Prussia&rdquo;</em>, not the Elector of Hesse. By autumn 1868 his homeland of Kurhessen no longer existed: Prussian armies had overrun Hesse-Kassel in summer 1866 and annexed the Electorate; Friedrich Wilhelm I, the only sovereign Charles had ever known as an adult and the namesake of his firstborn son in 1866 (Card 4), had been deposed two years earlier. <em>Charles renouncing the King of Prussia rather than the Elector of Hesse confirms that he both knew his homeland had been absorbed and made the formal civic acknowledgment of that fact.</em></p>
<p>This is the <strong>fourth Kurhessen reference</strong> in Charles&rsquo;s U.S. documentary record (after the 1862 enlistment, the 1866 marriage register, and the 1866 firstborn naming). It is independently corroborated by the 1900 federal census, which records Charles as <em>&ldquo;naturalized.&rdquo;</em></p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full card on the homepage", "../index.html#evidence"),
            ("Imaged source", "../sources/naturalization-record.html"),
        ],
        "scan": None,
    },
    {
        "n": 6, "slug": "card-6-1875-baptism-konsen",
        "title": "Card 6 — 1875 St. Marcus baptism · Erwin Carl Konsen",
        "subtitle": "27 August 1875 · Pastor Julius Hoffmann",
        "category": "Konsen attestation · linguistic time capsule",
        "tone": "default",
        "abstract": "The strongest direct surname link between Charles in St. Louis and the Konze line in Hesse: Pastor Hoffmann recorded his sixth child as Erwin Carl Konsen, preserving the German -en form. The 1890 daughter's death record reads Konsen a second time, fifteen years later — establishing two-record persistence by two different scribes.",
        "body_html": """
<p>Pastor <strong>Julius Hoffmann</strong>, Braschler&rsquo;s successor at St. Marcus from May 1875, recorded Charles&rsquo;s sixth child&rsquo;s baptism on 27 August 1875: <strong>&ldquo;Erwin Carl Konsen · Geburt: 27. Aug. 1875 · Taufe: 3. Oct. 1875 · Eltern: Carl Konsen u. d. ihm Ehefrau Auguste geb. Kreichelt · Pathen: Erwin Sproul, der Vater des Kindes.&rdquo;</strong></p>
<p>Hoffmann recorded the surname here as <strong>KONSEN</strong> — preserving the German-Hessian form 16 years after Charles emigrated. The closest German precedent is <em>Kontzen / Contzen</em>: only the soft <em>t</em> in the <em>tz</em> cluster collapses to <em>s</em>; the terminal <em>-en</em> is identical. Near-direct match.</p>
<p><strong>The Hessian -en form recurs.</strong> Fifteen years later, on the 1890 death record of Erwin Carl&rsquo;s sister Auguste, the maiden-name attestation reads <em>&ldquo;Auguste Somers geb Konzen&rdquo;</em> — the full Hessian z-form, by a different scribe (reading confirmed in the 17 May 2026 re-examination). <strong>Two-record persistence by two different scribes — <em>Konsen</em> 1875 with an s, <em>Konzen</em> 1890 with a z — is direct evidence that the German-Hessian surname was Charles&rsquo;s actual self-identification</strong>; the family kept the Hessian K-initial / <em>-en</em> form in continuous use across at least 15 years.</p>
<p>Erwin Carl went by &ldquo;Charles Johnson Jr.&rdquo; in adulthood, but the baptism preserves both his original given name and the parental surname in its German form &mdash; a linguistic time-capsule of the form Charles brought to America in 1859.</p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full card on the homepage", "../index.html#evidence"),
            ("Erwin Carl Konsen biography", "../children/erwin-carl-konsen.html"),
            ("The Konzen puzzle (linguistic analysis)", "../germany/konzen-puzzle.html"),
            ("Story · Konsen twice", "../stories/7-konsen.html"),
        ],
        "scan": {
            "src": "../evidence_images/evidence_4_baptism.webp",
            "alt": "1875 St. Marcus baptism register entry for Erwin Carl Konsen, Charles & Auguste's sixth child — Pastor Julius Hoffmann recording the surname as 'Konsen', the older Hessian -en form.",
            "title": "St. Marcus baptism · Erwin Carl Konsen · 27 Aug 1875",
            "source": "St. Marcus Evangelical Church baptism register, Pastor Julius Hoffmann",
            "height": "default",
        },
    },
    {
        "n": 7, "slug": "card-7-pension-file",
        "title": "Card 7 — Civil War Pension File F41-523680269E",
        "subtitle": "1890–1903 · NARA",
        "category": "Pension file · seven affidavits",
        "tone": "default",
        "abstract": "The richest U.S. document — birthdate, addresses, witnesses. No family-side affidavits — Charles emigrated alone. Page-by-page audit confirms: the pension file does not contain any Charles-self-stated birthplace declaration; its Kurhessen attribution is solely via the embedded 1862 service record.",
        "body_html": """
<p>The full pension file (NARA F41-523680269E) is the richest U.S. document the project has obtained: pension applications, supporting medical opinions, claim agent correspondence, and seven witness affidavits collected by St.&nbsp;Louis claim agent <strong>Fred. W. Fout</strong> in 1889&ndash;1891.</p>
<p><strong>No family-side affidavits</strong>. Of the seven personal witnesses now identified, four were Missouri Light Artillery veterans &mdash; the same Battery&nbsp;B alumni network. The narrative phrasings recur word-for-word across affidavits, identifying Fout&rsquo;s drafting hand. This pattern is the basis for the project&rsquo;s &ldquo;Pension Mutual-Aid Network&rdquo; theme: a coordinated mutual-aid filing run through a single Light Artillery alumni network rather than through Charles&rsquo;s family.</p>
<p>The pension file&rsquo;s Kurhessen reference is solely via the embedded 1862 Compiled Service Record bundled into the claim as proof of service. The pension file therefore reproduces, but does not independently re-attest, the Kurhessen identification on Card 2. <strong>Bonus finding from page 13:</strong> Charles&rsquo;s own 1898 affidavit names Pastor &ldquo;Geo. W. Wall&rdquo; as the officiant of his 1866 St. Marcus marriage &mdash; confirming Wall&rsquo;s role in his own hand 32 years after the wedding.</p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full card on the homepage", "../index.html#evidence"),
            ("Imaged source", "../sources/pension-file.html"),
            ("Pension Mutual-Aid theme", "../themes/pension-mutual-aid.html"),
        ],
        "scan": None,
    },
    {
        "n": 8, "slug": "card-8-1896-conson",
        "title": "Card 8 — 1896 St. Marcus death record · 'Auguste Conson'",
        "subtitle": "1896 · Pastor Eilt Heeren Eilts",
        "category": "Charles-self-attestation",
        "tone": "default",
        "abstract": "The strongest single Charles-self-attestation of his surname. Charles, age 61, gave Auguste's name to Pastor Eilts at the funeral; Eilts wrote what he heard — the C-initial form (Conson) that ties straight back to the Trendelburg Contzen line.",
        "body_html": """
<p>St. Marcus death register, 1896 entry: the funeral of <strong>Auguste Kreichelt Konzen</strong>, Charles&rsquo;s wife. Recorded by <strong>Pastor Eilt Heeren Eilts</strong> with <strong>Charles himself as the surviving informant</strong>. The maiden-name attestation reads &ldquo;Auguste <em>Conson</em>&rdquo; — the C-initial form that pairs directly with the Trendelburg parish&rsquo;s own Contze / Contzen entries (Card 1).</p>
<p>This is the project&rsquo;s strongest single Charles-self-attestation. Charles, age 61, walked into the parish, gave his deceased wife&rsquo;s name and his own surname directly to Eilts, and Eilts wrote what he heard. The C-initial form preserves the German <em>C</em>-initial documented in the Trendelburg parish itself (the cross-reference note &ldquo;siehe auch K. Contze, Cortze, Cordes, Contz&rdquo; plus primary entries Andreas Contze 1800, Johann Christoph Contze 1808), drops the silent <em>t</em>, softens the <em>tz</em> affricate to <em>s</em>, and Anglicizes the suffix to <em>-on</em>.</p>
<p><strong>Bookend Charles-self-attestations.</strong> Charles is the documented speaker at <em>both</em> ends of the surname trail: at his 1866 marriage (groom giving his name to Pastor Wall &rarr; <em>Gonnson</em>) and at his wife&rsquo;s 1896 funeral 30 years later (surviving spouse, the standard informant for a deceased spouse &rarr; <em>Conson</em>). Both records capture a [&#39674;n.s&#601;n] sound. The other three Charles-family records in between (1872 <em>Gonsen</em>, 1875 <em>Konsen</em>, 1890 <em>Konzen</em>) plausibly reflect the same spoken name to a clerk's ear &mdash; though the C-/G-initial varies.</p>
""",
        "evidence_status": "Confirmed",
        "external_anchors": [
            ("Full card on the homepage", "../index.html#evidence"),
            ("Story · Pastor speakers", "../stories/6-braschler.html"),
            ("Auguste Kreichelt biography", "../people/auguste-kreichelt.html"),
        ],
        "scan": {
            "src": "../evidence_images/death_1896_auguste_kreichelt_conson.webp",
            "alt": "1896 St. Marcus death register entry for Auguste Kreichelt — recorded as 'Auguste Conson' by Pastor Eilt Heeren Eilts at Charles's direct dictation, the strongest single Charles-self-attestation of the surname.",
            "title": "St. Marcus death register · Auguste 'Conson' · 1896",
            "source": "St. Marcus Evangelical Church death register, Pastor Eilt Heeren Eilts",
            "height": "default",
        },
    },
]


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#1F1A14">
<title>{title} — Charles Konzen Research</title>
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="../assets/theme.css">
<link rel="stylesheet" href="../assets/cinematic.css">
<meta name="description" content="{abstract_attr}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Charles Konzen Research">
<meta property="og:title" content="{title} — Charles Konzen Research">
<meta property="og:description" content="{abstract_attr}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="../assets/figures/og-card.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — Charles Konzen Research">
<meta name="twitter:description" content="{abstract_attr}">
<meta name="twitter:image" content="../assets/figures/og-card.svg">
<style>
  *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: var(--font-serif); background: var(--bg-page); color: var(--text-body); line-height: 1.65; }}
  header.card-hero {{
    background: linear-gradient(135deg, var(--bg-deep) 0%, var(--bg-deep-grad) 100%);
    color: var(--text-on-dark);
    padding: 2.2rem 1.5rem 1.6rem;
    border-bottom: 4px double var(--brand);
  }}
  header.card-hero.major {{ background: linear-gradient(135deg, #2c1f14 0%, #5a3a22 100%); }}
  header.card-hero .crumbs {{ font-size: 0.84rem; color: var(--text-on-dark-d); margin-bottom: 0.5rem; }}
  header.card-hero .crumbs a {{ color: var(--brand); border-bottom: none; }}
  header.card-hero .cardnum {{ font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--brand); font-weight: 700; margin-bottom: 0.4rem; }}
  header.card-hero h1 {{ color: var(--text-on-dark); font-size: 2rem; max-width: 880px; }}
  header.card-hero .when {{ color: var(--text-on-dark-d); font-style: italic; margin-top: 0.4rem; font-family: var(--font-mono); font-size: 0.85rem; }}
  main {{ max-width: 1100px; margin: 0 auto; padding: 1.8rem 1.4rem 4rem; }}
  .lede {{ font-size: 1.06rem; color: var(--text-meta); font-style: italic; margin-bottom: 1.4rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border-light); }}
  .body-prose p {{ margin-bottom: 1rem; }}
  a {{ color: var(--brand-dark); border-bottom: 1px dotted var(--border-medium); text-decoration: none; }}
  a:hover {{ color: var(--brand); }}
  h2 {{ font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--brand-dark); margin: 2rem 0 0.7rem; border-bottom: 1px solid var(--border-medium); padding-bottom: 0.3rem; }}
  .links {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem; }}
  .links a {{ display: inline-block; padding: 0.4rem 0.85rem; background: var(--bg-card); border: 1px solid var(--border-medium); border-left: 3px solid var(--brand); border-radius: 3px; font-size: 0.88rem; color: var(--brand-dark); border-bottom: 1px solid var(--border-medium); }}
  .links a:hover {{ background: var(--brand-tint, #fffaee); }}
  .pager {{ display: flex; justify-content: space-between; align-items: center; margin-top: 2.4rem; padding-top: 1rem; border-top: 1px solid var(--border-light); font-size: 0.92rem; }}
  .pager a {{ color: var(--brand-dark); border-bottom: none; padding: 0.5rem 0.9rem; background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 3px; max-width: 46%; }}
  .pager a:hover {{ background: var(--brand-tint, #fffaee); }}
  .pager .nlabel {{ font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.07em; color: var(--text-muted); display: block; }}
  .pager .nlabel + span {{ display: block; color: var(--text-strong); margin-top: 0.15rem; }}
  /* Respect prefers-reduced-motion (audit-fix pass, 8 May 2026). */
  @media (prefers-reduced-motion: reduce) {{
    *, *::before, *::after {{ animation-duration: 0.001ms !important; transition-duration: 0.001ms !important; scroll-behavior: auto !important; }}
  }}
</style>
<script defer src="../assets/site-search.js"></script>
<script defer src="../assets/cinematic.js"></script>
<link rel="stylesheet" href="../assets/site-nav.css">
<script defer src="../assets/site-nav.js"></script>
<link rel="stylesheet" href="../assets/cite-widget.css">
<script defer src="../assets/cite-widget.js"></script>
<link rel="stylesheet" href="../assets/deep-zoom.css">
<script defer src="../assets/deep-zoom.js"></script>
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body class="cine-typography">

<header class="card-hero {hero_class}">
  <div class="crumbs"><a href="../index.html">← Charles Konzen Research</a> &nbsp;/&nbsp; <a href="index.html">Key Evidence</a> &nbsp;/&nbsp; Card {n}</div>
  <div class="cardnum">Card {n} &middot; {category}</div>
  <h1>{h1}</h1>
  <div class="when">{subtitle}</div>
</header>

<main>

<p class="lede">{abstract_html}</p>

{scan_html}

<section class="body-prose">
{body_html}
</section>

<h2>Related links</h2>
<div class="links">
{links_html}
</div>

<div class="pager">
{pager_html}
</div>

</main>

</body>
</html>
"""


def render_card(card: dict, prev_card: dict | None, next_card: dict | None) -> str:
    n = card["n"]
    url = f"{BASE}/evidence/{card['slug']}.html"
    abstract_attr = card["abstract"].replace('"', '&quot;')
    abstract_html = card["abstract"].replace("'", "&rsquo;")
    h1_clean = card["title"].replace(f"Card {n} — ", "")
    title_no_dash = card["title"]

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": url + "#article",
        "headline": title_no_dash,
        "alternativeHeadline": h1_clean,
        "description": card["abstract"],
        "datePublished": "2026-04-01",
        "dateModified": "2026-05-08",
        "url": url,
        "isPartOf": {"@id": f"{BASE}/#website"},
        "about": {"@id": f"{BASE}/#charles"},
        "author": [
            {"@type": "Person", "name": "Jed Johnson"},
            {"@type": "Person", "name": "Peter Schräder"},
        ],
        "publisher": {"@type": "Person", "name": "Jed Johnson", "url": f"{BASE}/about.html"},
        "inLanguage": "en-US",
        "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
        "creditText": f"Charles Konzen Research, Key Evidence Card {n}",
    }

    scan_html = ""
    scan = card.get("scan")
    if scan:
        height_class = ""
        if scan.get("height") == "tall":
            height_class = " tall"
        elif scan.get("height") == "short":
            height_class = " short"
        scan_html = (
            f'<figure class="deep-zoom" data-src="{scan["src"]}" data-nav>\n'
            f'  <div class="dz-meta">\n'
            f'    <span class="dz-icon" aria-hidden="true">&#x1F50D;</span>\n'
            f'    <span class="dz-title">{scan["title"]}</span>\n'
            f'    <span class="dz-source">&middot; {scan["source"]}</span>\n'
            f'    <a href="{scan["src"]}" target="_blank" rel="noopener">Open scan in new tab &#x2197;</a>\n'
            f'  </div>\n'
            f'  <div class="dz-stage{height_class}">\n'
            f'    <img class="dz-fallback" src="{scan["src"]}" alt="{scan["alt"]}" loading="lazy">\n'
            f'    <div class="dz-loading">Loading high-resolution scan&hellip;</div>\n'
            f'  </div>\n'
            f'  <img class="dz-print-img" src="{scan["src"]}" alt="">\n'
            f'  <figcaption><strong>{scan["title"]}.</strong> {scan["alt"]}</figcaption>\n'
            f'</figure>'
        )

    links_html = "\n".join(f'  <a href="{href}">{label}</a>' for label, href in card["external_anchors"])

    pager_parts = []
    if prev_card:
        pager_parts.append(
            f'<a href="{prev_card["slug"]}.html"><span class="nlabel">← Card {prev_card["n"]}</span><span>{prev_card["title"].split(" — ", 1)[1]}</span></a>'
        )
    else:
        pager_parts.append('<a href="index.html"><span class="nlabel">← Back</span><span>Key Evidence index</span></a>')
    if next_card:
        pager_parts.append(
            f'<a href="{next_card["slug"]}.html"><span class="nlabel">Card {next_card["n"]} →</span><span>{next_card["title"].split(" — ", 1)[1]}</span></a>'
        )
    else:
        pager_parts.append('<a href="index.html"><span class="nlabel">Back →</span><span>Key Evidence index</span></a>')
    pager_html = "\n".join("  " + p for p in pager_parts)

    return PAGE_TEMPLATE.format(
        title=title_no_dash,
        url=url,
        abstract_attr=abstract_attr,
        abstract_html=abstract_html,
        body_html=card["body_html"],
        scan_html=scan_html,
        n=n,
        category=card["category"],
        subtitle=card["subtitle"],
        hero_class=card["tone"] if card["tone"] != "default" else "",
        h1=h1_clean,
        jsonld=json.dumps(jsonld, indent=2, ensure_ascii=False),
        links_html=links_html,
        pager_html=pager_html,
    )


def main() -> int:
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    for i, card in enumerate(CARDS):
        prev_c = CARDS[i - 1] if i > 0 else None
        next_c = CARDS[i + 1] if i < len(CARDS) - 1 else None
        path = EVIDENCE_DIR / f"{card['slug']}.html"
        path.write_text(render_card(card, prev_c, next_c), encoding="utf-8")
        print(f"  wrote {path.relative_to(ROOT)}")
    print(f"\nGenerated {len(CARDS)} evidence card pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
