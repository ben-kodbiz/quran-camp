#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Anfal Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals (The Trembling Heart, Divine Agency "Allah Threw", The Twin Shields, Reconciled Hearts)
- 10-Lecture Foundation Audio Syllabus Explorer
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_ANFAL_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_al_anfal_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_al_anfal_html_and_md import pages_data

# 10 Audio Foundation lectures syllabus
audio_lectures = [
    ("8.Al-anfal0introduction.opus", "Historical Context of Badr, Sovereignty of Spoils & The Trembling Heart", "Movement 1", "21m"),
    ("8.Al-anfal1.opus", "Subordination of Spoils & Reconciling Believers", "Movement 1", "20m"),
    ("8.Al-anfal2-11.opus", "Hallmarks of Faith, Reluctance for Battle & The 1,000 Angels", "Movement 1", "22m"),
    ("8.Al-anfal12-23.opus", "Angelic Assistance, Prohibition of Retreat & Divine Agency 'Allah Threw'", "Movement 2", "24m"),
    ("8.Al-anfal24-30.opus", "The Call to Life, Sovereignty Over Hearts & Plots of Makkah (Dar an-Nadwah)", "Movement 3", "22m"),
    ("8.Al-anfal31-42.opus", "Pre-Islamic Mindset, Shield of Istighfar & Division of Khumus", "Movement 4", "21m"),
    ("8.Al-anfal43-53.opus", "Topography of Badr, Prophetic Dreams, 4 Pillars of Victory & Satan's Flight", "Movement 5", "23m"),
    ("8.Al-anfal54-63.opus", "Fate of Tyrants, Changing Inward States & Defensive Deterrence", "Movement 6", "20m"),
    ("8.Al-anfal65-67.opus", "Inclination to Peace, Reconciled Hearts, Faith Ratios & The Captives", "Movement 7", "18m"),
    ("8.Al-anfal68-75.opus", "Lawful Spoils, The Pact of Wilayah & The Primacy of Blood Kin", "Movement 8", "19m")
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

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Anfal — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
  <style>
    :root {{
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
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
      line-height: 1.5;
      padding: 20px;
    }}
    .suite-shell {{
      max-width: 1480px;
      margin: 0 auto;
    }}
    header.suite-header {{
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
    }}
    .header-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .header-brand h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.05em;
    }}
    .header-brand span {{
      color: var(--text-muted);
      font-size: 0.9rem;
      border-left: 1px solid var(--border-muted);
      padding-left: 12px;
    }}
    .header-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .btn {{
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
    }}
    .btn-gold {{
      background: var(--gold);
      color: var(--navy-deep);
    }}
    .btn-gold:hover {{
      background: var(--gold-light);
    }}
    .btn-outline {{
      background: var(--navy-elevated);
      color: var(--white);
      border: 1px solid var(--border-muted);
    }}
    .btn-outline:hover {{
      border-color: var(--gold);
      color: var(--gold);
    }}
    .controls-bar {{
      display: flex;
      gap: 14px;
      margin-bottom: 20px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .search-input-wrap {{
      flex: 1;
      min-width: 260px;
      position: relative;
    }}
    .search-input-wrap input {{
      width: 100%;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 10px 16px 10px 38px;
      color: var(--white);
      font-size: 0.9rem;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input-wrap input:focus {{
      border-color: var(--gold);
    }}
    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 0.9rem;
    }}
    .nav-tabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 6px;
      margin-bottom: 20px;
    }}
    .tab-chip {{
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
    }}
    .tab-chip:hover {{
      border-color: var(--gold);
      color: var(--white);
    }}
    .tab-chip.active {{
      background: var(--navy-elevated);
      color: var(--gold);
      border-color: var(--gold);
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
    }}
    .plate-section {{
      display: none;
      margin-bottom: 30px;
    }}
    .plate-section.active {{
      display: block;
    }}
    .plate-title-bar {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 20px;
    }}
    .plate-title-bar h2 {{
      font-size: 1.15rem;
      color: var(--gold-light);
      margin-bottom: 4px;
    }}
    .plate-title-bar p {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
    .plate-badge-box {{
      display: flex;
      gap: 8px;
      align-items: center;
      flex-shrink: 0;
    }}
    .badge-gold {{
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
    }}
    .badge-emerald {{
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid var(--emerald);
      color: var(--emerald);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
    }}
    .pillars-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 980px) {{
      .pillars-layout {{
        grid-template-columns: 1fr;
      }}
    }}
    .pillar-box {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }}
    .pillar-bar {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-muted);
    }}
    .pillar-bar.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-bar.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-bar.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-bar.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-bar.rose {{ border-top: 3px solid var(--rose); }}
    .pillar-bar h3 {{
      font-size: 0.92rem;
      color: var(--white);
      margin-bottom: 2px;
    }}
    .pillar-bar p {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .cards-wrapper {{
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .card-item {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 14px;
      transition: all 0.2s;
    }}
    .card-item:hover {{
      border-color: var(--gold);
      transform: translateY(-1px);
    }}
    .card-title-row {{
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-bottom: 6px;
    }}
    .card-idx {{
      font-size: 0.7rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 1px 5px;
      border-radius: 3px;
    }}
    .card-title-row h4 {{
      font-size: 0.86rem;
      color: var(--white);
    }}
    .card-points {{
      list-style-type: none;
      padding-left: 0;
    }}
    .card-points li {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 3px;
      position: relative;
      padding-left: 12px;
    }}
    .card-points li::before {{
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 0.75rem;
    }}
    .audio-section {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 22px;
      margin-bottom: 24px;
    }}
    .audio-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 10px;
    }}
    .audio-header h3 {{
      font-size: 0.95rem;
      color: var(--gold-light);
    }}
    .audio-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 10px;
    }}
    .audio-row {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 8px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .audio-row:hover {{
      border-color: var(--gold);
      background: rgba(212, 175, 55, 0.05);
    }}
    .audio-meta-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      overflow: hidden;
    }}
    .audio-num {{
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.1);
      padding: 2px 6px;
      border-radius: 4px;
    }}
    .audio-title {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--white);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 240px;
    }}
    .audio-sub {{
      font-size: 0.7rem;
      color: var(--text-muted);
    }}
    .audio-duration {{
      font-size: 0.72rem;
      color: var(--emerald);
      font-weight: 600;
    }}
    footer.suite-footer {{
      border-top: 1px solid var(--border-muted);
      padding-top: 18px;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.8rem;
      line-height: 1.6;
    }}
    /* Modal Styles */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(4px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 999;
      padding: 20px;
    }}
    .modal-backdrop.show {{
      display: flex;
    }}
    .modal-window {{
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 8px;
      width: 100%;
      max-width: 760px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
    }}
    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-elevated);
    }}
    .modal-header h3 {{
      font-size: 1.05rem;
      color: var(--gold);
    }}
    .modal-close {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
      line-height: 1;
    }}
    .modal-close:hover {{
      color: var(--white);
    }}
    .modal-body {{
      padding: 20px;
    }}
    .modal-body h4 {{
      font-size: 0.92rem;
      color: var(--gold-light);
      margin: 14px 0 6px 0;
    }}
    .modal-body p {{
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 10px;
    }}
    .quote-box {{
      background: rgba(212, 175, 55, 0.08);
      border-left: 3px solid var(--gold);
      padding: 10px 14px;
      border-radius: 0 4px 4px 0;
      font-style: italic;
      color: var(--white);
      margin-bottom: 14px;
      font-size: 0.88rem;
    }}
  </style>
</head>
<body>
  <div class="suite-shell">
    <header class="suite-header">
      <div class="header-brand">
        <h1>HUURS STUDIO</h1>
        <span>Surah Al-Anfal Master Interactive Digital Cartography Suite</span>
      </div>
      <div class="header-actions">
        <button class="btn btn-outline" onclick="openModal('tremblingHeartModal')">The Trembling Heart</button>
        <button class="btn btn-outline" onclick="openModal('divineAgencyModal')">"Allah Threw"</button>
        <button class="btn btn-outline" onclick="openModal('twinShieldsModal')">The Twin Shields</button>
        <button class="btn btn-outline" onclick="openModal('reconciledHeartsModal')">Reconciled Hearts</button>
        <a href="SURAH_AL_ANFAL_MASTER_COMPENDIUM.pdf" class="btn btn-gold" target="_blank">Download PDF Compendium</a>
      </div>
    </header>

    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Live search across 64 cards, pillars, concepts (e.g. Badr, spoils, angels, tawakkul, istighfar)..." oninput="handleLiveSearch()">
      </div>
      <div id="statsBadge" style="font-size:0.8rem; color:var(--text-muted);">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>10</b> Lectures &bull; <b>100%</b> Sunni Verified
      </div>
    </div>

    <nav class="nav-tabs">
      {tab_buttons_html}
    </nav>

    <main>
      {plates_html}
    </main>

    <section class="audio-section">
      <div class="audio-header">
        <h3>Foundation Audio Syllabus (10 Expository Lectures &bull; 03h 30m 46s)</h3>
        <span style="font-size:0.8rem; color:var(--text-muted);">Click any lecture to explore its thematic movement</span>
      </div>
      <div class="audio-grid">
        {audio_items_html}
      </div>
    </section>

    <footer class="suite-footer">
      <p><strong>Huurs Studio</strong> &bull; Quranic Cartography & Authentic Sunni Classical Knowledge Architecture</p>
      <p>Exegetical Foundations: Imam at-Tabari, Al-Qurtubi, Ibn Kathir, Fakhr ad-Din ar-Razi, Al-Baghawi</p>
      <p>Operating Standard: Read. Reflect. Return. &bull; Strict Zero-Ayah-Number & Zero-Contemporary-Speaker Law</p>
    </footer>
  </div>

  <!-- MODAL 1: The Trembling Heart -->
  <div class="modal-backdrop" id="tremblingHeartModal" onclick="closeOnBackdrop(event, 'tremblingHeartModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Trembling Heart & Dynamic Faith (Innamal-Mu'minoon)</h3>
        <button class="modal-close" onclick="closeModal('tremblingHeartModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "The believers are only those who, when Allah is mentioned, their hearts tremble with awe, and when His verses are recited to them, it increases them in faith; and upon their Lord they rely—those who establish prayer and spend from what We have provided them. Those are the believers in truth."
        </div>
        <h4>Wajilat Qulubuhum: The Internal Tremor</h4>
        <p>Imam at-Tabari and Ibn Kathir elucidate that <em>Al-Wajal</em> is an involuntary, profound tremor of awe and solemn reverence that seizes the heart of a true believer whenever the majesty of Allah is recalled. It acts as an immediate moral restraint against transgression and an inward catalyst for humility.</p>
        <h4>Iman as a Dynamic Reality</h4>
        <p>The verse delivers foundational theological evidence for Ahl al-Sunnah: Faith (<em>Iman</em>) is not a static binary. It fluctuates—it increases dynamically (<em>Zadathum Eemana</em>) upon hearing the recited revelation, deep contemplation of divine wisdom, and righteous deeds, and decreases through neglect and disobedience.</p>
        <h4>The Foundation of Tawakkul</h4>
        <p>Before mentioning outward pillars like regular prayer (<em>Salah</em>) and charitable expenditure (<em>Infaq</em>), Revelation anchors reliance upon Allah alone (<em>'Ala Rabbihim Yatawakkaloon</em>). Outer strategic victory at Badr was born first from this inner posture of total spiritual reliance.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: Divine Agency "Allah Threw" -->
  <div class="modal-backdrop" id="divineAgencyModal" onclick="closeOnBackdrop(event, 'divineAgencyModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Metaphysics of Divine Agency: "You Did Not Throw When You Threw"</h3>
        <button class="modal-close" onclick="closeModal('divineAgencyModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And you did not kill them, but it was Allah who killed them. And you threw not, [O Muhammad], when you threw, but it was Allah who threw—that He might test the believers with a good test from Himself. Indeed, Allah is Hearing and Knowing."
        </div>
        <h4>The Physical Act and the Sovereign Effect</h4>
        <p>During the critical clash at Badr, the Messenger of Allah ﷺ scooped a handful of dust and pebbles and hurled it toward the advancing polytheist army, proclaiming: <em>Shahat al-wujuh</em> ("May these faces be confounded!"). Miraculously, the dust entered the eyes, nostrils, and mouths of every enemy combatant, breaking their momentum.</p>
        <h4>Sunni Theological Harmonization: Kasb vs Khalq</h4>
        <p>Imam Fakhr ad-Din ar-Razi explains the linguistic paradox: <em>"You threw not"</em> (negating the creation of the miraculous effect) <em>"when you threw"</em> (affirming the physical acquisition / <em>Kasb</em> of throwing) <em>"but it was Allah who threw"</em> (affirming divine creation / <em>Khalq</em> of the universal reach and impact). Human beings are obligated to take righteous action, but the ultimate causality and victory belong exclusively to Allah.</p>
        <h4>Purification from Arrogance</h4>
        <p>By stripping the victorious Companions of self-congratulatory pride, Revelation preserved the absolute spiritual purity of the Badr generation. Victory is never an entitlement of military numbers or personal prowess; it is an unmerited divine favor granted to humble servants.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: The Twin Shields -->
  <div class="modal-backdrop" id="twinShieldsModal" onclick="closeOnBackdrop(event, 'twinShieldsModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Twin Shields of Absolute Immunity (Al-Amanan)</h3>
        <button class="modal-close" onclick="closeModal('twinShieldsModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And Allah would not punish them while you, [O Muhammad], are among them, and Allah would not punish them while they seek forgiveness."
        </div>
        <h4>The Historical Insolence of Makkah</h4>
        <p>The polytheists of Makkah arrogantly challenged divine retribution, crying out: <em>"O Allah, if this is indeed the truth from You, rain down upon us stones from the sky or bring us a painful punishment!"</em> In response, Allah articulated the profound universal laws of collective immunity.</p>
        <h4>The First Shield: The Prophetic Presence</h4>
        <p>As long as the Messenger of Allah ﷺ resided physically in Makkah, collective annihilation could not strike the city, out of honor for his blessed person and mission. When the Prophet ﷺ was commanded to emigrate to Madinah, the first shield was lifted from the city of Makkah.</p>
        <h4>The Second Shield: Perpetual Istighfar</h4>
        <p>Ibn Abbas (as cited by Imam at-Tabari and Al-Qurtubi) proclaimed: <em>"There were two securities for humanity against divine wrath: the Prophet of Allah, and the seeking of forgiveness. The Prophet has departed, but Istighfar remains among you until the Day of Resurrection."</em> Sincere communal repentance shields civilizations from existential ruin.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Reconciled Hearts -->
  <div class="modal-backdrop" id="reconciledHeartsModal" onclick="closeOnBackdrop(event, 'reconciledHeartsModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Miracle of Reconciled Hearts & Strategic Cohesion</h3>
        <button class="modal-close" onclick="closeModal('reconciledHeartsModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And He brought together their hearts. If you had spent all that is in the earth, you could not have brought their hearts together; but Allah brought them together. Indeed, He is Exalted in Might and Wise."
        </div>
        <h4>The Healing of Ancient Blood Feuds</h4>
        <p>For more than a century before the Hijrah, the Arab tribes of Yathrib (the Aws and Khazraj) had been locked in brutal, generational blood feuds (such as the Battle of Bu'ath) that decimated their nobility. Human treaties, gold, and diplomacy had completely failed to heal the deep mutual enmity.</p>
        <h4>The Divine Synthesis of Ta'leef</h4>
        <p>Revelation emphasizes that unifying human hearts is beyond mortal capacity; it is a direct act of divine grace (<em>Ta'leef al-Quloob</em>). Only the transcendent bond of pure Tawhid and fraternal faith could transform lifelong mortal enemies into loving brothers who preferred one another over their own lives.</p>
        <h4>The Warning Against Tanazu' (Internal Strife)</h4>
        <p>Surah Al-Anfal explicitly links spiritual unity to military and strategic efficacy: <em>"Obey Allah and His Messenger, and do not dispute and [thus] lose courage and then your strength (Reeh) would depart; and be patient."</em> Internal factionalism destroys collective momentum and demoralizes the spirit, proving that brotherly cohesion is a military necessity.</p>
      </div>
    </div>
  </div>

  <script>
    function selectPlate(plateNum) {{
      document.querySelectorAll('.plate-section').forEach(sec => sec.classList.remove('active'));
      document.querySelectorAll('.tab-chip').forEach(tab => tab.classList.remove('active'));
      const targetSec = document.getElementById('plateSection' + plateNum);
      if (targetSec) targetSec.classList.add('active');
      const tabs = document.querySelectorAll('.tab-chip');
      if (tabs[plateNum - 1]) tabs[plateNum - 1].classList.add('active');
    }}

    function openModal(id) {{
      const modal = document.getElementById(id);
      if (modal) modal.classList.add('show');
    }}

    function closeModal(id) {{
      const modal = document.getElementById(id);
      if (modal) modal.classList.remove('show');
    }}

    function closeOnBackdrop(e, id) {{
      if (e.target.classList.contains('modal-backdrop')) {{
        closeModal(id);
      }}
    }}

    function handleLiveSearch() {{
      const query = document.getElementById('liveSearchInput').value.toLowerCase().trim();
      const plates = document.querySelectorAll('.plate-section');
      const tabs = document.querySelectorAll('.tab-chip');
      const statsBadge = document.getElementById('statsBadge');

      if (query === '') {{
        plates.forEach(p => p.classList.remove('active'));
        document.getElementById('plateSection1').classList.add('active');
        tabs.forEach(t => t.classList.remove('active'));
        tabs[0].classList.add('active');
        document.querySelectorAll('.card-item').forEach(c => c.style.display = 'block');
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>10</b> Lectures &bull; <b>100%</b> Sunni Verified';
        return;
      }}

      let matchedCount = 0;
      plates.forEach(plate => {{
        let plateHasMatch = false;
        const plateCards = plate.querySelectorAll('.card-item');
        plateCards.forEach(card => {{
          const searchData = card.getAttribute('data-search') || '';
          if (searchData.includes(query)) {{
            card.style.display = 'block';
            plateHasMatch = true;
            matchedCount++;
          }} else {{
            card.style.display = 'none';
          }}
        }});
        if (plateHasMatch) {{
          plate.classList.add('active');
        }} else {{
          plate.classList.remove('active');
        }}
      }});

      statsBadge.innerHTML = 'Found <b>' + matchedCount + ' Matches</b> for "' + query + '"';
    }}

    function filterByMovement(movName) {{
      const mapping = {{
        "Movement 1": 1,
        "Movement 2": 2,
        "Movement 3": 3,
        "Movement 4": 4,
        "Movement 5": 5,
        "Movement 6": 6,
        "Movement 7": 7,
        "Movement 8": 8
      }};
      if (mapping[movName]) {{
        selectPlate(mapping[movName]);
        window.scrollTo({{ top: 120, behavior: 'smooth' }});
      }}
    }}

    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('show'));
      }}
    }});
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated Surah Al-Anfal Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
