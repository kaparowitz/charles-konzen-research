#!/usr/bin/env python3
"""
Insert a plain-language family-reader intro paragraph BEFORE the existing
<p class="bottom-line"> in every people/*.html and children/*.html page.

Idempotent: re-running skips pages that already have <p class="family-intro">.

The intros are hand-crafted per page (lookup table below) so they accurately
describe the person's relationship to Charles in plain English. The existing
dense bottom-line paragraph (with FS-IDs, vital details, research framing) is
preserved intact — it remains directly below the new intro for readers who
want the full rigor.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path("/sessions/great-friendly-turing/mnt/Charles Gannsen Research")

# Hand-crafted plain-language openers, keyed by page filename.
# Each opener is 1–3 sentences in family-reader voice.
INTROS = {
    # ---------- The seven children (direct family) ----------
    "children/friedrich-wilhelm.html":
        "Charles and Auguste's firstborn son. He arrived in June 1866 — just months after their wedding — and died as an infant 16 months later. He never knew his six younger siblings.",

    "children/josephine-maria.html":
        "Charles and Auguste's second child and the first to survive infancy. She lived 22 years and died young in 1890. Her 1868 baptism is one of the eight U.S. records that preserve a phonetic spelling of the family surname.",

    "children/katherine-carolina.html":
        "Charles and Auguste's third child. She lived to seventy-nine, married into the Ruddy family, and was known to her family as Kate. Her 1870 baptism is the famous “Braschler smoking-gun” record — the same pastor who would baptise her sister Auguste two years later wrote two different spellings of the family name, evidence that the spelling came from Charles's own voice.",

    "children/auguste.html":
        "Charles and Auguste's fourth child, named directly after her mother. She lived 18 years and died young in 1890 — the same year as her older sister Josephine. Her 1890 death record is the single American attestation of the full Hessian z-form spelling “Konzen”, and the bridge to the German parish-register surname pool.",

    "children/louise.html":
        "Charles and Auguste's fifth child. She lived to seventy-four, married into the Foster family, and was known to her family simply as Louise.",

    "children/erwin-carl-konsen.html":
        "Charles and Auguste's sixth child and the one who, as an adult, carried his father's name into the next generation as <em>Charles Johnson Jr.</em> He lived to seventy-four and married Katherine Misch. His 1875 baptism is the keystone evidence record for the surname investigation: the parish clerk wrote his surname as <em>Konsen</em> &mdash; the closest match to the German Hessian spelling found anywhere on the U.S. record trail.",

    "children/bertha.html":
        "Charles and Auguste's seventh and youngest child, born Christmas Day 1880. She lived to seventy-nine, married into the Johnson family, and outlived all of her siblings.",

    # ---------- Auguste, Charles's wife (the family page) ----------
    "people/auguste-kreichelt.html":
        "<strong>Auguste was Charles's wife</strong> and the mother of all seven of his children. She was born around 1840 in Clausthal &mdash; a mining town in what is now Lower Saxony &mdash; and came to the United States with her parents in 1853 when she was about thirteen. She and Charles married at St. Marcus German Evangelical Church in St. Louis on 7 January 1866 and remained married for thirty years; she died in 1896, eight years before Charles. The 1896 St. Marcus death register records her surname as <em>Conson</em> &mdash; one of the eight American spellings of the family name that anchor the surname-trail evidence on this site.",

    # ---------- The Kreichelt in-laws (Auguste's parents and siblings) ----------
    "people/georg-kreichelt.html":
        "Charles's father-in-law &mdash; Auguste's father. A Hannoverian who brought his eight-child family to St. Louis in 1853 and later served alongside Charles in the same Civil War battery.",

    "people/henriette-kreichelt.html":
        "Charles's mother-in-law &mdash; Auguste's mother. She sponsored three of Charles and Auguste's seven baptisms.",

    "people/august-kreichelt.html":
        "Charles's brother-in-law &mdash; Auguste's eldest brother &mdash; and a Civil War comrade. The two served together in Battery B, 2nd Missouri Light Artillery.",

    "people/amalia-muenke.html":
        "Charles's sister-in-law by marriage &mdash; the wife of August Kreichelt (Auguste's eldest brother). She sponsored one of Charles and Auguste's children at baptism.",

    "people/carl-kreichelt.html":
        "Charles's brother-in-law &mdash; another of Auguste's brothers. By the late 19th century he had become a St. Louis saloonist and real-estate investor.",

    "people/catharina-albrecht.html":
        "Charles's sister-in-law by marriage &mdash; the fiancée (and later wife) of Carl Kreichelt when she sponsored the 1870 Katherine Carolina baptism.",

    "people/bertha-barbara-kreichelt.html":
        "Charles's sister-in-law &mdash; Auguste's youngest sister, known in the family as Babette. She sponsored two of Charles and Auguste's children at baptism.",

    # ---------- Daughter-in-law and the Misch/Gottlob bridge ----------
    "people/katherine-misch.html":
        "Charles's daughter-in-law &mdash; she married his son Erwin Carl (later <em>Charles Johnson Jr.</em>). Through her mother's second marriage she also became step-related to the Gottlob line, which is how the family-tree branches of this site connect.",

    "people/christina-hahl.html":
        "Charles's son's mother-in-law &mdash; Katherine Misch's mother. Her second marriage to Theodore Gottlob is the family-tree link that connects the Charles Konzen line to the Gottlob line. (For the site author Jed Johnson, she is a 2nd-great-grandmother.)",

    "people/theodore-gottlob.html":
        "Charles's next-door neighbor on DeKalb Street in St. Louis &mdash; and, via second marriages, the eventual grandfather of Charles's grandson. He co-witnessed Charles's 1890 pension declaration. (For the site author Jed Johnson, he is a 2nd-great-grandfather.)",

    # ---------- Civil War / Battery B comrades and pension witnesses ----------
    "people/adam-herweck.html":
        "The first witness named on Charles and Auguste's 1866 marriage register entry. A Hesse-born sergeant in the same Battery B that Charles would later serve in.",

    "people/august-derr.html":
        "Charles's direct supervisor during the Civil War &mdash; the 1st Sergeant of Company B, 2nd Missouri Light Artillery. He swore two pension affidavits for Charles in 1891.",

    "people/christian-meyer.html":
        "A Battery B private who served alongside Charles. His 1891 affidavit independently confirms two key events Charles cited in his pension claim: a September 1863 hearing-loss incident at New Madrid, and a November 1863 rupture.",

    "people/henry-stoll.html":
        "A Swiss-born St. Louis acquaintance who had known Charles since 1867. His 1890 affidavit testified to 24+ years' acquaintance and to Charles's pension-relevant injuries.",

    "people/henry-niemeier.html":
        "The longest-tenure civilian witness in Charles's pension file &mdash; a Westphalia-born acquaintance whose 1890 affidavit attested to 26 years of personal acquaintance.",

    "people/michael-nolan.html":
        "An Irish-born co-worker of Charles &mdash; the only pension witness whose testimony explicitly states that he \"worked with\" Charles. His affidavit confirms the consciousness-loss incident at New Madrid.",

    "people/john-hebbeler.html":
        "One of the two witnesses who co-signed Charles's 1891 Declaration for Invalid Pension &mdash; the formal claim instrument that opened the pension case.",

    "people/john-heitzenberger.html":
        "One of the witnesses on Charles's 1890 pension declaration. The name as written by the clerk reads <em>Heitzenberger</em>; subsequent research has identified him as a member of the Pennsylvania-Maryland-German Hitzelberger family.",

    "people/john-thurbecker.html":
        "Another co-witness on Charles's 1891 Declaration for Invalid Pension &mdash; likely a Westphalian/Lower-Saxon St. Louis neighbour.",

    "people/dr-charles-hess.html":
        "The only treating physician Charles ever named &mdash; cited by Charles himself in a handwritten letter to the Commissioner of Pensions in 1898.",

    # ---------- Sponsors at the seven baptisms ----------
    "people/erwin-spraul.html":
        "The sole named sponsor at the 1875 baptism of Charles's son Erwin Carl &mdash; the keystone <em>Konsen</em>-spelling record. A Baden-born Superintendent at the Anheuser-Busch brewery in St. Louis.",

    "people/frederick-pillmann.html":
        "A St. Louis butcher and the only person to sponsor TWO of Charles and Auguste's seven baptisms (the firstborn in 1866, and Katherine Carolina in 1870).",

    "people/jacob-reck.html":
        "A Bavarian-born St. Louis acquaintance who, with his first wife Josephine, sponsored the 1868 baptism of Charles and Auguste's second child.",

    "people/josephine-von-delian.html":
        "First wife of Jacob Reck and a co-sponsor at the 1868 baptism of Charles and Auguste's second child. Of the twelve named sponsors across all seven Gannsen baptisms, she is the one whose individual identity is still being researched.",

    "people/maria-agnes-goetz.html":
        "A sponsor at the 1868 baptism of Charles and Auguste's second child. The May-2026 research pass identifies her most plausibly as Anna Maria Agnes (Götz), wife of Andreas Goetz.",

    "people/wilhelmina-ebeling.html":
        "A sponsor at the 1866 baptism of Charles and Auguste's firstborn &mdash; a senior Soulard / Lafayette-area German Lutheran neighbour during the family's South 7th Street years.",
}


def insert_intro(page_rel: str, intro_text: str) -> tuple[bool, str]:
    """Insert the intro paragraph before the existing bottom-line. Returns (changed, reason)."""
    path = ROOT / page_rel
    if not path.exists():
        return False, f"file not found: {page_rel}"
    html = path.read_text(encoding="utf-8")

    # Idempotency: skip if a family-intro is already present.
    if 'class="family-intro"' in html:
        return False, "already has family-intro"

    # Find the first <p class="bottom-line"...> in the file (inside a summary-card).
    m = re.search(r'(<p class="bottom-line"[^>]*>)', html)
    if not m:
        return False, "no bottom-line paragraph found"

    intro_html = (
        '<p class="family-intro" style="font-size:1.05rem; line-height:1.6; '
        'margin:0 0 1rem; padding:0.7rem 0.95rem; background:var(--bg-card-tint, #fdf5d8); '
        'border-left:3px solid var(--brand, #d8b366); border-radius:3px; color:var(--text-body, #2c2620);">'
        + intro_text +
        "</p>\n  "
    )

    new_html = html[: m.start()] + intro_html + html[m.start():]
    path.write_text(new_html, encoding="utf-8")
    return True, "inserted"


def main():
    changed = 0
    skipped = 0
    missing = 0
    for page_rel, intro in INTROS.items():
        ok, reason = insert_intro(page_rel, intro)
        status = "OK" if ok else ("SKIP" if "already" in reason else "MISS")
        print(f"  [{status}] {page_rel:42s} {reason}")
        if ok:
            changed += 1
        elif "already" in reason:
            skipped += 1
        else:
            missing += 1
    print()
    print(f"Total: {len(INTROS)} pages")
    print(f"  Changed: {changed}")
    print(f"  Skipped (already had intro): {skipped}")
    print(f"  Missing: {missing}")


if __name__ == "__main__":
    main()
