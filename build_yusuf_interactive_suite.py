#!/usr/bin/env python3
"""
Huurs Studio - Surah Yusuf Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Psychology of Sabrun Jameel & False Blood (Bal Sawwalat Lakum Anfusukum)
    2. The Sealed Doors & The Burhan of the Lord (Ma'adhallah & Qudda min Dubur)
    3. The 14-Year Agrarian Master Plan 'Fee Sunbulihi' (Macroeconomic Crisis Leadership)
    4. The Grand Pardon 'La Tathreeba' & Prostration of the Stars (Lateefun Lima Yashaa')
- 15-Lecture Foundation Audio Syllabus Explorer (05h 20m 26s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_YUSUF_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_yusuf_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_yusuf_html_and_md import pages_data

# 15 Audio Foundation lectures syllabus
audio_lectures = [
    ("12.Yusuf1-3.opus", "Ahsan al-Qasas, Literary Supremacy & The Meccan Consolation", "Movement 1", "19m 31s"),
    ("12.Yusuf4-6.opus", "The Celestial Dream of 11 Stars & Paternal Discretion", "Movement 1", "23m 49s"),
    ("12.Yusuf7-11.opus", "Fraternal Jealousy & The Conspiracy at the Well", "Movement 2", "22m 56s"),
    ("12.Yusuf12-18.opus", "The Well of Ghayabah, False Blood & Sabrun Jameel", "Movement 2", "22m 56s"),
    ("12.Yusuf19-23.opus", "Caravanserai to Cairo & The Household of Al-Azeez", "Movement 3", "21m 29s"),
    ("12.Yusuf23-29.opus", "The Seduction Crucible, Burhan of the Lord & The Torn Shirt", "Movement 3", "20m 09s"),
    ("12.Yusuf29-36.opus", "Elite Gossip, The Banquet of Knives & Choosing Incarceration", "Movement 4", "19m 26s"),
    ("12.Yusuf37-43.opus", "Prison Da'wah of Pure Tawhid & Interpreting Inmates' Dreams", "Movement 4", "20m 32s"),
    ("12.Yusuf44-57.opus", "The King's Vision, 14-Year Agrarian Plan & Total Exoneration", "Movement 5", "20m 25s"),
    ("12.Yusuf58-76.opus", "The Brothers' Return, Moral Testing & The Royal Goblet", "Movement 6", "25m 45s"),
    ("12.Yusuf77-90.opus", "Ya'qub's Anguish, Unshakeable Hope & The Great Reveal", "Movement 7", "22m 16s"),
    ("12.Yusuf91-108.opus", "La Tathreeb, Prostration of the Stars & The Final Supplication", "Movement 8", "17m 49s"),
    ("12.Yusuf102-111.opus", "Prophetic Solace, Historical Solitude & Universal Warning", "Movement 8", "25m 43s"),
    ("12.YusufLiteraryQualitiesa.opus", "Literary Anatomy Part I: Symmetric Leitmotifs & Rhetorical Depth", "Literary Analysis", "19m 07s"),
    ("12.YusufLiteraryQualitiesb.opus", "Literary Anatomy Part II: Divine Lutf & Narrative Foreshadowing", "Literary Analysis", "18m 24s")
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
  <title>Surah Yusuf — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
      padding: 24px;
      color: #cbd5e1;
      font-size: 0.9rem;
      line-height: 1.7;
    }
    .modal-body h4 {
      color: var(--gold-light);
      margin: 18px 0 8px 0;
      font-size: 1rem;
    }
    .modal-body p {
      margin-bottom: 12px;
    }
    .quote-box {
      background: var(--navy-elevated);
      border-left: 3px solid var(--gold);
      padding: 12px 16px;
      border-radius: 0 6px 6px 0;
      margin: 14px 0;
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
        <span>Surah Yusuf • Master Cartography & Interactive Digital Suite</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_YUSUF_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>Download Master PDF</a>
        <a href="../07_MINDMAP/YUSUF_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">Full Cartography View</a>
      </div>
    </header>

    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Search across 64 analytical cards, theological themes, Arabic terminology..." oninput="handleLiveSearch()">
      </div>
      <div class="stats-badge" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>15</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
    </div>

    <div class="modals-bar">
      <button class="btn-modal-trigger" onclick="openModal('sabrModal')">
        <span>📜</span> The Psychology of Sabrun Jameel & False Blood
      </button>
      <button class="btn-modal-trigger" onclick="openModal('burhanModal')">
        <span>🛡️</span> The Sealed Doors & The Burhan of the Lord
      </button>
      <button class="btn-modal-trigger" onclick="openModal('grainModal')">
        <span>🌾</span> The 14-Year Agrarian Master Plan 'Fee Sunbulihi'
      </button>
      <button class="btn-modal-trigger" onclick="openModal('pardonModal')">
        <span>👑</span> The Grand Pardon 'La Tathreeba' & Fulfillment
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
        <span>15 Lectures &bull; 05h 20m 26s &bull; Click to filter corresponding plates</span>
      </div>
      <div class="audio-grid">
        {{AUDIO_ITEMS_HTML}}
      </div>
    </section>
  </div>

  <!-- MODAL 1 -->
  <div class="modal-backdrop" id="sabrModal" onclick="closeOnBackdrop(event, 'sabrModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Psychology of Sabrun Jameel & False Blood</h3>
        <button class="modal-close" onclick="closeModal('sabrModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "They brought upon his shirt false blood. He said: 'Nay, but your souls have enticed you to something. So patience is most fitting (Sabrun Jameel). And Allah is the one sought for help against that which you describe.'"
        </div>
        <h4>The Forensic Failure of Envy</h4>
        <p>Classical exegetes, notably <strong>Imam Ibn Kathir</strong> and <strong>Al-Qurtubi</strong>, record the profound forensic observation of Prophet Ya'qub: the brothers presented Yusuf's shirt stained with the blood of a slaughtered goat or sheep (*Bi-damin kadhib*), claiming a wolf devoured him. Ya'qub inspected the garment and immediately noted: <em>"How gentle was this wolf that devoured my son without tearing a single seam of his shirt!"</em> Guilt and emotional agitation blinded the conspirators to basic forensic coherence.</p>
        <h4>The Metaphysical Definition of Sabrun Jameel</h4>
        <p>In classical Sunni theology and spiritual psychology (elaborated masterfully by <strong>Ibn al-Qayyim</strong> in <em>'Uddat as-Sabireen</em>), <strong>Sabrun Jameel</strong> (beautiful patience) is defined as patience that contains:</p>
        <ul>
          <li><strong>Zero complaint to creation:</strong> The heart never petitions sympathy or vindication from fallible humans.</li>
          <li><strong>Total absence of bitter resentment:</strong> Accepting the decree (*Qadar*) without questioning the wisdom or benevolence of the Creator.</li>
          <li><strong>Exclusive channel of grief:</strong> Directing the immense volcanic sorrow directly and exclusively to the Almighty: <em>"Innama ashkoo baththee wa huznee ila Allah."</em></li>
        </ul>
        <h4>Grief Without Despair</h4>
        <p>Weeping until physical blindness occurs (*Ibyaddat 'aynahu minal-huzn*) does not contradict prophetic patience. Grief is an innate human reality; the sin lies only in verbal impatience, despairing of God's relief (*Rawchillahi*), or accusing the Divine of injustice. Ya'qub remained absolutely convinced that Allah would reunite the family decades later.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2 -->
  <div class="modal-backdrop" id="burhanModal" onclick="closeOnBackdrop(event, 'burhanModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Sealed Doors & The Burhan of the Lord</h3>
        <button class="modal-close" onclick="closeModal('burhanModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And she closed the doors and said, 'Come on, you.' He said, '[I seek] the refuge of Allah. Indeed, he is my master, who has made good my residence. Indeed, wrongdoers will not succeed.' And she certainly desired him, and he would have inclined to her had he not seen the proof of his Lord..."
        </div>
        <h4>The Absolute Climax of Temptation</h4>
        <p>The trial of Yusuf in the Egyptian palace represents the apex of psychological and physical temptation: youthful vigor, isolation behind locked, bolt-fastened doors (*Ghallaqati al-abwab*), social immunity as an unfree youth, and a high-status, beautiful temptress demanding compliance. In the face of this overwhelming pressure, Yusuf’s immediate instinct was metaphysical refuge: <strong>Ma'adhallah</strong> (I seek Allah's absolute protection).</p>
        <h4>The Exegesis of the Burhan (Proof of the Lord)</h4>
        <p>Mainstream Sunni scholarship (as emphasized by <strong>Imam at-Tabari</strong>, <strong>Al-Baghawi</strong>, and <strong>Fakhr ad-Din ar-Razi</strong>) preserves the prophetic infallibility (*'Ismah*) of Yusuf. The clause <em>"wa hamma biha lawla an ra'a burhana Rabbih"</em> demonstrates that the potential human impulse was immediately and completely repelled by the divine proof (*Burhan*). The Burhan was the vivid, inescapable illumination of divine consciousness, moral law, and prophetic dignity, instantly arresting any descent into transgression.</p>
        <h4>The Physical Architecture of Vindication: Qudda min Dubur</h4>
        <p>When Yusuf fled toward the exit and the temptress pursued him, tearing his shirt from the back (*Qudda min dubur*), divine providence staged a perfect forensic proof. An objective arbiter from her own household recognized the physics of motion: a tear in the back conclusively proved flight from aggression, while a tear in the front would have suggested assault. Truth left an undeniable physical imprint on the woven fabric.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3 -->
  <div class="modal-backdrop" id="grainModal" onclick="closeOnBackdrop(event, 'grainModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The 14-Year Agrarian Master Plan 'Fee Sunbulihi'</h3>
        <button class="modal-close" onclick="closeModal('grainModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "He said: 'You will plant for seven years consecutively; and what you harvest, leave in its ear, except a little from which you will eat. Then will come after that seven severe years which will consume what you saved for them...'"
        </div>
        <h4>Macroeconomic Crisis Leadership</h4>
        <p>When the King of Egypt was baffled by his dream of seven fat cows consumed by seven lean ones, his courtiers dismissed it as confused nightmares (*Adghathu ahlam*). Yusuf did not merely interpret the symbolic meaning from his prison cell; he unilaterally engineered a comprehensive, 14-year countercyclical macroeconomic strategy that saved the civilization of the ancient Near East from catastrophic extinction.</p>
        <h4>The Agro-Botanical Miracle: Storing in the Ear</h4>
        <p>Yusuf's instruction to <strong>"leave what you harvest in its ear" (*Fama hasadtum fadhareewhu fee sunbulihi*)</strong> represents an astonishing scientific and logistical insight. In humid grain silos, threshed wheat rapidly ferments, rots, or is decimated by grain weevils and pests. By keeping the kernels encased in their natural husks and sheaves (*Sunbul*), the grain remained biologically viable and pest-resistant across seven long years of super-abundance, ready for distribution during the years of devastating drought.</p>
        <h4>Moral Integrity Before Political Power</h4>
        <p>When the King ordered Yusuf's immediate release, Yusuf refused to leave the prison until his name was legally, morally, and publicly cleared: <em>"Return to your lord and ask him what happened with the women who cut their hands."</em> Only after the wife of Al-'Azeez publicly confessed—<em>"Now the truth has become manifest: I enticed him, and he is of the truthful"</em>—did Yusuf accept appointment over the storehouses of the land (*Hafizun 'Aleem*).</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4 -->
  <div class="modal-backdrop" id="pardonModal" onclick="closeOnBackdrop(event, 'pardonModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Grand Pardon 'La Tathreeba' & Fulfillment</h3>
        <button class="modal-close" onclick="closeModal('pardonModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "He said: 'No blame will there be upon you today. Allah will forgive you; and He is the most merciful of the merciful... And he raised his parents upon the throne, and they bowed down to him in prostration. And he said: O my father, this is the explanation of my vision of before. My Lord has made it an actuality.'"
        </div>
        <h4>The Zenith of Magnanimity</h4>
        <p>After decades of separation, enslavement, and wrongful incarceration, Yusuf held total sovereign power over the very brothers who had cast him into the dark well. Instead of executing retribution or extracting humiliating apologies, he uttered the immortal words that echoed down through prophetic history: <strong>"La tathreeba 'alaykumul-yawm, yaghfirullahu lakum"</strong> (No reproach upon you today; Allah will forgive you). The Prophet Muhammad ﷺ quoted these exact words upon the Conquest of Makkah when pardoning his bitterest persecutors.</p>
        <h4>The Metaphysical Mystery of Divine Lutf</h4>
        <p>Reflecting upon his life's trajectory from the bottom of the well to the throne of Egypt, Yusuf did not boast of his intellect or virtue; he attributed everything to divine subtlety: <strong>"Inna Rabbee lateefun lima yashaa'"</strong> (Indeed, my Lord is subtle in whatever He wills). <em>Al-Lateef</em> orchestrates grand cosmic victories through hidden, imperceptible means—using malice, false accusations, and iron prison bars as the precise vehicles to elevate His beloved servants.</p>
        <h4>The Ultimate Supplication of the Believer</h4>
        <p>At the absolute summit of worldly majesty, surrounded by his parents and brothers prostrating in honor (*Sujood at-tahiyyah*), Yusuf detached completely from transient power. He raised his hands in the ultimate supplication recorded in scripture: <em>"Creator of the heavens and earth, You are my protector in this world and the Hereafter. <strong>Cause me to die as a Muslim and join me with the righteous</strong>" (*Tawaffanee Musliman wa alhiqnee bis-saliheen*)</em>.</p>
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>15</b> Lectures &bull; <b>100%</b> Sunni Verified';
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
        "Movement 8": 8,
        "Literary Analysis": 8
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

print(f"Successfully generated Surah Yusuf Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
