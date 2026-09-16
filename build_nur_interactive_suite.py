#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Nur Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Ordeal of Slander (Hadith al-Ifk) & Communal Epistemology
    2. The Architecture of Domestic Privacy (Isti'dhan) & The Lowered Gaze
    3. Ayah an-Nur (Light Upon Light) & The Metaphysics of Illumination
    4. The Divine Charter of Succession (Ayat al-Istikhlaf) & The Assembly of Truth
- 5-Lecture Foundation Audio Syllabus Explorer (04h 16m 38s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_NUR_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_nur_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_nur_html_and_md import pages_data

# 5 Audio Foundation lectures syllabus (04h 16m 38s total)
audio_lectures = [
    ("24.An-nurPart1.opus", "Legal Boundaries, Qadhf & The Onset of the Ifk", "Movement 1", "01h 00m 45s"),
    ("24.An-nurPart2.opus", "The Vindication of 'A'ishah & Communal Ethics", "Movement 2", "01h 09m 00s"),
    ("24.An-nurPart3.opus", "Domestic Privacy, Modesty & The Architecture of Light", "Movement 3", "57m 13s"),
    ("24.An-nurPart4.opus", "The Houses of Dhikr & Parables of Darkness", "Movement 4", "34m 48s"),
    ("24.An-nurPart5.opus", "Cosmic Prostration, Istikhlaf & Prophetic Reverence", "Movement 5", "34m 50s")
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
  <title>Surah An-Nur — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>SURAH AN-NUR &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_NUR_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/NUR_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/NUR_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across An-Nur (e.g., ifk, slander, abu bakr, isti'dhan, gaze, ayah an-nur, mirage, istikhlaf)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>5</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('ifkModal')">The Slander & Abu Bakr's Pardon</button>
        <button class="btn btn-outline" onclick="openModal('privacyModal')">Domestic Privacy & The Gaze</button>
        <button class="btn btn-outline" onclick="openModal('lightModal')">Ayah an-Nur (Light Upon Light)</button>
        <button class="btn btn-outline" onclick="openModal('istikhlafModal')">Charter of Succession (Istikhlaf)</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (04h 16m 38s TOTAL)</span>
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

  <!-- MODAL 1: THE SLANDER & PARDON -->
  <div class="modal-backdrop" id="ifkModal" onclick="closeOnBackdrop(event, 'ifkModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Ordeal of Slander (Hadith al-Ifk) & Abu Bakr's Supreme Pardon</h3>
        <button class="modal-close" onclick="closeModal('ifkModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Indeed, those who came with falsehood are a group among you. Do not think it bad for you; rather it is good for you... And let not those of virtue among you and wealth swear not to give aid to relatives and the needy... Do you not love that Allah should forgive you? And Allah is Forgiving and Merciful."
        </div>
        <h4>The Trial of Hadith al-Ifk</h4>
        <p>Engineered by the hypocrites under Abdullah ibn Ubayy, the fabricated rumor sought to assassinate the character of Mother of the Believers 'A'ishah. Allah withheld revelation for thirty days to expose latent hypocrisy and test the spiritual maturity of the nascent Muslim community.</p>
        <h4>The Communal Principle of Wholesome Presumption</h4>
        <p>The Qur'an reprimanded the community: when hearing unsubstantiated allegations against a believer, the immediate internal obligation is to think well of them (<em>Dhannal-mu'minuna bi-anfusihim khayra</em>) and proclaim: <em>Subhanaka hadha buhtanun 'adheem</em> (Exalted are You! This is an immense slander!).</p>
        <h4>Abu Bakr's Pinnacle of Forgiveness</h4>
        <p>When Abu Bakr vowed never to aid his relative Mistah (who had shared the rumor), Allah revealed: <em>"Ala tuhibbuna an yaghfirallahu lakum?"</em> Abu Bakr immediately dissolved his oath, restoring the stipend with expanded generosity, setting the eternal standard for pardoning personal injury.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: DOMESTIC PRIVACY & THE GAZE -->
  <div class="modal-backdrop" id="privacyModal" onclick="closeOnBackdrop(event, 'privacyModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Architecture of Domestic Privacy (Isti'dhan) & The Lowered Gaze</h3>
        <button class="modal-close" onclick="closeModal('privacyModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "O you who have believed, do not enter houses other than your own houses until you ascertain welcome and greet their inhabitants... Tell the believing men to reduce of their vision and guard their private parts. That is purer for them... And tell the believing women to reduce of their vision and guard their private parts and not display their adornment except that which [ordinarily] appears thereof..."
        </div>
        <h4>The Inviolability of the Home (*Isti'dhan*)</h4>
        <p>The private household is established as an impenetrable sanctuary of emotional safety and modesty. Believers must seek permission and extend greetings of peace before entering. If asked to turn back, they must do so gracefully with zero resentment.</p>
        <h4>Lowering the Gaze (*Ghadhdh al-Basar*)</h4>
        <p>Ibn al-Qayyim notes that visual desire is the primary conduit to the heart. Restraining the gaze from provocative stimuli purifies the soul (<em>Azka lahum</em>) and deposits a profound sweetness of faith directly within the believer's consciousness.</p>
        <h4>The Veil of Dignity (*The Khumur*)</h4>
        <p>Women are directed to draw their head coverings over their bodices, concealing private beauty from commercialization and objectification, anchoring social interactions in intellectual and moral substance rather than physical display.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: AYAH AN-NUR -->
  <div class="modal-backdrop" id="lightModal" onclick="closeOnBackdrop(event, 'lightModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Ayah an-Nur (Light Upon Light) & The Metaphysics of Illumination</h3>
        <button class="modal-close" onclick="closeModal('lightModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Allah is the Light of the heavens and the earth. The example of His light is like a niche within which is a lamp, the lamp is within glass, the glass as if it were a pearlescent star lit from a blessed olive tree, neither of the east nor of the west, whose oil would almost glow even if untouched by fire. Light upon light. Allah guides to His light whom He wills."
        </div>
        <h4>The Niche, Glass & Radiant Lamp</h4>
        <p>In classical exegesis (<em>Ubayy ibn Ka'b, Ibn Abbas</em>), the niche represents the ribcage of the believer; the glass represents the clear, delicate heart; the lamp represents revelation; and the blessed olive tree represents the uncorrupted primordial nature (<em>fitrah</em>).</p>
        <h4>Spontaneous Combustion of Truth (*Noorun 'Ala Noor*)</h4>
        <p>The uncorrupted human fitrah is so naturally attuned to divine truth that its pure oil almost radiates on its own. When touched by the divine flame of Qur'anic revelation, the combustion produces <strong>Light Upon Light</strong>—a blazing, harmonious convergence of reason and scripture.</p>
        <h4>The Parables of Disbelief: Mirage & Ocean Abyss</h4>
        <p>In stark contrast, the deeds of deniers are like a desert mirage (dissolving into divine reckoning) or an abyssal ocean enveloped in waves beneath storm clouds: darkness upon darkness where one cannot see one's own hand. Whomever Allah grants no light has no light at all.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: CHARTER OF ISTIKHLAF -->
  <div class="modal-backdrop" id="istikhlafModal" onclick="closeOnBackdrop(event, 'istikhlafModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Divine Charter of Succession (Ayat al-Istikhlaf) & The Assembly</h3>
        <button class="modal-close" onclick="closeModal('istikhlafModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Allah has promised those who have believed among you and done righteous deeds that He will surely grant them succession upon the earth just as He granted it to those before them, and that He will surely establish for them their religion which He has preferred for them, and that He will surely substitute for them, after their fear, security, [for] they worship Me, not associating anything with Me."
        </div>
        <h4>The Inviolable Promise of Earthly Leadership (*Istikhlaf*)</h4>
        <p>Surah An-Nur establishes that political empowerment, cultural flourishing, and enduring security are divine fruits granted exclusively to communities that embody authentic faith, establish social equity, and worship Allah without any compromise or partnership.</p>
        <h4>The Hallmarks of Faith: "We Hear and We Obey"</h4>
        <p>While hypocrites flee from divine arbitration when it threatens their personal greed, true believers respond to divine law with unconditional submission: <em>Sami'na wa ata'na</em> (We hear and we obey). These are the truly triumphant (<em>Al-Muflihoon</em>).</p>
        <h4>Reverence in the Prophetic Assembly</h4>
        <p>The surah concludes by demanding absolute decorum and respect for the Messenger: do not address him casually, do not slip away stealthily from communal duties, and heed the grave warning: opposing his commands risks severe fitnah and painful affliction.</p>
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
        "Movement 3": 3,
        "Movement 4": 5,
        "Movement 5": 6
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

print(f"Successfully generated Surah An-Nur Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
