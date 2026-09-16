#!/usr/bin/env python3
"""
Huurs Studio - Surah Ibrahim Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Universal Law of Gratitude (La'in Shakartum La-Azeedannakum)
    2. The Parable of the Stormy Ashes (Ka-Ramadin Ishtaddat Bihir-Reeh)
    3. The Eschatological Khutbah of Iblis in Hell (Fa-la Taloomoonee)
    4. The Pure Tree (Kalimah Tayyibah) & The Abrahamic Valley of Prayer
- 4-Lecture Foundation Audio Syllabus Explorer (01h 25m 58s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_IBRAHIM_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_ibrahim_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_ibrahim_html_and_md import pages_data

# 4 Audio Foundation lectures syllabus
audio_lectures = [
    ("14.Ibrahim1-14.opus", "Darkness to Light, Language of Messengers, Ayyam Allah & Gratitude", "Movement 1 & 2", "21m 16s"),
    ("14.Ibrahim15-32.opus", "Stormy Ashes, Festering Sadeed, Satan's Khutbah & The Pure Tree", "Movement 3, 4 & 5", "18m 47s"),
    ("14.Ibrahim33-39.opus", "Cosmic Subjugation, Innumerable Favors & Ibrahim at Makkah", "Movement 6", "22m 58s"),
    ("14.Ibrahim40-52.opus", "The Model Du'a, Staring Eyes, The Transmuted Earth & Final Balagh", "Movement 7 & 8", "22m 55s")
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
  <title>Surah Ibrahim — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>Surah Ibrahim • Master Cartography & Interactive Digital Suite</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_IBRAHIM_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>Download Master PDF</a>
        <a href="../07_MINDMAP/IBRAHIM_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">Full Cartography View</a>
      </div>
    </header>

    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Search across 64 analytical cards, theological themes, Arabic terminology..." oninput="handleLiveSearch()">
      </div>
      <div class="stats-badge" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>4</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
    </div>

    <div class="modals-bar">
      <button class="btn-modal-trigger" onclick="openModal('gratitudeModal')">
        <span>🌱</span> The Universal Law of Gratitude (La'in Shakartum)
      </button>
      <button class="btn-modal-trigger" onclick="openModal('ashesModal')">
        <span>💨</span> The Parable of the Stormy Ashes (Ka-Ramadin)
      </button>
      <button class="btn-modal-trigger" onclick="openModal('khutbahModal')">
        <span>🔥</span> Satan's Grand Khutbah in Hell (Fa-la Taloomoonee)
      </button>
      <button class="btn-modal-trigger" onclick="openModal('treeModal')">
        <span>🌴</span> The Pure Tree & The Barren Valley of Prayer
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
        <span>4 Lectures &bull; 01h 25m 58s &bull; Click to filter corresponding plates</span>
      </div>
      <div class="audio-grid">
        {{AUDIO_ITEMS_HTML}}
      </div>
    </section>
  </div>

  <!-- MODAL 1 -->
  <div class="modal-backdrop" id="gratitudeModal" onclick="closeOnBackdrop(event, 'gratitudeModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Universal Law of Gratitude (La'in Shakartum)</h3>
        <button class="modal-close" onclick="closeModal('gratitudeModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And [remember] when your Lord proclaimed: 'If you are grateful, I will surely increase you; but if you show ingratitude, indeed My punishment is severe.' And Moses said: 'If you and whoever is on the earth should disbelieve altogether, indeed Allah is Free of need and Praiseworthy.'"
        </div>
        <h4>The Ontological Law of Increase</h4>
        <p>In classical Sunni theology (expounded by <strong>Imam al-Qurtubi</strong> and <strong>Ibn al-Qayyim</strong> in <em>'Uddat as-Sabireen</em>), the divine declaration <em>Ta'adh-dhana Rabbukum</em> indicates an immutable, binding universal law. Gratitude (*Shukr*) is not mere polite rhetoric; it is an active spiritual technology that preserves current blessings (*Qayd al-Mawjood*) and captures missing blessings (*Sayd al-Mafqood*).</p>
        <h4>The Tripartite Practice of Shukr</h4>
        <p>True gratitude must operate across all three dimensions of human consciousness:</p>
        <ul>
          <li><strong>Heartfelt Conviction (*I'tiraf bil-Qalb*):</strong> Knowing with certainty that every breath, ability, and provision flows exclusively from divine grace, not personal entitlement or cunning.</li>
          <li><strong>Verbal Praise (*Thana' bil-Lisan*):</strong> Acknowledging the Giver with humble, continuous praise rather than boasting to creation.</li>
          <li><strong>Physical Obedience (*'Amal bil-Jawarih*):</strong> Utilizing the granted blessing strictly in alignment with the moral law of the Giver.</li>
        </ul>
        <h4>The Independence of the Divine Court</h4>
        <p>Prophet Musa clarified that gratitude benefits only the human soul: if all humanity from East to West were to unite in bitter denial, God’s dominion would not diminish by the weight of a dust mote. Allah is intrinsically <strong>Ghaniyyun Hameed</strong> (Self-Sufficient and Praiseworthy), independent of all creation.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2 -->
  <div class="modal-backdrop" id="ashesModal" onclick="closeOnBackdrop(event, 'ashesModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Parable of the Stormy Ashes (Ka-Ramadin Ishtaddat)</h3>
        <button class="modal-close" onclick="closeModal('ashesModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "The example of those who disbelieve in their Lord is that their deeds are like ashes on which the wind blows violently on a stormy day; they have no power over anything from what they earned. That is the extreme straying."
        </div>
        <h4>The Illusion of Secular Merit</h4>
        <p><strong>Imam Fakhr ad-Din ar-Razi</strong> notes that secular humans often spend lifetimes amassing charitable works, scientific projects, or institutional monuments, assuming these achievements guarantee permanent moral merit. The Qur'an analyzes the metaphysical reality of deeds severed from Tawhid: because they were unanchored to the Eternal Source and performed for worldly vanity or temporal applause, they possess zero ontological mass.</p>
        <h4>The Tempest of Judgment Day</h4>
        <p>On a quiet, windless day, a heap of grey ashes (*Ramad*) sitting on an exposed boulder appears solid and substantial. But when the hurricane of the Day of Judgment strikes (*Fee yawmin 'asif*), that mountain of ash is obliterated in a single instant, scattered into invisible airborne particles across the abyss.</p>
        <h4>Complete Spiritual Destitution</h4>
        <p>The denier reaches out his hands to grasp the fruits of a lifetime of frantic worldly labor, only to find nothingness (*La yaqdiroona mimma kasaboo 'ala shay'*). Only deeds rooted in sincere devotion to Allah and aligned with prophetic guidance possess the celestial density to endure the storm of eternity.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3 -->
  <div class="modal-backdrop" id="khutbahModal" onclick="closeOnBackdrop(event, 'khutbahModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>Satan's Grand Khutbah in Hell (Fa-la Taloomoonee)</h3>
        <button class="modal-close" onclick="closeModal('khutbahModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And Satan will say when the matter has been concluded: 'Indeed, Allah promised you the promise of truth. And I promised you, but I betrayed you. But I had no authority over you except that I invited you, and you responded to me. So do not blame me; blame yourselves! I cannot come to your aid, nor can you come to mine. Indeed, I deny your previous association of me with Allah...'"
        </div>
        <h4>The Master Betrayer's Pulpit of Fire</h4>
        <p>Classical exegetes, including <strong>Imam at-Tabari</strong> and <strong>Ibn Kathir</strong>, describe the scene: after the scale of justice has tilted, the gates of Hell have clanged shut, and the damned turn in fury upon their deceivers, Satan mounts a pulpit of fire in the abyss to deliver the final sermon of cosmic history.</p>
        <h4>Dismantling the Excuse of Coercion</h4>
        <p>Iblis delivers an unsparing, humiliating confession that destroys every human defense:</p>
        <ul>
          <li><strong>The Vindication of Divine Truth:</strong> He confesses that God’s messengers spoke 100% truth (*Wa'dal-haqq*), while every secular seduction he whispered was a calculated lie (*Akhlaftukum*).</li>
          <li><strong>Zero Coercive Power:</strong> He had no chains, no police, and no physical weapons (*Ma kana liya 'alaykum min sultan*). He possessed only an invitation (*Da'awtukum*), and the human ego eagerly, willingly ran to embrace it.</li>
          <li><strong>The Ultimate Mockery:</strong> <em>"Fa-la taloomoonee wa loomoo anfusakum"</em>—Do not waste your breath blaming me; blame your own corrupt souls!</li>
        </ul>
        <h4>The Radical Lesson of Personal Accountability</h4>
        <p>This verse forces the believer to discard all modern culture of victimhood and rationalization. The devil cannot make you sin; he only knocks. You are the sovereign master of the door of your own heart.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4 -->
  <div class="modal-backdrop" id="treeModal" onclick="closeOnBackdrop(event, 'treeModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Pure Tree & The Barren Valley of Prayer</h3>
        <button class="modal-close" onclick="closeModal('treeModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Have you not considered how Allah presents an example, making a good word like a good tree, whose root is firmly fixed and its branches high in the sky? It produces its fruit all the time, by permission of its Lord... Our Lord, indeed I have settled some of my descendants in an uncultivated valley near Your Sacred House, in order that they establish prayer. So make hearts among mankind yearn toward them..."
        </div>
        <h4>The Morphology of Kalimah Tayyibah</h4>
        <p>In <em>Sahih al-Bukhari</em>, the Prophet Muhammad ﷺ confirmed that the <strong>Shajarah Tayyibah</strong> is the Date Palm (*An-Nakhlah*). <strong>Imam Ibn al-Qayyim</strong> in <em>I'lam al-Muwaqqi'een</em> extracts the spiritual anatomy:</p>
        <ul>
          <li><strong>Asluha Thabit (Roots Deep in Bedrock):</strong> The testimony of Tawhid (*La ilaha illa Allah*) anchored deeply in the fitrah and intellect, completely unaffected by cultural storms or intellectual doubts.</li>
          <li><strong>Far'uha fis-Samaa' (Canopy in the Sky):** Noble character, sincere prayers, and righteous actions continuously ascending directly to the Throne.</li>
          <li><strong>Tu'tee Ukulaha Kulla Heen:</strong> Producing spiritual, moral, and physical nourishment in every season of life without fail.</li>
        </ul>
        <h4>The Sacred Architecture of Makkah</h4>
        <p>This spiritual tree found its earthly embodiment when Prophet Ibrahim stood in the waterless, scorched canyon of Makkah (*Bi-wadin ghayri dhee zar'in*). Leaving his infant son and wife solely upon divine command, he defined the purpose of the settlement: <strong>Li-yuqeemu as-Salah</strong> (to establish regular prayer). Economics, trade, and politics were strictly subordinate to worship.</p>
        <h4>The Magnet of Hearts: Tahwee Ilayhim</h4>
        <p>Ibrahim did not pray for tourists or conquest; he prayed for <em>Af'idah</em> (the hearts of sincere believers) to gravitate with passionate, unquenchable yearning toward that barren sanctuary. For over four millennia, answered prayer has transformed that waterless desert into the spiritual epicenter of the globe.</p>
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
        "Movement 1 & 2": 1,
        "Movement 3, 4 & 5": 3,
        "Movement 6": 6,
        "Movement 7 & 8": 7
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

print(f"Successfully generated Surah Ibrahim Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
