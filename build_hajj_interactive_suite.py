#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Hajj Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Cataclysmic Tremor of the Hour & Sensory Dissolution (Zalzalat al-Sa'ah)
    2. Biological Embryology & Botanical Resurrection (Nutfah, Mudghah & Quivering Earth)
    3. The Ancient Sanctuary & Preservation of Multi-Confessional Houses of Worship
    4. The Parable of the Fly, Absolute Transcendence & The Abrahamic Call
- 6-Lecture Foundation Audio Syllabus Explorer (03h 33m 42s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_HAJJ_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_hajj_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_hajj_html_and_md import pages_data

# 6 Audio Foundation lectures syllabus (03h 33m 42s total)
audio_lectures = [
    ("22.Al-hajPart1a.opus", "The Cataclysmic Tremor of the Hour & Sensory Disruption", "Movement 1", "16m 42s"),
    ("22.Al-hajPart1b.opus", "Biological Embryology & Botanical Resurrection", "Movement 2", "20m 10s"),
    ("22.Al-hajPart1c.opus", "The Psychology of the Precipice & Conditional Worship", "Movement 3", "16m 27s"),
    ("22.Al-hajPart2.opus", "The Abrahamic Sanction, The Ancient House & Rites of Hajj", "Movement 4", "01h 03m 12s"),
    ("22.Al-hajPart3.opus", "The Metaphysics of Sacrifice, Taqwa & The Charter of Defense", "Movement 5", "37m 38s"),
    ("22.Al-hajPart4.opus", "Ruined Citadels, The Parable of the Fly & Abrahamic Identity", "Movement 6", "59m 31s")
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
  <title>Surah Al-Hajj — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
      gap: 12px;
    }
    .header-brand h1 {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.05em;
    }
    .header-brand span {
      font-size: 0.85rem;
      color: var(--text-muted);
    }
    .header-actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    .btn {
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-gold {
      background: var(--gold);
      color: var(--navy-deep);
      border: 1px solid var(--gold);
    }
    .btn-gold:hover {
      background: var(--gold-light);
    }
    .btn-outline {
      background: transparent;
      color: var(--text-muted);
      border: 1px solid var(--border-muted);
    }
    .btn-outline:hover {
      border-color: var(--gold);
      color: var(--white);
    }
    .search-panel {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .search-input-box {
      display: flex;
      gap: 10px;
      align-items: center;
    }
    .search-input-box input {
      flex: 1;
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 14px;
      color: var(--white);
      font-size: 0.88rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .search-input-box input:focus {
      border-color: var(--gold);
    }
    .search-stats {
      font-size: 0.78rem;
      color: var(--text-muted);
    }
    .deep-dive-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .audio-panel {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
    }
    .audio-panel h3 {
      font-size: 0.95rem;
      color: var(--gold);
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .audio-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
    }
    .audio-row {
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 8px 12px;
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
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.1);
      padding: 2px 6px;
      border-radius: 4px;
    }
    .audio-title {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--white);
    }
    .audio-sub {
      font-size: 0.7rem;
      color: var(--text-muted);
    }
    .audio-duration {
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--gold-light);
      white-space: nowrap;
    }
    .tab-bar {
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
      border-color: var(--gold);
      color: var(--gold);
    }
    .plate-section {
      display: none;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 24px;
    }
    .plate-section.active {
      display: block;
    }
    .plate-title-bar {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 14px;
      flex-wrap: wrap;
      gap: 12px;
    }
    .plate-title-bar h2 {
      font-size: 1.3rem;
      color: var(--white);
      margin-bottom: 4px;
    }
    .plate-title-bar p {
      color: var(--text-muted);
      font-size: 0.85rem;
    }
    .plate-badge-box {
      display: flex;
      gap: 8px;
    }
    .badge-gold {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      background: rgba(212, 175, 55, 0.15);
      color: var(--gold);
      border: 1px solid var(--gold);
      text-transform: uppercase;
    }
    .badge-emerald {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid var(--emerald);
      text-transform: uppercase;
    }
    .pillars-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
    }
    @media (max-width: 960px) {
      .pillars-layout { grid-template-columns: 1fr; }
    }
    .pillar-box {
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 14px;
    }
    .pillar-bar {
      margin-bottom: 12px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 8px;
    }
    .pillar-bar h3 {
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 2px;
    }
    .pillar-bar.cyan h3 { color: var(--cyan); }
    .pillar-bar.purple h3 { color: var(--purple); }
    .pillar-bar.emerald h3 { color: var(--emerald); }
    .pillar-bar.gold h3 { color: var(--gold); }
    .pillar-bar.rose h3 { color: var(--rose); }
    .pillar-bar p {
      font-size: 0.74rem;
      color: var(--text-muted);
    }
    .cards-wrapper {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .card-item {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px;
      transition: border-color 0.2s;
    }
    .card-item:hover {
      border-color: rgba(212, 175, 55, 0.4);
    }
    .card-title-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }
    .card-idx {
      font-size: 0.72rem;
      font-weight: 700;
      background: var(--navy-elevated);
      color: var(--gold);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }
    .card-title-row h4 {
      font-size: 0.85rem;
      color: var(--white);
    }
    .card-points {
      list-style-type: none;
      padding-left: 0;
    }
    .card-points li {
      font-size: 0.77rem;
      color: var(--text-muted);
      line-height: 1.45;
    }
    footer.suite-footer {
      border-top: 1px solid var(--border-muted);
      padding: 18px 0;
      font-size: 0.75rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .footer-left {
      display: flex;
      gap: 16px;
    }
    .footer-right {
      color: var(--gold);
      font-weight: 600;
    }
    /* Modal Styles */
    .modal-backdrop {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(5px);
      z-index: 9999;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    .modal-backdrop.show {
      display: flex;
    }
    .modal-card {
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 8px;
      max-width: 780px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
    }
    .modal-header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .modal-header h3 {
      font-size: 1.05rem;
      color: var(--gold);
    }
    .modal-close {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.3rem;
      cursor: pointer;
    }
    .modal-close:hover {
      color: var(--white);
    }
    .modal-body {
      padding: 20px;
      font-size: 0.85rem;
      color: var(--white);
      line-height: 1.6;
    }
    .modal-body h4 {
      color: var(--cyan);
      margin: 14px 0 6px 0;
      font-size: 0.92rem;
    }
    .modal-body p {
      margin-bottom: 10px;
      color: #d1d9e2;
    }
    .modal-body ul {
      margin-left: 20px;
      margin-bottom: 12px;
      color: #d1d9e2;
    }
    .modal-body li {
      margin-bottom: 4px;
    }
    .quote-box {
      background: var(--navy-elevated);
      border-left: 3px solid var(--gold);
      padding: 10px 14px;
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
        <span>SURAH AL-HAJJ &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_HAJJ_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/HAJJ_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/HAJJ_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across Al-Hajj (e.g., cataclysm, embryo, soil, precipice, ibrahim, sacrifice, defense, fly)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>6</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('cataclysmModal')">The Cataclysmic Tremor</button>
        <button class="btn btn-outline" onclick="openModal('embryoModal')">Embryology & Quivering Soil</button>
        <button class="btn btn-outline" onclick="openModal('sanctuaryModal')">The Ancient Sanctuary & Defense</button>
        <button class="btn btn-outline" onclick="openModal('parableModal')">The Parable of the Fly & Ease</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (03h 33m 42s TOTAL)</span>
        <span style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;">Click any lecture to jump to its corresponding plate</span>
      </h3>
      <div class="audio-grid">
        {{AUDIO_ITEMS_HTML}}
      </div>
    </div>

    <div class="tab-bar">
      {{TAB_BUTTONS_HTML}}
    </div>

    {{PLATES_HTML}}

    <footer class="suite-footer">
      <div class="footer-left">
        <span>Huurs Knowledge Systems</span>
        <span>&bull;</span>
        <span>Orthodox Sunni Source Discipline (Tabari, Ibn Kathir, Qurtubi, Razi, Baghawi)</span>
        <span>&bull;</span>
        <span>Zero External Speaker Attribution</span>
      </div>
      <div class="footer-right">
        READ. REFLECT. RETURN.
      </div>
    </footer>
  </div>

  <!-- MODAL 1: THE CATACLYSMIC TREMOR -->
  <div class="modal-backdrop" id="cataclysmModal" onclick="closeOnBackdrop(event, 'cataclysmModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Cataclysmic Tremor of the Hour & Sensory Dissolution</h3>
        <button class="modal-close" onclick="closeModal('cataclysmModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "O mankind, fear your Lord. Indeed, the earthquake of the Hour is an immense thing. On the Day you see it every nursing woman will be distracted from that which she was nursing, and every pregnant woman will drop her burden, and you will see the people as drunken, yet they will not be drunken, but the punishment of Allah is severe."
        </div>
        <h4>Cosmic Dismantling (*Zalzalat al-Sa'ah*)</h4>
        <p>Surah Al-Hajj opens with a metaphysical shockwave that disrupts the terrestrial sensorium. The opening earthquake is not a local geological fault; it is the comprehensive dissolution of planetary equilibrium, gravitational balance, and atmospheric order upon the blowing of the Horn.</p>
        <h4>The Severance of Maternal Instinct</h4>
        <p>Maternal affection is the strongest, most unselfish instinct embedded in creation. Yet the sheer dread of the Hour causes the nursing mother (<em>al-murdhi'ah</em>) to drop her baby in reflexive, involuntary panic—demonstrating that all worldly dependencies and bonds vanish before the divine presence.</p>
        <h4>The Stupefaction of Mankind (*Sukara wa Ma Hum Bi-Sukara*)</h4>
        <p>Humanity is observed staggering, disoriented, and incoherent as if heavily intoxicated with wine. Yet the Qur'an clarifies: they have consumed no intoxicating drink; rather, it is the devastating majesty and absolute reckoning of Allah that paralyzes the senses.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: EMBRYOLOGY & SOIL -->
  <div class="modal-backdrop" id="embryoModal" onclick="closeOnBackdrop(event, 'embryoModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Biological Embryology & Botanical Resurrection</h3>
        <button class="modal-close" onclick="closeModal('embryoModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "O mankind, if you should be in doubt about the Resurrection, then consider: We created you from dust, then from a sperm-drop, then from a clinging clot, and then from a lump of flesh, formed and unformed... And you see the earth barren, but when We send down upon it rain, it quivers and swells and grows of every pleasing kind."
        </div>
        <h4>The Seven-Fold Gestational Arc</h4>
        <p>The Qur'an refutes skepticism regarding bodily resurrection by guiding the human intellect through its own origin: starting from primordial dust, moving through the reproductive fluid (<em>nutfah</em>), the clinging embryo (<em>'alaqah</em>), and the differentiated tissue (<em>mudghah</em>) formed and unformed, into birth, physical vigor, and cognitive decrepitude (<em>ardhal al-'umur</em>).</p>
        <h4>The Botanical Epiphany (*Ihtazzat wa Rabat*)</h4>
        <p>The revelation draws an empirical parallel with the dead soil (<em>ardh hamidah</em>). Upon the descent of rain, the dormant mineral matrix vibrates (<em>ihtazzat</em>) and expands (<em>rabat</em>) with moisture and biological respiration, producing radiant, delightful pairs of vegetation (<em>zawjin baheej</em>).</p>
        <h4>The Rational Syllogism of Rebirth</h4>
        <p>Classical Sunni exegetes (<em>Al-Razi, Al-Baghawi</em>) emphasize the rational conclusion: He who initiates the astonishing transformation of inanimate clay into thinking, conscious human beings, and dead winter dust into blossoming orchards, possesses the effortless power to resurrect bodies from their graves.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: ANCIENT SANCTUARY & DEFENSE -->
  <div class="modal-backdrop" id="sanctuaryModal" onclick="closeOnBackdrop(event, 'sanctuaryModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Ancient Sanctuary & Preservation of Multi-Confessional Sanctuaries</h3>
        <button class="modal-close" onclick="closeModal('sanctuaryModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And proclaim to the people the Hajj; they will come to you on foot and on every lean camel; they will come from every deep ravine... Permission has been granted to those who are being fought, because they were wronged... were it not that Allah checks the people, some by means of others, there would have been demolished monasteries, churches, synagogues, and mosques in which the name of Allah is much mentioned."
        </div>
        <h4>Al-Bayt al-'Ateeq (The Ancient Liberated House)</h4>
        <p>The Ka'bah was assigned to Ibrahim as a sanctuary cleansed of idols, pride, and exploitation. It is designated <em>Al-Bayt al-'Ateeq</em> not only for its ancient antiquity, but because Allah liberated it (<em>'itq</em>) from the proprietary claim of any earthly monarch or empire.</p>
        <h4>The Miraculous Global Adhan</h4>
        <p>When Ibrahim was ordered to proclaim the pilgrimage across empty desert valleys, Allah promised: <em>"Yours is the proclamation; Ours is the conveyance."</em> Across centuries, countless millions answer this ancient call, traversing continents on foot and atop travel-worn mounts through every deep mountain pass (<em>fajjin 'ameeq</em>).</p>
        <h4>The Defense of Multi-Confessional Sanctuaries</h4>
        <p>Surah Al-Hajj introduces the constitutional permission for defense to protect civilization from tyrannical destruction. Without this divine check, the sacred enclaves where God's name is invoked would be annihilated: monastic hermitages (<em>sawami'</em>), Christian churches (<em>biya'</em>), Jewish synagogues (<em>salawat</em>), and Muslim mosques (<em>masajid</em>).</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: PARABLE OF THE FLY & EASE -->
  <div class="modal-backdrop" id="parableModal" onclick="closeOnBackdrop(event, 'parableModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Parable of the Fly, Absolute Transcendence & The Abrahamic Call</h3>
        <button class="modal-close" onclick="closeModal('parableModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "O mankind, an example is presented, so listen to it: Indeed, those you invoke besides Allah cannot create a fly, even if they gathered together for that purpose. And if the fly should steal away from them a thing, they could not recover it from him. Weak are both the pursuer and the pursued! They have not appraised Allah with true appraisal."
        </div>
        <h4>The Absolute Impotence of False Powers (*Mathal adh-Dhubab*)</h4>
        <p>The Qur'an issues an intellectual challenge to all human arrogance: even if all false gods, earthly rulers, and scientific alliances joined forces, they could never engineer or animate the intricate biological complexity of a common housefly.</p>
        <h4>Irreversible Predation & The Stolen Particle</h4>
        <p>When a fly lands on food, its digestive secretions dissolve nutrients instantaneously into chemical compounds before ingestion. Even if an idol or king wished to recover that stolen crumb, it is physically impossible. <em>"Dha'ufa al-talibu wal-matlub"</em> (weak is the seeker and the sought).</p>
        <h4>Religion Devoid of Hardship (*Ma Ja'ala Min Haraj*)</h4>
        <p>The surah concludes by calling humanity back to the perennial faith of father Ibrahim, who named believers <em>Muslimoon</em>. The divine law is established without crippling constriction or artificial hardship (<em>haraj</em>), inviting the soul to bow, prostrate, do good, and anchor its hope in the Best Guardian and Helper (<em>Ni'ma al-Mawla wa Ni'ma al-Naseer</em>).</p>
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
      if (e.target.id === id) closeModal(id);
    }

    function handleLiveSearch() {
      const query = document.getElementById('liveSearchInput').value.toLowerCase().trim();
      const plates = document.querySelectorAll('.plate-section');
      const tabs = document.querySelectorAll('.tab-chip');
      const statsBadge = document.getElementById('statsBadge');

      if (!query) {
        plates.forEach((p, idx) => {
          p.classList.toggle('active', idx === 0);
          p.querySelectorAll('.card-item').forEach(c => c.style.display = 'block');
        });
        tabs.forEach((t, idx) => t.classList.toggle('active', idx === 0));
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>6</b> Lectures &bull; <b>100%</b> Sunni Verified';
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
        "Movement 2": 1,
        "Movement 3": 2,
        "Movement 4": 3,
        "Movement 5": 4,
        "Movement 6": 6
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

print(f"Successfully generated Surah Al-Hajj Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
