#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-An'am Master Mindmap HTML & Markdown Generator
8 Landscape Plates &bull; 16 Thematic Pillars &bull; 64 Detailed Analytical Cards
"""

import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "AL_ANAM_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "AL_ANAM_MASTER_MINDMAP.md")

pages_data = [
    {
        "page": 1,
        "title": "COSMIC CREATION & THE KEYS OF THE UNSEEN",
        "desc": "Pillars 1 & 2: Primordial Creation, Al-Qahir Transcendence, Mafatih al-Ghayb & The Falling Leaf",
        "sec": "PLATE 01 : CREATION & OMNISCIENCE",
        "pillars": [
            {
                "name": "PILLAR 1: PRIMORDIAL CREATION & SKEPTICISM",
                "sub": "Cosmic Architecture, Clay Genesis & Demand for Miracles",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Divine Architecture: Darkness & Light",
                        "bullets": [
                            "Praise be to Allah who originated heavens, earth, darkness, and light ex nihilo.",
                            "Darkness mentioned in the plural (Zulumat); truth and light always in the singular.",
                            "Refuting dualistic philosophies: Setting up equals (Ya'diloon) is cosmic absurdity."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Creation from Clay & The Appointed Term",
                        "bullets": [
                            "Humankind originated from terrestrial clay; life bound to an appointed lifespan (Ajal).",
                            "A second term known exclusively to Him: The predetermined hour of resurrection.",
                            "Skepticism condemned: Despite manifest mortal boundaries, deniers continue to doubt."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Demand for Sensory Angels & Paper Books",
                        "bullets": [
                            "Even if a physical parchment descended from heaven, skeptics would dismiss it as sorcery.",
                            "Demands for visible angels refuted: An angel appearing would seal immediate judgment.",
                            "Were an angel sent as an emissary, he would have appeared in mortal human clothing."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Al-Qahir: Sovereign Might Over Creation",
                        "bullets": [
                            "He is the Irresistible Subduer (Al-Qahir) established supreme above all His servants.",
                            "If Allah touches you with adversity, none can remove it except Him alone.",
                            "If He touches you with good, He is over all things competent; the Wise, the Aware."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 2: MAFATIH AL-GHAYB: DIVINE OMNISCIENCE",
                "sub": "The Keys of the Unseen, Falling Leaves & Nocturnal Recall",
                "color": "purple",
                "cards": [
                    {
                        "num": "5",
                        "title": "The Keys of the Unseen: Known Only to Him",
                        "bullets": [
                            "With Him are the Keys of the Unseen (Mafatih al-Ghayb); none knows them except He.",
                            "Authenticated Sunnah enumerates five: The Hour, rain, womb secrets, morrow, and death.",
                            "Sovereign knowledge encompasses everything upon the dry land and in the fathomless ocean."
                        ]
                    },
                    {
                        "num": "6",
                        "title": "The Falling Leaf & Hidden Grain in Darkness",
                        "bullets": [
                            "Not a single leaf drops in any forest or mountain without His specific awareness.",
                            "Not a seed hidden in subterranean earth, nor anything moist or dry escapes.",
                            "Every microscopic motion is recorded in an infallible Preserved Register (Kitabin Mubeen)."
                        ]
                    },
                    {
                        "num": "7",
                        "title": "Nocturnal Recall: Sleep as Temporary Death",
                        "bullets": [
                            "He takes your souls by night (in sleep) and knows whatever deeds you commit by day.",
                            "Awakening humanity each morning until an appointed lifespan is fully realized.",
                            "Sleep serves as a daily living demonstration of the ease and reality of resurrection."
                        ]
                    },
                    {
                        "num": "8",
                        "title": "Al-Hisab: Swift Reckoner of All Existence",
                        "bullets": [
                            "When death approaches any servant, angelic messengers take his soul without neglect.",
                            "Returned unto Allah, their true Sovereign Master; to Him alone belongs all ultimate judgment.",
                            "Sovereign finality: He is the swiftest of all reckoners across entire cosmic creation."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 2,
        "title": "PROPHETIC CONSOLATION & THE CRUCIBLE OF DENIAL",
        "desc": "Pillars 3 & 4: Prophetic Solace, Futile Regret at the Fire, The Deception of Plenty & Path of Criminals",
        "sec": "PLATE 02 : CRUCIBLE OF DENIAL",
        "pillars": [
            {
                "name": "PILLAR 3: THE CONSOLATION OF TRUTH & HUMILIATION",
                "sub": "Denying Signs, Not the Prophet, The Fire's Edge & Dunya's Game",
                "color": "emerald",
                "cards": [
                    {
                        "num": "9",
                        "title": "Consoling the Prophet: They Reject God's Signs",
                        "bullets": [
                            "Divine solace to the Prophet: We know that what they say grieves your tender heart.",
                            "In reality, they do not consider you a liar; rather, the unjust reject the signs of God.",
                            "Past messengers endured rejection and persecution with patience until divine victory arrived."
                        ]
                    },
                    {
                        "num": "10",
                        "title": "The Futile Wish at the Fire: If Only We Returned!",
                        "bullets": [
                            "Standing before the Fire in horror: 'If only we could be returned to worldly life!'",
                            "Pleading to become believers, yet exposed as congenital liars driven by acute panic.",
                            "Divine diagnosis: Even if returned, they would inevitably revert to what was forbidden."
                        ]
                    },
                    {
                        "num": "11",
                        "title": "Dunya as Play and Amusement: The Real Abode",
                        "bullets": [
                            "Worldly existence is nothing but fleeting play (La'ib) and distraction (Lahw).",
                            "The home of the Hereafter is incomparably superior for those who possess authentic Taqwa.",
                            "Rhetorical piercing: 'Will you not then use your intellect and reason?'"
                        ]
                    },
                    {
                        "num": "12",
                        "title": "The Trial of Hardship: Why Not Humble Themselves?",
                        "bullets": [
                            "Nations before you were afflicted with poverty and illness so that they might humble themselves.",
                            "Tragedy of arrogance: When hardship struck, their hearts hardened instead of softening.",
                            "Satan adorned their corrupt deeds, blinding their moral faculties from seeking repentance."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 4: THE SUDDEN GRIP & SANCTUARY OF HUMBLE",
                "sub": "Istidraj Deception, Rooting Out Tyranny & Sabeel al-Mujrimeen",
                "color": "gold",
                "cards": [
                    {
                        "num": "13",
                        "title": "The Deception of Plenty: Opening All Doors",
                        "bullets": [
                            "When they forgot what they were reminded of, We opened to them gates of every luxury.",
                            "Until, as they rejoiced in their material abundance, We seized them suddenly in despair.",
                            "The spiritual law of Istidraj: Ungrateful prosperity precedes catastrophic divine collapse."
                        ]
                    },
                    {
                        "num": "14",
                        "title": "Radical Severance: Cutting Roots of Oppressors",
                        "bullets": [
                            "The remnant of the people who committed tyranny was utterly severed and eradicated.",
                            "Concluding cosmic doxology: 'And praise be to Allah, Lord of all the worlds!'",
                            "Divine justice cleanses the earth of persistent oppressors who terrorize creation."
                        ]
                    },
                    {
                        "num": "15",
                        "title": "Sanctuary of Humble: Repel Not Morning Callers",
                        "bullets": [
                            "Explicit divine order: Never dismiss those who call upon their Lord morning and evening.",
                            "Sincere seekers desiring only His Face; worldly elites have no claim to expel them.",
                            "Social egalitarianism of Islam: Spiritual sincerity outranks tribal lineage and wealth."
                        ]
                    },
                    {
                        "num": "16",
                        "title": "Sabeel al-Mujrimeen: Path of Criminals Distinct",
                        "bullets": [
                            "Thus We explain the signs in detail so that the pathway of criminals is made plain.",
                            "Epistemic clarity: Righteousness cannot be distinguished without exposing corruption.",
                            "Rebuffing compromises: Refusing to follow arbitrary passions that contradict truth."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 3,
        "title": "CELESTIAL EPISTEMOLOGY & IBRAHIM'S DIALECTIC",
        "desc": "Pillars 5 & 6: Ibrahim's Deconstruction of Astral Worship, La Uhibbul-Afileen & The Citadel of Security (Al-Amn)",
        "sec": "PLATE 03 : CELESTIAL EPISTEMOLOGY",
        "pillars": [
            {
                "name": "PILLAR 5: IBRAHIM'S DECONSTRUCTION OF ASTRAL DEITIES",
                "sub": "Stars, Moon, Sun & The Golden Principle: La Uhibbul-Afileen",
                "color": "rose",
                "cards": [
                    {
                        "num": "17",
                        "title": "Turning Away from Cynical Mockery of Truth",
                        "bullets": [
                            "When you see those who engage in mockery of Our verses, turn away until they change topic.",
                            "If Satan causes you to forget, do not sit after remembering with the unjust wrongdoers.",
                            "Intellectual and spiritual hygiene: Guarding the heart against cynical sarcasm."
                        ]
                    },
                    {
                        "num": "18",
                        "title": "The Star Rises: Can a Setting Body Be Divine?",
                        "bullets": [
                            "As darkness engulfed him, Ibrahim beheld a glittering celestial planet/star.",
                            "Postulating the opponent's premise: 'Is this my Lord?' testing its metaphysical reality.",
                            "As the star descended below the horizon, the premise collapsed through visible motion."
                        ]
                    },
                    {
                        "num": "19",
                        "title": "The Radiant Moon & Blazing Sun: Contingency",
                        "bullets": [
                            "Beholding the moon rising in radiance; yet when it waned and set, contingency was proved.",
                            "Beholding the sun blazing across the horizon: 'This is greater!' Yet it set into night.",
                            "Celestial luminaries are bound by physical laws; they are created signs, not gods."
                        ]
                    },
                    {
                        "num": "20",
                        "title": "La Uhibbul-Afileen: 'I Love Not That Which Sets!'",
                        "bullets": [
                            "The liberating epistemological axiom: The heart cannot anchor upon what disappears.",
                            "Setting bodies prove their non-divinity; true devotion belongs to the Permanent Originator.",
                            "Total disavowal: 'O my people, indeed I am free from all that you associate with God!'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 6: CITADEL OF SECURITY & PURE CREED",
                "sub": "Turning to Fatir as-Samawat, Freedom from Fear & Hujjatullah",
                "color": "cyan",
                "cards": [
                    {
                        "num": "21",
                        "title": "Wajjahtu Wajhiya: Total Consecration to Creator",
                        "bullets": [
                            "'I have turned my face toward Him who originated the heavens and earth, purely upright.'",
                            "Rejection of all polytheistic compromises: 'And I am not of those who associate partners.'",
                            "Complete orientation of heart and soul to the Transcendent Maker of cosmic order."
                        ]
                    },
                    {
                        "num": "22",
                        "title": "Confronting Fear: Who Has Greater Right to Peace?",
                        "bullets": [
                            "His people argued with him; Ibrahim replied: 'Do you argue with me concerning Allah?'",
                            "'How should I fear what you associate, when you fear not associating partners with God?'",
                            "Piercing challenge: Which of the two parties possesses greater right to absolute security?"
                        ]
                    },
                    {
                        "num": "23",
                        "title": "Tainting Not Faith with Dhulm: Shirk as Injustice",
                        "bullets": [
                            "Those who believe and taint not their faith with Dhulm—for them is absolute security (Al-Amn).",
                            "Sahih hadith clarification: Dhulm here is Shirk, as Luqman said: 'Shirk is a monstrous wrong.'",
                            "The psychological reward of pure Tawhid: Inner tranquility and infallible divine guidance."
                        ]
                    },
                    {
                        "num": "24",
                        "title": "Hujjatullah: Decisive Divine Proof Bestowed",
                        "bullets": [
                            "That was Our decisive argument (Hujjatuna) which We gave to Ibrahim against his people.",
                            "We raise in degrees whom We will; indeed, your Lord is All-Wise and All-Knowing.",
                            "Intellectual and prophetic triumph of monotheism over astrology and pagan superstition."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 4,
        "title": "THE PROPHETIC GOLDEN CHAIN & THE CRITERION OF TRUTH",
        "desc": "Pillars 7 & 8: The Constellation of 18 Prophets, Fa-bihudahumu-qtadih, Slander on Revelation & Slanderers' Agony",
        "sec": "PLATE 04 : THE PROPHETIC CHAIN",
        "pillars": [
            {
                "name": "PILLAR 7: THE PROPHETIC CONSTELLATION & MANDATE",
                "sub": "18 Named Prophets, Unified Lineage & The Duty of Emulation",
                "color": "purple",
                "cards": [
                    {
                        "num": "25",
                        "title": "The Golden Lineage: Patriarchs & Rulers",
                        "bullets": [
                            "Ibrahim blessed with Ishaq and Ya'qub; Nuh guided previously in ancient generation.",
                            "Prophetic leaders and kings: Dawud, Sulayman, Ayyub, Yusuf, Musa, and Harun.",
                            "All blessed with wisdom, moral fortitude, and victory: 'Thus do We reward the righteous.'"
                        ]
                    },
                    {
                        "num": "26",
                        "title": "Ascetic Emissaries: Zakariyya, Yahya, Isa & Ilyas",
                        "bullets": [
                            "Ascetic masters of prayer and purity: Zakariyya, Yahya, Isa, and Ilyas.",
                            "All affirmed as belonging to the righteous (As-Salileen), dedicated to unceasing worship.",
                            "Global heralds: Isma'il, Al-Yasa' (Elisha), Yunus, and Lut—favored over all nations."
                        ]
                    },
                    {
                        "num": "27",
                        "title": "Universal Favor: Chosen Above the Nations",
                        "bullets": [
                            "Chosen from their fathers, descendants, and brothers; guided to the One Straight Path.",
                            "Divine protection: That is the guidance of Allah by which He guides whom He wills.",
                            "Severe warning: If even they had committed Shirk, all their great deeds would have perished."
                        ]
                    },
                    {
                        "num": "28",
                        "title": "Fa-bihudahumu-qtadih: Follow Their United Guidance",
                        "bullets": [
                            "'Those are the ones whom Allah has guided, so by their guidance be guided!'",
                            "The Prophet Muhammad commanded to follow the unified monotheistic standard of all prophets.",
                            "Pure mission: 'I ask of you no monetary fee for this; it is but a reminder to the worlds.'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 8: REVEALING SCRIPTURE & SLANDERERS' AGONY",
                "sub": "Musa's Torah, Blessed Qur'an & The Agony of Death Throes",
                "color": "emerald",
                "cards": [
                    {
                        "num": "29",
                        "title": "Diminishing God: Claiming No Scripture Sent",
                        "bullets": [
                            "They did not appraise Allah with true appraisal when they said: 'Allah revealed nothing.'",
                            "Decisive historical counter-question: 'Who revealed the scripture that Musa brought?'",
                            "Bringing light and guidance to humanity, which they put into parchments hiding much."
                        ]
                    },
                    {
                        "num": "30",
                        "title": "The Light of Musa: Knowledge Formerly Unknown",
                        "bullets": [
                            "Taught through revelation that which neither you nor your ancestral fathers knew.",
                            "Divine dismissal of obstinacy: 'Say: Allah [revealed it]!' then leave them to play in folly.",
                            "Revelation is the supreme conduit of objective truth across all human history."
                        ]
                    },
                    {
                        "num": "31",
                        "title": "Mubarakun Musaddiq: Blessed Confirming Qur'an",
                        "bullets": [
                            "And this is a blessed Book We have sent down, confirming that which preceded it.",
                            "Revealed to warn the Mother of Cities (Makkah) and all civilization around its periphery.",
                            "Those who believe in the Hereafter believe in it and preserve their daily prayers."
                        ]
                    },
                    {
                        "num": "32",
                        "title": "Death Throes of Slanderers: Angels Strike",
                        "bullets": [
                            "Who is more unjust than one who invents lies against Allah or falsely claims revelation?",
                            "If only you could see when the unjust are in death agonies, angels stretching forth hands:",
                            "'Surrender your souls! Today you are awarded the humiliating punishment for your lies!'"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 5,
        "title": "COSMIC SIGNS, VEGETATION & THE SOLITARY RETURN",
        "desc": "Pillars 9 & 10: Furada Solitary Reckoning, Faliqul-Habbi Seeds, Cleaving Dawn & The Ripening Fruits",
        "sec": "PLATE 05 : SIGNS & SOLITARY RETURN",
        "pillars": [
            {
                "name": "PILLAR 9: SOLITARY RECKONING & CLEAVER OF SEEDS",
                "sub": "Furada Solitary Arrival, Severed Ties & The Sprouting Grain",
                "color": "gold",
                "cards": [
                    {
                        "num": "33",
                        "title": "Furada: Returning Solitary as Created",
                        "bullets": [
                            "'And you have returned to Us solitary (Furada), just as We created you the first time.'",
                            "All material fortunes, wealth, and status left completely behind your back on earth.",
                            "Stripped of earthly illusions, facing absolute eternal accountability before the Creator."
                        ]
                    },
                    {
                        "num": "34",
                        "title": "Severed Ties: Vanishing False Intercessors",
                        "bullets": [
                            "'We see not with you your intercessors whom you claimed were partners with Allah.'",
                            "All mythological connections severed; all fabricated illusions vanish into nothingness.",
                            "The total collapse of polytheistic dependency structures on the Day of Resurrection."
                        ]
                    },
                    {
                        "num": "35",
                        "title": "Faliqul-Habbi: Cleaving Grain and Date Seed",
                        "bullets": [
                            "Indeed, Allah is the Cleaver of the grain and date stone (Faliqul-Habbi wan-Nawa).",
                            "He brings forth the living from the dead, and brings forth the dead from the living.",
                            "That is Allah! How then are you deluded and turned away from His glorious reality?"
                        ]
                    },
                    {
                        "num": "36",
                        "title": "Faliqul-Isbah: Slicing the Radiance of Dawn",
                        "bullets": [
                            "Cleaver of the daybreak (Faliqul-Isbah), splitting cosmic darkness with morning light.",
                            "Appointed the night for rest and tranquility, and the sun and moon for precise calculation.",
                            "That is the flawless determination of the Exalted in Might, the All-Knowing."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 10: COSMIC CALENDARS & MIRACLES OF WATER",
                "sub": "Navigational Stars, Descending Rain & Botanical Ripening",
                "color": "rose",
                "cards": [
                    {
                        "num": "37",
                        "title": "Celestial Stars: Beacons in Ocean & Desert",
                        "bullets": [
                            "He placed the stars for you that you may navigate by them through darkness of land and sea.",
                            "Infallible cosmic compass: Guiding travelers across trackless wastes and ocean voyages.",
                            "We have detailed the signs for a people who possess knowledge and reflective intellect."
                        ]
                    },
                    {
                        "num": "38",
                        "title": "Nafsin Wahidah: Single Origin & Repositories",
                        "bullets": [
                            "It is He who produced you all from a single soul (Nafsin Wahidah); a shared origin.",
                            "Designated a place of dwelling on earth (Mustaqarr) and a repository in graves (Mustawda').",
                            "We have detailed the signs for a people who understand the deeper purpose of existence."
                        ]
                    },
                    {
                        "num": "39",
                        "title": "Descending Rain: Olives, Palms & Pomegranates",
                        "bullets": [
                            "Sending down water from heaven producing lush vegetation and thick-clustered dates.",
                            "Orchards of grapes, olives, and pomegranates—botanically resembling yet distinct in taste.",
                            "Diversity of chemical synthesis and sweetness springing from identical soil and water."
                        ]
                    },
                    {
                        "num": "40",
                        "title": "Look Upon the Fruit: Ripening Signs for Faith",
                        "bullets": [
                            "Contemplate its fruit when it bears fruit and when it ripens into rich nourishment.",
                            "Biological transition from bitter unformed matter into sweet, life-sustaining sustenance.",
                            "Indeed, in that are unmistakable signs for a people who truly believe in the Divine Maker."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 6,
        "title": "TRANSCENDENT ESSENCE & ETHICAL POLEMICS",
        "desc": "Pillars 11 & 12: Tanzih Transcendence, La Tudrikuhul-Absar, Civil Propriety & Deceptive Adorned Speech",
        "sec": "PLATE 06 : TRANSCENDENCE & ETHICS",
        "pillars": [
            {
                "name": "PILLAR 11: TANZIH: TRANSCENDENCE BEYOND SENSES",
                "sub": "Badi'us-Samawat, Eradicating Partners & La Tudrikuhul-Absar",
                "color": "cyan",
                "cards": [
                    {
                        "num": "41",
                        "title": "Fabricating Partners: Attributing Jinn & Sons",
                        "bullets": [
                            "Rebutting the pagans who attributed the jinn as partners with Allah, though He created them.",
                            "Falsely imputing sons and daughters unto Him without any knowledge or scriptural authority.",
                            "Sublime exaltation: 'Exalted and Transcendent is He above what they falsely describe!'"
                        ]
                    },
                    {
                        "num": "42",
                        "title": "Badi'us-Samawat: Originator Without Equal",
                        "bullets": [
                            "Originator of the heavens and the earth (Badi') without preexisting model or material.",
                            "'How could He have a child when He has no mate, and He created everything?'",
                            "And He is knowing of all things: Self-sufficient Lord devoid of physical genealogy."
                        ]
                    },
                    {
                        "num": "43",
                        "title": "La Tudrikuhul-Absar: Incomprehensible Majesty",
                        "bullets": [
                            "'No vision can encompass Him (La Tudrikuhul-Absar), but He encompasses all vision.'",
                            "Negates comprehensive encompassing (Ihatah); does not negate believers gazing in Akhirah.",
                            "Absolute transcendence: His Infinite Majesty cannot be circumscribed by created eyes."
                        ]
                    },
                    {
                        "num": "44",
                        "title": "Al-Lateef al-Khabeer: The Subtle, The Fully Aware",
                        "bullets": [
                            "And He is the Most Subtle (Al-Lateef), discerning the most imperceptible realities.",
                            "The All-Aware (Al-Khabeer), fully cognizant of the secret thoughts within human chests.",
                            "Enlightenment has come from your Lord; whoever sees benefits himself, whoever blinds bears it."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 12: ETHICS OF DISCOURSE & ADORNED LIES",
                "sub": "Sadd al-Dhara'i', Ornate Rhetoric of Devils & Supreme Arbiter",
                "color": "purple",
                "cards": [
                    {
                        "num": "45",
                        "title": "Civil Propriety: Revile Not Their Deities",
                        "bullets": [
                            "'Do not insult those whom they invoke besides Allah, lest they insult Allah in enmity.'",
                            "Juristic foundation of Sadd al-Dhara'i': Prohibiting permissible acts that cause greater evil.",
                            "High civil ethics: Persuasion conducted through reason and evidence, not vulgar mockery."
                        ]
                    },
                    {
                        "num": "46",
                        "title": "Retaliatory Blasphemy: Preventing Slander",
                        "bullets": [
                            "Provoking hostile deniers leads to reciprocal blasphemy against the Lord of the worlds.",
                            "Thus have We made attractive to every community their deeds; then to Him is their return.",
                            "Maintaining the sacred dignity of God's name above the cheap fray of polemical shouting."
                        ]
                    },
                    {
                        "num": "47",
                        "title": "Shayateen al-Ins wal-Jinn: Ornate Speech",
                        "bullets": [
                            "Devils among humans and jinn inspiring one another with adorned speech of delusion.",
                            "Intellectual seduction: Falsehood packaged in seductive, sophisticated philosophical rhetoric.",
                            "So leave them and whatever lies they fabricate; truth stands independent of propaganda."
                        ]
                    },
                    {
                        "num": "48",
                        "title": "Seeking None Other Than Allah as Arbiter",
                        "bullets": [
                            "'Shall I seek other than Allah as judge (Hakaman) when He revealed the Book explained?'",
                            "Those to whom We gave the scripture know it is revealed from your Lord in truth.",
                            "Concluding resolve: 'So never be among the doubters!'—Divine sovereignty in arbitration."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 7,
        "title": "THE DIVINE CODE, COMPASSION & PURIFIED SUSTENANCE",
        "desc": "Pillars 13 & 14: Tammat Kalimatu Rabbik, Danger of Majorities, Reborn Light & Eradication of Infanticide",
        "sec": "PLATE 07 : DIVINE CODE & COMPASSION",
        "pillars": [
            {
                "name": "PILLAR 13: PERFECTION OF THE WORD & PARABLE OF LIGHT",
                "sub": "Sidqan wa 'Adla, The Treachery of Majorities & Spiritual Resurrection",
                "color": "emerald",
                "cards": [
                    {
                        "num": "49",
                        "title": "Tammat Kalimatu Rabbika: Truth & Justice",
                        "bullets": [
                            "'And the word of your Lord has been fulfilled in truth (Sidqan) and in justice ('Adla).'",
                            "Complete in historical narrative and truth; equitable in all legal commandments and limits.",
                            "Inviolability of revelation: None can alter His eternal words, and He is Hearing and Knowing."
                        ]
                    },
                    {
                        "num": "50",
                        "title": "The Treachery of Majority: Crowds Mislead",
                        "bullets": [
                            "'If you obey most of those upon the earth, they will mislead you from the path of Allah.'",
                            "Human consensus is no measure of truth; crowds follow nothing except unverified conjecture.",
                            "Your Lord knows best who strays from His path, and He knows best who is rightly guided."
                        ]
                    },
                    {
                        "num": "51",
                        "title": "From Death to Light: Parable of Reborn Believer",
                        "bullets": [
                            "Is one who was spiritually dead, whom We brought to life and gave a light to walk among men,",
                            "Like one who is trapped in multi-layered darkness from which he cannot ever emerge?",
                            "Revelation transforms the dead soul into an illuminated, radiant guide for civil society."
                        ]
                    },
                    {
                        "num": "52",
                        "title": "The Constricted Chest: Climbing Into the Sky",
                        "bullets": [
                            "Whomever Allah wills to guide, He expands his chest to embrace the peace of Islam.",
                            "Whomever He allows to stray, He makes his chest tight and constricted as if climbing the sky.",
                            "Profound psychological insight: Rejection of truth creates suffocating existential constriction."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 14: ABOLISHING PAGAN TABOOS & INFANTICIDE",
                "sub": "Dar as-Salam, Abolishing Daughter-Slaughter & Livestock Purity",
                "color": "gold",
                "cards": [
                    {
                        "num": "53",
                        "title": "Dar as-Salam: The Abode of Inviolate Peace",
                        "bullets": [
                            "And this is the path of your Lord, leading straight; We have detailed the signs.",
                            "For them will be the Abode of Peace (Dar as-Salam) with their Lord in the Hereafter.",
                            "And He will be their loving protecting Ally because of the righteous deeds they worked."
                        ]
                    },
                    {
                        "num": "54",
                        "title": "The Criminality of Infanticide: Slaying Children",
                        "bullets": [
                            "Condemning pagan fathers whose idols adorned the slaughter of their innocent children.",
                            "Sacrificing daughters out of fear of shame or economic poverty; ruined in Dunya and Akhirah.",
                            "Lost indeed are those who murdered their children in ignorance, fabricating lies against God."
                        ]
                    },
                    {
                        "num": "55",
                        "title": "Fabricated Dedications: Crop & Cattle Superstitions",
                        "bullets": [
                            "Rebutting arbitrary dedications: 'This is for Allah, and this is for our fabricated partners.'",
                            "What belongs to partners reaches not Allah, but what belongs to Allah reaches their idols.",
                            "Evil is their judgment: Decimating the economic superstitions of pagan priesthoods."
                        ]
                    },
                    {
                        "num": "56",
                        "title": "The Eight Pairs of Livestock: Refuting Fake Harams",
                        "bullets": [
                            "Eight pairs of livestock: Sheep, goats, camels, and cattle created as divine sustenance.",
                            "Sarcastic challenge: 'Did He forbid the two males or two females or what the wombs contain?'",
                            "Dietary boundaries simplified: Maytah, running blood, swine, and unslaughtered meat alone."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 8,
        "title": "THE MASTER DECALOGUE & THE SUPREME DECLARATION",
        "desc": "Pillars 15 & 16: Al-Wasaya al-'Ashr (The Ten Commandments), Siratee Mustaqeema & Inna Salatee wa Nusukee",
        "sec": "PLATE 08 : THE MASTER DECALOGUE",
        "pillars": [
            {
                "name": "PILLAR 15: AL-WASAYA AL-'ASHR: QURANIC DECALOGUE",
                "sub": "The Universal Charter of Ethics, Sanctity of Life & Full Weights",
                "color": "rose",
                "cards": [
                    {
                        "num": "57",
                        "title": "The Universal Covenant: Tawhid & Parents",
                        "bullets": [
                            "'Say: Come, I will recite what your Lord has prohibited to you: Join no partners with Him.'",
                            "Command of filial devotion: Practice Ihsan toward parents in speech, sustenance, and care.",
                            "Foundational bedrock: The moral order begins with pure monotheism and parental reverence."
                        ]
                    },
                    {
                        "num": "58",
                        "title": "Economic Sanctity of Children & Purity",
                        "bullets": [
                            "'Do not kill your children out of poverty; We provide for you and for them.'",
                            "Absolute prohibition of shameful deeds (Fawahish), whether open or secret.",
                            "Eliminating the twin poisons of infanticide and sexual exploitation from civilization."
                        ]
                    },
                    {
                        "num": "59",
                        "title": "Sanctity of Soul, Orphan Wealth & Justice",
                        "bullets": [
                            "'Kill not the soul which Allah has sanctified, except by legal right.'",
                            "'Approach not the orphan's property except to enhance it until maturity.'",
                            "'Give full measure and weight with justice; when you speak, be fair even against relatives.'"
                        ]
                    },
                    {
                        "num": "60",
                        "title": "Hadha Siratee Mustaqeema: The One Pathway",
                        "bullets": [
                            "'And this is My path, which is straight, so follow it; and follow not divergent pathways.'",
                            "The Prophet drew a straight line in the dust, and lines branching off it, warned of devils.",
                            "Divergent sect pathways scatter you away from His road: The covenant of unified truth."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 16: UNIVERSAL SURRENDER & EARTH'S STEWARDS",
                "sub": "Tenfold Grace, Inna Salatee wa Nusukee & Khala'if al-Ard",
                "color": "cyan",
                "cards": [
                    {
                        "num": "61",
                        "title": "The Tenfold Bounty: Divine Mercy Multiplied",
                        "bullets": [
                            "Whoever brings a good deed shall receive ten times the like thereof in divine reward.",
                            "Whoever brings an evil deed shall not be recompensed except with its exact equivalent.",
                            "Divine justice is untainted: 'And they shall not be wronged in the slightest.'"
                        ]
                    },
                    {
                        "num": "62",
                        "title": "Inna Salatee wa Nusukee: The Master Declaration",
                        "bullets": [
                            "'Say: Indeed, my prayer, my sacrifice, my living, and my dying are all for Allah alone.'",
                            "'Lord of all the worlds; no partner has He; and with this I have been commanded.'",
                            "'And I am the first of those who surrender (Muslims)': The supreme manifesto of monotheism."
                        ]
                    },
                    {
                        "num": "63",
                        "title": "Bearing No Other's Burden: Personal Responsibility",
                        "bullets": [
                            "Every soul earns only against itself; no bearer of burdens bears the burden of another.",
                            "Rejection of inherited sin and collective guilt: Absolute moral individual accountability.",
                            "Then to your Lord is your return, and He will inform you concerning all that you disputed."
                        ]
                    },
                    {
                        "num": "64",
                        "title": "Khala'if al-Ard: Divine Test of Successorship",
                        "bullets": [
                            "It is He who made you successors upon the earth (Khala'if al-Ard), generation after generation.",
                            "Raised some of you above others in ranks that He may test you in what He has given you.",
                            "Final balance: Indeed, your Lord is swift in retribution, yet He is Forgiving and Merciful."
                        ]
                    }
                ]
            }
        ]
    }
]

# Generate Markdown Document
md_content = """# Surah Al-An'am: Master Landscape Mindmap Cartography
## 8 Master Plates • 16 Thematic Pillars • 64 Structured Cards
**Operating Philosophy:** **READ. REFLECT. RETURN.**  
**Brand Authority:** Huurs Studio Knowledge Architecture  
**Canonical Conspectus:** Imam al-Tabari, Imam al-Razi, Imam al-Qurtubi, Imam Ibn Kathir  

---
"""

for p in pages_data:
    md_content += f"\n## Plate {p['page']:02d}: {p['title']}\n"
    md_content += f"**Description:** {p['desc']}  \n"
    md_content += f"**Section Badge:** `{p['sec']}`\n\n"
    for pil in p['pillars']:
        md_content += f"### {pil['name']}\n"
        md_content += f"*{pil['sub']}*\n\n"
        for c in pil['cards']:
            md_content += f"#### Card {c['num']}: {c['title']}\n"
            for b in c['bullets']:
                md_content += f"- {b}\n"
            md_content += "\n"
    md_content += "---\n"

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"MD generated: {MD_OUT}")

# Generate HTML Document
html_plates = ""
tabs_html = ""
for p in pages_data:
    active_cls = "active" if p['page'] == 1 else ""
    tabs_html += f'<button class="tab-btn {active_cls}" onclick="showPage({p["page"]})">Plate {p["page"]:02d}: {p["sec"].split(":")[-1].strip()}</button>\n'
    
    col1 = p['pillars'][0]
    col2 = p['pillars'][1]
    
    def render_col(col):
        cards_html = ""
        for c in col['cards']:
            bullets = "".join(f"<li>{b}</li>" for b in c['bullets'])
            cards_html += f"""
            <div class="card">
              <div class="card-head">
                <span class="card-num">{c['num']}</span>
                <h4>{c['title']}</h4>
              </div>
              <ul>{bullets}</ul>
            </div>
            """
        return f"""
        <div class="pillar {col['color']}">
          <div class="pillar-header">
            <h3>{col['name']}</h3>
            <p>{col['sub']}</p>
          </div>
          <div class="cards-list">
            {cards_html}
          </div>
        </div>
        """

    html_plates += f"""
    <div class="page-container {active_cls}" id="page-{p['page']}">
      <div class="plate-banner">
        <div>
          <h2>{p['title']}</h2>
          <p>{p['desc']}</p>
        </div>
        <div class="badge-box">
          <span class="badge-gold">[{p['sec']}]</span>
          <span class="badge-emerald">100% SUNNI VERIFIED</span>
        </div>
      </div>
      <div class="columns-grid">
        {render_col(col1)}
        {render_col(col2)}
      </div>
    </div>
    """

html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-An'am Master Landscape Mindmap | Huurs Studio</title>
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
      background: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.5;
      padding: 24px;
    }}
    .wrapper {{ max-width: 1440px; margin: 0 auto; }}
    header.header {{
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
      gap: 12px;
    }}
    .header h1 {{ font-size: 1.25rem; color: var(--gold); letter-spacing: 0.05em; }}
    .header span {{ color: var(--text-muted); font-size: 0.9rem; margin-left: 8px; }}
    .tabs-bar {{
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
      overflow-x: auto;
      padding-bottom: 4px;
    }}
    .tab-btn {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .tab-btn:hover {{ border-color: var(--gold); color: var(--white); }}
    .tab-btn.active {{
      background: var(--gold);
      color: var(--navy-deep);
      border-color: var(--gold);
      font-weight: 700;
    }}
    .page-container {{ display: none; }}
    .page-container.active {{ display: block; }}
    .plate-banner {{
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
    .plate-banner h2 {{ font-size: 1.15rem; color: var(--gold-light); margin-bottom: 4px; }}
    .plate-banner p {{ font-size: 0.85rem; color: var(--text-muted); }}
    .badge-box {{ display: flex; gap: 8px; }}
    .badge-gold {{
      background: rgba(212, 175, 55, 0.15);
      color: var(--gold);
      border: 1px solid var(--gold);
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
    }}
    .badge-emerald {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid var(--emerald);
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
    }}
    .columns-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 1024px) {{ .columns-grid {{ grid-template-columns: 1fr; }} }}
    .pillar {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }}
    .pillar.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar.purple {{ border-top: 3px solid var(--purple); }}
    .pillar.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar.gold {{ border-top: 3px solid var(--gold); }}
    .pillar.rose {{ border-top: 3px solid var(--rose); }}
    .pillar-header {{
      background: var(--navy-elevated);
      padding: 12px 18px;
      border-bottom: 1px solid var(--border-muted);
    }}
    .pillar-header h3 {{ font-size: 0.95rem; color: var(--white); }}
    .pillar-header p {{ font-size: 0.78rem; color: var(--text-muted); margin-top: 2px; }}
    .cards-list {{ padding: 14px; display: flex; flex-direction: column; gap: 12px; }}
    .card {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 16px;
      transition: all 0.2s;
    }}
    .card:hover {{ border-color: var(--gold); transform: translateY(-1px); }}
    .card-head {{ display: flex; align-items: baseline; gap: 8px; margin-bottom: 8px; }}
    .card-num {{
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .card-head h4 {{ font-size: 0.88rem; font-weight: 700; color: var(--white); }}
    .card ul {{ list-style-type: none; padding-left: 0; }}
    .card li {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 4px;
      position: relative;
      padding-left: 14px;
    }}
    .card li::before {{
      content: "▪";
      position: absolute;
      left: 0;
      color: var(--gold);
      font-size: 0.8rem;
    }}
    footer.footer {{
      margin-top: 40px;
      border-top: 1px solid var(--border-muted);
      padding: 20px 0;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>
  <div class="wrapper">
    <header class="header">
      <div>
        <h1>HUURS STUDIO</h1>
        <span>Surah Al-An'am Master Landscape Mindmap Cartography</span>
      </div>
      <div style="font-size:0.8rem; color:var(--gold);">
        8 Master Plates &bull; 16 Thematic Pillars &bull; 64 Cards
      </div>
    </header>

    <div class="tabs-bar">
      {tabs_html}
    </div>

    <main>
      {html_plates}
    </main>

    <footer class="footer">
      <p><b>HUURS STUDIO</b> &bull; READ. REFLECT. RETURN. &bull; Sunni Islamic Source Discipline</p>
      <p style="font-size:0.75rem; margin-top:4px;">Imam al-Tabari &bull; Imam al-Razi &bull; Imam al-Qurtubi &bull; Imam Ibn Kathir</p>
    </footer>
  </div>

  <script>
    function showPage(pnum) {{
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.page-container').forEach(page => page.classList.remove('active'));
      document.querySelectorAll('.tab-btn')[pnum - 1].classList.add('active');
      document.getElementById('page-' + pnum).classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}
  </script>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_full)

print(f"HTML generated: {HTML_OUT}")
