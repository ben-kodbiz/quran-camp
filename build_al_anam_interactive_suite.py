#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-An'am Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals (Mafatih al-Ghayb, Ibrahim's Dialectic, Al-Wasaya al-'Ashr, Inna Salatee wa Nusukee)
- 20-Lecture Foundation Audio Syllabus Explorer
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_ANAM_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_al_anam_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_al_anam_html_and_md import pages_data

# 20 Audio Foundation lectures syllabus
audio_lectures = [
    ("6.Al-anaam0introduction.opus", "Makkan Epistemic Context, 70,000 Angels & Cosmic Tawhid", "Movement 1", "25m"),
    ("6.Al-anaam1-6.opus", "Creation of Heavens, Earth, Darkness & Light, Clay Genesis", "Movement 1", "14m"),
    ("6.Al-anaam7-17.opus", "Demand for Paper Scriptures, Al-Qahir & Removal of Harm", "Movement 1", "18m"),
    ("6.Al-anaam18-25.opus", "Divine Supreme Witness & Unmasking Self-Deception", "Movement 1", "25m"),
    ("6.Al-anaam26-32.opus", "Pleading at the Fire & Worldly Life as Ephemeral Play", "Movement 2", "22m"),
    ("6.Al-anaam33-43.opus", "Prophetic Consolation: Slandering Signs & Afflictions for Tadarru'", "Movement 2", "16m"),
    ("6.Al-anaam43-55.opus", "Sudden Seizure of Istidraj, Sanctuary of Humble & Sabeel al-Mujrimeen", "Movement 2", "25m"),
    ("6.Al-anaam56-67.opus", "Mafatih al-Ghayb (Keys of Unseen), Falling Leaves & Sleep as Recall", "Movement 2", "22m"),
    ("6.Al-anaam68-72.opus", "Turning Away from Mockery & Warning Against Regression", "Movement 3", "21m"),
    ("6.Al-anaam73-82.opus", "Ibrahim's Celestial Dialectic (Star, Moon, Sun) & Al-Amn", "Movement 3", "23m"),
    ("6.Al-anaam83-90.opus", "The Golden Chain of 18 Prophets & Fa-bihudahumu-qtadih", "Movement 4", "20m"),
    ("6.Al-anaam91-93.opus", "Rebutting Slander on Revelation & Death Throes of Slanderers", "Movement 4", "23m"),
    ("6.Al-anaam94-99.opus", "Returning Solitary (Furada), Faliqul-Habbi & Cosmic Vegetation", "Movement 5", "21m"),
    ("6.Al-anaam100-106.opus", "Rebutting Jinn Offspring, Badi'us-Samawat & La Tudrikuhul-Absar", "Movement 5", "20m"),
    ("6.Al-anaam107-114.opus", "Prohibition of Reviling False Gods & Ornate Deceptions", "Movement 6", "24m"),
    ("6.Al-anaam115-125.opus", "Perfected Word (Sidqan wa 'Adla), Majoritarianism & Light vs Darkness", "Movement 6", "24m"),
    ("6.Al-anaam126-136.opus", "Dar as-Salam (Abode of Peace), Gathering of Jinn & Pagan Taboos", "Movement 7", "24m"),
    ("6.Al-anaam137-146.opus", "Pagan Superstitions of Cattle & Divine Dietary Boundaries", "Movement 7", "23m"),
    ("6.Al-anaam147-158.opus", "Refuting Fatalism, Al-Wasaya al-'Ashr (The Decalogue) & Sirat Mustaqeem", "Movement 8", "21m"),
    ("6.Al-anaam159-165.opus", "Denouncing Sects, Inna Salatee wa Nusukee & Earthly Stewardship", "Movement 8", "29m")
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
  <title>Surah Al-An'am — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <h1>SURAH AL-AN'AM</h1>
        <span>Master Cartography & Exegetical Suite</span>
      </div>
      <div class="header-actions">
        <button class="btn btn-outline" onclick="openModal('keysModal')">Mafatih al-Ghayb</button>
        <button class="btn btn-outline" onclick="openModal('ibrahimModal')">Ibrahim's Dialectic</button>
        <button class="btn btn-outline" onclick="openModal('wasayaModal')">Al-Wasaya al-'Ashr</button>
        <button class="btn btn-outline" onclick="openModal('surrenderModal')">Inna Salatee</button>
        <a href="SURAH_AL_ANAM_MASTER_COMPENDIUM.pdf" class="btn btn-gold" target="_blank">Download Master PDF</a>
      </div>
    </header>

    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Live search 64 analytical cards across all 8 plates (e.g., Ibrahim, Mafatih, Seed, Wasaya, Tawhid)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="stats-badge" id="statsBadge">
        <span>Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>20</b> Lectures &bull; <b>100%</b> Sunni Verified</span>
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
        <h3>Foundation Audio Syllabus (20 Expository Lectures &bull; 07h 21m 41s)</h3>
        <span style="font-size:0.8rem; color:var(--text-muted);">Click any lecture to explore its thematic movement</span>
      </div>
      <div class="audio-grid">
        {audio_items_html}
      </div>
    </section>

    <footer class="suite-footer">
      <p><strong>Huurs Studio</strong> &bull; Quranic Cartography & Authentic Sunni Classical Knowledge Architecture</p>
      <p>Exegetical Foundations: Imam at-Tabari, Al-Qurtubi, Ibn Kathir, Fakhr ad-Din ar-Razi</p>
      <p>Operating Standard: Read. Reflect. Return. &bull; Strict Zero-Ayah-Number & Zero-Contemporary-Speaker Law</p>
    </footer>
  </div>

  <!-- MODAL 1: Mafatih al-Ghayb -->
  <div class="modal-backdrop" id="keysModal" onclick="closeOnBackdrop(event, 'keysModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Cosmic Keys of the Unseen (Mafatih al-Ghayb) & Omniscience</h3>
        <button class="modal-close" onclick="closeModal('keysModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And with Him are the keys of the unseen; none knows them except Him. And He knows what is on the land and in the sea. Not a leaf falls but that He knows it. And no grain is there within the darknesses of the earth and no moist or dry [thing] but that it is [written] in a clear record."
        </div>
        <h4>Classical Sunni Exegesis (Tabari & Ibn Kathir)</h4>
        <p>Imam Ibn Kathir records that the "Keys of the Unseen" are five primordial matters referenced at the conclusion of Surah Luqman: knowledge of the Hour, the descent of rain, the gender and destiny in the wombs, what a soul will earn tomorrow, and the land in which each soul will die. None possesses unmediated knowledge of these except Allah.</p>
        <h4>The Falling Leaf & Microscopic Omniscience</h4>
        <p>Imam Fakhr ad-Din ar-Razi highlights that divine omniscience is not merely holistic or universal (*Kulliyyat*), but encompasses every individual particle and microscopic alteration (*Juz'iyyat*). The motion of a single leaf detaching from a branch in the deepest primordial forest, its trajectory through the wind, and its exact resting place upon the earth is registered in the archetypal Book (*Kitabin Mubeen*).</p>
        <h4>Sleep as Ontological Recall (Al-Wafah al-Sughra)</h4>
        <p>The passage immediately binds this infinite knowledge to mortal vulnerability: God takes the souls by night in gentle death, knowing all that is committed during waking daylight, and resurrects consciousness until an appointed term is satisfied. Thus, human life is suspended daily in divine mercy.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: Ibrahim's Dialectic -->
  <div class="modal-backdrop" id="ibrahimModal" onclick="closeOnBackdrop(event, 'ibrahimModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Ibrahim's Celestial Dialectic & The Citadel of Security</h3>
        <button class="modal-close" onclick="closeModal('ibrahimModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "When the night covered him over with darkness, he saw a star. He said, 'This is my lord.' But when it set, he said, 'I love not that which sets.' ... Indeed, I have turned my face toward Him who created the heavens and the earth, purely upright; and I am not of the polytheists."
        </div>
        <h4>Pedagogical Debate vs. Personal Skepticism</h4>
        <p>Classical authorities (Imam at-Tabari and Al-Qurtubi) decisively clarify that Ibrahim never worshipped the celestial bodies; rather, his discourse was a pedagogical debate (*Munazarah*) designed to expose the absurdity of astral deities worshipped by his Mesopotamian people. By hypothetically adopting their premise ("This is my Lord?"), he led them to observe its inevitable decline.</p>
        <h4>The Principle: La Uhibbul-Afileen</h4>
        <p>Any entity subject to setting, transit, eclipse, or ontological limitation (*Uful*) is contingent (*Hadith*) and created. A contingent being can never be the Absolute Sustainer (*Rabb*). From the dim star to the radiant moon and finally the blinding sun, every celestial entity reveals itself as subordinate to cosmic law.</p>
        <h4>The Citadel of Security (Al-Amn)</h4>
        <p>When his people threatened him with their false idols, Ibrahim posed the supreme epistemic question: Which of the two factions has greater right to security? Revelation answers: "Those who believe and taint not their faith with injustice [Shirk]—for them is absolute security, and they are rightly guided." When the companions asked regarding this verse, the Prophet clarified that 'injustice' here means Shirk, as Luqman counseled his son.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Al-Wasaya al-'Ashr -->
  <div class="modal-backdrop" id="wasayaModal" onclick="closeOnBackdrop(event, 'wasayaModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Quranic Decalogue (Al-Wasaya al-'Ashr) & The Master Path</h3>
        <button class="modal-close" onclick="closeModal('wasayaModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Say, 'Come, I will recite what your Lord has prohibited to you: Do not associate anything with Him, and to parents, good treatment, and do not kill your children out of poverty; We will provide for you and them... And this is My path, which is straight, so follow it; and do not follow [other] ways, for you will be separated from His way.'"
        </div>
        <h4>The Eternal Ten Commandments</h4>
        <p>Abdullah ibn Mas'ud stated: <em>"Whoever wishes to look upon the testament of the Messenger of Allah upon which is his seal, let him recite these verses: 'Say, Come, I will recite what your Lord has prohibited to you...'"</em></p>
        <ul>
          <li><strong>Pillar 1:</strong> Pure Tawhid & Absolute Refusal of Shirk.</li>
          <li><strong>Pillar 2:</strong> Filial Piety & Righteous Treatment of Parents (*Ihsan bil-Walidayn*).</li>
          <li><strong>Pillar 3:</strong> Sanctity of Offspring: Forbidding Infanticide out of Fear of Poverty.</li>
          <li><strong>Pillar 4:</strong> Abstinence from Indecencies (*Fawahish*), Both Manifest & Hidden.</li>
          <li><strong>Pillar 5:</strong> Sanctity of Human Life: Slaying No Innocent Soul Unjustly.</li>
          <li><strong>Pillar 6:</strong> Fiduciary Purity: Protecting the Property of Orphans.</li>
          <li><strong>Pillar 7:</strong> Economic Integrity: Exact Measures & Equity in the Marketplace.</li>
          <li><strong>Pillar 8:</strong> Objective Judicial Veracity: Speaking Truth Regardless of Kinship.</li>
          <li><strong>Pillar 9:</strong> Covenantal Fidelity: Fulfilling All Pacts Established with God.</li>
          <li><strong>Pillar 10:</strong> Adherence to the Singular Straight Path (*Siratan Mustaqeema*) and Rejection of Fractured Splinter Paths.</li>
        </ul>
        <h4>The Diagram of the Prophet</h4>
        <p>Imam Ahmad and An-Nasa'i record that the Prophet drew a straight line in the sand, saying: "This is the Path of Allah." Then he drew divergent lines to the right and left, saying: "These are pathways, upon each of which is a devil calling toward it." Then he recited: <em>"And do not follow [other] ways, for you will be separated from His way."</em></p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Inna Salatee -->
  <div class="modal-backdrop" id="surrenderModal" onclick="closeOnBackdrop(event, 'surrenderModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Supreme Creed of Surrender & Earthly Stewardship</h3>
        <button class="modal-close" onclick="closeModal('surrenderModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Say, 'Indeed, my prayer, my rites of sacrifice, my living and my dying are for Allah, Lord of the worlds. No partner has He. And this I have been commanded, and I am the first of the Muslims.' ... And He it is who has made you successors upon the earth and has raised some of you above others in degrees [of rank] that He may try you through what He has given you."
        </div>
        <h4>Comprehensive Ontological Consecration</h4>
        <p>This verse represents the zenith of prophetic devotion. Ritual prayer (*Salah*) and sacrificial devotion (*Nusuk*) are unified with every breath of mortal life (*Mahyaya*) and the final passage of death (*Mamatee*). Nothing in the believer's existence remains profane or isolated from divine devotion.</p>
        <h4>Individual Accountability: Wa La Taziru Waziratun Wizra Ukhra</h4>
        <p>Every soul bears exclusively its own moral weight. No inherited guilt, no vicarious atonement, and no tribal shielding can alleviate the individual's reckoning before the Sovereign. This principle dismantled the collective culpability structures of pre-Islamic Arabia.</p>
        <h4>Succession & Ethical Testing (Khala'if al-Ard)</h4>
        <p>Human beings are placed upon this terrestrial realm as stewards and successors (*Khala'if*). The disparities in wealth, intellect, status, and physical strength are not badges of inherent superiority, but instruments of divine examination (*Li-yabluwakum fee ma atakum*). The Surah concludes by balancing absolute accountability with transcendent hope: swift in retribution, yet Most Forgiving and Ever Merciful.</p>
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
      if (e.target.id === id) {{
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>20</b> Lectures &bull; <b>100%</b> Sunni Verified';
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

print(f"Successfully generated Surah Al-An'am Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
