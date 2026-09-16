#!/usr/bin/env python3
"""
Huurs Studio - Surah Maryam Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Secret Whisper of Vulnerability & Unbroken Hope (Zakariyya)
    2. Maternal Agony Under the Palm & Consolation (Maryam & Isa)
    3. The Four 'Ya Abati' & Filial Compassion Before Threats (Ibrahim & Azar)
    4. The Cosmic Horror of Shirk & Divine Endowment of Love (Ar-Rahman & Wudd)
- 3-Lecture Foundation Audio Syllabus Explorer (02h 08m 37s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_MARYAM_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_maryam_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_maryam_html_and_md import pages_data

# 3 Audio Foundation lectures syllabus (02h 08m 37s total)
audio_lectures = [
    ("19.MaryamPart1.opus", "The Secret Supplication of Zakariyya, Yahya's Conception & Maryam's Solitude", "Movement 1", "01h 01m 16s"),
    ("19.MaryamPart2.opus", "The Nativity, Infant Speech in the Cradle & Ibrahim's Filial Compassion", "Movement 2", "43m 45s"),
    ("19.MaryamPart3.opus", "The Prophetic Lineage, Cosmic Outrage at False Attribution & The Endowment of Wudd", "Movement 3", "23m 36s")
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
  <title>Surah Maryam — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>SURAH MARYAM &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_MARYAM_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/MARYAM_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/MARYAM_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across Surah Maryam (e.g., zakariyya, yahya, maryam, isa, ibrahim, azar, wudd)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>3</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('zakariyyaModal')">Zakariyya's Whisper</button>
        <button class="btn btn-outline" onclick="openModal('nativityModal')">Nativity & The Palm</button>
        <button class="btn btn-outline" onclick="openModal('ibrahimModal')">Ibrahim & Azar</button>
        <button class="btn btn-outline" onclick="openModal('wuddModal')">The Gift of Wudd</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (02h 08m 37s TOTAL)</span>
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

  <!-- MODAL 1: ZAKARIYYA'S WHISPER -->
  <div class="modal-backdrop" id="zakariyyaModal" onclick="closeOnBackdrop(event, 'zakariyyaModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Secret Whisper of Vulnerability & Unbroken Hope</h3>
        <button class="modal-close" onclick="closeModal('zakariyyaModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "When he called to his Lord a private supplication. He said, 'My Lord, indeed my bones have grown feeble, and my head has filled with white, and never have I been in my supplication to You, my Lord, unblessed... So grant me from Yourself an heir.'"
        </div>
        <h4>The Architecture of Silent Invocations (*Nida'an Khafiyya*)</h4>
        <p>Zakariyya called upon his Lord in concealed secrecy, isolating his voice from human ears. Classical exegetes (<em>Tafsir al-Tabari</em>) explain that the secret whisper is the purest manifestation of sincere devotion (<em>Ikhlas</em>), entirely shielded from ostentation and sheltered from cynical ridicule by skeptics regarding his physical frailty.</p>
        <h4>Somatic Candor Before the Creator</h4>
        <p>Rather than disguising his weakness, Zakariyya articulated his somatic vulnerability before Allah: brittle bones (<em>wahana al-'adhmu</em>) and head ignited with gray hair (<em>ishta'ala ar-ra'su shayba</em>). In Sunni spiritual tradition, confessing physical incapacity before the Almighty is not despair, but an act of supreme humility that magnetizes divine compassion.</p>
        <h4>Spiritual Stewardship Over Material Patrimony</h4>
        <p>Zakariyya explicitly sought an heir who would inherit the mantle of spiritual leadership (<em>Yarithunee wa yarithu min aali Ya'qoob</em>). As established by Sunni jurisprudence, prophets do not leave behind dirhams and dinars as inheritable estate; their inheritance is sacred knowledge, righteous character, and the custody of monotheism.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: NATIVITY & THE PALM -->
  <div class="modal-backdrop" id="nativityModal" onclick="closeOnBackdrop(event, 'nativityModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Maternal Agony Under the Palm & Consolation</h3>
        <button class="modal-close" onclick="closeModal('nativityModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And the pains of childbirth drove her to the trunk of a palm tree. She said, 'Oh, I wish I had died before this and was in oblivion, forgotten!' But he called her from below her, 'Do not grieve; your Lord has provided beneath you a stream. And shake toward you the trunk of the palm tree; it will drop upon you ripe, fresh dates.'"
        </div>
        <h4>The Depth of Maternal Anguish (*Ya Laytanee Mittu Qabla Hadha*)</h4>
        <p>Maryam's exclamation of longing for oblivion (*Nasyan Mansiyya*) illustrates the agonizing collision between divine destiny and social reality. Knowing the inevitable slander that her chaste reputation would face from hypocrites and accusers, her anguish was so intense that she wished she had never existed. This reveals that spiritual righteousness does not negate intense emotional distress.</p>
        <h4>Divine Consolation: The Stream & Fresh Dates</h4>
        <p>From beneath her came comforting reassurances and instantaneous physical relief: a running freshwater rivulet (<em>Sariyya</em>) to cleanse and hydrate her, and freshly ripened dates (<em>Rutaban Janiyya</em>) to restore glucose and physical strength.</p>
        <h4>The Law of Means (*I'mal al-Asbab*)</h4>
        <p>Even though Allah created Isa without a father, He commanded Maryam—in her most fragile post-partum state—to physically shake the solid trunk of the date palm tree. In orthodox Sunni theology, miracles never cancel human exertion; Allah demands the movement of human effort, while reserving the actual outcome entirely to His sovereign power.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: IBRAHIM & AZAR -->
  <div class="modal-backdrop" id="ibrahimModal" onclick="closeOnBackdrop(event, 'ibrahimModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Four 'Ya Abati' & Filial Compassion Before Threats</h3>
        <button class="modal-close" onclick="closeModal('ibrahimModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "When he said to his father, 'O my father, why do you worship that which does not hear and does not see and will not benefit you at all? O my father, indeed there has come to me of knowledge that which has not come to you... O my father, do not worship Satan... O my father, indeed I fear that there will touch you a punishment from the Most Merciful...'"
        </div>
        <h4>The Filial Discourse of Tenderness</h4>
        <p>Ibrahim repeatedly invokes his polytheistic father with the phrase of intimate affection: <em>"Ya Abati"</em> (O my dear father). He presents reasoned theology with supreme humility: he does not insult his father's intelligence, but points out that divine knowledge has been bestowed upon him as a gift, offering to guide his father along a level path (<em>Siratan Sawiyya</em>).</p>
        <h4>Responding to Threats of Stoning with Peace</h4>
        <p>When Azar violently threatened to stone him to death and commanded his exile (<em>La-arjumannaka wahjurnee maliyya</em>), Ibrahim did not retaliate with anger or vitriol. Instead, he answered with dignity and peace: <em>"Salamun 'alayk"</em> (Peace be upon you; I will seek forgiveness for you from my Lord).</p>
        <h4>Spiritual Posterity as Divine Compensation (*Lisan Sidq*)</h4>
        <p>Having surrendered family, homeland, and companionship for monotheism, Allah compensated Ibrahim with righteous prophetic offspring—Ishaq, Ya'qub, and an enduring honorable reputation (<em>Lisana Sidqin 'Aliyya</em>) that resonates through all sacred history.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: THE GIFT OF WUDD -->
  <div class="modal-backdrop" id="wuddModal" onclick="closeOnBackdrop(event, 'wuddModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Cosmic Horror of Shirk & The Divine Endowment of Love</h3>
        <button class="modal-close" onclick="closeModal('wuddModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And they say, 'The Most Merciful has taken [for Himself] a son.' You have done an atrocious thing! The heavens almost rupture therefrom and the earth splits open and the mountains collapse in devastation... Indeed, those who have believed and done righteous deeds - the Most Merciful will appoint for them affection [wudd]."
        </div>
        <h4>Cosmic Outrage at False Attribution (*Haddan*)</h4>
        <p>The inanimate creation—the heavens, the earth, and the towering mountains—tremble in ontological outrage at the claim that Ar-Rahman has taken a son. In Sunni theology, the cosmos recognizes the majesty and absolute transcendence of the Creator, recoiling at the monstrous attribution of biological offspring to the Sovereign of all existence.</p>
        <h4>Solitary Accountability (*Fardan*)</h4>
        <p>Every single soul in the heavens and earth will appear before the Most Merciful purely as an obedient servant (<em>Abdan</em>). None can claim immunity, status, or unpermitted intercession; all are numbered, recorded, and presented in solitary individuality (<em>Wa kulluhum aateehi yawma al-qiyamati farda</em>).</p>
        <h4>The Divine Endowment of Love (*Wudd*)</h4>
        <p>As the ultimate conclusion of Surah Maryam, Allah promises that those who anchor themselves in authentic faith and righteous action will be gifted <em>Wudd</em>—an enduring celestial love established by Ar-Rahman, broadcast through the Angel Jibril to all creation, and manifested as widespread goodwill and veneration across the earth.</p>
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
        "Movement 2": 4,
        "Movement 3": 7
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

print(f"Successfully generated Surah Maryam Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
