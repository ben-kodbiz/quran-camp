#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Nahl Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card live fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Biological Miracle of Pure Milk (Labanan Khalisan Sa'ighan)
    2. The Divine Inspiration of the Bee & Honey as Healing (Al-Nahl & Shifa' Lin-Nas)
    3. The Universal Moral Charter & The Unraveling Weaver ('Adl, Ihsan & Naqadat Ghazlaha)
    4. The Universal Guarantee of Hayatan Tayyibah & The Sanctuary of Duress (Hayatan Tayyibah & Illa Man Ukriha)
- 5-Lecture Foundation Audio Syllabus Explorer (03h 56m 05s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_NAHL_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_nahl_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_nahl_html_and_md import pages_data

# 5 Audio Foundation lectures syllabus
audio_lectures = [
    ("16.An-nahlPart1.opus", "Cosmic Sovereignty, Aesthetic Splendor of Herds & Water from Heaven", "Movement 1", "40m 54s"),
    ("16.An-nahlPart2.opus", "The Ocean Highway, Mountain Pegs & Innumerable Favors vs Skeptic Blindness", "Movement 2", "34m 02s"),
    ("16.An-nahlPart3.opus", "Pure Milk from Chyme/Blood, Inspiration of the Bee & Two Parables", "Movement 3", "01h 01m 22s"),
    ("16.An-nahlPart4.opus", "The Universal Moral Charter, The Unraveling Weaver & Hayatan Tayyibah", "Movement 4", "55m 39s"),
    ("16.An-nahlPart5.opus", "Isti'adhah Protocol, Coerced Faith, Model Ibrahim & Charter of Dawah", "Movement 5", "44m 08s")
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
  <title>Surah An-Nahl — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>SURAH AN-NAHL &bull; MASTER CARTOGRAPHY & INTERACTIVE SUITE</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_NAHL_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>
          <span>Download 10-Plate Master PDF</span>
        </a>
        <a href="../07_MINDMAP/NAHL_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">
          <span>Mindmap HTML</span>
        </a>
        <a href="../07_MINDMAP/NAHL_MASTER_MINDMAP.md" class="btn btn-outline" target="_blank">
          <span>Markdown Source</span>
        </a>
      </div>
    </header>

    <div class="search-panel">
      <div class="search-input-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Filter 64 cards across An-Nahl (e.g., milk, bee, weaver, tayyibah, duress, covenant)..." onkeyup="handleLiveSearch()">
      </div>
      <div class="search-stats" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>5</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
      <div class="deep-dive-bar">
        <button class="btn btn-outline" onclick="openModal('milkModal')">Pure Milk</button>
        <button class="btn btn-outline" onclick="openModal('beeModal')">Inspiration of the Bee</button>
        <button class="btn btn-outline" onclick="openModal('weaverModal')">Unraveling Weaver</button>
        <button class="btn btn-outline" onclick="openModal('tayyibahModal')">Hayatan Tayyibah & Duress</button>
      </div>
    </div>

    <div class="audio-panel">
      <h3>
        <span>FOUNDATION AUDIO LECTURE SYLLABUS (03h 56m 05s TOTAL)</span>
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

  <!-- MODAL 1: PURE MILK -->
  <div class="modal-backdrop" id="milkModal" onclick="closeOnBackdrop(event, 'milkModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Biological Miracle of Pure Milk (Labanan Khalisan Sa'ighan)</h3>
        <button class="modal-close" onclick="closeModal('milkModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And indeed, for you in grazing livestock is a lesson. We give you drink from what is in their bellies - between chyme and blood - pure milk, palatable to drinkers."
        </div>
        <h4>The Interstitial Synthesis (*Min Bayni Farthin wa Dam*)</h4>
        <p>In classical Sunni exegesis (<em>At-Tabari, Al-Qurtubi, Ibn Kathir</em>), the phrase <em>min bayni farthin wa dam</em> describes a profound physiological boundary. Digested fodder resides in the gut as chyme (<em>farth</em>), while circulating blood (<em>dam</em>) traverses vascular networks. Pure, pristine milk (<em>labanan khalisan</em>) emerges perfectly filtered between them, bearing neither the foul stench of bodily waste nor the crimson stain of blood.</p>
        <h4>Metaphysical Significance for the Soul</h4>
        <p>Al-Razi highlights that this physiological miracle serves as an allegorical compass for spiritual preservation. Just as nourishing, white sustenance is extracted unsullied from a digestive tract fraught with impurities, the sincere believer's faith (*Tawhid*) must remain pure, uncontaminated by societal corruption, moral compromise, or philosophical skepticism.</p>
        <h4>Palatability (*Sa'ighan Li-sh-Sharibeen*)</h4>
        <p>Milk is unique among fluids: nourishing, soothing, and effortlessly digested. It lubricates the throat and provides complete bodily sustenance. In prophetic tradition, when milk is consumed, the specific supplication is: <em>Allahumma barik lana feehi wa zidna minhu</em>—acknowledging it as the only single food that simultaneously replaces both food and beverage.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: INSPIRATION OF THE BEE -->
  <div class="modal-backdrop" id="beeModal" onclick="closeOnBackdrop(event, 'beeModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Divine Inspiration of the Bee & Honey as Healing</h3>
        <button class="modal-close" onclick="closeModal('beeModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And your Lord inspired to the bee, 'Take for yourself among the mountains, houses, and among the trees and in that which they construct. Then eat from all the fruits and follow the ways of your Lord laid down [for you].' There emerges from their bellies a drink, varying in colors, in which there is healing for people."
        </div>
        <h4>The Nature of Instinctual Inspiration (*Al-Wahy al-Ilhami*)</h4>
        <p>The term <em>awha</em> here does not signify prophetic legislative revelation (<em>wahy ash-shar'</em>), but divine instinctual direction and instinctive engineering (<em>wahy ilham wa taskhir</em>). Classical scholars (<em>Ibn al-Qayyim, Al-Baghawi</em>) remark upon the awe-inspiring architectural precision of the bee: constructing perfect hexagonal cells with minimal wax and maximal volumetric efficiency without compass or ruler.</p>
        <h4>The Subjugated Pathways (*Subula Rabbiki Dhulula*)</h4>
        <p>The worker bee flies miles away from its hive across vast meadows and rugged terrain, yet navigates unerringly back through complex flight paths made docile (*dhulul*) by divine decree. It extracts minuscule nectars without injuring foliage or floral structures, modeling ecological harmony.</p>
        <h4>Chromatic Diversity & Curative Power (*Shifa'un Lin-Nas*)</h4>
        <p>The exudation varies in color—amber, golden, translucent, and dark brown—reflecting soil mineralogy and floral species. Honey possesses proven antibacterial, regenerative, and soothing qualities. Authenticated in <em>Sahih al-Bukhari</em>, the Prophet ﷺ prescribed honey for chronic digestive disorders, asserting: <em>Sadaqa Allahu wa kadhaba batnu akheek</em> ("Allah has spoken truth, and your brother's stomach has lied").</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: UNRAVELING WEAVER -->
  <div class="modal-backdrop" id="weaverModal" onclick="closeOnBackdrop(event, 'weaverModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Universal Moral Charter & The Unraveling Weaver</h3>
        <button class="modal-close" onclick="closeModal('weaverModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Indeed, Allah orders justice and good conduct and giving to relatives and forbids immorality and bad conduct and oppression. He admonishes you that perhaps you will be reminded... And do not be like she who untwisted her spun thread after it was strong [by] taking your oaths as [a means of] deceit between you."
        </div>
        <h4>The Friday Moral Charter (*Ayat al-Jumu'ah*)</h4>
        <p>Ibn Mas'ud declared this passage the most comprehensive verse in the entire Qur'an regarding virtues and vices. Historically adopted by the righteous caliph 'Umar ibn 'Abd al-'Aziz to conclude every Friday sermon, it structures human ethics across a master triad:</p>
        <ul>
          <li><strong>Commanded:</strong> Justice (<em>'Adl</em> - equitable balance), Benevolence (<em>Ihsan</em> - gracious excellence beyond duty), and Kinship Support (<em>Ita'i Dhil-Qurba</em> - communal solidarity).</li>
          <li><strong>Prohibited:</strong> Immorality (<em>Fahsha'</em> - lewdness & hidden sins), Transgression (<em>Munkar</em> - public vices repudiated by conscience), and Oppression (<em>Baghy</em> - tyrannical aggression against rights).</li>
        </ul>
        <h4>The Parable of the Mecca Weaver (*Naqadat Ghazlaha*)</h4>
        <p>Classical commentators identify the tragic archetype as a mentally erratic woman of Mecca named Raytah, who would painstakingly spin fine woolen yarn all morning, only to violently dismantle it thread by thread before sundown. The Qur'an uses this unforgettable imagery to warn believers against nullifying accumulated righteousness, dismantling treaties, or breaking solemn vows for petty geopolitical opportunism.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: HAYATAN TAYYIBAH & DURESS -->
  <div class="modal-backdrop" id="tayyibahModal" onclick="closeOnBackdrop(event, 'tayyibahModal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>The Guarantee of Hayatan Tayyibah & The Sanctuary of Duress</h3>
        <button class="modal-close" onclick="closeModal('tayyibahModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Whoever does righteousness, whether male or female, while he is a believer - We will surely cause him to live a good life, and We will surely give them their reward according to the best of what they used to do... Whoever disbelieves in Allah after his belief - except for one who is forced [to renounce it] while his heart is secure in faith - but those who [willingly] open their breasts to disbelief, upon them is wrath from Allah."
        </div>
        <h4>The Egalitarian Guarantee of Wholesome Life (*Hayatan Tayyibah*)</h4>
        <p>This verse dismantles pre-Islamic misogyny and spiritual hierarchy: spiritual elevation and divine reward are identical for man and woman (*min dhakarin aw untha*). Commentators (<em>Ibn Abbas, Ali ibn Abi Talib, Al-Hasan al-Basri</em>) define <em>Hayatan Tayyibah</em> not as hedonistic affluence, but as inward tranquility, contentment (*qana'ah*), and the sweetness of intimate connection with Allah in this world.</p>
        <h4>The Jurisprudence of Duress (*Rukhsa of Ammar ibn Yasir*)</h4>
        <p>Revealed concerning the brutal torture of the companion Ammar ibn Yasir, whose parents Sumayyah and Yasir were martyred before his eyes. When coerced by intense torment to utter blasphemous words, Ammar wept before the Prophet ﷺ in deep anguish. The Prophet asked: <em>Kayfa tajidu qalbaka?</em> ("How do you find your heart?"). Ammar replied: <em>Mutma'innan bil-iman</em> ("Secure and tranquil in faith").</p>
        <p>The Prophet ﷺ replied: <em>In 'adoo fa-'ud</em> ("If they return to torture you, say it again"). This established a cornerstone principle in Islamic jurisprudence: legal culpability requires intention and free will; coerced verbal utterances under threat of death or severe mutilation do not nullify faith when the heart remains an unyielding fortress of belief.</p>
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
        "Movement 3": 4,
        "Movement 4": 6,
        "Movement 5": 7
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

print(f"Successfully generated Surah An-Nahl Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
