#!/usr/bin/env python3
"""
Huurs Studio - Surah Saba Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Dynasty of Gratitude: Dawud's Molten Iron & Sulayman's Subjugated Winds
    2. The Staff of Solomon, The Terminal Termite & Occult Demolition
    3. The Civilization of Saba: The Dam of Ma'rib & The Sin of Proximity Fatigue
    4. Angelic Dread, Severing Shirk & The Solitary Awakening
- Exegetical Thematic Movements Roadmap
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_SABA_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_saba_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_saba_html_and_md import pages_data

thematic_movements = [
    ("Movement 1", "The Cosmic Hamd & The Omniscience of the Atom's Weight", "Movement 1", "Plates 01–02"),
    ("Movement 2", "The Dynasty of Gratitude: Dawud's Iron & Sulayman's Winds", "Movement 2", "Plates 03–04"),
    ("Movement 3", "The Staff of Solomon & The Demolition of Occult Superstition", "Movement 3", "Plate 05"),
    ("Movement 4", "The Rise and Fall of Saba: The Burst Dam & Proximity Fatigue", "Movement 4", "Plates 06–07"),
    ("Movement 5", "Angelic Awe, The Solitary Path & The Final Partition", "Movement 5", "Plate 08")
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
  <title>Surah Saba — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
  <style>
    :root {{
      --bg-deep: #060A12;
      --bg-card: #0D1422;
      --bg-elevated: #141E32;
      --gold: #D4AF59;
      --gold-light: #E8D194;
      --cyan: #38BDF8;
      --purple: #A855F7;
      --emerald: #10B981;
      --rose: #F43F5E;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --border-muted: #26354D;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg-deep);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
      line-height: 1.5;
    }}
    header.top-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--bg-card);
      border-bottom: 2px solid var(--border-muted);
      padding: 18px 32px;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .brand-left h1 {{
      font-size: 1.35rem;
      color: var(--gold);
      letter-spacing: 1.5px;
      font-weight: 800;
    }}
    .brand-left span {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 500;
    }}
    .nav-actions {{
      display: flex;
      gap: 12px;
      align-items: center;
    }}
    .btn-action {{
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      color: var(--text-main);
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .btn-action:hover {{
      border-color: var(--gold);
      color: var(--gold);
    }}
    .btn-gold {{
      background: var(--gold);
      color: var(--bg-deep);
      border-color: var(--gold);
    }}
    .btn-gold:hover {{
      background: var(--gold-light);
      color: var(--bg-deep);
    }}

    main.container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 32px 24px;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, rgba(13, 20, 34, 0.95), rgba(20, 30, 50, 0.85));
      border: 1px solid var(--border-muted);
      border-left: 5px solid var(--gold);
      border-radius: 10px;
      padding: 28px 32px;
      margin-bottom: 32px;
    }}
    .hero-banner h2 {{
      font-size: 1.8rem;
      color: var(--text-main);
      margin-bottom: 8px;
    }}
    .hero-banner p {{
      color: var(--text-muted);
      font-size: 0.95rem;
      max-width: 1000px;
      line-height: 1.6;
    }}

    .search-filter-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .search-filter-box input {{
      flex: 1;
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 16px;
      color: var(--text-main);
      font-size: 0.92rem;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-filter-box input:focus {{
      border-color: var(--gold);
    }}
    .search-count {{
      font-size: 0.82rem;
      color: var(--gold);
      font-weight: 600;
      white-space: nowrap;
    }}

    .modals-bar {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-bottom: 28px;
    }}
    @media (max-width: 1024px) {{
      .modals-bar {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
      .modals-bar {{ grid-template-columns: 1fr; }}
    }}
    .modal-trigger-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 14px 16px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .modal-trigger-card:hover {{
      border-color: var(--gold);
      transform: translateY(-2px);
    }}
    .mtc-tag {{
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 6px;
    }}
    .mtc-tag.cyan {{ color: var(--cyan); }}
    .mtc-tag.purple {{ color: var(--purple); }}
    .mtc-tag.gold {{ color: var(--gold); }}
    .mtc-tag.emerald {{ color: var(--emerald); }}
    .modal-trigger-card h4 {{
      font-size: 0.92rem;
      color: var(--text-main);
      margin-bottom: 4px;
    }}
    .modal-trigger-card p {{
      font-size: 0.76rem;
      color: var(--text-muted);
      line-height: 1.4;
      margin-bottom: 8px;
    }}
    .mtc-cta {{
      font-size: 0.74rem;
      color: var(--gold);
      font-weight: 600;
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
      padding: 9px 16px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .tab-chip:hover {{
      border-color: var(--gold);
      color: var(--text-main);
    }}
    .tab-chip.active {{
      background: var(--gold);
      color: var(--bg-deep);
      border-color: var(--gold);
    }}

    .plate-section {{
      display: none;
    }}
    .plate-section.active {{
      display: block;
    }}
    .plate-title-bar {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 24px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}
    .plate-title-bar h2 {{
      font-size: 1.3rem;
      color: var(--text-main);
      margin-bottom: 4px;
    }}
    .plate-title-bar p {{
      font-size: 0.84rem;
      color: var(--text-muted);
    }}
    .plate-badge-box {{
      display: flex;
      gap: 8px;
      flex-shrink: 0;
    }}

    .pillars-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 32px;
    }}
    @media (max-width: 960px) {{
      .pillars-layout {{ grid-template-columns: 1fr; }}
    }}

    .pillar-box {{
      background: var(--bg-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px;
    }}
    .pillar-bar {{
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 10px;
      margin-bottom: 14px;
    }}
    .pillar-bar h3 {{
      font-size: 1.05rem;
      margin-bottom: 4px;
    }}
    .pillar-bar.cyan h3 {{ color: var(--cyan); }}
    .pillar-bar.purple h3 {{ color: var(--purple); }}
    .pillar-bar.emerald h3 {{ color: var(--emerald); }}
    .pillar-bar.gold h3 {{ color: var(--gold); }}
    .pillar-bar.rose h3 {{ color: var(--rose); }}
    .pillar-bar p {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}

    .cards-wrapper {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .card-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 14px 16px;
      transition: all 0.2s ease;
    }}
    .card-item:hover {{
      border-color: var(--gold);
      transform: translateY(-2px);
    }}
    .card-title-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .card-idx {{
      background: var(--bg-elevated);
      color: var(--gold);
      font-size: 0.74rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}
    .card-title-row h4 {{
      font-size: 0.92rem;
      color: var(--text-main);
      font-weight: 600;
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

    .movements-section {{
      margin-top: 48px;
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 10px;
      padding: 24px 30px;
    }}
    .movements-section h3 {{
      font-size: 1.2rem;
      color: var(--gold);
      margin-bottom: 18px;
    }}
    .movement-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 16px;
      border-bottom: 1px solid var(--border-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .movement-row:last-child {{ border-bottom: none; }}
    .movement-row:hover {{
      background: var(--bg-elevated);
    }}
    .movement-meta-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .movement-num {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--gold);
      opacity: 0.8;
      width: 28px;
    }}
    .movement-title {{
      font-size: 0.95rem;
      color: var(--text-main);
      font-weight: 600;
      margin-bottom: 2px;
    }}
    .movement-sub {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .movement-tag {{
      background: var(--bg-elevated);
      color: var(--cyan);
      font-size: 0.72rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid rgba(56, 189, 248, 0.2);
    }}

    /* Modal Overlay */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(4px);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }}
    .modal-overlay.open {{
      display: flex;
    }}
    .modal-content {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 12px;
      max-width: 820px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 32px;
      position: relative;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
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
      transition: all 0.2s ease;
    }}
    .modal-close-btn:hover {{
      color: var(--text-main);
      border-color: var(--gold);
    }}
    .modal-header h3 {{
      font-size: 1.4rem;
      color: var(--gold-light);
      margin-bottom: 6px;
    }}
    .modal-header p {{
      font-size: 0.82rem;
      color: var(--cyan);
      margin-bottom: 20px;
    }}
    .modal-body h4 {{
      font-size: 1.05rem;
      color: var(--text-main);
      margin-top: 18px;
      margin-bottom: 6px;
    }}
    .modal-body p {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 14px;
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
      <span>SURAH SABA (34) • MASTER CARTOGRAPHY</span>
    </div>
    <div class="nav-actions">
      <a href="../07_MINDMAP/SABA_MASTER_MINDMAP.html" class="btn-action" target="_blank">Mindmap View ↗</a>
      <a href="SURAH_SABA_MASTER_COMPENDIUM.pdf" class="btn-action btn-gold" target="_blank">Compendium PDF ↗</a>
    </div>
  </header>

  <main class="container">

    <section class="hero-banner">
      <h2>SURAH SABA: THE DYNASTY OF GRATITUDE & CIVILIZATIONAL COLLAPSE</h2>
      <p>The definitive 8-plate visual and analytical cartography detailing the Cosmic Hamd, The Omniscience of the Atom's Weight (Mithqala Dharrah), Dawud's Singing Mountains & Malleable Iron, Sulayman's Subjugated Winds & Molten Copper, The Terminal Termite Demystifying the Occult, The Two Gardens of Ma'rib & The Flood of 'Arim, The Sin of Proximity Fatigue, and The Solitary Reflection.</p>
    </section>

    <!-- Deep Exegetical Modals Bar -->
    <div class="modals-bar">
      <div class="modal-trigger-card" onclick="openModal('modal1')">
        <div>
          <span class="mtc-tag cyan">Theological Archetype</span>
          <h4>The Dynasty of Gratitude</h4>
          <p>Dawud's Singing Mountains, Malleable Iron & Sulayman's Winds.</p>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>
      <div class="modal-trigger-card" onclick="openModal('modal2')">
        <div>
          <span class="mtc-tag purple">Occult Demolition</span>
          <h4>Solomon's Staff & The Termite</h4>
          <p>Silent Departure in Prayer & Exposing Jinn Blindness to Ghayb.</p>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>
      <div class="modal-trigger-card" onclick="openModal('modal3')">
        <div>
          <span class="mtc-tag emerald">Civilizational Ruin</span>
          <h4>The Two Gardens & Burst Dam</h4>
          <p>Baldatun Tayyibah, Sayl al-'Arim & The Sin of Proximity Fatigue.</p>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>
      <div class="modal-trigger-card" onclick="openModal('modal4')">
        <div>
          <span class="mtc-tag gold">Epistemic Protocol</span>
          <h4>Angelic Awe & Solitude</h4>
          <p>Severing 4 Roots of Shirk, Trembling Angels & The Solitary Path.</p>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>
    </div>

    <!-- Search / Filter -->
    <div class="search-filter-box">
      <input type="text" id="liveSearchInput" placeholder="Search across all 64 cards (e.g., 'iron', 'termite', 'Marib', 'Arim', 'wind', 'gratitude', 'angels')..." oninput="filterCards()">
      <span class="search-count" id="searchCountBadge">64 Cards Available</span>
    </div>

    <!-- Tab Strip -->
    <div class="tab-strip" id="tabStrip">
      {tab_buttons_html}
    </div>

    <!-- Plates Content -->
    {plates_html}

    <!-- Thematic Roadmap Section -->
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
        <h3>The Dynasty of Gratitude: Dawud's Molten Iron & Sulayman's Winds</h3>
        <p>Tafsir al-Tabari & Ibn Kathir • The House of David</p>
      </div>
      <div class="modal-body">
        <h4>1. Symphonic Praises of the Natural World</h4>
        <p>Allah bestowed upon David (Dawud عليه السلام) a peerless acoustic miracle: <em>Ya jibalu awwibee ma'ahu wat-tayr</em>. When David chanted from the Psalms (Zabur), towering granite mountains and airborne birds halted their motion, resonating in symphonic praise with his voice. The physical universe is intrinsically conscious and worshipping, joining the voice of the human servant aligned with the Creator.</p>
        
        <h4>2. Malleable Iron & Defensive Metallurgy</h4>
        <p><em>Wa alanna lahu al-hadeed</em>: Solid iron became soft as dough or wax in David's bare hands without fire or forge. Rather than manufacturing imperial offensive weapons, he was commanded to weave flexible chain mail (<em>Sabighat</em>) with balanced interlocking links (<em>Qaddir fis-sard</em>), establishing the moral ethics of defense and the sacred dignity of manual labor.</p>

        <h4>3. The Monthly Flight & Fluid Copper</h4>
        <p>Solomon was given the wind covering a month's march between dawn and midday, and a subterranean fountain of molten copper (<em>'Ayn al-Qitr</em>) flowing like liquid water. Yet the divine command was not self-glorification, but active devotion: <em>I'maloo Ala Dawooda Shukra</em> ("Work, O family of David, in gratitude!"). Gratitude in Islam is an active imperative verb.</p>
      </div>
    </div>
  </div>

  <!-- Modal 2 -->
  <div class="modal-overlay" id="modal2">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal2')">✕</button>
      <div class="modal-header">
        <h3>Solomon's Staff, The Terminal Termite & Occult Demolition</h3>
        <p>Tafsir al-Qurtubi & Ibn Kathir • Debunking Jinn Omniscience</p>
      </div>
      <div class="modal-body">
        <h4>1. The Mortal Departure in Prayer</h4>
        <p>Solomon passed away while standing propped upright against his walking staff (<em>Minsa'ah</em>) inside his glass sanctuary. Outside, the conscripted Jinn continued in agonizing, backbreaking servitude for months, terrified by the motionless silhouette of the king whom they believed was continuously watching over them.</p>
        
        <h4>2. The Wood-Boring Insect (Dabbat al-Ard)</h4>
        <p>An infinitesimal creature—a wood-boring termite (<em>Al-Aradah</em>)—burrowed into the core of the staff, consuming the cellulose fibers grain by grain. When the hollowed wood fractured under the king's weight, his body collapsed to the earth (<em>Kharra</em>).</p>

        <h4>3. The Permanent Theological Liberation</h4>
        <p><em>Law kanoo ya'lamoona al-ghayb ma labithoo fil-'adhabi al-muheen</em>: Had the Jinn known the unseen, they would never have remained in humiliating torment serving a corpse! This dramatic historical event forever shattered pagan superstitions, astrology, and fear of occult spirits. Knowledge of the Unseen belongs exclusively to Allah.</p>
      </div>
    </div>
  </div>

  <!-- Modal 3 -->
  <div class="modal-overlay" id="modal3">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal3')">✕</button>
      <div class="modal-header">
        <h3>The Civilization of Saba: The Dam of Ma'rib & Proximity Fatigue</h3>
        <p>Tafsir al-Tabari & 'Uddat as-Sabirin • The Archaeology of Decline</p>
      </div>
      <div class="modal-body">
        <h4>1. Baldatun Tayyibah: The Hydraulic Paradise</h4>
        <p>The kingdom of Saba at Ma'rib was blessed with a monumental stone dam feeding twin garden valleys on the right and left (<em>Jannatani 'an yameenin wa shimal</em>). The microclimate was so pure that pests and sickness were unknown, and sweet fruit dropped spontaneously into carried baskets.</p>
        
        <h4>2. The Cataclysm of Sayl al-'Arim</h4>
        <p>When Saba turned away in self-satisfaction and attributed their prosperity to their own commercial prowess, burrowing rodents undermined the stone foundations of the Great Dam. Monsoon torrents burst the structure in a catastrophic tidal wave, transforming their lush orchards into barren scrubland bearing only bitter shrubs (<em>Khamt</em>), tamarisk (<em>Athl</em>), and sparse thorns (<em>Sidr qaleel</em>).</p>

        <h4>3. The Sin of Proximity Fatigue</h4>
        <p>Allah had linked Yemen to Syria with unbroken, visible settlements (<em>Quran zahirah</em>) where travelers moved safely day and night. But elite merchant cartels grew bored of egalitarian security and prayed: <em>Rabbana ba'id bayna asfarina</em> ("Lengthen our journeys!"), wishing for harsh deserts to monopolize prices. Allah destroyed their roads and scattered their tribes across Arabia into mere campfire folklore (<em>Ahadeeth</em>).</p>
      </div>
    </div>
  </div>

  <!-- Modal 4 -->
  <div class="modal-overlay" id="modal4">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal4')">✕</button>
      <div class="modal-header">
        <h3>Angelic Awe, Severing Shirk & The Solitary Awakening</h3>
        <p>Sahih al-Bukhari 4701 & Mafatih al-Ghayb • Epistemic Sincerity</p>
      </div>
      <div class="modal-body">
        <h4>1. The Four Cords of Shirk Severed (Verse 22)</h4>
        <p>Imam Ibn al-Qayyim notes that Verse 22 severs all four roots of polytheism: false gods possess not an atom's weight in heaven or earth (zero independent ownership), share zero partnership in creation, offer zero assistance to the Almighty, and possess zero autonomous intercession.</p>
        
        <h4>2. Angelic Dread at Divine Speech</h4>
        <p>In <em>Sahih al-Bukhari</em> 4701, when Allah decrees an affair in heaven, archangels strike their wings in awe like an iron chain dragged over smooth stone, collapsing in prostration. When terror subsides from their hearts (<em>Hatta idha fuzzi'a 'an quloobihim</em>), they ask Gabriel: <em>"What has your Lord said?"</em> Gabriel replies: <em>"Al-Haqq (The Truth)!"</em> If archangels tremble before divine words, how grotesque is it for mortal humans to worship stones or dead men?</p>

        <h4>3. The Protocol of Solitary Sincerity (Verse 46)</h4>
        <p><em>Qul innama a'idukum bi-wahidah: an taqoomoo lillahi mathna wa furada thumma tatafakkaroo</em>: Step away from the noise of the mob. Stand up for Allah alone or in pairs, and reflect with intellectual honesty. The truth of divine revelation and the integrity of the Prophet ﷺ shine with undeniable clarity when freed from herd mentality.</p>
      </div>
    </div>
  </div>

  <footer class="site-footer">
    <p>HUURS STUDIO SACRED MEDIA CAMPAIGN • SURAH SABA MASTER INTERACTIVE SUITE</p>
    <span>READ. REFLECT. RETURN.</span>
  </footer>

  <script>
    function selectPlate(pageNumber) {{
      document.querySelectorAll('.plate-section').forEach(sec => sec.classList.remove('active'));
      document.querySelectorAll('.tab-chip').forEach(btn => btn.classList.remove('active'));
      
      const target = document.getElementById('plateSection' + pageNumber);
      if (target) {{
        target.classList.add('active');
      }}
      const buttons = document.querySelectorAll('.tab-chip');
      if (buttons[pageNumber - 1]) {{
        buttons[pageNumber - 1].classList.add('active');
      }}
    }}

    function filterCards() {{
      const q = document.getElementById('liveSearchInput').value.toLowerCase().trim();
      const allCards = document.querySelectorAll('.card-item');
      let visibleCount = 0;

      if (!q) {{
        allCards.forEach(c => c.style.display = 'block');
        document.getElementById('searchCountBadge').innerText = '64 Cards Available';
        return;
      }}

      allCards.forEach(c => {{
        const hay = c.getAttribute('data-search') || '';
        if (hay.includes(q)) {{
          c.style.display = 'block';
          visibleCount++;
        }} else {{
          c.style.display = 'none';
        }}
      }});

      document.getElementById('searchCountBadge').innerText = visibleCount + ' Cards Matched';
    }}

    function filterByMovement(movName) {{
      let targetPage = 1;
      if (movName === 'Movement 1') targetPage = 1;
      else if (movName === 'Movement 2') targetPage = 3;
      else if (movName === 'Movement 3') targetPage = 5;
      else if (movName === 'Movement 4') targetPage = 6;
      else if (movName === 'Movement 5') targetPage = 8;
      selectPlate(targetPage);
      window.scrollTo({{ top: document.getElementById('plateSection' + targetPage).offsetTop - 80, behavior: 'smooth' }});
    }}

    function openModal(id) {{
      const el = document.getElementById(id);
      if (el) el.classList.add('open');
    }}

    function closeModal(id) {{
      const el = document.getElementById(id);
      if (el) el.classList.remove('open');
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

print(f"[OK] Generated Surah Saba Interactive Suite HTML: {OUTPUT_HTML}")
