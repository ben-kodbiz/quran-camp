import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign"
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_FATIHAH_INTERACTIVE_SUITE.html")

pages_data = [
    {
        "plate": 1,
        "title": "THE CELESTIAL PROLOGUE & ABSOLUTE PRAISE",
        "desc": "Pillars 1 & 2: Hermeneutical foundations, the halved prayer dialogue, and the grammar of eternal Hamd",
        "sec": "PLATE 01 OF 04",
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
        "plate": 2,
        "title": "THE OCEANS OF MERCY & SOVEREIGN ACCOUNTABILITY",
        "desc": "Pillars 3 & 4: The dual dynamics of compassion, dual Qira'at sovereignty, and settling the cosmic loan",
        "sec": "PLATE 02 OF 04",
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
        "plate": 3,
        "title": "THE CENTRAL COVENANT & THE HIGHWAY OF GUIDANCE",
        "desc": "Pillars 5 & 6: The Iltifat pivot, exclusive devotion, and the four tiers of ascending Hidayah",
        "sec": "PLATE 03 OF 04",
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
        "plate": 4,
        "title": "THE THREE DESTINIES & COSMIC RING BALANCE",
        "desc": "Pillars 7 & 8: Historical models of guidance, passive adab of wrath, and the architectural ring seed of the Qur'an",
        "sec": "PLATE 04 OF 04",
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

dataset_json = json.dumps(pages_data, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Fatihah — Master Interactive Digital Compendium | Huurs Studio</title>
  <style>
    :root {{
      --navy-deep: #060a12;
      --navy-card: #0d1422;
      --navy-elevated: #141e32;
      --navy-hover: #1c2a44;
      --gold: #d4af37;
      --gold-light: #e8d194;
      --gold-glow: rgba(212, 175, 55, 0.25);
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.2);
      --purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.2);
      --emerald: #10b981;
      --rose: #f43f5e;
      --white: #f8fafc;
      --text-muted: #adc0d4;
      --border-muted: #243247;
      --border-gold: rgba(212, 175, 55, 0.4);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background-color: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    header {{
      background: var(--navy-card);
      border-bottom: 2px solid var(--gold);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      gap: 16px;
    }}

    .header-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 280px;
    }}

    .brand-crest {{
      width: 36px;
      height: 36px;
      border: 1.5px solid var(--gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.08);
      border-radius: 4px;
      box-shadow: 0 0 10px var(--gold-glow);
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .brand-name {{
      font-size: 14px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }}

    .brand-sub {{
      font-size: 11px;
      color: var(--text-muted);
      letter-spacing: 0.5px;
    }}

    .search-wrapper {{
      flex: 1;
      max-width: 480px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 20px;
      padding: 8px 16px 8px 36px;
      color: var(--white);
      font-size: 13px;
      outline: none;
      transition: all 0.2s ease;
    }}

    .search-input:focus {{
      border-color: var(--gold);
      box-shadow: 0 0 12px var(--gold-glow);
    }}

    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 13px;
      color: var(--text-muted);
      pointer-events: none;
    }}

    .search-clear {{
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 12px;
      color: var(--text-muted);
      cursor: pointer;
      display: none;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn {{
      padding: 7px 14px;
      font-size: 12px;
      font-weight: 600;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}

    .btn-gold {{
      background: linear-gradient(135deg, var(--gold), #b8972f);
      color: var(--navy-deep);
      border: none;
    }}

    .btn-gold:hover {{
      background: linear-gradient(135deg, var(--gold-light), var(--gold));
      box-shadow: 0 0 12px var(--gold-glow);
    }}

    .btn-outline {{
      background: transparent;
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
    }}

    .btn-outline:hover {{
      border-color: var(--gold);
      color: var(--white);
      background: rgba(212, 175, 55, 0.08);
    }}

    .btn-showcase-1 {{
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid var(--cyan);
      color: var(--cyan);
    }}

    .btn-showcase-1:hover {{
      background: var(--cyan);
      color: var(--navy-deep);
      box-shadow: 0 0 12px var(--cyan-glow);
    }}

    .btn-showcase-2 {{
      background: rgba(168, 85, 247, 0.12);
      border: 1px solid var(--purple);
      color: var(--purple);
    }}

    .btn-showcase-2:hover {{
      background: var(--purple);
      color: var(--navy-deep);
      box-shadow: 0 0 12px var(--purple-glow);
    }}

    .app-container {{
      display: flex;
      flex: 1;
      height: calc(100vh - 62px);
      overflow: hidden;
    }}

    .sidebar {{
      width: 320px;
      background: var(--navy-card);
      border-right: 1px solid var(--border-muted);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      overflow-y: auto;
    }}

    .sidebar-header {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-deep);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sidebar-title {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      color: var(--gold);
      text-transform: uppercase;
    }}

    .sidebar-badge {{
      font-size: 10px;
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      padding: 2px 6px;
      border-radius: 3px;
      font-weight: 600;
    }}

    .plate-nav-list {{
      padding: 10px 8px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .plate-nav-item {{
      padding: 12px 14px;
      border-radius: 6px;
      cursor: pointer;
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      display: flex;
      flex-direction: column;
      gap: 3px;
      transition: all 0.15s ease;
    }}

    .plate-nav-item:hover {{
      border-color: var(--gold);
      background: var(--navy-hover);
    }}

    .plate-nav-item.active {{
      border-color: var(--gold);
      box-shadow: inset 3px 0 0 var(--gold);
      background: rgba(212, 175, 55, 0.08);
    }}

    .plate-nav-num {{
      font-size: 10.5px;
      font-weight: 700;
      color: var(--gold);
    }}

    .plate-nav-title {{
      font-size: 12px;
      font-weight: 600;
      color: var(--white);
      line-height: 1.3;
    }}

    .sidebar-section-title {{
      padding: 12px 16px 4px 16px;
      font-size: 10px;
      font-weight: 700;
      color: var(--gold-light);
      letter-spacing: 1px;
      text-transform: uppercase;
    }}

    .audio-breakdown-list {{
      padding: 4px 12px 16px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      font-size: 11px;
      color: var(--text-muted);
    }}

    .audio-file-item {{
      padding: 6px 8px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-muted);
      border-radius: 4px;
      display: flex;
      justify-content: space-between;
    }}

    .audio-file-item span.title {{
      color: var(--white);
      font-weight: 500;
    }}

    .main-viewport {{
      flex: 1;
      overflow-y: auto;
      background: var(--navy-deep);
      padding: 20px 28px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .plate-banner {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      overflow: hidden;
    }}

    .plate-banner::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--gold);
    }}

    .banner-meta {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 4px;
    }}

    .badge-plate {{
      font-size: 11px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 1px;
    }}

    .badge-tag {{
      font-size: 10px;
      color: var(--text-muted);
      background: var(--navy-elevated);
      padding: 2px 8px;
      border-radius: 3px;
      border: 1px solid var(--border-muted);
    }}

    .banner-title {{
      font-size: 20px;
      font-weight: 700;
      color: var(--white);
      letter-spacing: 0.5px;
    }}

    .banner-anchors {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    .banner-anchors span {{
      color: var(--gold-light);
      font-weight: 600;
    }}

    .plate-nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 8px 14px;
    }}

    .tabs-group {{
      display: flex;
      gap: 8px;
    }}

    .tab-btn {{
      padding: 8px 18px;
      font-size: 12px;
      font-weight: 600;
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .tab-btn:hover {{
      color: var(--white);
      border-color: var(--gold);
    }}

    .tab-btn.active {{
      background: rgba(212, 175, 55, 0.12);
      border-color: var(--gold);
      color: var(--gold);
      box-shadow: 0 0 10px var(--gold-glow);
    }}

    .toggle-btn {{
      font-size: 11.5px;
      color: var(--text-muted);
      background: transparent;
      border: 1px solid var(--border-muted);
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .toggle-btn:hover, .toggle-btn.active {{
      background: var(--navy-elevated);
      color: var(--white);
      border-color: var(--text-muted);
    }}

    .page-display {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .page-card {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .page-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 12px;
    }}

    .page-heading h3 {{
      font-size: 15px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .page-heading p {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .page-sec-badge {{
      font-size: 10.5px;
      font-weight: 700;
      color: var(--gold-light);
      background: var(--navy-elevated);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}

    .pillars-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}

    @media (max-width: 1024px) {{
      .pillars-container {{ grid-template-columns: 1fr; }}
    }}

    .pillar-box {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .pillar-header {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-muted);
      background: rgba(255, 255, 255, 0.02);
    }}

    .pillar-header.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-header.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-header.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-header.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-header.rose {{ border-top: 3px solid var(--rose); }}

    .pillar-title {{
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .pillar-header.gold .pillar-title {{ color: var(--gold); }}
    .pillar-header.cyan .pillar-title {{ color: var(--cyan); }}
    .pillar-header.purple .pillar-title {{ color: var(--purple); }}
    .pillar-header.emerald .pillar-title {{ color: var(--emerald); }}
    .pillar-header.rose .pillar-title {{ color: var(--rose); }}

    .pillar-sub {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .cards-stack {{
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .card-item {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 5px;
      padding: 10px 14px;
      transition: all 0.2s ease;
    }}

    .card-item:hover {{
      border-color: var(--border-gold);
      transform: translateY(-1px);
    }}

    .card-item.highlight-pulse {{
      animation: pulseHighlight 2s ease infinite;
    }}

    @keyframes pulseHighlight {{
      0% {{ border-color: var(--gold); box-shadow: 0 0 5px var(--gold-glow); }}
      50% {{ border-color: var(--cyan); box-shadow: 0 0 15px var(--cyan-glow); }}
      100% {{ border-color: var(--gold); box-shadow: 0 0 5px var(--gold-glow); }}
    }}

    .card-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 6px;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }}

    .card-title span.num {{
      color: var(--gold);
      font-size: 11.5px;
    }}

    .card-bullets {{
      list-style-type: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .card-bullets li {{
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.45;
      position: relative;
      padding-left: 14px;
    }}

    .card-bullets li::before {{
      content: "•";
      position: absolute;
      left: 2px;
      color: var(--gold);
      font-size: 12px;
    }}

    .search-results-panel {{
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      margin-top: 6px;
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 8px;
      max-height: 400px;
      overflow-y: auto;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.7);
      z-index: 2000;
      display: none;
    }}

    .search-results-panel.open {{ display: block; }}

    .search-meta-bar {{
      padding: 8px 14px;
      font-size: 11px;
      font-weight: 700;
      color: var(--gold);
      background: var(--navy-elevated);
      border-bottom: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
    }}

    .search-item {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-muted);
      cursor: pointer;
      transition: background 0.15s ease;
    }}

    .search-item:hover {{ background: var(--navy-hover); }}

    .search-item-header {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 2px;
    }}

    .search-item-location {{
      font-size: 9.5px;
      color: var(--cyan);
      margin-bottom: 4px;
      text-transform: uppercase;
    }}

    .search-item-snippet {{
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.35;
    }}

    .highlight-term {{
      background: rgba(212, 175, 55, 0.35);
      color: var(--white);
      padding: 0 2px;
      border-radius: 2px;
      font-weight: 600;
    }}

    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(6px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 3000;
      padding: 20px;
    }}

    .modal-backdrop.open {{ display: flex; }}

    .modal-content {{
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 10px;
      max-width: 860px;
      width: 100%;
      max-height: 88vh;
      overflow-y: auto;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8);
      display: flex;
      flex-direction: column;
    }}

    .modal-header {{
      padding: 16px 24px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-elevated);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.5px;
    }}

    .modal-close {{
      background: transparent;
      border: none;
      font-size: 20px;
      color: var(--text-muted);
      cursor: pointer;
    }}

    .modal-close:hover {{ color: var(--white); }}

    .modal-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      font-size: 13px;
      line-height: 1.6;
      color: var(--text-muted);
    }}

    .modal-body h4 {{
      font-size: 14px;
      color: var(--white);
      border-left: 3px solid var(--gold);
      padding-left: 8px;
      margin-bottom: 6px;
    }}

    .modal-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}

    .modal-card {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 14px;
    }}

    .modal-card-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 6px;
    }}

    footer {{
      background: var(--navy-card);
      border-top: 1px solid var(--border-muted);
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--text-muted);
    }}

    .footer-gold {{ color: var(--gold); font-weight: 600; }}
  </style>
</head>
<body>

  <header>
    <div class="header-brand">
      <div class="brand-crest">H</div>
      <div class="brand-text">
        <div class="brand-name">Huurs Studio</div>
        <div class="brand-sub">Deeper Thought Campaign &bull; Read. Reflect. Return.</div>
      </div>
    </div>

    <div class="search-wrapper">
      <span class="search-icon">🔍</span>
      <input type="text" id="globalSearch" class="search-input" placeholder="Search across all 32 conceptual cards & 8 pillars..." autocomplete="off">
      <span id="searchClear" class="search-clear">✕</span>
      <div id="searchResults" class="search-results-panel"></div>
    </div>

    <div class="header-actions">
      <button class="btn btn-showcase-1" onclick="openModal('modalDialogue')">👑 Divine Dialogue</button>
      <button class="btn btn-showcase-2" onclick="openModal('modalRing')">🛡️ Ring Composition</button>
      <button class="btn btn-outline" onclick="openModal('modalAudit')">📜 Sunni Audit</button>
      <a href="./SURAH_AL_FATIHAH_MASTER_COMPENDIUM.pdf" target="_blank" class="btn btn-gold">📥 Master PDF (6 Plates)</a>
    </div>
  </header>

  <div class="app-container">
    <aside class="sidebar">
      <div class="sidebar-header">
        <span class="sidebar-title">Surah Al-Fatihah</span>
        <span class="sidebar-badge">4 Content Plates</span>
      </div>

      <div class="plate-nav-list" id="plateNavList">
        <!-- Injected via JS -->
      </div>

      <div class="sidebar-section-title">Foundation Audio Corpus</div>
      <div class="audio-breakdown-list">
        <div class="audio-file-item">
          <span class="title">1. Introduction & Basmalah</span>
          <span>01h 25m</span>
        </div>
        <div class="audio-file-item">
          <span class="title">2. Al-Hamd & Lordship</span>
          <span>28m 12s</span>
        </div>
        <div class="audio-file-item">
          <span class="title">3. Ar-Rahman & Ar-Rahim</span>
          <span>09m 04s</span>
        </div>
        <div class="audio-file-item">
          <span class="title">4. Yawm ad-Deen Justice</span>
          <span>24m 08s</span>
        </div>
        <div class="audio-file-item">
          <span class="title">5. Iyyaka Na'budu Covenant</span>
          <span>20m 55s</span>
        </div>
        <div class="audio-file-item">
          <span class="title">6. Ihdinas-Sirat Guidance</span>
          <span>17m 29s</span>
        </div>
        <div class="audio-file-item">
          <span class="title">7. The Three Trajectories</span>
          <span>25m 28s</span>
        </div>
        <div class="audio-file-item">
          <span class="title">8. Balance & Observations</span>
          <span>16m 46s</span>
        </div>
        <div class="audio-file-item">
          <span class="title">9. Synthesis & Outro</span>
          <span>02m 28s</span>
        </div>
      </div>
    </aside>

    <main class="main-viewport" id="mainViewport">
      <section class="plate-banner" id="plateBanner">
        <div>
          <div class="banner-meta">
            <span class="badge-plate" id="bannerPlateBadge">PLATE 01 OF 04</span>
            <span class="badge-tag">UMM AL-KITAB</span>
            <span class="badge-tag">MUTAWATIR</span>
          </div>
          <h1 class="banner-title" id="bannerTitle">Plate Title</h1>
          <div class="banner-anchors">
            Classical Exegetical Anchors: <span>Tafsir Ibn Kathir &bull; Jami' al-Bayan (Al-Tabari) &bull; Al-Jami' li-Ahkam al-Qur'an (Al-Qurtubi) &bull; Mafatih al-Ghayb (Al-Razi)</span>
          </div>
        </div>
        <div>
          <a href="../07_MINDMAP/FATIHAH_MASTER_MINDMAP.pdf" target="_blank" class="btn btn-outline">📄 Vector PDF</a>
        </div>
      </section>

      <div class="plate-nav-bar">
        <div class="tabs-group" id="tabsGroup">
          <button class="tab-btn active" onclick="switchPlate(1)">
            <span>Plate 01</span>
            <small style="opacity:0.7;">Pillars 1 & 2</small>
          </button>
          <button class="tab-btn" onclick="switchPlate(2)">
            <span>Plate 02</span>
            <small style="opacity:0.7;">Pillars 3 & 4</small>
          </button>
          <button class="tab-btn" onclick="switchPlate(3)">
            <span>Plate 03</span>
            <small style="opacity:0.7;">Pillars 5 & 6</small>
          </button>
          <button class="tab-btn" onclick="switchPlate(4)">
            <span>Plate 04</span>
            <small style="opacity:0.7;">Pillars 7 & 8</small>
          </button>
        </div>
        <div>
          <button id="toggleExpandBtn" class="toggle-btn" onclick="toggleExpandAll()">👁️ Show All 4 Plates</button>
        </div>
      </div>

      <section class="page-display" id="pageDisplay">
        <!-- Rendered via JS -->
      </section>
    </main>
  </div>

  <footer>
    <div>HUURS KNOWLEDGE SYSTEMS &bull; AUTHENTIC SUNNI SOURCE DISCIPLINE &bull; ZERO TIMESTAMPS &bull; ZERO SPEAKER NAMES</div>
    <div class="footer-gold">SURAH AL-FATIHAH DIGITAL SUITE &bull; 6 PLATES &bull; 8 PILLARS &bull; 32 CARDS</div>
  </footer>

  <!-- MODAL: DIVINE DIALOGUE -->
  <div class="modal-backdrop" id="modalDialogue">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">👑 THE DIVINE DIALOGUE: THE HALVED PRAYER (SAHIH MUSLIM #395)</div>
        <button class="modal-close" onclick="closeModal('modalDialogue')">&times;</button>
      </div>
      <div class="modal-body">
        <div>
          <h4>The Live Responsive Encounter in Prayer</h4>
          <p>
            Imam Muslim records from Abu Hurairah that the Messenger of Allah (peace be upon him) said: 
            <em>Allah the Exalted said: "I have divided the prayer between Myself and My servant into two halves, and My servant shall have what he asked for."</em>
          </p>
        </div>

        <div class="modal-grid">
          <div class="modal-card">
            <div class="modal-card-title">1. The Master's Half (Praise & Sovereignty)</div>
            <ul style="padding-left:16px; font-size:11.5px; color:var(--text-muted); display:flex; flex-direction:column; gap:4px;">
              <li><strong>Servant:</strong> <em>Al-Hamdu lillahi Rabbil-'Alamin</em><br>&rarr; <strong>Allah:</strong> «Hamidani 'Abdi» (My servant has praised Me).</li>
              <li><strong>Servant:</strong> <em>Ar-Rahmanir-Rahim</em><br>&rarr; <strong>Allah:</strong> «Athna 'alayya 'Abdi» (My servant has exalted Me).</li>
              <li><strong>Servant:</strong> <em>Maliki Yawmid-Deen</em><br>&rarr; <strong>Allah:</strong> «Majjadani 'Abdi» (My servant has glorified Me).</li>
            </ul>
          </div>

          <div class="modal-card">
            <div class="modal-card-title">2. The Servant's Half (Petition & Guidance)</div>
            <ul style="padding-left:16px; font-size:11.5px; color:var(--text-muted); display:flex; flex-direction:column; gap:4px;">
              <li><strong>Servant:</strong> <em>Iyyaka Na'budu wa Iyyaka Nasta'een</em><br>&rarr; <strong>Allah:</strong> «Hadha bayni wa bayna 'abdi, wa li-'abdi ma sa'al» (This is between Me and My servant, and My servant shall have what he asked).</li>
              <li><strong>Servant:</strong> <em>Ihdinas-Sirat al-Mustaqeem...</em><br>&rarr; <strong>Allah:</strong> «Hadha li-'abdi, wa li-'abdi ma sa'al» (This is for My servant, and My servant shall have what he asked).</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: RING COMPOSITION -->
  <div class="modal-backdrop" id="modalRing">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">🛡️ THE CONCENTRIC RING COMPOSITION OF SURAH AL-FATIHAH</div>
        <button class="modal-close" onclick="closeModal('modalRing')">&times;</button>
      </div>
      <div class="modal-body">
        <div>
          <h4>The Symmetrical Architecture of Revelation</h4>
          <p>
            Surah Al-Fatihah is structured around a central fulcrum (Verse 5) flanked by three opening verses of pure divine description and three closing verses of pure human petition:
          </p>
        </div>

        <div class="modal-card">
          <ul style="padding-left:16px; font-size:12px; color:var(--text-muted); display:flex; flex-direction:column; gap:6px;">
            <li><strong>A:</strong> Transcendent Name & Dual Mercy &bull; <em>Verse 1 (Basmalah)</em></li>
            <li><strong>B:</strong> Cosmic Lordship & Absolute Praise &bull; <em>Verse 2 (Al-Hamd)</em></li>
            <li><strong>C:</strong> Maternal Compassion Re-iterated &bull; <em>Verse 3 (Ar-Rahman)</em></li>
            <li><strong>D:</strong> Sovereign Court of Recompense &bull; <em>Verse 4 (Yawm ad-Deen)</em></li>
            <li><strong style="color:var(--gold);">★ E (CENTER PIVOT): THE COVENANT OF SURRENDER &bull; <em>Verse 5 (Iyyaka Na'budu)</em></strong></li>
            <li><strong>D':</strong> Sovereign Guidance Requested &bull; <em>Verse 6 (Ihdinas-Sirat)</em></li>
            <li><strong>C':</strong> Bestowal of Divine Favor &bull; <em>Verse 7a (An'amta 'alayhim)</em></li>
            <li><strong>B':</strong> Protection from Earned Wrath &bull; <em>Verse 7b (Ghayril-maghdub)</em></li>
            <li><strong>A':</strong> Protection from Wandering Astray &bull; <em>Verse 7c (Wa lad-Dallin)</em></li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: SUNNI AUDIT -->
  <div class="modal-backdrop" id="modalAudit">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">📜 AUTHENTIC SUNNI SOURCE DISCIPLINE & GUARANTEE</div>
        <button class="modal-close" onclick="closeModal('modalAudit')">&times;</button>
      </div>
      <div class="modal-body">
        <div>
          <h4>Huurs Studio Verification Protocol</h4>
          <p>
            All 4 content plates, 8 thematic pillars, and 32 conceptual cards have been audited claim-by-claim by <strong>Source Verification (AGENT-03)</strong> and <strong>Islamic QA (AGENT-15)</strong>:
          </p>
          <ul style="margin-top:8px; padding-left:16px; font-size:12px; color:var(--text-muted); display:flex; flex-direction:column; gap:6px;">
            <li><strong>Canonical Exegetes:</strong> Tafsir Ibn Kathir, Jami' al-Bayan (Al-Tabari), Al-Jami' li-Ahkam al-Qur'an (Al-Qurtubi), and Mafatih al-Ghayb (Al-Razi).</li>
            <li><strong>Authentic Hadith Method:</strong> Traditions verified in Sahih al-Bukhari, Sahih Muslim, and sunan compilations with established isnads.</li>
            <li><strong>Zero Contemporary Speaker Names:</strong> Pure institutional voice reflecting universal Sunni scholarship.</li>
            <li><strong>Zero Audio Timestamps:</strong> Conceptual and spiritual permanence without ephemeral media tags.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <script>
    const DATASET = {dataset_json};
    let currentPlateIndex = 0;
    let isExpandedAll = false;

    function initSidebar() {{
      const list = document.getElementById('plateNavList');
      list.innerHTML = '';

      DATASET.forEach((p, idx) => {{
        const item = document.createElement('div');
        item.className = `plate-nav-item ${{idx === currentPlateIndex ? 'active' : ''}}`;
        item.onclick = () => selectPlate(idx);

        item.innerHTML = `
          <div class="plate-nav-num">PLATE 0${{p.plate}}</div>
          <div class="plate-nav-title">${{p.title}}</div>
        `;
        list.appendChild(item);
      }});
    }}

    function selectPlate(idx) {{
      currentPlateIndex = idx;
      document.querySelectorAll('.plate-nav-item').forEach((it, i) => {{
        it.classList.toggle('active', i === idx);
      }});
      document.querySelectorAll('.tab-btn').forEach((btn, i) => {{
        btn.classList.toggle('active', i === idx);
      }});
      updateBanner();
      renderPlates();
    }}

    function switchPlate(pNum) {{
      if (isExpandedAll) toggleExpandAll();
      selectPlate(pNum - 1);
    }}

    function updateBanner() {{
      const p = DATASET[currentPlateIndex];
      document.getElementById('bannerPlateBadge').textContent = `PLATE 0${{p.plate}} OF 04`;
      document.getElementById('bannerTitle').textContent = p.title;
    }}

    function toggleExpandAll() {{
      isExpandedAll = !isExpandedAll;
      const btn = document.getElementById('toggleExpandBtn');
      btn.classList.toggle('active', isExpandedAll);
      btn.textContent = isExpandedAll ? '📄 Single Plate View' : '👁️ Show All 4 Plates';

      const tabGroup = document.getElementById('tabsGroup');
      if (isExpandedAll) {{
        tabGroup.style.opacity = '0.4';
        tabGroup.style.pointerEvents = 'none';
      }} else {{
        tabGroup.style.opacity = '1';
        tabGroup.style.pointerEvents = 'auto';
      }}
      renderPlates();
    }}

    function renderPlates() {{
      const display = document.getElementById('pageDisplay');
      display.innerHTML = '';

      const platesToRender = isExpandedAll ? DATASET : [DATASET[currentPlateIndex]];

      platesToRender.forEach(pg => {{
        const pageCard = document.createElement('div');
        pageCard.className = 'page-card';

        let pillarsHtml = '';
        pg.pillars.forEach(pil => {{
          let cardsHtml = '';
          pil.cards.forEach(c => {{
            let bulletsHtml = c.bullets.map(b => `<li>${{b}}</li>`).join('');
            cardsHtml += `
              <div class="card-item" id="card-${{pg.plate}}-${{pil.name.replace(/[^0-9]/g, '')}}-${{c.num}}">
                <div class="card-title">
                  <span class="num">${{c.num}}.</span>
                  <span>${{c.title}}</span>
                </div>
                <ul class="card-bullets">${{bulletsHtml}}</ul>
              </div>
            `;
          }});

          pillarsHtml += `
            <div class="pillar-box">
              <div class="pillar-header ${{pil.color}}">
                <div class="pillar-title">${{pil.name}}</div>
                <div class="pillar-sub">${{pil.sub}}</div>
              </div>
              <div class="cards-stack">
                ${{cardsHtml}}
              </div>
            </div>
          `;
        }});

        pageCard.innerHTML = `
          <div class="page-card-header">
            <div class="page-heading">
              <h3>${{pg.title}}</h3>
              <p>${{pg.desc}}</p>
            </div>
            <span class="page-sec-badge">${{pg.sec}}</span>
          </div>
          <div class="pillars-container">
            ${{pillarsHtml}}
          </div>
        `;
        display.appendChild(pageCard);
      }});
    }}

    // Search functionality
    const searchInput = document.getElementById('globalSearch');
    const searchResults = document.getElementById('searchResults');
    const searchClear = document.getElementById('searchClear');

    searchInput.addEventListener('input', (e) => {{
      const query = e.target.value.trim().toLowerCase();
      if (query.length < 2) {{
        searchResults.classList.remove('open');
        searchClear.style.display = 'none';
        return;
      }}
      searchClear.style.display = 'block';
      performSearch(query);
    }});

    searchClear.addEventListener('click', () => {{
      searchInput.value = '';
      searchResults.classList.remove('open');
      searchClear.style.display = 'none';
      searchInput.focus();
    }});

    function performSearch(query) {{
      const matches = [];
      DATASET.forEach((pg, pIdx) => {{
        pg.pillars.forEach((pil) => {{
          pil.cards.forEach((c) => {{
            const inTitle = c.title.toLowerCase().includes(query);
            const matchedBullets = c.bullets.filter(b => b.toLowerCase().includes(query));
            if (inTitle || matchedBullets.length > 0) {{
              matches.push({{
                plateIdx: pIdx,
                plateNum: pg.plate,
                pillarName: pil.name,
                cardTitle: c.title,
                snippet: matchedBullets[0] || c.title,
                cardId: `card-${{pg.plate}}-${{pil.name.replace(/[^0-9]/g, '')}}-${{c.num}}`
              }});
            }}
          }});
        }});
      }});

      renderSearchResults(matches, query);
    }}

    function renderSearchResults(matches, query) {{
      if (matches.length === 0) {{
        searchResults.innerHTML = `
          <div class="search-meta-bar">
            <span>NO MATCHES FOUND</span>
            <span>0 RESULTS</span>
          </div>
          <div style="padding:16px; font-size:12px; color:var(--text-muted); text-align:center;">
            No cards found matching "${{query}}". Try searching for "hamd", "mercy", "sirat", "iyyaka", or "guidance".
          </div>
        `;
        searchResults.classList.add('open');
        return;
      }}

      let html = `
        <div class="search-meta-bar">
          <span>SEARCH RESULTS ACROSS 32 CARDS</span>
          <span>${{matches.length}} MATCHES</span>
        </div>
      `;

      const regex = new RegExp(`(${{query}})`, 'gi');

      matches.forEach(m => {{
        const hlTitle = m.cardTitle.replace(regex, '<span class="highlight-term">$1</span>');
        const hlSnippet = m.snippet.replace(regex, '<span class="highlight-term">$1</span>');
        html += `
          <div class="search-item" onclick="jumpToSearchResult(${{m.plateIdx}}, '${{m.cardId}}')">
            <div class="search-item-location">Plate 0${{m.plateNum}} &bull; ${{m.pillarName}}</div>
            <div class="search-item-header">${{hlTitle}}</div>
            <div class="search-item-snippet">${{hlSnippet}}</div>
          </div>
        `;
      }});

      searchResults.innerHTML = html;
      searchResults.classList.add('open');
    }}

    function jumpToSearchResult(plateIdx, cardId) {{
      searchResults.classList.remove('open');
      if (!isExpandedAll) {{
        selectPlate(plateIdx);
      }}
      setTimeout(() => {{
        const cardElem = document.getElementById(cardId);
        if (cardElem) {{
          cardElem.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          cardElem.classList.add('highlight-pulse');
          setTimeout(() => cardElem.classList.remove('highlight-pulse'), 4000);
        }}
      }}, 200);
    }}

    function openModal(id) {{ document.getElementById(id).classList.add('open'); }}
    function closeModal(id) {{ document.getElementById(id).classList.remove('open'); }}

    window.onclick = function(event) {{
      if (event.target.classList.contains('modal-backdrop')) {{
        event.target.classList.remove('open');
      }}
      if (!event.target.closest('.search-wrapper')) {{
        searchResults.classList.remove('open');
      }}
    }};

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('open'));
        searchResults.classList.remove('open');
      }}
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {{
        e.preventDefault();
        searchInput.focus();
      }}
    }});

    initSidebar();
    selectPlate(0);
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"SURAH_AL_FATIHAH_INTERACTIVE_SUITE.html generated: {OUTPUT_HTML} ({len(html_template)} bytes)")
