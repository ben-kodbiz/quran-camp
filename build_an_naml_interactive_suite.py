#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Naml Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Ant's Pastoral Wisdom & The Sublime Du'a of Awzi'ni
    2. The Diplomatic Missive & The Paved Crystal Palace
    3. The Five Cosmic Interrogations: A-Ilahun Ma'allah?
    4. Sun'allah: The Flawless Craftsmanship of Moving Mountains
- Exegetical Thematic Movements Roadmap
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AN_NAML_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_an_naml_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_an_naml_html_and_md import pages_data

thematic_movements = [
    ("Movement 1", "Sacred Illumination, Musa's Call & The Wisdom of Dawud/Sulayman", "Movement 1", "Plates 01–02"),
    ("Movement 2", "The Hoopoe Scout, Bilqis & The Translocation of the Throne", "Movement 2", "Plates 03–04"),
    ("Movement 3", "Thamud's Conspirators & The Five Cosmic Interrogations", "Movement 3", "Plates 05–06"),
    ("Movement 4", "Eschatological Signs, Moving Mountains & Supreme Praise", "Movement 4", "Plates 07–08")
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

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah An-Naml — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
  <style>
    :root {
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
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    .top-header {
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-muted);
      padding: 18px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .brand-left {
      display: flex;
      align-items: baseline;
      gap: 14px;
    }
    .brand-left h1 {
      font-size: 1.3rem;
      letter-spacing: 2px;
      color: var(--gold);
      font-weight: 800;
    }
    .brand-left span {
      font-size: 0.85rem;
      color: var(--text-muted);
      letter-spacing: 0.5px;
    }
    .header-badges {
      display: flex;
      gap: 10px;
    }
    .badge {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }
    .badge-gold { background: var(--bg-elevated); color: var(--gold); border-color: var(--gold); }
    .badge-cyan { background: var(--bg-elevated); color: var(--cyan); border-color: var(--cyan); }
    .badge-emerald { background: var(--bg-elevated); color: var(--emerald); border-color: var(--emerald); }

    .main-container {
      max-width: 1560px;
      width: 100%;
      margin: 0 auto;
      padding: 24px 32px;
      flex: 1;
    }

    .hero-banner {
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
    }
    .hero-banner::after {
      content: "النمل";
      position: absolute;
      right: 20px;
      top: -15px;
      font-size: 8rem;
      color: rgba(212, 175, 89, 0.04);
      font-family: serif;
      pointer-events: none;
    }
    .hero-text h2 {
      font-size: 1.8rem;
      color: var(--white);
      margin-bottom: 6px;
      font-weight: 700;
    }
    .hero-text p {
      font-size: 0.95rem;
      color: var(--text-muted);
      max-width: 820px;
      line-height: 1.5;
    }
    .hero-stats {
      display: flex;
      gap: 24px;
      text-align: right;
    }
    .stat-box .val {
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--gold);
    }
    .stat-box .lbl {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .search-filter-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      gap: 16px;
      align-items: center;
    }
    .search-input-box {
      flex: 1;
      position: relative;
    }
    .search-input-box input {
      width: 100%;
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 14px 10px 38px;
      color: var(--white);
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .search-input-box input:focus {
      border-color: var(--gold);
    }
    .search-input-box::before {
      content: "🔍";
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.85rem;
      color: var(--text-muted);
    }
    .quick-modals-bar {
      display: flex;
      gap: 8px;
    }
    .modal-trigger-btn {
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      color: var(--gold-light);
      padding: 8px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.2s;
      white-space: nowrap;
    }
    .modal-trigger-btn:hover {
      border-color: var(--gold);
      color: var(--gold);
      background: var(--bg-card);
    }

    .navigation-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
    }
    .tab-chip {
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      padding: 9px 16px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.2s;
    }
    .tab-chip:hover {
      color: var(--white);
      border-color: var(--gold);
    }
    .tab-chip.active {
      background: var(--bg-elevated);
      color: var(--gold);
      border-color: var(--gold);
      box-shadow: 0 0 12px var(--gold-glow);
    }

    .plate-section { display: none; }
    .plate-section.active { display: block; }

    .plate-title-bar {
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 24px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .plate-title-bar h2 {
      font-size: 1.25rem;
      color: var(--white);
      margin-bottom: 4px;
    }
    .plate-title-bar p {
      font-size: 0.85rem;
      color: var(--text-muted);
    }
    .plate-badge-box {
      display: flex;
      gap: 8px;
    }

    .pillars-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .pillar-box {
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }
    .pillar-bar {
      padding: 14px 20px;
      border-bottom: 1px solid var(--border-muted);
    }
    .pillar-bar.cyan h3 { color: var(--cyan); }
    .pillar-bar.purple h3 { color: var(--purple); }
    .pillar-bar.emerald h3 { color: var(--emerald); }
    .pillar-bar.gold h3 { color: var(--gold); }
    .pillar-bar.rose h3 { color: var(--rose); }
    .pillar-bar h3 {
      font-size: 0.95rem;
      letter-spacing: 0.5px;
      margin-bottom: 3px;
    }
    .pillar-bar p {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-style: italic;
    }

    .cards-wrapper {
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .card-item {
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 14px 16px;
      transition: all 0.2s;
    }
    .card-item:hover {
      border-color: rgba(212, 175, 89, 0.4);
      transform: translateY(-2px);
    }
    .card-title-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }
    .card-idx {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--gold);
      background: var(--bg-elevated);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }
    .card-title-row h4 {
      font-size: 0.9rem;
      color: var(--white);
    }
    .card-points {
      list-style-type: none;
      padding-left: 0;
    }
    .card-points li {
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
    }

    .movements-section {
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 10px;
      padding: 22px 28px;
      margin-top: 36px;
    }
    .movements-section h3 {
      font-size: 1.1rem;
      color: var(--gold);
      margin-bottom: 16px;
      letter-spacing: 1px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .movement-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }
    .movement-row {
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s;
    }
    .movement-row:hover {
      border-color: var(--gold);
      transform: translateX(4px);
    }
    .movement-meta-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .movement-num {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--gold);
      background: var(--bg-card);
      padding: 4px 8px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }
    .movement-title {
      font-size: 0.88rem;
      color: var(--white);
      font-weight: 600;
    }
    .movement-sub {
      font-size: 0.74rem;
      color: var(--text-muted);
    }
    .movement-tag {
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--cyan);
      background: var(--bg-card);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }

    .modal-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(6, 10, 18, 0.88);
      backdrop-filter: blur(6px);
      display: none;
      justify-content: center;
      align-items: center;
      z-index: 1000;
      padding: 24px;
    }
    .modal-overlay.open { display: flex; }
    .modal-content {
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 12px;
      max-width: 860px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 32px;
      position: relative;
    }
    .modal-close-btn {
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
    }
    .modal-close-btn:hover {
      color: var(--white);
      border-color: var(--rose);
      background: var(--rose);
    }
    .modal-header h3 {
      font-size: 1.3rem;
      color: var(--gold);
      margin-bottom: 6px;
    }
    .modal-header p {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 20px;
    }
    .modal-body {
      color: var(--white);
      font-size: 0.92rem;
      line-height: 1.65;
    }
    .modal-body h4 {
      color: var(--cyan);
      margin: 18px 0 8px;
      font-size: 1rem;
    }
    .modal-body p {
      color: var(--text-muted);
      margin-bottom: 12px;
    }
    .modal-body ul {
      margin-left: 20px;
      margin-bottom: 16px;
    }
    .modal-body li {
      color: var(--text-muted);
      margin-bottom: 6px;
    }

    footer.site-footer {
      background: var(--bg-card);
      border-top: 1px solid var(--border-muted);
      padding: 24px 32px;
      text-align: center;
      margin-top: 48px;
    }
    footer.site-footer p {
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 6px;
    }
    footer.site-footer span {
      font-size: 0.74rem;
      color: var(--gold-light);
      font-weight: 600;
      letter-spacing: 1px;
    }
  </style>
</head>
<body>

  <header class="top-header">
    <div class="brand-left">
      <h1>HUURS STUDIO</h1>
      <span>SURAH AN-NAML (27) • MASTER CARTOGRAPHY</span>
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
        <h2>Surah An-Naml: The Dominion of Wisdom</h2>
        <p>The definitive visual cartography of Surah 27: from Musa's theophany at the burning bush and the linguistic wisdom of Sulayman to the translocation of Sheba's throne, the five cosmic interrogations, and the fluid passing of mountains under the craftsmanship of Allah.</p>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <div class="val">93</div>
          <div class="lbl">Verses</div>
        </div>
        <div class="stat-box">
          <div class="val">4</div>
          <div class="lbl">Movements</div>
        </div>
        <div class="stat-box">
          <div class="val">64</div>
          <div class="lbl">Cards</div>
        </div>
      </div>
    </section>

    <section class="search-filter-panel">
      <div class="search-input-box">
        <input type="text" id="searchInput" placeholder="Live search across all 64 cards (e.g., 'Sulayman', 'Ants', 'Awzi'ni', 'Sheba', 'Mountains')..." onkeyup="filterCards()">
      </div>
      <div class="quick-modals-bar">
        <button class="modal-trigger-btn" onclick="openModal('modalAnts')">The Ants & Awzi'ni</button>
        <button class="modal-trigger-btn" onclick="openModal('modalSheba')">Sheba & Palace</button>
        <button class="modal-trigger-btn" onclick="openModal('modalCosmic')">Cosmic Questions</button>
        <button class="modal-trigger-btn" onclick="openModal('modalMountains')">Moving Mountains</button>
      </div>
    </section>

    <div class="search-results-stats" id="searchStats" style="display:none; margin-bottom:16px; font-size:0.85rem; color:var(--gold);"></div>

    <nav class="navigation-tabs" id="tabsBar">
      __TAB_BUTTONS__
    </nav>

    <div class="plates-container" id="platesContainer">
      __PLATES_CONTENT__
    </div>

    <section class="movements-section">
      <h3>
        <span>EXEGETICAL THEMATIC MOVEMENTS ROADMAP</span>
        <span style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;">Click any movement to jump to its corresponding plate</span>
      </h3>
      <div class="movement-grid">
        __MOVEMENT_ITEMS__
      </div>
    </section>

  </main>

  <!-- Deep Exegetical Modals -->
  <div class="modal-overlay" id="modalAnts">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModals()">&times;</button>
      <div class="modal-header">
        <h3>The Ant's Pastoral Wisdom & The Sublime Du'a of Awzi'ni</h3>
        <p>Ethics of Pastoral Leadership and Gratitude (Verses 15–19)</p>
      </div>
      <div class="modal-body">
        <h4>1. The Multi-Layered Address of the Female Ant</h4>
        <p>The ant addressed her colony with breathtaking precision: issuing an urgent warning (*La yahtimannakum*), directing them to safe underground chambers (*Masakinakum*), and excusing Sulayman's army of cruelty (*Wa hum la yash'uroon*—exonerating them of intentional harm).</p>
        <h4>2. The Smiles of Wonder & The Awzi'ni Supplication</h4>
        <p>Sulayman smiled in joyful laughter at her speech. Instead of feeling self-satisfied by his vast army, he immediately bowed his soul in gratitude: <i>'Rabbi awzi'ni an ashkura ni'mataka...'</i>—asking Allah to gather his faculties in thanksgiving, bless his parents, and admit him among the righteous.</p>
        <h4>3. Power Subordinated to Mercy</h4>
        <p>The passage demonstrates that true prophetic power does not crush the weak; it hears the whisper of the smallest creature and halts the march of armies to preserve life.</p>
      </div>
    </div>
  </div>

  <div class="modal-overlay" id="modalSheba">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModals()">&times;</button>
      <div class="modal-header">
        <h3>The Diplomatic Missive & The Paved Crystal Palace</h3>
        <p>Geopolitics, Translocation of Power, and Optical Dissolution (Verses 20–44)</p>
      </div>
      <div class="modal-body">
        <h4>1. Strategic Reconnaissance of the Hoopoe</h4>
        <p>The Hoopoe scouted Sheba, discovering a prosperous queen ruling with a magnificent throne (*Laha 'arshun 'adheem*), yet trapped in solar polytheism. Sulayman responded with the imperial letter: <i>'Innahu min Sulaymana wa innahu bismillahir-rahmanir-raheem'</i>.</p>
        <h4>2. The Scholar of the Book vs. The Mighty Jinn</h4>
        <p>When Sulayman challenged his council to bring her throne, the *'Ifrit* offered delivery before he rose from his seat; but the one endowed with Book Knowledge (*'Ilmun minal-kitab*) delivered it in the twinkling of an eye. Sulayman grounded his victory in humility: <i>'Hadha min fadli rabbi li-yabluwani a-ashkuru am akfur'</i>.</p>
        <h4>3. The Dissolution of Polytheistic Illusion</h4>
        <p>Entering the crystal pavilion paved over water (*Sarhun mumarradun min qawareer*), Bilqis mistook glass for deep water. Recognizing that she had similarly mistaken the physical sun for the Divine Light, she surrendered her soul with Sulayman to Allah, Lord of the Worlds.</p>
      </div>
    </div>
  </div>

  <div class="modal-overlay" id="modalCosmic">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModals()">&times;</button>
      <div class="modal-header">
        <h3>The Five Cosmic Interrogations: A-Ilahun Ma'allah?</h3>
        <p>Rhetorical Doxology of Cosmic Creation and Existential Mercy (Verses 60–64)</p>
      </div>
      <div class="modal-body">
        <h4>The Five Unanswered Questions:</h4>
        <ul>
          <li><b>Ecology:</b> Who created the heavens and earth and sprouted magnificent gardens? <i>A-ilahun ma'allah?</i></li>
          <li><b>Geology:</b> Who stabilized the crust, laid rivers, and placed the marine partition (*Hajiz*)? <i>A-ilahun ma'allah?</i></li>
          <li><b>Mercy:</b> Who responds to the desperate soul (*Al-Mudtarr*) when he calls and removes harm? <i>A-ilahun ma'allah?</i></li>
          <li><b>Navigation:</b> Who guides you in the dark lands and seas and sends winds of glad tidings? <i>A-ilahun ma'allah?</i></li>
          <li><b>Sustenance:</b> Who originates life, recreates it, and provides from sky and soil? <i>A-ilahun ma'allah?</i></li>
        </ul>
      </div>
    </div>
  </div>

  <div class="modal-overlay" id="modalMountains">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModals()">&times;</button>
      <div class="modal-header">
        <h3>Sun'allah: The Flawless Craftsmanship of Moving Mountains</h3>
        <p>Geophysical and Eschatological Realities (Verses 87–93)</p>
      </div>
      <div class="modal-body">
        <h4>1. The Mountains Passing Like Clouds</h4>
        <p><i>'Wa tara al-jibala tahsabuha jamidatan wa hiya tamurru marra as-sahab'</i>. The mountains that human eyes perceive as motionless and permanent are moving smoothly like clouds, revealing the dynamic nature of planetary mechanics and cosmic dissolution.</p>
        <h4>2. The Perfection of Divine Craftsmanship</h4>
        <p><i>'Sun'a Allahi alladhi atqana kulla shay''</i>. Allah's artistry is stamped across all creation: He who perfected the intricate anatomy of the ant and the planetary ballet of mountains can effortlessly resurrect mankind.</p>
        <h4>3. The Prophetic Manifesto</h4>
        <p>The surah seals its message with the Prophet's charter: worshiping the Lord of Mecca, living in total surrender, reciting the living Qur'an, and proclaiming: <i>'Al-Hamdu lillah, sa-yureekum ayatihi fa-ta'rifoonaha'</i>.</p>
      </div>
    </div>
  </div>

  <footer class="site-footer">
    <p>Huurs Knowledge Systems • Strict Sunni Islamic Source Discipline • 100% Tier-1 Certified</p>
    <span>READ. REFLECT. RETURN.</span>
  </footer>

  <script>
    function selectPlate(num) {
      document.querySelectorAll('.plate-section').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-chip').forEach(el => el.classList.remove('active'));

      const target = document.getElementById('plateSection' + num);
      if (target) target.classList.add('active');

      const tabs = document.querySelectorAll('.tab-chip');
      if (tabs[num - 1]) tabs[num - 1].classList.add('active');
      window.scrollTo({ top: 320, behavior: 'smooth' });
    }

    function openModal(id) {
      const modal = document.getElementById(id);
      if (modal) modal.classList.add('open');
    }

    function closeModals() {
      document.querySelectorAll('.modal-overlay').forEach(el => el.classList.remove('open'));
    }

    window.onclick = function(event) {
      if (event.target.classList.contains('modal-overlay')) {
        closeModals();
      }
    }

    function filterCards() {
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.card-item');
      const statsBadge = document.getElementById('searchStats');

      if (!query) {
        cards.forEach(c => c.style.display = 'block');
        statsBadge.style.display = 'none';
        return;
      }

      let matchedCount = 0;
      cards.forEach(card => {
        const text = card.getAttribute('data-search') || '';
        if (text.includes(query)) {
          card.style.display = 'block';
          matchedCount++;
        } else {
          card.style.display = 'none';
        }
      });

      statsBadge.style.display = 'block';
      statsBadge.innerHTML = 'Found <b>' + matchedCount + ' Matches</b> for "' + query + '"';
    }

    function filterByMovement(movName) {
      const mapping = {
        "Movement 1": 1,
        "Movement 2": 3,
        "Movement 3": 5,
        "Movement 4": 7
      };
      const targetPlate = mapping[movName] || 1;
      selectPlate(targetPlate);
    }
  </script>
</body>
</html>
"""

full_html = html_template.replace("__TAB_BUTTONS__", tab_buttons_html)
full_html = full_html.replace("__PLATES_CONTENT__", plates_html)
full_html = full_html.replace("__MOVEMENT_ITEMS__", movement_items_html)

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Generated Interactive Digital Suite: {OUTPUT_HTML}")
