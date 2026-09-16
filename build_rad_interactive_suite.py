#!/usr/bin/env python3
"""
Huurs Studio - Surah Ar-Ra'd Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals:
    1. The Invisible Pillars & The Miracle of One Water (Bighayri 'Amad & Qita'un Mutajawirat)
    2. The Universal Sociological Law of Inner Change (Hatta Yughayyiroo Ma Bi-Anfusihim)
    3. The Sentient Thunder & The Physics of Lightning (Yusabbihu Ar-Ra'du Bi-Hamdih)
    4. The Flash Flood, Smelted Ore & The Vanishing Foam (Az-Zabadu Fayadh-habu Jufaa')
- 5-Lecture Foundation Audio Syllabus Explorer (01h 49m 36s)
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_RAD_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_rad_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_rad_html_and_md import pages_data

# 5 Audio Foundation lectures syllabus
audio_lectures = [
    ("13.Ar-rad1-6.opus", "The Invisible Pillars, Celestial Mechanics & Botanical Refutation of Materialism", "Movement 1", "22m 36s"),
    ("13.Ar-rad7-15.opus", "Resurrective Skepticism, Guardian Angels & The Sentient Thunder Hymn", "Movement 2 & 3", "17m 45s"),
    ("13.Ar-rad16-25.opus", "The Parable of the Flash Flood, Ulul-Albab Virtues & The Angelic Greeting", "Movement 4, 5 & 6", "23m 31s"),
    ("13.Ar-rad26-37.opus", "The Peace of Dhikr (Ala Bi-Dhikrillah), Tooba & Scripture Moving Mountains", "Movement 7", "24m 11s"),
    ("13.Ar-rad38-43.opus", "Historical Consolation, Erasing Decrees, Ummul-Kitab & The Sufficient Witness", "Movement 8", "21m 30s")
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
  <title>Surah Ar-Ra'd — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>Surah Ar-Ra'd • Master Cartography & Interactive Digital Suite</span>
      </div>
      <div class="header-actions">
        <a href="SURAH_RAD_MASTER_COMPENDIUM.pdf" class="btn btn-gold" download>Download Master PDF</a>
        <a href="../07_MINDMAP/RAD_MASTER_MINDMAP.html" class="btn btn-outline" target="_blank">Full Cartography View</a>
      </div>
    </header>

    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">🔍</span>
        <input type="text" id="liveSearchInput" placeholder="Search across 64 analytical cards, theological themes, Arabic terminology..." oninput="handleLiveSearch()">
      </div>
      <div class="stats-badge" id="statsBadge">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>5</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
    </div>

    <div class="modals-bar">
      <button class="btn-modal-trigger" onclick="openModal('pillarsModal')">
        <span>🌌</span> The Invisible Pillars & The Miracle of One Water
      </button>
      <button class="btn-modal-trigger" onclick="openModal('changeModal')">
        <span>🔄</span> The Universal Law of Change (Hatta Yughayyiroo)
      </button>
      <button class="btn-modal-trigger" onclick="openModal('thunderModal')">
        <span>⚡</span> The Sentient Thunder & Physics of Lightning
      </button>
      <button class="btn-modal-trigger" onclick="openModal('torrentModal')">
        <span>🌊</span> The Flash Flood, Smelted Ore & Vanishing Scum
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
        <span>5 Lectures &bull; 01h 49m 36s &bull; Click to filter corresponding plates</span>
      </div>
      <div class="audio-grid">
        {{AUDIO_ITEMS_HTML}}
      </div>
    </section>
  </div>

  <!-- MODAL 1 -->
  <div class="modal-backdrop" id="pillarsModal" onclick="closeOnBackdrop(event, 'pillarsModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Invisible Pillars of the Cosmos & The Miracle of One Water</h3>
        <button class="modal-close" onclick="closeModal('pillarsModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Allah is He who raised the heavens without pillars that you see, then established Himself above the Throne... And within the earth are neighboring plots of land, and gardens of grapevines and crops and date palms... watered with one water; yet We cause some of them to excel others in taste. Indeed in that are signs for a people who reason."
        </div>
        <h4>The Demise of Mythological & Mechanical Scaffolding</h4>
        <p>In classical Sunni scholarship, <strong>Imam Ibn Kathir</strong> and <strong>At-Tabari</strong> highlight the dual readings of <em>Bighayri 'amadin tarawnaha</em>: either the heavens are sustained by immense structural and gravitational forces imperceptible to the human eye, or they are held suspended purely by the sovereign, unassisted power of Allah without any physical pillars whatsoever. Both explanations shattered the pagan myths of the ancient world which posited physical giants, turtles, or cosmic pillars holding the sky.</p>
        <h4>The Empirical Refutation of Materialism (Dahriyyah)</h4>
        <p><strong>Imam Fakhr ad-Din ar-Razi</strong> observes in <em>Mafatih al-Ghayb</em> that verse 4 delivers a definitive, insurmountable refutation of philosophical naturalism. Consider contiguous tracts of agricultural soil (*Qita'un mutajawirat*):</p>
        <ul>
          <li>They share identical spatial coordinates, solar irradiation, and mineral chemistry.</li>
          <li>They are irrigated with identical chemical water (*Yusqa bi-ma'in wahid*).</li>
          <li>Yet from this uniform input emerges radical divergence: sweet grapes next to bitter herbs; clustered date palms (*Sinwan*) next to solitary stems (*Ghayru sinwan*).</li>
        </ul>
        <p>If nature were a blind, mechanical engine devoid of will, identical inputs would inevitably produce identical outputs. The radical differentiation in flavor, scent, form, and medicinal potency proves an intentional, choosing, and transcendent Will (*Al-Fa'il al-Mukhtar*).</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2 -->
  <div class="modal-backdrop" id="changeModal" onclick="closeOnBackdrop(event, 'changeModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Universal Sociological Law of Inner Change</h3>
        <button class="modal-close" onclick="closeModal('changeModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "For him are successive [angels] before him and behind him, guarding him by the command of Allah. Indeed, Allah will not change the condition of a people until they change what is in themselves."
        </div>
        <h4>The Directionality of Historical Change</h4>
        <p>This immortal axiom constitutes the master key of Qur'anic historical philosophy and social science. Classical commentators, including <strong>Imam al-Qurtubi</strong> and <strong>Ibn Kathir</strong>, emphasize that divine blessing, sovereignty, and security are baseline gifts. Allah never revokes worldly peace or collective dignity from a society arbitrarily. External political subjugation, economic collapse, and social fractures are the secondary consequences of an internal rupture: when a community replaces gratitude with arrogance, justice with exploitation, and sacred covenants with moral degeneration.</p>
        <h4>The Fallacy of Pure Externalism</h4>
        <p>The Qur'an rejects the secular socialist or authoritarian fallacy that reforming external political structures alone will regenerate human society. If the souls of a people remain colonized by greed, envy, cynicism, and moral rot, changing the ruler or the legal bureaucracy will merely reproduce tyranny in new forms. True civilizational resurrection must begin within: purifying intentions, restoring Tawhid, and repairing personal and communal ethics.</p>
        <h4>The Shield of Al-Mu'aqqibat</h4>
        <p>Verse 11 prefaces this sociological law by revealing the spiritual retinue: four angels shadowing every human being in alternating shifts of day and night, shielding him from stray, undecreed harms (*Yahfazoonahu min amrillah*). But when the collective threshold of corruption triggers divine decree, the angels step aside, allowing the natural harvest of their own internal choices to strike.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3 -->
  <div class="modal-backdrop" id="thunderModal" onclick="closeOnBackdrop(event, 'thunderModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Sentient Thunder & The Physics of Lightning</h3>
        <button class="modal-close" onclick="closeModal('thunderModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "It is He who shows you lightning, [causing] fear and aspiration, and generates the heavy clouds. And the thunder hymns His praise, and the angels [as well] from fear of Him; and He sends thunderbolts and strikes therewith whom He wills while they dispute concerning Allah..."
        </div>
        <h4>Cosmic Sentience Beyond Secular Sterility</h4>
        <p>Modern meteorology describes thunder as the acoustic shockwave caused by the rapid thermal expansion of air surrounding a lightning channel. While scientifically accurate on the material plane, the Qur'an unveils the metaphysical reality: <strong>atmospheric thunder is a sentient worshiper hymning the praise of its Creator (*Yusabbihu ar-ra'du bi-hamdih*)</strong>, joined by ranks of celestial angels trembling in awe (*Min kheefatih*).</p>
        <h4>The Paradox of Lightning: Khawfan wa Tama'an</h4>
        <p>Lightning evokes two diametrically opposed human emotions simultaneously:</p>
        <ul>
          <li><strong>Khawf (Dread):</strong> Fear of catastrophic wildfires, destructive strikes, and the sudden shattering of human structures.</li>
          <li><strong>Tama' (Aspiration):</strong> Intense hope for the parched farmer and arid wilderness, anticipating torrential rain that will recharge groundwater and sustain agriculture.</li>
        </ul>
        <p>This meteorological paradox mirrors the spiritual state of the believer, who lives perpetually suspended between awe-inspired vigilance (*Khawf*) of divine majesty and radiant aspiration (*Raja'*) for divine mercy.</p>
        <h4>Precision Strikes on Arrogant Disputants</h4>
        <p>The surah records that thunderbolts (*Sawa'iq*) are dispatched with surgical divine precision, striking arrogant deniers down while they insolently argue about the reality of God. In Sunni history (*Sabab an-Nuzul* recorded by At-Tabari), figures like Arbad ibn Qays or 'Amir ibn at-Tufayl plotted against the Prophet ﷺ, only to be struck down instantaneously by lightning bolts, demonstrating that Allah is <strong>Shadeed al-Mihal</strong> (severe in cosmic might).</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4 -->
  <div class="modal-backdrop" id="torrentModal" onclick="closeOnBackdrop(event, 'torrentModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Flash Flood, Smelted Ore & The Vanishing Foam</h3>
        <button class="modal-close" onclick="closeModal('torrentModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "He sends down from the sky rain, and valleys flow according to their capacity, and the torrent carries a swelling foam... As for the foam, it vanishes as [useless] scum; but as for that which benefits humanity, it remains deeply rooted in the earth."
        </div>
        <h4>The Double Parable of Water and Fire</h4>
        <p><strong>Imam Ibn al-Qayyim</strong> in <em>I'lam al-Muwaqqi'een</em> analyzes this magnificent allegory: Allah strikes two parallel parables—one hydrological (water) and one metallurgical (fire):</p>
        <ul>
          <li><strong>The Rain & The Valleys:</strong> The rain represents pure divine revelation (*Wahy*). The valleys through which it flows represent human hearts. Vast valleys absorb massive rivers of knowledge; narrow creeks hold only a trickle (*Fasalat awdiyatun bi-qadariha*).</li>
          <li><strong>The Swelling Foam (Az-Zabad):</strong> The violent torrent stirs up dirt, sticks, and bubbling froth (*Zabadan rabiya*). The foam rides high, bloated, loud, and visible, obscuring the clear water beneath. This foam represents transient doubts (*Shubuhat*) and base desires (*Shahawat*) that flare up when truth challenges a corrupted society.</li>
          <li><strong>The Smelted Ore:</strong> Metals heated in a blazing crucible produce slag that floats to the surface, appearing dominant before being discarded.</li>
        </ul>
        <h4>The Immutable Axiom: Jufaa' vs. Yamkuth</h4>
        <p>Surah Ar-Ra'd gives humanity an eternal heuristic for evaluating trends, ideologies, and historical movements:</p>
        <ul>
          <li><strong>Fa-amma az-zabadu fayadh-habu jufaa':</strong> Falsehood, vanity, corrupt fashions, and noisy propaganda are like the foam—they look enormous and loud, but they are hollow, quickly scattering into non-existence.</li>
          <li><strong>Wa amma ma yanfa'u an-nasa fayamkuthu fil-ard:</strong> That which genuinely benefits human souls—authentic faith, virtuous deeds, beneficial science, sincere charity—sinks deeply into the earth and endures across generations.</li>
        </ul>
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
        "Movement 2 & 3": 2,
        "Movement 4, 5 & 6": 4,
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

print(f"Successfully generated Surah Ar-Ra'd Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
