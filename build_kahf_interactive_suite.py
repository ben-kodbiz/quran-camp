#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Kahf Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Sanctuary of Faith & The 309-Year Slumber (Ashab al-Kahf)
    2. The Anatomy of Wealth Arrogance & Hand-Wringing Regret (Two Gardens)
    3. The Divine Pedagogy of Paradox & Hidden Mercy (Musa & Khidr)
    4. Ethical Governance & Advanced Metallurgy (Dhul-Qarnayn & Iron Rampart)
- 13-Lecture Foundation Audio Syllabus Explorer (04h 37m 25s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_KAHF_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_kahf_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_kahf_html_and_md import pages_data

# 13 Audio Foundation lectures syllabus
audio_lectures = [
    ("18.Al-kahf1-3.opus", "The Uncrooked Scripture, Warning & Glad Tidings", "Movement 1", "23m 27s"),
    ("18.Al-kahf4-9.opus", "False Divinity Refuted & Terrestrial Adornment as Trial", "Movement 1", "20m 34s"),
    ("18.Al-kahf10-16.opus", "The Youth of the Cave, State Tyranny & Prayer for Mercy", "Movement 1", "22m 12s"),
    ("18.Al-kahf15-19.opus", "Astronomical Sunlight, Somatic Turning & The Outstretched Dog", "Movement 2", "18m 34s"),
    ("18.Al-kahf20-25.opus", "The Awakening, Pure Sustenance & The 309-Year Span", "Movement 2", "18m 07s"),
    ("18.Al-kahf26-29.opus", "The Protocol of In Sha' Allah & Companionship of Believers", "Movement 2", "18m 07s"),
    ("18.Al-kahf30-37.opus", "The Parable of the Two Gardens: Capitalistic Hubris", "Movement 3", "20m 05s"),
    ("18.Al-kahf38-45.opus", "The Believer's Dialectic, Tempest Ruin & Agricultural Parable", "Movement 3", "16m 33s"),
    ("18.Al-kahf46-57.opus", "Al-Baqiyat as-Salihat, Barren Earth & The Unfolded Ledger", "Movement 4", "24m 07s"),
    ("18.Al-kahf58-73.opus", "Musa's Resolution, The Revived Fish & Meeting Al-Khidr", "Movement 5", "22m 56s"),
    ("18.Al-kahf74-82.opus", "The Three Epistemological Paradoxes Unveiled", "Movement 6", "22m 01s"),
    ("18.Al-kahf83-99.opus", "Dhul-Qarnayn's Expeditions, Iron-Copper Metallurgy & Gog/Magog", "Movement 7", "24m 38s"),
    ("18.Al-kahf100-110.opus", "The Ultimate Losers, Gardens of Firdaus & The Ocean of Ink", "Movement 8", "26m 05s")
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
  <title>Surah Al-Kahf — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
      font-size: 0.82rem;
      color: var(--text-muted);
    }
    .search-stats b {
      color: var(--cyan);
    }
    .deep-dive-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .tab-bar {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      overflow-x: auto;
      padding-bottom: 6px;
    }
    .tab-chip {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.82rem;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .tab-chip:hover {
      border-color: var(--cyan);
      color: var(--white);
    }
    .tab-chip.active {
      background: var(--navy-elevated);
      border-color: var(--gold);
      color: var(--gold);
      font-weight: 600;
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
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 14px;
      margin-bottom: 20px;
      gap: 16px;
      flex-wrap: wrap;
    }
    .plate-title-bar h2 {
      font-size: 1.15rem;
      color: var(--white);
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
    }
    .badge-gold {
      background: rgba(212, 175, 55, 0.12);
      color: var(--gold);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .badge-emerald {
      background: rgba(16, 185, 129, 0.12);
      color: var(--emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 600;
    }
    .pillars-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    @media (max-width: 900px) {
      .pillars-layout {
        grid-template-columns: 1fr;
      }
    }
    .pillar-box {
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .pillar-bar {
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-muted);
    }
    .pillar-bar.cyan { border-top: 3px solid var(--cyan); }
    .pillar-bar.purple { border-top: 3px solid var(--purple); }
    .pillar-bar.emerald { border-top: 3px solid var(--emerald); }
    .pillar-bar.gold { border-top: 3px solid var(--gold); }
    .pillar-bar.rose { border-top: 3px solid var(--rose); }
    .pillar-bar h3 {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--white);
    }
    .pillar-bar p {
      font-size: 0.75rem;
      color: var(--text-muted);
    }
    .cards-wrapper {
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      flex: 1;
    }
    .card-item {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 5px;
      padding: 10px 12px;
      transition: border-color 0.2s, transform 0.2s;
    }
    .card-item:hover {
      border-color: var(--cyan);
      transform: translateY(-1px);
    }
    .card-title-row {
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-bottom: 6px;
    }
    .card-idx {
      background: rgba(255, 255, 255, 0.06);
      color: var(--gold-light);
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 5px;
      border-radius: 3px;
    }
    .card-title-row h4 {
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--white);
    }
    .card-points {
      list-style-type: none;
      padding-left: 0;
    }
    .card-points li {
      position: relative;
      padding-left: 12px;
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-bottom: 3px;
      line-height: 1.4;
    }
    .card-points li::before {
      content: "•";
      position: absolute;
      left: 2px;
      color: var(--gold);
    }
    .audio-panel {
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 20px;
      margin-bottom: 24px;
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
      color: var(--gold_light);
      white-space: nowrap;
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
        <span>SURAH AL-KAHF &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_KAHF_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/KAHF_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/KAHF_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across Al-Kahf (e.g., cave, dog, gardens, musa, khidr, ship, dhul-qarnayn)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>13</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('youthModal')">The Cave Sanctuary</button>
        <button class="btn btn-outline" onclick="openModal('gardensModal')">The Two Gardens</button>
        <button class="btn btn-outline" onclick="openModal('khidrModal')">Musa & Al-Khidr</button>
        <button class="btn btn-outline" onclick="openModal('sovereigntyModal')">Dhul-Qarnayn & Iron</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (04h 37m 25s TOTAL)</span>
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

  <!-- MODAL 1: THE CAVE SANCTUARY -->
  <div class="modal-backdrop" id="youthModal" onclick="closeOnBackdrop(event, 'youthModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Sanctuary of Faith & The 309-Year Slumber</h3>
        <button class="modal-close" onclick="closeModal('youthModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "When the youths retreated to the cave and said, 'Our Lord, grant us from Yourself mercy and prepare for us from our affair right guidance.' ... And you would think them awake, while they were asleep. And We turned them to the right and to the left, while their dog stretched his forelegs at the entrance."
        </div>
        <h4>The Trial of Faith Under State Tyranny</h4>
        <p>The young men of the Cave (<em>Ashab al-Kahf</em>) faced imperial state tyranny mandating idolatrous sacrifice. Choosing physical exile over spiritual betrayal, they retreated into an unadorned stone cave, placing their absolute trust in Allah's unseen mercy (<em>Min ladunka rahmah</em>).</p>
        <h4>Divine Astronomical & Biological Architecture</h4>
        <p>The cave was carved facing north, allowing the rising sun to incline to the right and the setting sun to skirt past to the left (<em>Tazawaru & Taqriduhum</em>). This orientation provided ambient illumination and fresh mountain air while shielding their bodies from direct solar ultraviolet radiation. Concurrently, divine providence shifted their bodies between right and left sides to prevent circulatory stasis, decubitus ulcers, and tissue necrosis over three centuries.</p>
        <h4>The Honor of Righteous Companionship</h4>
        <p>Their dog lay with forelegs outstretched at the threshold (<em>Waseed</em>). Classical scholars (<em>Al-Qurtubi</em>) observe that if an animal attains immortal mention and honor in scripture merely by keeping company with the righteous, how immense is the blessing for a human being who keeps company with the friends of God?</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: THE TWO GARDENS -->
  <div class="modal-backdrop" id="gardensModal" onclick="closeOnBackdrop(event, 'gardensModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Anatomy of Wealth Arrogance & Hand-Wringing Regret</h3>
        <button class="modal-close" onclick="closeModal('gardensModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And he had fruit, so he said to his companion while he was conversing with him, 'I am greater than you in wealth and more eminent in followers.' ... And his fruits were encompassed [with ruin], so he began to turn his hands over [in regret] over what he had spent on it, while it had collapsed upon its trellises..."
        </div>
        <h4>The Pathology of Capital (*Ana Aktharu Minka Malan*)</h4>
        <p>The garden owner possessed two thriving vineyards surrounded by date palms, bisected by a flowing freshwater river, yielding uninterrupted agricultural wealth. His material abundance produced severe cognitive intoxication: he confused worldly capital with eternal favor, boasted over his poorer companion, and arrogantly doubted the coming of the Day of Judgment.</p>
        <h4>The Spiritual Vaccine: *Ma Sha'a Allah*</h4>
        <p>The believing companion offered the definitive monotheistic antidote: acknowledging that all property is a revocable loan from the Creator. Uttering <em>Ma sha'a Allah la quwwata illa billah</em> disarms the ego and anchors the soul in transcendent gratitude.</p>
        <h4>Irreversible Regret (*Yuqallibu Kaffayhi*)</h4>
        <p>A nocturnal disaster struck the orchards, leveling the vines and sinking the groundwater beyond retrieval. Waking to find his empire eradicated, the owner wrung his hands in bitter helplessness. His ultimate cry: <em>"Ya laytanee lam ushrik bi-rabbi ahada"</em>—revealing that deifying wealth and self-sufficiency is a fatal form of polytheism.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: MUSA & AL-KHIDR -->
  <div class="modal-backdrop" id="khidrModal" onclick="closeOnBackdrop(event, 'khidrModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Divine Pedagogy of Paradox & Hidden Mercy</h3>
        <button class="modal-close" onclick="closeModal('khidrModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And they found a servant from among Our servants to whom We had given mercy from Us and had taught him from Us a [certain] knowledge... [Khidr] said, 'Did I not tell you that with me you would never be able to have patience?'"
        </div>
        <h4>The Epistemological Humbling of the Prophet</h4>
        <p>When Musa assumed he was the most knowledgeable man on earth, Allah directed him to the confluence of the two seas (<em>Majma' al-Bahrayni</em>) to learn from Al-Khidr—a servant endowed with transcendent knowledge of destiny (<em>'Ilm Ladunni</em>) that operates beyond apparent causality.</p>
        <h4>The Three Manifest Paradoxes</h4>
        <ul>
          <li><strong>Damaging the Ship:</strong> Seemed like malicious destruction; in reality, it preserved impoverished fishermen from a tyrant king seizing every intact boat by force.</li>
          <li><strong>Slaying the Youth:</strong> Seemed like unprovoked murder; in reality, it spared pious parents from spiritual heartbreak and apostasy, replacing him with a dutiful child.</li>
          <li><strong>Rebuilding the Wall:</strong> Seemed like naive unpaid labor for hostile townsmen; in reality, it preserved buried inheritance for two orphan boys whose father was righteous.</li>
        </ul>
        <h4>Consummate Humility (*Wa Ma Fa'altuhu 'An Amree*)</h4>
        <p>Khidr concluded by completely disavowing personal credit: <em>"And I did not do it of my own accord."</em> The journey establishes that human agitation is caused by incomplete information; what appears as painful damage in life is often the divine shield against fatal ruin.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: DHUL-QARNAYN & IRON -->
  <div class="modal-backdrop" id="sovereigntyModal" onclick="closeOnBackdrop(event, 'sovereigntyModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Ethical Governance & Advanced Metallurgy</h3>
        <button class="modal-close" onclick="closeModal('sovereigntyModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Indeed We established him upon the earth and We gave him to everything a way... He said, 'Bring me sheets of iron' - until, when he had leveled [all] between the two mountain cliffs, he said, 'Blow,' until when he had made it [like] fire, he said, 'Bring me, that I may pour over it molten copper.'"
        </div>
        <h4>The Model of Just Statecraft</h4>
        <p>Dhul-Qarnayn was endowed with vast geopolitical sovereignty, logistical mastery, and scientific capabilities (<em>Sababa</em>). Traversing from the western shores where the sun set in a dark spring to the eastern nomads, he governed with unyielding equity: punishing oppressors, honoring believers, and respecting vulnerable populations without cultural erasure.</p>
        <h4>Refusing Bribery & Mobilizing Collective Labor</h4>
        <p>When an isolated society offered him tribute to construct a barrier against the violent marauders of Gog and Magog (<em>Ya'juj & Ma'juj</em>), Dhul-Qarnayn refused their money: <em>"That in which my Lord has established me is better."</em> Instead of creating dependency, he organized collaborative labor: <em>"Help me with strength/labor (*Fa-a'eenoonee bi-quwwatin*)."</em></p>
        <h4>Advanced Civil Metallurgy & Sovereign Humility</h4>
        <p>By stacking massive iron blocks between mountain cliffs, blowing bellows until glowing red, and pouring molten copper (<em>Qitr</em>), he engineered an impenetrable, rust-resistant alloy rampart. Standing before this supreme engineering triumph, he claimed zero personal glory: <em>"Hadha rahmatun min rabbi"</em> ("This is a mercy from my Lord; when His promise arrives, He will level it to dust").</p>
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>13</b> Lectures &bull; <b>100%</b> Sunni Verified';
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
        "Movement 3": 3,
        "Movement 4": 4,
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

print(f"Successfully generated Surah Al-Kahf Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
