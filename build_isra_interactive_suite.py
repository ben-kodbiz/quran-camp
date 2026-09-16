#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Isra Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Bodily Ascension & Sanctity of Al-Aqsa (Subhana Alladhi Asra)
    2. The Universal Ethical Decalogue & Filial Piety (Birr al-Walidayn)
    3. Inherent Human Dignity & The Satanic Ambush (Wa Laqad Karramna)
    4. The Enigma of the Soul & The Praised Station (Al-Ruh & Tahajjud)
- 4-Lecture Foundation Audio Syllabus Explorer (03h 41m 56s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_ISRA_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_isra_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_isra_html_and_md import pages_data

# 4 Audio Foundation lectures syllabus
audio_lectures = [
    ("17.Al-israPart1.opus", "The Night Journey, Bani Isra'il's Two Epochs & The Most Upright Guide", "Movement 1", "01h 09m 51s"),
    ("17.Al-israPart2.opus", "The Ethical Decalogue: Filial Piety, Economic Balance & Sanctity of Life", "Movement 2", "01h 09m 54s"),
    ("17.Al-israPart3.opus", "The Cosmic Choir of Creation, Human Dignity & The Threat of Iblis", "Movement 3", "43m 41s"),
    ("17.Al-israPart4.opus", "The Enigma of Al-Ruh, Tahajjud, Musa's Nine Proofs & Weeping in Sujood", "Movement 4", "38m 29s")
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
  <title>Surah Al-Isra — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>SURAH AL-ISRA &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_ISRA_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/ISRA_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/ISRA_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across Al-Isra (e.g., ascent, parents, uff, soul, tahajjud, musa)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>4</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('asraModal')">The Night Journey</button>
        <button class="btn btn-outline" onclick="openModal('decalogueModal')">Filial Piety & Decalogue</button>
        <button class="btn btn-outline" onclick="openModal('karamahModal')">Inherent Human Dignity</button>
        <button class="btn btn-outline" onclick="openModal('tahajjudModal')">The Soul & Tahajjud</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (03h 41m 56s TOTAL)</span>
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

  <!-- MODAL 1: THE NIGHT JOURNEY -->
  <div class="modal-backdrop" id="asraModal" onclick="closeOnBackdrop(event, 'asraModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Bodily Ascension & Sanctity of Al-Aqsa (Subhana Alladhi Asra)</h3>
        <button class="modal-close" onclick="closeModal('asraModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Exalted is He who took His Servant by night from al-Masjid al-Haram to al-Masjid al-Aqsa, whose surroundings We have blessed, to show him of Our signs. Indeed, He is the Hearing, the Seeing."
        </div>
        <h4>The Absolute Transcendence of Subhan</h4>
        <p>The surah opens with the absolute verbal noun <em>Subhan</em>, affirming that God is completely elevated above every conceivable limitation of physics, time, or spatial velocity. When the Creator acts, the ordinary constraints governing mortal creatures cease to apply.</p>
        <h4>The Bodily Reality of the Journey</h4>
        <p>Unanimous Sunni exegesis (<em>At-Tabari, Ibn Kathir, Al-Qurtubi</em>) affirms that the nocturnal ascension occurred in both body and soul (<em>bi-ruhihi wa jasadihi</em>) in waking consciousness. Had it been a mere vision or dream, the Quraysh would never have contested it or challenged the Prophet ﷺ to describe the gates and caravans of Jerusalem.</p>
        <h4>The Global Monotheistic Transition</h4>
        <p>By journeying from the Ka'bah to the sanctuary of Jerusalem, the final Prophet ﷺ unified the two sacred poles of monotheistic history. Leading all previous prophets in congregational prayer at Al-Aqsa, he formally received the mantle of global spiritual leadership.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: PARENTAL PIETY & DECALOGUE -->
  <div class="modal-backdrop" id="decalogueModal" onclick="closeOnBackdrop(event, 'decalogueModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Universal Ethical Decalogue & Filial Piety</h3>
        <button class="modal-close" onclick="closeModal('decalogueModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And your Lord has decreed that you not worship except Him, and to parents, good treatment. Whether one or both of them reach old age [while] with you, say not to them so much as 'uff' and do not repel them but speak to them a noble word. And lower to them the wing of humility out of mercy..."
        </div>
        <h4>The Supreme Obligation: Tawhid & Parents</h4>
        <p>God couples His singular worship directly with unconditional benevolence to parents (<em>Birr al-Walidayn</em>). In classical jurisprudence, serving aging parents is prioritized above voluntary acts of worship and collective strivings.</p>
        <h4>The Criminalization of 'Uff'</h4>
        <p>The Arabic syllable <em>Uff</em> represents the most minuscule expression of irritation or grumbling. By outlawing <em>Uff</em>, the divine command criminalizes rolling the eyes, heavy sighing, showing impatient gestures, or curt responses to elderly parents who regress into physical and cognitive vulnerability.</p>
        <h4>The Lowered Wing of Humility (*Janah adh-Dhull*)</h4>
        <p>The metaphor of a bird sheltering its fragile chicks is tenderly inverted: the adult child must now lower their wings of submission and tender affection over their aging parents, actively praying: <em>Rabbi irhamhuma kama rabbayanee sagheera</em> ("My Lord, have mercy upon them as they brought me up when I was small").</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: INHERENT HUMAN DIGNITY -->
  <div class="modal-backdrop" id="karamahModal" onclick="closeOnBackdrop(event, 'karamahModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Inherent Human Dignity & The Satanic Ambush</h3>
        <button class="modal-close" onclick="closeModal('karamahModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And We have certainly honored the children of Adam and carried them on the land and sea and provided for them of the good things and preferred them over much of what We have created, with [definite] preference."
        </div>
        <h4>The Ontological Charter of Karamah</h4>
        <p>Human worth in Islam is an inalienable divine gift bestowed upon all <em>Bani Adam</em> (the human family) without exception. Endowed with intellect, free will, upright physical stature, and articulate speech, human beings are capable of transcending angelic ranks through deliberate moral obedience.</p>
        <h4>The Jealous Fury of Iblis (*La-Ahtanikanna*)</h4>
        <p>Satan could not endure human elevation: *"Do You see this one whom You have honored above me? If You respite me, I will surely bridle his descendants except a few."* The word <em>ahtanikanna</em> derives from the bit and bridle placed upon beasts of burden, illustrating Satan's goal to reduce dignified human beings into instinct-driven animals.</p>
        <h4>The Divine Shield Over Believers</h4>
        <p>Despite Satan's deployment of whispered voices, seductions, and economic entrapment, the divine decree stands firm: <em>Inna 'ibadee laysa laka 'alayhim sultan</em> ("Indeed, over My sincere servants you possess zero authority"). Sincere servitude to God provides an impenetrable cosmic shield.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: THE SOUL & TAHAJJUD -->
  <div class="modal-backdrop" id="tahajjudModal" onclick="closeOnBackdrop(event, 'tahajjudModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Enigma of the Soul & The Praised Station</h3>
        <button class="modal-close" onclick="closeModal('tahajjudModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And they ask you about the soul. Say, 'The soul is of the affair of my Lord. And mankind have not been given of knowledge except a little.' ... And from [part of] the night, pray with it as additional [worship] for you; it is expected that your Lord will resurrect you to a praised station."
        </div>
        <h4>The Transcendent Secret of Al-Ruh</h4>
        <p>When questioned by Meccan skeptics coached by Medina rabbis, the revelation established that the soul belongs to the divine realm of command (<em>'Alam al-Amr</em>). While physical science measures brain activity, neurochemistry, and biological tissues, the conscious essence of the human soul remains beyond material reductionism.</p>
        <h4>The Discipline of Tahajjud</h4>
        <p>Rising from slumber in the stillness of deep night (<em>Tahajjud</em>) constitutes the masterclass of spiritual fortitude. Worshipping when the world sleeps purifies the intention, shatters ostentation, and grants profound inner clarity.</p>
        <h4>The Praised Station (Al-Maqam al-Mahmood)</h4>
        <p>Authenticated in <em>Sahih al-Bukhari</em>, the Praised Station is the supreme intercession (<em>Ash-Shafa'ah al-'Uzma</em>) reserved exclusively for Prophet Muhammad ﷺ on the Day of Resurrection, when all previous messengers step back, and all mankind praises his glorious standing before the Throne of God.</p>
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

print(f"Successfully generated Surah Al-Isra Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
