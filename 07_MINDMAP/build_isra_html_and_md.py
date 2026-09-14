#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Isra Master Mindmap HTML & Markdown Generator
8 Landscape Plates • 16 Thematic Pillars • 64 Detailed Analytical Cards
"""

import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "ISRA_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "ISRA_MASTER_MINDMAP.md")
PDF_SRC = os.path.join(BASE_DIR, "build_isra_mindmap_pdf.py")

with open(PDF_SRC, "r", encoding="utf-8") as f:
    text = f.read()

pages_raw = text.split("pdf.new_page(w, h)")[1:]
pages_data = []

color_map = {
    "CYAN": "cyan",
    "PURPLE": "purple",
    "EMERALD": "emerald",
    "GOLD": "gold",
    "ROSE": "rose"
}

for pidx, p_text in enumerate(pages_raw):
    pnum = pidx + 1
    chrome = re.search(r"draw_chrome\(\s*" + str(pnum) + r",\s*8,\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*\"([^\"]+)\"\s*\)", p_text)
    if not chrome:
        print(f"Warning: Chrome not matched for page {pnum}")
        continue
    title, desc, sec = chrome.groups()
    
    col1_m = re.search(r"pdf\.text\(\"(PILLAR \d+:[^\"]+)\",\s*c1_x \+ 12,\s*c1_y \+ c1_h - 16,\s*font=\"F2\",\s*size=8\.8,\s*rgb=([A-Z_]+)\)", p_text)
    col1_sub = re.search(r"pdf\.text\(\"([^\"]+)\",\s*c1_x \+ 12,\s*c1_y \+ c1_h - 28,\s*font=\"F3\",\s*size=7\.2,\s*rgb=TEXT_MUTED\)", p_text)
    
    col2_m = re.search(r"pdf\.text\(\"(PILLAR \d+:[^\"]+)\",\s*c2_x \+ 12,\s*c1_y \+ c1_h - 16,\s*font=\"F2\",\s*size=8\.8,\s*rgb=([A-Z_]+)\)", p_text)
    subs = re.findall(r"pdf\.text\(\"([^\"]+)\",\s*c\d+_x \+ 12,\s*c\d+_y \+ c1_h - 28,\s*font=\"F3\",\s*size=7\.2,\s*rgb=TEXT_MUTED\)", p_text)
    
    card_pattern = re.compile(r"draw_card\(\s*c(\d+)_x,\s*[^,]+,\s*[^,]+,\s*(\d+),\s*\"([^\"]+)\",\s*\n?\s*\"([^\"]+)\"\s*\)")
    card_matches = card_pattern.findall(p_text)
    
    col1_cards = []
    col2_cards = []
    for ccol, cnum, ctitle, ctext in card_matches:
        card_obj = {
            "num": f"{int(cnum):02d}",
            "title": ctitle,
            "bullets": [ctext]
        }
        if ccol == "1":
            col1_cards.append(card_obj)
        else:
            col2_cards.append(card_obj)
            
    p_obj = {
        "page": pnum,
        "title": title,
        "desc": desc,
        "sec": sec,
        "pillars": [
            {
                "name": col1_m.group(1) if col1_m else f"PILLAR {pnum*2-1}",
                "sub": col1_sub.group(1) if col1_sub else "",
                "color": color_map.get(col1_m.group(2) if col1_m else "CYAN", "cyan"),
                "cards": col1_cards
            },
            {
                "name": col2_m.group(1) if col2_m else f"PILLAR {pnum*2}",
                "sub": subs[1] if len(subs) > 1 else "",
                "color": color_map.get(col2_m.group(2) if col2_m else "PURPLE", "purple"),
                "cards": col2_cards
            }
        ]
    }
    pages_data.append(p_obj)

# ==========================================
# GENERATE MARKDOWN
# ==========================================
md_lines = [
    "# Surah Al-Isra Master Landscape Mindmap",
    "## 8 Landscape Plates • 16 Thematic Pillars • 64 Detailed Analytical Cards",
    "",
    "> **Huurs Studio Knowledge Systems** • Sunni Islamic Source Discipline • Read. Reflect. Return.",
    "> Classical Authorities: *Tafsir al-Tabari, Tafsir Ibn Kathir, Tafsir al-Qurtubi, Mafatih al-Ghayb (Al-Razi), Ma'alim al-Tanzil (Al-Baghawi)*",
    "",
    "---",
    ""
]

for p in pages_data:
    md_lines.append(f"## Plate {p['page']:02d}: {p['title']}")
    md_lines.append(f"**Section:** `{p['sec']}` | **Focus:** {p['desc']}\n")
    
    for pil in p["pillars"]:
        md_lines.append(f"### {pil['name']}")
        if pil["sub"]:
            md_lines.append(f"*{pil['sub']}*\n")
        
        for c in pil["cards"]:
            md_lines.append(f"#### [{c['num']}] {c['title']}")
            for b in c["bullets"]:
                md_lines.append(f"- {b}")
            md_lines.append("")
    md_lines.append("---\n")

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"MD generated: {MD_OUT} ({len(pages_data)} plates, 64 cards)")

# ==========================================
# GENERATE HTML
# ==========================================
tabs_html = ""
html_plates = ""

for idx, p in enumerate(pages_data):
    active = "active" if idx == 0 else ""
    sec_short = p["sec"].split(":")[-1].strip()
    tabs_html += f'<button class="tab-btn {active}" onclick="showPage({p["page"]})">Plate {p["page"]:02d}: {sec_short}</button>\n'
    
    pillars_markup = ""
    for pil in p["pillars"]:
        cards_markup = ""
        for c in pil["cards"]:
            bullets_li = "".join(f"<li>{b}</li>" for b in c["bullets"])
            cards_markup += f"""
            <div class="card">
              <div class="card-head">
                <span class="card-num">{c['num']}</span>
                <h4>{c['title']}</h4>
              </div>
              <ul>
                {bullets_li}
              </ul>
            </div>"""
        pillars_markup += f"""
        <div class="pillar {pil['color']}">
          <div class="pillar-header">
            <h3>{pil['name']}</h3>
            <p>{pil['sub']}</p>
          </div>
          <div class="cards-grid">
            {cards_markup}
          </div>
        </div>"""

    html_plates += f"""
    <section class="page-container {active}" id="page-{p['page']}">
      <div class="page-header">
        <div class="page-meta">
          <span class="badge badge-gold">[{p['sec']}]</span>
          <span class="badge badge-blue">Page {p['page']:02d} / 08</span>
        </div>
        <h2>{p['title']}</h2>
        <p class="desc">{p['desc']}</p>
      </div>
      <div class="columns-grid">
        {pillars_markup}
      </div>
    </section>"""

html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Isra Master Landscape Mindmap | Huurs Studio</title>
  <style>
    :root {{
      --navy-deep: #060a12;
      --navy-card: #0d1422;
      --navy-elevated: #141e32;
      --gold: #d4af37;
      --gold-light: #e8d194;
      --cyan: #38bdf8;
      --purple: #a855f7;
      --emerald: #10b981;
      --rose: #f43f5e;
      --white: #f8fafc;
      --text-muted: #adc0d4;
      --border-muted: #29384f;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      padding: 24px;
      line-height: 1.5;
    }}
    .wrapper {{
      max-width: 1400px;
      margin: 0 auto;
    }}
    header.header {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-top: 3px solid var(--gold);
      border-radius: 8px;
      padding: 16px 24px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    header.header h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.05em;
    }}
    header.header span {{
      color: var(--text-muted);
      font-size: 0.9rem;
      border-left: 1px solid var(--border-muted);
      padding-left: 12px;
      margin-left: 12px;
    }}
    .tabs-bar {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 8px;
      margin-bottom: 20px;
    }}
    .tab-btn {{
      background: var(--navy-card);
      color: var(--text-muted);
      border: 1px solid var(--border-muted);
      padding: 10px 16px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .tab-btn:hover {{
      border-color: var(--gold);
      color: var(--white);
    }}
    .tab-btn.active {{
      background: var(--navy-elevated);
      color: var(--gold);
      border-color: var(--gold);
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
    }}
    .page-container {{
      display: none;
    }}
    .page-container.active {{
      display: block;
    }}
    .page-header {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px 24px;
      margin-bottom: 20px;
    }}
    .page-meta {{
      display: flex;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .badge {{
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .badge-gold {{ background: rgba(212, 175, 55, 0.15); color: var(--gold-light); border: 1px solid var(--gold); }}
    .badge-blue {{ background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid var(--cyan); }}
    .page-header h2 {{
      font-size: 1.25rem;
      color: var(--white);
      margin-bottom: 4px;
    }}
    .page-header p.desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
    }}
    .columns-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 900px) {{
      .columns-grid {{ grid-template-columns: 1fr; }}
    }}
    .pillar {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }}
    .pillar.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar.purple {{ border-top: 3px solid var(--purple); }}
    .pillar.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar.gold {{ border-top: 3px solid var(--gold); }}
    .pillar.rose {{ border-top: 3px solid var(--rose); }}
    .pillar-header {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-elevated);
    }}
    .pillar-header h3 {{
      font-size: 0.95rem;
      color: var(--white);
      margin-bottom: 2px;
    }}
    .pillar-header p {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .cards-grid {{
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .card {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 16px;
      transition: all 0.2s;
    }}
    .card:hover {{ border-color: var(--gold); transform: translateY(-1px); }}
    .card-head {{ display: flex; align-items: baseline; gap: 10px; margin-bottom: 8px; }}
    .card-num {{
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .card-head h4 {{ font-size: 0.88rem; font-weight: 700; color: var(--white); }}
    .card ul {{ list-style-type: none; padding-left: 0; }}
    .card li {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 4px;
      position: relative;
      padding-left: 14px;
    }}
    .card li::before {{
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 0.8rem;
    }}
    footer.footer {{
      margin-top: 40px;
      border-top: 1px solid var(--border-muted);
      padding: 20px 0;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>
  <div class="wrapper">
    <header class="header">
      <div>
        <h1>HUURS STUDIO</h1>
        <span>Surah Al-Isra Master Landscape Mindmap Cartography</span>
      </div>
      <div style="font-size:0.8rem; color:var(--gold);">
        8 Master Plates &bull; 16 Thematic Pillars &bull; 64 Cards
      </div>
    </header>

    <div class="tabs-bar">
      {tabs_html}
    </div>

    <main>
      {html_plates}
    </main>

    <footer class="footer">
      <p><b>HUURS STUDIO</b> &bull; READ. REFLECT. RETURN. &bull; Sunni Islamic Source Discipline</p>
      <p style="font-size:0.75rem; margin-top:4px;">Imam at-Tabari &bull; Imam ar-Razi &bull; Imam al-Qurtubi &bull; Imam Ibn Kathir &bull; Imam al-Baghawi</p>
    </footer>
  </div>

  <script>
    function showPage(pnum) {{
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.page-container').forEach(page => page.classList.remove('active'));
      document.querySelectorAll('.tab-btn')[pnum - 1].classList.add('active');
      document.getElementById('page-' + pnum).classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}
  </script>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_full)

print(f"HTML generated: {HTML_OUT}")
