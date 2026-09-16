#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Ma'idah Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals (Completion of Deen, Sanctity of Life, Quran as Muhaymin, Isa's Trial)
- 19-Lecture Foundation Audio Syllabus Explorer
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_MAIDAH_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_al_maidah_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_al_maidah_html_and_md import pages_data

# 19 Audio Foundation lectures syllabus
audio_lectures = [
    ("5.Al-maidah1-3.opus", "Awfoo bil-'Uqud & The Completion of Deen", "Movement 1", "26m"),
    ("5.Al-maidah4-5.opus", "Wholesome Provisions (At-Tayyibat) & Trained Hunt", "Movement 1", "14m"),
    ("5.Al-maidah5-8.opus", "Structural Taharah & Objective Justice Toward Enemies", "Movement 1", "21m"),
    ("5.Al-maidah9-15.opus", "The Twelve Chieftains, Broken Pacts & Noorun Mubeen", "Movement 2", "26m"),
    ("5.Al-maidah16-26.opus", "Pathways of Peace & Cowardice Before the Holy Land", "Movement 2", "16m"),
    ("5.Al-maidah27-32.opus", "Habil and Qabil: Sincerity vs Envy & Cosmic Sanctity of Life", "Movement 2", "18m"),
    ("5.Al-maidah33-35.opus", "Deterring Chaos: The Law of Hirabah & Seeking Al-Wasilah", "Movement 3", "24m"),
    ("5.Al-maidah36-40.opus", "Futility of Ransom & Safeguarding Wealth (Sariqah)", "Movement 3", "17m"),
    ("5.Al-maidah41-42.opus", "Grief Over Disbelief, Akkaluna lis-Suht & Equitable Law", "Movement 3", "22m"),
    ("5.Al-maidah43-46.opus", "The Torah (Guidance & Light) & Retributive Justice", "Movement 4", "21m"),
    ("5.Al-maidah47-49.opus", "Injeel, The Qur'an as Muhaymin & Shir'atan wa Minhaja", "Movement 4", "20m"),
    ("5.Al-maidah50-54.opus", "Hukm al-Jahiliyyah, Compromised Pacts & The Loving Vanguard", "Movement 5", "20m"),
    ("5.Al-maidah54-63.opus", "Hallmarks of Believers, Rebuking Mockery & True Wilayah", "Movement 5", "21m"),
    ("5.Al-maidah64-68.opus", "Bal Yadahu Mabsutatani & Balligh: Absolute Conveyance", "Movement 5", "21m"),
    ("5.Al-maidah69-76.opus", "Dismantling Christological Deification & Kana Ya'kulani", "Movement 6", "22m"),
    ("5.Al-maidah77-89.opus", "The Curse of Silence on Scholars & Tears of Righteous Monks", "Movement 6", "27m"),
    ("5.Al-maidah90-97.opus", "Decisive Abolition of Khamr/Maysir & The Sanctity of Ihram", "Movement 6", "23m"),
    ("5.Al-maidah98-106.opus", "Superfluous Questions, Jahili Superstitions & Purity of Wills", "Movement 6", "24m"),
    ("5.Al-maidah107-120.opus", "The Heavenly Table, Isa's Trial (Subhanaka) & Cosmic Kingship", "Movement 6", "23m")
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
  <title>Surah Al-Ma'idah — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
    .stats-badge {{
      background: var(--navy-elevated);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.8rem;
      color: var(--text-muted);
      border: 1px solid var(--border-muted);
      white-space: nowrap;
    }}
    .stats-badge b {{
      color: var(--gold);
    }}
    .tabs-bar {{
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
      overflow-x: auto;
      padding-bottom: 6px;
    }}
    .tab-chip {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
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
      background: var(--gold);
      color: var(--navy-deep);
      border-color: var(--gold);
      font-weight: 700;
    }}
    .plate-section {{
      display: none;
      margin-bottom: 30px;
    }}
    .plate-section.active {{
      display: block;
    }}
    .plate-title-bar {{
      background: var(--navy-card);
      border-left: 4px solid var(--gold);
      padding: 16px 20px;
      border-radius: 6px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .plate-title-bar h2 {{
      font-size: 1.15rem;
      color: var(--gold-light);
      margin-bottom: 4px;
      letter-spacing: 0.03em;
    }}
    .plate-title-bar p {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .plate-badge-box {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}
    .badge-gold {{
      background: rgba(212, 175, 55, 0.15);
      color: var(--gold);
      border: 1px solid var(--gold);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
    }}
    .badge-emerald {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid var(--emerald);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
    }}
    .pillars-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 1024px) {{
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
      padding: 12px 18px;
      border-bottom: 1px solid var(--border-muted);
    }}
    .pillar-bar.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-bar.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-bar.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-bar.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-bar.rose {{ border-top: 3px solid var(--rose); }}
    .pillar-bar h3 {{
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--white);
      letter-spacing: 0.03em;
    }}
    .pillar-bar p {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 2px;
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
      padding: 12px 16px;
      transition: all 0.2s ease;
    }}
    .card-item:hover {{
      border-color: var(--gold);
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    .card-title-row {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 8px;
    }}
    .card-idx {{
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .card-item h4 {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--white);
    }}
    .card-points {{
      list-style-type: none;
      padding-left: 0;
    }}
    .card-points li {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 4px;
      position: relative;
      padding-left: 14px;
    }}
    .card-points li::before {{
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 0.8rem;
      top: -1px;
    }}
    .audio-section {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px;
      margin-top: 30px;
      margin-bottom: 40px;
    }}
    .audio-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .audio-header h3 {{
      font-size: 1.05rem;
      color: var(--gold-light);
      display: flex;
      align-items: center;
      gap: 8px;
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
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .audio-row:hover {{
      border-color: var(--cyan);
      background: rgba(56, 189, 248, 0.06);
    }}
    .audio-meta-left {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .audio-num {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 3px 6px;
      border-radius: 4px;
    }}
    .audio-title {{
      font-size: 0.83rem;
      font-weight: 600;
      color: var(--white);
    }}
    .audio-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
    }}
    .audio-duration {{
      font-size: 0.76rem;
      color: var(--gold);
      font-weight: 600;
      padding-left: 8px;
    }}
    .modal-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(4px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-backdrop.show {{
      display: flex;
    }}
    .modal-window {{
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 10px;
      max-width: 820px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      position: relative;
      animation: modalSlide 0.25s ease-out;
    }}
    @keyframes modalSlide {{
      from {{ transform: translateY(20px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}
    .modal-header {{
      background: var(--navy-elevated);
      padding: 16px 24px;
      border-bottom: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 10;
    }}
    .modal-header h3 {{
      color: var(--gold-light);
      font-size: 1.15rem;
    }}
    .modal-close {{
      background: none;
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
      padding: 24px;
      color: var(--text-muted);
      font-size: 0.9rem;
      line-height: 1.7;
    }}
    .modal-body h4 {{
      color: var(--white);
      margin-top: 16px;
      margin-bottom: 8px;
      font-size: 1.02rem;
    }}
    .modal-body p {{
      margin-bottom: 12px;
    }}
    .modal-body ul {{
      padding-left: 20px;
      margin-bottom: 14px;
    }}
    .modal-body li {{
      margin-bottom: 6px;
    }}
    .quote-box {{
      border-left: 3px solid var(--gold);
      background: var(--navy-elevated);
      padding: 12px 18px;
      border-radius: 0 6px 6px 0;
      margin: 14px 0;
      font-style: italic;
      color: var(--white);
    }}
    footer.suite-footer {{
      border-top: 1px solid var(--border-muted);
      padding: 24px 0;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.8rem;
    }}
    footer.suite-footer b {{
      color: var(--gold);
    }}
  </style>
</head>
<body>

<div class="suite-shell">

  <!-- Header -->
  <header class="suite-header">
    <div class="header-brand">
      <h1>HUURS STUDIO</h1>
      <span>Surah Al-Ma'idah &bull; Master Cartography & Interactive Digital Suite</span>
    </div>
    <div class="header-actions">
      <button class="btn btn-outline" onclick="openModal('modalIkmal')">Perfection of Deen</button>
      <button class="btn btn-outline" onclick="openModal('modalLife')">Sanctity of Life</button>
      <button class="btn btn-outline" onclick="openModal('modalMuhaymin')">Qur'an as Muhaymin</button>
      <button class="btn btn-gold" onclick="openModal('modalIsa')">Isa's Defense (Subhanaka)</button>
    </div>
  </header>

  <!-- Controls Bar -->
  <div class="controls-bar">
    <div class="search-input-wrap">
      <span class="search-icon">&#128269;</span>
      <input type="text" id="searchInput" placeholder="Search across all 64 Analytical Cards (e.g., covenant, life, habil, muhaymin, table, subhanaka, yad)..." onkeyup="handleSearch()">
    </div>
    <div class="stats-badge" id="statsBadge">
      Showing <b>8 Plates</b> &bull; <b>16 Pillars</b> &bull; <b>64 Cards</b> &bull; <b>19 Foundation Lectures</b>
    </div>
  </div>

  <!-- Plate Tab Bar -->
  <div class="tabs-bar" id="tabsBar">
    {tab_buttons_html}
  </div>

  <!-- All 8 Plates Content -->
  <main id="platesContainer">
    {plates_html}
  </main>

  <!-- Audio Foundation Syllabus Explorer -->
  <section class="audio-section" id="audioSection">
    <div class="audio-header">
      <div>
        <h3>Foundation Audio Syllabus Explorer (19 Systematic Lectures)</h3>
        <p style="font-size:0.78rem; color:var(--text-muted); margin-top:2px;">Complete 06-Hour 43-Minute Exegetical Discourse &bull; Sunni Exegetical Provenance</p>
      </div>
      <div style="font-size:0.8rem; color:var(--gold); font-weight:600;">
        Total: 19 Lectures &bull; 06h 43m 58s
      </div>
    </div>
    <div class="audio-grid">
      {audio_items_html}
    </div>
  </section>

  <!-- Footer -->
  <footer class="suite-footer">
    <p><b>HUURS STUDIO</b> &bull; READ. REFLECT. RETURN. &bull; Al-Ma'idah Master Cartography & Interactive Suite</p>
    <p style="margin-top: 6px; font-size: 0.75rem; color: #718096;">Strict Sunni Exegesis: Imam al-Tabari, Imam Ibn Kathir, Imam al-Qurtubi, Imam Fakhr al-Din al-Razi, Imam Abu Bakr al-Jassas. Zero contemporary speaker names &bull; Zero audio timestamps &bull; Zero Ayah numbers in display typography.</p>
  </footer>

</div>

<!-- MODAL 1: Perfection of Deen -->
<div class="modal-backdrop" id="modalIkmal" onclick="closeOnBackdrop(event, 'modalIkmal')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>The Perfection of Deen (Al-Yawma Akmaltu Lakum) & The Farewell Pilgrimage</h3>
      <button class="modal-close" onclick="closeModal('modalIkmal')">&times;</button>
    </div>
    <div class="modal-body">
      <div class="quote-box">
        "This day I have perfected for you your religion and completed My favor upon you and have approved for you Islam as your religion."
      </div>
      <h4>Historical Occasion & Canonical Verification</h4>
      <p>
        Revealed on the afternoon of Friday, the 9th of Dhul-Hijjah during the Farewell Pilgrimage at the Plain of Arafah (10 AH). Sahih al-Bukhari relates that a Jewish scholar remarked to Umar ibn al-Khattab: <i>"Had this verse been revealed to our people, we would have consecrated that day as an annual festival ('Eid)."</i>
      </p>
      <h4>Theological Ramifications</h4>
      <ul>
        <li><b>Closure of Normative Legislation:</b> Islam's creed, ritual worship, halal, and haram were declared structurally finished. No post-prophetic authority possesses the right to innovate or abrogate core doctrines.</li>
        <li><b>Self-Sufficiency of Revelation:</b> Humanity is liberated from relying upon man-made ethical philosophies for ultimate salvation and societal justice.</li>
        <li><b>Divine Approval (*Ridha*):</b> Islam is the sole divinely sanctioned pathway (*Deen*) pleasing to the Lord of the worlds.</li>
      </ul>
    </div>
  </div>
</div>

<!-- MODAL 2: Sanctity of Life -->
<div class="modal-backdrop" id="modalLife" onclick="closeOnBackdrop(event, 'modalLife')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>The Cosmic Sanctity of Life: Habil, Qabil & Universal Value</h3>
      <button class="modal-close" onclick="closeModal('modalLife')">&times;</button>
    </div>
    <div class="modal-body">
      <div class="quote-box">
        "Because of that, We decreed upon the Children of Israel that whoever kills a soul unless for a soul or for corruption in the land—it is as if he had slain all mankind; and whoever saves a life, it is as if he had saved all mankind."
      </div>
      <h4>The Moral Archetype of Habil's Restraint</h4>
      <p>
        When envy consumed Qabil because his brother's sacrifice was accepted while his own was rejected, Habil established the timeless ethic of principled non-violence: <i>"Even if you stretch out your hand to kill me, I shall not stretch out my hand to kill you. Indeed, I fear Allah, Lord of the worlds."</i>
      </p>
      <h4>The Equation of Universal Sanctity</h4>
      <ul>
        <li><b>Assault on the Principle of Being:</b> Killing one innocent human being is not a localized crime; it attacks the sacred right to life bestowed by the Creator, cosmically undermining the moral integrity of all human existence.</li>
        <li><b>The Radiance of Life-Saving (*Ihya'*):</b> Saving a drowning victim, treating the dying, sheltering the persecuted, or restraining murder is treated by God as if one has sustained the entirety of humanity.</li>
      </ul>
    </div>
  </div>
</div>

<!-- MODAL 3: Qur'an as Muhaymin -->
<div class="modal-backdrop" id="modalMuhaymin" onclick="closeOnBackdrop(event, 'modalMuhaymin')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>The Qur'an as Muhaymin & Diverse Dispensations (Shir'atan wa Minhaja)</h3>
      <button class="modal-close" onclick="closeModal('modalMuhaymin')">&times;</button>
    </div>
    <div class="modal-body">
      <div class="quote-box">
        "And We have revealed to you the Book in truth, confirming that which preceded it of the Scripture and as a Muhaymin (guardian, judge, and criterion) over it... To each of you We prescribed a law and a method."
      </div>
      <h4>The Meaning of Muhaymin</h4>
      <p>
        According to Ibn Abbas, Imam al-Tabari, and classical lexicographers, a <b>Muhaymin</b> is a trustworthy guardian (*Ameen*), an incorruptible witness (*Shahid*), and a supreme ruler/evaluator (*Hakim*).
      </p>
      <ul>
        <li>The Qur'an confirms the pristine original revelations given to Musa (Torah) and Isa (Injeel).</li>
        <li>It acts as the final judge that identifies, corrects, and supersedes human interpolations and sectarian deviations that arose over history.</li>
      </ul>
      <h4>Unity of Creed, Diversity of Law</h4>
      <p>
        <i>"Li-kullin ja'alna minkum shir'atan wa minhaja"</i>: All prophets taught the identical core faith of Tawhid (strict monotheism) and moral virtue. However, specific legal ordinances (*Shir'ah*) varied across historical eras according to human capacity and divine wisdom.
      </p>
      <p>
        The Quran commands humanity to channel its competitive impulses away from sectarian animosity and into moral excellence: <b>"Fastabiqul-Khayrat"</b> (So race together toward all that is good!).
      </p>
    </div>
  </div>
</div>

<!-- MODAL 4: Isa's Defense -->
<div class="modal-backdrop" id="modalIsa" onclick="closeOnBackdrop(event, 'modalIsa')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>The Eschatological Cross-Examination & Isa's Defense (Subhanaka!)</h3>
      <button class="modal-close" onclick="closeModal('modalIsa')">&times;</button>
    </div>
    <div class="modal-body">
      <div class="quote-box">
        "And when Allah will say, 'O Isa, son of Maryam, did you say to the people, 'Take me and my mother as deities besides Allah'?' He will say, 'Exalted are You! It was not for me to say that to which I have no right...'"
      </div>
      <h4>The Solemn Day of Resurrection Witness</h4>
      <p>
        In the grand climax of Surah Al-Ma'idah, Allah interrogates the Messiah before the gathered assembly of all human generations. This divine inquiry serves not to learn what Allah already knows, but to establish an irrevocable eschatological witness against trinitarian blasphemy and Christological idolatry.
      </p>
      <h4>Isa's Masterclass in Divine Propriety (*Adab*)</h4>
      <ul>
        <li><b>Immediate Glorification (*Tanzih*):</b> Isa begins with <i>"Subhanaka!"</i> (Glory and Transcendence be to You!), affirming that God is utterly beyond partners.</li>
        <li><b>Appeal to Omniscience:</b> <i>"If I had said it, You would surely have known it. You know what is within myself, and I do not know what is within Yourself. Indeed, You are the Knower of the unseen."</i></li>
        <li><b>Pristine Monotheistic Mandate:</b> <i>"I said not to them except what You commanded me: 'Worship Allah, my Lord and your Lord.'"</i></li>
      </ul>
      <h4>The Intercession Formula</h4>
      <div class="quote-box">
        "If You punish them, indeed they are Your servants; and if You forgive them, indeed You are the Exalted in Might, the Wise."
      </div>
      <p>
        The Prophet Muhammad (peace be upon him) repeated this single verse through an entire night of weeping prayer, petitioning for the forgiveness and mercy of his followers.
      </p>
    </div>
  </div>
</div>

<script>
  function selectPlate(plateNum) {{
    document.querySelectorAll('.tab-chip').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.plate-section').forEach(sec => sec.classList.remove('active'));
    
    const targetTab = document.querySelectorAll('.tab-chip')[plateNum - 1];
    const targetSec = document.getElementById('plateSection' + plateNum);
    
    if (targetTab) targetTab.classList.add('active');
    if (targetSec) targetSec.classList.add('active');
    
    window.scrollTo({{ top: 120, behavior: 'smooth' }});
  }}

  function handleSearch() {{
    const query = document.getElementById('searchInput').value.toLowerCase().trim();
    const cards = document.querySelectorAll('.card-item');
    const plates = document.querySelectorAll('.plate-section');
    const tabs = document.querySelectorAll('.tab-chip');
    const statsBadge = document.getElementById('statsBadge');

    if (query === '') {{
      plates.forEach(p => p.classList.remove('active'));
      document.getElementById('plateSection1').classList.add('active');
      tabs.forEach(t => t.classList.remove('active'));
      tabs[0].classList.add('active');
      cards.forEach(c => c.style.display = 'block');
      statsBadge.innerHTML = 'Showing <b>8 Plates</b> &bull; <b>16 Pillars</b> &bull; <b>64 Cards</b> &bull; <b>19 Foundation Lectures</b>';
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

  function filterByMovement(mov) {{
    const searchInput = document.getElementById('searchInput');
    searchInput.value = mov;
    handleSearch();
  }}

  function openModal(id) {{
    const el = document.getElementById(id);
    if (el) el.classList.add('show');
  }}

  function closeModal(id) {{
    const el = document.getElementById(id);
    if (el) el.classList.remove('show');
  }}

  function closeOnBackdrop(e, id) {{
    if (e.target.id === id) {{
      closeModal(id);
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

print(f"Successfully generated Surah Al-Ma'idah Interactive Suite: {OUTPUT_HTML} ({len(full_html)} bytes)")
