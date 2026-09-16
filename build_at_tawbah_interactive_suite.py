#!/usr/bin/env python3
"""
Huurs Studio - Surah At-Tawbah Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals (Omission of Basmalah, Cave of Thawr, Agony of the Three, Sacred Commerce & Prophetic Mercy)
- 11-Lecture Foundation Audio Syllabus Explorer
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AT_TAWBAH_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_at_tawbah_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_at_tawbah_html_and_md import pages_data

# 11 Audio Foundation lectures syllabus
audio_lectures = [
    ("9.At-tawbahPart1.opus", "Omission of Basmalah, Proclamation of Bara'ah & Treaty Ethics", "Movement 1", "64m"),
    ("9.At-tawbahPart2.opus", "Battle of Hunayn, Descent of Sakinah & The Cave of Thawr (Thani Ithnayn)", "Movement 2", "59m"),
    ("9.At-tawbahPart3.opus", "Call to March for Tabuk, Clinging to Earth & Mockery Rebuked", "Movement 3", "62m"),
    ("9.At-tawbahPart4.opus", "Social Dynamics of Hypocrisy, Believers as Awliya & 8 Zakah Recipients", "Movement 4", "66m"),
    ("9.At-tawbahPart5.opus", "Broken Pledges of Wealth, The Miserly Sealed & Sneering at Charity", "Movement 5", "24m"),
    ("9.At-tawbahPart6.opus", "The Subversion of Masjid ad-Dirar vs Sanctity of Masjid Quba", "Movement 5", "18m"),
    ("9.At-tawbahPart7.opus", "The Divine Commerce (Inna Allaha-shtara) & Ibrahim's Disassociation", "Movement 6", "20m"),
    ("9.At-tawbahPart8.opus", "Hardship of Tabuk, Divine Pardon & Case of the Three Left Behind", "Movement 7", "14m"),
    ("9.At-tawbahPart9.opus", "The Fifty-Day Boycott, The Constricted Earth & Divine Descent of Tawbah", "Movement 7", "21m"),
    ("9.At-tawbahPart10.opus", "Civilizational Mandate for Knowledge (Tafaqquh) & The Litmus Test", "Movement 8", "21m"),
    ("9.At-tawbahPart11.opus", "Pity & Mercy of the Prophetic Heart (Ra'oofun Raheem) & Hasbiyallah", "Movement 8", "23m")
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
  <title>Surah At-Tawbah — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
        <span>Surah At-Tawbah Master Interactive Digital Cartography Suite</span>
      </div>
      <div class="header-actions">
        <button class="btn btn-outline" onclick="openModal('omissionModal')">Omission of Basmalah</button>
        <button class="btn btn-outline" onclick="openModal('caveModal')">The Cave of Thawr</button>
        <button class="btn btn-outline" onclick="openModal('agonyModal')">Agony of the Three</button>
        <button class="btn btn-outline" onclick="openModal('purchaseModal')">The Divine Commerce</button>
        <a href="SURAH_AT_TAWBAH_MASTER_COMPENDIUM.pdf" class="btn btn-gold" target="_blank">Download PDF Compendium</a>
      </div>
    </header>

    <div class="controls-bar">
      <div class="search-input-wrap">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="liveSearchInput" placeholder="Live search across 64 cards, pillars, concepts (e.g. Tabuk, Hunayn, Ka'b, Dirar, Zakah, Sakinah)..." oninput="handleLiveSearch()">
      </div>
      <div id="statsBadge" style="font-size:0.8rem; color:var(--text-muted);">
        Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>11</b> Lectures &bull; <b>100%</b> Sunni Verified
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
        <h3>Foundation Audio Syllabus (11 Expository Lectures &bull; 06h 31m 20s)</h3>
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

  <!-- MODAL 1: Omission of the Basmalah -->
  <div class="modal-backdrop" id="omissionModal" onclick="closeOnBackdrop(event, 'omissionModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Omission of the Basmalah & The Ultimatum of Truth (Bara'ah)</h3>
        <button class="modal-close" onclick="closeModal('omissionModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "A declaration of immunity and disavowal from Allah and His Messenger to those with whom you made a treaty among the polytheists... So travel freely throughout the land for four months, but know that you cannot frustrate Allah, and that Allah will disgrace the disbelievers."
        </div>
        <h4>The Explanation of Sayyiduna Ali ibn Abi Talib</h4>
        <p>Imam al-Hakim and Ibn Kathir record that when asked why the <em>Basmalah</em> was omitted at the opening of Surah At-Tawbah, Sayyiduna Ali clarified: <em>"Because Bismillah is peace and security (Aman), while Bara'ah was revealed with the sword to terminate polytheistic treachery and demand absolute moral accounting. False peace cannot accompany a divine ultimatum."</em></p>
        <h4>The Four-Month Grace Period (Faseehoo)</h4>
        <p>Rather than launching sudden hostilities, Revelation established an unconditional four-month period of respite (*Faseehoo arba'ata ash-hur*). Polytheists were permitted to travel the Arabian peninsula in complete safety, inspect the newly unified Islamic polity, and decide their destiny without coercion.</p>
        <h4>The Inviolable Law of Asylum (Istajaraka)</h4>
        <p>Surah At-Tawbah codifies the highest ethic of wartime chivalry: Even during active confrontation, if an enemy soldier or citizen requests protection (*Istajaraka*), Muslims are commanded to shelter him immediately, allow him to hear the recited Word of Allah, and—should he choose not to accept faith—safely escort him back to his home territory of security (*Ma'manah*).</p>
      </div>
    </div>
  </div>

  <!-- MODAL 2: The Cave of Thawr -->
  <div class="modal-backdrop" id="caveModal" onclick="closeOnBackdrop(event, 'caveModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Sanctuary of the Cave (Thawr) & "Do Not Grieve"</h3>
        <button class="modal-close" onclick="closeModal('caveModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "If you do not aid the Prophet—Allah has already aided him when those who disbelieved drove him out as one of two, when they were in the cave and he said to his companion: 'Do not grieve; indeed Allah is with us.' And Allah sent down His tranquility upon him and supported him with legions you did not see..."
        </div>
        <h4>The Solitary Two: Thani Ithnayn</h4>
        <p>When believers hesitated to march for Tabuk, Revelation dismantled their sense of self-importance by recalling the Hijrah. The Prophet ﷺ does not depend upon human mobilizations. When driven out of Makkah with no army, no armor, and only a single companion—Sayyiduna Abu Bakr—Allah protected him completely in the Cave of Thawr.</p>
        <h4>The Formula of Absolute Reliance: La Tahzan</h4>
        <p>As the trackers of Quraysh stood inches above the cave mouth, Abu Bakr wept out of anguish for the Prophet's life: <em>"If one of them looks down at his feet, he will see us!"</em> The Prophet ﷺ replied with sovereign composure: <em>"O Abu Bakr, what do you think of two with whom Allah is the Third? Do not grieve; indeed Allah is with us."</em></p>
        <h4>Tranquility in the Storm (As-Sakinah)</h4>
        <p>Divine Sakinah descended upon the Prophet ﷺ not after the crisis had passed, but in the very jaws of danger. Backed by invisible angelic forces, the word of the deniers was cast into the lowest depths, while the Word of Allah proved supreme.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Agony of the Three -->
  <div class="modal-backdrop" id="agonyModal" onclick="closeOnBackdrop(event, 'agonyModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Agony of the Three & The Cosmic Constriction of Souls</h3>
        <button class="modal-close" onclick="closeModal('agonyModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "And He turned in forgiveness to the three who were left behind, until the earth was constricted for them despite its vastness and their own souls were constricted, and they became certain that there is no refuge from Allah except unto Him. Then He turned to them in mercy that they might repent..."
        </div>
        <h4>The Truthfulness of Ka'b ibn Malik</h4>
        <p>When the expedition of Tabuk returned, eighty hypocrites offered false excuses and oaths; the Prophet accepted their outward claims. But Ka'b ibn Malik, possessing wealth and health, refused to lie: <em>"I had no excuse; I was never stronger or wealthier than when I stayed behind."</em> The Prophet remarked: <em>"As for this man, he has spoken the truth."</em></p>
        <h4>The Fifty-Night Boycott: Daqat 'Alayhimul-Ard</h4>
        <p>The entire city of Madinah was commanded to sever communication with the three. For fifty nights, Ka'b walked through the markets; no one answered his greeting, and his closest kin averted their eyes. An imperial letter arrived from King Ghassan offering him sanctuary and riches; Ka'b cast it into the fire. The earth, despite its vastness, felt like an agonizing vice suffocating their chests.</p>
        <h4>The Breakthrough: Fleeing to God</h4>
        <p>In total isolation, their pride was pulverized into absolute realization: <em>Wa zannoo an la malja'a min Allahi illa ilayh</em> (There is nowhere to flee from God except returning directly to Him). Allah initiated mercy first (<em>Thumma taba 'alayhim</em>), and revelation descended at dawn clearing their names eternally.</p>
      </div>
    </div>
  </div>

  <!-- MODAL 4: The Divine Commerce -->
  <div class="modal-backdrop" id="purchaseModal" onclick="closeOnBackdrop(event, 'purchaseModal')">
    <div class="modal-window">
      <div class="modal-header">
        <h3>The Divine Commerce (Inna Allaha-shtara) & Prophetic Mercy</h3>
        <button class="modal-close" onclick="closeModal('purchaseModal')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="quote-box">
          "Indeed, Allah has purchased from the believers their lives and their wealth in exchange for Paradise... So rejoice in the transaction which you have contracted. And that is the great attainment... There has certainly come to you a Messenger from among yourselves; grievous to him is what you suffer; ardently concerned for you, and to the believers is full of pity and mercy."
        </div>
        <h4>The Cosmic Contract: Al-Mubaya'ah</h4>
        <p>Al-Hasan al-Basri noted: <em>"Consider the generosity of your Creator: He granted you life and wealth, and then purchases them back from you in exchange for eternal Paradise!"</em> This covenant is ratified across the Torah, the Gospel, and the Holy Qur'an, demanding that the believer treat his mortal faculties as assets held in trust for the divine Buyer.</p>
        <h4>The Civilizational Mandate: Tafaqquh fid-Deen</h4>
        <p>To prevent militaristic imbalance, Surah At-Tawbah establishes that not all believers may go forth to battle. A dedicated contingent must remain behind to gain deep mastery of sacred jurisprudence and revelation (*Tafaqquh*), ensuring that returning fighters find an educated, spiritually grounded society.</p>
        <h4>The Prophetic Heart & Hasbiyallah</h4>
        <p>The Surah concludes by revealing the throbbing empathy of the Prophet Muhammad ﷺ: <em>'Azeezun 'Alayhi Ma 'Anittum</em> (pained to his core by human hardship) and <em>Ra'oofun Raheem</em> (full of tender pity and mercy). And should all humanity turn away, the believer rests invulnerable within the ultimate fortress: <strong>Hasbiyallah</strong> (Allah alone suffices me; upon Him I rely, Lord of the Great Throne).</p>
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
        statsBadge.innerHTML = 'Showing <b>8</b> Plates &bull; <b>16</b> Pillars &bull; <b>64</b> Cards &bull; <b>11</b> Lectures &bull; <b>100%</b> Sunni Verified';
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

print(f"Successfully generated Surah At-Tawbah Interactive Digital Suite: {OUTPUT_HTML} ({len(full_html):,} bytes)")
