#!/usr/bin/env python3
"""
Huurs Studio - Surah Fatir Master Mindmap HTML & Markdown Generator
8 Landscape Plates • 16 Thematic Pillars • 64 Detailed Analytical Cards
"""

import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "FATIR_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "FATIR_MASTER_MINDMAP.md")
PDF_SRC = os.path.join(BASE_DIR, "build_fatir_mindmap_pdf.py")

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
    chrome = re.search(r'draw_chrome\(\s*' + str(pnum) + r',\s*8,\s*"([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\s*\)', p_text)
    if not chrome:
        print(f"Warning: Chrome not matched for page {pnum}")
        continue
    title, desc, sec = chrome.groups()
    
    col1_m = re.search(r'pdf\.text\("(PILLAR \d+:[^"]+)",\s*c1_x \+ 12,\s*c1_y \+ c1_h - 16,\s*font="F2",\s*size=8\.8,\s*rgb=([A-Z_]+)\)', p_text)
    col1_sub = re.search(r'pdf\.text\("([^"]+)",\s*c1_x \+ 12,\s*c1_y \+ c1_h - 28,\s*font="F3",\s*size=7\.2,\s*rgb=TEXT_MUTED\)', p_text)
    
    col2_m = re.search(r'pdf\.text\("(PILLAR \d+:[^"]+)",\s*c2_x \+ 12,\s*c1_y \+ c1_h - 16,\s*font="F2",\s*size=8\.8,\s*rgb=([A-Z_]+)\)', p_text)
    subs = re.findall(r'pdf\.text\("([^"]+)",\s*c\d+_x \+ 12,\s*c\d+_y \+ c1_h - 28,\s*font="F3",\s*size=7\.2,\s*rgb=TEXT_MUTED\)', p_text)
    
    card_pattern = re.compile(r'draw_card\(\s*c(\d+)_x,\s*[^,]+,\s*[^,]+,\s*(\d+),\s*"([^"]+)",\s*\n?\s*"([^"]+)"\s*\)')
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
                "color": color_map.get(col1_m.group(2), "cyan") if col1_m else "cyan",
                "cards": col1_cards
            },
            {
                "name": col2_m.group(1) if col2_m else f"PILLAR {pnum*2}",
                "sub": subs[1] if len(subs) > 1 else "",
                "color": color_map.get(col2_m.group(2), "purple") if col2_m else "purple",
                "cards": col2_cards
            }
        ]
    }
    pages_data.append(p_obj)

# Generate Markdown
md_lines = [
    "# Surah Fatir: Master Mindmap Knowledge Architecture",
    "### 16:9 Landscape Cartography • 8 Plates • 16 Thematic Pillars • 64 Analytical Cards",
    "**Source Authority:** Classical Sunni Exegesis (Tabari, Ibn Kathir, Qurtubi, Razi, Baghawi, Ibn al-Qayyim)",
    "**Operating Principle:** Read. Reflect. Return.\n",
    "---\n"
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

# Generate HTML
tabs_html = ""
html_plates = ""

for idx, p in enumerate(pages_data):
    active = "active" if idx == 0 else ""
    sec_short = p["sec"].split(":")[-1].strip()
    tabs_html += f'<button class="tab-btn {active}" onclick="showPage({p["page"]})">Plate {p["page"]:02d}: {sec_short}</button>\n'
    
    pillars_html = ""
    for pil in p["pillars"]:
        cards_html = ""
        for c in pil["cards"]:
            bullets = "".join(f"<li>{b}</li>" for b in c["bullets"])
            cards_html += f'''
            <div class="card">
              <div class="card-head">
                <span class="card-num">{c["num"]}</span>
                <h4>{c["title"]}</h4>
              </div>
              <ul>{bullets}</ul>
            </div>'''
        pillars_html += f'''
        <div class="pillar">
          <div class="pillar-header {pil["color"]}">
            <h3>{pil["name"]}</h3>
            <p>{pil["sub"]}</p>
          </div>
          <div class="pillar-cards">
            {cards_html}
          </div>
        </div>'''
        
    html_plates += f'''
    <div id="page-{p["page"]}" class="page-container {active}">
      <div class="plate-title-bar">
        <div>
          <h2>{p["title"]}</h2>
          <p>{p["desc"]}</p>
        </div>
        <span class="plate-badge">{p["sec"]}</span>
      </div>
      <div class="pillars-grid">
        {pillars_html}
      </div>
    </div>'''

html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Fatir Master Mindmap • Huurs Studio</title>
  <style>
    :root {{
      --navy-deep: #060A12;
      --navy-card: #0D1422;
      --navy-elevated: #141E32;
      --gold: #D4AF59;
      --gold-light: #E8D194;
      --cyan: #38BDF8;
      --purple: #A855F7;
      --emerald: #10B981;
      --rose: #F43F5E;
      --white: #F8FAFC;
      --text-muted: #94A3B8;
      --border-muted: #26354D;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
      line-height: 1.5;
    }}
    .wrapper {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 24px;
    }}
    header.header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--border-muted);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    header.header h1 {{
      font-size: 1.4rem;
      color: var(--gold);
      letter-spacing: 1px;
    }}
    header.header span {{
      font-size: 0.9rem;
      color: var(--text-muted);
    }}
    .tabs-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
    }}
    .tab-btn {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      padding: 8px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.82rem;
      transition: all 0.2s;
    }}
    .tab-btn:hover {{
      border-color: var(--gold);
      color: var(--white);
    }}
    .tab-btn.active {{
      background: var(--navy-elevated);
      border-color: var(--gold);
      color: var(--gold);
      font-weight: 600;
    }}
    .page-container {{
      display: none;
    }}
    .page-container.active {{
      display: block;
    }}
    .plate-title-bar {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-left: 4px solid var(--gold);
      padding: 16px 20px;
      border-radius: 8px;
      margin-bottom: 20px;
    }}
    .plate-title-bar h2 {{
      font-size: 1.15rem;
      color: var(--white);
      margin-bottom: 4px;
    }}
    .plate-title-bar p {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .plate-badge {{
      background: var(--navy-elevated);
      color: var(--gold);
      border: 1px solid var(--gold);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.5px;
      white-space: nowrap;
    }}
    .pillars-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 900px) {{
      .pillars-grid {{ grid-template-columns: 1fr; }}
    }}
    .pillar {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }}
    .pillar-header {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-elevated);
    }}
    .pillar-header.cyan h3 {{ color: var(--cyan); }}
    .pillar-header.purple h3 {{ color: var(--purple); }}
    .pillar-header.emerald h3 {{ color: var(--emerald); }}
    .pillar-header.gold h3 {{ color: var(--gold); }}
    .pillar-header.rose h3 {{ color: var(--rose); }}
    .pillar-header h3 {{
      font-size: 0.95rem;
      margin-bottom: 4px;
      letter-spacing: 0.5px;
    }}
    .pillar-header p {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .pillar-cards {{
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .card {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 14px;
      transition: transform 0.15s, border-color 0.15s;
    }}
    .card:hover {{
      transform: translateY(-2px);
      border-color: var(--gold);
    }}
    .card-head {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .card-num {{
      background: var(--navy-card);
      color: var(--gold);
      border: 1px solid var(--border-muted);
      font-size: 0.72rem;
      font-weight: bold;
      padding: 2px 6px;
      border-radius: 4px;
    }}
    .card-head h4 {{
      font-size: 0.88rem;
      color: var(--white);
      font-weight: 600;
    }}
    .card ul {{
      list-style-type: none;
      padding-left: 0;
    }}
    .card li {{
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}
    footer.footer {{
      margin-top: 40px;
      border-top: 1px solid var(--border-muted);
      padding-top: 16px;
      text-align: center;
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>
  <div class="wrapper">
    <header class="header">
      <div>
        <h1>SURAH FATIR • MASTER MINDMAP ARCHITECTURE</h1>
        <span>8 Widescreen Plates • 16 Pillars • 64 Detailed Analytical Cards</span>
      </div>
      <div>
        <a href="FATIR_MASTER_MINDMAP.pdf" target="_blank" style="background:var(--gold); color:var(--navy-deep); padding:8px 14px; border-radius:6px; font-weight:600; text-decoration:none; font-size:0.82rem;">Download Vector PDF ↗</a>
      </div>
    </header>

    <div class="tabs-bar">
      {tabs_html}
    </div>

    {html_plates}

    <footer class="footer">
      Huurs Knowledge Systems • Classical Sunni Source Discipline (Tabari, Ibn Kathir, Qurtubi, Razi, Baghawi, Ibn al-Qayyim) • READ. REFLECT. RETURN.
    </footer>
  </div>

  <script>
    function showPage(pnum) {{
      document.querySelectorAll('.page-container').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      
      const target = document.getElementById('page-' + pnum);
      if (target) target.classList.add('active');
      
      const btns = document.querySelectorAll('.tab-btn');
      if (btns[pnum - 1]) btns[pnum - 1].classList.add('active');
    }}
  </script>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_full)

print(f"HTML generated: {HTML_OUT}")
