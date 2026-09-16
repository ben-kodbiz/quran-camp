#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-A'raf Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals (Libas at-Taqwa, Ashab al-A'raf, Sinai Theophany, Primordial Mithaq)
- 22-Lecture Foundation Audio Syllabus Explorer
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_ARAF_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_al_araf_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_al_araf_html_and_md import pages_data

# 22 Audio Foundation lectures syllabus
audio_lectures = [
    ("7.Al-araf1-6.opus", "Book Revealed, No Constriction & Absolute Scales of Truth", "Movement 1", "22m"),
    ("7.Al-araf7-15.opus", "Creation of Adam, Iblis's Pride (Fire vs Clay) & Respite Granted", "Movement 1", "22m"),
    ("7.Al-araf16-21.opus", "Ambush on the Straight Path & Whispering at the Forbidden Tree", "Movement 1", "22m"),
    ("7.Al-araf22-26.opus", "Exposed Vulnerability, Rabbana Zalamna & Libas at-Taqwa", "Movement 1", "24m"),
    ("7.Al-araf27-31.opus", "Warning to Bani Adam, Rebutting Naked Rituals & Zeenah at Masjid", "Movement 2", "20m"),
    ("7.Al-araf32-43.opus", "Lawful Provisions, Recriminations in Fire & Cleansing Malice in Jannah", "Movement 2", "23m"),
    ("7.Al-araf44-53.opus", "Dwellers of Jannah Call the Fire, Ashab al-A'raf & Cry for Water", "Movement 3", "21m"),
    ("7.Al-araf54-64.opus", "Hexaemeron Creation, Istawa 'alal-'Arsh, Adab of Du'a & Nuh's Naseehah", "Movement 4", "20m"),
    ("7.Al-araf65-79.opus", "Hud to 'Ad, Salih to Thamud, Miraculous She-Camel & The Rajfah", "Movement 4", "20m"),
    ("7.Al-araf80-85.opus", "Lut Rebukes Moral Degeneracy, Brimstone Rain & Shu'ayb's Call", "Movement 5", "21m"),
    ("7.Al-araf86-99.opus", "Honest Measures, Threats of Exile, Destruction of Madyan & Makr Allah", "Movement 5", "24m"),
    ("7.Al-araf100-103.opus", "Lessons of Destroyed Civilizations & Commissioning of Musa", "Movement 6", "19m"),
    ("7.Al-araf104-122.opus", "Musa Confronts Fir'awn, Radiant Hand & Sorcerers Fall in Sujood", "Movement 6", "18m"),
    ("7.Al-araf123-131.opus", "Fir'awn Threatens Crucifixion, Defiant Faith & Years of Drought", "Movement 6", "19m"),
    ("7.Al-araf132-141.opus", "The Five Plagues, Drowning of Fir'awn & Legacy to the Oppressed", "Movement 6", "20m"),
    ("7.Al-araf142-149.opus", "Forty Nights of Sinai, Rabbi Arini, Pulverized Mountain & Tablets", "Movement 7", "21m"),
    ("7.Al-araf150-158.opus", "Musa's Indignation, The Lowing Calf, 70 Elders & The Ummi Prophet", "Movement 7", "23m"),
    ("7.Al-araf159-167.opus", "Twelve Springs, Gate of Hittah, Sabbath-Breakers & Despised Apes", "Movement 8", "18m"),
    ("7.Al-araf168-174.opus", "Mountain Raised Like Canopy & Primordial Covenant (Alastu bi-Rabbikum)", "Movement 8", "20m"),
    ("7.Al-araf175-180.opus", "Parable of the Panting Dog (Apostate Scholar) & Deadened Hearts", "Movement 8", "19m"),
    ("7.Al-araf181-199.opus", "The Ninety-Nine Beautiful Names, Sudden Hour & Impotence of Idols", "Movement 8", "23m"),
    ("7.Al-araf200-206final.opus", "Refuge from Whispers, Silent Quranic Adab & The Universal Sajdah", "Movement 8", "23m")
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

# Audio list HTML
audio_items_html = ""
for idx, (filename, title, mov, dur) in enumerate(audio_lectures, start=1):
    audio_items_html += f"""
    <div class="audio-row" onclick="filterByMovement('{mov}')">
      <div class="audio-meta-left">
        <span class="audio-num">{idx:02d}</span>
        <div>
          <div class="audio-title">{title}</div>
          <div class="audio-sub">{filename} &bull; {mov}</div>
        </div>
      </div>
      <span class="audio-duration">{dur}</span>
    </div>"""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-A'raf — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
      line-height: 1.5;
      padding: 20px;
    }}
    .suite-shell {{
      max-width: 1480px;
      margin: 0 auto;
    }}
    header.suite-header {{
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
      gap: 16px;
    }}
    .header-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .header-brand h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.05em;
    }}
    .header-brand span {{
      color: var(--text-muted);
      font-size: 0.9rem;
      border-left: 1px solid var(--border-muted);
      padding-left: 12px;
    }}
    .header-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .btn {{
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: none;
    }}
    .btn-gold {{
      background: var(--gold);
      color: var(--navy-deep);
    }}
    .btn-gold:hover {{
      background: var(--gold-light);
    }}
    .btn-outline {{
      background: var(--navy-elevated);
      color: var(--white);
      border: 1px solid var(--border-muted);
    }}
    .btn-outline:hover {{
      border-color: var(--gold);
      color: var(--gold);
    }}
    .controls-bar {{
      display: flex;
      gap: 14px;
      margin-bottom: 20px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .search-input-wrap {{
      flex: 1;
      min-width: 260px;
      position: relative;
    }}
    .search-input-wrap input {{
      width: 100%;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 16px 10px 38px;
      color: var(--white);
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input-wrap input:focus {{
      border-color: var(--gold);
    }}
    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.9rem;
    }}
    .stats-badge {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 9px 16px;
      font-size: 0.82rem;
      color: var(--gold-light);
      display: flex;
      gap: 16px;
    }}
    .stats-badge strong {{
      color: var(--white);
    }}
    .nav-tabs-scroll {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 12px;
      margin-bottom: 20px;
    }}
    .nav-tabs-scroll::-webkit-scrollbar {{
      height: 4px;
    }}
    .nav-tabs-scroll::-webkit-scrollbar-thumb {{
      background: var(--border-muted);
      border-radius: 4px;
    }}
    .tab-chip {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 8px 14px;
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .tab-chip:hover {{
      color: var(--white);
      border-color: var(--gold);
    }}
    .tab-chip.active {{
      background: var(--navy-elevated);
      color: var(--gold);
      border-color: var(--gold);
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
    }}
    .plate-section {{
      display: none;
    }}
    .plate-section.active {{
      display: block;
    }}
    .plate-title-bar {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .plate-title-bar h2 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--gold-light);
      letter-spacing: 0.04em;
    }}
    .plate-title-bar p {{
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-top: 3px;
    }}
    .plate-badge-box {{
      display: flex;
      gap: 8px;
    }}
    .badge-gold {{
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
    }}
    .badge-emerald {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--emerald);
      color: var(--emerald);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
    }}
    .pillars-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}
    @media (max-width: 960px) {{
      .pillars-layout {{
        grid-template-columns: 1fr;
      }}
    }}
    .pillar-box {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }}
    .pillar-bar {{
      padding: 12px 18px;
      border-bottom: 1px solid var(--border-muted);
    }}
    .pillar-bar.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-bar.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-bar.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-bar.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-bar.rose {{ border-top: 3px solid var(--rose); }}
    .pillar-bar h3 {{
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--white);
      letter-spacing: 0.03em;
    }}
    .pillar-bar p {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}
    .cards-wrapper {{
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .card-item {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 16px;
      transition: all 0.2s ease;
    }}
    .card-item:hover {{
      border-color: var(--gold);
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    .card-title-row {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .card-idx {{
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .card-item h4 {{
      font-size: 0.88rem;
      font-weight: 700;
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
      margin-bottom: 4px;
      position: relative;
      padding-left: 14px;
    }}
    .card-points li::before {{
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 0.8rem;
      top: -1px;
    }}
    .audio-section {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px;
      margin-top: 30px;
      margin-bottom: 40px;
    }}
    .audio-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 12px;
    }}
    .audio-header h3 {{
      font-size: 1.05rem;
      color: var(--gold-light);
    }}
    .audio-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }}
    @media (max-width: 860px) {{
      .audio-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .audio-row {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .audio-row:hover {{
      border-color: var(--gold);
      background: rgba(212, 175, 55, 0.06);
    }}
    .audio-meta-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .audio-num {{
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border-radius: 4px;
      padding: 2px 6px;
    }}
    .audio-title {{
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--white);
    }}
    .audio-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
    }}
    .audio-duration {{
      font-size: 0.76rem;
      color: var(--gold);
      font-weight: 600;
      padding-left: 8px;
    }}
    .modal-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(4px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-backdrop.show {{
      display: flex;
    }}
    .modal-window {{
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 10px;
      max-width: 820px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      position: relative;
      animation: modalSlide 0.25s ease-out;
    }}
    @keyframes modalSlide {{
      from {{ transform: translateY(20px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}
    .modal-header {{
      background: var(--navy-elevated);
      padding: 16px 24px;
      border-bottom: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 10;
    }}
    .modal-header h3 {{
      color: var(--gold-light);
      font-size: 1.15rem;
    }}
    .modal-close {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
      line-height: 1;
    }}
    .modal-close:hover {{
      color: var(--white);
    }}
    .modal-body {{
      padding: 24px;
      color: var(--text-muted);
      font-size: 0.9rem;
      line-height: 1.7;
    }}
    .modal-body h4 {{
      color: var(--white);
      margin-top: 16px;
      margin-bottom: 8px;
      font-size: 1.02rem;
    }}
    .modal-body p {{
      margin-bottom: 12px;
    }}
    .modal-body ul {{
      padding-left: 20px;
      margin-bottom: 14px;
    }}
    .modal-body li {{
      margin-bottom: 6px;
    }}
    .quote-box {{
      border-left: 3px solid var(--gold);
      background: var(--navy-elevated);
      padding: 12px 18px;
      border-radius: 0 6px 6px 0;
      margin: 14px 0;
      font-style: italic;
      color: var(--white);
    }}
    footer.suite-footer {{
      border-top: 1px solid var(--border-muted);
      padding: 24px 0;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.8rem;
    }}
    footer.suite-footer p {{
      margin-bottom: 4px;
    }}
  </style>
</head>
<body>

  <div class="suite-shell">
    <header class="suite-header">
      <div class="header-brand">
        <h1>SURAH AL-A'RAF</h1>
        <span>Master Cartography & Exegetical Suite</span>
      </div>
      <div class="header-actions">
        <button class="btn btn-outline" onclick="openModal('garmentModal')">Libas at-Taqwa</button>
        <button class="btn btn-outline" onclick="openModal('heightsModal')">Ashab al-A'raf</button>
        <button class="btn btn-outline" onclick="openModal('sinaiModal')">Sinai Theophany</button>
        <button class="btn btn-outline" onclick="openModal('mithaqModal')">Primordial Mithaq</button>
        <a href="SURAH_AL_ARAF_MASTER_COMPENDIUM.pdf" class="btn btn-gold" target="_blank">Download Master PDF</a>
      </div>
    </header>

    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Live search 64 analytical cards across all 8 plates (e.g., Adam, Iblis, Taqwa, Heights, Musa, Mithaq)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="stats-badge" id="statsBadge">
        <span>Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>22</b> Lectures &bull; <b>100%</b> Sunni Verified</span>
      </div>
    </div>

    <nav class="nav-tabs-scroll" id="tabsBar">
      {tab_buttons_html}
    </nav>

    <main id="platesContainer">
      {plates_html}
    </main>

    <section class="audio-section">
      <div class="audio-header">
        <h3>Foundation Audio Syllabus (22 Expository Lectures &bull; 07h 41m 17s)</h3>
        <span style="font-size:0.8rem; color:var(--text-muted);">Click any lecture to explore its thematic movement</span>
      </div>
      <div class="audio-grid">
        {audio_items_html}
      </div>
    </section>

    <footer class="suite-footer">
      <p><strong>Huurs Studio</strong> &bull; Quranic Cartography & Authentic Sunni Classical Knowledge Architecture</p>
      <p>Exegetical Foundations: Imam at-Tabari, Al-Qurtubi, Ibn Kathir, Fakhr ad-Din ar-Razi, Al-Baghawi</p>
      <p>Operating Standard: Read. Reflect. Return. &bull; Strict Zero-Ayah-Number & Zero-Contemporary-Speaker Law</p>
    </footer>
  </div>

  <!-- MODAL 1: Libas at-Taqwa -->
  <div class="modal-backdrop" id="garmentModal" onclick="closeOnBackdrop(event, 'garmentModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Garment of Piety (Libas at-Taqwa) & Sacred Modesty</h3>
        <button class="modal-close" onclick="closeModal('garmentModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "O children of Adam, We have bestowed upon you clothing to conceal your private parts and as adornment; but the clothing of righteousness—that is best. That is from the signs of Allah that perhaps they will remember."
        </div>
        <h4>The Threefold Architecture of Clothing</h4>
        <p>Classical authorities (Ibn Abbas, Imam at-Tabari, and Ibn Kathir) extract three distinct dimensions of clothing bestowed upon humanity: baseline concealment (<em>Satr</em>), aesthetic beauty and comfort (<em>Reesh</em>), and the supreme inner garment: <strong>Libas at-Taqwa</strong> (the clothing of God-consciousness, moral modesty, and righteous conduct).</p>
        <h4>Satan's Ancient Strategy: Stripping Modesty</h4>
        <p>Revelation explicitly connects the devil's primordial ambush in the Garden—deceiving Adam and Hawwa into tasting from the forbidden tree so their private vulnerability would be exposed—with modern assaults on human dignity. Exposing nakedness is not liberation; it is the ancient trap of Iblis designed to strip humanity of its angelic decorum.</p>
        <h4>Decorum at the Sanctuary: Khudhoo Zeenatakum</h4>
        <p>Islam decisively abolished the pre-Islamic pagan ritual where pilgrims were forced to perform Tawaf around the Ka'bah naked under the guise of false asceticism. Revelation established that taking one's adornment (clean, beautiful attire) at every place of prayer and enjoying wholesome lawful food and drink are intrinsic acts of Islamic worship.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: Ashab al-A'raf -->
  <div class="modal-backdrop" id="heightsModal" onclick="closeOnBackdrop(event, 'heightsModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Men on the Heights (Ashab al-A'raf) & The Vaulted Bridge</h3>
        <button class="modal-close" onclick="closeModal('heightsModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And between them will be a partition, and on the heights are men who recognize all by their mark. And they call out to the companions of Paradise, 'Peace be upon you.' They have not [yet] entered it, but they long [to do so]... And when their eyes are turned toward the companions of the Fire, they say, 'Our Lord, do not place us with the wrongdoing people!'"
        </div>
        <h4>The Identity of the Men on the Heights</h4>
        <p>According to the consensus of the Sahabah (narrated from Ibn Abbas, Ibn Mas'ud, and Hudhayfah by Imam at-Tabari), <em>Ashab al-A'raf</em> are believers whose good deeds and sins weighed exactly equal upon the cosmic Scales. Their good deeds rescued them from falling into Hell, yet their shortcomings deferred their immediate admission into Paradise.</p>
        <h4>The Agony of the Ramparts</h4>
        <p>Standing upon the elevated barrier dividing the cosmos, they gaze upon the radiance, rivers, and fragrance of Paradise with overwhelming longing (<em>Tama'</em>), greeting its dwellers with peace. Yet when their vision turns involuntarily toward the roars and black smoke of Hellfire, they recoil in sheer terror, pleading: <em>"Our Lord, do not place us with the wrongdoing people!"</em></p>
        <h4>Purification on the Vaulted Bridge (Al-Qantarah)</h4>
        <p>Before any believer enters the eternal gates of bliss, Allah removes all lingering worldly grievances, envy, and malice from their breasts (<em>Wa naza'na ma fee sudoorihim min ghill</em>). Purified on the vaulted bridge, they enter Jannah as true, radiant brothers embracing upon thrones.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Sinai Theophany -->
  <div class="modal-backdrop" id="sinaiModal" onclick="closeOnBackdrop(event, 'sinaiModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Theophany of Mount Sinai & The Sacred Tablets</h3>
        <button class="modal-close" onclick="closeModal('sinaiModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "He said, 'My Lord, show me Yourself that I may look upon You.' He said, 'You will never see Me, but look at the mountain; if it should remain in place, then you will see Me.' But when his Lord manifested His glory to the mountain, He made it crumble to dust, and Musa fell unconscious. And when he awoke, he said, 'Glory be to You! I turn to You in repentance, and I am the first of the believers.'"
        </div>
        <h4>The Longing of Kaleemullah</h4>
        <p>Musa's request arose not from skepticism, but from transcendent prophetic love after enjoying direct divine speech (<em>Takleem</em>). Allah did not reprimand Musa for the yearning, but revealed the metaphysical limit of mortal existence: earthly physical faculties cannot sustain the direct, unmediated radiance of the Divine Essence.</p>
        <h4>The Shattered Granite: Ja'alahu Dakkan</h4>
        <p>When Allah revealed merely an infinitesimal glimmer of His light to the colossal mountain of granite, the mountain pulverized instantly into swirling dust. Musa fell down in total swoon (<em>Kharra Musa sa'iqa</em>), overwhelmed by cosmic awe. Awakening, he proclaimed his repentance and submission to mortal boundaries.</p>
        <h4>The Inscribed Tablets: Al-Alwah</h4>
        <p>Allah inscribed for Musa upon the sacred Tablets guidance and detailed admonitions for all things, commanding him to seize them with unshakeable resolve. When Musa returned to find his people worshipping the lowing calf effigy, his righteous anger caused him to cast down the Tablets and confront Harun, illustrating that defense of pure Tawhid eclipses all sentimentality.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Primordial Mithaq -->
  <div class="modal-backdrop" id="mithaqModal" onclick="closeOnBackdrop(event, 'mithaqModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Primordial Covenant (Mithaq Adam) & The Beautiful Names</h3>
        <button class="modal-close" onclick="closeModal('mithaqModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And when your Lord took from the children of Adam—from their loins—their descendants and made them testify of themselves: 'Am I not your Lord?' They said: 'Yes, we testify!'—lest you should say on the Day of Resurrection: 'Indeed, we were of this unaware.'"
        </div>
        <h4>The Blueprint of the Human Soul (Fitrah)</h4>
        <p>Imam Ahmad and At-Tirmidhi record that on the Plain of Na'man (near Arafah), Allah extracted every soul of the progeny of Adam that would ever exist until the end of time. Bestowing upon them consciousness and speech, He extracted their universal testimony to His absolute Lordship (<em>Rububiyyah</em>). This sacred memory is woven into the human conscience as the primordial <strong>Fitrah</strong>.</p>
        <h4>The Parable of the Panting Dog</h4>
        <p>Contrasting with the primordial covenant is the tragedy of the scholar (Balaam ibn Ba'ura) who was gifted divine verses yet shed them like a reptile sheds skin, pursuing base worldly ambition. His likeness is that of an insatiably panting dog: whether driven away or left alone, he pants ceaselessly. Worldly greed without sacred purpose leaves the soul in permanent, agonizing thirst.</p>
        <h4>Al-Asma al-Husna & The Culminating Prostration</h4>
        <p>Revelation commands the faithful to seek refuge and invoke Allah through His Ninety-Nine Most Beautiful Names, avoiding theological deviation (<em>Ilhad</em>). The Surah culminates with the divine protocol of revelation: listening in silence when the Qur'an is recited, continuous morning and evening dhikr, and falling into awestruck prostration (<em>Sajdah</em>) with the angelic host.</p>
      </div>
    </div>
  </div>

  <script>
    function selectPlate(plateNum) {{
      document.querySelectorAll('.plate-section').forEach(sec => sec.classList.remove('active'));
      document.querySelectorAll('.tab-chip').forEach(tab => tab.classList.remove('active'));
      const targetSec = document.getElementById('plateSection' + plateNum);
      if (targetSec) targetSec.classList.add('active');
      const tabs = document.querySelectorAll('.tab-chip');
      if (tabs[plateNum - 1]) tabs[plateNum - 1].classList.add('active');
    }}

    function openModal(id) {{
      const modal = document.getElementById(id);
      if (modal) modal.classList.add('show');
    }}

    function closeModal(id) {{
      const modal = document.getElementById(id);
      if (modal) modal.classList.remove('show');
    }}

    function closeOnBackdrop(e, id) {{
      if (e.target.classList.contains('modal-backdrop')) {{
        closeModal(id);
      }}
    }}

    function handleLiveSearch() {{
      const query = document.getElementById('liveSearchInput').value.toLowerCase().trim();
      const plates = document.querySelectorAll('.plate-section');
      const tabs = document.querySelectorAll('.tab-chip');
      const statsBadge = document.getElementById('statsBadge');

      if (query === '') {{
        plates.forEach(p => p.classList.remove('active'));
        document.getElementById('plateSection1').classList.add('active');
        tabs.forEach(t => t.classList.remove('active'));
        tabs[0].classList.add('active');
        document.querySelectorAll('.card-item').forEach(c => c.style.display = 'block');
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>22</b> Lectures &bull; <b>100%</b> Sunni Verified';
        return;
      }}

      let matchedCount = 0;
      plates.forEach(plate => {{
        let plateHasMatch = false;
        const plateCards = plate.querySelectorAll('.card-item');
        plateCards.forEach(card => {{
          const searchData = card.getAttribute('data-search') || '';
          if (searchData.includes(query)) {{
            card.style.display = 'block';
            plateHasMatch = true;
            matchedCount++;
          }} else {{
            card.style.display = 'none';
          }}
        }});
        if (plateHasMatch) {{
          plate.classList.add('active');
        }} else {{
          plate.classList.remove('active');
        }}
      }});

      statsBadge.innerHTML = 'Found <b>' + matchedCount + ' Matches</b> for "' + query + '"';
    }}

    function filterByMovement(movName) {{
      const mapping = {{
        "Movement 1": 1,
        "Movement 2": 2,
        "Movement 3": 3,
        "Movement 4": 4,
        "Movement 5": 5,
        "Movement 6": 6,
        "Movement 7": 7,
        "Movement 8": 8
      }};
      if (mapping[movName]) {{
        selectPlate(mapping[movName]);
        window.scrollTo({{ top: 120, behavior: 'smooth' }});
      }}
    }}

    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('show'));
      }}
    }});
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated Surah Al-A'raf Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
