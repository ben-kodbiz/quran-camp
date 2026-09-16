#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Ahzab Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Siege of the Trench & The Paragon of Prophecy (Uswatun Hasanah)
    2. The Mothers of the Believers: Ayat al-Takhyir & Ayat al-Tatheer
    3. The Decalogue of Spiritual Parity & Khatam an-Nabiyyeen
    4. Salat 'ala an-Nabi, Ayat al-Jilbab & The Cosmic Trust (Al-Amanah)
- Exegetical Thematic Movements Roadmap
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_AHZAB_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_al_ahzab_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_al_ahzab_html_and_md import pages_data

thematic_movements = [
    ("Movement 1", "The Integrity of Heart, Adoption Abolition & Prophetic Primacy", "Movement 1", "Plate 01"),
    ("Movement 2", "The Crucible of the Trench: Siege of 10,000, Uswah & Divine Gale", "Movement 2", "Plates 02–04"),
    ("Movement 3", "The Mothers of the Believers, Ayat al-Tatheer & Spiritual Parity", "Movement 3", "Plates 05–06"),
    ("Movement 4", "Khatam an-Nabiyyeen, Salat 'ala an-Nabi, Jilbab & The Cosmic Trust", "Movement 4", "Plates 07–08")
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
  <title>Surah Al-Ahzab — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
    .header-badges {{
      display: flex;
      gap: 10px;
    }}
    .badge {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}
    .badge-gold {{ background: rgba(212, 175, 89, 0.12); color: var(--gold); border-color: var(--gold); }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.12); color: var(--cyan); border-color: var(--cyan); }}
    .badge-emerald {{ background: rgba(16, 185, 129, 0.12); color: var(--emerald); border-color: var(--emerald); }}

    .main-container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 28px 24px;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-elevated) 100%);
      border: 1px solid var(--border-muted);
      border-radius: 12px;
      padding: 28px 32px;
      margin-bottom: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
    }}
    .hero-text h2 {{
      font-size: 1.6rem;
      color: var(--gold-light);
      margin-bottom: 8px;
    }}
    .hero-text p {{
      color: var(--text-muted);
      font-size: 0.92rem;
      max-width: 820px;
      line-height: 1.55;
    }}
    .hero-stats {{
      display: flex;
      gap: 20px;
      text-align: center;
    }}
    .stat-box {{
      background: var(--bg-deep);
      border: 1px solid var(--border-muted);
      padding: 12px 18px;
      border-radius: 8px;
      min-width: 90px;
    }}
    .stat-box .val {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--gold);
    }}
    .stat-box .lbl {{
      font-size: 0.72rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .search-filter-panel {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 14px 20px;
      margin-bottom: 24px;
      display: flex;
      gap: 16px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .search-input-box {{
      flex: 1;
      min-width: 260px;
    }}
    .search-input-box input {{
      width: 100%;
      background: var(--bg-deep);
      border: 1px solid var(--border-muted);
      color: var(--text-main);
      padding: 10px 16px;
      border-radius: 6px;
      font-size: 0.88rem;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input-box input:focus {{
      border-color: var(--gold);
    }}
    .search-stats {{
      font-size: 0.82rem;
      color: var(--text-muted);
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
      border-color: rgba(212, 175, 89, 0.4);
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
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}
    .card-title-row h4 {{
      font-size: 0.88rem;
      color: var(--text-main);
      font-weight: 600;
    }}
    .card-points {{
      list-style-type: none;
    }}
    .card-points li {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .thematic-modals-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin: 36px 0;
    }}
    @media (max-width: 1024px) {{
      .thematic-modals-grid {{ grid-template-columns: 1fr 1fr; }}
    }}
    @media (max-width: 600px) {{
      .thematic-modals-grid {{ grid-template-columns: 1fr; }}
    }}
    .modal-trigger-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .modal-trigger-card:hover {{
      border-color: var(--gold);
      transform: translateY(-2px);
    }}
    .mtc-header {{
      font-size: 0.72rem;
      color: var(--gold);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }}
    .mtc-title {{
      font-size: 1rem;
      color: var(--text-main);
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .mtc-desc {{
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 14px;
    }}
    .mtc-cta {{
      font-size: 0.78rem;
      color: var(--gold-light);
      font-weight: 600;
    }}

    .movements-section {{
      background: var(--bg-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 36px;
    }}
    .movements-section h3 {{
      font-size: 1.15rem;
      color: var(--gold-light);
      margin-bottom: 16px;
    }}
    .movement-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 16px;
      border-bottom: 1px solid var(--border-muted);
      cursor: pointer;
      transition: background 0.15s ease;
    }}
    .movement-row:last-child {{
      border-bottom: none;
    }}
    .movement-row:hover {{
      background: var(--bg-elevated);
    }}
    .movement-meta-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .movement-num {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--gold);
      background: var(--bg-deep);
      padding: 4px 8px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}
    .movement-title {{
      font-size: 0.92rem;
      color: var(--text-main);
      font-weight: 600;
      margin-bottom: 2px;
    }}
    .movement-sub {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .movement-tag {{
      font-size: 0.74rem;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.1);
      padding: 4px 8px;
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
      <span>SURAH AL-AHZAB (33) • MASTER CARTOGRAPHY</span>
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
        <h2>Surah Al-Ahzab: The Siege of the Trench & Uswatun Hasanah</h2>
        <p>The definitive visual cartography of Surah 33: from the Two Hearts axiom and the 10,000 confederate siege (Ghazwat al-Khandaq) to the peerless prophetic role model (Uswatun Hasanah), the freezing gale (Reeh Sarsar), Ayat al-Takhyir, the Decalogue of Spiritual Parity (Ayah 35), Khatam an-Nabiyyeen, Ayat al-Jilbab, and the crushing weight of the Cosmic Trust (Al-Amanah).</p>
      </div>
      <div class="hero-stats">
        <div class="stat-box">
          <div class="val">73</div>
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
        <input type="text" id="liveSearchInput" placeholder="Filter through all 64 cards across 8 plates (e.g., Trench, Uswah, Hearts, Gale, Zayd, Zaynab, Khatam, Jilbab, Amanah)..." onkeyup="filterCards()">
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
          <div class="mtc-title">The Crucible of the Trench</div>
          <div class="mtc-desc">The 10,000 confederates, hearts reaching throats, hypocrites exposed, and the Prophet ﷺ as Uswah Hasanah in shared dirt.</div>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>

      <div class="modal-trigger-card" onclick="openModal('modal2')">
        <div>
          <div class="mtc-header">Deep Monograph 02</div>
          <div class="mtc-title">The Mothers of the Believers</div>
          <div class="mtc-desc">Ayat al-Takhyir, 'A'ishah's immediate choice of the Hereafter, domestic decorum, and Ayat al-Tatheer purifying the prophetic house.</div>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>

      <div class="modal-trigger-card" onclick="openModal('modal3')">
        <div>
          <div class="mtc-header">Deep Monograph 03</div>
          <div class="mtc-title">Spiritual Parity & Finality</div>
          <div class="mtc-desc">The ten paired virtues of Ayah 35 for men and women, the marriage of Zaynab, and Muhammad ﷺ as Khatam an-Nabiyyeen.</div>
        </div>
        <div class="mtc-cta">Read Monograph →</div>
      </div>

      <div class="modal-trigger-card" onclick="openModal('modal4')">
        <div>
          <div class="mtc-header">Deep Monograph 04</div>
          <div class="mtc-title">Salat, Jilbab & The Cosmic Trust</div>
          <div class="mtc-desc">The universal command of Salat upon the Prophet ﷺ, the protective outer cloak of Jilbab, and the shuddering mountains declining Al-Amanah.</div>
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
        <h3>The Crucible of the Trench & The Prophetic Paragon</h3>
        <p>Tafsir al-Tabari & Ibn Kathir • Ghazwat al-Khandaq</p>
      </div>
      <div class="modal-body">
        <h4>1. The Terrifying Encirclement</h4>
        <p>In Shawwal 5 AH, a coalition of 10,000 warriors surrounded Medina. Internal treachery from Banu Qurayzah threatened Muslim homes from the rear. The Qur'an captures this extreme trial: <em>Balaghati al-quloobu al-hanajir</em> (hearts reached the throats in violent palpitations) and <em>Zulziloo zilzalan shadeeda</em> (they were shaken with a severe shaking).</p>
        
        <h4>2. Hypocrisy Unmasked</h4>
        <p>Under this intense heat, hypocrites claimed: <em>Inna buyootana 'awrah</em> (Our houses are exposed) to flee the frontlines, mocking the prophetic promises of future civilizational victories.</p>

        <h4>3. Uswatun Hasanah: Shared Hardship</h4>
        <p>Amidst this siege, Allah presents the Messenger ﷺ as the consummate role model: <em>Laqad kana lakum fee Rasoolillahi uswatun hasanah</em>. He wielded the pickaxe, carried soil, strapped stones to his abdomen against hunger, and led with immovable spiritual resolve.</p>
      </div>
    </div>
  </div>

  <!-- Modal 2 -->
  <div class="modal-overlay" id="modal2">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal2')">✕</button>
      <div class="modal-header">
        <h3>The Mothers of the Believers & Ayat al-Tatheer</h3>
        <p>Sahih al-Bukhari 4785 & Sahih Muslim 2424 • Household Sanctity</p>
      </div>
      <div class="modal-body">
        <h4>1. Ayat al-Takhyir: The Verse of Choice</h4>
        <p>When the Prophet's wives requested increased allowances, Allah commanded him to offer them a choice: worldly luxuries accompanied by generous divorce, or remaining with the Messenger in pious austerity for immense eternal reward. 'A'ishah immediately chose Allah and His Messenger, and every wife followed her example.</p>
        
        <h4>2. Ethical Elevation and Domestic Sanctity</h4>
        <p>Because of their station, they were commanded: <em>Fa-la takhda'na bil-qawl</em> (do not speak with flirtatious softness so diseased hearts lust; speak uprightly) and <em>Wa qarna fee buyootikunna</em> (settle gracefully in your homes, shunning the ostentatious display of Jahiliyyah).</p>

        <h4>3. Ayat al-Tatheer</h4>
        <p><em>Innama yureedu Allahu li-yudh-hiba 'ankumu ar-rijsa ahla al-bayti wa yutahhirakum tat-heera</em>: Allah's sovereign intent to remove all spiritual impurity from the Prophet's household and purify them completely.</p>
      </div>
    </div>
  </div>

  <!-- Modal 3 -->
  <div class="modal-overlay" id="modal3">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal3')">✕</button>
      <div class="modal-header">
        <h3>Spiritual Parity & The Seal of Prophethood</h3>
        <p>Jami' at-Tirmidhi 3211 & Sahih al-Bukhari 3535 • Virtue and Culmination</p>
      </div>
      <div class="modal-body">
        <h4>1. The Decalogue of Spiritual Parity (Ayah 35)</h4>
        <p>Responding to Umm Salamah's inquiry, Allah revealed Verse 35 enumerating ten paired virtues for men and women: Islam, Iman, Obedience, Truthfulness, Patience, Humility, Charity, Fasting, Chastity, and Abundant Remembrance. Both receive identical divine forgiveness and immense eternal reward.</p>
        
        <h4>2. Dissolving Adoption Taboos</h4>
        <p>The marriage of Zayd and Zaynab bint Jahsh proved incompatible. After their divorce, Allah divinely ordained her marriage to the Prophet ﷺ to irrevocably shatter the pre-Islamic superstition that marrying the former wife of an adopted son was prohibited.</p>

        <h4>3. Khatam an-Nabiyyeen</h4>
        <p><em>Ma kana Muhammadun aba ahadin min rijalikum wa lakin Rasoola Allahi wa Khatama an-Nabiyyeen</em>: Muhammad is not the father of adult men, but the Messenger of Allah and the final Seal of the Prophets, culminating revelation for all eternity.</p>
      </div>
    </div>
  </div>

  <!-- Modal 4 -->
  <div class="modal-overlay" id="modal4">
    <div class="modal-content">
      <button class="modal-close-btn" onclick="closeModal('modal4')">✕</button>
      <div class="modal-header">
        <h3>Salat 'ala an-Nabi, Ayat al-Jilbab & The Cosmic Trust</h3>
        <p>Sahih al-Bukhari 4797 & Classical Exegesis • Honour, Modesty & Moral Agency</p>
      </div>
      <div class="modal-body">
        <h4>1. Universal Mandate of Salat upon the Prophet</h4>
        <p><em>Inna Allaha wa mala'ikatahu yusalloona 'ala an-Nabi</em>: Allah praises His Messenger in the celestial assembly and angels pray for him. Believers are commanded to join this cosmic chorus, sending blessings and peace upon the teacher of mankind.</p>
        
        <h4>2. Ayat al-Jilbab: The Cloak of Protection</h4>
        <p>Believing women are instructed to draw outer cloaks (Jalabeeb) over themselves when outdoors, establishing an unmistakable aura of dignity and modesty that repels public harassment.</p>

        <h4>3. The Shuddering Cosmos and Al-Amanah</h4>
        <p>In Verses 72–73, the Cosmic Trust (moral agency, free will, and divine commandments) was offered to the heavens, earth, and granite mountains. They shuddered and declined it in holy dread of failing. Man boldly undertook it, proving prone to self-injustice and ignorance, yet those who fulfill the trust are embraced by divine forgiveness and mercy.</p>
      </div>
    </div>
  </div>

  <footer class="site-footer">
    <p>Huurs Knowledge Systems • Deeper Thought Series • Surah Al-Ahzab Master Interactive Suite</p>
    <span>100% Classical Sunni Source Discipline • Read. Reflect. Return.</span>
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
      const cards = document.querySelectorAll('.card-item');
      let matches = 0;

      if (!query) {{
        cards.forEach(c => c.style.display = 'block');
        document.getElementById('searchMatchCount').innerText = 'Showing 64 of 64 cards';
        return;
      }}

      cards.forEach(c => {{
        const text = c.getAttribute('data-search') || '';
        if (text.includes(query)) {{
          c.style.display = 'block';
          matches++;
        }} else {{
          c.style.display = 'none';
        }}
      }});

      document.getElementById('searchMatchCount').innerText = `Showing ${{matches}} of 64 cards`;
    }}

    function filterByMovement(movName) {{
      const plateMap = {{
        'Movement 1': 1,
        'Movement 2': 2,
        'Movement 3': 5,
        'Movement 4': 7
      }};
      if (plateMap[movName]) {{
        selectPlate(plateMap[movName]);
        window.scrollTo({{ top: 380, behavior: 'smooth' }});
      }}
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
    }}
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Successfully generated Surah Al-Ahzab Interactive Suite: {OUTPUT_HTML}")
