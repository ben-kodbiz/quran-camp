#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Nisa Master Mindmap HTML & Markdown Generator
8 Landscape Plates &bull; 16 Thematic Pillars &bull; 64 Detailed Analytical Cards
"""

import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "AN_NISA_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "AN_NISA_MASTER_MINDMAP.md")

pages_data = [
    {
        "page": 1,
        "title": "THE PRIMORDIAL ORIGIN & INHERITANCE BOUNDARIES",
        "desc": "Pillars 1 & 2: Nafsin Wahidah, Sacred Arham, Protection of Orphan Wealth, and Hududullah Fara'id",
        "sec": "PLATE 01 : ORIGIN & INHERITANCE",
        "pillars": [
            {
                "name": "PILLAR 1: NAFSIN WAHIDAH & SACRED WOMBS",
                "sub": "Ontological Origin, Kinship & Orphan Sanctuary",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Nafsin Wahidah: Ontological Human Equality",
                        "bullets": [
                            "Humanity created from a single primordial soul; shared ontological root.",
                            "Male and female share identical moral dignity and accountability before God.",
                            "Dismantles patriarchal elitism and racial hierarchy at the source."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Taqwa of the Wombs (Al-Arham)",
                        "bullets": [
                            "Fear of Allah coupled directly with reverencing the ties of kinship (Arham).",
                            "Maternal sanctuary and uterine bonds elevated to supreme religious piety.",
                            "Severe warning against severing family ties or abandoning dependents."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Sacred Trust of Orphan Wealth",
                        "bullets": [
                            "Prohibits substituting worthless goods for the valuable assets of orphans.",
                            "Swallowing orphan property is described as stuffing blazing fire into bellies.",
                            "Society's moral legitimacy depends on protecting minors lacking legal power."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Polygyny as Social Welfare Mechanism",
                        "bullets": [
                            "Revealed post-Uhud to provide honorable shelter for widows and orphan girls.",
                            "Conditioned upon absolute financial and emotional equity among wives.",
                            "'If you fear that you cannot deal equitably, then marry only one.'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 2: THE DIVINE INHERITANCE STATUTES",
                "sub": "Fara'id Shares, Economic Dignity & Hududullah",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "Female Economic Agency & Bridal Gifts (Saduqat)",
                        "bullets": [
                            "Bridal gift (Saduqat) is a mandatory unconditional gift (Nihlah) to the woman.",
                            "It belongs solely to the female recipient; male guardians cannot seize a dime.",
                            "Establishes complete financial independence of women in Islamic jurisprudence."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Mandatory Shares for Female Heirs",
                        "bullets": [
                            "Abolishes pre-Islamic custom where women and young minors inherited nothing.",
                            "Mothers, daughters, sisters, and wives assigned fixed mathematical shares.",
                            "Wealth circulation decentralized across immediate and extended families."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Mathematical Balance of Fara'id",
                        "bullets": [
                            "Precise fractions (1/2, 1/3, 1/4, 1/6, 1/8) decreed directly by divine wisdom.",
                            "Balances hereditary inheritance shares with legally mandated financial burdens.",
                            "Eradicates testamentary tyranny and bitter family inheritance disputes."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Hududullah: The Immutable Divine Boundaries",
                        "bullets": [
                            "Inheritance shares explicitly designated as the sacred boundaries of Allah.",
                            "Those who obey enter gardens beneath which rivers flow forever.",
                            "Those who violate or alter these boundaries face agonizing eternal humiliation."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 2,
        "title": "MARITAL EQUITY, ECONOMIC CONTRACTS & DOMESTIC PEACE",
        "desc": "Pillars 3 & 4: Eradicating Forced Marriage, 'Ashiroohunna bil-Ma'roof, Qiwamah, and The Two Arbiters",
        "sec": "PLATE 02 : MARITAL EQUITY",
        "pillars": [
            {
                "name": "PILLAR 3: HONORABLE COMPANIONSHIP & BOUNDS",
                "sub": "Emancipating Widows & Sacred Forbidden Ties",
                "color": "emerald",
                "cards": [
                    {
                        "num": "1",
                        "title": "Abolition of Inheriting Women by Force",
                        "bullets": [
                            "'It is not lawful for you to inherit women against their will.'",
                            "Eradicated the pagan practice of claiming deceased relatives' wives as property.",
                            "Women granted total legal sovereignty to marry or live as they choose."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "'Ashiroohunna bil-Ma'roof: Principled Kindness",
                        "bullets": [
                            "Living with wives in honorable kindness regardless of fluctuating emotions.",
                            "'For if you dislike them, perhaps you dislike something Allah made greatly good.'",
                            "Demands moral character and patience during marital friction and hardship."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Meethaqan Ghaleedha: The Weighty Covenant",
                        "bullets": [
                            "Marriage designated with the supreme title of a heavy, solemn covenant.",
                            "Forbids taking back paid dowries even if a treasure (Qintar) was given.",
                            "Protects women's financial assets from vindictive post-divorce reclaiming."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Prohibited Bounds of Marriage (Al-Muharramat)",
                        "bullets": [
                            "Precise legal classification of unlawful marriages (mothers, daughters, sisters).",
                            "Includes fosterage (milk-kinship) and marrying two sisters simultaneously.",
                            "Establishes the sanctity of family boundaries and prevents genetic corruption."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 4: QIWAMAH & ARBITRATION PROTOCOLS",
                "sub": "Protective Guardianship & Marital Conflict Resolution",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Commercial Ethics: Free Consent (Tijaratan 'an Taradin)",
                        "bullets": [
                            "Consuming wealth unjustly through fraud, usury, or coercion is forbidden.",
                            "Economic transactions require genuine mutual consent of contracting parties.",
                            "'And do not kill yourselves; indeed, Allah is ever Merciful to you.'"
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Qiwamah as Protective Custodianship",
                        "bullets": [
                            "Men appointed as caretakers (Qawwamoon) based on divine duty to spend wealth.",
                            "Qiwamah represents protective maintenance and defense, not patriarchal ego.",
                            "A man who fails his financial and moral duty violates the terms of Qiwamah."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "De-escalating Domestic Strife (Nushuz)",
                        "bullets": [
                            "Three-stage graduated intervention for marital rebellion: Admonition first.",
                            "Followed by separation of sleeping quarters to encourage cool reflection.",
                            "If partners return to harmony, seeking further grievance is strictly forbidden."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Two Arbiters (Hakamayn) Protocol",
                        "bullets": [
                            "Convening trusted mediators from his family and hers before divorce proceeds.",
                            "'If both arbiters desire reconciliation, Allah will cause harmony between them.'",
                            "Institutionalizes external family diplomacy to save marriages from dissolution."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 3,
        "title": "THE DECALOGUE OF COMPASSION & DIVINE GOVERNANCE",
        "desc": "Pillars 5 & 6: The Ten Concentric Rings of Ihsan, Rendering Trusts, and The Constitutional Hierarchy of Authority",
        "sec": "PLATE 03 : GOVERNANCE & RIGHTS",
        "pillars": [
            {
                "name": "PILLAR 5: THE TEN PILLARS OF COMPASSION",
                "sub": "Concentric Circles of Mercy & Dismantling Arrogance",
                "color": "purple",
                "cards": [
                    {
                        "num": "1",
                        "title": "Monotheism Anchoring the Social Decalogue",
                        "bullets": [
                            "'Worship Allah and associate nothing with Him' opens the social charter.",
                            "Shunning the boastful, arrogant soul; humility before God produces mercy.",
                            "Social justice is not secular policy, but an act of direct worship."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Immediate Circle: Parents, Relatives & Orphans",
                        "bullets": [
                            "Unconditional excellence (Ihsan) to mother and father as first social duty.",
                            "Sustaining kin ties and sheltering vulnerable orphans and the poor.",
                            "Family preservation forms the core foundation of a healthy civil order."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Expanding Sphere: Near & Far Neighbors",
                        "bullets": [
                            "Duty extends to the immediate neighbor and the stranger/distant neighbor.",
                            "Honoring the companion at your side (work colleagues, traveling partners).",
                            "Eradicating social alienation through continuous daily neighborhood care."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Wayfarer & Domestic Subordinates",
                        "bullets": [
                            "Welcoming traveling strangers and protecting domestic workers and servants.",
                            "Condemning those who are stingy and hoard God's favors from the weak.",
                            "A society is judged by how it treats its most powerless and transient guests."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 6: RENDERING TRUSTS & HIERARCHY OF LAW",
                "sub": "Amanat Custodianship & The Constitutional Order",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "Rendering Trusts (Amanat) to Their Rightful Owners",
                        "bullets": [
                            "'Allah commands you to render trusts to those to whom they are due.'",
                            "Key of the Ka'bah returned to Uthman ibn Talha, establishing meritocracy.",
                            "Public office and judicial authority are sacred trusts, not political spoils."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Impartial Judicial Decree: In Tahkumu bil-'Adl",
                        "bullets": [
                            "'And when you judge between people, judge with absolute justice.'",
                            "The command applies to all mankind ('Bayan an-Nas'), not only Muslims.",
                            "Judicial objectivity is immune to racial, sectarian, or national bias."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Constitutional Chain of Authority (Ayah 59)",
                        "bullets": [
                            "1. Obey Allah (Qur'an)  2. Obey the Messenger (Sunnah)  3. Uli al-Amr.",
                            "Disputed state matters must be referred back to Allah and the Messenger.",
                            "Obedience to human rulers is never absolute; it is conditional on revelation."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Inner Submission to Prophetic Verdict (Ayah 65)",
                        "bullets": [
                            "'No, by your Lord, they do not believe until they make you judge in disputes.'",
                            "Demands complete eradication of internal resentment (Haraj) against verdicts.",
                            "Sincere faith culminates in joyful surrender (Yusallimoo Tasleema)."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 4,
        "title": "SACRED DEFENSE, OPPRESSED CRIES & DIVINE DECREE",
        "desc": "Pillars 7 & 8: Rescuing the Mustad'afeen, Tactical Vigilance, Inevitable Mortality, and Tadabbur of Scripture",
        "sec": "PLATE 04 : SACRED DEFENSE",
        "pillars": [
            {
                "name": "PILLAR 7: RESCUING THE OPPRESSED",
                "sub": "Humanitarian Liberation & Tactical Preparedness",
                "color": "rose",
                "cards": [
                    {
                        "num": "1",
                        "title": "Tactical Vigilance: Khudhu Hidhrakum",
                        "bullets": [
                            "Believers commanded to maintain tactical alertness and situational security.",
                            "Advancing in prepared detachments (Thubatin) or as a unified collective force.",
                            "Faith in divine protection never excuses operational negligence."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Warfare as Humanitarian Liberation (Ayah 75)",
                        "bullets": [
                            "'Why do you not fight in Allah's cause and for the oppressed (Mustad'afeen)?'",
                            "Children, women, and the elderly weeping for rescue from tyrannical cities.",
                            "Islamic combat is defined not by conquest, but by breaking the chains of tyrants."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Combat of Faith vs. The Way of Taghut",
                        "bullets": [
                            "The sincere fight in the path of Allah to establish truth and end persecution.",
                            "The corrupt fight in the path of Taghut (tyranny, greed, and idolatry).",
                            "'Fight the allies of Satan; indeed, Satan's plot is inherently frail.'"
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Inescapable Hour in Fortified Towers",
                        "bullets": [
                            "'Wherever you may be, death will find you, even if in towering fortresses.'",
                            "Cowardice cannot postpone death, and courageous defense cannot hasten it.",
                            "Liberating the human mind from existential dread and paralyzing fear."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 8: TADABBUR & ETHICAL ENGAGEMENT",
                "sub": "Scriptural Harmony, Mediation & Restraint",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Afala Yatadabbaroon: The Proof of Harmony (Ayah 82)",
                        "bullets": [
                            "'Do they not contemplate the Qur'an with deep reflective intellect?'",
                            "Had it been from other than Allah, they would find much contradiction in it.",
                            "Internal structural perfection over 23 years confirms divine revelation."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Shafa'ah Hasanah: Moral Complicity",
                        "bullets": [
                            "Whoever intercedes for a righteous cause shares in its eternal reward.",
                            "Whoever intercedes for an evil cause bears full spiritual liability for it.",
                            "Words and political endorsements carry heavy eschatological weight."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Returning the Greeting of Peace with Excellence",
                        "bullets": [
                            "'When greeted with a greeting, greet with one better or return it equally.'",
                            "Elevating everyday social interaction into an arena of intentional goodwill.",
                            "Fostering mutual warmth and peace within the collective civic sphere."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Dealing with Neutral Factions & Covenants",
                        "bullets": [
                            "Those who join allies with a treaty, or come reluctant to fight you, are spared.",
                            "If they withdraw, refrain from combat, and offer peace, war is forbidden.",
                            "War is restricted strictly to active combatants who persecute faith."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 5,
        "title": "SANCTITY OF BLOOD, INVESTIGATION & COMBAT PRAYER",
        "desc": "Pillars 9 & 10: Inviolability of Muslim Life, The Duty of Fatabayyanoo, Hijrah, and Salat al-Khawf",
        "sec": "PLATE 05 : SANCTITY OF LIFE",
        "pillars": [
            {
                "name": "PILLAR 9: INVIOLABILITY OF LIFE & VERIFICATION",
                "sub": "Blood Penalties, Fatabayyanoo & Spiritual Migration",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Inviolability of Believing Life & Homicide Law",
                        "bullets": [
                            "Accidental killing requires freeing a believing slave and blood-money (Diyah).",
                            "Deliberate killing of a believer punished with Hell, divine curse, and wrath.",
                            "Establishing the absolute sanctity of human life as an inviolable boundary."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Fatabayyanoo: Mandatory Verification Before Action",
                        "bullets": [
                            "'When you go forth in Allah's cause, investigate (*Fatabayyanoo*) thoroughly.'",
                            "Never say to one who offers peace 'You are not a believer' to seize cattle.",
                            "The Prophet severely reprimanded Usamah for slaying one who uttered Tawhid."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Hierarchy of Striving vs. Passive Inaction",
                        "bullets": [
                            "Believers who sit back without physical excuse are not equal to active strivers.",
                            "Striving with wealth and life elevated by immense ranks, mercy, and forgiveness.",
                            "Honor in the divine sight belongs to proactive sacrifice, not passive comfort."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Hijrah: Escaping Spiritual Oppression",
                        "bullets": [
                            "Angels question dying souls: 'Were you not oppressed? Was not earth spacious?'",
                            "Enduring compromise under tyranny is condemned when migration is possible.",
                            "Migration to preserve faith guarantees expansive refuge and abundant provision."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 10: SALAT AL-KHAWF & PRAYER TIMINGS",
                "sub": "Combat Worship Architecture & Timeless Fixed Statutes",
                "color": "emerald",
                "cards": [
                    {
                        "num": "1",
                        "title": "Qasr: Divine Leniency in Shortening Prayer",
                        "bullets": [
                            "When traveling through the earth, shortening four-unit prayer is permitted.",
                            "Especially ordained during times of fear or impending enemy engagement.",
                            "Divine legislation provides merciful adaptability without compromising duty."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Salat al-Khawf: Corporate Worship Under Fire",
                        "bullets": [
                            "The army divides into two shifts: One party prays while holding weapons.",
                            "The second party guards against surprise enemy encirclement, then alternates.",
                            "Even in the roar of battle, congregational prayer cannot be abandoned."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Post-Combat Dhikr: Constant Mindful Presence",
                        "bullets": [
                            "'When you finish prayer, remember Allah standing, sitting, and on your sides.'",
                            "Deep psychological grounding to heal trauma and adrenaline after combat.",
                            "Re-connecting the soldier's heart to eternal peace through divine praise."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Kitaban Mawqoota: The Fixed Timings of Prayer",
                        "bullets": [
                            "'Indeed, prayer has been decreed upon the believers at specified times.'",
                            "Re-establishing normal full prayer once physical security is restored.",
                            "The 5 daily appointments are an unbending spiritual anchor across life."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 6,
        "title": "ABSOLUTE JUSTICE, TREASON & COMBATING SHIRK",
        "desc": "Pillars 11 & 12: The Trial of Tu'mah, Condemnation of Deceit, Rebutting Satan, and Qawwameena bil-Qist",
        "sec": "PLATE 06 : ABSOLUTE JUSTICE",
        "pillars": [
            {
                "name": "PILLAR 11: JUDICIAL INTEGRITY & TU'MAH'S TRIAL",
                "sub": "Exonerating the Innocent & Exposing Tribal Collusion",
                "color": "rose",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Trial of Tu'mah ibn Ubayriq",
                        "bullets": [
                            "A nominal Muslim stole armor and hid it with an innocent Jewish citizen.",
                            "Tu'mah's clan pressured the Prophet to defend him to protect Muslim pride.",
                            "Revelation descended from seven heavens exposing the Muslim and clearing the Jew."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Wa La Takun lil-Kha'ineena Khaseema",
                        "bullets": [
                            "'And do not plead on behalf of the deceitful and treacherous.'",
                            "Severe divine reprimand: God's Prophet cannot be used as an advocate for fraud.",
                            "Establishes that truth and innocence transcend religious and tribal identity."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Ethics of Secret Counsel (Najwa)",
                        "bullets": [
                            "'No good is there in much of their private whispers (Najwa).'",
                            "Permitted only when commanding charity, virtue, or reconciliation.",
                            "Condemns covert factional plotting, political gossip, and conspiracies."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Slander and Moral Guilt: Buhtanan wa Ithman",
                        "bullets": [
                            "'Whoever commits a sin and then blames an innocent person bears slander.'",
                            "Framing an innocent individual carries double guilt in the court of God.",
                            "Protecting the reputation of every citizen against malicious defamation."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 12: QAWWAMEENA BIL-QIST",
                "sub": "Unforgivable Shirk & Absolute Universal Justice",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Unpardonable Treason of Shirk",
                        "bullets": [
                            "'Indeed, Allah does not forgive that partners be associated with Him.'",
                            "He forgives anything lesser to whom He wills; Shirk is cosmic falsehood.",
                            "Associating created dust with the Uncreated Sustainer corrupts human purpose."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Satan's Deceptions: Altering the Creation",
                        "bullets": [
                            "Satan vows to misguide mankind through false hopes and superstitious rituals.",
                            "Inciting humanity to alter the physical and moral creation of Allah.",
                            "'Whoever takes Satan as an ally has suffered a manifest and total loss.'"
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Absolute Gender Equality in Salvation",
                        "bullets": [
                            "'Whoever does righteous deeds, whether male or female, while believing...'",
                            "Those will enter Paradise and not be wronged by even the speck on a date-seed.",
                            "Demolishes all patriarchal claims of preferential spiritual status."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Qawwameena bil-Qist: Absolute Justice (Ayah 135)",
                        "bullets": [
                            "'Be persistently standing firm in justice, witnesses for Allah.'",
                            "Even if against yourselves, parents, or kin; whether rich or poor.",
                            "'Follow not personal passion, lest you deviate from the truth.'"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 7,
        "title": "THE ANATOMY OF HYPOCRISY & ISA'S VINDICATION",
        "desc": "Pillars 13 & 14: Mudhbdhabeen Wavering, Ad-Dark al-Asfal, Exonerating Maryam, and Refuting Crucifixion",
        "sec": "PLATE 07 : HYPOCRISY & ISA",
        "pillars": [
            {
                "name": "PILLAR 13: THE ANATOMY OF HYPOCRISY",
                "sub": "Opportunistic Wavering & The Fourfold Path of Taubah",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Mudhbdhabeen: The Fluctuating Soul",
                        "bullets": [
                            "Hypocrites waver between belief and disbelief; belonging to neither camp.",
                            "They watch the tide: If Muslims triumph, they claim alliance; if not, they join foes.",
                            "Opportunism destroys moral integrity and leaves the soul adrift."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Sluggish Prayer & Performative Display (Riya')",
                        "bullets": [
                            "'When they stand for prayer, they stand lazily, to be seen by people.'",
                            "They remember Allah only marginally, devoid of reverence and presence.",
                            "Performing religious rituals as social performance corrupts spiritual value."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Ad-Dark al-Asfal: The Lowest Abyss of Fire",
                        "bullets": [
                            "'Indeed, the hypocrites will be in the lowest depth of the Fire.'",
                            "And never will you find for them a protector or helper against God.",
                            "Internal betrayal of truth receives harsher retribution than open denial."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Fourfold Door of Sincere Redemption",
                        "bullets": [
                            "Except those who: 1. Repent  2. Rectify wrongs  3. Hold fast to Allah",
                            "And 4. Purify their religion solely for Him; they are with sincere believers.",
                            "Divine mercy remains open even to the worst hypocrite upon true reform."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 14: EXONERATING MARYAM & REFUTING CRUCIFIXION",
                "sub": "Rebutting Slanders & The Heavenly Rescue of Isa",
                "color": "purple",
                "cards": [
                    {
                        "num": "1",
                        "title": "Rebutting Monstrous Slanders Against Maryam",
                        "bullets": [
                            "Condemning those who uttered a monstrous slander (Buhtanan 'Adheema).",
                            "Vindicating the virgin Maryam's purity, honor, and celestial election.",
                            "Slandering chaste women is condemned as an unforgivable moral crime."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The Boast of Deicide Dismantled",
                        "bullets": [
                            "Rebutting the arrogant boast: 'We killed the Messiah Isa, the messenger.'",
                            "Human beings have no power to execute the chosen Word of God.",
                            "Demolishing both Jewish boast of execution and Christian theology of deicide."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Wa Ma Qataloohu Wa Ma Salaboohu",
                        "bullets": [
                            "'They killed him not, nor did they crucify him, but so it appeared to them.'",
                            "Those who dispute regarding his fate are in doubt, following mere conjecture.",
                            "'For surely, they killed him not!' — categorical Quranic certainty."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Heavenly Ascension & Preservation of the Prophet",
                        "bullets": [
                            "'Rather, Allah raised him to Himself; Allah is ever Exalted in Might, Wise.'",
                            "Isa was spared physical crucifixion, elevated bodily to heavenly honor.",
                            "Preserved until his appointed return before the Day of Resurrection."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 8,
        "title": "THE PROPHETIC CHAIN, PROHIBITING GHULUWW & THE SEAL",
        "desc": "Pillars 15 & 16: The Cosmic Prophetic Stream, Takleem Musa, Demolishing Trinitarian Excess, and The Kalalah Seal",
        "sec": "PLATE 08 : PROPHETIC SEAL",
        "pillars": [
            {
                "name": "PILLAR 15: THE PROPHETIC CHAIN & TAKLEEM MUSA",
                "sub": "Unbroken Revelation & Direct Divine Speech",
                "color": "emerald",
                "cards": [
                    {
                        "num": "1",
                        "title": "The Cosmic Chain of Inspired Messengers",
                        "bullets": [
                            "Revelation sent to Muhammad as sent to Nuh, Ibrahim, Isma'il, Ishaq, Ya'qub.",
                            "Tribes, Isa, Ayyub, Yunus, Harun, Sulayman, and the Zabur given to Dawud.",
                            "Islam unites the entire prophetic lineage into a single divine message."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Messengers Mentioned & Unmentioned",
                        "bullets": [
                            "'Messengers We have related to you before and messengers We have not.'",
                            "Universal prophetic presence: Every civilization received divine warning.",
                            "Humility in recognizing that God's guidance transcends known historical records."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Wa Kallamallahu Musa Takleema: Direct Divine Speech",
                        "bullets": [
                            "'And to Musa Allah spoke directly with real speech (Takleema).'",
                            "Affirming the divine attribute of Kalam without metaphorical dilution.",
                            "Honoring Musa as Kalimullah who heard the speech of God at Mount Tuwa."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Messengers as Bearers of Glad Tidings & Warning",
                        "bullets": [
                            "Messengers bring glad tidings of Paradise and warning of divine punishment.",
                            "Sent so mankind will have no argument against Allah after the messengers.",
                            "God's justice is perfect: Accountability only occurs after clear warning."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 16: DEMOLISHING GHULUWW & THE KALALAH SEAL",
                "sub": "Pristine Monotheism & The Final Inheritance Charter",
                "color": "gold",
                "cards": [
                    {
                        "num": "1",
                        "title": "La Taghloo: Prohibition of Religious Extremism",
                        "bullets": [
                            "'O People of the Scripture, do not exceed limits (Ghuluww) in your religion.'",
                            "Do not speak about Allah except the absolute truth of His transcendent Tawhid.",
                            "Religious excess corrupts monotheism and deifies mortal human beings."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "The True Definition of the Messiah Isa",
                        "bullets": [
                            "'The Messiah Isa, son of Maryam, was only a messenger of Allah.'",
                            "And His Word cast into Maryam, and a Spirit created by Him (Ruhun Minhu).",
                            "Honored as a noble prophet and humble servant, never as Lord or partner."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Wa La Taqooloo Thalathah: Cease the Trinity!",
                        "bullets": [
                            "'Believe in Allah and His messengers, and do not say \"Three\"!'",
                            "'Cease! It is better for you. Indeed, Allah is but one God.'",
                            "Exalted is He above having a son; to Him belongs whatever is in creation."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Statutory Seal: Kalalah (Ayah 176)",
                        "bullets": [
                            "Final verse codifying inheritance for individuals without parents or children.",
                            "Shares for brothers and sisters precisely established to prevent family ruin.",
                            "Surah concludes as it began: Safeguarding the property and rights of the weak."
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
  <title>Surah An-Nisa — Master Mindmap | Huurs Studio</title>
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
        <span>DEEPER THOUGHT CAMPAIGN &bull; SURAH AN-NISA</span>
      </div>
      <div class="header-badges">
        <div class="badge emerald">FOUNDATION MEDIA: 29 LECTURES (10H 13M)</div>
        <div class="badge gold">8 PLATES &bull; 16 PILLARS &bull; 64 CARDS</div>
      </div>
    </header>

    <div class="tab-nav">
      {nav_buttons_html}
    </div>

    {pages_html}

    <footer>
      <div>HUURS KNOWLEDGE SYSTEMS &bull; AUTHENTIC SUNNI SOURCE DISCIPLINE &bull; READ. REFLECT. RETURN.</div>
      <div><span class="gold">SURAH AN-NISA MASTER MINDMAP CARTOGRAPHY</span></div>
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
id: QURAN-AN-NISA-MINDMAP-001
title: "Foundation Mindmap Cartography: Surah An-Nisa (The Women)"
version: 1.0.0
author: "Huurs Knowledge Visualization Group (AGENT-06)"
source_artifact: "01_RESEARCH/DEEPER-THOUGHT-RESEARCH-AN-NISA.md"
verified_by: "Source Verification (AGENT-03) & Islamic QA (AGENT-15)"
campaign_id: "DEEPER-THOUGHT-CAMPAIGN-AN-NISA-001"
date: "2026-09-12"
status: "Published Master Mindmap Suite"
orientation: "Landscape Widescreen (16:9 / 1.65:1)"
theological_certainty: "Tier-1 (Mutawatir Qur'an & Authentic Sunni Consensus)"
derivatives:
  pdf: "07_MINDMAP/AN_NISA_MASTER_MINDMAP.pdf"
  html: "07_MINDMAP/AN_NISA_MASTER_MINDMAP.html"
  previews:
    - "07_MINDMAP/previews/an_nisa_page-1.png"
    - "07_MINDMAP/previews/an_nisa_page-2.png"
    - "07_MINDMAP/previews/an_nisa_page-3.png"
    - "07_MINDMAP/previews/an_nisa_page-4.png"
    - "07_MINDMAP/previews/an_nisa_page-5.png"
    - "07_MINDMAP/previews/an_nisa_page-6.png"
    - "07_MINDMAP/previews/an_nisa_page-7.png"
    - "07_MINDMAP/previews/an_nisa_page-8.png"
---

# Surah An-Nisa Master Mindmap Cartography
## The Complete 8-Plate Visual Knowledge Architecture Across 29 Foundation Audio Lectures

> **Foundation Media:** 29 Audio Lectures in `deeperthought/04_An-Nisa/` (Duration: 10:13:44)  
> **Core Operating Philosophy:** **READ. REFLECT. RETURN.**  
> **Format:** 8-Plate Master Landscape Vector PDF (792 x 480 pt) & Interactive Widescreen Canvas  

---

## 1. Master Mindmap Architecture

Surah An-Nisa is systematically deconstructed across eight cohesive, symmetrical landscape plates:

```text
SURAH AN-NISA (10h 13m 44s &bull; 29 Lectures)
│
├── PLATE 1: THE PRIMORDIAL ORIGIN & INHERITANCE BOUNDARIES
│   ├── Pillar 1: Nafsin Wahidah & Sacred Wombs (Single Soul Origin, Arham Kinship, Orphan Property, Polygyny Welfare)
│   └── Pillar 2: The Divine Inheritance Statutes (Female Economic Agency, Mandatory Shares, Mathematical Balance, Hududullah)
│
├── PLATE 2: MARITAL EQUITY, ECONOMIC CONTRACTS & DOMESTIC PEACE
│   ├── Pillar 3: Honorable Companionship & Bounds (Widow Emancipation, 'Ashiroohunna bil-Ma'roof, Heavy Covenant, Forbidden Bounds)
│   └── Pillar 4: Qiwamah & Arbitration Protocols (Mutual Consent Trade, Protective Qiwamah, Conflict De-escalation, Two Arbiters)
│
├── PLATE 3: THE DECALOGUE OF COMPASSION & DIVINE GOVERNANCE
│   ├── Pillar 5: The Ten Pillars of Compassion (Tawhid & Social Duty, Parents & Kin, Near/Far Neighbors, Servants/Wayfarers)
│   └── Pillar 6: Rendering Trusts & Hierarchy of Law (Amanat to Owners, Impartial Judgment, Ayah 59 Chain, Prophetic Arbitration)
│
├── PLATE 4: SACRED DEFENSE, OPPRESSED CRIES & DIVINE DECREE
│   ├── Pillar 7: Rescuing the Oppressed (Tactical Caution, Liberating Mustad'afeen, Allah vs Taghut, Inescapable Death)
│   └── Pillar 8: Tadabbur & Ethical Engagement (Contemplation of Harmony, Shafa'ah Hasanah, Greeting Peace, Neutral Treaties)
│
├── PLATE 5: SANCTITY OF BLOOD, INVESTIGATION & COMBAT PRAYER
│   ├── Pillar 9: Inviolability of Life & Verification (Homicide Law, Fatabayyanoo Duty, Striving vs Passivity, Spiritual Hijrah)
│   └── Pillar 10: Salat al-Khawf & Prayer Timings (Qasr Leniency, Divided Shifts in Battle, Post-Combat Dhikr, Kitaban Mawqoota)
│
├── PLATE 6: ABSOLUTE JUSTICE, TREASON & COMBATING SHIRK
│   ├── Pillar 11: Judicial Integrity & Tu'mah's Trial (Tu'mah Incident, No Defense for Deceit, Secret Whispering, Slander Guilt)
│   └── Pillar 12: Qawwameena bil-Qist (Unforgivable Shirk, Satan's Creation Alteration, Gender Equality in Deeds, Ayah 135 Witness)
│
├── PLATE 7: THE ANATOMY OF HYPOCRISY & ISA'S VINDICATION
│   ├── Pillar 13: The Anatomy of Hypocrisy (Mudhbdhabeen Wavering, Sluggish Prayer, Ad-Dark al-Asfal Abyss, Fourfold Taubah Door)
│   └── Pillar 14: Exonerating Maryam & Refuting Crucifixion (Rebutting Slanders, Deicide Boast Broken, Wa Ma Qataloohu, Ascension)
│
└── PLATE 8: THE PROPHETIC CHAIN, PROHIBITING GHULUWW & THE SEAL
    ├── Pillar 15: The Prophetic Chain & Takleem Musa (Cosmic Chain of Messengers, Mentioned/Unmentioned, Direct Speech Musa, Warnings)
    └── Pillar 16: Demolishing Ghuluww & The Kalalah Seal (Prohibiting Excess, Isa as Word/Spirit, Cease Trinity, Kalalah Statute)
```

---

## 2. Deliverables Summary

* **Vector PDF:** [`07_MINDMAP/AN_NISA_MASTER_MINDMAP.pdf`](file:///mnt/AI/ag/Campaign/07_MINDMAP/AN_NISA_MASTER_MINDMAP.pdf)
* **Interactive HTML Canvas:** [`07_MINDMAP/AN_NISA_MASTER_MINDMAP.html`](file:///mnt/AI/ag/Campaign/07_MINDMAP/AN_NISA_MASTER_MINDMAP.html)
* **Primary Research Dossier:** [`01_RESEARCH/DEEPER-THOUGHT-RESEARCH-AN-NISA.md`](file:///mnt/AI/ag/Campaign/01_RESEARCH/DEEPER-THOUGHT-RESEARCH-AN-NISA.md)
* **Verification Report:** [`02_VERIFICATION/DEEPER-THOUGHT-VERIFY-AN-NISA.md`](file:///mnt/AI/ag/Campaign/02_VERIFICATION/DEEPER-THOUGHT-VERIFY-AN-NISA.md)
* **Tafsir Monograph:** [`05_TAFSIR/DEEPER-THOUGHT-SUNNI-TAFSIR-AN-NISA.md`](file:///mnt/AI/ag/Campaign/05_TAFSIR/DEEPER-THOUGHT-SUNNI-TAFSIR-AN-NISA.md)
* **Tadabbur Monograph:** [`06_TADABBUR/DEEPER-THOUGHT-TADABBUR-AN-NISA.md`](file:///mnt/AI/ag/Campaign/06_TADABBUR/DEEPER-THOUGHT-TADABBUR-AN-NISA.md)
"""

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"MD generated: {MD_OUT}")
