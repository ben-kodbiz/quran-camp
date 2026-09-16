#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Hijr Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Seven-Fold Divine Guarantee of Dhikr (Inna Nahnu Nazzalna)
    2. Primordial Genesis from Sounding Mud & The Rebellion of Iblis (Salsal & Qiyas Batil)
    3. The Metaphysics of Seduction & The Fortress of Sincerity (Al-Mukhliseen)
    4. Al-Sab' al-Mathani & The Divine Antidote to the Constricted Heart (Tasbih & Sujood)
- 5-Lecture Foundation Audio Syllabus Explorer (01h 35m 03s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_HIJR_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_hijr_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_hijr_html_and_md import pages_data

# 5 Audio Foundation lectures syllabus
audio_lectures = [
    ("15.Al-hijr1-11.opus", "Preservation of Dhikr, Future Regret & The Eavesdropping Defense", "Movement 1", "18m 47s"),
    ("15.Al-hijr12-25.opus", "Constellations, Fertilizing Winds & The Architecture of Creation", "Movement 2", "16m 46s"),
    ("15.Al-hijr26-47.opus", "Primordial Clay, Rebellion of Iblis & Immunity of Al-Mukhliseen", "Movement 3 & 4", "19m 31s"),
    ("15.Al-hijr48-75.opus", "Paradise Peace, Ibrahim's Emissaries & The Fall of Sodom", "Movement 5 & 6", "17m 06s"),
    ("15.Al-hijr76-99.opus", "The Hewn Fortresses of Thamud, Al-Fatihah & The Cure of Sujood", "Movement 7 & 8", "22m 52s")
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

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Hijr — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
  <style>
    :root {
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
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      background: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
      line-height: 1.5;
      padding: 20px;
    }
    .suite-shell {
      max-width: 1480px;
      margin: 0 auto;
    }
    header.suite-header {
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
    }
    .header-brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .header-brand h1 {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.05em;
    }
    .header-brand span {
      color: var(--text-muted);
      font-size: 0.9rem;
      border-left: 1px solid var(--border-muted);
      padding-left: 12px;
    }
    .header-actions {
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }
    .btn {
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
    }
    .btn-gold {
      background: var(--gold);
      color: var(--navy-deep);
    }
    .btn-gold:hover {
      background: var(--gold-light);
    }
    .btn-outline {
      background: var(--navy-elevated);
      color: var(--white);
      border: 1px solid var(--border-muted);
    }
    .btn-outline:hover {
      border-color: var(--gold);
    }
    .search-panel {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      gap: 16px;
      align-items: center;
      flex-wrap: wrap;
    }
    .search-input-box {
      flex: 1;
      min-width: 280px;
      position: relative;
    }
    .search-input-box input {
      width: 100%;
      background: var(--navy-elevated);
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
      box-shadow: 0 0 8px rgba(212, 175, 55, 0.25);
    }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.95rem;
    }
    .stats-badge {
      font-size: 0.82rem;
      color: var(--text-muted);
    }
    .stats-badge b {
      color: var(--gold);
    }
    .modals-bar {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }
    .btn-modal-trigger {
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      color: var(--white);
      padding: 9px 15px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-modal-trigger:hover {
      border-color: var(--gold);
      color: var(--gold-light);
      transform: translateY(-1px);
    }
    .nav-tabs {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 8px;
      margin-bottom: 20px;
    }
    .tab-chip {
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
    }
    .tab-chip:hover {
      border-color: var(--gold);
      color: var(--white);
    }
    .tab-chip.active {
      background: var(--navy-elevated);
      color: var(--gold);
      border-color: var(--gold);
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
    }
    .plate-section {
      display: none;
      margin-bottom: 30px;
    }
    .plate-section.active {
      display: block;
    }
    .plate-title-bar {
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
    }
    .plate-title-bar h2 {
      font-size: 1.15rem;
      color: var(--white);
      margin-bottom: 2px;
    }
    .plate-title-bar p {
      font-size: 0.82rem;
      color: var(--text-muted);
    }
    .plate-badge-box {
      display: flex;
      gap: 8px;
    }
    .badge-gold {
      background: rgba(212, 175, 55, 0.15);
      color: var(--gold-light);
      border: 1px solid var(--gold);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
    }
    .badge-emerald {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid var(--emerald);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
    }
    .pillars-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }
    @media (max-width: 960px) {
      .pillars-layout { grid-template-columns: 1fr; }
    }
    .pillar-box {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }
    .pillar-bar {
      padding: 14px 18px;
      background: var(--navy-elevated);
      border-bottom: 1px solid var(--border-muted);
    }
    .pillar-bar.cyan { border-top: 3px solid var(--cyan); }
    .pillar-bar.purple { border-top: 3px solid var(--purple); }
    .pillar-bar.emerald { border-top: 3px solid var(--emerald); }
    .pillar-bar.gold { border-top: 3px solid var(--gold); }
    .pillar-bar.rose { border-top: 3px solid var(--rose); }
    .pillar-bar h3 {
      font-size: 0.92rem;
      color: var(--white);
      margin-bottom: 2px;
    }
    .pillar-bar p {
      font-size: 0.78rem;
      color: var(--text-muted);
    }
    .cards-wrapper {
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .card-item {
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 14px;
      transition: all 0.2s;
    }
    .card-item:hover {
      border-color: var(--gold);
      transform: translateY(-1px);
    }
    .card-title-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }
    .card-idx {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 2px 6px;
      border-radius: 3px;
    }
    .card-title-row h4 {
      font-size: 0.85rem;
      color: var(--white);
      font-weight: 700;
    }
    .card-points {
      list-style-type: none;
      padding-left: 0;
    }
    .card-points li {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 4px;
      position: relative;
      padding-left: 14px;
    }
    .card-points li::before {
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 0.78rem;
    }
    .audio-section {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px;
      margin-top: 30px;
    }
    .audio-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .audio-header h3 {
      font-size: 1.05rem;
      color: var(--gold);
    }
    .audio-header span {
      font-size: 0.82rem;
      color: var(--text-muted);
    }
    .audio-grid {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .audio-row {
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s;
    }
    .audio-row:hover {
      border-color: var(--cyan);
      transform: translateX(3px);
    }
    .audio-meta-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .audio-num {
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 8px;
      border-radius: 4px;
    }
    .audio-title {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--white);
    }
    .audio-sub {
      font-size: 0.75rem;
      color: var(--text-muted);
    }
    .audio-duration {
      font-size: 0.8rem;
      color: var(--gold-light);
      font-weight: 600;
    }
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(6px);
      z-index: 9999;
      display: none;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    .modal-backdrop.show {
      display: flex;
    }
    .modal-window {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-top: 3px solid var(--gold);
      border-radius: 8px;
      max-width: 800px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 12px;
    }
    .modal-header h3 {
      font-size: 1.15rem;
      color: var(--gold);
    }
    .modal-close {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      cursor: pointer;
      line-height: 1;
    }
    .modal-close:hover {
      color: var(--white);
    }
    .modal-body {
      font-size: 0.88rem;
      line-height: 1.6;
      color: var(--text-muted);
    }
    .modal-body h4 {
      color: var(--white);
      margin: 14px 0 6px 0;
      font-size: 0.95rem;
    }
    .modal-body p {
      margin-bottom: 10px;
    }
    .modal-body ul {
      margin: 8px 0 12px 20px;
    }
    .modal-body li {
      margin-bottom: 6px;
    }
    .quote-box {
      background: var(--navy-elevated);
      border-left: 3px solid var(--gold);
      padding: 12px 16px;
      margin-bottom: 14px;
      font-style: italic;
      color: var(--gold-light);
    }
  </style>
</head>
<body>
  <div class="suite-shell">
    <header class="suite-header">
      <div class="header-brand">
        <h1>HUURS STUDIO</h1>
        <span>Surah Al-Hijr &bull; Master Interactive Digital Suite</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_HIJR_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>📥</span> Download Compendium PDF
        </a>
        <a href="../07_MINDMAP/HIJR_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>🗺️</span> Standalone Mindmap
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Live search across 64 cards, themes, concepts, or terms..." oninput="handleLiveSearch()">
      </div>
      <div class="stats-badge" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>5</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
    </div>

    <div class="modals-bar">
      <button class="btn-modal-trigger" onclick="openModal('preservationModal')">
        <span>📖</span> The Infallible Guarantee of Dhikr (Inna Nahnu Nazzalna)
      </button>
      <button class="btn-modal-trigger" onclick="openModal('creationModal')">
        <span>🏺</span> Primordial Genesis & The Rebellion of Iblis (Salsal & Qiyas)
      </button>
      <button class="btn-modal-trigger" onclick="openModal('seductionModal')">
        <span>🛡️</span> The Strategy of Seduction & Sincerity (Al-Mukhliseen)
      </button>
      <button class="btn-modal-trigger" onclick="openModal('sujoodModal')">
        <span>🤲</span> Al-Sab' al-Mathani & The Cure of Sujood
      </button>
    </div>

    <div class="nav-tabs" id="plateTabs">
      {{TAB_BUTTONS_HTML}}
    </div>

    <div id="platesContainer">
      {{PLATES_HTML}}
    </div>

    <section class="audio-section">
      <div class="audio-header">
        <h3>Foundation Audio Syllabus Explorer</h3>
        <span>5 Lectures &bull; 01h 35m 03s &bull; Click to filter corresponding plates</span>
      </div>
      <div class="audio-grid">
        {{AUDIO_ITEMS_HTML}}
      </div>
    </section>
  </div>

  <!-- MODAL 1 -->
  <div class="modal-backdrop" id="preservationModal" onclick="closeOnBackdrop(event, 'preservationModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Seven-Fold Divine Guarantee of Dhikr (Inna Nahnu Nazzalna)</h3>
        <button class="modal-close" onclick="closeModal('preservationModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Indeed, it is We who sent down the Dhikr [the Reminder], and indeed, We will be its Guardian."
        </div>
        <h4>The Inviolable Fortress of Scripture</h4>
        <p>In classical Sunni exegesis (expounded by <strong>Imam at-Tabari</strong>, <strong>Imam ar-Razi</strong>, and <strong>Imam al-Qurtubi</strong>), this single verse stands as the foundational theological and historical bedrock guaranteeing the perpetual incorruptibility of the Holy Qur'an. Unlike previous scriptures whose physical preservation was entrusted to human scribes and rabbis—who subsequently altered, concealed, or lost them—Allah took the guardianship of this final Revelation upon Himself directly.</p>
        <h4>The Seven Layers of Rhetorical Fortification</h4>
        <p>Classical grammarians highlight seven emphatic particles (*Mu'akkidat*) packed into this short sentence:</p>
        <ul>
          <li><strong>Inna (إِنَّا):</strong> The emphatic particle of absolute certainty.</li>
          <li><strong>Nahnu (نَحْنُ):</strong> The royal sovereign pronoun asserting exclusive divine agency.</li>
          <li><strong>Nazzalna (نَزَّلْنَا):</strong> The verbal form indicating deliberate, measured revelation into human history.</li>
          <li><strong>Adh-Dhikr (الذِّكْرَ):</strong> Defining revelation as 'The Reminder' harmonizing with primordial fitrah.</li>
          <li><strong>Wa Inna (وَإِنَّا):</strong> Second affirmation initiating the divine preservation covenant.</li>
          <li><strong>Lahu (لَهُ):</strong> Pre-positioned pronoun signifying exclusivity of protection.</li>
          <li><strong>La-Hafizoon (لَحَافِظُونَ):</strong> The lam of emphasis attached to an active participle denoting eternal, unbroken preservation.</li>
        </ul>
        <h4>Historical & Empirical Vindication</h4>
        <p>Across fourteen centuries, through wars, library destructions, and political upheaval, the exact Arabic syllables of the Qur'an have been preserved identically in memory and manuscript from West Africa to East Asia, fulfilling this sovereign promise.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2 -->
  <div class="modal-backdrop" id="creationModal" onclick="closeOnBackdrop(event, 'creationModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Primordial Genesis from Sounding Mud & The Rebellion of Iblis</h3>
        <button class="modal-close" onclick="closeModal('creationModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And [remember] when your Lord said to the angels: 'I will create a mortal from sounding clay of altered mud. So when I have proportioned him and breathed into him of My Spirit, fall down before him in prostration.' So the angels prostrated—all of them entirely. Except Iblis..."
        </div>
        <h4>The Four Metamorphic Stages of Clay</h4>
        <p><strong>Imam Ibn Kathir</strong> details the stages of Adam's biological creation: from raw dust (*Turab*), into moist mud (*Teen*), into dark altered fermented mud (*Hama' Masnoon*), culminating in dry clay that resonates like pottery when struck (*Salsal*). This humblest earthly vessel was then elevated by the created divine Spirit (*Ruh*).</p>
        <h4>The Origin of Racism & False Analogy (Qiyas Batil)</h4>
        <p>Iblis refused to prostrate, grounding his insubordination in materialist arrogance: <em>'I will not bow to a mortal created from altered clay!'</em> As noted by <strong>Al-Hasan al-Basri</strong>, Iblis was the first to deploy false analogy, assuming that fire was inherently superior to clay. In his blinded vanity, he failed to see that clay possesses stability, humility, and the capacity to bear life, whereas fire is volatile, destructive, and consumed by ash.</p>
        <h4>The Universal Prostration of the Angels</h4>
        <p>The phrasing <em>Fasajada al-mala'ikatu kulluhum ajma'oon</em> emphasizes absolute angelic obedience. No true angel hesitated; Iblis fell because he was of the jinn (as explicitly clarified in Surah Al-Kahf 18:50) who possessed moral free will and chose treason.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3 -->
  <div class="modal-backdrop" id="seductionModal" onclick="closeOnBackdrop(event, 'seductionModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Strategy of Seduction & Sincerity (Al-Mukhliseen)</h3>
        <button class="modal-close" onclick="closeModal('seductionModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "[Iblis] said: 'My Lord, because You have put me in error, I will surely glamorize evil for them on earth and mislead them all—except Your sincere, devoted servants among them.' [Allah] said: 'This is a straight path binding upon Me: Indeed, over My servants you possess no authority...'"
        </div>
        <h4>The Warfare of Glamorization (Tazyeen)</h4>
        <p>Satan cannot create an atom of matter, nor can he physically force a human limb to commit sin. His entire stratagem relies upon <strong>Tazyeen</strong>—cosmetic decoration. He disguises destructive sins in the alluring vocabulary of sophistication, freedom, autonomy, and modern trend, making self-destruction look enlightened.</p>
        <h4>The Impenetrable Shield of Ikhlas</h4>
        <p>Iblis himself confessed his complete powerlessness before <strong>Al-Mukhliseen</strong>—those whose hearts are purified, singular, and devoted exclusively to Allah. Sincerity strips the devil of all leverage: Satan tempts human beings using worldly bait (wealth, fame, ego, sexual indulgence); but a soul whose heart desires only the pleasure of the Creator cannot be bought.</p>
        <h4>The Seven Tiered Gates of Jahannam</h4>
        <p>Those who voluntarily surrender their agency to demonic whispers are promised Hellfire, engineered with seven distinct, descending gates (*Sab'atu abwab*). As narrated from <strong>'Ali ibn Abi Talib</strong>, the punishments are layered in descending tiers, precisely calibrated to the depth of worldly defiance.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4 -->
  <div class="modal-backdrop" id="sujoodModal" onclick="closeOnBackdrop(event, 'sujoodModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Al-Sab' al-Mathani & The Cure for the Constricted Heart</h3>
        <button class="modal-close" onclick="closeModal('sujoodModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And We have certainly given you seven oft-repeated verses and the grand Qur'an... And We certainly know that your breast is constricted by what they say. So glorify your Lord with praise, and be among those who prostrate, and worship your Lord until there comes to you the certainty [death]."
        </div>
        <h4>The Seven Oft-Repeated (Al-Sab' al-Mathani)</h4>
        <p>Authenticated in <em>Sahih al-Bukhari</em> by the Prophet ﷺ, the <strong>Seven Oft-Repeated Verses</strong> are <strong>Surah Al-Fatihah</strong>. Possessing this divine treasure elevates the believer above all material empires. Hence the divine command: <em>La tamuddanna 'aynayka</em>—do not strain your eyes in covetous envy toward the transient luxuries given to worldly elites.</p>
        <h4>Divine Empathy for Human Pain</h4>
        <p>The Qur'an tenderly acknowledges the psychological burden of slander, mockery, and social hostility: <em>Wa laqad na'lamu annaka yadeequ sadruk</em>. God does not demand that His servants be emotionally numb; He validates the constriction of the chest caused by vicious words.</p>
        <h4>The Tripartite Spiritual Prescription</h4>
        <p>The divine remedy for acute emotional exhaustion and social grief is threefold:</p>
        <ul>
          <li><strong>Fa-sabbih bi-hamdi rabbik (Tasbih & Hamd):</strong> Exalting Allah with praise reorients the cognitive focus away from the hostility of human beings toward the transcendent perfection of the Creator.</li>
          <li><strong>Wa kun mina as-sajideen (Physical Sujood):</strong> Placing the forehead upon the dust discharges psychic pressure, humbles the ego, and brings the soul into the closest possible proximity to God.</li>
          <li><strong>Wa'bud rabbaka hatta ya'tiyaka al-yaqeen:</strong> Enduring in steadfast, serene worship until <em>Al-Yaqeen</em>—unanimously interpreted by classical authorities (*At-Tabari, Ibn Kathir*) as the arrival of death.</li>
        </ul>
      </div>
    </div>
  </div>

  <script>
    function selectPlate(plateNum) {
      document.querySelectorAll('.plate-section').forEach(sec => sec.classList.remove('active'));
      document.querySelectorAll('.tab-chip').forEach(tab => tab.classList.remove('active'));
      const targetSec = document.getElementById('plateSection' + plateNum);
      if (targetSec) targetSec.classList.add('active');
      const tabs = document.querySelectorAll('.tab-chip');
      if (tabs[plateNum - 1]) tabs[plateNum - 1].classList.add('active');
    }

    function openModal(id) {
      const modal = document.getElementById(id);
      if (modal) modal.classList.add('show');
    }

    function closeModal(id) {
      const modal = document.getElementById(id);
      if (modal) modal.classList.remove('show');
    }

    function closeOnBackdrop(e, id) {
      if (e.target.classList.contains('modal-backdrop')) {
        closeModal(id);
      }
    }

    function handleLiveSearch() {
      const query = document.getElementById('liveSearchInput').value.toLowerCase().trim();
      const plates = document.querySelectorAll('.plate-section');
      const tabs = document.querySelectorAll('.tab-chip');
      const statsBadge = document.getElementById('statsBadge');

      if (query === '') {
        plates.forEach(p => p.classList.remove('active'));
        document.getElementById('plateSection1').classList.add('active');
        tabs.forEach(t => t.classList.remove('active'));
        tabs[0].classList.add('active');
        document.querySelectorAll('.card-item').forEach(c => c.style.display = 'block');
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>5</b> Lectures &bull; <b>100%</b> Sunni Verified';
        return;
      }

      let matchedCount = 0;
      plates.forEach(plate => {
        let plateHasMatch = false;
        const plateCards = plate.querySelectorAll('.card-item');
        plateCards.forEach(card => {
          const searchData = card.getAttribute('data-search') || '';
          if (searchData.includes(query)) {
            card.style.display = 'block';
            plateHasMatch = true;
            matchedCount++;
          } else {
            card.style.display = 'none';
          }
        });
        if (plateHasMatch) {
          plate.classList.add('active');
        } else {
          plate.classList.remove('active');
        }
      });

      statsBadge.innerHTML = 'Found <b>' + matchedCount + ' Matches</b> for "' + query + '"';
    }

    function filterByMovement(movName) {
      const mapping = {
        "Movement 1": 1,
        "Movement 2": 2,
        "Movement 3 & 4": 3,
        "Movement 5 & 6": 5,
        "Movement 7 & 8": 7
      };
      if (mapping[movName]) {
        selectPlate(mapping[movName]);
        window.scrollTo({ top: 120, behavior: 'smooth' });
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('show'));
      }
    });
  </script>
</body>
</html>
"""

full_html = html_template.replace("{{TAB_BUTTONS_HTML}}", tab_buttons_html)\
                         .replace("{{PLATES_HTML}}", plates_html)\
                         .replace("{{AUDIO_ITEMS_HTML}}", audio_items_html)

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated Surah Al-Hijr Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
