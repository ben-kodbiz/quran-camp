#!/usr/bin/env python3
"""
Huurs Studio - Surah Yunus Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals:
    1. Cosmic Chronometry: Solar Diya' vs Lunar Noor & The Architecture of Divine Measure
    2. The Beatific Vision: 'Az-Ziyadah' in Dar as-Salam (Sunni Affirmation of the Divine Countenance)
    3. The Fourfold Quranic Medicine: Maw'izah, Shifa', Huda, and Rahmah for the Diseased Breast
    4. The Preserved Corpse of Pharaoh & The Miraculous Repentance of Nineveh
- 10-Lecture Foundation Audio Syllabus Explorer (03h 35m 31s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_YUNUS_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_yunus_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_yunus_html_and_md import pages_data

# 10 Audio Foundation lectures syllabus
audio_lectures = [
    ("10.Yunus0introduction.opus", "Cosmic Order, Divine Sovereignty & The Architecture of Revelation", "Movement 1", "30m"),
    ("10.Yunus1-10.opus", "Signs in the Heavens, Solar Diya' & Lunar Noor, Truth vs Speculation", "Movement 1 & 2", "22m"),
    ("10.Yunus11-21.opus", "Human Ingratitude, Maritime Storm Metaphor & Rash Prayers Rebuffed", "Movement 2", "17m"),
    ("10.Yunus22-25.opus", "The Mirage of Mortal Splendor (Dunya as Vanishing Vegetation)", "Movement 3", "19m"),
    ("10.Yunus26-38.opus", "Dar as-Salam, The Beatific Vision (Az-Ziyadah) & Cosmic Stewardship", "Movement 3 & 4", "20m"),
    ("10.Yunus39-55.opus", "The Deniers Challenged, The Preserved Book & Reality of the Hereafter", "Movement 4 & 5", "23m"),
    ("10.Yunus56-63.opus", "The Fourfold Cure: Maw'izah, Shifa', Huda, Rahmah & Awliya Allah", "Movement 5", "20m"),
    ("10.Yunus64-82.opus", "Prophetic Archetypes: Nuh's Steadfastness & Musa Confronting the Magicians", "Movement 6", "20m"),
    ("10.Yunus83-95.opus", "Exodus, The Drowning of Pharaoh & The Preserved Corpse (Ayah li-Man Khalfak)", "Movement 7", "19m"),
    ("10.Yunus96-109.opus", "The Repentance of Nineveh, Faith Unto Death & Absolute Divine Decree", "Movement 8", "25m")
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
  <title>Surah Yunus — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
      color: var(--gold);
    }
    .controls-bar {
      display: flex;
      gap: 14px;
      margin-bottom: 20px;
      align-items: center;
      flex-wrap: wrap;
    }
    .search-input-wrap {
      flex: 1;
      min-width: 260px;
      position: relative;
    }
    .search-input-wrap input {
      width: 100%;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 16px 10px 38px;
      color: var(--white);
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .search-input-wrap input:focus {
      border-color: var(--gold);
    }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.9rem;
    }
    .nav-tabs {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 6px;
      margin-bottom: 20px;
    }
    .tab-chip {
      background: var(--navy-card);
      color: var(--text-muted);
      border: 1px solid var(--border-muted);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
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
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
    }
    .plate-title-bar h2 {
      font-size: 1.15rem;
      color: var(--gold-light);
      margin-bottom: 4px;
    }
    .plate-title-bar p {
      font-size: 0.82rem;
      color: var(--text-muted);
    }
    .plate-badge-box {
      display: flex;
      gap: 8px;
      align-items: center;
      flex-shrink: 0;
    }
    .badge-gold {
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
    }
    .badge-emerald {
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid var(--emerald);
      color: var(--emerald);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
    }
    .pillars-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    @media (max-width: 980px) {
      .pillars-layout {
        grid-template-columns: 1fr;
      }
    }
    .pillar-box {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }
    .pillar-bar {
      padding: 14px 18px;
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
      gap: 12px;
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
      align-items: baseline;
      gap: 8px;
      margin-bottom: 6px;
    }
    .card-idx {
      font-size: 0.7rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 1px 5px;
      border-radius: 3px;
    }
    .card-title-row h4 {
      font-size: 0.86rem;
      color: var(--white);
    }
    .card-points {
      list-style-type: none;
      padding-left: 0;
    }
    .card-points li {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 3px;
      position: relative;
      padding-left: 12px;
    }
    .card-points li::before {
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 0.75rem;
    }
    .audio-section {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 22px;
      margin-bottom: 24px;
    }
    .audio-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 10px;
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
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 10px;
    }
    .audio-row {
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s;
    }
    .audio-row:hover {
      border-color: var(--gold);
      background: #19263e;
    }
    .audio-meta-left {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .audio-num {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.25);
      border-radius: 4px;
      padding: 2px 6px;
    }
    .audio-title {
      font-size: 0.83rem;
      font-weight: 600;
      color: var(--white);
    }
    .audio-sub {
      font-size: 0.72rem;
      color: var(--text-muted);
    }
    .audio-duration {
      font-size: 0.75rem;
      color: var(--gold-light);
      font-weight: 600;
      flex-shrink: 0;
    }
    .modals-bar {
      display: flex;
      gap: 10px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }
    .btn-modal-trigger {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--gold-light);
      padding: 10px 16px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-modal-trigger:hover {
      border-color: var(--gold);
      background: var(--navy-elevated);
      color: var(--gold);
    }
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(4, 7, 13, 0.85);
      backdrop-filter: blur(4px);
      display: none;
      justify-content: center;
      align-items: center;
      z-index: 1000;
      padding: 20px;
    }
    .modal-backdrop.show {
      display: flex;
    }
    .modal-window {
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 10px;
      max-width: 820px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 10px 30px rgba(0,0,0,0.7);
    }
    .modal-header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      background: var(--navy-card);
      z-index: 10;
    }
    .modal-header h3 {
      color: var(--gold);
      font-size: 1.05rem;
    }
    .modal-close {
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      cursor: pointer;
      line-height: 1;
    }
    .modal-close:hover {
      color: var(--rose);
    }
    .modal-body {
      padding: 20px 24px;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #cbd5e1;
    }
    .modal-body h4 {
      color: var(--gold-light);
      margin: 16px 0 6px 0;
      font-size: 0.95rem;
    }
    .modal-body p {
      margin-bottom: 12px;
    }
    .modal-body .quote-box {
      background: var(--navy-elevated);
      border-left: 3px solid var(--gold);
      padding: 12px 16px;
      margin-bottom: 16px;
      font-style: italic;
      color: var(--gold-light);
      border-radius: 0 6px 6px 0;
    }
    footer.suite-footer {
      margin-top: 30px;
      padding-top: 20px;
      border-top: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--text-muted);
      font-size: 0.8rem;
      flex-wrap: wrap;
      gap: 12px;
    }
  </style>
</head>
<body>
  <div class="suite-shell">
    <header class="suite-header">
      <div class="header-brand">
        <h1>HUURS STUDIO</h1>
        <span>SURAH YUNUS &bull; MASTER CARTOGRAPHY &amp; INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_YUNUS_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download PDF Compendium (10 Plates)
        </a>
        <a href="../07_MINDMAP/YUNUS_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          View Mindmap HTML
        </a>
      </div>
    </header>

    <!-- Deep Exegetical Modals Section -->
    <div class="modals-bar">
      <button class="btn-modal-trigger" onclick="openModal('chronometryModal')">
        <span>☀️🌙</span> Cosmic Chronometry: Solar Diya' vs Lunar Noor
      </button>
      <button class="btn-modal-trigger" onclick="openModal('ziyadahModal')">
        <span>👁️✨</span> Beatific Vision: 'Az-Ziyadah' in Dar as-Salam
      </button>
      <button class="btn-modal-trigger" onclick="openModal('shifaModal')">
        <span>🌿💧</span> Fourfold Medicine: Maw'izah, Shifa', Huda, Rahmah
      </button>
      <button class="btn-modal-trigger" onclick="openModal('pharaohModal')">
        <span>🌊🏛️</span> Preserved Corpse of Pharaoh & Repentance of Nineveh
      </button>
    </div>

    <!-- Live Search & Stats -->
    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Search 64 analytical cards, theological themes, classical citations..." oninput="handleLiveSearch()">
      </div>
      <div id="statsBadge" class="badge-gold">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>10</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="nav-tabs" id="navTabsContainer">
      {{TAB_BUTTONS_HTML}}
    </div>

    <!-- Plates Container -->
    <div id="platesContainer">
      {{PLATES_HTML}}
    </div>

    <!-- 10 Audio Syllabus Explorer -->
    <div class="audio-section">
      <div class="audio-header">
        <div>
          <h3>Deeper Thought Audio Foundation Syllabus (10 Movements)</h3>
          <span>Complete Exegetical Audio Arc &bull; 03 Hours 35 Minutes 31 Seconds &bull; Anchored in Sunni Classical Tafsir</span>
        </div>
        <span class="badge-gold">10 Opus Modules</span>
      </div>
      <div class="audio-grid">
        {{AUDIO_ITEMS_HTML}}
      </div>
    </div>

    <footer class="suite-footer">
      <div>Huurs Studio &bull; Deeper Thought Series &bull; Surah Yunus (The Prophetic Jonah)</div>
      <div>Operating Philosophy: <b>READ. REFLECT. RETURN.</b> &bull; 100% Sunni Classical Fidelity</div>
    </footer>
  </div>

  <!-- MODAL 1: Cosmic Chronometry -->
  <div class="modal-backdrop" id="chronometryModal" onclick="closeOnBackdrop(event, 'chronometryModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Cosmic Chronometry: Solar Diya' vs Lunar Noor</h3>
        <button class="modal-close" onclick="closeModal('chronometryModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "It is He who made the sun a shining light (Diya') and the moon a reflected radiance (Noor) and determined for it phases - that you may know the number of years and account [of time]. Allah has not created this except in truth. He details the signs for a people who know."
        </div>
        <h4>The Linguistic Distinction: Diya' vs. Noor</h4>
        <p>In classical Arabic lexicography and exegetical scholarship (At-Tabari, Al-Qurtubi, Ibn Kathir), <em>Diya'</em> denotes an inherent, self-generating blazing luminary emitting heat and radiation, whereas <em>Noor</em> signifies a gentle, cool, reflected illumination. Surah Yunus specifically attributes <em>Diya'</em> exclusively to the sun and <em>Noor</em> to the moon, establishing a precise physical and semantic hierarchy that aligns with cosmic reality.</p>
        <h4>The Determination of Mansions (Manazil)</h4>
        <p>Allah ordained twenty-eight lunar stations (<em>Manazil</em>) through which the moon traverses every month, allowing humanity to establish calendar reckoning, worship schedules (Hajj, Ramadan), and civil contracts without ambiguity. This precision demonstrates that the universe is governed not by blind chance, but by deliberate, measured truth (<em>bil-Haqq</em>).</p>
        <h4>Cognitive Purpose of the Cosmos</h4>
        <p>The alternation of night and day is designated as a sign for the mindful (<em>Li-Qawmin Yattaqun</em>). Those who reduce nature to secular mechanics overlook the ontological signature of the Designer, failing to recognize that celestial bodies are divine signposts directing human consciousness back toward its Originator.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: The Beatific Vision -->
  <div class="modal-backdrop" id="ziyadahModal" onclick="closeOnBackdrop(event, 'ziyadahModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Beatific Vision: 'Az-Ziyadah' in Dar as-Salam</h3>
        <button class="modal-close" onclick="closeModal('ziyadahModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "For them who have done good is the best reward [Al-Husna] and extra [Az-Ziyadah]. No darkness will cover their faces, nor humiliation. Those are companions of Paradise; they will abide therein eternally."
        </div>
        <h4>The Hadith of Suhayb ar-Rumi in Sahih Muslim</h4>
        <p>The Prophet Muhammad ﷺ explicitly elucidated this verse in an authentic narration recorded in <em>Sahih Muslim</em>: When the dwellers of Paradise enter Paradise, Allah Blessed and Exalted will say: <em>"Do you desire that I give you something more?"</em> They will reply: <em>"Have You not brightened our faces? Have You not admitted us to Paradise and saved us from the Fire?"</em> Thereupon Allah will remove the veil, and they will not have been granted anything more beloved to them than beholding the Countenance of their Lord (<em>An-Nazru ila Wajhi Rabbihim</em>).</p>
        <h4>Sunni Orthodoxy vs. Mu'tazilite Denial</h4>
        <p>Imam At-Tabari, Imam Ibn Kathir, and Al-Baghawi establish that <em>Al-Husna</em> represents Paradise itself, while <em>Az-Ziyadah</em> represents the supreme delight of directly gazing upon the Divine Countenance. This is a foundational creedal tenet of <em>Ahl as-Sunnah wal-Jama'ah</em>, refuting the rationalistic allegorizations of the Mu'tazilah who denied the beatific vision in the Hereafter.</p>
        <h4>The Psychology of Ihsan</h4>
        <p>Those who worshipped Allah in the earthly realm as though they saw Him (the station of <em>Ihsan</em>) are rewarded in Dar as-Salam by being granted the unmediated sight of the Divine Reality. While the faces of the damned are smothered in darkness (<em>Qataron</em>) and degradation, the faces of the people of Ihsan radiate with unadulterated tranquility.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: The Fourfold Medicine -->
  <div class="modal-backdrop" id="shifaModal" onclick="closeOnBackdrop(event, 'shifaModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Fourfold Quranic Medicine: Maw'izah, Shifa', Huda, Rahmah</h3>
        <button class="modal-close" onclick="closeModal('shifaModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "O mankind, there has come to you instruction [Maw'izah] from your Lord and healing [Shifa'] for what is in the breasts and guidance [Huda] and mercy [Rahmah] for the believers. Say, 'In the bounty of Allah and in His mercy - in that let them rejoice; it is better than what they accumulate.'"
        </div>
        <h4>The Sequential Therapeutic Arc</h4>
        <p>Imam Fakhr ad-Din ar-Razi in <em>Mafatih al-Ghayb</em> notes the meticulous order of these four spiritual stages:
          <br>1. <strong>Maw'izah (Instruction/Admonition):</strong> Shakes the dormant soul out of heedlessness through vivid warnings and moral awakenings.
          <br>2. <strong>Shifa' (Healing of the Breast):</strong> Purges the heart of chronic pathologies—doubt (<em>Shakk</em>), hypocrisy (<em>Nifaq</em>), rancor (<em>Ghill</em>), and arrogance (<em>Kibr</em>).
          <br>3. <strong>Huda (Constructive Guidance):</strong> Plants divine principles, sound theological convictions, and ethical clarity into the freshly sanitized heart.
          <br>4. <strong>Rahmah (Transfiguring Mercy):</strong> Engulfs the believer in perpetual serenity, spiritual illumination, and the ultimate felicity of Paradise.
        </p>
        <h4>The True Metric of Wealth: Al-Fadl and Ar-Rahmah</h4>
        <p>Ibn 'Abbas explained that <em>Fadl Allah</em> is sacred knowledge (the Qur'an) and <em>Rahmah</em> is Islam itself. The believer is commanded to exult and rejoice in revelation rather than the accumulation of perishable worldly assets, for material wealth vanishes upon death while the Qur'anic remedy endures across eternity.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Preserved Corpse of Pharaoh -->
  <div class="modal-backdrop" id="pharaohModal" onclick="closeOnBackdrop(event, 'pharaohModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Preserved Corpse of Pharaoh & Miraculous Repentance of Nineveh</h3>
        <button class="modal-close" onclick="closeModal('pharaohModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "So today We will save you in your body that you may be to those who succeed you a sign [Ayatan]. And indeed, many among the people, of Our signs, are heedless... Why was there not a single city that believed so its faith benefited it except the people of Jonah? When they believed, We removed from them the punishment of disgrace in worldly life and granted them enjoyment for a time."
        </div>
        <h4>The Rejection of Coerced Deathbed Faith</h4>
        <p>When the parting waves of the Red Sea collapsed upon Pharaoh and drowning overtook him, he declared: <em>"I believe that there is no deity except that in whom the Children of Israel believe, and I am of the Muslims."</em> The divine response shattered his desperate bargain: <em>"Al-ana wa qad 'asayta qablu?"</em> (Now?! While you previously rebelled and were of the corrupters?). Sunni consensus affirms that repentance at the agonal death rattle (<em>Al-Ghargharah</em>) or upon the sensory arrival of physical punishment is null and void.</p>
        <h4>The Physical Sign: Al-Yazfahu bi-Badanik</h4>
        <p>The Israelites doubted Pharaoh's death, suspecting his tyrannical immortality. Allah commanded the sea to cast his lifeless, waterlogged body onto a high hill so that his subjects could inspect his mortal defeat. The preservation of his physical form stands as an everlasting sign (<em>Ayatan li-Man Khalfak</em>) for all tyrannical despots across time.</p>
        <h4>The Exceptional Pardon of Nineveh</h4>
        <p>In the entire annals of sacred history, only one community broke the theological law of delayed repentance: the people of Prophet Yunus (Jonah) in Nineveh. When Yunus departed and dark clouds of retribution gathered over their horizon, the entire populace—men, women, suckling infants, and livestock—poured onto the mountains in tearful, sincere contrition before the final stroke of destruction descended. Allah uniquely lifted the temporal doom from them, making Nineveh a solitary beacon of divine clemency.</p>
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>10</b> Lectures &bull; <b>100%</b> Sunni Verified';
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
        "Movement 1 & 2": 2,
        "Movement 2": 2,
        "Movement 3": 3,
        "Movement 3 & 4": 4,
        "Movement 4 & 5": 4,
        "Movement 5": 5,
        "Movement 6": 6,
        "Movement 7": 7,
        "Movement 8": 8
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

print(f"Successfully generated Surah Yunus Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
