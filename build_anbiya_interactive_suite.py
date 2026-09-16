#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Anbiya Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Primordial Singularity & The Biological Matrix of Water (Ratqan & Water)
    2. Socratic Iconoclasm & The Temperate Furnace (Ibrahim & Bardan wa Salaman)
    3. Restorative Jurisprudence & Celestial Metallurgy (Dawud & Sulayman)
    4. The Symphony of Deliverance & Universal Mercy (Yunus, Ayyub & Rahmatan)
- 3-Lecture Foundation Audio Syllabus Explorer (02h 19m 40s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_ANBIYA_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_anbiya_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_anbiya_html_and_md import pages_data

# 3 Audio Foundation lectures syllabus (02h 19m 40s total)
audio_lectures = [
    ("21.Al-anbiyaPart1.opus", "The Imminent Reckoning, Cosmic Architecture, Water Matrix & The Scales of Justice", "Movement 1", "01h 00m 03s"),
    ("21.Al-anbiyaPart2.opus", "Ibrahim's Socratic Iconoclasm, The Cool Fire & The Jurisprudence of Dawud and Sulayman", "Movement 2", "58m 15s"),
    ("21.Al-anbiyaPart3.opus", "The Litany of Deliverance (Ayyub, Yunus, Zakariyya) & The Universal Mercy", "Movement 3", "21m 21s")
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
  <title>Surah Al-Anbiya — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>SURAH AL-ANBIYA &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_ANBIYA_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/ANBIYA_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/ANBIYA_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across Al-Anbiya (e.g., reckoning, water, ibrahim, fire, dawud, sulayman, ayyub, yunus)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>3</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('cosmicModal')">Cosmic Singularity & Water</button>
        <button class="btn btn-outline" onclick="openModal('fireModal')">Ibrahim & The Cool Fire</button>
        <button class="btn btn-outline" onclick="openModal('jurisprudenceModal')">Dawud & Sulayman's Law</button>
        <button class="btn btn-outline" onclick="openModal('litanyModal')">The Litany of Yunus & Mercy</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (02h 19m 40s TOTAL)</span>
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

  <!-- MODAL 1: COSMIC SINGULARITY & WATER -->
  <div class="modal-backdrop" id="cosmicModal" onclick="closeOnBackdrop(event, 'cosmicModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Primordial Singularity & The Biological Matrix of Water</h3>
        <button class="modal-close" onclick="closeModal('cosmicModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Have those who disbelieved not seen that the heavens and the earth were a joined entity, and We clove them asunder, and made from water every living thing? Then will they not believe?"
        </div>
        <h4>The Primordial Singularity (*Ratqan Fa-Fataqnahuma*)</h4>
        <p>Surah Al-Anbiya reveals that the universe originated as an integrated, contiguous singular mass (<em>Ratq</em>). By divine decree, the heavens and earth were cleaved apart (<em>Fatq</em>), expanding the celestial space and separating atmospheric vaults from the terrestrial crust, establishing the dynamic ecosystem required for life.</p>
        <h4>The Universal Biological Law of Water</h4>
        <p><em>"Wa ja'alna min al-ma'i kulla shay'in hayy."</em> Water is not merely an external resource; it is the fundamental biochemical matrix of all living matter. Every cell, tissue, metabolic cycle, and photosynthetic process across flora, fauna, and human biology is physically constituted of water.</p>
        <h4>Planetary Anchors & Celestial Canopies</h4>
        <p>The earth is stabilized against seismic rocking by mountain pegs (<em>Rawasiya</em>), while the sky acts as a protected canopy (<em>Saqfan mahfoodha</em>)—shielding terrestrial biology from lethal cosmic radiation while celestial bodies swim harmoniously in ordained orbits (<em>Falak</em>).</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: IBRAHIM & THE COOL FIRE -->
  <div class="modal-backdrop" id="fireModal" onclick="closeOnBackdrop(event, 'fireModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Socratic Iconoclasm & The Temperate Furnace</h3>
        <button class="modal-close" onclick="closeModal('fireModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "He said, 'Rather, this - the largest of them - did it, so ask them, if they should be able to speak.' ... We said, 'O fire, be coolness and peace upon Abraham.'"
        </div>
        <h4>Dialectical Irony with the Axe</h4>
        <p>Ibrahim shattered the idols of Babylon during their festival, placing the battle-axe on the shoulder of the chief statue. Interrogated by furious elders, he forced them into an inescapable cognitive trap: if these carved statues cannot identify their attacker, defend themselves, or speak, why are rational human beings worshipping them?</p>
        <h4>The Transmutation of Combustion (*Bardan wa Salaman*)</h4>
        <p>Catapulted into a roaring imperial bonfire, Allah suspended the natural thermal properties of combustion: <em>"Koonee bardan wa salaman."</em> Classical scholars (<em>Ibn 'Abbas</em>) note that had Allah only commanded cold (<em>Bardan</em>), the extreme chill would have killed him; by adding peace (<em>Salaman</em>), the inferno became a temperate garden of security.</p>
        <h4>The Frustration of Tyrannical Plots</h4>
        <p>The Babylonians intended to erase the young prophet in a public execution; instead, Allah made them the ultimate losers (<em>Al-Akhsareen</em>), establishing that divine protection renders imperial violence completely powerless.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: DAWUD & SULAYMAN'S LAW -->
  <div class="modal-backdrop" id="jurisprudenceModal" onclick="closeOnBackdrop(event, 'jurisprudenceModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Restorative Jurisprudence & Celestial Metallurgy</h3>
        <button class="modal-close" onclick="closeModal('jurisprudenceModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And Dawud and Sulayman, when they gave judgment concerning the field, when the sheep of the people pastured therein by night... And We explained it to Sulayman, and to each We gave judgment and knowledge. And We taught him the craft of chainmail armor for you..."
        </div>
        <h4>The Dispute of the Midnight Flock</h4>
        <p>Sheep wandered into a neighbor's enclosed vineyard by night, eating the fruit and trampling the vines. Dawud ruled that the entire flock be transferred permanently to the vineyard owner as fair financial compensation for the lost crop.</p>
        <h4>Sulayman's Restorative Justice (*Fa-Fahhamnaha*)</h4>
        <p>Sulayman conceived a restorative compromise: the vineyard owner takes the sheep temporarily to use their milk, wool, and offspring, while the shepherd works to rehabilitate the damaged vineyard until it is restored to full health, at which point both parties reclaim their original property. This healed both the economic loss and the social relationship.</p>
        <h4>The Invention of Flexible Chainmail (*Laboosin Lakum*)</h4>
        <p>Allah softened iron for Dawud, teaching him the revolutionary craft of interlocking woven rings (chainmail armor). This eliminated the suffocating weight of solid bronze plating, protecting warriors on the battlefield while preserving agile movement, defining technology as a sacred gift requiring gratitude.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: YUNUS & MERCY -->
  <div class="modal-backdrop" id="litanyModal" onclick="closeOnBackdrop(event, 'litanyModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Symphony of Deliverance & The Universal Mercy</h3>
        <button class="modal-close" onclick="closeModal('litanyModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And he called out in the darknesses, 'There is no deity except You; exalted are You! Indeed, I have been of the wrongdoers.' So We responded to him and saved him from the distress. And thus do We deliver the believers... And We have not sent you except as a mercy to all the worlds."
        </div>
        <h4>Ayyub's Sublime Courtesy (*Adab*)</h4>
        <p>Suffering eighteen years of debilitating illness, loss of wealth, and family, Ayyub never complained against God. He phrased his condition with extreme modesty: <em>"Adversity has touched me,"</em> appealing to the mercy of Ar-Rahman rather than demanding relief. Allah answered immediately, healing his body and doubling his family.</p>
        <h4>The Infallible Tripartite Litany of Yunus (Dhun-Nun)</h4>
        <p>In the triple darkness of the whale's belly, the ocean depths, and the night, Yunus uttered the supreme formula: Monotheism (<em>La ilaha illa Anta</em>), Transcendence (<em>Subhanaka</em>), and Confession of Fault (<em>Innee kuntu minadh-dhalimeen</em>). The Prophet confirmed that no Muslim recites this in distress except that Allah rescues them.</p>
        <h4>The Prophet as Cosmic Mercy (*Rahmatan lil-'Alameen*)</h4>
        <p>Surah Al-Anbiya concludes with the supreme definition of the Prophet Muhammad's universal mission: he was sent not as an instrument of destruction or imperial domination, but as an embodied, all-encompassing outpouring of divine mercy embracing humanity, animals, and the cosmos.</p>
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>3</b> Lectures &bull; <b>100%</b> Sunni Verified';
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
        "Movement 3": 6
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

print(f"Successfully generated Surah Al-Anbiya Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
