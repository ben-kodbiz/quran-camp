#!/usr/bin/env python3
"""
Huurs Studio - Surah Ta-Ha Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Solace of Revelation & The Sacred Ground of Tuwa (Li-Tashqa & Tuwa)
    2. The Architecture of Inner Fortitude & Gentle Speech (Sharh as-Sadr & Qawlan Layyina)
    3. The Epistemological Victory of Truth & Defiance of Crucifixion (Saharatu Sujjadan)
    4. The Suffocation of Heedlessness & Adam's Shield (Ma'eeshatan Danka & Fa-la Yashqa)
- 4-Lecture Foundation Audio Syllabus Explorer (04h 05m 17s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_TAHA_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_taha_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_taha_html_and_md import pages_data

# 4 Audio Foundation lectures syllabus (04h 05m 17s total)
audio_lectures = [
    ("20.Ta-haPart1.opus", "The Solace of Revelation, Ar-Rahman's Throne, The Fire of Tuwa & The Command of Prayer", "Movement 1", "48m 03s"),
    ("20.Ta-haPart2.opus", "The Du'a of Expansiveness, Past Divine Mercies, River Taboot & Gentle Speech to Pharaoh", "Movement 2", "57m 46s"),
    ("20.Ta-haPart3.opus", "The Festival Contest, Devouring Staff, Defiance of Crucifixion & The Dry Sea Highway", "Movement 3", "01h 03m 42s"),
    ("20.Ta-haPart4.opus", "As-Samiri's Golden Calf, Musa's Wrath, Blind Resurrection & The Covenant with Adam", "Movement 4", "01h 15m 44s")
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
  <title>Surah Ta-Ha — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
    }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.95rem;
    }
    .search-stats {
      font-size: 0.8rem;
      color: var(--text-muted);
      padding: 6px 12px;
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
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
        <span>SURAH TA-HA &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_TAHA_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/TAHA_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/TAHA_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across Surah Ta-Ha (e.g., tuwa, staff, harun, pharaoh, sorcerers, samiri, adam)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>4</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('solaceModal')">The Solace of Tuwa</button>
        <button class="btn btn-outline" onclick="openModal('expansivenessModal')">Inner Fortitude & Mildness</button>
        <button class="btn btn-outline" onclick="openModal('sorcerersModal')">Sorcerers' Prostration</button>
        <button class="btn btn-outline" onclick="openModal('remembranceModal')">Adam & Remembrance</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (04h 05m 17s TOTAL)</span>
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

  <!-- MODAL 1: THE SOLACE OF TUWA -->
  <div class="modal-backdrop" id="solaceModal" onclick="closeOnBackdrop(event, 'solaceModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Solace of Revelation & The Sacred Ground of Tuwa</h3>
        <button class="modal-close" onclick="closeModal('solaceModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Ta-Ha. We have not sent down to you the Qur'an that you be distressed, but only as a reminder for those who fear... Indeed, I am your Lord, so remove your sandals. Indeed, you are in the sacred valley of Tuwa... And establish prayer for My remembrance."
        </div>
        <h4>Dismantling the Myth of Spiritual Misery (*Li-Tashqa*)</h4>
        <p>Surah Ta-Ha begins by completely disarming the pagan accusation that divine revelation is a source of exhaustion and grief. The Qur'an was sent down not to crush the human spirit, but as an illumination (*Nur*) and an expansive reminder (*Tadhkirah*) that anchors the wandering soul in peace.</p>
        <h4>Stripping the Sandals of the Ego (*Ikhla' Na'layk*)</h4>
        <p>Entering the sanctified valley of Tuwa, Musa was commanded to remove his sandals. Classical exegetes (<em>Al-Qurtubi</em>) observe that stepping barefoot upon holy soil represents stripping away worldly arrogance, social status, and external identity, presenting oneself in total, unadorned vulnerability before the Living God.</p>
        <h4>The Prime Directive: Prayer for Remembrance (*Li-Dhikri*)</h4>
        <p>Before commissioning Musa for geopolitical confrontation or detailing legal codes, Allah established the primary purpose of ritual worship: <em>"Aqimi as-salata li-dhikri."</em> Salah is the ultimate cognitive defense mechanism against the amnesia of modern life, sustaining constant alignment with transcendent reality.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: INNER FORTITUDE & MILDNESS -->
  <div class="modal-backdrop" id="expansivenessModal" onclick="closeOnBackdrop(event, 'expansivenessModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Architecture of Inner Fortitude & Gentle Speech</h3>
        <button class="modal-close" onclick="closeModal('expansivenessModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "[Musa] said, 'My Lord, expand for me my breast and ease for me my task and untie the knot from my tongue that they may understand my speech... And speak to him with gentle speech that perhaps he may be reminded or fear.'"
        </div>
        <h4>The Expanding Heart (*Sharh as-Sadr*)</h4>
        <p>Tasked with confronting the most brutal tyrant of antiquity, Musa did not request legions of angels or armies. He prayed for the expansion of his heart—the spiritual vessel that absorbs hostility, mockery, and intimidation without retaliating with malice or collapsing in panic.</p>
        <h4>Communicative Humility (*Yafqahu Qawli*)</h4>
        <p>Musa asked for the removal of his speech impediment solely so his listeners could comprehend his message: <em>"Yafqahu qawli."</em> His goal was not rhetorical showmanship or public adulation, but functional cognitive clarity that allows truth to penetrate resistant hearts.</p>
        <h4>The Ethics of Mild Speech (*Qawlan Layyina*)</h4>
        <p>Even when addressing Pharaoh—who claimed supreme divinity and slaughtered newborn infants—Allah commanded mild, gentle speech (<em>Qawlan layyina</em>). If divine law forbids vitriol against a genocidal tyrant, how could any believer justify arrogance, cruelty, or sarcasm when advising fellow human beings?</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: SORCERERS' PROSTRATION -->
  <div class="modal-backdrop" id="sorcerersModal" onclick="closeOnBackdrop(event, 'sorcerersModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Epistemological Victory of Truth & Defiance of Crucifixion</h3>
        <button class="modal-close" onclick="closeModal('sorcerersModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "So the magicians fell down in prostration. They said, 'We have believed in the Lord of Aaron and Moses.' ... [Pharaoh said], 'I will surely cut off your hands and your feet on opposite sides and crucify you on the trunks of palm trees.' ... They said, 'We will never prefer you over what has come to us of clear proofs... You can only decree for this worldly life.'"
        </div>
        <h4>Sensory Illusion vs. Ontological Reality</h4>
        <p>Egypt's elite magicians utilized mercury and ropes to create mass optical illusions, deceiving spectator senses into perceiving slithering vipers. But when Musa's staff was cast, it did not perform a competing illusion; it physically swallowed their props (*Talqaf ma sana'oo*), proving that authentic truth consumes falsehood.</p>
        <h4>The Spontaneous Surrender of Experts (*Sujjadan*)</h4>
        <p>Because the magicians were master practitioners of deception, they possessed the technical expertise to recognize that Musa's miracle was an act of divine creation beyond human power. They collapsed in prostration immediately, entirely unconcerned with Pharaoh's reaction.</p>
        <h4>Transcendent Conviction Over State Terror</h4>
        <p>Threatened with gruesome cross-amputation and crucifixion on palm trunks, their immortal response defined spiritual liberation: <em>"Innama taqdee hadhihi al-hayat al-dunya."</em> They recognized that imperial violence is bound strictly to biological existence, while the mercy of Allah is eternal.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: ADAM & REMEMBRANCE -->
  <div class="modal-backdrop" id="remembranceModal" onclick="closeOnBackdrop(event, 'remembranceModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Suffocation of Heedlessness & The Divine Shield</h3>
        <button class="modal-close" onclick="closeModal('remembranceModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And whoever turns away from My remembrance - indeed, he will have a depressed life, and We will gather him on the Day of Resurrection blind... So if there comes to you guidance from Me - then whoever follows My guidance will neither go astray nor suffer misery."
        </div>
        <h4>The Pathology of Spiritual Constriction (*Ma'eeshatan Danka*)</h4>
        <p>Surah Ta-Ha diagnoses the existential affliction of human estrangement from God: <em>Ma'eeshatan danka</em> (the constricted, choking life). Regardless of sensory luxuries, wealth, and societal fame, a heart devoid of divine remembrance suffocates under ceaseless anxiety, loneliness, and terror of mortality.</p>
        <h4>The Blind Resurrection (*A'ma*)</h4>
        <p>On the Day of Standing, the heedless soul is resurrected physically blind, protesting the loss of worldly sight. The divine verdict establishes precise moral symmetry: just as you deliberately closed your eyes to divine signs during life, today you are left in darkness and forgotten.</p>
        <h4>The Universal Shield Against Grief (*Fa-La Yashqa*)</h4>
        <p>Reflecting on Adam's temporary lapse through forgetfulness (*Nisyan*) and his immediate restoration through repentance, Allah concludes with the supreme promise: whoever adheres to divine guidance will never stumble into intellectual confusion (*La yadillu*) nor drown in existential misery (*La yashqa*).</p>
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>4</b> Lectures &bull; <b>100%</b> Sunni Verified';
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
        "Movement 2": 3,
        "Movement 3": 5,
        "Movement 4": 7
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

print(f"Successfully generated Surah Ta-Ha Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
