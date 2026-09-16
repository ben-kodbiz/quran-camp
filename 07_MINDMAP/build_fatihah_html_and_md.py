import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "FATIHAH_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "FATIHAH_MASTER_MINDMAP.md")

pages_data = [
    {
        "page": 1,
        "title": "THE CELESTIAL PROLOGUE & THE ARCHITECTURE OF ABSOLUTE PRAISE",
        "desc": "Pillars 1 & 2: Hermeneutical foundations, the halved prayer dialogue, and the grammar of eternal Hamd",
        "sec": "PART 1 : SECTION 1",
        "pillars": [
            {
                "name": "PILLAR 1: HERMENEUTICAL FOUNDATIONS",
                "sub": "Umm al-Kitab, The Halved Prayer & Isti'adhah",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Umm al-Kitab: The Mother & Seed of Revelation",
                        "bullets": [
                            "Hadith (Bukhari): Designated as Umm al-Qur'an, Sab' al-Mathani, and Shifa'.",
                            "In Semitic idiom, the 'Umm' (mother) of something is its comprehensive root.",
                            "Every theme across the 113 following surahs is contained in seed form here."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Divine Dialogue: The Prayer Halved in Two",
                        "bullets": [
                            "Sahih Muslim: 'I have divided the prayer between Myself and My servant in two halves.'",
                            "Each recited verse receives an immediate, personal response from Allah.",
                            "Prayer is transformed from a human monologue into an intimate, living conversation."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Isti'adhah: Spiritual Sanctuary Before Recitation",
                        "bullets": [
                            "Commanded in An-Nahl (16:98): Clean pipes are required for clean water.",
                            "Shaytan attacks the intellect precisely when approaching divine guidance.",
                            "Seeking refuge purges cynical distraction and opens the heart to guidance."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Basmalah: The Grammar of Divine Inception",
                        "bullets": [
                            "Prepositional 'Bi': Denotes Isti'anah (seeking empowerment) and Musahabah.",
                            "The believer acts not in personal weakness, but accompanied by the Sacred Name.",
                            "Root R-H-M (the womb) establishes that divine power is cloaked in compassion."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 2: THE ARCHITECTURE OF ABSOLUTE PRAISE",
                "sub": "Al-Hamd, Nominal Permanence & Cosmic Lordship",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "Al-Hamd vs. Shukr: The Unconditional Stance",
                        "bullets": [
                            "Shukr is reactive to favors; Hamd combines intrinsic praise with gratitude.",
                            "Al-Istighraq: Definite article 'Al-' claims every conceivable praise for God.",
                            "Praise belongs to Allah even in the darkest trial, independent of personal ease."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Nominal Permanence (Jumla Ismiyyah) Over Action",
                        "bullets": [
                            "Verbal sentences ('Nahmadullah') depend on time and fallible human action.",
                            "A nominal sentence establishes an immutable, eternal, self-subsisting reality.",
                            "God's praise is unalterable: It existed before creation and endures forever."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Rabb: The Nurturing Master & Caretaker",
                        "bullets": [
                            "Root R-B-B unites Sayyid (master), Malik (owner), and Murabbi (nurturer).",
                            "A Murabbi fosters development from embryonic weakness to full perfection.",
                            "Every circumstance is part of a divine curriculum designed for the soul's growth."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Al-'Alamin: Signs Testifying in Every Realm",
                        "bullets": [
                            "Plural of 'Alam, derived from 'Alamah (a landmark, symbol, or sign).",
                            "Every sphere—physical cosmos, angelic realms, flora, fauna, human societies—",
                            "Exists as an unmistakable indicator pointing directly to its Sovereign Maker."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 2,
        "title": "THE OCEANS OF MERCY & SOVEREIGN ACCOUNTABILITY",
        "desc": "Pillars 3 & 4: The dual dynamics of compassion, dual Qira'at sovereignty, and settling the cosmic loan",
        "sec": "PART 1 : SECTION 2",
        "pillars": [
            {
                "name": "PILLAR 3: THE DUAL DYNAMICS OF COMPASSION",
                "sub": "Ar-Rahman, Ar-Rahim & Dismantling Despair",
                "color": "emerald",
                "cards": [
                    {
                        "num": "1",
                        "title": "Balancing Awe with Maternal Tenderness",
                        "bullets": [
                            "Rabbil-'Alamin invokes awe, immense power, and cosmic subjugation.",
                            "Human kings and overlords inspire paralyzing dread and alienation.",
                            "Allah immediately comforts hearts: Authority is anchored in maternal mercy."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Morphological Contrast: Fa'lan vs. Fa'eel",
                        "bullets": [
                            "Fa'lan (Ar-Rahman): Intensity, surging fullness, and overflowing immediacy.",
                            "Fa'eel (Ar-Rahim): Constancy, permanence, and unbroken continuity.",
                            "One name captures the bursting flood; the other captures the permanent ocean."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Cosmic Torrent vs. Permanent Salvific Shelter",
                        "bullets": [
                            "Ar-Rahman embraces all creation in Dunya: oxygen, water, health, and sunlight.",
                            "Ar-Rahim is the specialized, eternal mercy reserved for believers in Akhirah.",
                            "The believer lives under universal care today and rests in eternal shelter tomorrow."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Root R-H-M: The Primordial Sanctuary",
                        "bullets": [
                            "Derived from the mother's womb (Rahim), providing warmth and unconditional safety.",
                            "A child receives maternal care before earning anything or performing any service.",
                            "Divine love precedes human striving, destroying cynicism and religious self-hatred."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 4: THE DAY OF MORAL RECKONING",
                "sub": "Malik, Maalik, Yawm ad-Deen & Ultimate Justice",
                "color": "purple",
                "cards": [
                    {
                        "num": "1",
                        "title": "Dual Qira'at: Malik (King) and Maalik (Owner)",
                        "bullets": [
                            "Canonical readings: Warsh reads Malik (Sovereign); Hafs reads Maalik (Owner).",
                            "An owner possesses physical assets; a king holds judicial jurisdiction.",
                            "Allah alone synthesizes both: Absolute property ownership and supreme judicial decree."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Yawm ad-Deen: Settling the Cosmic Debt",
                        "bullets": [
                            "Root D-Y-N denotes Dayn (debt, loan, contract, binding obligation).",
                            "Life is an unearned loan of consciousness, health, wealth, and agency.",
                            "Yawm ad-Deen is the exact accounting day where every loan is audited to the penny."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Moral Bedrock: Eradicating Nihilism",
                        "bullets": [
                            "If death ends all, oppressors triumph and martyrs sacrifice in vain.",
                            "Recompense establishes an objective moral cosmos: Tyranny faces retribution.",
                            "Sincere strivings, hidden tears, and quiet integrity are recognized and redeemed."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Divine Keystone: Mercy United with Justice",
                        "bullets": [
                            "Mercy without accountability degenerates into permissive moral anarchy.",
                            "Justice without mercy crushes the human soul in unbearable legalism.",
                            "Al-Fatihah perfectly balances both: Immense mercy crowned by impartial justice."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 3,
        "title": "THE CENTRAL COVENANT & THE HIGHWAY OF GUIDANCE",
        "desc": "Pillars 5 & 6: The Iltifat pivot, exclusive devotion, and the four tiers of ascending Hidayah",
        "sec": "PART 1 : SECTION 3",
        "pillars": [
            {
                "name": "PILLAR 5: THE CHARTER OF SERVITUDE",
                "sub": "Iyyaka Na'budu, Iltifat Shift & Collective Devotion",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Rhetorical Pivot: Shift to Direct Presence",
                        "bullets": [
                            "Verses 1-4 speak of God in the 3rd person: 'All praise belongs to Him...'",
                            "Verse 5 shifts dramatically to 2nd person: 'You alone we worship!' (Iltifat).",
                            "The soul ascends from knowing about God to standing directly in His audience."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Grammatical Fronting (Hasr): Absolute Exclusivity",
                        "bullets": [
                            "Normal syntax: 'Na'buduka' (We worship You); Qur'an fronts: 'Iyyaka Na'budu'.",
                            "Fronting the object induces Hasr wal-Ikhtisas (confinement and exclusivity).",
                            "'You alone we worship, and under no circumstances do we bow to any rival!'"
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Divine Right Before Human Need: 'Ibadah First",
                        "bullets": [
                            "Worship ('Ibadah) precedes petitioning for assistance (Isti'anah).",
                            "Worship is the Creator's rightful due; assistance is the creature's need.",
                            "We honor the Master's sovereign claim before presenting our personal requests."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Collective Plural: Dismantling Spiritual Ego",
                        "bullets": [
                            "The text does not say 'I worship' (A'budu); it proclaims 'We worship' (Na'budu).",
                            "Even when praying alone at midnight, the believer dissolves the isolated ego.",
                            "Our frail prayer is wrapped inside the global communion of righteous believers."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 6: THE ANATOMY OF ULTIMATE GUIDANCE",
                "sub": "Ihdina, The Four Tiers of Hidayah & Al-Sirat",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Universal Petition: Guidance as Sole Life Need",
                        "bullets": [
                            "Standing in divine presence, the servant asks for neither wealth nor status.",
                            "The master petition is Hidayah: Divine light navigating every crossroads.",
                            "With guidance, poverty and prosperity, sickness and health lead alike to salvation."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Four Ascending Tiers of Guidance (Ibn al-Qayyim)",
                        "bullets": [
                            "1. Instinctual Guidance (creation biologies); 2. Clarification (scripture/intellect).",
                            "3. Tawfeeq (heart opening to practice truth); 4. Celestial Guidance across Sirat.",
                            "The guided believer continually asks for firmness, deeper insight, and tawfeeq."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Sirat: The Broad, Straight Highway",
                        "bullets": [
                            "Unlike winding trails (Subul) or dark alleys (Turuq), Sirat is always singular.",
                            "A wide, illuminated highway that accommodates all humanity without bottleneck.",
                            "A straight line is mathematically the shortest distance between creature and Creator."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Al-Mustaqeem: The Demands of Uprightness",
                        "bullets": [
                            "Derived from Root Q-W-M (to stand upright, unswerving, consistent).",
                            "Istiqamah requires ethical courage: Resisting ideological fashion and compromise.",
                            "The path is grounded in eternal divine truth, not shifting cultural trends."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 4,
        "title": "THE THREE DESTINIES & COSMIC RING BALANCE",
        "desc": "Pillars 7 & 8: Historical models of guidance, passive adab of wrath, and the architectural ring seed of the Qur'an",
        "sec": "PART 1 : SECTION 4",
        "pillars": [
            {
                "name": "PILLAR 7: THE THREE SPIRITUAL PATHS",
                "sub": "The Favored, The Wrath-Incurred & The Astray",
                "color": "rose",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Blessed Fellowship: Four Historical Exemplars",
                        "bullets": [
                            "Glossed in An-Nisa (4:69): Prophets, Truthful, Martyrs, and the Righteous.",
                            "Guidance is not abstract ideology; it is a paved path walked by real humans.",
                            "Walking with the righteous shields the soul from isolation and doubt."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Evoked Wrath: Passive Voice & Divine Adab",
                        "bullets": [
                            "Favor is active: 'An'amta' (You blessed); Wrath is passive: 'Al-Maghdubi 'alayhim'.",
                            "The agent of wrath is omitted: God does not act maliciously; rebellion earns wrath.",
                            "Pure goodness is ascribed to the Creator; human destruction is self-inflicted."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Bewildered Straying: Zeal Without Knowledge",
                        "bullets": [
                            "Wa lad-Dallin: Those who lose the way through emotion, dogma, and speculation.",
                            "Sincerity without sound knowledge inevitably drifts into superstition and error.",
                            "Religion is preserved by revelation and intellect, not subjective whims."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Golden Mean: Synthesis of Knowledge & Action",
                        "bullets": [
                            "Maghdub = Knowledge without Action (hypocrisy, cynicism, arrogance).",
                            "Dallin = Action without Knowledge (blind emotionalism, religious innovation).",
                            "The Straight Path synthesizes deep knowledge inseparably with righteous action."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 8: STRUCTURAL CHIASMUS & SEED OF QUR'AN",
                "sub": "Ring Composition, Cosmic Symmetry & Al-Baqarah",
                "color": "purple",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Concentric Ring Composition of Al-Fatihah",
                        "bullets": [
                            "7 Verses: 3 verses of divine praise + 1 center pivot + 3 verses of human petition.",
                            "Symmetrical chiasmus: Verse 1 mirrors 7; Verse 2 mirrors 6; Verse 3 mirrors 5.",
                            "The prayer is structurally anchored upon the central covenant of surrender."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Mirror Symmetry of Praise and Petition",
                        "bullets": [
                            "Top Half: Belongs entirely to the Master (Names, Lordship, Cosmic Mercy, Justice).",
                            "Bottom Half: Belongs entirely to the Servant (Guidance, Fellowship, Protection).",
                            "Verse 5 unites both: 'Iyyaka Na'budu' (Master's right) & 'Iyyaka Nasta'een' (servant's need)."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Microcosmic Blueprint: Seed to Expansive Tree",
                        "bullets": [
                            "Al-Fatihah is the seed; the remaining 113 surahs are the branches and fruit.",
                            "Stories of ancient nations illustrate the favored, the maghdub, and the dallin.",
                            "Legal ordinances detail the Sirat; eschatological surahs detail Yawm ad-Deen."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Seamless Handshake: The Prayer Answered",
                        "bullets": [
                            "Al-Fatihah ends with humanity's urgent cry: 'Ihdinas-Sirat al-Mustaqeem!'",
                            "Al-Baqarah instantly answers: 'Dhalikal-Kitabu la rayba feeh, hudal-lil-muttaqin.'",
                            "What the soul begs for in Al-Fatihah is placed into its hands in Al-Baqarah."
                        ]
                    }
                ]
            }
        ]
    }
]

# Generate HTML
pages_html = ""
for pg in pages_data:
    active = "active" if pg["page"] == 1 else ""
    pillars_html = ""
    for pil in pg["pillars"]:
        cards_html = ""
        for c in pil["cards"]:
            bullets_html = "".join(f"<li>{b}</li>" for b in c["bullets"])
            cards_html += f"""
          <div class="info-card">
            <div class="card-num"><span>{c["num"]}.</span> {c["title"]}</div>
            <ul class="card-bullets">
              {bullets_html}
            </ul>
          </div>"""
        pillars_html += f"""
      <div class="pillar-column">
        <div class="pillar-header {pil["color"]}">
          <div class="pillar-title">
            <h3>{pil["name"]}</h3>
            <p>{pil["sub"]}</p>
          </div>
        </div>
        <div class="pillar-cards">
          {cards_html}
        </div>
      </div>"""

    pages_html += f"""
  <!-- PAGE {pg["page"]} -->
  <div id="page{pg["page"]}" class="page-section {active}">
    <div class="section-header">
      <div>
        <h2>{pg["title"]}</h2>
        <p>{pg["desc"]}</p>
      </div>
      <div class="meta-part">{pg["sec"]}</div>
    </div>
    <div class="columns-grid">
      {pillars_html}
    </div>
  </div>"""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Fatihah — Master Mindmap | Huurs Studio</title>
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
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background-color: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    header {{
      background: var(--navy-card);
      border-bottom: 2px solid var(--gold);
      padding: 16px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand-title {{
      font-size: 16px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 1px;
    }}
    .brand-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-left: 8px;
    }}
    .nav-tabs {{
      display: flex;
      gap: 12px;
    }}
    .tab-btn {{
      background: var(--navy-elevated);
      color: var(--text-muted);
      border: 1px solid var(--border-muted);
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .tab-btn:hover {{
      color: var(--white);
      border-color: var(--gold);
    }}
    .tab-btn.active {{
      background: var(--gold);
      color: var(--navy-deep);
      border-color: var(--gold);
    }}
    main {{
      flex: 1;
      padding: 24px 32px;
      display: flex;
      flex-direction: column;
    }}
    .page-section {{
      display: none;
      flex-direction: column;
      height: 100%;
    }}
    .page-section.active {{
      display: flex;
    }}
    .section-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 12px;
    }}
    .section-header h2 {{
      font-size: 18px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.5px;
    }}
    .section-header p {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
    }}
    .meta-part {{
      font-size: 11px;
      font-weight: 700;
      color: var(--gold-light);
      background: var(--navy-elevated);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}
    .columns-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      flex: 1;
    }}
    .pillar-column {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .pillar-header {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-elevated);
    }}
    .pillar-header.gold {{ border-top: 4px solid var(--gold); }}
    .pillar-header.cyan {{ border-top: 4px solid var(--cyan); }}
    .pillar-header.purple {{ border-top: 4px solid var(--purple); }}
    .pillar-header.emerald {{ border-top: 4px solid var(--emerald); }}
    .pillar-header.rose {{ border-top: 4px solid var(--rose); }}
    .pillar-title h3 {{
      font-size: 13px;
      font-weight: 700;
      color: var(--white);
    }}
    .pillar-title p {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
    }}
    .pillar-cards {{
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex: 1;
    }}
    .info-card {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 4px;
      padding: 12px 14px;
    }}
    .card-num {{
      font-size: 12.5px;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 6px;
    }}
    .card-num span {{
      color: var(--gold);
    }}
    .card-bullets {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .card-bullets li {{
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.4;
      position: relative;
      padding-left: 14px;
    }}
    .card-bullets li::before {{
      content: "•";
      position: absolute;
      left: 2px;
      color: var(--gold);
    }}
    footer {{
      background: var(--navy-card);
      border-top: 1px solid var(--border-muted);
      padding: 12px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--text-muted);
    }}
    .footer-gold {{
      color: var(--gold);
      font-weight: 600;
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <span class="brand-title">HUURS STUDIO</span>
      <span class="brand-sub">SURAH AL-FATIHAH MASTER MINDMAP</span>
    </div>
    <div class="nav-tabs">
      <button class="tab-btn active" onclick="showPage(1)">Page 1</button>
      <button class="tab-btn" onclick="showPage(2)">Page 2</button>
      <button class="tab-btn" onclick="showPage(3)">Page 3</button>
      <button class="tab-btn" onclick="showPage(4)">Page 4</button>
    </div>
  </header>

  <main>
    {pages_html}
  </main>

  <footer>
    <div>HUURS KNOWLEDGE SYSTEMS &bull; AUTHENTIC SUNNI SOURCE DISCIPLINE &bull; READ. REFLECT. RETURN.</div>
    <div class="footer-gold">SURAH AL-FATIHAH FOUNDATION ARCHITECTURE</div>
  </footer>

  <script>
    function showPage(pageNumber) {{
      document.querySelectorAll(".page-section").forEach(sec => sec.classList.remove("active"));
      document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
      const targetPage = document.getElementById("page" + pageNumber);
      if (targetPage) targetPage.classList.add("active");
      const buttons = document.querySelectorAll(".tab-btn");
      if (buttons[pageNumber - 1]) buttons[pageNumber - 1].classList.add("active");
    }}
  </script>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"HTML generated: {HTML_OUT}")

# Generate MD
md_content = """---
id: QURAN-FATIHAH-MINDMAP-001
title: "Foundation Mindmap Cartography: Surah Al-Fatihah (The Opening)"
version: 1.0.0
author: "Huurs Knowledge Visualization Group (AGENT-06)"
source_artifact: "01_RESEARCH/DEEPER-THOUGHT-RESEARCH-FATIHAH.md"
verified_by: "Source Verification (AGENT-03) & Islamic QA (AGENT-15)"
campaign_id: "DEEPER-THOUGHT-CAMPAIGN-FATIHAH-001"
date: "2026-09-12"
status: "Published Master Mindmap Suite"
orientation: "Landscape Widescreen (16:9 / 1.65:1)"
theological_certainty: "Tier-1 (Mutawatir Qur'an & Authentic Sunni Consensus)"
derivatives:
  pdf: "07_MINDMAP/FATIHAH_MASTER_MINDMAP.pdf"
  html: "07_MINDMAP/FATIHAH_MASTER_MINDMAP.html"
  previews:
    - "07_MINDMAP/previews/fatihah_page-1.png"
    - "07_MINDMAP/previews/fatihah_page-2.png"
    - "07_MINDMAP/previews/fatihah_page-3.png"
    - "07_MINDMAP/previews/fatihah_page-4.png"
---

# Surah Al-Fatihah Master Mindmap Cartography
## The Complete 4-Page Visual Knowledge Architecture of the Opening of the Book

> **Foundation Media:** 9 Audio Lectures in `deeperthought/01_Al-Fatihah/` (Duration: 03:33:35)  
> **Core Operating Philosophy:** **READ. REFLECT. RETURN.**  
> **Format:** 4-Page Master Landscape Vector PDF (792 x 480 pt) & Interactive Widescreen Canvas  

---

## 1. Master Mindmap Architecture

Surah Al-Fatihah is systematically deconstructed across four cohesive, symmetrical landscape plates:

```text
SURAH AL-FATIHAH (03:33:35)
│
├── PAGE 1: THE CELESTIAL PROLOGUE & ABSOLUTE PRAISE
│   ├── Pillar 1: Hermeneutical Foundations (Umm al-Kitab, Halved Prayer, Isti'adhah, Basmalah)
│   └── Pillar 2: The Architecture of Absolute Praise (Hamd vs Shukr, Nominal sentence, Rabb, 'Alamin)
│
├── PAGE 2: THE OCEANS OF MERCY & SOVEREIGN RECOMPENSE
│   ├── Pillar 3: The Dual Dynamics of Compassion (Fa'lan vs Fa'eel, Cosmic vs Salvific, Root R-H-M)
│   └── Pillar 4: The Day of Moral Reckoning (Malik vs Maalik, Yawm ad-Deen debt, Eradicating nihilism)
│
├── PAGE 3: THE CENTRAL COVENANT & THE HIGHWAY OF GUIDANCE
│   ├── Pillar 5: The Charter of Servitude (Iltifat pivot, Hasr exclusivity, Right before need, Plural)
│   └── Pillar 6: The Anatomy of Ultimate Guidance (Universal petition, 4 tiers of Hidayah, Sirat, Istiqamah)
│
└── PAGE 4: THE THREE DESTINIES & COSMIC RING BALANCE
    ├── Pillar 7: The Three Spiritual Paths (Blessed fellowship [4:69], Maghdub adab, Dallin zeal)
    └── Pillar 8: Structural Chiasmus & The Seed of Revelation (Concentric ring, Seed to tree, Answering Al-Baqarah)
```

---

## 2. Deliverables Summary

* **Vector PDF:** [`07_MINDMAP/FATIHAH_MASTER_MINDMAP.pdf`](file:///mnt/AI/ag/Campaign/07_MINDMAP/FATIHAH_MASTER_MINDMAP.pdf)
* **Interactive HTML Canvas:** [`07_MINDMAP/FATIHAH_MASTER_MINDMAP.html`](file:///mnt/AI/ag/Campaign/07_MINDMAP/FATIHAH_MASTER_MINDMAP.html)
* **Research Foundation:** [`01_RESEARCH/DEEPER-THOUGHT-RESEARCH-FATIHAH.md`](file:///mnt/AI/ag/Campaign/01_RESEARCH/DEEPER-THOUGHT-RESEARCH-FATIHAH.md)
* **Verification Report:** [`02_VERIFICATION/DEEPER-THOUGHT-VERIFY-FATIHAH.md`](file:///mnt/AI/ag/Campaign/02_VERIFICATION/DEEPER-THOUGHT-VERIFY-FATIHAH.md)
"""

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"MD generated: {MD_OUT}")
