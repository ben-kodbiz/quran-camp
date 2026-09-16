#!/usr/bin/env python3
"""
Huurs Studio - Surah Hud Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Severity of Istiqamah: The Verse That Grayed the Messenger (Fastaqim Kama Umirta)
    2. The Ark of Salvation, Boiling Tannoor & Dissolution of Bloodlines (Laysa min Ahlik)
    3. Cosmic Dominion & The Forelock of Creation (Aakhidhun bi-Nasiyatiha)
    4. Economic Justice (Baqiyyatullah) & The Sociological Immunity of Reformers (Ahluha Muslihoon)
- 8-Lecture Foundation Audio Syllabus Explorer (03h 19m 48s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_HUD_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_hud_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_hud_html_and_md import pages_data

# 8 Audio Foundation lectures syllabus
audio_lectures = [
    ("11.Hud1-5.opus", "Perfection of Scripture, The Economy of Istighfar & Divine Omniscience", "Movement 1", "21m"),
    ("11.Hud6-9.opus", "Guaranteed Sustenance, The Throne Upon Water & Qualitative Excellence", "Movement 1", "23m"),
    ("11.Hud10-17.opus", "Psychological Volatility, The Ten Surahs Challenge & The Anchored Soul", "Movement 2", "21m"),
    ("11.Hud18-49.opus", "The Epic of Nuh: Oligarchic Contempt, The Ark, Deluge & The Drowned Son", "Movement 3 & 4", "56m"),
    ("11.Hud50-65.opus", "Prophetic Calling to 'Ad & Thamud: Forelock Metaphysics & The Sonic Blast", "Movement 5", "17m"),
    ("11.Hud66-77.opus", "Angelic Tidings to Ibrahim, Sarah's Wonder & Pleading for Sodom", "Movement 6", "16m"),
    ("11.Hud78-97.opus", "The Agony of Lut, Rain of Sijjeel & Shu'ayb's Financial Manifesto in Madyan", "Movement 6 & 7", "20m"),
    ("11.Hud98-123.opus", "Pharaoh to the Fire, The Graying Command of Istiqamah & Sovereign Return", "Movement 7 & 8", "26m")
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
  <title>Surah Hud — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>SURAH HUD &bull; MASTER CARTOGRAPHY &amp; INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_HUD_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download PDF Compendium (10 Plates)
        </a>
        <a href="../07_MINDMAP/HUD_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          View Mindmap HTML
        </a>
      </div>
    </header>

    <!-- Deep Exegetical Modals Section -->
    <div class="modals-bar">
      <button class="btn-modal-trigger" onclick="openModal('istiqamahModal')">
        <span>⚖️📜</span> The Severity of Istiqamah: The Verse that Grayed the Prophet
      </button>
      <button class="btn-modal-trigger" onclick="openModal('arkModal')">
        <span>🌊🚢</span> The Ark of Nuh, The Boiling Oven & Severed Bloodlines
      </button>
      <button class="btn-modal-trigger" onclick="openModal('forelockModal')">
        <span>🦁⚡</span> Prophetic Defiance & Holding Every Creature by Its Forelock
      </button>
      <button class="btn-modal-trigger" onclick="openModal('reformModal')">
        <span>🏛️🌱</span> Economic Justice (Baqiyyatullah) & The Immunity of Reformers
      </button>
    </div>

    <!-- Live Search & Stats -->
    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Search 64 analytical cards, theological themes, classical citations..." oninput="handleLiveSearch()">
      </div>
      <div id="statsBadge" class="badge-gold">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>8</b> Lectures &bull; <b>100%</b> Sunni Verified
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

    <!-- 8 Audio Syllabus Explorer -->
    <div class="audio-section">
      <div class="audio-header">
        <div>
          <h3>Deeper Thought Audio Foundation Syllabus (8 Movements)</h3>
          <span>Complete Exegetical Audio Arc &bull; 03 Hours 19 Minutes 48 Seconds &bull; Anchored in Sunni Classical Tafsir</span>
        </div>
        <span class="badge-gold">8 Opus Modules</span>
      </div>
      <div class="audio-grid">
        {{AUDIO_ITEMS_HTML}}
      </div>
    </div>

    <footer class="suite-footer">
      <div>Huurs Studio &bull; Deeper Thought Series &bull; Surah Hud (The Prophetic Resilience)</div>
      <div>Operating Philosophy: <b>READ. REFLECT. RETURN.</b> &bull; 100% Sunni Classical Fidelity</div>
    </footer>
  </div>

  <!-- MODAL 1: The Severity of Istiqamah -->
  <div class="modal-backdrop" id="istiqamahModal" onclick="closeOnBackdrop(event, 'istiqamahModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Severity of Istiqamah: The Verse That Grayed the Messenger ﷺ</h3>
        <button class="modal-close" onclick="closeModal('istiqamahModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "So stand firm and upright as you have been commanded, along with those who turn in repentance with you, and do not transgress; indeed He is Seeing of what you do. And do not incline toward those who do wrong, lest the Fire touch you..."
        </div>
        <h4>The White Hairs of Prophetic Awe</h4>
        <p>In <em>Sunan at-Tirmidhi</em>, Abu Bakr as-Siddiq observed gray hairs appearing in the beard of the Prophet Muhammad ﷺ, remarking: <em>"O Messenger of Allah, you have aged!"</em> The Prophet ﷺ answered: <strong>"Shayyabatni Hud wa Akhawatuha"</strong> (Surah Hud and its sisters have aged me!). Classical exegetes (Ibn 'Abbas, Al-Qurtubi, Ibn Kathir) note that no verse in the entire Qur'an was revealed upon the Prophet that was more severe, demanding, or weighty upon his soul than <em>"Fastaqim kama umirta"</em>.</p>
        <h4>The Razor's Edge: Between Laxity and Fanaticism</h4>
        <p><em>Istiqamah</em> is not merely passive ritual observance; it is unbending uprightness under intense trial, persecution, and social hostility. The divine command adds two crucial conditions:
          <br>1. <strong>"Kama Umirta" (As Commanded):</strong> Uprightness must be calibrated to divine revelation, not human whim, cultural traditions, or emotional preferences.
          <br>2. <strong>"Wa La Tatghaw" (And Do Not Transgress):</strong> It strictly forbids fanaticism, extremism, and exceeding divinely revealed boundaries. True uprightness maintains a razor-sharp balance between negligence (*Tafreet*) and extremism (*Tughyan*).
        </p>
        <h4>The Absolute Ban on Incline to Tyrants (Wa La Tarkanoo)</h4>
        <p>The command is immediately reinforced with a terrifying warning: <em>"And do not incline toward those who do wrong (Wa La Tarkanoo), lest the Fire touch you!"</em> Imam al-Qurtubi explains that <em>Ar-Rukoon</em> signifies even the slightest psychological leaning, flattering, compromising, or justifying tyrannical regimes. If merely sympathizing with oppressors invites the Fire, what of actively aiding or executing their tyranny?</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: The Ark of Nuh -->
  <div class="modal-backdrop" id="arkModal" onclick="closeOnBackdrop(event, 'arkModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Ark of Nuh, The Boiling Oven & Severed Bloodlines</h3>
        <button class="modal-close" onclick="closeModal('arkModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And it sailed with them through waves like mountains, and Nuh called to his son who was apart: 'O my son, embark with us and do not be with the disbelievers!'... He said: 'O Nuh, indeed he is not of your family; indeed, his conduct is unrighteous...'"
        </div>
        <h4>The Cosmic Sign: The Boiling Tannoor</h4>
        <p>When the appointed time matured, subterranean water erupted violently from a domestic clay baking oven (*Farat-tannoor*), inverting fire into water to trigger the planetary deluge. The Ark had no sails, oars, or rudders; its course across mountainous waves (*Mawjin kal-jibal*) was steered exclusively by the Divine Name: <em>"Bismillahi majreeha wa mursaaha"</em>.</p>
        <h4>The Mountain Sanctuary Fallacy</h4>
        <p>Nuh witnessed his rebellious son clinging to a rocky outcrop and pleaded in paternal heartbreak: <em>"Ya bunayya-rkab ma'ana!"</em> The son placed his faith in physical topography: <em>"I will take refuge on a mountain to protect me."</em> Nuh replied with eternal theological truth: <em>"There is no protector today from the decree of Allah except whom He shows mercy!"</em> Before another word could be spoken, a colossal wave surged between them, and the son was swallowed by the dark abyss.</p>
        <h4>The Dissolution of Genetic Lineage (Laysa min Ahlik)</h4>
        <p>When Nuh pleaded for his son based on the divine promise to save his household, the Creator answered with an absolute decree that revolutionized sacred sociology: <strong>"Innahu laysa min ahlika, innahu 'amalun ghayru salih"</strong> (Indeed he is not of your family; indeed his conduct is unrighteous). In the Divine Court, biological pedigree and bloodlines are completely meaningless without spiritual alignment in Tawhid.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Forelock of Creation -->
  <div class="modal-backdrop" id="forelockModal" onclick="closeOnBackdrop(event, 'forelockModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Prophetic Defiance & Holding Every Creature by Its Forelock</h3>
        <button class="modal-close" onclick="closeModal('forelockModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Indeed, I have relied upon Allah, my Lord and your Lord. There is not a moving creature but that He holds it by its forelock. Indeed, my Lord is on a straight path."
        </div>
        <h4>The Solitary Prophet Before an Empire of Giants</h4>
        <p>Prophet Hud stood completely alone against 'Ad—a civilization of physical giants renowned for unmatched military architecture and stone pillars. Accused by their priests of being struck with insanity by their stone idols, Hud responded with magnificent, unshakeable defiance: <em>"Plot against me, all of you together, and give me no respite!"</em></p>
        <h4>The Forelock of Subjugation (Aakhidhun bi-Nasiyatiha)</h4>
        <p>Hud revealed the source of his superhuman fearlessness: <strong>Every living creature on earth is held by its forelock (*Nasiyah*) in the hand of Almighty Allah</strong>. In ancient Arabic culture, grasping someone by the forelock signified complete, humiliating subjugation and helplessness. Because the forelocks of all tyrants, armies, and bullies are physically gripped by God, the believer fears no earthly power.</p>
        <h4>The Straight Path of Divine Governance</h4>
        <p>Hud concludes: <em>"Inna Rabbee 'ala siratin mustaqeem"</em> (Indeed, my Lord is on a straight path). Divine administration is not erratic, tyrannical, or whimsical; it governs the universe with absolute justice, ensuring that arrogance is eventually pulverized and righteous perseverance is eternally vindicated.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Economic Justice & Reformers -->
  <div class="modal-backdrop" id="reformModal" onclick="closeOnBackdrop(event, 'reformModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Economic Justice (Baqiyyatullah) & The Immunity of Reformers</h3>
        <button class="modal-close" onclick="closeModal('reformModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "I only desire reform to the best of my ability. And my success is not but through Allah; upon Him I rely, and unto Him I return... And your Lord would never destroy the cities unjustly while their people were reformers."
        </div>
        <h4>Shu'ayb's Financial Manifesto in Madyan</h4>
        <p>Prophet Shu'ayb linked monotheistic worship directly to commercial market integrity, forbidding fraudulent weights and scales (*Al-Mikyala wal-Meezan*). He introduced the concept of <strong>Baqiyyatullah</strong>: that a modest, lawful profit (*Halal*) blessed by God possesses far greater enduring wealth and peace than vast fortunes accumulated through predatory deception and usurious short-changing.</p>
        <h4>The Secular Capitalist Objection</h4>
        <p>The merchants of Madyan sneered: <em>"Does your prayer command you that we stop doing what we will with our wealth?!"</em> They demanded a total partition between sacred morality and economic enterprise. Shu'ayb responded with the timeless motto of all true prophets: <em>"In ureedu illal-islaha ma-stata'tu"</em> (I only desire reform to the best of my ability; and my success is only through Allah).</p>
        <h4>The Sociological Law: Muslihoon vs. Salihun</h4>
        <p>Surah Hud establishes a fundamental law of civilizational survival: <em>"Wa ma kana Rabbuka li-yuhlikal-qura bi-zulmin wa ahluha muslihoon."</em> Allah never destroys a society unjustly <strong>so long as its people are active reformers (*Muslihoon*)</strong>. Personal, passive piety (*Salihun*) does not grant societal immunity if people remain silent before systemic corruption; only proactive public reform preserves a civilization from divine doom.</p>
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>8</b> Lectures &bull; <b>100%</b> Sunni Verified';
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
        "Movement 5": 5,
        "Movement 6": 6,
        "Movement 6 & 7": 7,
        "Movement 7 & 8": 8
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

print(f"Successfully generated Surah Hud Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
