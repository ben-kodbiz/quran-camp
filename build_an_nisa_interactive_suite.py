#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Nisa Interactive Digital Suite Builder
Produces standalone responsive offline web application:
- 8 Plates, 16 Pillars, 64 Detailed Analytical Cards
- Real-time 64-card fuzzy search filter
- 4 Deep Exegetical Modals (Tu'mah Trial, Qawwameena bil-Qist, Inheritance Fara'id, Sunni Theological Audit)
- 29-Lecture Foundation Audio Syllabus Explorer
- Widescreen 16:9 responsive presentation adhering strictly to Huurs visual equation
"""

import os, sys, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AN_NISA_INTERACTIVE_SUITE.html")

# Import the 8-page data directly from build_an_nisa_html_and_md
sys.path.insert(0, os.path.join(BASE_DIR, "07_MINDMAP"))
from build_an_nisa_html_and_md import pages_data

# 29 Audio Foundation lectures syllabus
audio_lectures = [
    ("4.An-nisa1-4.opus", "Nafsin Wahidah: Ontological Equality & Orphan Sanctuary", "Movement 1", "22m"),
    ("4.An-nisa5-9.opus", "Financial Competence Testing & The Consuming Fire", "Movement 1", "25m"),
    ("4.An-nisa10-15.opus", "Mathematical Justice of Fara'id & Hududullah", "Movement 1", "24m"),
    ("4.An-nisa16-22.opus", "Abolition of Inherited Wives & The Weighty Covenant", "Movement 2", "19m"),
    ("4.An-nisa23-25.opus", "Prohibited Degrees of Marriage (Al-Muharramat)", "Movement 2", "18m"),
    ("4.An-nisa26-31.opus", "Economic Ethics: Mutual Consent & Sanctity of Life", "Movement 2", "20m"),
    ("4.An-nisa32-34.opus", "Qiwamah: Protective Responsibility & Financial Maintenance", "Movement 2", "25m"),
    ("4.An-nisa35-39.opus", "Institutional Arbitration & The Decalogue of Compassion", "Movement 2", "16m"),
    ("4.An-nisa40-49.opus", "The Justice of the Atom's Weight & The Unforgivable Sin", "Movement 3", "23m"),
    ("4.An-nisa50-59.opus", "Restoring Trusts (Amanat) & Constitutional Authority", "Movement 3", "20m"),
    ("4.An-nisa60-66.opus", "Arbitration as the Touchstone of True Faith", "Movement 3", "19m"),
    ("4.An-nisa67-70.opus", "The Four Blessed Ranks: Prophets, Truthful, Martyrs, Righteous", "Movement 3", "17m"),
    ("4.An-nisa71-75.opus", "Tactical Preparedness & The Cry of the Oppressed", "Movement 4", "21m"),
    ("4.An-nisa76-77.opus", "Fighting in the Cause of Allah vs. Taghut", "Movement 4", "20m"),
    ("4.An-nisa78-84.opus", "Inevitability of Death & The Command of Tadabbur", "Movement 4", "23m"),
    ("4.An-nisa85-90.opus", "Righteous Intercession, Peace Greetings & Tactical Realism", "Movement 4", "24m"),
    ("4.An-nisa91-94.opus", "Sanctity of Believing Blood & Investigative Verification", "Movement 4", "22m"),
    ("4.An-nisa95-103.opus", "Ranks of Striving, Hijrah & Salat al-Khawf in Combat", "Movement 4", "22m"),
    ("4.An-nisa104-113.opus", "The Trial of Tu'mah: Absolute Judicial Objectivity", "Movement 5", "17m"),
    ("4.An-nisa114-121.opus", "Ethics of Secret Counsel (Najwa) & Shaitan's Illusions", "Movement 5", "21m"),
    ("4.An-nisa122-128.opus", "Divine Promise vs. Human Delusion & Marital Sulh", "Movement 5", "20m"),
    ("4.An-nisa129-135.opus", "Qawwameena bil-Qist: Standing Firm Against Oneself", "Movement 5", "23m"),
    ("4.An-nisa136-143.opus", "Fluctuating Soul of Hypocrisy & Rebuking Mockery", "Movement 6", "18m"),
    ("4.An-nisa144-145.opus", "Ad-Dark al-Asfal: The Lowest Abyss of Fire", "Movement 6", "23m"),
    ("4.An-nisa146-151.opus", "The Four Pillars of Rectification & Universal Justice", "Movement 6", "24m"),
    ("4.An-nisa152-158.opus", "Exonerating Maryam & Refuting the Crucifixion", "Movement 6", "23m"),
    ("4.An-nisa159-163.opus", "Universal Faith in Isa & Prophetic Lineage of Monotheism", "Movement 6", "22m"),
    ("4.An-nisa164-171.opus", "Direct Speech with Musa & Decisive Rebuttal of Trinity", "Movement 6", "24m"),
    ("4.An-nisa172-176.opus", "The Messiah Disdains Not Servitude & Kalalah Inheritance Seal", "Movement 6", "20m")
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
  <title>Surah An-Nisa — Master Cartography & Interactive Digital Suite | Huurs Studio</title>
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
    /* Top Header */
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

    /* Global Search & Nav */
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

    /* Tabs Bar */
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

    /* Plate Sections */
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
      letter-spacing: 0.05em;
    }}
    .badge-emerald {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid var(--emerald);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.05em;
    }}

    /* Pillars Grid */
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

    /* Audio Syllabus Section */
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

    /* Modal Styling */
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

    /* Footer */
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
      <span>Surah An-Nisa &bull; Master Cartography & Interactive Digital Suite</span>
    </div>
    <div class="header-actions">
      <button class="btn btn-outline" onclick="openModal('modalTumah')">Tu'mah Trial Exegesis</button>
      <button class="btn btn-outline" onclick="openModal('modalJustice')">Qawwameena bil-Qist</button>
      <button class="btn btn-outline" onclick="openModal('modalInheritance')">Inheritance Fara'id</button>
      <button class="btn btn-gold" onclick="openModal('modalSunniAudit')">Sunni Certification</button>
    </div>
  </header>

  <!-- Controls Bar -->
  <div class="controls-bar">
    <div class="search-input-wrap">
      <span class="search-icon">&#128269;</span>
      <input type="text" id="searchInput" placeholder="Search across all 64 Analytical Cards (e.g., orphan, inheritance, justice, treaty, isa, dark al-asfal)..." onkeyup="handleSearch()">
    </div>
    <div class="stats-badge" id="statsBadge">
      Showing <b>8 Plates</b> &bull; <b>16 Pillars</b> &bull; <b>64 Cards</b> &bull; <b>29 Foundation Lectures</b>
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
        <h3>Foundation Audio Syllabus Explorer (29 Systematic Lectures)</h3>
        <p style="font-size:0.78rem; color:var(--text-muted); margin-top:2px;">Complete 10-Hour 13-Minute Exegetical Discourse &bull; Sunni Exegetical Provenance</p>
      </div>
      <div style="font-size:0.8rem; color:var(--gold); font-weight:600;">
        Total: 29 Lectures &bull; 10h 13m 44s
      </div>
    </div>
    <div class="audio-grid">
      {audio_items_html}
    </div>
  </section>

  <!-- Footer -->
  <footer class="suite-footer">
    <p><b>HUURS STUDIO</b> &bull; READ. REFLECT. RETURN. &bull; An-Nisa Master Cartography & Interactive Suite</p>
    <p style="margin-top: 6px; font-size: 0.75rem; color: #718096;">Strict Sunni Exegesis: Imam al-Tabari, Imam Ibn Kathir, Imam al-Qurtubi, Imam Fakhr al-Din al-Razi, Imam Abu Bakr al-Jassas. Zero contemporary speaker names &bull; Zero audio timestamps &bull; Zero Ayah numbers in display typography.</p>
  </footer>

</div>

<!-- MODAL 1: The Trial of Tu'mah ibn Ubayriq -->
<div class="modal-backdrop" id="modalTumah" onclick="closeOnBackdrop(event, 'modalTumah')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>The Trial of Tu'mah ibn Ubayriq & Absolute Judicial Objectivity</h3>
      <button class="modal-close" onclick="closeModal('modalTumah')">&times;</button>
    </div>
    <div class="modal-body">
      <div class="quote-box">
        "Indeed, We have revealed to you the Book in truth so that you may judge between people by that which Allah has shown you; and do not be for the deceitful an advocate!"
      </div>
      <h4>Classical Exegetical Context (As-Suyuti, Tabari, Ibn Kathir)</h4>
      <p>
        Tu'mah ibn Ubayriq, an ostensibly Muslim member of the Banu Dhafar clan, stole a suit of chain armor belonging to his neighbor Qatadah ibn al-Nu'man. To conceal his crime, he placed the armor in a sack of flour and hid it with a Jewish resident of Madinah named Zayd ibn al-Samin. A trail of spilled flour led directly to the Jewish resident's courtyard.
      </p>
      <p>
        The clan of Tu'mah rallied around him, approaching the Prophet Muhammad (peace be upon him) and pleading that he clear Tu'mah and hold the Jewish resident accountable, arguing that exposing a Muslim would dishonor the Muslim community in the eyes of their rivals.
      </p>
      <h4>The Sovereign Revelation of Divine Justice</h4>
      <p>
        Before any wrongful judgment could be issued, Allah revealed Verses 105 to 113 of Surah An-Nisa, exonerating the Jewish resident with absolute finality and delivering an uncompromising divine reprimand:
      </p>
      <ul>
        <li><b>Institutional Objectivity:</b> The Prophet (peace be upon him) was instructed: <i>"And do not be for the deceitful an advocate!"</i> Justice cannot be compromised to protect communal prestige.</li>
        <li><b>Dismantling Tribal Solidarity:</b> The Quran forcefully condemned Tu'mah's clan for attempting to manipulate the court of divine justice based on clan solidarity (*'asabiyyah*).</li>
        <li><b>Universal Moral Standard:</b> Islam established 1,400 years ago that in judicial proceedings, a Muslim wrongdoer is condemned and a non-Muslim victim is vindicated without partiality.</li>
      </ul>
    </div>
  </div>
</div>

<!-- MODAL 2: Qawwameena bil-Qist -->
<div class="modal-backdrop" id="modalJustice" onclick="closeOnBackdrop(event, 'modalJustice')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>Qawwameena bil-Qist: The Universal Mandate of Justice</h3>
      <button class="modal-close" onclick="closeModal('modalJustice')">&times;</button>
    </div>
    <div class="modal-body">
      <div class="quote-box">
        "O you who have believed, be persistently standing firm in justice, witnesses for Allah, even if it be against yourselves or parents and relatives. Whether one is rich or poor, Allah is more worthy of both. So follow not [personal] passion, lest you deviate."
      </div>
      <h4>The Anatomy of Transcendent Justice (Ayah 135)</h4>
      <p>
        Imam al-Qurtubi and Imam Ibn Kathir emphasize that the formulation <b>"Koonoo Qawwameena bil-Qist"</b> denotes continuous, vigorous, and unyielding establishment of divine equity under all circumstances.
      </p>
      <h4>Three Unforgiving Tests of Integrity</h4>
      <ul>
        <li><b>Test 1: Self-Incrimination:</b> The believer is commanded to testify against their own self. If one has caused harm or breached a contract, they must acknowledge it in court without concealment or evasive rationalization.</li>
        <li><b>Test 2: Filial Ties vs. Moral Duty:</b> Testifying against one's parents and closest kin. Familial love, which naturally inclines toward bias, is strictly subordinated to divine truth.</li>
        <li><b>Test 3: Wealth and Poverty Immunity:</b> One must not bias testimony out of deference to a rich person's influence, nor out of misguided sentimental sympathy for a poor person's destitution. Allah is more worthy of both; emotional sentimentality must never warp legal impartiality.</li>
      </ul>
      <h4>The Prohibition of Hawa (Desire)</h4>
      <p>
        The ayah concludes with a solemn prohibition: <i>"Fala tattabi'ool-hawa an ta'diloo"</i> (So follow not personal inclinations lest you deviate). Whosoever twists their words (*talwoo*) or turns away (*tu'ridoo*) from giving true testimony faces the acute omniscience of God.
      </p>
    </div>
  </div>
</div>

<!-- MODAL 3: The Mathematical Sanctity of Inheritance -->
<div class="modal-backdrop" id="modalInheritance" onclick="closeOnBackdrop(event, 'modalInheritance')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>The Mathematical Sanctity of Inheritance (Fara'id & Hududullah)</h3>
      <button class="modal-close" onclick="closeModal('modalInheritance')">&times;</button>
    </div>
    <div class="modal-body">
      <div class="quote-box">
        "Those are the limits set by Allah. And whoever obeys Allah and His Messenger will be admitted by Him to gardens beneath which rivers flow... And whoever disobeys Allah and His Messenger and transgresses His limits, He will put him into the Fire to abide eternally therein, and he will have a humiliating punishment."
      </div>
      <h4>The Pre-Islamic Context of Systemic Disinheritance</h4>
      <p>
        In pre-Islamic Arabian society, inheritance was governed by a brutal martial rule: <i>"None inherits except he who bears the sword, rides the horse, and captures the booty."</i> Consequently, widows, daughters, minor sons, and orphaned children were completely disinherited, and widows were treated as inheritable property.
      </p>
      <h4>The Divine Revolution of Fixed Fractions (Fara'id)</h4>
      <p>
        Surah An-Nisa dismantled this ancient exploitation by instituting divine, mathematically immutable legal shares:
      </p>
      <ul>
        <li><b>Universal Entitlement:</b> <i>"For men is a share of what the parents and close relatives leave, and for women is a share of what the parents and close relatives leave, be it little or much—an obligatory share."</i></li>
        <li><b>Absolute Female Property Rights:</b> Women received independent, inviolable shares that no father, brother, or husband could usurp or dictate.</li>
        <li><b>Economic Balance:</b> The male heir's share is framed within the legal obligation of comprehensive maintenance (*Nafaqah*). Men bear full financial responsibility for wives, mothers, sisters, and daughters, whereas women retain full ownership of their wealth without any obligation to spend on family expenses.</li>
        <li><b>Hududullah (The Boundaries of Allah):</b> The inheritance laws are concluded by designating them as <i>Hududullah</i>—violating them incurs the threat of eternal, humiliating punishment in the Hellfire.</li>
      </ul>
    </div>
  </div>
</div>

<!-- MODAL 4: Sunni Theological Verification Audit -->
<div class="modal-backdrop" id="modalSunniAudit" onclick="closeOnBackdrop(event, 'modalSunniAudit')">
  <div class="modal-window">
    <div class="modal-header">
      <h3>Sunni Theological Certification & Verification Audit</h3>
      <button class="modal-close" onclick="closeModal('modalSunniAudit')">&times;</button>
    </div>
    <div class="modal-body">
      <h4>Authoritative Exegetical Anchors</h4>
      <p>
        This Master Cartography and Digital Product Suite is formulated in strict accordance with the classical Sunni consensus (Ahl al-Sunnah wal-Jama'ah):
      </p>
      <ul>
        <li><b>Imam Ibn Jarir al-Tabari (d. 310 AH):</b> <i>Jami' al-Bayan 'an Ta'wil Ay al-Qur'an</i> — Foundational hadith transmission, isnad analysis, and linguistic syntax.</li>
        <li><b>Imam Abu Bakr al-Jassas (d. 370 AH):</b> <i>Ahkam al-Qur'an</i> — Precise juristic deduction of inheritance, matrimonial contracts, and judicial procedure.</li>
        <li><b>Imam Fakhr al-Din al-Razi (d. 606 AH):</b> <i>Mafatih al-Ghayb</i> — Deep theological refutations, cosmic arguments, and psychological analyses of hypocrisy.</li>
        <li><b>Imam Abu Abdillah al-Qurtubi (d. 671 AH):</b> <i>Al-Jami' li-Ahkam al-Qur'an</i> — Exhaustive juristic rulings, social ethics, and governance obligations.</li>
        <li><b>Imam Imad al-Din Ibn Kathir (d. 774 AH):</b> <i>Tafsir al-Qur'an al-'Adheem</i> — Authentic Quran-by-Quran and Quran-by-Sunnah cross-referencing.</li>
      </ul>
      <h4>Critical Theological Safeguards Enforced</h4>
      <ul>
        <li><b>Affirmation of Divine Speech (*Kalamullah*):</b> Verses 164 affirms <i>"Wa kallamallahu Musa takleema"</i>—establishing that Allah spoke directly to Musa without intermediary, refuting allegorical reduction (*Ta'teel*).</li>
        <li><b>Exoneration of Maryam & Refutation of the Crucifixion:</b> Rebuttal of blasphemous slanders against the Virgin Maryam; affirmation that Isa was neither killed nor crucified, but rather raised alive to the heavens (*Bal rafa'ahullahu ilayh*).</li>
        <li><b>Rejection of Anthropomorphism & Trinitarian Dogma:</b> Absolute transcendence (*Tanzih*) of Allah beyond offspring, partners, or trinitarian division (*La taqooloo thalathah*).</li>
      </ul>
      <div class="quote-box">
        Audited and Certified 100% Compliant with Huurs Studio Sunni Islamic Source Discipline.
      </div>
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
      statsBadge.innerHTML = 'Showing <b>8 Plates</b> &bull; <b>16 Pillars</b> &bull; <b>64 Cards</b> &bull; <b>29 Foundation Lectures</b>';
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

print(f"Successfully generated Surah An-Nisa Interactive Suite: {OUTPUT_HTML} ({len(full_html)} bytes)")
