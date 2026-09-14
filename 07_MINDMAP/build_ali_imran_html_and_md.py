#!/usr/bin/env python3
"""
Huurs Studio - Surah Ali-Imran Master Mindmap HTML & Markdown Generator
8 Landscape Plates &bull; 16 Thematic Pillars &bull; 64 Detailed Analytical Cards
"""

import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "ALI_IMRAN_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "ALI_IMRAN_MASTER_MINDMAP.md")

pages_data = [
    {
        "page": 1,
        "title": "EPISTEMOLOGY, REVELATION & THE PRIMORDIAL CREED",
        "desc": "Pillars 1 & 2: Muhkam vs. Mutashabih, Rooted Scholars, Rabbana La Tuzigh, and The Metric of Divine Love",
        "sec": "PLATE 01 : CREED",
        "pillars": [
            {
                "name": "PILLAR 1: EPISTEMOLOGY & ROOTED SCHOLARSHIP",
                "sub": "Muhkam, Mutashabih & Epistemological Humility",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Umm al-Kitab: The Decisive Core of Revelation",
                        "bullets": [
                            "Muhkamat: Explicit, unequivocal verses forming the mother/core of the Book.",
                            "They establish immutable creed, moral boundaries, and unambiguous law.",
                            "They serve as the constitutional anchor that prevents theological drift."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Mutashabihat: The Crucible of Human Humility",
                        "bullets": [
                            "Mutashabihat: Multi-dimensional, allegorical verses regarding the Unseen.",
                            "Diseased hearts obsess over ambiguities seeking discord and false interpretation.",
                            "Revelation intentionally contains mystery to test intellectual submission."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Al-Rasikhuna fil-'Ilm: Deeply Rooted Wisdom",
                        "bullets": [
                            "Rooted scholars interpret the ambiguous strictly in light of the clear core.",
                            "Their defining hallmark is not arrogant debate, but reverent surrender.",
                            "Their declaration: 'We believe in it; all of it is from our Lord!'"
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Al-Hayyul-Qayyum: The Uncreated Fountainhead",
                        "bullets": [
                            "Opens with the supreme divine names mirroring the crown of Ayat al-Kursi.",
                            "The Ever-Living, Self-Sustaining Lord who holds creation in continuous order.",
                            "Anchors human epistemology in an absolute, unshakeable ontological source."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 2: THE ANCHORED HEART & PROPHETIC METRIC",
                "sub": "Rabbana La Tuzigh & The Verification of Love",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "Rabbana La Tuzigh: The Supplication of the Rooted",
                        "bullets": [
                            "'Our Lord, let not our hearts deviate after You have guided us.'",
                            "Intellectual brilliance cannot safeguard faith without continuous divine grace.",
                            "Teaches that deviation is a perpetual hazard requiring daily begging for mercy."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Divine Bestowal: Al-Wahhab and Pure Grace",
                        "bullets": [
                            "Guidance is not an entitlement earned by human intellect, but an unearned gift.",
                            "Al-Wahhab bestows spiritual firmness from His immediate presence (Ladunka).",
                            "Humility before the Bestower dissolves self-congratulatory spiritual pride."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Prophetic Emulation: The Metric of Love",
                        "bullets": [
                            "'Say: If you love Allah, then follow me, and Allah will love you.'",
                            "The Divine Love Metric: Divine love is not sentimental emotion or poetry.",
                            "True love is verified exclusively through rigorous imitation of the Messenger."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Sovereign Criterion: Warning Against Deviation",
                        "bullets": [
                            "Obey Allah and the Messenger; turning away exposes counterfeit devotion.",
                            "Rejects esoteric spiritualities that bypass legal and moral commandments.",
                            "Alignment with the Prophetic model is the sole gateway to divine forgiveness."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 2,
        "title": "THE FAMILY OF IMRAN & THE SANCTUARY OF MARYAM",
        "desc": "Pillars 3 & 4: Hannah's Dedicated Vow, The Mihrab Miracles, and Zakariyya's Renewal of Hope",
        "sec": "PLATE 02 : SANCTUARY",
        "pillars": [
            {
                "name": "PILLAR 3: HANNAH'S VOW & MARYAM'S SANCTUARY",
                "sub": "Unconditional Consecration & Out-of-Season Fruits",
                "color": "emerald",
                "cards": [
                    {
                        "num": "1",
                        "title": "Divine Election of the Righteous Lineage",
                        "bullets": [
                            "Allah chose Adam, Nuh, Ibrahim's family, and Imran's family over all mankind.",
                            "A lineage of unbroken devotion where each generation passed the flame of faith.",
                            "Spiritual nobility is anchored in moral uprightness, not biological privilege."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Hannah's Consecrated Vow (Muharraran)",
                        "bullets": [
                            "Hannah dedicated her unborn child exclusively to divine sanctuary service.",
                            "Surrendering personal possessiveness: The child belongs entirely to God.",
                            "Sincere maternal intention transforms private birth into a cosmic turning point."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Female Elevated Beyond Expectation",
                        "bullets": [
                            "Hannah surrendered: 'And the male is not like the female.'",
                            "Divine wisdom honored her birth, elevating Maryam above all worldly men.",
                            "Protected Maryam and her child from Satan's touch at the instant of birth."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Mihrab: Sanctuary of Out-of-Season Fruits",
                        "bullets": [
                            "Secluded in devotion, Maryam received winter fruit in summer and summer in winter.",
                            "When asked, she replied: 'It is from Allah; He provides without measure.'",
                            "The Mihrab proves that God transcends biological seasons and human limits."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 4: ZAKARIYYA'S PETITION & YAHYA'S PROMISE",
                "sub": "Audacious Hope & The Miraculous Conception",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Catalyst: Witnessing Impossible Sustenance",
                        "bullets": [
                            "Witnessing Maryam's out-of-season fruit revived Zakariyya's dormant hope.",
                            "If God provides fruit without trees, He can provide a child without youth.",
                            "Spiritual fellowship ignites audacious supplication in barren circumstances."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Supplication for Pure Lineage (Dhurriyyatan Tayyibah)",
                        "bullets": [
                            "Prayed not for genetic immortality or worldly legacy, but for a pure servant.",
                            "Sincere prayer in the Mihrab: 'Indeed, You are the Hearer of all prayer.'",
                            "Selfless paternal intention oriented wholly toward divine worship."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Angelic Glad Tidings of Yahya",
                        "bullets": [
                            "Angels called while he stood praying: Allah gives glad tidings of Yahya.",
                            "A witness confirming the Word from Allah, noble, chaste, and a prophet.",
                            "Divine response breaks biological impossibility in an instant."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Sign of Sacred Silence: Three Days of Dhikr",
                        "bullets": [
                            "Zakariyya's sign: Inability to speak to people for three days except by gesture.",
                            "Speech arrested from mundane chatter, yet freed for glorifying God abundantly.",
                            "Silence disciplines the tongue and focuses the soul on constant Dhikr."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 3,
        "title": "THE REALITY OF ISA & THE DECISIVE THEOLOGICAL PROOF",
        "desc": "Pillars 5 & 6: Creation from Dust, Miracles by Divine Leave, and The Ultimate Proof of Mubahalah",
        "sec": "PLATE 03 : MONOTHEISM",
        "pillars": [
            {
                "name": "PILLAR 5: CREATION FROM DUST: KAMATHALI ADAM",
                "sub": "Demolition of Deification & The Command Kun",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Annunciation & Infancy Miracles",
                        "bullets": [
                            "Maryam chosen above the women of all creation, receiving the Word from Allah.",
                            "Isa speaks from the cradle in mature eloquence to exonerate his mother.",
                            "Demonstrating prophetic authority from infancy without claiming divinity."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Prophetic Signs Subordinated to Divine Will",
                        "bullets": [
                            "Fashioning clay birds, healing the blind and leper, and raising the dead.",
                            "Every miracle explicitly bound to 'Bi-Idhnillah' (by Allah's permission).",
                            "Signs are instruments of Prophetic vindication, not proofs of godly essence."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Kamathali Adam: The Decisive Exegetical Parable",
                        "bullets": [
                            "'The likeness of Isa with Allah is as the likeness of Adam.'",
                            "Created from dust without father or mother; if birth without father proved",
                            "Divinity, Adam would have greater claim. Both are humble servants made of dust."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Kun Fa-Yakun: Sovereign Transcendent Fiat",
                        "bullets": [
                            "Creation requires no biological mechanism, spouse, or earthly parentage.",
                            "When Allah decrees an affair, He merely says 'Be' (Kun) and it is.",
                            "Exalts Allah above pagan notions of physical procreation and divine sonship."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 6: DISCIPLES, ASCENT & MUBAHALAH",
                "sub": "Hawariyyun, Heavenly Elevation & Decisive Conviction",
                "color": "purple",
                "cards": [
                    {
                        "num": "1",
                        "title": "Al-Hawariyyun: Helpers of Allah in Faith",
                        "bullets": [
                            "When Isa sensed disbelief, he asked: 'Who are my helpers for Allah?'",
                            "The disciples responded: 'We are helpers of Allah; we believe in Him.'",
                            "True followers identify themselves as Muslims submitting to one God."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Divine Elevation: Refuting Crucifixion & Murder",
                        "bullets": [
                            "The plotters schemed, but Allah is the best of planners (Makr).",
                            "'I will take you and raise you to Myself and purify you from the deniers.'",
                            "Isa was not humiliated on a cross; his honor was preserved by divine rescue."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Event of Mubahalah: Invoking the Curse",
                        "bullets": [
                            "Confronting Najran's dogmatic stubbornness with the ultimate test of truth.",
                            "The Prophet was ordered to gather his family and invoke Allah's curse on liars.",
                            "Ultimate proof of moral conviction: Liars never risk the destruction of loved ones."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Retreat of Najran & Unquestioned Truth",
                        "bullets": [
                            "The Najran delegation withdrew from the duel of prayer, seeking peaceful treaty.",
                            "Their retreat stands in history as silent admission of Islamic authenticity.",
                            "Monotheism stands vindicated on both rational argument and spiritual reality."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 4,
        "title": "THE SCRIPTURAL DIALOGUE & THE IBRAHIMIC STANDARD",
        "desc": "Pillars 7 & 8: Kalimatin Sawa', Exonerating Ibrahim, The Prophetic Covenant, and The Summit of Charity",
        "sec": "PLATE 04 : COVENANT",
        "pillars": [
            {
                "name": "PILLAR 7: THE EQUITABLE WORD & IBRAHIM",
                "sub": "Common Ground, Primordial Islam & Dismantling Sects",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Kalimatin Sawa': The Invitation to Common Ground",
                        "bullets": [
                            "'Come to a word that is equitable between us and you.'",
                            "That we worship none but Allah and associate no partner with Him.",
                            "Establishing that religious unity can only rest on pure Tawhid."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Ma Kana Ibrahimu: Exonerating the Patriarch",
                        "bullets": [
                            "'Ibrahim was neither a Jew nor a Christian; he was Hanifan Musliman.'",
                            "Torah and Gospel were revealed centuries after Ibrahim's passing.",
                            "Exposing retroactive sectarian claims as historically anachronistic."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Hanifan Musliman: Upright Primordial Submission",
                        "bullets": [
                            "Hanif: Turning away from all falsehood toward uncompromising Tawhid.",
                            "Ibrahim was never of the polytheists in theology or allegiance.",
                            "Islam is not a 7th-century novelty, but the primordial religion of all prophets."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Reclaiming Sacred Spiritual Lineage",
                        "bullets": [
                            "'Indeed, the closest people to Ibrahim are those who followed him, this Prophet'",
                            "Spiritual legitimacy belongs to those who embody the patriarch's monotheism.",
                            "Faith in the Final Messenger supersedes biological and tribal genealogies."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 8: PROPHETIC COVENANT & PEAK CHARITY",
                "sub": "Mithaq al-Nabiyyeen & Spending What is Beloved",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "Mithaq al-Nabiyyeen: The Covenant of All Messengers",
                        "bullets": [
                            "Every prophet took a sacred oath to believe in and aid the Final Messenger.",
                            "Establishing the cosmic brotherhood and unity of all divine missions.",
                            "Rejection of the Prophet Muhammad contradicts the core pledge of past prophets."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Islam: The Sole Divine Deen Accepted by God",
                        "bullets": [
                            "'Whoever desires other than Islam as religion, never will it be accepted.'",
                            "In the Hereafter he will be among the ultimate losers.",
                            "Rejects religious relativism: Truth is unified and singular before Allah."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Lan Tanalul-Birr: The Summit of True Righteousness",
                        "bullets": [
                            "'Never will you attain true righteousness until you spend from what you love.'",
                            "Faith is not verified by discarding excess leftovers or token scraps.",
                            "The spiritual summit requires detaching the heart from cherished wealth."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Noble Sacrifice of Abu Talha",
                        "bullets": [
                            "Abu Talha gave up Bairuha', his most beloved, freshwater palm garden.",
                            "Surrendered instantly upon hearing the verse, asking for nothing in return.",
                            "Living proof of how the Companions translated abstract verses into deeds."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 5,
        "title": "THE GOLDEN ANCHOR OF UNITY & THE BEST NATION",
        "desc": "Pillars 9 & 10: Holding Fast to Hablillah, Reconciliation of the Heart, and The Mandate of Khayra Ummah",
        "sec": "PLATE 05 : UNITY",
        "pillars": [
            {
                "name": "PILLAR 9: HOLDING THE ROPE OF ALLAH (HABLILLAH)",
                "sub": "Uncompromising Taqwa & Healing Ancient Blood Feuds",
                "color": "emerald",
                "cards": [
                    {
                        "num": "1",
                        "title": "Ittaqu Allaha Haqqa Tuqatih: The Standard of Taqwa",
                        "bullets": [
                            "'Fear Allah as He deserves to be feared, and do not die except as Muslims.'",
                            "Ibn Mas'ud: Remembered and not forgotten, obeyed and not disobeyed, thanked.",
                            "Vigilant God-consciousness must govern every breath until death."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Hablillah: The Unbreakable Divine Lifeline",
                        "bullets": [
                            "'Hold fast to the rope of Allah all together, and do not become divided.'",
                            "The Qur'an and authentic Sunnah form the sole vertical anchor of community.",
                            "Collective survival is impossible when individual strands sever connection."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Miraculous Union of Hearts (Aws & Khazraj)",
                        "bullets": [
                            "Reminding the Ansar of centuries of tribal civil slaughter and hatred.",
                            "Islam bonded their hearts when they stood on the brink of a pit of Fire.",
                            "Fraternal unity is a divine miracle that no worldly wealth could buy."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Mortal Ruin of Sectarian Fracturing",
                        "bullets": [
                            "Warning against imitating nations who splintered after clear proof came.",
                            "Sectarian fracturing invites humiliating punishment in this world and next.",
                            "Preservation of community unity is an existential theological duty."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 10: THE UNIVERSAL MANDATE: KHAYRA UMMAH",
                "sub": "Moral Activism, Civilizational Leadership & Cosmic Dignity",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Dedicated Vanguard of Public Reform",
                        "bullets": [
                            "'Let there arise from you a nation inviting to good and enjoining right.'",
                            "An institutional core dedicated to spiritual education and social justice.",
                            "Civilizations rot from within when moral accountability is abandoned."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Definition of Khayra Ummah: Best Nation",
                        "bullets": [
                            "'You are the best nation brought forth for mankind.'",
                            "Superiority is not genetic or tribal; it exists purely as functional service.",
                            "Enjoining what is right, forbidding evil, and uncompromising faith in Allah."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Moral Activism on Behalf of All Humanity",
                        "bullets": [
                            "'Ukhrijat lin-Nas': Brought forth outwardly for the benefit of all humanity.",
                            "The community exists not for inward tribal enrichment, but universal blessing.",
                            "Rescuing humanity from tyranny, exploitation, and spiritual blindness."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Luminous Faces vs. Darkened Faces on the Day",
                        "bullets": [
                            "The Day when some faces turn radiant white with joy and others turn black.",
                            "The radiant: People of unity and Sunnah enveloped in eternal divine mercy.",
                            "The darkened: People of sectarian division who bartered truth for discord."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 6,
        "title": "THE CRUCIBLE OF UHUD: DISCIPLINE & DIVINE AUDIT",
        "desc": "Pillars 11 & 12: The Archers' Deviation, The Contrast of Badr, Sorrow Upon Sorrow, and The Purifying Fire",
        "sec": "PLATE 06 : CRUCIBLE OF UHUD",
        "pillars": [
            {
                "name": "PILLAR 11: ARCHERS' DEVIATION & THE LURE OF DUNYA",
                "sub": "Mount Rumah, Strategic Discipline & Exposed Desires",
                "color": "rose",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Contrast: Badr Humility vs. Uhud Complacency",
                        "bullets": [
                            "At Badr, Muslims were weak, helpless (Adhilla), relying 100% on God: Victory.",
                            "At Uhud, tactical confidence and material distraction compromised obedience.",
                            "Physical superiority means nothing without total spiritual surrender."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Sacred Order on Mount Rumah",
                        "bullets": [
                            "Fifty archers posted with absolute command: Guard our back under all odds.",
                            "Even if you see birds snatching our flesh, do not leave until ordered.",
                            "Frontline discipline is the non-negotiable safeguard of the entire body."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Catastrophic Desertion of the Post",
                        "bullets": [
                            "Enemy routed initially; forty archers rushed down to gather spoils.",
                            "Leaving only ten defenders exposed the mountain pass to enemy cavalry.",
                            "A single lapse in frontline discipline turned absolute triumph into rout."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Divine Diagnostic: Minkum Man Yureedud-Dunya",
                        "bullets": [
                            "'Among you are some who desire this world, and some who desire Hereafter.'",
                            "God lays bare the hidden motive: A tiny crack of Dunya infected the ranks.",
                            "Collective disaster often stems from internal spiritual compromise."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 12: SORROW UPON SORROW & THE PURIFYING FIRE",
                "sub": "Ghamman bi-Ghamm, The False Rumor & Purification",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "Sorrow Compounded: Ghamman bi-Ghamm",
                        "bullets": [
                            "Loss of spoils, military encirclement, 70 martyrs, and injuries to the Prophet.",
                            "Divine pedagogy: Overwhelming sorrow cures attachment to lesser worldly loss.",
                            "Pain acts as psychological cauterization, purifying the soul of trivia."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Anchored to the Message, Not the Mortal Messenger",
                        "bullets": [
                            "False rumor that the Prophet was killed shattered morale on the battlefield.",
                            "'Muhammad is but a messenger; if he dies or is killed, will you turn back?'",
                            "Faith must be anchored in the Living, Eternal Creator, not earthly presence."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Divine Surgery: Purging Hypocrisy from Ranks",
                        "bullets": [
                            "Adversity acts as divine filtration (Tamhees), separating gold from slag.",
                            "Hypocrites deserted before battle; adversity unmasks hidden traitors.",
                            "A smaller, purified community is invincible compared to a compromised crowd."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Mandate Against Despair: Wa La Tahinu",
                        "bullets": [
                            "'Do not weaken and do not grieve; you will be superior if you are believers.'",
                            "History alternates in alternating cycles (Al-Ayyam) to cultivate true patience.",
                            "Defeat in battle is not defeat in cosmic reality; true victory is steadfast faith."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 7,
        "title": "LEADERSHIP IN CRISIS & THE LIVING MARTYRS",
        "desc": "Pillars 13 & 14: Prophetic Mildness, Restorative Shura, Tawakkul, and The Emerald Birds of Paradise",
        "sec": "PLATE 07 : GOVERNANCE",
        "pillars": [
            {
                "name": "PILLAR 13: PROPHETIC MILDNESS, SHURA & TAWAKKUL",
                "sub": "Linta Lahum & The Fourfold Leadership Architecture",
                "color": "emerald",
                "cards": [
                    {
                        "num": "1",
                        "title": "Linta Lahum: Divine Mercy Manifested in Mildness",
                        "bullets": [
                            "'By mercy from Allah, you were gentle with them in the aftermath of defeat.'",
                            "Had the Prophet been harsh or hard-hearted, the community would have dispersed.",
                            "True leadership heals fractured followers rather than crushing them in blame."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Fa'fu 'Anhum & Wastaghfir Lahum: The Double Pardon",
                        "bullets": [
                            "Step 1: Pardon them personally for tactical errors and battlefield disobedience.",
                            "Step 2: Pray for their divine forgiveness before God to remove spiritual guilt.",
                            "A leader absorbs personal grief and intercedes for the moral recovery of staff."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Wa Shawirhum fil-Amr: Restoring Dignity Through Shura",
                        "bullets": [
                            "Re-engaging the very men whose advice led to catastrophe in new consultation.",
                            "Consultation restores broken dignity, rebuilding confidence and ownership.",
                            "Shura prevents autocratic bitterness and reaffirms community solidarity."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Fa-Idha 'Azamta Fa-Tawakkal: Resolute Execution",
                        "bullets": [
                            "Once a decision is resolved, move forward with absolute reliance upon Allah.",
                            "Eliminating second-guessing, paralyzing 'what-ifs', and post-hoc regret.",
                            "Total Tawakkul balances consultative wisdom with decisive moral action."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 14: THE LIVING MARTYRS & TRANQUILITY",
                "sub": "Ahya'un 'Inda Rabbihim & Serenity Amidst Chaos",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "An-Nu'as: Supernatural Slumber of Serenity",
                        "bullets": [
                            "In the thick of peril, divine peace caused sincere believers to nod in sleep.",
                            "Swords slipped from hands in miraculous calm; psychological sign of faith.",
                            "Divine tranquility descends precisely when worldly terror peaks."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Torment of Jahiliyyah Suspicion",
                        "bullets": [
                            "In contrast, hypocrites stayed awake, sweating in self-absorbed anxiety.",
                            "Thinking thoughts of Jahiliyyah: 'Had we a say, we would not have been killed.'",
                            "Lack of faith traps the soul in paranoid dread and bitter self-pity."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Bal Ahya'un: Transcendent Reality of Martyrs",
                        "bullets": [
                            "'Do not think of those killed in the path of Allah as dead.'",
                            "Rather, they are alive with their Lord, receiving celestial provision.",
                            "Death in the path of truth is not termination, but graduation into real life."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Emerald Birds Beneath the Throne of God",
                        "bullets": [
                            "Authentic Hadith: Souls of martyrs inhabit green birds roaming Paradise.",
                            "Roosting in golden chandeliers suspended beneath the Divine Throne.",
                            "Begging God to return to earth solely to experience the joy of martyrdom again."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 8,
        "title": "THE ULUL-ALBAB & THE COSMOLOGICAL SEAL",
        "desc": "Pillars 15 & 16: Cosmic Contemplation, Purposeful Creation, Answered Petitions, and The Quadruple Mandate",
        "sec": "PLATE 08 : COSMIC SEAL",
        "pillars": [
            {
                "name": "PILLAR 15: COSMOLOGICAL CONTEMPLATION & INTELLECT",
                "sub": "Ulul-Albab, Night Architecture & Purposeful Creation",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Cosmic Signs for People of Intellect (Ulul-Albab)",
                        "bullets": [
                            "In the creation of heavens, earth, and alternation of night and day are signs.",
                            "The Prophet wept until his beard was soaked: 'Woe to him who reads and reflects not!'",
                            "Nature is not an inert backdrop, but a dynamic scripture shouting God's glory."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Standing, Sitting, and on Sides: Constant Dhikr",
                        "bullets": [
                            "The hallmark of the wise: Remembering Allah across all postures of life.",
                            "Scientific exploration divorced from divine remembrance produces nihilism.",
                            "The Qur'an unifies cosmic observation with deep, trembling worship."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Rabbana Ma Khalaqta Hadha Batila: Cosmic Purpose",
                        "bullets": [
                            "'Our Lord, You did not create all this in vain; Glory be to You!'",
                            "Teleological conviction: The universe is not an accidental cosmic accident.",
                            "Every celestial orbit, atomic particle, and season possesses divine purpose."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Subhanaka Faqina 'Adhaban-Nar: Moral Reflex",
                        "bullets": [
                            "True cosmological insight does not end in cold intellectual abstraction.",
                            "It triggers an immediate moral reflex: Exalt God and beg rescue from Hellfire.",
                            "Linking cosmic grandeur directly with personal moral responsibility."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 16: ANSWERED PETITIONS & FINAL MANDATE",
                "sub": "Fastajaba Lahum & The Quadruple Blueprint for Success",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "Fastajaba Lahum Rabbuhum: Divine Confirmation",
                        "bullets": [
                            "Their Lord responded: 'I will never lose the deed of any worker among you.'",
                            "Whether male or female, you are of one another in moral accountability.",
                            "Absolute spiritual equality: Every tear, sacrifice, and action is rewarded."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Expiation & Eternal Gardens Beneath Rivers",
                        "bullets": [
                            "Those who emigrated, were expelled, and harmed in God's path have sins erased.",
                            "Admitted into gardens beneath which rivers flow as reward from Allah.",
                            "Earthly displacement and battlefield sorrow culminate in eternal triumph."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Illusion of Worldly Material Dominance",
                        "bullets": [
                            "'Let not the strutting of the deniers through the lands deceive you.'",
                            "Brief worldly enjoyment (Mata'un Qaleel), then their refuge is Hell.",
                            "Warning the believers never to measure ultimate truth by temporary wealth."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Final Quadruple Mandate for Ultimate Triumph",
                        "bullets": [
                            "1. Isbiru (Endure personally)  2. Sabiru (Outvie in collective patience)",
                            "3. Rabitu (Remain steadfast at the posts)  4. Ittaqullah (Fear Allah).",
                            "The definitive seal: Internal resilience and constant Taqwa guarantee success."
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
      <div class="meta-part">[{pg["sec"]}]</div>
    </div>
    <div class="columns-grid">
      {pillars_html}
    </div>
  </div>"""

nav_buttons_html = ""
for pg in pages_data:
    active = "active" if pg["page"] == 1 else ""
    nav_buttons_html += f"""<button class="nav-btn {active}" onclick="showPage({pg["page"]})">Plate {pg["page"]:02d}: {pg["sec"].split(':')[-1].strip()}</button>\n"""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Ali-Imran — Master Mindmap | Huurs Studio</title>
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
      background-color: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
      line-height: 1.5;
      padding: 24px;
    }}
    .app-container {{
      max-width: 1440px;
      margin: 0 auto;
    }}
    header {{
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
    .brand-title {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .brand-title h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--gold);
    }}
    .brand-title span {{
      color: var(--text-muted);
      font-size: 0.9rem;
      border-left: 1px solid var(--border-muted);
      padding-left: 12px;
    }}
    .header-badges {{
      display: flex;
      gap: 12px;
      align-items: center;
    }}
    .badge {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.05em;
    }}
    .badge.emerald {{ color: var(--emerald); }}
    .badge.gold {{ color: var(--gold); }}

    /* Tab Navigation */
    .tab-nav {{
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      overflow-x: auto;
      padding-bottom: 6px;
    }}
    .nav-btn {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      padding: 10px 16px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .nav-btn:hover {{
      background: var(--navy-elevated);
      color: var(--white);
      border-color: var(--gold);
    }}
    .nav-btn.active {{
      background: var(--gold);
      color: var(--navy-deep);
      border-color: var(--gold);
      font-weight: 700;
    }}

    /* Page Container */
    .page-section {{
      display: none;
      background: var(--navy-deep);
      border-radius: 8px;
      animation: fadeIn 0.3s ease-in-out;
    }}
    .page-section.active {{
      display: block;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .section-header {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 24px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .section-header h2 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 4px;
    }}
    .section-header p {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .meta-part {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.05em;
    }}

    /* Grid Columns */
    .columns-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 900px) {{
      .columns-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .pillar-column {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    .pillar-header {{
      padding: 16px 20px;
      background: var(--navy-elevated);
      border-bottom: 1px solid var(--border-muted);
    }}
    .pillar-header.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-header.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-header.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-header.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-header.rose {{ border-top: 3px solid var(--rose); }}

    .pillar-title h3 {{
      font-size: 0.95rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      margin-bottom: 4px;
    }}
    .pillar-header.cyan .pillar-title h3 {{ color: var(--cyan); }}
    .pillar-header.gold .pillar-title h3 {{ color: var(--gold); }}
    .pillar-header.emerald .pillar-title h3 {{ color: var(--emerald); }}
    .pillar-header.purple .pillar-title h3 {{ color: var(--purple); }}
    .pillar-header.rose .pillar-title h3 {{ color: var(--rose); }}

    .pillar-title p {{
      font-size: 0.78rem;
      color: var(--text-muted);
      font-style: italic;
    }}

    .pillar-cards {{
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .info-card {{
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 14px;
    }}
    .info-card:last-child {{
      border-bottom: none;
      padding-bottom: 0;
    }}
    .card-num {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 8px;
    }}
    .card-num span {{
      color: var(--gold-light);
    }}
    .card-bullets {{
      list-style: none;
      padding-left: 0;
    }}
    .card-bullets li {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
      position: relative;
      padding-left: 16px;
      margin-bottom: 5px;
    }}
    .card-bullets li::before {{
      content: "-";
      position: absolute;
      left: 0;
      color: var(--border-muted);
    }}

    footer {{
      margin-top: 32px;
      padding-top: 16px;
      border-top: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      color: var(--text-muted);
      flex-wrap: wrap;
      gap: 8px;
    }}
    footer span.gold {{ color: var(--gold); font-weight: 600; }}
  </style>
</head>
<body>
  <div class="app-container">
    <header>
      <div class="brand-title">
        <h1>HUURS STUDIO</h1>
        <span>DEEPER THOUGHT CAMPAIGN &bull; SURAH ALI-IMRAN</span>
      </div>
      <div class="header-badges">
        <div class="badge emerald">FOUNDATION MEDIA: 41 LECTURES (13H 38M)</div>
        <div class="badge gold">8 PLATES &bull; 16 PILLARS &bull; 64 CARDS</div>
      </div>
    </header>

    <div class="tab-nav">
      {nav_buttons_html}
    </div>

    {pages_html}

    <footer>
      <div>HUURS KNOWLEDGE SYSTEMS &bull; AUTHENTIC SUNNI SOURCE DISCIPLINE &bull; READ. REFLECT. RETURN.</div>
      <div><span class="gold">SURAH ALI-IMRAN MASTER MINDMAP CARTOGRAPHY</span></div>
    </footer>
  </div>

  <script>
    function showPage(num) {{
      document.querySelectorAll('.page-section').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      
      const targetPage = document.getElementById('page' + num);
      if (targetPage) targetPage.classList.add('active');
      
      const buttons = document.querySelectorAll('.nav-btn');
      if (buttons[num - 1]) buttons[num - 1].classList.add('active');
    }}
  </script>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"HTML generated: {HTML_OUT}")

# Markdown Summary Suite
md_content = """---
id: QURAN-ALI-IMRAN-MINDMAP-001
title: "Foundation Mindmap Cartography: Surah Ali-Imran (The Family of Imran)"
version: 1.0.0
author: "Huurs Knowledge Visualization Group (AGENT-06)"
source_artifact: "01_RESEARCH/DEEPER-THOUGHT-RESEARCH-ALI-IMRAN.md"
verified_by: "Source Verification (AGENT-03) & Islamic QA (AGENT-15)"
campaign_id: "DEEPER-THOUGHT-CAMPAIGN-ALI-IMRAN-001"
date: "2026-09-12"
status: "Published Master Mindmap Suite"
orientation: "Landscape Widescreen (16:9 / 1.65:1)"
theological_certainty: "Tier-1 (Mutawatir Qur'an & Authentic Sunni Consensus)"
derivatives:
  pdf: "07_MINDMAP/ALI_IMRAN_MASTER_MINDMAP.pdf"
  html: "07_MINDMAP/ALI_IMRAN_MASTER_MINDMAP.html"
  previews:
    - "07_MINDMAP/previews/ali_imran_page-1.png"
    - "07_MINDMAP/previews/ali_imran_page-2.png"
    - "07_MINDMAP/previews/ali_imran_page-3.png"
    - "07_MINDMAP/previews/ali_imran_page-4.png"
    - "07_MINDMAP/previews/ali_imran_page-5.png"
    - "07_MINDMAP/previews/ali_imran_page-6.png"
    - "07_MINDMAP/previews/ali_imran_page-7.png"
    - "07_MINDMAP/previews/ali_imran_page-8.png"
---

# Surah Ali-Imran Master Mindmap Cartography
## The Complete 8-Plate Visual Knowledge Architecture Across 41 Foundation Audio Lectures

> **Foundation Media:** 41 Audio Lectures in `deeperthought/03_Ali-Imran/` (Duration: 13:38:01)  
> **Core Operating Philosophy:** **READ. REFLECT. RETURN.**  
> **Format:** 8-Plate Master Landscape Vector PDF (792 x 480 pt) & Interactive Widescreen Canvas  

---

## 1. Master Mindmap Architecture

Surah Ali-Imran is systematically deconstructed across eight cohesive, symmetrical landscape plates:

```text
SURAH ALI-IMRAN (13h 38m 01s &bull; 41 Lectures)
│
├── PLATE 1: EPISTEMOLOGY, REVELATION & THE PRIMORDIAL CREED
│   ├── Pillar 1: Epistemology & Rooted Scholarship (Umm al-Kitab, Mutashabihat, Rooted Scholars, Al-Hayyul-Qayyum)
│   └── Pillar 2: The Anchored Heart & Prophetic Metric (Rabbana La Tuzigh, Wahhab Grace, Metric of Love, Warning)
│
├── PLATE 2: THE FAMILY OF IMRAN & THE SANCTUARY OF MARYAM
│   ├── Pillar 3: Hannah's Vow & Maryam's Sanctuary (Divine Election, Consecrated Vow, Elevation of Female, Mihrab Miracles)
│   └── Pillar 4: Zakariyya's Petition & Yahya's Promise (Catalyst of Mihrab, Pure Lineage Du'a, Yahya's Conception, Sacred Silence)
│
├── PLATE 3: THE REALITY OF ISA & THE DECISIVE THEOLOGICAL PROOF
│   ├── Pillar 5: Creation from Dust: Kamathali Adam (Annunciation, Miracles Bi-Idhnillah, Analogy with Adam, Kun Fa-Yakun)
│   └── Pillar 6: Disciples, Ascent & Mubahalah (Hawariyyun Helpers, Heavenly Rescue, Mubahalah Challenge, Najran Retreat)
│
├── PLATE 4: THE SCRIPTURAL DIALOGUE & THE IBRAHIMIC STANDARD
│   ├── Pillar 7: The Equitable Word & Ibrahim (Kalimatin Sawa', Exonerating Ibrahim, Hanifan Musliman, Spiritual Heirs)
│   └── Pillar 8: Prophetic Covenant & Peak Charity (Mithaq al-Nabiyyeen, Accepted Deen, Lan Tanalul-Birr, Abu Talha's Garden)
│
├── PLATE 5: THE GOLDEN ANCHOR OF UNITY & THE BEST NATION
│   ├── Pillar 9: Holding the Rope of Allah (Ittaqu Allaha, Hablillah Cable, Aws & Khazraj Reconciliation, Sectarian Ruin)
│   └── Pillar 10: Universal Mandate: Khayra Ummah (Vanguard of Reform, Defining the Best Nation, Moral Activism, Two Faces)
│
├── PLATE 6: THE CRUCIBLE OF UHUD: DISCIPLINE & DIVINE AUDIT
│   ├── Pillar 11: Archers' Deviation & The Lure of Dunya (Badr vs Uhud, Mount Rumah Order, Desertion, Minkum Man Yureedud-Dunya)
│   └── Pillar 12: Sorrow Upon Sorrow & The Purifying Fire (Ghamman bi-Ghamm, Message vs Messenger, Hypocrisy Purged, Wa La Tahinu)
│
├── PLATE 7: LEADERSHIP IN CRISIS & THE LIVING MARTYRS
│   ├── Pillar 13: Prophetic Mildness, Shura & Tawakkul (Linta Lahum, Double Pardon, Shura Restoration, Resolute Tawakkul)
│   └── Pillar 14: The Living Martyrs & Tranquility (An-Nu'as Slumber, Jahiliyyah Panic, Bal Ahya'un, Emerald Birds)
│
└── PLATE 8: THE ULUL-ALBAB & THE COSMOLOGICAL SEAL
    ├── Pillar 15: Cosmological Contemplation & Intellect (Signs of Day & Night, Constant Dhikr, Purposeful Cosmos, Moral Reflex)
    └── Pillar 16: Answered Petitions & Final Mandate (Fastajaba Confirmation, Expiation & Gardens, Worldly Illusion, Quadruple Mandate)
```

---

## 2. Deliverables Summary

* **Vector PDF:** [`07_MINDMAP/ALI_IMRAN_MASTER_MINDMAP.pdf`](file:///mnt/AI/ag/Campaign/07_MINDMAP/ALI_IMRAN_MASTER_MINDMAP.pdf)
* **Interactive HTML Canvas:** [`07_MINDMAP/ALI_IMRAN_MASTER_MINDMAP.html`](file:///mnt/AI/ag/Campaign/07_MINDMAP/ALI_IMRAN_MASTER_MINDMAP.html)
* **Research Foundation:** [`01_RESEARCH/DEEPER-THOUGHT-RESEARCH-ALI-IMRAN.md`](file:///mnt/AI/ag/Campaign/01_RESEARCH/DEEPER-THOUGHT-RESEARCH-ALI-IMRAN.md)
* **Verification Report:** [`02_VERIFICATION/DEEPER-THOUGHT-VERIFY-ALI-IMRAN.md`](file:///mnt/AI/ag/Campaign/02_VERIFICATION/DEEPER-THOUGHT-VERIFY-ALI-IMRAN.md)
* **Tafsir Monograph:** [`05_TAFSIR/DEEPER-THOUGHT-SUNNI-TAFSIR-ALI-IMRAN.md`](file:///mnt/AI/ag/Campaign/05_TAFSIR/DEEPER-THOUGHT-SUNNI-TAFSIR-ALI-IMRAN.md)
* **Tadabbur Monograph:** [`06_TADABBUR/DEEPER-THOUGHT-TADABBUR-ALI-IMRAN.md`](file:///mnt/AI/ag/Campaign/06_TADABBUR/DEEPER-THOUGHT-TADABBUR-ALI-IMRAN.md)
"""

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"MD generated: {MD_OUT}")
