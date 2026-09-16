#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Qasas Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The River Nile & Asiyah's Sanctuary: Subverting Totalitarian Rule
    2. The Well of Madyan & The Beggar's Du'a: Chivalry, Modesty & The Hiring Blueprint
    3. The Sacred Theophany & Haman's Baked Clay Tower
    4. The Collapse of Qarun & The Eternal Abode: The Fallacy of the Self-Made Man
- Exegetical Thematic Movements Roadmap
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_QASAS_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_al_qasas_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_al_qasas_html_and_md import pages_data

thematic_movements = [
    ("Movement 1", "The Oppressed Vanguard, River of Faith & Asiyah's Sanctuary", "Movement 1", "Plates 01–02"),
    ("Movement 2", "The Crisis in Egypt, Desert Flight & The Well of Madyan", "Movement 2", "Plates 03–04"),
    ("Movement 3", "Mount Tur Theophany, Haman's Tower & The Sovereign Law of Guidance", "Movement 3", "Plates 05–06"),
    ("Movement 4", "The Hubris of Qarun, Liquefaction & The Eternal Abode", "Movement 4", "Plates 07–08")
]

# Generate Plates HTML
plates_html = ""
for pg in pages_data:
    active = "active" if pg["page"] == 1 else ""
    pillars_html = ""
    for pil in pg["pillars"]:
        cards_html = ""
        for c in pil["cards"]:
            bullets_html = "".join(f"<li>{b}</li>" for b in c["bullets"])
            cards_html += f"""
          <div class="card-item" data-search="{c['title'].lower()} {' '.join(c['bullets']).lower()}">
            <div class="card-title-row">
              <span class="card-idx">{c["num"]}</span>
              <h4>{c["title"]}</h4>
            </div>
            <ul class="card-points">
              {bullets_html}
            </ul>
          </div>"""
        pillars_html += f"""
      <div class="pillar-box">
        <div class="pillar-bar {pil["color"]}">
          <h3>{pil["name"]}</h3>
          <p>{pil["sub"]}</p>
        </div>
        <div class="cards-wrapper">
          {cards_html}
        </div>
      </div>"""

    plates_html += f"""
  <div class="plate-section {active}" id="plateSection{pg["page"]}">
    <div class="plate-title-bar">
      <div>
        <h2>{pg["title"]}</h2>
        <p>{pg["desc"]}</p>
      </div>
      <div class="plate-badge-box">
        <span class="badge-gold">[{pg["sec"]}]</span>
        <span class="badge-emerald">100% SUNNI VERIFIED</span>
      </div>
    </div>
    <div class="pillars-layout">
      {pillars_html}
    </div>
  </div>"""

# Tab buttons
tab_buttons_html = ""
for pg in pages_data:
    active = "active" if pg["page"] == 1 else ""
    tab_buttons_html += f"""<button class="tab-chip {active}" onclick="selectPlate({pg["page"]})">Plate {pg["page"]:02d}: {pg["sec"].split(':')[-1].strip()}</button>\n"""

# Movement list HTML
movement_items_html = ""
for idx, (code, title, mov, plates_range) in enumerate(thematic_movements, start=1):
    movement_items_html += f"""
    <div class="movement-row" onclick="filterByMovement('{mov}')">
      <div class="movement-meta-left">
        <span class="movement-num">{idx:02d}</span>
        <div>
          <div class="movement-title">{title}</div>
          <div class="movement-sub">{mov} • {plates_range}</div>
        </div>
      </div>
      <span class="movement-tag">Thematic Section</span>
    </div>"""

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Qasas — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
  <style>
    :root {{
      --bg-deep: #060A12;
      --bg-card: #0D1422;
      --bg-elevated: #141E32;
      --border-muted: #26354D;
      --gold: #D4AF59;
      --gold-light: #E8D194;
      --gold-glow: rgba(212, 175, 89, 0.25);
      --cyan: #38BDF8;
      --purple: #A855F7;
      --emerald: #10B981;
      --rose: #F43F5E;
      --white: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    .top-header {{
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-muted);
      padding: 18px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .brand-left {{
      display: flex;
      align-items: baseline;
      gap: 14px;
    }}
    .brand-left h1 {{
      font-size: 1.3rem;
      letter-spacing: 2px;
      color: var(--gold);
      font-weight: 800;
    }}
    .brand-left span {{
      font-size: 0.85rem;
      color: var(--text-muted);
      letter-spacing: 0.5px;
    }}
    .header-badges {{
      display: flex;
      gap: 10px;
    }}
    .badge {{
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}
    .badge-gold {{ background: var(--bg-elevated); color: var(--gold); border-color: var(--gold); }}
    .badge-cyan {{ background: var(--bg-elevated); color: var(--cyan); border-color: var(--cyan); }}
    .badge-emerald {{ background: var(--bg-elevated); color: var(--emerald); border-color: var(--emerald); }}

    .main-container {{
      max-width: 1560px;
      width: 100%;
      margin: 0 auto;
      padding: 24px 32px;
      flex: 1;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-elevated) 100%);
      border: 1px solid var(--border-muted);
      border-radius: 12px;
      padding: 28px 36px;
      margin-bottom: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      overflow: hidden;
    }}
    .hero-banner::after {{
      content: "القصص";
      position: absolute;
      right: 20px;
      top: -15px;
      font-size: 8rem;
      color: rgba(212, 175, 89, 0.04);
      font-family: serif;
      pointer-events: none;
    }}
    .hero-text h2 {{
      font-size: 1.8rem;
      color: var(--white);
      margin-bottom: 6px;
      font-weight: 700;
    }}
    .hero-text p {{
      font-size: 0.95rem;
      color: var(--text-muted);
      max-width: 820px;
      line-height: 1.5;
    }}
    .hero-stats {{
      display: flex;
      gap: 24px;
      text-align: right;
    }}
    .stat-box .val {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--gold);
    }}
    .stat-box .lbl {{
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .search-filter-panel {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      gap: 16px;
      align-items: center;
    }}
    .search-input-box {{
      flex: 1;
      position: relative;
    }}
    .search-input-box input {{
      width: 100%;
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 16px 10px 40px;
      color: var(--white);
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input-box input:focus {{
      border-color: var(--gold);
    }}
    .search-input-box::before {{
      content: "🔍";
      position: absolute;
      left: 14px;
      top: 10px;
      font-size: 0.85rem;
      opacity: 0.6;
    }}
    .search-stats {{
      font-size: 0.85rem;
      color: var(--text-muted);
      white-space: nowrap;
    }}

    .tab-strip {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
    }}
    .tab-chip {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      padding: 8px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .tab-chip:hover {{
      color: var(--white);
      border-color: var(--gold);
    }}
    .tab-chip.active {{
      background: var(--bg-elevated);
      color: var(--gold);
      border-color: var(--gold);
    }}

    .plate-section {{ display: none; }}
    .plate-section.active {{ display: block; }}

    .plate-title-bar {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .plate-title-bar h2 {{
      font-size: 1.2rem;
      color: var(--white);
      margin-bottom: 4px;
    }}
    .plate-title-bar p {{
      font-size: 0.84rem;
      color: var(--text-muted);
    }}
    .plate-badge-box {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}

    .pillars-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    .pillar-box {{
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }}
    .pillar-bar {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-muted);
    }}
    .pillar-bar.cyan h3 {{ color: var(--cyan); }}
    .pillar-bar.purple h3 {{ color: var(--purple); }}
    .pillar-bar.emerald h3 {{ color: var(--emerald); }}
    .pillar-bar.gold h3 {{ color: var(--gold); }}
    .pillar-bar.rose h3 {{ color: var(--rose); }}
    .pillar-bar h3 {{
      font-size: 0.95rem;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}
    .pillar-bar p {{
      font-size: 0.78rem;
      color: var(--text-muted);
      font-style: italic;
    }}
    .cards-wrapper {{
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .card-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 16px;
      transition: all 0.2s;
    }}
    .card-item:hover {{
      border-color: rgba(212, 175, 55, 0.4);
      transform: translateY(-1px);
    }}
    .card-title-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .card-idx {{
      font-size: 0.72rem;
      font-weight: 700;
      background: var(--bg-elevated);
      color: var(--gold);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}
    .card-title-row h4 {{
      font-size: 0.88rem;
      color: var(--white);
    }}
    .card-points {{
      list-style-type: none;
      padding-left: 0;
    }}
    .card-points li {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .thematic-modals-grid {{
      margin-top: 36px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }}
    .modal-trigger-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 20px;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .modal-trigger-card:hover {{
      border-color: var(--gold);
      transform: translateY(-2px);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }}
    .mtc-header {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--gold);
      margin-bottom: 8px;
    }}
    .mtc-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 10px;
      line-height: 1.35;
    }}
    .mtc-desc {{
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.4;
      margin-bottom: 14px;
      flex: 1;
    }}
    .mtc-cta {{
      font-size: 0.78rem;
      color: var(--cyan);
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .movements-section {{
      margin-top: 36px;
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 10px;
      padding: 24px;
    }}
    .movements-section h3 {{
      font-size: 1.1rem;
      color: var(--gold);
      margin-bottom: 16px;
      letter-spacing: 1px;
    }}
    .movement-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 16px;
      border-radius: 6px;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s;
      margin-bottom: 8px;
    }}
    .movement-row:hover {{
      background: var(--bg-elevated);
      border-color: var(--border-muted);
    }}
    .movement-meta-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .movement-num {{
      font-size: 1rem;
      font-weight: 800;
      color: var(--cyan);
      background: var(--bg-elevated);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--border-muted);
    }}
    .movement-title {{
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--white);
    }}
    .movement-sub {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .movement-tag {{
      font-size: 0.75rem;
      color: var(--gold);
      background: var(--bg-elevated);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}

    .modal-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(6px);
      display: none;
      justify-content: center;
      align-items: center;
      z-index: 1000;
      padding: 24px;
    }}
    .modal-overlay.open {{ display: flex; }}
    .modal-content {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 12px;
      max-width: 860px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 32px;
      position: relative;
    }}
    .modal-close-btn {{
      position: absolute;
      top: 20px;
      right: 20px;
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }}
    .modal-close-btn:hover {{
      color: var(--white);
      border-color: var(--rose);
      background: var(--rose);
    }}
    .modal-header h3 {{
      font-size: 1.3rem;
      color: var(--gold);
      margin-bottom: 6px;
    }}
    .modal-header p {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 20px;
    }}
    .modal-body {{
      color: var(--white);
      font-size: 0.92rem;
      line-height: 1.65;
    }}
    .modal-body h4 {{
      color: var(--cyan);
      margin: 18px 0 8px;
      font-size: 1rem;
    }}
    .modal-body p {{
      color: var(--text-muted);
      margin-bottom: 12px;
    }}
    .modal-body ul {{
      margin-left: 20px;
      margin-bottom: 16px;
    }}
    .modal-body li {{
      color: var(--text-muted);
      margin-bottom: 6px;
    }}

    footer.site-footer {{
      background: var(--bg-card);
      border-top: 1px solid var(--border-muted);
      padding: 24px 32px;
      text-align: center;
      margin-top: 48px;
    }}
    footer.site-footer p {{
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}
    footer.site-footer span {{
      font-size: 0.74rem;
      color: var(--gold-light);
      font-weight: 600;
      letter-spacing: 1px;
    }}
  </style>
</head>
<body>

  <header class="top-header">
    <div class="brand-left">
      <h1>HUURS STUDIO</h1>
      <span>SURAH AL-QASAS (28) • MASTER CARTOGRAPHY</span>
    </div>
    <div class="header-badges">
      <span class="badge badge-gold">8 PLATES</span>
      <span class="badge badge-cyan">16 PILLARS</span>
      <span class="badge badge-emerald">64 ANALYTICAL CARDS</span>
    </div>
  </header>

  <main class="main-container">

    <section class="hero-banner">
      <div class="hero-text">
        <h2>Surah Al-Qasas: The Subversion of Tyranny</h2>
        <p>The definitive visual cartography of Surah 28: from the oppressed vanguard and the Nile basket to the chivalry of Madyan, the Acacia shade, the celestial fire at Mount Tur, the ziggurat of Haman, and the liquefaction of Qarun's vaults.</p>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <div class="val">88</div>
          <div class="lbl">Verses</div>
        </div>
        <div class="stat-box">
          <div class="val">16</div>
          <div class="lbl">Pillars</div>
        </div>
        <div class="stat-box">
          <div class="val">64</div>
          <div class="lbl">Cards</div>
        </div>
      </div>
    </section>

    <section class="search-filter-panel">
      <div class="search-input-box">
        <input type="text" id="liveSearchInput" placeholder="Filter through all 64 cards across 8 plates (e.g., Asiyah, Madyan, Qarun, Haman, Istihya', Du'a)..." onkeyup="filterCards()">
      </div>
      <div class="search-stats" id="searchMatchCount">Showing 64 of 64 cards</div>
    </section>

    <div class="tab-strip">
      {tab_buttons_html}
    </div>

    <main id="platesContainer">
      {plates_html}
    </main>

    <div class="thematic-modals-grid">
      <div class="modal-trigger-card" onclick="openModal('modal1')">
        <div>
          <div class="mtc-header">Deep Monograph 01</div>
          <div class="mtc-title">The Nile Basket & Asiyah's Sanctuary</div>
          <div class="mtc-desc">How divine providence nurtured the instrument of Pharaoh's downfall inside Pharaoh's own palace through Asiyah's maternal intercession.</div>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>

      <div class="modal-trigger-card" onclick="openModal('modal2')">
        <div>
          <div class="mtc-header">Deep Monograph 02</div>
          <div class="mtc-title">The Well of Madyan & The Beggar's Du'a</div>
          <div class="mtc-desc">Chivalric service without compensation, the universal du'a in the acacia shade, sacred modesty, and the hiring standard: Al-Qawiyyu Al-Ameen.</div>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>

      <div class="modal-trigger-card" onclick="openModal('modal3')">
        <div>
          <div class="mtc-header">Deep Monograph 03</div>
          <div class="mtc-title">Mount Tur & Haman's Baked Clay Tower</div>
          <div class="mtc-desc">The theophany at the sacred bush, the miracles of the serpent and radiant hand, and the monumental narcissism of Pharaoh's mud-brick ziggurat.</div>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>

      <div class="modal-trigger-card" onclick="openModal('modal4')">
        <div>
          <div class="mtc-header">Deep Monograph 04</div>
          <div class="mtc-title">The Collapse of Qarun & The Eternal Abode</div>
          <div class="mtc-desc">Dismantling the meritocratic myth of the self-made man ('Ala 'Ilmin 'Indi), the sudden liquefaction of the earth, and the criteria of the Akhirah.</div>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>
    </div>

    <section class="movements-section">
      <h3>Exegetical Thematic Movements</h3>
      {movement_items_html}
    </section>

  </main>

  <!-- Modal 1 -->
  <div class="modal-overlay" id="modal1">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal1')">✕</button>
      <div class="modal-header">
        <h3>The Nile Basket & Asiyah's Sanctuary: Subverting Totalitarian Rule</h3>
        <p>Tafsir al-Tabari, Ibn Kathir & Al-Qurtubi • Sunni Exegetical Analysis</p>
      </div>
      <div class="modal-body">
        <h4>1. Pharaoh's Caste Fracturing & State Infanticide</h4>
        <p>Pharaoh exalted himself in the land by fragmenting society into hostile factions (<em>Shiya'an</em>), systematically slaughtering male infants of the Israelites. Against this ruthless machinery, Allah revealed Verse 5: <em>Wa nureedu an namunna 'ala alladhina-stud'ifu fil-ardi wa naj'alahum a'immatan wa naj'alahum al-waritheen</em>—the divine decree to elevate the oppressed and make them heirs of the land.</p>
        
        <h4>2. The Two Commands, Two Prohibitions, and Two Promises</h4>
        <p>Musa's mother received divine inspiration containing a complete theological covenant: Two commands (suckle him, cast him in the river), two prohibitions (do not fear, do not grieve), and two divine promises (We will return him to you, and We will make him a messenger). Placing a newborn in a river normally guarantees death, but when commanded by Allah, the river becomes a vessel of deliverance.</p>

        <h4>3. The Sanctuary of Queen Asiyah</h4>
        <p>When the palace guards opened the basket, Pharaoh intended immediate execution. Queen Asiyah (may Allah be pleased with her) stepped forward: <em>Qurratu 'aynin lee wa lak, la taqtuloohu 'asa an yanfa'ana aw nattakhidhahu walada</em> ("A comfort of the eye for me and you! Do not kill him"). In divine irony, Pharaoh ended up personally funding, clothing, and guarding the very child destined to dismantle his empire.</p>

        <h4>4. The Emptied Heart Bound by Divine Ribāt</h4>
        <p>The mother's heart became <em>Farighan</em>—empty of all earthly thoughts except Musa. Allah tied firm bonds upon her heart (<em>Rabatna 'ala qalbiha</em>), teaching that emotional resilience under catastrophic grief is a supernatural gift from Allah.</p>
      </div>
    </div>
  </div>

  <!-- Modal 2 -->
  <div class="modal-overlay" id="modal2">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal2')">✕</button>
      <div class="modal-header">
        <h3>The Well of Madyan & The Beggar's Du'a: Chivalry & Modesty</h3>
        <p>Fiqh of Leadership & Moral Adab • Tafsir Ibn Kathir & Al-Siyasah al-Shar'iyyah</p>
      </div>
      <div class="modal-body">
        <h4>1. Chivalric Service Without Compensation</h4>
        <p>Arriving at Madyan exhausted, starving, and barefoot, Musa saw male shepherds aggressively jostling at the well while two young women held back their flock (<em>Tadhudaan</em>). Musa lifted the heavy well stone unassisted and watered their flock, demanding no wage, praise, or social interaction, and immediately retreated to the acacia shade.</p>

        <h4>2. The Masterpiece Beggar's Du'a</h4>
        <p>Resting in the shade, Musa prayed: <em>Rabbi inni lima anzalta ilayya min khayrin faqeer</em> ("My Lord, indeed I am in desperate need of whatever good You send down upon me"). He did not dictate terms or demand gold; he declared his complete, humble destitution before whatever grace Allah chose to bestow.</p>

        <h4>3. Walking with Sacred Modesty (Istihya')</h4>
        <p>When one daughter returned with her father's invitation, the Qur'an describes her deportment: <em>Tamshi 'ala istihya'</em>. Modesty is not weakness; it is a radiant shield of dignity in speech, gait, and interpersonal dealings.</p>

        <h4>4. The Universal Hiring Benchmark: Al-Qawiyyu Al-Ameen</h4>
        <p>The daughter advised her father: <em>Inna khayra mani-sta'jarta al-qawiyyu al-ameen</em> ("The best of those you hire is the strong and trustworthy"). As Imam Ibn Taymiyyah notes in <em>Al-Siyasah al-Shar'iyyah</em>, every position of leadership rests on these twin pillars: Competence (<em>Quwwah</em>) and Integrity (<em>Amanah</em>).</p>
      </div>
    </div>
  </div>

  <!-- Modal 3 -->
  <div class="modal-overlay" id="modal3">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal3')">✕</button>
      <div class="modal-header">
        <h3>Mount Tur & Haman's Baked Clay Tower: Totalitarian Narcissism</h3>
        <p>Tafsir al-Razi & Al-Baghawi • The Theophany and Cosmic Arrogance</p>
      </div>
      <div class="modal-body">
        <h4>1. The Theophany at the Blessed Bush</h4>
        <p>After completing ten years of pastoral covenant, Musa traveled with his family across the Sinai. Seeing a fire upon Mount Tur, he was addressed from the right bank of the blessed valley from the tree: <em>Ya Musa inni ana Allahu rabbu al-'alameen</em>. He was granted the miracles of the staff turning into a serpent and the hand shining with celestial light.</p>

        <h4>2. Harun as Ministerial Partner</h4>
        <p>Recognizing human limits, Musa petitioned for his brother Harun as an articulate ministerial assistant: <em>Fa-arsilhu ma'iya rid'an yusaddiqunee</em>. Divine missions benefit from shared responsibility and collaborative clarity.</p>

        <h4>3. Pharaoh's Ziggurat of Clay</h4>
        <p>Pharaoh claimed absolute divinity: <em>Ma 'alimtu lakum min ilahin ghayri</em>, and commanded Haman to fire clay bricks to build an immense tower (<em>Sarhan</em>) to gaze at Musa's God. Totalitarian regimes invariably construct monumental architectural vanity to distract from their ethical bankruptcy.</p>

        <h4>4. The Sovereign Law of Guidance</h4>
        <p>The surah lays down the eternal law: <em>Innaka la tahdi man ahbabta wa lakinna Allaha yahdi man yasha'u</em>. Revealed upon Abu Talib's passing, it confirms that guidance belongs exclusively to Allah; human messengers are conveyors, not masters of human hearts.</p>
      </div>
    </div>
  </div>

  <!-- Modal 4 -->
  <div class="modal-overlay" id="modal4">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal4')">✕</button>
      <div class="modal-header">
        <h3>The Collapse of Qarun & The Eternal Abode: Dismantling Meritocracy</h3>
        <p>Madarij al-Salikin & Tafsir al-Qurtubi • Economic Ethics in Sunni Orthodoxy</p>
      </div>
      <div class="modal-body">
        <h4>1. Qarun's Hoard & The Fatal Claim: 'Ala 'Ilmin 'Indi</h4>
        <p>Qarun accumulated treasures whose iron keys burdened a cohort of strong men. When the righteous scholars offered him a fivefold ethical economic charter, he retorted with the slogan of predatory capitalism: <em>Innama ooteetuhu 'ala 'ilmin 'indi</em> ("I was only given this because of knowledge that I possess!"). He attributed his wealth to his personal intellect, denying divine favor.</p>

        <h4>2. The Sudden Cataclysm of Liquefaction</h4>
        <p>While parading in opulence before envious onlookers, the earth cracked open: <em>Fa-khasafna bihi wa bi-darihi al-ard</em>. The ground swallowed Qarun, his mansions, and his vaults. Neither his gold nor his armed guards could delay the divine decree.</p>

        <h4>3. The Constitutional Charter of the Akhirah</h4>
        <p>Verse 83 sets the eternal standard for salvation: <em>Tilka ad-daru al-akhiratu naj'aluha lilladhina la yureedoona 'uluwwan fil-ardi wa la fasada, wal-'aqibatu lil-muttaqeen</em>. The eternal Home of the Hereafter belongs strictly to those free of high-handed tyranny (<em>'Uluww</em>) and societal corruption (<em>Fasad</em>).</p>

        <h4>4. The Promise of Return</h4>
        <p>Exiled from Mecca, the Prophet ﷺ was given the divine promise: <em>Inna alladhi farada 'alayka al-Qur'ana la-raadduka ila ma'ad</em>. The surah closes with the ultimate doxological foundation: <em>Kullu shay'in halikun illa wajhah</em>—everything will perish except His Face.</p>
      </div>
    </div>
  </div>

  <footer class="site-footer">
    <p>Huurs Knowledge Systems • Deeper Thought Campaign • Surah Al-Qasas (28)</p>
    <span>AUTHENTIC SUNNI ISLAMIC SOURCE DISCIPLINE • READ. REFLECT. RETURN.</span>
  </footer>

  <script>
    function selectPlate(num) {{
      document.querySelectorAll('.plate-section').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-chip').forEach(el => el.classList.remove('active'));

      const target = document.getElementById('plateSection' + num);
      if (target) target.classList.add('active');

      const chips = document.querySelectorAll('.tab-chip');
      if (chips[num - 1]) chips[num - 1].classList.add('active');
    }}

    function filterCards() {{
      const query = document.getElementById('liveSearchInput').value.toLowerCase().trim();
      const allCards = document.querySelectorAll('.card-item');
      let visibleCount = 0;

      allCards.forEach(card => {{
        const searchData = card.getAttribute('data-search');
        if (!query || searchData.includes(query)) {{
          card.style.display = 'block';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      document.getElementById('searchMatchCount').innerText = `Showing ${{visibleCount}} of ${{allCards.length}} cards`;

      if (query.length > 0) {{
        document.querySelectorAll('.plate-section').forEach(sec => sec.classList.add('active'));
      }} else {{
        selectPlate(1);
      }}
    }}

    function filterByMovement(movName) {{
      if (movName === 'Movement 1') selectPlate(1);
      else if (movName === 'Movement 2') selectPlate(3);
      else if (movName === 'Movement 3') selectPlate(5);
      else if (movName === 'Movement 4') selectPlate(7);
      window.scrollTo({{ top: 400, behavior: 'smooth' }});
    }}

    function openModal(id) {{
      const m = document.getElementById(id);
      if (m) m.classList.add('open');
    }}

    function closeModal(id) {{
      const m = document.getElementById(id);
      if (m) m.classList.remove('open');
    }}

    window.onclick = function(event) {{
      if (event.target.classList.contains('modal-overlay')) {{
        event.target.classList.remove('open');
      }}
    }};
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"[OK] Interactive Suite HTML generated: {OUTPUT_HTML}")
