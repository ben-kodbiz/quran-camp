#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Mu'minun Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Decalogue of Falah & The Seven Hallmarks of the Heirs of Firdaus
    2. Biological Morphogenesis: From Clay Extract to Ensouled Being
    3. The Trembling Hearts of the Righteous (Qulubuhum Wajilah) & Pure Sustenance
    4. The Irreversible Threshold of Death, The Barzakh & Refuting Nihilism ('Abathan)
- 3-Lecture Foundation Audio Syllabus Explorer (02h 59m 43s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_MUMINUN_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_muminun_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_muminun_html_and_md import pages_data

# 3 Audio Foundation lectures syllabus (02h 59m 43s total)
audio_lectures = [
    ("23.Al-muminoonPart1.opus", "The Seven Hallmarks of Believers & Embryological Morphogenesis", "Movement 1", "59m 22s"),
    ("23.Al-muminoonPart2.opus", "Cosmic Canopy, Prophetic Struggles & Sincerity of the Righteous", "Movement 2", "01h 02m 05s"),
    ("23.Al-muminoonPart3.opus", "The Threshold of Death, The Barzakh & Cosmic Vindication", "Movement 3", "58m 16s")
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
  <title>Surah Al-Mu'minun — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>SURAH AL-MU'MINUN &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_MUMINUN_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/MUMINUN_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/MUMINUN_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across Al-Mu'minun (e.g., khushu, falah, embryo, nuh, pure diet, wajilah, barzakh, scales)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>3</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('falahModal')">The Decalogue of Falah</button>
        <button class="btn btn-outline" onclick="openModal('embryoModal')">Embryology & Ensoulment</button>
        <button class="btn btn-outline" onclick="openModal('wajilahModal')">Trembling Hearts (Wajilah)</button>
        <button class="btn btn-outline" onclick="openModal('barzakhModal')">The Threshold of Barzakh</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (02h 59m 43s TOTAL)</span>
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

  <!-- MODAL 1: THE DECALOGUE OF FALAH -->
  <div class="modal-backdrop" id="falahModal" onclick="closeOnBackdrop(event, 'falahModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Decalogue of Falah & The Seven Hallmarks of the Heirs of Firdaus</h3>
        <button class="modal-close" onclick="closeModal('falahModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Certainly will the believers have succeeded: They who are during their prayer humbly submissive, and they who turn away from ill speech, and they who are observant of zakah, and they who guard their private parts... And they who are to their trusts and their promises attentive... Those are the inheritors who will inherit al-Firdaus."
        </div>
        <h4>The Definitive Guarantee (*Qad Aflaha*)</h4>
        <p>The surah opens with categorical certainty. <em>Al-Falah</em> in Arabic encompasses the attainment of every cherished blessing and absolute deliverance from every feared outcome. The Prophet (peace be upon him) affirmed that whoever establishes these opening ten verses is guaranteed entry into Paradise.</p>
        <h4>The Inward Pillar: Khushu' in Prayer</h4>
        <p><em>Khushu'</em> is the core spiritual engine: stillness of the physical limbs combined with reverent, trembling awe within the soul. Fidgeting, glancing about, and distracted contemplation of worldly concerns negate the essence of prayer.</p>
        <h4>The Protective Shield: Shunning Laghw & Guarding Chastity</h4>
        <p>The noble believer disdains <em>Laghw</em>—vain talk, digital clutter, and frivolous entertainment. Concurrently, moral discipline is anchored in <em>Hifdh al-furuj</em>, reserving intimacy strictly within lawful marriage, while guarding sacred trusts and solemn covenants.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: EMBRYOLOGY & ENSOULMENT -->
  <div class="modal-backdrop" id="embryoModal" onclick="closeOnBackdrop(event, 'embryoModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Biological Morphogenesis: From Clay Extract to Ensouled Being</h3>
        <button class="modal-close" onclick="closeModal('embryoModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And certainly did We create man from an extract of clay. Then We placed him as a sperm-drop in a firm lodging. Then We made the sperm-drop into a clinging clot, and We made the clot into a lump [of flesh], and We made [from] the lump, bones, and We covered the bones with flesh; then We developed him into another creation. So blessed is Allah, the best of creators."
        </div>
        <h4>Primordial Soil & Secure Uterine Lodging</h4>
        <p>Humanity traces its elemental composition to the mineral nutrients of the earth (<em>Sulalah min teen</em>). This establishes universal humility, reminding man of his fragile foundation before placing the zygote in the maternal womb (<em>Qararin makeen</em>), insulated from physical trauma.</p>
        <h4>Osteogenesis & Myogenesis</h4>
        <p>The embryo transitions from a clinging structure (<em>'alaqah</em>) into a compact somite mass (<em>mudghah</em>). Bone cartilage is mineralized into skeletal architecture, which is subsequently clad with protective, agile muscle fibers.</p>
        <h4>Ensoulment into Another Creation (*Khalqan Akhar*)</h4>
        <p>The ensoulment represents the miraculous threshold where purely biological tissue is elevated into an ensouled, sentient moral being endowed with spiritual consciousness, celebrated with the doxology: <em>Fa-tabarakallahu ahsanul-khaliqeen</em>.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: TREMBLING HEARTS & PURE SUSTENANCE -->
  <div class="modal-backdrop" id="wajilahModal" onclick="closeOnBackdrop(event, 'wajilahModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Trembling Hearts of the Righteous (Qulubuhum Wajilah) & Pure Diet</h3>
        <button class="modal-close" onclick="closeModal('wajilahModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "O messengers, eat from the good pure foods and work righteousness. Indeed, I am Knowing of what you do... And they who give what they give while their hearts are fearful because they will be returning to their Lord - it is those who hasten to good deeds, and they are foremost therein."
        </div>
        <h4>The Prerequisite of Halal Sustenance (*Al-Tayyibat*)</h4>
        <p>All messengers of Allah were charged with an inviolable decree: consume only pure, ethically acquired food (<em>tayyibat</em>) and perform righteous deeds. Consuming unlawful earnings deadens spiritual receptivity, blunts prayers, and disqualifies deeds from divine acceptance.</p>
        <h4>The Spiritual Psychology of Wajilah</h4>
        <p>When 'A'ishah asked the Prophet if those with trembling hearts were sinners who stole or drank wine, he clarified: <em>"No, O daughter of al-Siddiq! Rather, they are those who fast, pray, and give charity, yet fear their deeds will not be accepted."</em></p>
        <h4>The Antidote to Self-Righteousness</h4>
        <p>The true believer combines diligent righteous effort with reverent humility, avoiding spiritual arrogance. This acute awareness of returning to the Sovereign accelerates their urgency to race toward further good deeds.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: BARZAKH & REFUTING NIHILISM -->
  <div class="modal-backdrop" id="barzakhModal" onclick="closeOnBackdrop(event, 'barzakhModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Irreversible Threshold of Death, The Barzakh & Refuting Nihilism</h3>
        <button class="modal-close" onclick="closeModal('barzakhModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "[For such is the state of the disbelievers], until, when death comes to one of them, he says, 'My Lord, send me back that I might do righteousness in that which I left behind.' By no means! It is only a word he is speaking; and behind them is a barrier until the Day they are resurrected... Then did you think that We created you uselessly and that to Us you would not be returned?"
        </div>
        <h4>The Panic of the Unprepared Soul (*Rabbi Irji'oon*)</h4>
        <p>At the instant of death, the veil of physical distraction evaporates. The unrepentant soul weeps in desperate horror, pleading for a second chance to perform righteous works. The divine response is absolute: <em>"Kalla!"</em> (Never!), sealing the testing grounds of mortal life.</p>
        <h4>The Impenetrable Intermediate Realm (*Al-Barzakh*)</h4>
        <p>Between physical death and the cosmic resurrection lies <em>Al-Barzakh</em>—a metaphysical veil through which no deceased soul can return to the earth. Earthly life was the singular, non-repeatable opportunity to choose salvation.</p>
        <h4>The Refutation of Meaninglessness (*'Abathan*)</h4>
        <p>The surah demolishes atheistic absurdity: the intricate human body and celestial cosmos were not forged in aimless sport. Life is infused with absolute teleological purpose, culminating in eternal judgment before the Supreme King: <em>Fa-ta'ala Allahu al-Maliku al-Haqq</em>.</p>
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

print(f"Successfully generated Surah Al-Mu'minun Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
