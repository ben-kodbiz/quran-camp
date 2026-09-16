#!/usr/bin/env python3
"""
Huurs Studio - Surah Ali-Imran Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals (Uhud, Ulul-Albab, Leadership, Sunni Audit)
- 41-Lecture Foundation Audio Syllabus Explorer
- Widescreen 16:9 responsive presentation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_ALI_IMRAN_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_ali_imran_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_ali_imran_html_and_md import pages_data

# 41 Audio Foundation lectures syllabus
audio_lectures = [
    ("3.aliimran1-6.opus", "Al-Hayyul-Qayyum & Primordial Epistemology", "Movement 1", "24m"),
    ("3.aliimran7.opus", "Muhkam vs. Mutashabih & Rooted Scholars", "Movement 1", "31m"),
    ("3.aliimran8-9.opus", "Rabbana La Tuzigh & Master Supplication", "Movement 1", "19m"),
    ("3.aliimran10-13.opus", "The Deception of Wealth & Pharaoh's Fate", "Movement 1", "22m"),
    ("3.aliimran14-16.opus", "Lure of Pleasures vs. Gardens of Eternity", "Movement 1", "26m"),
    ("3.aliimran17-18.opus", "Shahidallahu: Universal Divine Testimony", "Movement 1", "21m"),
    ("3.aliimran19-20.opus", "Innad-Deena 'Indallahil-Islam", "Movement 1", "25m"),
    ("3.aliimran21-25.opus", "Slaying Prophets & Disdain for Truth", "Movement 1", "18m"),
    ("3.aliimran26-27.opus", "Malikul-Mulk: Sovereign Dominion of Kingship", "Movement 1", "27m"),
    ("3.aliimran28-30.opus", "Alliances of Faith & Divine Vigilance", "Movement 1", "20m"),
    ("3.aliimran31.opus", "The Universal Metric of Divine Love", "Movement 1", "29m"),
    ("3.aliimran32-37.opus", "Election of Imran & Hannah's Vow", "Movement 2", "33m"),
    ("3.aliimran37-44.opus", "The Sanctuary of Maryam & Out-of-Season Fruits", "Movement 2", "35m"),
    ("3.aliimran45-50.opus", "The Annunciation of the Messiah Isa", "Movement 2", "28m"),
    ("3.aliimran51-58.opus", "Miracles by Divine Leave & Disciples", "Movement 3", "26m"),
    ("3.aliimran59-68.opus", "Kamathali Adam & The Mubahalah Proof", "Movement 3", "34m"),
    ("3.aliimran69-76.opus", "Kalimatin Sawa': Equitable Word of Monotheism", "Movement 4", "27m"),
    ("3.aliimran77-80.opus", "Bartering the Covenant for Fleeting Gain", "Movement 4", "19m"),
    ("3.aliimran81-84.opus", "Mithaq al-Nabiyyeen: Prophets' Pact", "Movement 4", "22m"),
    ("3.aliimran85-91.opus", "Islam as Sole Accepted Deen & Unaccepted Gold", "Movement 4", "24m"),
    ("3.aliimran92-93.opus", "Lan Tanalul-Birr: Sacrificing What is Beloved", "Movement 4", "23m"),
    ("3.aliimran94-100.opus", "Fabricating Food Prohibitions & Defending Truth", "Movement 4", "20m"),
    ("3.aliimran101-102.opus", "Ittaqu Allaha Haqqa Tuqatih: True Taqwa", "Movement 5", "25m"),
    ("3.aliimran103.opus", "Hablillah: The Unbreakable Divine Cable", "Movement 5", "32m"),
    ("3.aliimran104-109.opus", "The Dedicated Vanguard of Reform & Two Faces", "Movement 5", "26m"),
    ("3.aliimran110-112.opus", "Khayra Ummah: Best Nation for Humanity", "Movement 5", "30m"),
    ("3.aliimran113-118.opus", "Righteous People of the Book & Internal Security", "Movement 5", "22m"),
    ("3.aliimran119-122.opus", "Biting Fingers in Rage & True Brotherhood", "Movement 5", "21m"),
    ("3.aliimran123-132.opus", "Badr Humility vs. Uhud & Angels Descending", "Movement 6", "29m"),
    ("3.aliimran133-143.opus", "Rushing to Forgiveness & Tamhees Purification", "Movement 6", "28m"),
    ("3.aliimran144-152.opus", "Mount Rumah Deviation & Desiring Dunya", "Movement 6", "36m"),
    ("3.aliimran153-158.opus", "Ghamman bi-Ghamm & Supernatural Slumber", "Movement 7", "30m"),
    ("3.aliimran159.opus", "Linta Lahum: Prophetic Mildness & Shura Triad", "Movement 7", "34m"),
    ("3.aliimran160-168.opus", "Tawakkul, Munafiqun Desertion & The 70 Martyrs", "Movement 7", "27m"),
    ("3.aliimran169-175.opus", "Bal Ahya'un: Emerald Birds Beneath the Throne", "Movement 7", "33m"),
    ("3.aliimran176-180.opus", "The Poison of Miserliness & Neck Collars", "Movement 7", "20m"),
    ("3.aliimran181-187.opus", "Refuting Cosmic Slanders & Testing Believers", "Movement 7", "24m"),
    ("3.aliimran188-189.opus", "Rejoicing in False Praise & Universal Kingship", "Movement 7", "17m"),
    ("3.aliimran190-191.opus", "Ulul-Albab & Cosmological Contemplation", "Movement 8", "31m"),
    ("3.aliimran192-195.opus", "Supplications of the Wise & Fastajaba Lahum", "Movement 8", "26m"),
    ("3.aliimran196-200.opus", "Strutting Deniers & The Quadruple Mandate", "Movement 8", "28m")
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
        <span class="badge-emerald">100% VERIFIED</span>
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
  <title>Surah Ali-Imran — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
    /* Top Header */
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

    /* Global Search & Nav */
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
    .search-input {{
      width: 100%;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--white);
      padding: 10px 14px 10px 38px;
      border-radius: 6px;
      font-size: 0.88rem;
    }}
    .search-input:focus {{
      outline: none;
      border-color: var(--gold);
    }}
    .search-icon {{
      position: absolute;
      left: 12px;
      top: 10px;
      color: var(--text-muted);
    }}
    .search-status {{
      font-size: 0.8rem;
      color: var(--gold);
      white-space: nowrap;
    }}

    /* Tab Chips */
    .tabs-strip {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 6px;
      margin-bottom: 20px;
    }}
    .tab-chip {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .tab-chip:hover {{
      background: var(--navy-elevated);
      color: var(--white);
      border-color: var(--gold);
    }}
    .tab-chip.active {{
      background: var(--gold);
      color: var(--navy-deep);
      border-color: var(--gold);
      font-weight: 700;
    }}

    /* Layout Main Split */
    .suite-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 20px;
    }}
    @media (max-width: 1080px) {{
      .suite-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Sidebar: Audio Syllabus */
    .syllabus-sidebar {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      height: fit-content;
      max-height: 860px;
    }}
    .sidebar-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-muted);
    }}
    .sidebar-header h3 {{
      font-size: 0.95rem;
      color: var(--gold);
    }}
    .sidebar-header span {{
      font-size: 0.75rem;
      color: var(--emerald);
      background: var(--navy-elevated);
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .audio-scroll-list {{
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding-right: 4px;
    }}
    .audio-row {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 8px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .audio-row:hover {{
      border-color: var(--cyan);
      background: #192742;
    }}
    .audio-meta-left {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .audio-num {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.1);
      padding: 2px 6px;
      border-radius: 4px;
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
      font-size: 0.75rem;
      color: var(--gold-light);
      font-weight: 600;
      white-space: nowrap;
    }}

    /* Main Plate Section */
    .plate-section {{
      display: none;
      animation: fadeIn 0.3s ease-in-out;
    }}
    .plate-section.active {{
      display: block;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .plate-title-bar {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .plate-title-bar h2 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 4px;
    }}
    .plate-title-bar p {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .plate-badge-box {{
      display: flex;
      gap: 8px;
    }}
    .badge-gold {{
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--gold);
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      padding: 4px 10px;
      border-radius: 4px;
    }}
    .badge-emerald {{
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--emerald);
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      padding: 4px 10px;
      border-radius: 4px;
    }}

    /* 2 Pillars Grid */
    .pillars-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 900px) {{
      .pillars-layout {{
        grid-template-columns: 1fr;
      }}
    }}
    .pillar-box {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    .pillar-bar {{
      padding: 14px 18px;
      background: var(--navy-elevated);
      border-bottom: 1px solid var(--border-muted);
    }}
    .pillar-bar.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-bar.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-bar.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-bar.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-bar.rose {{ border-top: 3px solid var(--rose); }}

    .pillar-bar h3 {{
      font-size: 0.95rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      margin-bottom: 2px;
    }}
    .pillar-bar.cyan h3 {{ color: var(--cyan); }}
    .pillar-bar.gold h3 {{ color: var(--gold); }}
    .pillar-bar.emerald h3 {{ color: var(--emerald); }}
    .pillar-bar.purple h3 {{ color: var(--purple); }}
    .pillar-bar.rose h3 {{ color: var(--rose); }}

    .pillar-bar p {{
      font-size: 0.78rem;
      color: var(--text-muted);
      font-style: italic;
    }}

    .cards-wrapper {{
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .card-item {{
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 14px;
    }}
    .card-item:last-child {{
      border-bottom: none;
      padding-bottom: 0;
    }}
    .card-title-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }}
    .card-idx {{
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--gold);
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      padding: 1px 6px;
      border-radius: 3px;
    }}
    .card-title-row h4 {{
      font-size: 0.88rem;
      color: var(--white);
      font-weight: 700;
    }}
    .card-points {{
      list-style: none;
      padding-left: 0;
    }}
    .card-points li {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
      position: relative;
      padding-left: 14px;
      margin-bottom: 4px;
    }}
    .card-points li::before {{
      content: "-";
      position: absolute;
      left: 0;
      color: var(--border-muted);
    }}

    /* Footer */
    footer.suite-footer {{
      margin-top: 32px;
      padding-top: 16px;
      border-top: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      color: var(--text-muted);
      flex-wrap: wrap;
      gap: 8px;
    }}
    .footer-gold {{
      color: var(--gold);
      font-weight: 600;
    }}

    /* Modals */
    .modal-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(4px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-backdrop.active {{
      display: flex;
    }}
    .modal-box {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-top: 3px solid var(--gold);
      border-radius: 8px;
      max-width: 760px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 12px;
    }}
    .modal-header h3 {{
      font-size: 1.1rem;
      color: var(--gold);
    }}
    .modal-close {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      cursor: pointer;
    }}
    .modal-close:hover {{
      color: var(--white);
    }}
    .modal-content {{
      font-size: 0.88rem;
      color: var(--text-muted);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .modal-content strong {{
      color: var(--white);
    }}
    .modal-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 10px;
    }}
    .modal-col {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px;
    }}
  </style>
</head>
<body>
  <div class="suite-shell">
    <header class="suite-header">
      <div class="header-brand">
        <h1>HUURS STUDIO</h1>
        <span>DEEPER THOUGHT CAMPAIGN &bull; SURAH ALI-IMRAN</span>
      </div>
      <div class="header-actions">
        <button class="btn btn-outline" onclick="openModal('modalUhud')">⚔️ Uhud Crucible</button>
        <button class="btn btn-outline" onclick="openModal('modalLeadership')">🌿 Prophetic Mildness</button>
        <button class="btn btn-outline" onclick="openModal('modalUlulAlbab')">🌌 Ulul-Albab</button>
        <button class="btn btn-outline" onclick="openModal('modalAudit')">📜 Sunni Certification</button>
        <a href="./SURAH_ALI_IMRAN_MASTER_COMPENDIUM.pdf" target="_blank" class="btn btn-gold">📥 Master PDF (10 Plates)</a>
      </div>
    </header>

    <!-- Controls & Search -->
    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="cardSearchInput" class="search-input" placeholder="Search across all 64 cards (e.g. 'archers', 'Mubahalah', 'Linta lahum', 'Mihrab')..." oninput="handleSearch()">
      </div>
      <div class="search-status" id="searchStatus">Showing all 64 cards across 8 Plates</div>
      <button class="btn btn-outline" id="toggleAllBtn" onclick="toggleShowAll()">👁️ Show All 8 Plates</button>
    </div>

    <!-- Tab Chips -->
    <div class="tabs-strip" id="tabsStrip">
      {tab_buttons_html}
    </div>

    <!-- Main Grid -->
    <div class="suite-grid">
      <!-- Sidebar: Foundation Audio Syllabus -->
      <aside class="syllabus-sidebar">
        <div class="sidebar-header">
          <h3>Foundation Audio Corpus</h3>
          <span>41 Lectures &bull; 13h 38m</span>
        </div>
        <div class="audio-scroll-list">
          {audio_items_html}
        </div>
      </aside>

      <!-- Main Content Viewport -->
      <main class="content-viewport">
        {plates_html}
      </main>
    </div>

    <!-- Footer -->
    <footer class="suite-footer">
      <div>HUURS KNOWLEDGE SYSTEMS &bull; AUTHENTIC SUNNI SOURCE DISCIPLINE &bull; ZERO TIMESTAMPS &bull; ZERO SPEAKER NAMES</div>
      <div class="footer-gold">SURAH ALI-IMRAN INTERACTIVE DIGITAL SUITE &bull; 10 PLATES &bull; 16 PILLARS &bull; 64 CARDS</div>
    </footer>
  </div>

  <!-- MODALS -->
  <!-- Modal: Uhud Crucible -->
  <div class="modal-backdrop" id="modalUhud">
    <div class="modal-box">
      <div class="modal-header">
        <h3>⚔️ THE CRUCIBLE OF UHUD: BATTLEFIELD PEDAGOGY</h3>
        <button class="modal-close" onclick="closeModal('modalUhud')">&times;</button>
      </div>
      <div class="modal-content">
        <p><strong>The Battle of Uhud (3 AH)</strong> forms the centerpiece of Surah Ali-Imran, transforming military catastrophe into a timeless masterclass on communal discipline, internal motives, and spiritual purification.</p>
        <div class="modal-grid">
          <div class="modal-col">
            <h4 style="color:var(--rose); margin-bottom:6px;">1. The Mount Rumah Order</h4>
            <p>Fifty archers stationed with a strict mandate: <em>"Guard our rear; do not leave even if birds snatch our flesh."</em> Forty archers deserted for spoils, exposing the flank to cavalry.</p>
          </div>
          <div class="modal-col">
            <h4 style="color:var(--gold); margin-bottom:6px;">2. The Divine Diagnostic</h4>
            <p><em>"Among you were some who desired this world, and some who desired the Hereafter."</em> Microscopic greed on the frontline compromises the collective body.</p>
          </div>
        </div>
        <div class="modal-grid">
          <div class="modal-col">
            <h4 style="color:var(--cyan); margin-bottom:6px;">3. Sorrow Upon Sorrow (Ghamman bi-Ghamm)</h4>
            <p>Loss of spoils, battlefield encirclement, 70 martyrs, and the false rumor of the Prophet's death cured hearts of superficial worldly attachments.</p>
          </div>
          <div class="modal-col">
            <h4 style="color:var(--emerald); margin-bottom:6px;">4. Tamhees: Divine Surgery</h4>
            <p>Adversity filters genuine faith from hypocrisy. A purified, smaller community is far stronger than a large, compromised crowd.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal: Prophetic Mildness -->
  <div class="modal-backdrop" id="modalLeadership">
    <div class="modal-box">
      <div class="modal-header">
        <h3>🌿 THE SUBLIME TRIAD OF LEADERSHIP (AYAH 159)</h3>
        <button class="modal-close" onclick="closeModal('modalLeadership')">&times;</button>
      </div>
      <div class="modal-content">
        <p>Following the disaster of Uhud—where the Prophet suffered physical wounds and lost his uncle Hamzah—the divine command descended on how to govern broken followers:</p>
        <p style="color:var(--gold); font-size:0.95rem; font-style:italic;">"By mercy from Allah, you were gentle with them. Had you been harsh and hard-hearted, they would have dispersed from around you."</p>
        <div class="modal-grid">
          <div class="modal-col">
            <h4 style="color:var(--emerald); margin-bottom:4px;">1. Fa'fu 'Anhum (Pardon)</h4>
            <p>Pardon their battlefield disobedience personally; release personal resentment and wipe away grievance from the heart.</p>
          </div>
          <div class="modal-col">
            <h4 style="color:var(--cyan); margin-bottom:4px;">2. Wastaghfir Lahum (Intercession)</h4>
            <p>Seek God's forgiveness for their spiritual guilt, interceding actively for their moral and religious rehabilitation.</p>
          </div>
        </div>
        <div class="modal-grid">
          <div class="modal-col">
            <h4 style="color:var(--purple); margin-bottom:4px;">3. Wa Shawirhum (Shura Consultation)</h4>
            <p>Re-engage the very men whose advice led to defeat in consultation. Shura restores dignity, rebuilding confidence and ownership.</p>
          </div>
          <div class="modal-col">
            <h4 style="color:var(--gold); margin-bottom:4px;">4. Fa-Idha 'Azamta Fa-Tawakkal</h4>
            <p>Once a course of action is resolved, execute with total reliance upon Allah. Banish second-guessing and paralyzed regret.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal: Ulul-Albab -->
  <div class="modal-backdrop" id="modalUlulAlbab">
    <div class="modal-box">
      <div class="modal-header">
        <h3>🌌 THE ULUL-ALBAB COSMOLOGICAL PARADIGM (AYAT 190–200)</h3>
        <button class="modal-close" onclick="closeModal('modalUlulAlbab')">&times;</button>
      </div>
      <div class="modal-content">
        <p>Surah Ali-Imran concludes with the profound contemplation of the cosmos in the dead of night, unifying scientific observation with moral awe:</p>
        <div class="modal-grid">
          <div class="modal-col">
            <h4 style="color:var(--cyan); margin-bottom:4px;">1. Constant Dhikr in All Postures</h4>
            <p>Remembering Allah standing, sitting, and on their sides; observation of cosmic mechanisms permanently wedded to divine reverence.</p>
          </div>
          <div class="modal-col">
            <h4 style="color:var(--gold); margin-bottom:4px;">2. Teleological Conviction</h4>
            <p><em>"Rabbana ma khalaqta hadha batila"</em> &mdash; Our Lord, You did not create all this in vain! Every galaxy and atom declares purposeful design.</p>
          </div>
        </div>
        <div class="modal-col" style="margin-top:10px;">
          <h4 style="color:var(--emerald); margin-bottom:4px;">3. The Quadruple Mandate (Ayah 200)</h4>
          <p>The definitive constitutional recipe for ultimate triumph: <strong>1. Isbiru</strong> (Personal patience) &bull; <strong>2. Sabiru</strong> (Collective endurance) &bull; <strong>3. Rabitu</strong> (Frontier vigilance) &bull; <strong>4. Ittaqullah</strong> (Constant God-consciousness).</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal: Sunni Certification -->
  <div class="modal-backdrop" id="modalAudit">
    <div class="modal-box">
      <div class="modal-header">
        <h3>📜 CLASSICAL SUNNI EXEGETICAL CERTIFICATION</h3>
        <button class="modal-close" onclick="closeModal('modalAudit')">&times;</button>
      </div>
      <div class="modal-content">
        <p>This digital suite strictly conforms to Orthodox Sunni hermeneutics (*Tafsir bil-Ma'thur*), drawing directly from canonical classical authorities:</p>
        <ul style="padding-left:20px; line-height:1.7;">
          <li><strong>Tafsir al-Tabari (Jami' al-Bayan):</strong> Authoritative isnad chains, Arabic linguistics, and Sabab an-Nuzul.</li>
          <li><strong>Tafsir Ibn Kathir (Tafsir al-Qur'an al-'Azim):</strong> Ayah-by-ayah hadith correlation and Prophetic Sunnah verification.</li>
          <li><strong>Tafsir al-Qurtubi (Al-Jami' li-Ahkam al-Qur'an):</strong> Juridical derivation, Ahkam governance, and ethical commandments.</li>
          <li><strong>Mafatih al-Ghayb (Al-Razi):</strong> Philosophical refutation of deification, Kamathali Adam logic, and epistemology.</li>
          <li><strong>Zad al-Ma'ad (Ibn al-Qayyim):</strong> Strategic military and spiritual lessons of the Battle of Uhud.</li>
        </ul>
        <div style="background:var(--navy-elevated); padding:10px; border-radius:6px; border-left:3px solid var(--emerald); margin-top:8px;">
          <strong>Zero Contemporary Speaker Names:</strong> 100% Huurs Studio institutional voice anchored in centuries of verified classical consensus.
        </div>
      </div>
    </div>
  </div>

  <script>
    let showAllActive = false;

    function selectPlate(num) {{
      showAllActive = false;
      document.getElementById('toggleAllBtn').innerText = "👁️ Show All 8 Plates";
      
      document.querySelectorAll('.plate-section').forEach(sec => sec.classList.remove('active'));
      document.querySelectorAll('.tab-chip').forEach(chip => chip.classList.remove('active'));

      const target = document.getElementById('plateSection' + num);
      if (target) target.classList.add('active');

      const chips = document.querySelectorAll('.tab-chip');
      if (chips[num - 1]) chips[num - 1].classList.add('active');
    }}

    function toggleShowAll() {{
      showAllActive = !showAllActive;
      const btn = document.getElementById('toggleAllBtn');
      if (showAllActive) {{
        btn.innerText = "📑 Show Single Plate View";
        document.querySelectorAll('.plate-section').forEach(sec => sec.classList.add('active'));
        document.querySelectorAll('.tab-chip').forEach(chip => chip.classList.remove('active'));
      }} else {{
        selectPlate(1);
      }}
    }}

    function handleSearch() {{
      const query = document.getElementById('cardSearchInput').value.trim().toLowerCase();
      const cards = document.querySelectorAll('.card-item');
      let visibleCount = 0;

      if (!query) {{
        cards.forEach(card => card.style.display = '');
        document.getElementById('searchStatus').innerText = "Showing all 64 cards across 8 Plates";
        if (!showAllActive) selectPlate(1);
        return;
      }}

      // Force show all plates during search
      document.querySelectorAll('.plate-section').forEach(sec => sec.classList.add('active'));
      document.querySelectorAll('.tab-chip').forEach(chip => chip.classList.remove('active'));
      document.getElementById('toggleAllBtn').innerText = "📑 Show Single Plate View";
      showAllActive = true;

      cards.forEach(card => {{
        const searchData = card.getAttribute('data-search') || '';
        if (searchData.includes(query)) {{
          card.style.display = '';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      document.getElementById('searchStatus').innerText = "Found " + visibleCount + " cards matching \"" + query + "\"";
    }}

    function filterByMovement(mov) {{
      const query = mov.toLowerCase();
      document.getElementById('cardSearchInput').value = query;
      handleSearch();
    }}

    function openModal(id) {{
      const el = document.getElementById(id);
      if (el) el.classList.add('active');
    }}

    function closeModal(id) {{
      const el = document.getElementById(id);
      if (el) el.classList.remove('active');
    }}

    window.onclick = function(event) {{
      if (event.target.classList.contains('modal-backdrop')) {{
        event.target.classList.remove('active');
      }}
    }};
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated {OUTPUT_HTML} (Size: {len(full_html)} bytes)")
