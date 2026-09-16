import os

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
MD_FILE = os.path.join(BASE_DIR, "BAQARAH_PART_09_MINDMAP.md")
HTML_FILE = os.path.join(BASE_DIR, "BAQARAH_PART_09_MINDMAP.html")

md_content = """# Surah Al-Baqarah — Master Mindmap: Part 9

**Campaign:** Deeper Thought Campaign (`Deeper_thought_campaignv01`)  
**Series:** Surah Al-Baqarah  
**Designation:** Part 9  
**Foundation Media:** `deeperthought/02_Al-Baqarah/Surah2.Al-baqarahAyats142-157.opus`  
**Layout Format:** 16:9 Landscape Vector PDF (792 x 480 pt) & Interactive HTML Canvas  
**Status:** Completed & 100% Verified  

---

## 1. Executive Cartography Overview

Part 9 inaugurates Juz 2, establishing the geopolitical, spiritual, and theological independence of the Muslim Ummah through the Qiblah redirection, the mandate of the median nation, the living reality of martyrs, and the five crucibles of adversity:

- **Page 1: The Median Nation & The Crucible of Obedience**
  - Pillar 1: The Median Nation & Qiblah Shift (*Sayaqoolus-Sufaha'*, East and West belong to Allah, *Ummatan Wasata*, *Shuhada'a 'Alan-Nas*).
  - Pillar 2: The Sift of Sincere Obedience (*Li-Na'lama Man Yattabi'ur-Rasool*, *Yanqalibu 'Ala 'Aqibayh*, *Wa Ma Kanallahu Li-Yudee'a Eemanakum*, *Raoofur-Raheem*).
- **Page 2: The Perpetual Sanctuary & The Moral Contest**
  - Pillar 3: The Sacred Sanctuary (*Taqalluba Wajhika*, *Fawalli Wajhaka Shatral-Masjidil-Haram*, threefold legal affirmation, eliminating polemical pretexts).
  - Pillar 4: Certainty, Concealment & Fastabiqul-Khayrat (*Kama Ya'rifoona Abna'ahum*, *Al-Haqqu Min Rabbika*, *Li-Kullin Wijhah*, *Fastabiqul-Khayrat*).
- **Page 3: The Prophetic Curriculum & Reciprocal Dhikr**
  - Pillar 5: The Living Prophetic Legacy (*Wa Li-Utimma Ni'matee*, *Rasoolan Minkum*, Fourfold Mission: Recitation, *Tazkiyah*, *Hikmah*, *Ma Lam Takoonoo Ta'lamoon*).
  - Pillar 6: Reciprocal Remembrance & Gratitude (*Fadhkuroonee Adhkurkum*, dimensions of Dhikr, *Washkuroo Lee*, severe prohibition of ingratitude).
- **Page 4: The Crucible of Trial, Martyrdom & Istirja'**
  - Pillar 7: Fortitude & The Living Martyrs (*Ista'eenoo Bis-Sabri Was-Salah*, divine *Ma'iyyah*, *Bal Ahya'un*, *Wa Lakin La Tash'uroon*).
  - Pillar 8: The Five Crucibles & Istirja' (*Wa Lanabluwannakum*, fear, hunger, and loss, *Wa Bashshiris-Sabireen*, *Inna Lillahi Wa Inna Ilayhi Raji'oon*, *Salawatun Min Rabbihim*).

---

## 2. Deliverables & Asset Locations

- **Vector PDF (4 Pages, 16:9 Landscape):** [`07_MINDMAP/BAQARAH_PART_09_MINDMAP.pdf`](file:///mnt/AI/ag/Campaign/07_MINDMAP/BAQARAH_PART_09_MINDMAP.pdf)
- **Interactive HTML Canvas:** [`07_MINDMAP/BAQARAH_PART_09_MINDMAP.html`](file:///mnt/AI/ag/Campaign/07_MINDMAP/BAQARAH_PART_09_MINDMAP.html)
- **Research Dossier:** [`01_RESEARCH/DEEPER-THOUGHT-RESEARCH-BAQARAH-PART-09.md`](file:///mnt/AI/ag/Campaign/01_RESEARCH/DEEPER-THOUGHT-RESEARCH-BAQARAH-PART-09.md)
- **Verification Report:** [`02_VERIFICATION/DEEPER-THOUGHT-VERIFY-BAQARAH-PART-09.md`](file:///mnt/AI/ag/Campaign/02_VERIFICATION/DEEPER-THOUGHT-VERIFY-BAQARAH-PART-09.md)
- **Page Previews:** `07_MINDMAP/previews/part09_page-1.png` through `part09_page-4.png`
"""

with open(MD_FILE, "w") as f:
    f.write(md_content)
print(f"[OK] Wrote: {MD_FILE}")

# HTML Canvas
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Baqarah — Part 9 Master Mindmap | Huurs Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-deep: #060a12;
      --bg-surface: #0b1220;
      --bg-elevated: #111a2e;
      --bg-card: rgba(17, 26, 46, 0.88);
      --gold: #d4af59;
      --gold-light: #f3dfa2;
      --gold-glow: rgba(212, 175, 89, 0.22);
      --emerald: #10b981;
      --cyan: #38bdf8;
      --purple: #a855f7;
      --rose: #f43f5e;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-card: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(212, 175, 89, 0.35);
      --shadow-lux: 0 20px 40px -15px rgba(0, 0, 0, 0.8);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-deep);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    header {
      background: rgba(6, 10, 18, 0.95);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-gold);
      padding: 12px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 50;
      flex-shrink: 0;
    }
    .header-left {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .brand-crest {
      width: 36px;
      height: 36px;
      border: 1.5px solid var(--gold);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Cinzel', serif;
      font-weight: 700;
      color: var(--gold);
      background: rgba(212, 175, 89, 0.08);
      box-shadow: 0 0 15px var(--gold-glow);
    }
    .header-title h1 {
      font-family: 'Cinzel', serif;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--gold-light);
    }
    .header-title p {
      font-size: 11px;
      color: var(--text-muted);
      letter-spacing: 0.02em;
    }

    .header-center {
      display: flex;
      gap: 6px;
      background: var(--bg-surface);
      padding: 4px;
      border-radius: 30px;
      border: 1px solid var(--border-card);
    }
    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .tab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.04);
    }
    .tab-btn.active {
      background: var(--gold);
      color: var(--bg-deep);
      box-shadow: 0 0 12px var(--gold-glow);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .badge {
      background: var(--bg-elevated);
      border: 1px solid var(--border-card);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 10px;
      font-weight: 600;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .btn-action {
      background: rgba(212, 175, 89, 0.12);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    .btn-action:hover {
      background: var(--gold);
      color: var(--bg-deep);
    }

    main {
      flex: 1;
      position: relative;
      overflow-y: auto;
      padding: 24px 30px;
    }

    .page-section {
      display: none;
      animation: fadeIn 0.3s ease-out;
      max-width: 1540px;
      margin: 0 auto;
    }
    .page-section.active {
      display: block;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .section-header {
      margin-bottom: 18px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-card);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .section-header h2 {
      font-family: 'Cinzel', serif;
      font-size: 19px;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--text-main);
    }
    .section-header p {
      font-size: 11.5px;
      color: var(--text-muted);
    }
    .meta-part {
      font-family: 'Cinzel', serif;
      font-size: 12px;
      font-weight: 700;
      color: var(--gold);
    }

    .columns-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }

    .pillar-column {
      background: var(--bg-surface);
      border-radius: 10px;
      border: 1px solid var(--border-card);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .pillar-header {
      background: var(--bg-elevated);
      padding: 12px 18px;
      border-bottom: 1px solid var(--border-card);
    }
    .pillar-header.cyan { border-top: 2.5px solid var(--cyan); }
    .pillar-header.emerald { border-top: 2.5px solid var(--emerald); }
    .pillar-header.gold { border-top: 2.5px solid var(--gold); }
    .pillar-header.purple { border-top: 2.5px solid var(--purple); }

    .pillar-title h3 {
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.04em;
    }
    .pillar-header.cyan .pillar-title h3 { color: var(--cyan); }
    .pillar-header.emerald .pillar-title h3 { color: var(--emerald); }
    .pillar-header.gold .pillar-title h3 { color: var(--gold); }
    .pillar-header.purple .pillar-title h3 { color: var(--purple); }
    .pillar-title p {
      font-size: 10px;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .pillar-cards {
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: rgba(11, 18, 32, 0.6);
    }

    .info-card {
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: 7px;
      padding: 12px 14px;
      transition: all 0.2s ease;
    }
    .info-card:hover {
      border-color: rgba(212, 175, 89, 0.4);
      transform: translateY(-1.5px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    .card-num {
      font-size: 11.5px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .card-num span {
      color: var(--gold);
    }
    .card-bullets {
      list-style: none;
    }
    .card-bullets li {
      position: relative;
      padding-left: 14px;
      font-size: 11px;
      line-height: 1.5;
      color: var(--text-muted);
      margin-bottom: 4px;
    }
    .card-bullets li:last-child {
      margin-bottom: 0;
    }
    .card-bullets li::before {
      content: "•";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 12px;
      line-height: 1;
    }

    footer {
      background: rgba(6, 10, 18, 0.95);
      backdrop-filter: blur(16px);
      border-top: 1px solid var(--border-card);
      padding: 10px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 10px;
      color: var(--text-muted);
      flex-shrink: 0;
    }
    .footer-gold {
      color: var(--gold);
      font-weight: 600;
      letter-spacing: 0.05em;
    }
  </style>
</head>
<body>

  <header>
    <div class="header-left">
      <div class="brand-crest">H</div>
      <div class="header-title">
        <h1>SURAH AL-BAQARAH &mdash; PART 9</h1>
        <p>HUURS STUDIO &bull; DEEPER THOUGHT CAMPAIGN</p>
      </div>
    </div>

    <div class="header-center">
      <button class="tab-btn active" onclick="showPage(1)">PAGE 1 &bull; MEDIAN NATION</button>
      <button class="tab-btn" onclick="showPage(2)">PAGE 2 &bull; SACRED SANCTUARY</button>
      <button class="tab-btn" onclick="showPage(3)">PAGE 3 &bull; PROPHETIC LEGACY</button>
      <button class="tab-btn" onclick="showPage(4)">PAGE 4 &bull; CRUCIBLE & RETURN</button>
    </div>

    <div class="header-right">
      <span class="badge">Part 9 Complete</span>
      <a href="BAQARAH_PART_09_MINDMAP.pdf" class="btn-action" target="_blank">PDF Version</a>
    </div>
  </header>

  <main>
    <!-- PAGE 1 -->
    <div class="page-section active" id="page1">
      <div class="section-header">
        <div>
          <h2>THE MEDIAN NATION & THE SIFT OF OBEDIENCE</h2>
          <p>Pillars 1 & 2: The Qiblah shift, Ummatan Wasatan, witness over humanity, and the trial of submission</p>
        </div>
        <div class="meta-part">PART 9 : SECTION 1</div>
      </div>

      <div class="columns-grid">
        <div class="pillar-column">
          <div class="pillar-header cyan">
            <div class="pillar-title">
              <h3>PILLAR 1: THE MEDIAN NATION & QIBLAH SHIFT</h3>
              <p>Sufaha' Polemics, Universal Sovereignty, Ummatan Wasatan & Shuhada'</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> Cynical Objections: 'Sayaqoolus-Sufaha''</div>
              <ul class="card-bullets">
                <li>Ignorant critics question the divine redirection from Jerusalem: 'What has turned them from their Qiblah?'</li>
                <li>Absolute divine sovereignty: 'To Allah belong the East and the West; He guides whom He wills to a straight path.'</li>
                <li>Sacred geography is not inherent in stone; sanctity derives purely from divine decree and obedience.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> The Median Nation: 'Ummatan Wasata'</div>
              <ul class="card-bullets">
                <li>Commissioned as an ethically balanced, just, and superlative Ummah ('adlan khiyara).</li>
                <li>Positioned as the impartial median between cultural extremes: ascetic neglect and material excess.</li>
                <li>Standing as the moral standard of justice for all mankind, anchored by prophetic testimony.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> Cosmic Witnesses: 'Li-Takoonoo Shuhada'a'</div>
              <ul class="card-bullets">
                <li>The Ummah will bear witness over previous nations on the Day of Judgment regarding prophetic delivery.</li>
                <li>The Messenger Muhammad ﷺ serves as the supreme witness confirming the Ummah's testimony.</li>
                <li>High cosmic responsibility requiring profound moral consistency and unwavering fidelity to revelation.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> The Original Axis: Divine Strategic Pedagogy</div>
              <ul class="card-bullets">
                <li>Praying toward Jerusalem in early Islam honored the prophetic lineage and softened hearts.</li>
                <li>The subsequent redirection toward Makkah cemented the independent spiritual identity of Islam.</li>
                <li>Both directions served specific developmental phases under divine pedagogical wisdom.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="pillar-column">
          <div class="pillar-header emerald">
            <div class="pillar-title">
              <h3>PILLAR 2: THE CRUCIBLE OF OBEDIENCE</h3>
              <p>The Divine Sieve, Exposing Vanity, Overcoming Custom & Preserving Faith</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> Sifting the Sincere: 'Li-Na'lama Man Yattabi'ur-Rasool'</div>
              <ul class="card-bullets">
                <li>The shift of orientation served as a deliberate divine sieve (imtihan) separating truth from counterfeit.</li>
                <li>Exposed those who blindly worshipped geographic custom versus those who submitted to the Prophet's command.</li>
                <li>True faith is surrender to the Commander, not sentimental attachment to the coordinates.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> Reversion on Heels: 'Man Yanqalibu 'Ala 'Aqibayh'</div>
              <ul class="card-bullets">
                <li>Those plagued by tribal vanity and hypocrisy turned on their heels in ideological retreat.</li>
                <li>Revealed that their adherence was conditional upon religious forms matching personal comfort.</li>
                <li>Apostasy in moments of transition unmasks underlying hypocrisy and spiritual pride.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> The Burden of Submission: 'Wa In Kanat La-Kabeerah'</div>
              <ul class="card-bullets">
                <li>Shifting direction was indeed an immense burden (kabeerah) except for those blessed with divine guidance.</li>
                <li>Overcoming lifelong habit and ancestral ties demands deep heart-level submission (khushu').</li>
                <li>Divine guidance transforms difficult mandates into sources of profound spiritual tranquility.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> Eternal Preservation: 'Wa Ma Kanallahu Li-Yudee'a Eemanakum'</div>
              <ul class="card-bullets">
                <li>Consolation to the Companions: past prayers offered toward Jerusalem remain fully credited and rewarded.</li>
                <li>'Allah would never cause your faith (Salah) to be lost' — divine justice honors every sincere prostration.</li>
                <li>'Indeed Allah is to mankind Full of Kindness, Most Merciful' (Inna Allaha bin-nasi la-raoofur-raheem).</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- PAGE 2 -->
    <div class="page-section" id="page2">
      <div class="section-header">
        <div>
          <h2>THE PERPETUAL SANCTUARY & THE MORAL CONTEST</h2>
          <p>Pillars 3 & 4: Turning toward the Ka'bah, resolving sectarian disputes, and the race for righteous deeds</p>
        </div>
        <div class="meta-part">PART 9 : SECTION 2</div>
      </div>

      <div class="columns-grid">
        <div class="pillar-column">
          <div class="pillar-header gold">
            <div class="pillar-title">
              <h3>PILLAR 3: THE SACRED SANCTUARY</h3>
              <p>Prophetic Longing, Universal Mandate, Threefold Affirmation & Stripping Pretexts</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> Prophetic Longing: 'Taqalluba Wajhika Fis-Sama''</div>
              <ul class="card-bullets">
                <li>The Prophet gazed silently into the heavens, yearning for the Abrahamic Ka'bah without demanding.</li>
                <li>Exemplary prophetic etiquette: supplicating through devotion and awaiting divine command patiently.</li>
                <li>'We have certainly seen the turning of your face toward the heaven; We will surely turn you to a Qiblah pleasing you.'</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> The Universal Decree: 'Fawalli Wajhaka Shatral-Masjidil-Haram'</div>
              <ul class="card-bullets">
                <li>Definitive mandate: 'Turn your face toward the Sacred Mosque; wherever you are, turn your faces toward it.'</li>
                <li>Unifies the global Ummah along a single concentric axis of prayer across all continents and eras.</li>
                <li>Reconnects the final revelation directly with the primeval monotheistic sanctuary built by Ibrahim.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> Threefold Affirmation: Legal & Spiritual Finality</div>
              <ul class="card-bullets">
                <li>The command is repeated three times across verses to address distinct jurisdictions and situations.</li>
                <li>First: General community law; Second: Universal application in travels; Third: Closing all debate.</li>
                <li>Pedagogical reinforcement establishing irreversible legislative and historical permanence.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> Eliminating Pretext: 'Li-Alla Yakoona Lin-Nasi 'Alaykum Hujjah'</div>
              <ul class="card-bullets">
                <li>Turning to Makkah stripped both Arab pagans and People of the Book of polemical accusations.</li>
                <li>Fulfilled ancient biblical prophecy of a prophet facing the southern sanctuary of Paran.</li>
                <li>Except the unjust who dispute obstinately; believers are commanded: 'Fear them not, but fear Me.'</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="pillar-column">
          <div class="pillar-header cyan">
            <div class="pillar-title">
              <h3>PILLAR 4: CERTAINTY, CONCEALMENT & FASTABIQUL-KHAYRAT</h3>
              <p>Intimate Recognition, Grounded Certitude, Cultural Orientations & Moral Race</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> Intimate Recognition: 'Ya'rifoonahoo Kama Ya'rifoona Abna'ahum'</div>
              <ul class="card-bullets">
                <li>Scripture scholars recognized the Prophet's characteristics as intimately as their own sons.</li>
                <li>Yet an arrogant faction deliberately concealed the truth while possessing certain knowledge.</li>
                <li>Intellectual arrogance turns objective knowledge into an instrument of personal damnation.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> The Unshakable Truth: 'Al-Haqqu Min Rabbika'</div>
              <ul class="card-bullets">
                <li>'The truth is from your Lord, so never be among the doubters (Fa-la takoonanna minal-mumtareen).'</li>
                <li>Divine revelation requires no secondary external validation; its internal coherence is absolute.</li>
                <li>Believers must remain grounded in divine certitude despite waves of social skepticism.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> Distinct Orientations: 'Li-Kullin Wijhatun Huwa Muwalleeha'</div>
              <ul class="card-bullets">
                <li>Every religious community has a focal direction and cultural orientation assigned to them.</li>
                <li>Do not become bogged down in tribal rivalry over physical directions and geographic symbols.</li>
                <li>True religion transcends ritual outwardness to embrace moral and ethical transformation.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> The Race for Excellence: 'Fastabiqul-Khayrat'</div>
              <ul class="card-bullets">
                <li>The ultimate divine imperative: 'Race one another toward good deeds (Fastabiqul-khayrat)!'</li>
                <li>Wherever you are, Allah will bring you all together on the Day of Resurrection.</li>
                <li>Shift the human competitive impulse from material hoarding to spiritual and ethical elevation.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- PAGE 3 -->
    <div class="page-section" id="page3">
      <div class="section-header">
        <div>
          <h2>THE PROPHETIC CURRICULUM & RECIPROCAL DHIKR</h2>
          <p>Pillars 5 & 6: The completed blessing, fourfold prophetic mission, and the heights of divine remembrance</p>
        </div>
        <div class="meta-part">PART 9 : SECTION 3</div>
      </div>

      <div class="columns-grid">
        <div class="pillar-column">
          <div class="pillar-header emerald">
            <div class="pillar-title">
              <h3>PILLAR 5: THE LIVING PROPHETIC LEGACY</h3>
              <p>Completed Grace, Prophetic Kinship, Fourfold Mission & Intellectual Elevation</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> Perfected Grace: 'Wa Li-Utimma Ni'matee 'Alaykum'</div>
              <ul class="card-bullets">
                <li>The Qiblah alignment completes Allah's favor upon the believers that they may be rightly guided.</li>
                <li>Spiritual sovereignty is the culmination of divine benevolence and communal dignity.</li>
                <li>Blessing is fully realized when revelation shapes both public worship and private morality.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> An Internal Messenger: 'Kama Arsalna Feekum Rasoolan Minkum'</div>
              <ul class="card-bullets">
                <li>The Prophet was sent from within themselves: sharing their humanity, language, and lived reality.</li>
                <li>An accessible, empathetic model who embodies the revelation in daily conduct and leadership.</li>
                <li>The direct answer to the ancient supplication of Ibrahim and Isma'il at the foundations of the Ka'bah.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> Fourfold Prophetic Mission: Recitation, Tazkiyah, Hikmah</div>
              <ul class="card-bullets">
                <li>1. Reciting the living signs (Yatloo 'alaykum ayatina); 2. Moral and spiritual purification (Yuzakkeekum).</li>
                <li>3. Teaching the Scripture and profound Wisdom (Yu'allimukumul-kitaba wal-hikmah).</li>
                <li>4. Imparting timeless knowledge that human intellect could never discover independently.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> Liberation from Ignorance: 'Ma Lam Takoonoo Ta'lamoon'</div>
              <ul class="card-bullets">
                <li>Prior to prophetic guidance, society languished in tribal vengeance, infanticide, and spiritual blindness.</li>
                <li>Revelation unlocked metaphysics, ethics, cosmic purpose, and eternal destiny.</li>
                <li>Knowledge of divine origins and moral accountability elevates human dignity to its zenith.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="pillar-column">
          <div class="pillar-header gold">
            <div class="pillar-title">
              <h3>PILLAR 6: RECIPROCAL REMEMBRANCE & GRATITUDE</h3>
              <p>The Divine Reciprocity, Living Mindfulness, Active Gratitude & Shielding from Kufr</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> The Supreme Reciprocity: 'Fadhkuroonee Adhkurkum'</div>
              <ul class="card-bullets">
                <li>'Remember Me; I will remember you' — the most staggering reciprocal promise in divine revelation.</li>
                <li>If a servant mentions Allah within himself, Allah mentions him in His sublime company.</li>
                <li>Continuous conscious awareness of the Creator sanctifies every mundane human endeavor.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> Manifestations of Dhikr: Tongue, Heart, and Action</div>
              <ul class="card-bullets">
                <li>Dhikr is not passive chanting: it encompasses Salah, Quranic contemplation, and righteous action.</li>
                <li>Remembering God's commands at moments of temptation preserves the soul from transgression.</li>
                <li>Living in persistent mindfulness transforms everyday existence into continuous divine worship.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> The Mandate of Gratitude: 'Washkuroo Lee'</div>
              <ul class="card-bullets">
                <li>Believers are commanded to express active gratitude: acknowledging favors through word and generous action.</li>
                <li>Gratitude (Shukr) preserves existing blessings and unlocks boundless divine abundance.</li>
                <li>True gratitude requires utilizing God's gifts in service of His truth and His creation.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> Prohibition of Ingratitude: 'Wa La Takfuroon'</div>
              <ul class="card-bullets">
                <li>Severe admonition: 'And never be ungrateful to Me (Wa la takfuroon).'</li>
                <li>Ingratitude blinds the heart to divine benevolence and breeds bitter entitlement.</li>
                <li>Recognizing our utter dependence upon God is the foundation of spiritual humility and peace.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- PAGE 4 -->
    <div class="page-section" id="page4">
      <div class="section-header">
        <div>
          <h2>THE CRUCIBLE OF TRIAL, MARTYRDOM & ISTIRJA'</h2>
          <p>Pillars 7 & 8: Patience, prayer, the reality of martyrs, five crucibles of adversity, and the divine blessing of return</p>
        </div>
        <div class="meta-part">PART 9 : SECTION 4</div>
      </div>

      <div class="columns-grid">
        <div class="pillar-column">
          <div class="pillar-header purple">
            <div class="pillar-title">
              <h3>PILLAR 7: FORTITUDE & THE LIVING MARTYRS</h3>
              <p>Patience and Prayer, Divine Companionship, The Living Dead & Veiled Perception</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> Twin Anchors of Resilience: 'Ista'eenoo Bis-Sabri Was-Salah'</div>
              <ul class="card-bullets">
                <li>'Seek assistance through patience and prayer; indeed, Allah is with the patient (Ma'as-Sabireen).'</li>
                <li>Sabr provides the psychological endurance; Salah establishes direct spiritual communion with God.</li>
                <li>Believers confront political hostility and personal grief through rooted metaphysical connection.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> Divine Companionship: 'Inna Allaha Ma'as-Sabireen'</div>
              <ul class="card-bullets">
                <li>Divine companionship (Ma'iyyah) is not passive sympathy, but active support, fortitude, and light.</li>
                <li>The patient soul never suffers in isolation; God's intimate presence sustains them through the dark.</li>
                <li>Adversity becomes the catalyst that deepens intimacy between the servant and the Lord.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> The Living Dead: 'Bal Ahya'un'</div>
              <ul class="card-bullets">
                <li>'Do not say of those slain in the path of Allah: They are dead. Nay, they are alive!'</li>
                <li>Physical demise on the battlefield is an elevation into an eternal, higher plane of consciousness.</li>
                <li>Their souls dwell in the Barzakh, sustained and rejoicing in divine bounty beyond mortal senses.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> Veiled Perception: 'Wa Lakin La Tash'uroon'</div>
              <ul class="card-bullets">
                <li>'...but you do not perceive' — mortal senses are incapable of measuring spiritual realities.</li>
                <li>What appears to worldly cynics as tragic defeat is recognized by faith as ultimate victory.</li>
                <li>Martyrdom shatters fear of death, liberating believers to stand courageously for justice.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="pillar-column">
          <div class="pillar-header cyan">
            <div class="pillar-title">
              <h3>PILLAR 8: THE FIVE CRUCIBLES & ISTIRJA'</h3>
              <p>The Inevitable Trials, Glad Tidings, Total Surrender & The Triple Crown</p>
            </div>
          </div>
          <div class="pillar-cards">
            <div class="info-card">
              <div class="card-num"><span>1.</span> Universal Curriculum: 'Wa Lanabluwannakum'</div>
              <ul class="card-bullets">
                <li>Divine decree: 'We will surely test you with something of fear, hunger, loss of wealth, lives, and fruits.'</li>
                <li>Earthly life is not a pleasure resort; it is an active educational crucible engineered for spiritual growth.</li>
                <li>Trials are distributed by divine wisdom to temper the soul, strip vanity, and uncover genuine faith.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>2.</span> Glad Tidings to the Patient: 'Wa Bashshiris-Sabireen'</div>
              <ul class="card-bullets">
                <li>The divine commission to the Prophet: announce boundless glad tidings to those who maintain constancy.</li>
                <li>The patient endure sorrow without bitterness, resentment, or despairing of divine mercy.</li>
                <li>True nobility is forged not in ease, but in steadfast devotion during the storm.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>3.</span> The Litany of Absolute Return: 'Inna Lillahi Wa Inna Ilayhi Raji'oon'</div>
              <ul class="card-bullets">
                <li>The response of the patient: 'Indeed we belong to Allah, and indeed to Him we shall return.'</li>
                <li>Absolute surrender: Recognizing that wealth, children, and our very lives are divine loans, not possessions.</li>
                <li>When the Owner reclaims His loan, the heart yields with tranquil acceptance, awaiting reunion.</li>
              </ul>
            </div>
            <div class="info-card">
              <div class="card-num"><span>4.</span> The Triple Crown: 'Salawat, Rahmah & Muhtadoon'</div>
              <ul class="card-bullets">
                <li>Believers who utter Istirja' receive three divine crowns: Blessings (Salawat), Mercy (Rahmah), and Guidance.</li>
                <li>'Ula'ika 'alayhim salawatun min rabbihim wa rahmah, wa ula'ika humul-muhtadoon.'</li>
                <li>Transformative suffering elevates the believer to the highest ranks of divine proximity and enlightenment.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer>
    <div>HUURS KNOWLEDGE SYSTEMS &bull; AUTHENTIC SUNNI SOURCE DISCIPLINE &bull; READ. REFLECT. RETURN.</div>
    <div class="footer-gold">SURAH AL-BAQARAH FOUNDATION ARCHITECTURE</div>
  </footer>

  <script>
    function showPage(pageNumber) {
      document.querySelectorAll('.page-section').forEach(sec => sec.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      
      const targetPage = document.getElementById('page' + pageNumber);
      if (targetPage) {
        targetPage.classList.add('active');
      }
      
      const buttons = document.querySelectorAll('.tab-btn');
      if (buttons[pageNumber - 1]) {
        buttons[pageNumber - 1].classList.add('active');
      }
    }
  </script>
</body>
</html>
"""

with open(HTML_FILE, "w") as f:
    f.write(html_content)
print(f"[OK] Wrote: {HTML_FILE}")
