#!/usr/bin/env python3
"""
Generate at-a-glance SVG family trees for the family sections of
germany/konze-family-by-town.html, presented as standard genealogical
drop-line (descendant) charts:

  * strict generation ranks, labelled I / II / III in the left margin
  * spouses joined by the conventional "=" with the marriage date at
    the union point
  * children in birth order, numbered i, ii, iii (Register style);
    children who do not carry the line forward are presented as a
    stacked list to keep charts compact
  * person boxes follow Kontze_Family_Tree_Graphic.html (blue male /
    rose female / grey unresolved / dashed gold contested)

One tree per family sub-section. SVGs render at native size.
Data is declared in TREES below (curated from the page's own tables).
Idempotent: strips every <!-- BEGIN-TOWN-TREE:... --> block and
re-inserts. Usage:  python3 scripts/build-bytown-trees.py
"""
from __future__ import annotations
import html as H
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "germany" / "konze-family-by-town.html"

# ---------------- geometry constants ----------------
BOXW = 268          # person box width
HGAP = 18           # horizontal gap between sibling columns
CGAP = 38           # gap between the two spouse boxes (holds the "=")
RANKGAP = 64        # vertical gap between generation ranks
STACKGAP = 12       # vertical gap inside a stacked sibling list
CLUSTER_GAP = 48    # vertical gap between clusters
PAD = 16            # outer padding
GENW = 38           # left margin reserved for generation labels
LABEL_H = 28        # cluster section-label height

ROMAN_GEN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
ROMAN_CHILD = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii",
               "ix", "x", "xi", "xii", "xiii", "xiv"]


def P(name, dates="", detail="", sex="u", cand=False):
    return {"t": "p", "name": name, "dates": dates, "detail": detail,
            "sex": sex, "cand": cand}


def U(a, b=None, m="", children=None, maxrow=None):
    # maxrow is accepted for backward compatibility but unused in the
    # ranked drop-chart layout.
    return {"t": "u", "a": a, "b": b, "m": m, "children": children or []}


# ---------------- helpers ----------------

def box_h(p):
    lines = 1 + (1 if p["dates"] else 0) + (1 if p["detail"] else 0)
    return {1: 44, 2: 64, 3: 82}[lines]


def esc(s):
    return H.escape(s, quote=False)


def numberable(p):
    n = p["name"][:1]
    return n.isalpha() and n.isupper()


# ---------------- ranked layout (build cells) ----------------

def build_cell(node, rank):
    """Return a layout cell. Cells:
       {'t':'p',...} single box · {'t':'stack',...} stacked sibling list
       {'t':'u',...} union with couple + child columns."""
    if node["t"] == "p":
        return {"t": "p", "p": node, "w": BOXW, "h": box_h(node),
                "rank": rank, "num": None}
    u = node
    a_h = box_h(u["a"])
    if u["b"]:
        couple_w = BOXW * 2 + CGAP
        couple_h = max(a_h, box_h(u["b"]))
    else:
        couple_w, couple_h = BOXW, a_h
    cols, stack_items, stack_pos = [], [], None
    n = 0
    for c in u["children"]:
        pers = c if c["t"] == "p" else c["a"]
        num = None
        if numberable(pers):
            num = ROMAN_CHILD[min(n, len(ROMAN_CHILD) - 1)]
            n += 1
        if c["t"] == "p":
            if stack_pos is None:
                stack_pos = len(cols)
                cols.append(None)           # placeholder for the stack
            stack_items.append((c, num))
        else:
            cell = build_cell(c, rank + 1)
            cell["num"] = num
            cols.append(cell)
    if stack_items:
        h = sum(box_h(c) for c, _ in stack_items) + STACKGAP * (len(stack_items) - 1)
        cols[stack_pos] = {"t": "stack", "items": stack_items, "w": BOXW,
                           "h": h, "rank": rank + 1}
    cols = [c for c in cols if c]
    kids_w = sum(c["w"] for c in cols) + HGAP * (len(cols) - 1) if cols else 0
    return {"t": "u", "u": u, "w": max(couple_w, kids_w),
            "couple_w": couple_w, "couple_h": couple_h,
            "cols": cols, "rank": rank, "num": None}


def collect_rank_h(cell, rank_h):
    r = cell["rank"]
    own = cell["couple_h"] if cell["t"] == "u" else cell["h"]
    rank_h[r] = max(rank_h.get(r, 0), own)
    if cell["t"] == "u":
        for c in cell["cols"]:
            collect_rank_h(c, rank_h)


# ---------------- rendering ----------------

def render_person(p, x, y, out, num=None):
    h = box_h(p)
    cls = {"m": "male", "f": "female", "u": "unknown"}[p["sex"]]
    if p["cand"]:
        cls = "candidate"
    name = (f"{num} · " if num else "") + p["name"]
    out.append(f'<g class="person-box {cls}" transform="translate({x:.0f}, {y:.0f})">')
    out.append(f'  <rect width="{BOXW}" height="{h}"/>')
    name_fs = ""
    if len(name) > 30:
        name_fs = ' font-size="13.5"'
    if len(name) > 37:
        name_fs = ' font-size="12"'
    ty = 26
    out.append(f'  <text x="{BOXW//2}" y="{ty}" text-anchor="middle" class="person-name"{name_fs}>{esc(name)}</text>')
    if p["dates"]:
        dates_fs = ' font-size="11"' if len(p["dates"]) > 38 else ""
        out.append(f'  <text x="{BOXW//2}" y="{ty+19}" text-anchor="middle" class="person-dates"{dates_fs}>{esc(p["dates"])}</text>')
    if p["detail"]:
        dy = ty + (36 if p["dates"] else 19)
        detail_fs = ' font-size="10.5"' if len(p["detail"]) > 40 else ""
        out.append(f'  <text x="{BOXW//2}" y="{dy}" text-anchor="middle" class="person-detail"{detail_fs}>{esc(p["detail"])}</text>')
    out.append('</g>')


def render_cell(cell, x, rank_y, out):
    y = rank_y[cell["rank"]]
    if cell["t"] == "p":
        render_person(cell["p"], x, y, out, cell.get("num"))
        return
    if cell["t"] == "stack":
        yy = y
        prev_bottom = None
        for p, num in cell["items"]:
            if prev_bottom is not None:
                out.append(f'<line x1="{x+BOXW/2:.0f}" y1="{prev_bottom:.0f}" '
                           f'x2="{x+BOXW/2:.0f}" y2="{yy:.0f}" class="descent-line"/>')
            render_person(p, x, yy, out, num)
            prev_bottom = yy + box_h(p)
            yy = prev_bottom + STACKGAP
        return
    # ---- union ----
    u = cell["u"]
    couple_left = x + (cell["w"] - cell["couple_w"]) / 2
    a_h = box_h(u["a"])
    render_person(u["a"], couple_left, y, out, cell.get("num"))
    if u["b"]:
        bx = couple_left + BOXW + CGAP
        render_person(u["b"], bx, y, out)
        ly = y + min(a_h, box_h(u["b"])) / 2
        gap_mid = couple_left + BOXW + CGAP / 2
        # conventional "=" union symbol between the spouses
        out.append(f'<text x="{gap_mid:.0f}" y="{ly+4:.0f}" text-anchor="middle" class="marriage-eq">=</text>')
        spine_x = gap_mid
    else:
        spine_x = couple_left + BOXW / 2
    couple_bottom = y + cell["couple_h"]
    if u["m"]:
        # offset to the right of the descent spine so the line never runs
        # through the date text
        out.append(f'<text x="{spine_x+7:.0f}" y="{couple_bottom+16:.0f}" class="marriage-label">{esc(u["m"])}</text>')
    if not cell["cols"]:
        return
    next_y = rank_y[cell["rank"] + 1]
    bus_y = next_y - 14
    kids_w = sum(c["w"] for c in cell["cols"]) + HGAP * (len(cell["cols"]) - 1)
    kx = x + (cell["w"] - kids_w) / 2
    drops = []
    cx = kx
    for c in cell["cols"]:
        if c["t"] == "u":
            cl = cx + (c["w"] - c["couple_w"]) / 2
            drops.append(cl + BOXW / 2)        # drop onto the child, not the spouse
        else:
            drops.append(cx + BOXW / 2)
        cx += c["w"] + HGAP
    lo = min(drops + [spine_x])
    hi = max(drops + [spine_x])
    out.append(f'<line x1="{spine_x:.0f}" y1="{couple_bottom:.0f}" x2="{spine_x:.0f}" y2="{bus_y:.0f}" class="descent-line"/>')
    out.append(f'<line x1="{lo:.0f}" y1="{bus_y:.0f}" x2="{hi:.0f}" y2="{bus_y:.0f}" class="descent-line"/>')
    cx = kx
    for c, d in zip(cell["cols"], drops):
        out.append(f'<line x1="{d:.0f}" y1="{bus_y:.0f}" x2="{d:.0f}" y2="{next_y:.0f}" class="descent-line"/>')
        render_cell(c, cx, rank_y, out)
        cx += c["w"] + HGAP
    return


# ---------------- tree assembly ----------------

def build_svg(tree):
    """tree["clusters"] = [(label or "", [nodes...]), ...]"""
    measured = []
    total_w = 0
    total_h = PAD
    for label, nodes in tree["clusters"]:
        cells = [build_cell(n, 0) for n in nodes]
        rank_h = {}
        for c in cells:
            collect_rank_h(c, rank_h)
        ranks = sorted(rank_h)
        ch = sum(rank_h[r] for r in ranks) + RANKGAP * (len(ranks) - 1)
        cw = sum(c["w"] for c in cells) + HGAP * 2 * (len(cells) - 1)
        total_w = max(total_w, cw)
        total_h += (LABEL_H if label else 6) + ch + CLUSTER_GAP
        measured.append((label, cells, rank_h, cw, ch))
    total_h -= CLUSTER_GAP - 8
    total_w += PAD * 2 + GENW
    out = []
    out.append(f'<svg viewBox="0 0 {total_w:.0f} {total_h:.0f}" '
               f'width="{total_w:.0f}" height="{total_h:.0f}" role="img" '
               f'aria-label="{esc(tree["aria"])}" '
               f'style="display:block; margin:0 auto;" '
               f'xmlns="http://www.w3.org/2000/svg">')
    y = PAD
    for label, cells, rank_h, cw, ch in measured:
        if label:
            out.append(f'<text x="{PAD}" y="{y+14}" class="section-label">{esc(label)}</text>')
            y += LABEL_H
        else:
            y += 6
        ranks = sorted(rank_h)
        rank_y = {}
        ry = y
        for r in ranks:
            rank_y[r] = ry
            ry += rank_h[r] + RANKGAP
        # generation labels in the left margin (only for true multi-rank trees)
        if len(ranks) > 1:
            for r in ranks:
                out.append(f'<text x="{PAD}" y="{rank_y[r]+18:.0f}" class="gen-label">{ROMAN_GEN[min(r, len(ROMAN_GEN)-1)]}</text>')
        x = PAD + GENW + (total_w - 2 * PAD - GENW - cw) / 2
        for c in cells:
            render_cell(c, x, rank_y, out)
            x += c["w"] + HGAP * 2
        y += ch + CLUSTER_GAP
    out.append('</svg>')
    return "\n".join(out)


TREE_CSS = """
<!-- BEGIN-TOWN-TREE-CSS -->
<style>
  /* At-a-glance tree styling — mirrors Kontze_Family_Tree_Graphic.html.
     SVGs render at native size; wide trees scroll horizontally. */
  .town-tree { overflow-x: auto; padding: 10px 6px 4px; margin: 0.6rem 0 1.5rem;
               background: var(--bg-card, #fffaf0); border: 1px solid var(--border-light, #d8c8a8);
               border-radius: 5px;
               /* Break out of the 1100px article column: the figure hugs the
                  SVG's natural width, centred on the column, capped at the
                  viewport. Wider-than-viewport trees scroll horizontally. */
               width: fit-content; max-width: calc(100vw - 3rem);
               margin-left: 50%; transform: translateX(-50%); }
  .town-tree-caption { font-size: 0.8rem; color: var(--text-meta, #6a5a42); font-style: italic;
                       padding: 0.35rem 0.8rem 0.5rem; margin: 0; }
  .town-tree-legend { display: flex; flex-wrap: wrap; gap: 0.3rem 1.4rem; align-items: center;
                      font-size: 0.82rem; color: var(--text-meta, #6a5a42);
                      padding: 0.25rem 0.8rem 0.6rem; border-bottom: 1px dashed var(--border-light, #d8c8a8);
                      margin-bottom: 0.4rem; }
  .town-tree-legend .leg { display: inline-block; width: 14px; height: 14px; border-radius: 3px;
                           margin-right: 0.4rem; vertical-align: -2px; }
  .town-tree-legend .leg.male { background: #e8f0fe; border: 1.5px solid #4a76c8; }
  .town-tree-legend .leg.female { background: #fde8ef; border: 1.5px solid #c84a76; }
  .town-tree-legend .leg.unknown { background: #f0eee8; border: 1.5px solid #8a8070; }
  .town-tree-legend .leg.candidate { background: #fff3cd; border: 2px dashed #d8b366; }
  :root.theme-dark .town-tree-legend .leg.male { background: #1c2638; border-color: #6a8ad8; }
  :root.theme-dark .town-tree-legend .leg.female { background: #36202a; border-color: #d86a8a; }
  :root.theme-dark .town-tree-legend .leg.unknown { background: #2a261e; border-color: #8a7a4a; }
  :root.theme-dark .town-tree-legend .leg.candidate { background: #2c2516; border-color: #d8b366; }
  .town-tree .person-box rect { rx: 6; ry: 6; stroke-width: 1.5; }
  .town-tree .male rect { fill: #e8f0fe; stroke: #4a76c8; }
  .town-tree .female rect { fill: #fde8ef; stroke: #c84a76; }
  .town-tree .unknown rect { fill: #f0eee8; stroke: #8a8070; }
  .town-tree .candidate rect { fill: #fff3cd; stroke: #d8b366; stroke-width: 2.5; stroke-dasharray: 6,3; }
  .town-tree .person-name { font-weight: bold; font-size: 15px; fill: #2c2c2c; }
  .town-tree .person-dates { font-size: 12.5px; fill: #666; }
  .town-tree .person-detail { font-size: 12px; fill: #888; font-style: italic; }
  .town-tree .marriage-line { stroke: #666; stroke-width: 1.5; }
  .town-tree .descent-line { stroke: #999; stroke-width: 1; fill: none; }
  .town-tree .marriage-label { font-size: 11.5px; fill: #888; }
  .town-tree .marriage-eq { font-weight: bold; font-size: 19px; fill: #555; }
  .town-tree .gen-label { font-size: 15px; fill: #b0a583; font-style: italic; font-weight: bold; }
  .town-tree .section-label { font-size: 17px; fill: #555; font-weight: bold; }
  :root.theme-dark .town-tree .male rect { fill: #1c2638; stroke: #6a8ad8; }
  :root.theme-dark .town-tree .female rect { fill: #36202a; stroke: #d86a8a; }
  :root.theme-dark .town-tree .unknown rect { fill: #2a261e; stroke: #8a7a4a; }
  :root.theme-dark .town-tree .candidate rect { fill: #2c2516; stroke: #d8b366; }
  :root.theme-dark .town-tree .person-name { fill: #f4e2b0; }
  :root.theme-dark .town-tree .person-dates { fill: #c8b896; }
  :root.theme-dark .town-tree .person-detail { fill: #a89a76; }
  :root.theme-dark .town-tree .section-label { fill: #c8b896; }
  :root.theme-dark .town-tree .marriage-label { fill: #a89a76; }
  :root.theme-dark .town-tree .marriage-eq { fill: #c8b896; }
  :root.theme-dark .town-tree .gen-label { fill: #8a7a4a; }
  :root.theme-dark .town-tree .marriage-line { stroke: #a89a76; }
  :root.theme-dark .town-tree .descent-line { stroke: #6a5e3e; }
</style>
<!-- END-TOWN-TREE-CSS -->
"""

LEGEND_HTML = ('<div class="town-tree-legend" role="note" aria-label="Tree key">'
               '<span><span class="leg male"></span>male</span>'
               '<span><span class="leg female"></span>female</span>'
               '<span><span class="leg unknown"></span>sex / identity unresolved</span>'
               '<span><span class="leg candidate"></span>contested or unconfirmed</span>'
               '<span><strong>=</strong>&nbsp; marriage</span>'
               '<span><strong>I&nbsp;II&nbsp;III</strong>&nbsp; generations</span>'
               '<span><strong>i&nbsp;·&nbsp;ii&nbsp;·&nbsp;iii</strong>&nbsp; children in birth order</span>'
               '<span><strong>geb.</strong>&nbsp; née / maiden name</span>'
               '<span><strong>×1&nbsp;×2</strong>&nbsp; first / second marriage</span>'
               '<span style="font-style:italic;">surnames appear as the scribe wrote them — Konde / Konten are pre-1770 spellings of Kontze</span>'
               '<span style="font-style:italic;">person-by-person rows with sources follow each chart</span>'
               '</div>')

# ====================================================================
#  DATA — one tree per family sub-section (June 2026 state)
#  h2: the town section id;  h3: a distinctive substring of the
#  sub-section heading (plain text, entities resolved); h3=None puts
#  the tree right after the town intro paragraph.
# ====================================================================

TREES = [

# ===================== TRENDELBURG =====================
{
    "key": "tr-earliest", "h2": "trendelburg", "h3": "earliest generation",
    "aria": "Family tree of the earliest Trendelburg Kontze generation, 1708–1772",
    "legend": True,
    "clusters": [
        ("", [
            U(P("Andreas Kontze sen.", "fl. 1708 — d. 1742×46", "council alderman (Ratsschöffe)", "m"),
              P("Margretha geb. Pfankuchen", "b. ~1683 — d. 1746", "", "f"),
              children=[
                  P("Arnold Philipp", "bap. 4 Mar 1708", "→ his line below", "m"),
                  P("Anna Catherina", "bap. 8 Dec 1712", "", "f"),
                  P("Mathias", "bap. 1714 — d. 1742", "", "m"),
              ]),
            U(P("Andreas Kontze jun.", "b. ~1672 — d. 1761", "church elder (Kirchen-Senior)", "m"),
              P("Anna Catharina geb. Klieben", "d. 1758, ~58", "", "f"),
              children=[
                  P("Anna Catherina", "bap. 13 Sep 1713", "", "f"),
                  P("Johann Melcher", "bap. 9 Oct 1715", "", "m"),
              ]),
        ]),
        ("Nies Kontze Sr.'s household — prob. source of the Stammtafel (pedigree) branch", [
            U(P("Nies (Dionysius) Kontze Sr.", "b. ~1681 — d. 1746", "burgher & farmer", "m"),
              P("Cath. Elis. geb. Uffelmann", "b. ~1692 — d. 1759", "", "f"),
              m="m. ~1712",
              children=[
                  P("Joh. Daniel", "bap. 3 Aug 1714", "", "m"),
                  P("Anna Catharina", "m. 1752 Henßen", "", "f"),
                  P("Anna Christina", "m. 1761 Wagner", "", "f"),
                  P("prob. Andreas", "m. 1760", "→ Stammtafel (pedigree) branch", "m", cand=True),
                  P("prob. Dionysius jr.", "b. ~1738 — d. 1763", "never married", "m"),
              ]),
        ]),
        ("", [
            U(P("Joan Henric Konde [= Kontze]", "b. ~1705 — d. 1762", "church elder & master baker", "m"),
              P("×1 Dorothea Elis. Bornemann", "d. 1741 · ×2 a widow", "", "f"),
              children=[
                  P("Maria Elisabeth", "m. 1754 Pfankuche", "", "f"),
                  P("2 infant daughters", "d. 1742 · d. 1745", "", "f"),
                  P("+ son, daughters", "of ×1 and ×2", "", "u"),
              ]),
            U(P("Dionysius Konde [= Kontze]", "b. ~1699 — d. 1742", "“vor dem Thor” (outside the town gate)", "m"),
              None,
              children=[P("one daughter", "survived him", "", "f")]),
        ]),
        ("Early Kontze women (marriages out)", [
            P("Anna Margretha Wiechard", "b. ~1702 — d. 1777", "geb. Kontze · × H. Wiechard", "f"),
            P("Margretha Elis. Konten [= Kontze]", "m. 1749", "× Conrad Austermühlen", "f"),
            P("Maria Christina Kersting", "b. ~1726 — d. 1806", "geb. Konze · m. 1748 Kersting", "f"),
        ]),
    ],
},
{
    "key": "tr-arnold", "h2": "trendelburg", "h3": "Arnold Philipp Kontze",
    "aria": "Family tree of Arnold Philipp Kontze's town-councillor (Rathsverwandter) line",
    "clusters": [
        ("", [
            U(P("Arnold Philipp Kontze", "bap. 1708 — d. 1780", "town councillor & farmer", "m"),
              P("×1 A. Elis. Uffelmann (d. 1754)", "×2 A. Dorothea Uffelmann", "she ~1733–1785", "f"),
              children=[
                  P("Andreas", "b. 1743 — d. 1745", "died in infancy", "m"),
                  U(P("Johann Henrich Kontze", "b. ~1740 — d. 1804", "eldest son", "m"),
                    P("×1 M. E. Wiechard (1773)", "×2 A. C. Osthermann (1783)", "she 1748–1818", "f"),
                    children=[
                        P("Anna Margaretha", "b. 1774 · m. 1797 Nickel", "", "f"),
                        P("Anna Christina", "b. 1777 · m. 1805 Koch", "2 Koch children", "f"),
                        P("Anna Margretha", "b. ~1778 — d. 1784", "died in childhood", "f"),
                        P("Maria Elisabetha", "b. 28 Apr 1779", "", "f"),
                        P("Anna Catharina", "b. 13 Feb 1782", "", "f"),
                        U(P("Andreas Kontze", "bap. 1787 — d. 1830", "of ×2 · PZXN-SFV", "m"),
                          P("×1 Wilh. Grosbernd (1807)", "×2 A. Christina Heidt (1818)", "", "f"),
                          children=[
                              P("Joh. Christoph", "b. 1808 — d. 1880", "", "m"),
                              P("Joh. Friedrich", "b. 1810 — d. ?", "margin cross", "m"),
                              P("Johannes", "b. 1814 — d. 1894", "", "m"),
                          ]),
                    ]),
                  U(P("Johannes Kontze", "d. after 1818", "2nd son · burgher & farmer", "m"),
                    P("×1 A. M. Thielin of Deisel (1780)", "×2 M. E. Grosbernd (1806)", "she ~1751–1804", "f"),
                    children=[
                        P("Wilhelmina", "b. 1782 — d. 1783", "died in infancy", "f"),
                        P("Anna Catharina", "b. 1783 · m. 1808 Doenges", "3 Doenges children", "f"),
                        P("Johann Henrich", "b. 1786 — d. 1818", "unmarried", "m"),
                        P("Joh. Conrad", "b. 1788 — d. 1789", "died in infancy", "m"),
                        P("Maria Christina", "b./d. 1790", "died in infancy", "f"),
                        P("Johann Philip", "b. 1792 — d. 1798", "died in childhood", "m"),
                        P("Johannes jr.", "b. 1794", "FS: m. 1832 Henze", "m"),
                        P("Carl Wilhelm", "b. 1808 — d. 1817", "of ×2 · died in childhood", "m"),
                        P("Carl Ludwig", "b. 1811", "of ×2", "m"),
                    ], maxrow=5),
              ], maxrow=2),
        ]),
    ],
},
{
    "key": "tr-elder-jh", "h2": "trendelburg", "h3": "elder Johann Henrich",
    "aria": "Family tree of the elder Johann Henrich Kontze households",
    "clusters": [
        ("", [
            U(P("“Elder” Joh. Henrich Kontze", "d. before Feb 1774", "town councillor (title flagged)", "m"),
              None,
              children=[
                  P("Anna Margretha", "m. 1774 H. David Lotz", "3 Lotz children", "f"),
              ]),
            U(P("Johann Henrich Kontze", "b. ≤~1722 — d. bef. 1787", "brandy distiller (Branntweinbrenner)", "m"),
              P("Anna Margretha geb. Uffelmann", "b. ~1722 — d. 1787", "", "f"),
              children=[
                  P("Martha Elisabeth", "b. ~1779 — d. 1783", "died in childhood", "f"),
              ]),
        ]),
    ],
},
{
    "key": "tr-stammtafel", "h2": "trendelburg", "h3": "Stammtafel",
    "aria": "Family tree of the town-councillor (Rathsverwandter) Andreas Kontze line, the Stammtafel branch",
    "clusters": [
        ("", [
            U(P("Andreas Contze", "b. ~1723 — d. 1800", "town councillor · the Elder of Stammen", "m"),
              P("Anna Christina geb. Contzen", "b. ~1735 — d. 1807", "a Konze–Konze intermarriage", "f"),
              m="m. 13 Jun 1760",
              children=[
                  P("Maria Elisabeth", "m. 1794 Albrecht", "", "f"),
                  U(P("Johann Friedrich Kontze", "b. 1763 — d. 1823", "99Z3-6H9 · ⚠ paternity contested", "m"),
                    P("Dorothea Elis. geb. Jorden", "b. 1766 — d. 1823", "Mayor Jorden's daughter", "f"),
                    m="m. 15 Feb 1795",
                    children=[
                        U(P("Andreas Konze", "b. 1795 — d. 1854 Mainz", "PZF8-X19 · → Friedrichsfeld", "m"),
                          P("×1 Wilh. Hofeditz (1821)", "×2 M. Sophia Hofeditz", "she d. Oct 1835", "f"),
                          children=[
                              P("Elisa Melusine", "b. 1822 — d. 1865 Stammen", "never married", "f"),
                              P("3 infants", "1824 · 1825 · 1824/25", "died in infancy", "u"),
                              P("Maria Carolina", "b. 1828", "", "f"),
                              P("Justus Ernst", "b. 1829", "untraced after 1843", "m"),
                              P("Heinrich Wilhelm", "b. 1832 — d. 1858 Stammen", "PZFD-1X4", "m"),
                              P("Maria Sabine", "b. 1834", "P878-ZSG", "f"),
                              P("August", "b./d. Oct 1834", "died at two days", "m"),
                          ], maxrow=4),
                        P("Anna Christina", "b. 1800 — d. 1852 Sielen", "m. C. W. Hofeditz", "f"),
                        U(P("Carl Ludwig Kontze", "b. 1804 — d. 1862", "farmer-burgher, Haus Nr. 34", "m"),
                          P("Marie Wilhelmine Albrecht", "", "", "f"),
                          children=[
                              P("Maria Caroline", "b. 1826", "FS: m. 1846 Grossberndt", "f"),
                              P("Caroline Jeanette", "b. 1829 — d. 1889", "m. Ludwig Kohlus", "f"),
                              U(P("Carl Wilhelm Konze", "b. 1831 — d. 1869", "99Z3-DFK", "m"),
                                P("Marie Lauterbach", "of Deisel", "", "f"),
                                children=[
                                    P("Joh. Friedrich Wilhelm", "b. ~23 Jun 1861", "Nottaufe — emergency baptism", "m"),
                                ]),
                              P("Chr. Wilh. Philippine", "b. 1834", "", "f"),
                          ], maxrow=4),
                    ], maxrow=2),
              ]),
        ]),
    ],
},
{
    "key": "tr-beckermeister", "h2": "trendelburg", "h3": "Beckermeister",
    "aria": "Family tree of Johann Philipp Kontze the Beckermeister's household",
    "clusters": [
        ("", [
            U(P("Johann Philipp Kontze", "d. after 1818 (?)", "burgher & master baker", "m"),
              None,
              children=[
                  P("Anna Catharina", "b. 10 Aug 1774", "", "f"),
                  P("Maria Christina", "b. 1778 †", "", "f"),
                  P("Maria Christina", "b. ~1781 — d. 1784", "died in childhood", "f"),
                  P("Anna Margretha", "m. 1796 Joh. Albrecht", "7 Albrecht children", "f"),
                  P("prob. Anna Margaretha", "~1749 — d. 1800", "× Henning Albrecht bef. 1776", "f", cand=True),
              ]),
        ]),
    ],
},
{
    "key": "tr-grenadier", "h2": "trendelburg", "h3": "dismissed Grenadier",
    "aria": "Family tree of Johann Christoph Contze the dismissed Grenadier's household",
    "clusters": [
        ("", [
            U(P("Johann Christoph Contze", "b. ~1747 — d. ?", "grenadier → day labourer · cf. Deisel", "m"),
              P("Anna Catharina geb. Pfeil", "von Homberg", "", "f"),
              children=[
                  U(P("Maria Elisabeth Konze", "bap. 1799 — d. 1834", "unmarried mother", "f"),
                    None,
                    children=[
                        P("Johann George", "b. 22 May 1825", "illegitimate", "m"),
                    ]),
                  P("Maria Wilhelmina", "b. 1801", "", "f"),
                  P("Johannes", "b. 1804", "margin cross", "m"),
                  P("Johannes (the earlier)", "b. ~1804 — d. 1808", "died in childhood", "m"),
                  P("Anton Wilhelm", "b. 1806", "", "m"),
                  P("M. Carolina Joannette", "b. 1809", "", "f"),
                  P("Anna Margaretha", "b. 1811", "", "f"),
              ], maxrow=4),
        ]),
    ],
},
{
    "key": "tr-variants", "h2": "trendelburg", "h3": "Contze / Contzen variant",
    "aria": "Chart of the Contze / Contzen variant households and women",
    "clusters": [
        ("", [
            U(P("Anna Cath. Jordan geb. Contzin", "b. ~1743 — d. 1797", "× Mayor Joh. Philipp Jordan", "f"),
              None,
              children=[P("the Jordan children", "not itemized", "", "u")]),
            U(P("Anna Christina geb. Contzen", "", "× Daniel v. Biesenroth", "f"),
              None,
              children=[P("Fridelice / Friederike", "b. ~Jan 1806–07", "", "f")]),
            U(P("Anna Catharina geb. Conze", "d. before Oct 1830", "× Joh. George Lennig (1st wife)", "f"),
              None,
              children=[P("Christine Wilhelmine", "d. 1830, aged 21", "", "f")]),
            U(P("Anna Catharina Contzin", "unmarried, 1810", "", "f"),
              None,
              children=[P("Maria Carolina", "b. 20 Jan 1810", "illegit. · margin cross", "f")]),
        ]),
    ],
},
{
    "key": "tr-other19c", "h2": "trendelburg", "h3": "Other 19th-century",
    "aria": "Chart of the other 19th-century Trendelburg Konze households",
    "clusters": [
        ("", [
            U(P("Joh. Christoph Konze", "fl. 1854", "slate-roofer (Schieferdecker)", "m"),
              P("Marie Elisabeth Heine", "", "", "f"),
              children=[P("Karl Heinrich", "b. 19 Nov 1854", "", "m")]),
            U(P("Marie Elis. Enders geb. Kontze", "", "× J. H. W. Enders, day labourer", "f"),
              None,
              children=[P("2 Enders children", "1832 · 1834 (stillborn)", "", "u")]),
        ]),
        ("", [
            P("“Karl Wilhelm Konze,” lodger", "", "distinct from Carl Wilhelm b. 1831", "m"),
            P("Wilhelm Kontze(?)", "journeyman shoemaker, Cassel", "brother of Marie Elis. Enders", "m"),
        ]),
    ],
},

# ===================== JUNGKONZE =====================
{
    "key": "jk-stammen-roots", "h2": "jungkonze", "h3": "Stammen roots",
    "aria": "Family tree of the Jungkonze Stammen roots, the beadle (Amtsdiener) Joan Georg's household",
    "clusters": [
        ("", [
            U(P("Christoph Jungkonze", "d. before Nov 1755", "of Stammen · MHTZ-L81", "m"),
              None,
              children=[
                  U(P("Joan Georg Jungkonze", "b. ~1733 — d. 1797", "beadle (Amtsdiener) · MG26-FLC", "m"),
                    P("×1 A. M. E. Schnell (1755)", "×2 A. E. Kohlstätten (1762)", "she ~1727–1806", "f"),
                    children=[
                        P("Anna Gerdruth", "m. 1801 J. G. Thiele", "2 Thiele children", "f"),
                        P("(FS) Johann Heinrich", "b. 1766 · m. 1811 Paderborn", "MG26-F2F", "m", cand=True),
                    ]),
              ]),
        ]),
    ],
},
{
    "key": "jk-fruchtmesser", "h2": "jungkonze", "h3": "Hussar corporal",
    "aria": "Family tree of Joh. Henrich Jungconze the Fruchtmesser's household",
    "clusters": [
        ("", [
            U(P("Joh. Henrich Jungconze", "b. ~1740/42 — d. 1808", "Hussar corporal → grain-measurer (Fruchtmesser)", "m"),
              P("×1 M. E. Schellhase", "×2 A. C. Steitz (1797)", "", "f"),
              children=[
                  P("Christoph Henrich", "~1769 — d. 1770", "died in infancy", "m"),
                  P("Johann Conrad", "b. 17 Jul 1774", "not yet traced", "m"),
                  P("Johannes", "~1777 — d. 1778", "died in infancy", "m"),
                  P("Anna Elisabeth", "~1775 — d. 1785", "died in childhood", "f"),
                  P("Maria Elisabeth", "b. 1782 — d. 1783", "died in infancy", "f"),
                  P("Joh. George", "b. 1785 — d. 1786", "died in infancy", "m"),
                  P("Maria Elisabeth II", "godparent-age by 1795", "", "f"),
                  P("Catharina Elisab.", "m. 1804 Zollmann · ×2 Heidt", "4 children", "f"),
                  P("poss. Henrich (soldier)", "b. ~1765", "Rgmt v. Bose, mustered 1784", "m", cand=True),
              ], maxrow=5),
        ]),
    ],
},
{
    "key": "jk-schneidermeister", "h2": "jungkonze", "h3": "Schneidermeister",
    "aria": "Family tree of the master-tailor (Schneidermeister) Jungkonze house, Trendelburg Nr. 53",
    "clusters": [
        ("", [
            U(P("Johannes Jungkontz (the elder)", "", "beadle (Amtsdiener)", "m"),
              None,
              children=[
                  U(P("Johannes Jungkonze", "d. after Aug 1834", "burgher & master tailor", "m"),
                    P("Carolina Charlotte Enders", "hatter Enders's daughter", "", "f"),
                    m="m. 29 Apr 1792",
                    children=[
                        P("Carl Ludwig (“Ludwig”)", "b. 1793 — d. ~1862", "tailor · × Meerkamm · below", "m"),
                        P("Johann George", "b. 1794", "artillery NCO (Unteroffizier)", "m"),
                        P("Joh. Henrich", "b. 1798 — d. 1799", "died in infancy", "m"),
                        P("Wilhelmina (twin)", "b. 1801 — d. ~1863", "× Grosberndt · below", "f"),
                        P("Christina Charlotta (twin)", "b./d. 1801", "died in infancy", "f"),
                        P("Maria Elisabeth", "b. 1804", "unmarried mother · below", "f"),
                        P("Maria Caroline", "b. 1807 — d. ~1855", "× Wichard · d. Gottsbüren", "f"),
                    ], maxrow=4),
              ]),
        ]),
        ("Parentage open — the artillerist's line", [
            U(P("Johannes Jungkonze", "d. before Apr 1836 (?)", "artillerist · NOT a master-tailor son", "m"),
              P("Dorothea Steinbach", "of Cassel", "unmarried union", "f"),
              children=[
                  P("Eduard Jung-Konze", "b. 26 Apr 1822", "illegit. · conf. 1836", "m"),
              ]),
        ]),
    ],
},
{
    "key": "jk-ludwig-children", "h2": "jungkonze", "h3": "Ludwig Jungkonze",
    "aria": "Family tree of Ludwig Jungkonze's children at Trendelburg Nr. 53",
    "clusters": [
        ("", [
            U(P("Carl Ludwig Jungkonze", "b. 1793 — d. ~1862", "tailor · KLVT-72P", "m"),
              P("Marie Meerkamm", "", "", "f"),
              children=[
                  P("Heinrich Christoph", "b. 1827", "FS: m. 1866 Aplerbeck → Dortmund", "m"),
                  P("Fr. Wilhelm Eduard", "b. 1829 — d. 1832", "died in childhood", "m"),
                  P("Friedrich Wilhelm", "b. 1833 — d. 1834", "died in infancy", "m"),
                  P("Carl Wilhelm Ludwig", "b. 1835 — d. 1837", "died in childhood", "m"),
              ], maxrow=4),
        ]),
    ],
},
{
    "key": "jk-daughters-children", "h2": "jungkonze", "h3": "Wilhelmine&rsquo;s children",
    "h3_alt": "Wilhelmine's children",
    "aria": "Family tree of Maria Elisabeth's and Wilhelmine's children",
    "clusters": [
        ("", [
            U(P("Maria Elisabeth Jungkonze", "b. 1804", "unmarried mother", "f"),
              None,
              children=[
                  P("Maria Wilhelmine", "b. 1829 — d. 1831", "died in infancy", "f"),
                  P("Philipp Freier", "b. 1834", "father: J. F. C. Freier", "m"),
              ]),
            U(P("Wilhelmina geb. Jungkonze", "b. 1801 — d. ~1863", "the twin", "f"),
              P("Johannes Grosberndt jun.", "master wheelwright · his 2nd wife", "", "m"),
              children=[
                  P("Philippine Charlotte", "b. 1829 — d. 1887", "m. 1855", "f"),
                  P("Carl", "b. 1830", "Grosberndt line", "m"),
              ]),
        ]),
    ],
},
{
    "key": "jk-stammen-women", "h2": "jungkonze", "h3": "Jungkontze women in Stammen",
    "aria": "Chart of the Jungkontze women attested in Stammen, 1835",
    "clusters": [
        ("", [
            P("Wilhelmine Pappenheim", "geb. Jungkontze · KZPG-7DL", "× J. C. Pappenheim · a Hümme line", "f"),
            P("Anne Elisabeth Schäfer", "geb. Jungkontze", "× C. W. Schäfer, tailor", "f"),
        ]),
    ],
},

# ===================== DEISEL =====================
{
    "key": "de-founding", "h2": "deisel", "h3": "founding generation",
    "aria": "Family tree of the founding Deisel Konze generation, Andreas Kontze I and his sons",
    "clusters": [
        ("", [
            U(P("Andreas Kontze I, the Küster", "b. ~1718 — d. 21 Mar 1791", "sexton (Küster) · House Nr. 1 · G9DK-DLV", "m"),
              P("×1 Elisabetha Temme ×2 M. Guthmann", "m. 1739 (she d. 1772) · m. 1773", "register-verified · “Brandt” withdrawn", "f"),
              children=[
                  P("Johann Friedrich", "b. 1763 — d. 1823", "⚠ paternity contested → Trendelburg", "m", cand=True),
                  P("Johann Christoph", "b. ~1747", "Grenadier · prob. = Trendelburg man", "m"),
                  U(P("Johann Henrich Kontze", "b. ~1747 — d. 1792", "farmer · G8HG-P2S", "m"),
                    P("Anna Catharina geb. Köster", "b. ~1753 — d. 1811", "", "f"),
                    children=[P("no children recorded", "cf. the Joh. Henrich line", "", "u")]),
                  U(P("Konrad Konze", "b. 1780 — d. 22 Dec 1841", "farmer (Ackermann)", "m"),
                    P("Anna Catharina Köster", "b. 1774 — d. 25 Dec 1841", "widow of Philipp Köster", "f"),
                    children=[P("no children recorded", "", "", "u")]),
              ], maxrow=4),
        ]),
        ("Elder households", [
            U(P("Joh. Christoph Konze sen.", "b. 1740 — d. 1817", "church elder · L1PR-HTM", "m"),
              P("Catharina Elisabeth Köster", "b. 1768 — d. 1821", "", "f"),
              children=[
                  P("Maria Elisabeth", "b. 1805 (the second)", "+ likely others of 29 baptisms", "f"),
              ]),
            U(P("Christian Konze", "b. ~1756 — d. 1829", "GP7M-NBH · FS: a son of the sexton", "m"),
              P("Anna Dorothea geb. Brönner", "b. ~1766 — d. 1821", "", "f"),
              children=[
                  P("a stillborn son", "25 May 1801", "poss. others", "u"),
              ]),
        ]),
        ("", [
            U(P("Joh. Christoph Konze jun.", "b. 1774 — d. 1814", "resident & farmer", "m"),
              None,
              children=[
                  P("prob. 3 child burials", "1809 · 1811 · 1815", "attribution uncertain", "u"),
              ]),
            U(P("Johann Christoph Kontze", "d. before Jan 1796", "an earlier one", "m"),
              None,
              children=[
                  P("Johann Conrad", "b. ~1777 — d. 1796", "died at 18", "m"),
              ]),
            P("Carl Wilhelm Kontze", "b. ~1776 — d. 1796", "son of a deceased Andreas", "m"),
            P("Anna Catharina Konze", "b. ~1760 — d. 1826", "“an old unmarried person”", "f"),
        ]),
    ],
},
{
    "key": "de-klaus-andreas", "h2": "deisel", "h3": "Klaus Andreas",
    "aria": "Family tree of Klaus Andreas Kontze's household and the other Andreas household",
    "clusters": [
        ("House Nr. 29 — Klaus Andreas (alias “Schildknecht”)", [
            U(P("Klaus Andreas Kontze", "b. 1774 — d. 1847", "alias Schildknecht · GH4T-TLC", "m"),
              P("Catharina Elis. geb. Thiele", "b. 1778 — d. 1832", "", "f"),
              m="FS: m. 30 Nov 1798",
              children=[
                  P("Wilhelmine", "b. 1800 — d. 1843", "× Ludwig Köster II", "f"),
                  P("Johann Christoph", "b. 1802 — d. 1845", "× Maria Drönner 1833 → son Ludwig 1836", "m"),
                  P("Maria Elisabeth", "b. Mar 1805", "poss. × Christian Köster III", "f"),
                  P("Charlotte", "b./d. 1811", "died at 3 months", "f"),
                  P("Johannes", "b. 1813 — d. 1835", "shepherd's hand, unmarried", "m"),
              ]),
        ]),
        ("Johann Christoph’s son (218842 E268 — register-verified)", [
            P("Ludwig Konze", "b. 25 Oct 1836 · m. 1864 Frankfurt", "9F7F-Q16 · godfather Ludwig Köster, “Schwager des Vaters”", "m"),
        ]),
        ("Steinweg 136 — the OTHER Andreas", [
            U(P("Andreas Konze", "b. ~1768 — d. 1828", "GD1G-4L7", "m"),
              P("Cath. Elis. geb. Loßin", "b. 1770 — d. 1838", "", "f"),
              m="FS: m. 25 Jan 1793",
              children=[
                  U(P("Joh. Christoph Konze “IV”", "b. 1796 — d. 1873", "farmer, Steinweg 136", "m"),
                    P("Marie Temme", "", "", "f"),
                    children=[
                        P("Ludwig", "b. 1824 — d. 1896", "", "m"),
                        P("Philipp Heinrich", "b. 1831 — d. 1860", "unmarried", "m"),
                        P("Maria Wilhelmine", "b. ~1834 — d. ~1841", "", "f"),
                        P("Sophie", "b./d. 1839", "+ stillborn son 1841", "f"),
                    ], maxrow=2),
                  U(P("Ludwig Konze 1r", "b. 1808 — d. 1875", "church elder · GHKF-CRH", "m"),
                    P("Amalie geb. Meimbresse", "Spiegelstraße 19", "", "f"),
                    children=[
                        P("Amalie", "b. ~1836 — d. 1840", "died in childhood", "f"),
                        P("Julius", "b. 1846 — d. 1848", "died in childhood", "m"),
                        P("(FS) C. Friedrich Wilhelm", "b. 1834 · × Amalie Garbe", "→ late network", "m", cand=True),
                    ]),
              ]),
        ]),
        ("Disambiguation — the two Wilhelmines", [
            P("Wilhelmine Schildknecht geb. Konze", "the OTHER Wilhelmine", "× J. H. Schildknecht · child 1835", "f"),
            P("Maria Wilhelmine Schildknecht", "b. 1811 — d. ~1874", "dau. of Schildknecht × geb. Kontzin", "f"),
        ]),
    ],
},
{
    "key": "de-buergermeister", "h2": "deisel", "h3": "Johann Christoph Konze",
    "aria": "Family tree of Bürgermeister Christoph Konze's line, Haus 125",
    "clusters": [
        ("", [
            U(P("Bürgermeister Christoph Konze", "b. 1784 — d. 1846", "mayor · GKD4-TB2 · two-wives overlap flagged", "m"),
              P("×1 A. M. Hillebrand (d. 1846)", "×2 M. E. Schrage (d. 1862)", "", "f"),
              children=[
                  P("Andreas", "b. 1806 — d. 1883", "of ×1", "m"),
                  U(P("Joh. Christoph “II”", "b. 1808 — d. 1860", "of ×1", "m"),
                    P("Wilhelmine Schrage", "", "", "f"),
                    children=[
                        U(P("Heinrich Wilhelm Konze", "b. 1844 — d. 1877", "Steinweg 139 · GV33-JSR", "m"),
                          P("Wilh. Heidemeier geb. Niemeyer", "m. 12 Dec 1875", "", "f"),
                          children=[P("no children recorded", "", "", "u")]),
                    ]),
                  P("Anna Catharina", "b. 1811", "of ×1", "f"),
                  P("Charlotte", "b. 1814 — d. 1859", "of ×1 · m. 1838 Heggemann/Kloppmann", "f"),
                  P("Christian", "b. 1808 †", "of ×2", "m"),
                  P("Wilhelmine", "b. 1811 — d. 1881", "of ×2", "f"),
                  P("Ludwig", "b. 1813", "of ×2", "m"),
                  P("Catharina Elisabeth", "b. 1815 — d. 1883", "of ×2", "f"),
                  P("Amalie", "b. 1818 — d. 1845", "of ×2 · × Sasse — family extinguished", "f"),
                  P("Maria", "b. 1821 — d. 1895", "of ×2", "f"),
                  U(P("Philipp Konze 1r", "b. 1825 — d. 1872", "village headman · GH8K-6HH", "m"),
                    P("Josephine Flor. Schildknecht", "m. 28 Oct 1849", "", "f"),
                    children=[P("prob. Philipp Ludwig", "b./d. 1872", "posthumous? flagged", "m")]),
                  P("Louise Amalia", "b. 1828 — d. 1829", "of ×2 · died at 8 months", "f"),
              ], maxrow=4),
        ]),
    ],
},
{
    "key": "de-jh-line", "h2": "deisel", "h3": "Joh. Henrich line",
    "aria": "Family tree of the Deisel Joh. Henrich line and other early-19th-century households",
    "clusters": [
        ("", [
            U(P("Johann Heinrich Kontze", "b. 1790 — d. 1865", "farmer · GQMB-K8C", "m"),
              P("Anna Catharina Köster", "d. before Jun 1850", "2nd J.H. × Köster couple", "f"),
              children=[
                  P("Wilhelmine", "b. 1820 — d. 1857", "× Philipp Köster 2r", "f"),
                  P("Ludwig", "b. 1821 — d. 1883", "", "m"),
                  U(P("Philipp Konze #2", "b. 1824 — d. ~1893 (FS)", "G36L-2RZ", "m"),
                    P("Wilhelmine Moritz", "b. 1823", "", "f"),
                    m="m. 14 Jun 1850",
                    children=[
                        P("(FS) Maria Catharina", "1850–1885 · × Schildknecht", "", "f", cand=True),
                        P("(FS) Philipp August", "1854–1909 · d. Kassel", "", "m", cand=True),
                    ]),
              ]),
        ]),
        ("", [
            U(P("Johannes Konze", "b. 1771 — d. 1838", "former village headman, Trift 66", "m"),
              P("Katharina Elisabeth Jordan", "d. 1842", "", "f"),
              children=[P("not yet traced", "", "", "u")]),
            U(P("Andreas Konze", "", "farmer · × Pfeffkumpf", "m"),
              P("Elisabeth Pfeffkumpf", "", "", "f"),
              children=[
                  P("Ludwig Friedrich", "b. early Jan 1835", "Entry 194 — reading flagged", "m", cand=True),
              ]),
            U(P("Johannes Konze", "", "× Hofedietz, before 1813", "m"),
              P("Anna Catharina Hofedietz", "", "", "f"),
              children=[
                  P("Ludwig", "b. 1813 — d. ~1880", "distinct from Ludwig b. 1808", "m"),
              ]),
        ]),
    ],
},
{
    "key": "de-late-network", "h2": "deisel", "h3": "late-19th-century",
    "aria": "Chart of the late-19th-century Deisel Konze network",
    "clusters": [
        ("≥8 patriarchs by ~1880 — children mostly died young", [
            U(P("Heinrich Konze", "", "farmer (Ackermann)", "m"), P("Maria Lemme", "", "", "f"),
              children=[P("Catharina Wilhelmine", "1866 — d. 1877", "", "f")]),
            U(P("Heinrich Konze (Steinweg 135)", "FS: 1835–1919", "G41K-C3S", "m"),
              P("Elise Sab. Phil. geb. Thiele", "FS: 1839–1909", "", "f"),
              children=[P("Philipp Ludwig", "b./d. 1868", "+ stillborn son 1876", "m"),
                        P("Ludwig Heinrich", "1873 — d. 1878", "(× C. P. Thiele row — same FS household)", "m")]),
            U(P("Ludwig Konze 3r", "", "farmer · GKD3-LFX", "m"),
              P("Marie geb. Kuhlmann", "vom Hesselhof", "", "f"),
              children=[P("Marie Elise Amalie", "b. 1858", "the one surviving child", "f"),
                        P("4 children died young", "1852–73 + stillborn 1857", "", "u")]),
        ]),
        ("", [
            U(P("C. Friedrich Wilhelm Konze", "FS: b. 1834", "farmer · GRGQ-F88", "m"),
              P("Amalie Garbe", "FS: m. 1860 Graebe", "", "f"),
              children=[P("Maria Wilhelmine", "1874 — d. 1879", "", "f"),
                        P("Catharina Elise", "1877 — d. 1879", "", "f")]),
            U(P("Heinrich Konze V.", "FS: 1847–1936", "GC4P-4Y1", "m"),
              P("Phil. Charl. Amalie Schildknecht", "b. ~1861 — d. 1889 · m. 9 May 1880", "register-verified · “Ohldhunst” was a misread", "f"),
              children=[P("Maria Martha", "d. 1881", "", "f")]),
            U(P("Johann Ludwig Konze", "", "farmer & innkeeper, Haus 50", "m"),
              P("Marie Amalie Auguste Konze", "b. 1857(?) — d. 1923", "a Konze–Konze marriage", "f"),
              children=[P("no children recorded", "", "", "u")]),
        ]),
        ("", [
            P("Ludwig Theodor × Schäfer", "child d. 1874", "day labourer", "m"),
            P("Philipp [Theodor?] × Schildknecht", "child d. 1874", "", "m"),
            P("Heinrich (Dorf 94) × Temme", "2 children d. 1869 · 1874", "", "m"),
            P("Carl Wilhelm × Lagemann", "child 1875–78", "day labourer", "m"),
            P("Heinrich Ludwig × Brümeyer", "one child documented", "House No. 45", "m"),
            P("Johannes Friedrich × Maria", "no children recorded", "farmer (Ackermann)", "m"),
        ]),
        ("", [
            P("Catharine Elise Steitz geb. Konze", "d. 13 Sep 1874", "× Steitz · a child d. 1874", "f"),
        ]),
    ],
},
{
    "key": "de-daughters", "h2": "deisel", "h3": "daughters married out",
    "aria": "Chart of the Deisel Konze daughters who married out",
    "clusters": [
        ("", [
            P("Marie Elisabeth Theile", "b. 1803 — d. bef. 1831", "× Ludwig Theile, miller", "f"),
            P("Cath. Elis. Weisenbach", "d. bef. Sep 1848", "×1 Schildknecht ×2 Weisenbach", "f"),
            P("M. Wilhelmine Kuhlmann", "~1790 — d. 1811", "childbed · GK82-23W", "f"),
            P("Anna Kath. Kuhlmann", "b. 1793 — d. 1842", "her sister-successor · G4YM-HJD", "f"),
        ]),
        ("", [
            P("Amalia Sasse née Konze", "b. 1813", "× Sasse", "f"),
            P("Anna Eufrosine née Konze", "", "husband not yet found", "f"),
            P("Maria Schildknecht geb. Konze", "d. before 1856", "× Christoph Schildknecht", "f"),
            P("Charlotte Meimbresse geb. Konze", "", "× K. W. L. Meimbresse", "f"),
        ]),
    ],
},

# ===================== FRIEDRICHSFELD (no h3s) =====================
{
    "key": "friedrichsfeld", "h2": "friedrichsfeld", "h3": None,
    "aria": "At-a-glance family tree of the Friedrichsfeld Konze baptisms",
    "caption": "The full Andreas-b.1795 family is charted under Trendelburg (Stammtafel branch).",
    "clusters": [
        ("", [
            U(P("Andreas Konze", "b. 1795 Trendelburg — d. 1854 Mainz", "PZF8-X19 · → Trendelburg chart", "m"),
              P("×1 Wilhelmine Hofeditz (1821)", "×2 Maria Sophia Hofeditz", "Hofeditz colonist family", "f"),
              children=[
                  P("Heinrich Wilhelm Kontze", "b. 12 Feb 1832 — d. 1858 Stammen", "PZFD-1X4 · baptized here", "m"),
                  P("August Konze", "b. 15 Oct — d. 17 Oct 1834", "P878-8L1 · died at two days", "m"),
                  P("“[?]ard Kontze, Colonist”", "1835 — probably spurious", "2026 re-read: a Dölfer baptism", "u", cand=True),
              ]),
        ]),
    ],
},

# ===================== STAMMEN (no h3s) =====================
{
    "key": "stammen", "h2": "stammen", "h3": None,
    "aria": "At-a-glance family tree of the Stammen Konze household",
    "clusters": [
        ("The swineherd's family — fully reconstructed (Session 96): Andreas, son of Arnold Philipp Konze of Trendelburg", [
            U(P("Andreas Kontze, swineherd", "b. ~1758 Trendelburg — d. 31 Dec 1828 Stammen", "son of Arnold Philipp Konze", "m"),
              P("Maria Elisabeth Gerlandt", "b. ~1760 — d. 20 Nov 1817 Stammen", "dau. of Christoph Gerlandt", "f"),
              m="m. 23 Mar 1783, Stammen",
              children=[
                  P("George Henrich", "1784 — †1784", "", "m"),
                  P("Johann Christian", "b. 1 Jul 1785", "untraced — worth following", "m"),
                  P("Johannes", "b. 26 Jul 1788 — d. 1837 Hümme", "linen weaver · → Hümme chart", "m"),
                  P("Catharina Elisabeth", "b. 30 Aug 1791", "poss. × Lorenz Becker", "f"),
                  P("Maria Sophia", "1793 — d. 26 Dec 1829", "× J.C.A.W. Müller ~1815", "f"),
                  P("Johann Conrad", "1796 — d. 19 Mar 1812", "died at 15", "m"),
                  P("Anna Catharina", "b. 25 Jan 1799", "not yet traced", "f"),
                  P("Johann Henrich", "b. 20 May 1800", "untraced — worth following", "m"),
                  P("Johann Ludwig", "1802 — †1804", "", "m"),
                  P("Maria Charlotta", "1805 — †1805", "", "f"),
                  U(P("Christian Ludwig Kontze", "b. 20 Nov 1806 STAMMEN — d. 11 Apr 1883", "bap. here · day labourer, Nr. 21", "m"),
                    P("Anne Gertrud Temme", "b. ~1800 Stammen", "", "f"),
                    m="m. 9 Jun 1833",
                    children=[
                        P("a stillborn son", "b. 14 Mar 1835", "bur. 16 Mar 1835 — not Charles", "m"),
                    ]),
                  P("Sophia Maria", "1809 — †1810", "", "f"),
              ], maxrow=4),
        ]),
        ("Stammen Jungkonze households", [
            P("Joh. Christoph Jungkontze", "b. ~1768 — d. 16 May 1824", "Maurer · brother of Johannes", "m"),
            U(P("Johannes Jungkonze", "", "× Maria Catharina Lohr", "m"),
              P("Maria Catharina Lohr", "", "", "f"),
              children=[
                  P("Anna Elisabeth", "b. 16 Dec 1801", "", "f"),
                  P("Johann Conrad", "1805 — †1807", "", "m"),
                  P("Johannes jr.", "b. 22 Jun 1808 — †1865", "prob. the 1834 Weißbindergesell", "m"),
                  P("Wilhelmina", "1809 — †1809", "", "f"),
                  P("Maria Sophia", "1811 — †1812", "", "f"),
              ]),
        ]),
        ("Trendelburg Konze who lived or died in Stammen", [
            P("Andreas Contze “the Elder”", "b. ~1723 — d. 1800", "resident 1787 · → Trendelburg", "m"),
            P("Elisa Melusine Kontze", "b. 1822 — d. 1865 here", "PZF6-H42 · never married", "f"),
            P("Heinrich Wilhelm Kontze", "b. 1832 — d. 1858 here", "PZFD-1X4 · FS: m. 1856 Pappenheim", "m"),
        ]),
    ],
},

# ===================== GOTTSBÜREN (no h3s) =====================
{
    "key": "gottsbueren", "h2": "gottsbueren", "h3": None,
    "aria": "At-a-glance chart of the claimed, unconfirmed Gottsbüren Konze connection",
    "caption": "The claim is REFUTED — Christian Ludwig's baptism (20 Nov 1806) is in STAMMEN; no Kontze event in Gottsbüren's registers.",
    "clusters": [
        ("The refuted claim — the family was Stammen's, not Gottsbüren's", [
            U(P("Andreas Kontze, swineherd", "b. ~1758 — d. 1828 Stammen", "burial found · never of Gottsbüren", "m", cand=True),
              P("Marie Elis. geb. Gerlandt", "b. ~1760 — d. 1817 Stammen", "Gerlandt kin around Stammen", "f", cand=True),
              m="m. 23 Mar 1783, Stammen",
              children=[
                  P("Johannes", "b. 1788 Stammen — d. 1837 Hümme", "→ Hümme chart", "m"),
                  P("Christian Ludwig", "bap. 20 Nov 1806 IN STAMMEN", "the 1833 “von Gottsbüren” is wrong", "m"),
              ]),
        ]),
        ("Died here", [
            P("Maria Caroline Wichard", "b. 1807 Trendelburg — d. ~1855", "geb. Jungconze · × Wichard", "f"),
        ]),
    ],
},

# ===================== HÜMME =====================
{
    "key": "hu-kuester", "h2": "huemme", "h3": "sexton",
    "aria": "Family tree of the Hümme sexton (Küster) line and elders",
    "clusters": [
        ("", [
            U(P("Johann Conrad Kontze", "d. before Sep 1834", "sexton (Küster) & farmer", "m"),
              P("Marie Elisabeth Knüppel", "b. ~1760 — d. 1834", "", "f"),
              children=[P("not yet traced", "", "", "u")]),
            P("Johann Konrad Kontze", "b. 1766 — d. 1849", "military pensioner · never married", "m"),
        ]),
        ("", [
            U(P("Johann Christoph Kontze", "d. before Apr 1831", "G245-6VQ · FS: 1763–1828", "m"),
              P("Anne Christine Göbel", "b. ~1772 — d. 1837", "of Deisel", "f"),
              m="FS: m. 4 Sep 1795",
              children=[
                  U(P("Johannes Kontze", "b. 1801 — d. 1834", "farmer, Haus 126", "m"),
                    P("Marie Magd. Uffelmann", "she remarried Davin", "", "f"),
                    m="m. 10 Apr 1831",
                    children=[
                        U(P("Conrad Kontze", "b. ~26 Jan 1833 — d. 1895", "farmer (Ackermann)", "m"),
                          P("Marie Wilhelmine Rödde", "d. 1901", "", "f"),
                          m="m. 16 Jan 1859",
                          children=[
                              P("3 children died young", "1859–66", "", "u"),
                              P("Marie Sofie Emilie", "b. 1867 · m. Hoff 1890", "", "f"),
                          ]),
                        P("Wilhelmina Friederika", "b. ~1833 · m. Becker 1856", "", "f"),
                    ]),
              ]),
        ]),
    ],
},
{
    "key": "hu-busch", "h2": "huemme", "h3": "named emigrant",
    "aria": "Family tree of the Friedrich Kontze × Busch household with the named emigrant Christoph",
    "clusters": [
        ("", [
            U(P("Friedrich Kontze", "d. before May 1828", "farmer · GRC2-K99", "m"),
              P("Marie Sophie Busch", "d. before 1828–30", "children orphaned by 1828", "f"),
              children=[
                  U(P("Johannes Kontze", "b. 1810 — d. 1871 Stammen", "day labourer", "m"),
                    P("×1 M. C. Hofeditz (1841)", "×2 Anna Catharine Sasse", "", "f"),
                    children=[P("children not itemized", "", "", "u")]),
                  P("Christoph Kontze", "b. 13 Feb 1814 — vanishes", "★ presumed 1840s emigrant", "m", cand=True),
                  U(P("Friedrich Kontze", "b. 1817 — d. 1897", "day labourer", "m"),
                    P("Wilhelmine Büngener", "d. 1884", "", "f"),
                    m="m. ~15 Apr 1843",
                    children=[
                        P("Conrad", "b. 1844 · m. 1867 — d. 1906", "", "m"),
                        P("Christoph Heinrich", "b. 1847 — d. 1909", "m. 1877 + 1889", "m"),
                        P("Friedrich Wilhelm", "1849 — d. 1854", "died in childhood", "m"),
                        P("Elise Amalie", "b. 1853 · m. 1874", "", "f"),
                        P("Karl", "b./d. 1856", "died in infancy", "m"),
                    ], maxrow=3),
              ], maxrow=3),
        ]),
    ],
},
{
    "key": "hu-swineherd-son", "h2": "huemme", "h3": "swineherd&rsquo;s son",
    "h3_alt": "swineherd's son",
    "aria": "Family tree of Johannes Kontze the linen weaver, the Stammen swineherd's son",
    "clusters": [
        ("", [
            U(P("Johannes Kontze, linen weaver", "b. 1788 Stammen — d. 1837", "Haus 86 · brother of Christian Ludwig", "m"),
              P("Cath. Elis. Lichtefeld", "b. 1788 — d. 1849", "", "f"),
              children=[
                  U(P("Friedrich Kontze", "b. 1816 — d. 1873 Hümme", "linen weaver · GPK7-JYP", "m"),
                    P("×1 Büngener ×2 Koch", "×3 K. W. Thiele (1856)", "FS “d. New York” claim — flagged", "f"),
                    children=[P("Marie Caroline", "b./d. 1858", "died in infancy", "f")]),
                  P("Heinrich", "b. 1823 — d. 1842", "journeyman tailor", "m"),
                  P("Margarethe Elisabeth", "m. Hoff 1845", "", "f"),
              ]),
        ]),
    ],
},
{
    "key": "hu-jh-line", "h2": "huemme", "h3": "Johann Heinrich line",
    "aria": "Family tree of the Hümme Johann Heinrich line and other households",
    "clusters": [
        ("", [
            U(P("Johann Heinrich Kontze", "b. 1793 — d. 1840", "farm-estate owner", "m"),
              P("Marie Elisabeth Büngener", "b. 1802 — d. 1852", "", "f"),
              children=[
                  U(P("Wilhelm Kontze", "b. ~1827 — d. after Sep 1911", "diamond wedding 1911!", "m"),
                    P("Sabina Philippina Busch", "golden wedding 1901", "", "f"),
                    m="m. 28 Sep 1851",
                    children=[
                        P("Marie", "b. 1852 · m. 1876", "", "f"),
                        P("Johannes", "b./d. 1855", "died in infancy", "m"),
                        P("Emilie Karoline", "b. 1857 · m. 1884", "", "f"),
                        P("Joh. Friedrich Wilhelm", "b. 1861 · m. 1889 — d. 1933", "", "m"),
                    ], maxrow=4),
              ]),
        ]),
        ("", [
            U(P("Georg Friedrich Kontze", "b. 1800 — d. 1856", "day labourer", "m"),
              P("Marie Christine Kuhlmann", "b. 1804 — d. 1864", "of Eberschütz", "f"),
              children=[
                  P("Anna Rosina", "b. ~1823 · m. Schwedes 1850", "", "f"),
                  P("Wilhelm", "b./d. 1848", "died in infancy", "m"),
              ]),
        ]),
        ("Married-out Kontze women", [
            P("Marie Elisabeth Laubert", "geb. Kontze", "× Christoph Laubert (bef. 1829)", "f"),
            P("Anne Catharine Altmann", "geb. Kontze", "widow by 1831 · a daughter m. 1831", "f"),
        ]),
    ],
},
]


# ---------------- page insertion ----------------

def strip_text(s):
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', H.unescape(s)).strip()


def find_anchor(page, tree):
    """Return index in page right after which the tree block is inserted."""
    h2m = re.search(f'<h2 id="{tree["h2"]}"', page)
    if not h2m:
        raise SystemExit(f'h2 anchor not found for {tree["key"]}')
    h2end = page.find('</h2>', h2m.start()) + 5
    next_h2 = re.search(r'<h2 id="', page[h2end:])
    sec_end = h2end + (next_h2.start() if next_h2 else len(page) - h2end)
    if tree["h3"] is None:
        subm = re.compile(r'<p class="town-sub">.*?</p>', re.S).search(page, h2end, sec_end)
        return subm.end() if subm and subm.start() - h2end < 400 else h2end
    wanted = [strip_text(tree["h3"])]
    if tree.get("h3_alt"):
        wanted.append(strip_text(tree["h3_alt"]))
    for m in re.finditer(r'<h3[^>]*>(.*?)</h3>', page[h2end:sec_end], re.S):
        text = strip_text(m.group(1))
        for wantedsub in wanted:
            # normalise quotes for matching
            t = text.replace('’', "'").replace('“', '"').replace('”', '"')
            w = wantedsub.replace('’', "'").replace('“', '"').replace('”', '"')
            if w.lower() in t.lower():
                return h2end + m.end()
    raise SystemExit(f'h3 anchor "{tree["h3"]}" not found for {tree["key"]}')


def main():
    page = PAGE.read_text(encoding="utf-8")

    # 1. strip every previous tree block + CSS (idempotent)
    page = re.sub(r'\n*<!-- BEGIN-TOWN-TREE:[\w-]+ -->.*?<!-- END-TOWN-TREE:[\w-]+ -->\n*',
                  '\n', page, flags=re.S)
    page = re.sub(r'\n?<!-- BEGIN-TOWN-TREE-CSS -->.*?<!-- END-TOWN-TREE-CSS -->\n?',
                  '', page, flags=re.S)
    page = page.replace('</head>', TREE_CSS + '\n</head>', 1)

    # 2. insert each tree at its sub-section anchor
    for tree in TREES:
        svg = build_svg(tree)
        cap = (f'\n<figcaption class="town-tree-caption">{tree["caption"]}</figcaption>'
               if tree.get("caption") else '')
        leg = (LEGEND_HTML + '\n') if tree.get("legend") else ''
        block = (f'<!-- BEGIN-TOWN-TREE:{tree["key"]} -->\n'
                 f'<figure class="town-tree" aria-label="{esc(tree["aria"])}">\n'
                 f'{leg}{svg}{cap}\n'
                 f'</figure>\n'
                 f'<!-- END-TOWN-TREE:{tree["key"]} -->')
        at = find_anchor(page, tree)
        page = page[:at] + '\n\n' + block + page[at:]

    PAGE.write_text(page, encoding="utf-8")
    print(f'inserted/updated {len(TREES)} family trees in {PAGE.name}')


if __name__ == "__main__":
    main()
