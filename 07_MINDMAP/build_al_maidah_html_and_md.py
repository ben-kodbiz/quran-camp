#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Ma'idah Master Mindmap HTML & Markdown Generator
8 Landscape Plates &bull; 16 Thematic Pillars &bull; 64 Detailed Analytical Cards
"""

import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "AL_MAIDAH_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "AL_MAIDAH_MASTER_MINDMAP.md")

pages_data = [
    {
        "page": 1,
        "title": "THE INVIOLABILITY OF COVENANTS & SACRED BOUNDARIES",
        "desc": "Pillars 1 & 2: Awfoo bil-'Uqud, Completion of Deen, Ritual Taharah & Objective Justice Toward Antagonists",
        "sec": "PLATE 01 : COVENANTS & PURITY",
        "pillars": [
            {
                "name": "PILLAR 1: AWFOO BIL-'UQUD & HALAL PROVISIONS",
                "sub": "Supreme Contractual Mandate, Sacramental Boundaries & Wholesome Diet",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Awfoo bil-'Uqud: Supreme Contractual Mandate",
                        "bullets": [
                            "Uncompromising divine injunction to honor all covenants, pacts, and contracts.",
                            "Encompasses vertical oaths with Allah, civil treaties, and commercial agreements.",
                            "Foundational legal maxim: Binding force of contracts is the primary Islamic default."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Sanctity of Sacred Symbols (Sha'a'irullah)",
                        "bullets": [
                            "Reverence commanded for sacred precincts, pilgrimage signs, and sacrificial offerings.",
                            "Severe prohibition against desecrating sacred months or hindering pilgrims.",
                            "Righteous cooperation mandate: Co-operate in Birr and Taqwa, never in sin."
                        ]
                    },
                    {
                        "num": "3",
                        "title": "The Completion of Deen: Al-Yawma Akmaltu Lakum",
                        "bullets": [
                            "Revealed on the Day of Arafah during Farewell Pilgrimage sealing prophetic legislation.",
                            "Islam declared jurisprudentially complete and perfected; zero legislative innovation.",
                            "Divine self-sufficiency: Guidance is fully realized, leaving no moral ambiguity."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "Wholesome Provisions (At-Tayyibat) & Trained Hunt",
                        "bullets": [
                            "Decisive dietary boundary: Maytah, flowing blood, swine, and unslaughtered beasts forbidden.",
                            "Lawful utilization of trained hunting animals (Jawarih) mentioning Allah's name.",
                            "Food of the People of the Book made permissible, expanding civil interaction."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 2: PURIFICATION & OBJECTIVE EQUITY",
                "sub": "Bodily Sanctity, Hearing-Obeying & Justice Beyond Enmity",
                "color": "purple",
                "cards": [
                    {
                        "num": "5",
                        "title": "Structural Purification: Wudu, Ghusl & Tayammum",
                        "bullets": [
                            "Comprehensive hygiene protocol: Washing face, arms, wiping head, washing feet.",
                            "Divine facilitation of Tayammum using clean earth when water is absent.",
                            "Spiritual purpose revealed: Allah intends purity and completion of favor, not hardship."
                        ]
                    },
                    {
                        "num": "6",
                        "title": "The Primordial Pledge: Sami'na wa Ata'na",
                        "bullets": [
                            "Remembering the divine favor and solemn pledge taken with the Messenger of Allah.",
                            "Unconditional submission: We have heard and we have obeyed in public and private.",
                            "Continuous Taqwa reminder: Allah is fully aware of all secrets within human chests."
                        ]
                    },
                    {
                        "num": "7",
                        "title": "Objective Equity: I'diloo Huwa Aqrabu lit-Taqwa",
                        "bullets": [
                            "Persistent establishment of divine equity: Standing as truthful witnesses for Allah.",
                            "Transcendent legal maxim: Justice is the closest practical manifestation of Taqwa.",
                            "Impartiality enforced: Favoritism and subjective bias strictly excised from judgment."
                        ]
                    },
                    {
                        "num": "8",
                        "title": "Enmity Transcended: Justice Toward Antagonists",
                        "bullets": [
                            "Hatred of a hostile people must never induce believers to commit legal injustice.",
                            "Enemies entitled to absolute fairness in judicial rulings, treaties, and testimony.",
                            "Supreme standard of Islamic statecraft: Ethical righteousness outranks resentment."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 2,
        "title": "HISTORICAL COVENANTS & THE SANCTITY OF LIFE",
        "desc": "Pillars 3 & 4: The Twelve Chieftains, Broken Pacts, Fratricide of Habil/Qabil & Cosmic Sanctity of Existence",
        "sec": "PLATE 02 : PACTS & SANCTITY OF LIFE",
        "pillars": [
            {
                "name": "PILLAR 3: THE BROKEN PACTS OF BANI ISRA'IL",
                "sub": "Twelve Chieftains, Hardened Hearts & Wilderness Cowardice",
                "color": "emerald",
                "cards": [
                    {
                        "num": "9",
                        "title": "The Twelve Chieftains (Ithnay 'Ashara Naqeeba)",
                        "bullets": [
                            "God commissioned twelve leaders to govern the twelve tribes under divine covenant.",
                            "Covenant conditions: Establishing prayer, giving zakah, honoring messengers, loaning to God.",
                            "Historical archetype of collective leadership bound to divine accountability."
                        ]
                    },
                    {
                        "num": "10",
                        "title": "Hardened Hearts & Textual Distortion (Yuharrifoon)",
                        "bullets": [
                            "Breaking covenants resulted in divine curses and spiritual calcification of hearts.",
                            "Distortion of revelation: Displacing words from their rightful context and forgetting.",
                            "Treasonous betrayals encountered continuously, yet Prophetic pardon commanded."
                        ]
                    },
                    {
                        "num": "11",
                        "title": "Noorun wa Kitabun Mubeen: Pathways of Peace",
                        "bullets": [
                            "A radiant light and clear Book sent to humanity from the Divine Throne.",
                            "Guiding whoever seeks His pleasure to Subul as-Salam (pathways of inner and outer peace).",
                            "Extracting consciousness from suffocating darkness into illuminated guidance."
                        ]
                    },
                    {
                        "num": "12",
                        "title": "The Desert Wilderness: Cowardice Before Holy Land",
                        "bullets": [
                            "Command to enter Holy Land defied: 'Go, you and your Lord, and fight! We sit here!'",
                            "Two God-fearing men urge faith: 'Enter through the gate; when you enter, you will overcome.'",
                            "Forty-year wandering in wilderness (Fee al-ardi yateehoon) as consequence of rebellion."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 4: HABIL, QABIL & THE INVIOLABILITY OF LIFE",
                "sub": "Sincerity vs Envy, First Fratricide & Cosmic Value of Soul",
                "color": "gold",
                "cards": [
                    {
                        "num": "13",
                        "title": "The First Fratricide: Sincerity vs Envy",
                        "bullets": [
                            "Two sons of Adam offer sacrifice; accepted from one, rejected from the other.",
                            "Universal truth revealed: Allah accepts solely from those who possess authentic Taqwa.",
                            "Envy triggers the murderous threat: 'I will surely kill you!' out of wounded pride."
                        ]
                    },
                    {
                        "num": "14",
                        "title": "The Ethics of Non-Violence: Habil's Restraint",
                        "bullets": [
                            "Habil refuses reciprocal violence: 'If you stretch your hand to kill me, I shall not strike.'",
                            "Unshakable fear of the Lord of the worlds governs moral restraint under lethal assault.",
                            "Willingness to let the aggressor bear the double burden of original sin and fratricide."
                        ]
                    },
                    {
                        "num": "15",
                        "title": "The Raven's Lesson: Awakening Remorse",
                        "bullets": [
                            "Qabil murders his brother, overwhelmed by his soul's impulse, becoming a total loser.",
                            "Allah sends a raven scratching the earth to teach the killer how to conceal the corpse.",
                            "The agony of late remorse: 'Woe to me! Am I unable to be like this raven?'"
                        ]
                    },
                    {
                        "num": "16",
                        "title": "Cosmic Sanctity of Life: Saving One is Saving All",
                        "bullets": [
                            "Murdering an innocent soul is cosmically equivalent to murdering all of humanity.",
                            "Preserving a single life from destruction is cosmically equivalent to saving all mankind.",
                            "Absolute divine sanctity placed upon the human soul, forbidding vigilantism and slaughter."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 3,
        "title": "SOCIAL ORDER, PENAL JUSTICE & PURIFIED DEVOTION",
        "desc": "Pillars 5 & 6: Deterring Chaos (Hirabah), Seeking Al-Wasilah, Protecting Wealth & Judicial Autonomy",
        "sec": "PLATE 03 : PENAL JUSTICE & ORDER",
        "pillars": [
            {
                "name": "PILLAR 5: HIRABAH, SARIQAH & SEEKING AL-WASILAH",
                "sub": "Deterring Armed Insurrection, Drawing Near via Obedience & Safeguarding Wealth",
                "color": "rose",
                "cards": [
                    {
                        "num": "17",
                        "title": "Deterring Chaos: The Law of Hirabah (Terrorism)",
                        "bullets": [
                            "Severe penalties for armed banditry, terrorizing highways, and spreading civil corruption.",
                            "Judicial discretion: Execution, crucifixion, cross-amputation, or exile based on crime.",
                            "Repentance door: Those who repent before apprehension are granted divine forgiveness."
                        ]
                    },
                    {
                        "num": "18",
                        "title": "Seeking Al-Wasilah: Drawing Near via Obedience",
                        "bullets": [
                            "Command to attain Taqwa and seek Al-Wasilah (the means of near approach to Allah).",
                            "Sunni consensus: Wasilah is righteous deeds, worship, and obedience, not deceased intercessors.",
                            "Striving in His path (Jihad) as the highest active instrument of spiritual elevation."
                        ]
                    },
                    {
                        "num": "19",
                        "title": "Futility of Earthly Ransom on the Last Day",
                        "bullets": [
                            "Disbelievers possessing everything on earth and double its quantity cannot ransom themselves.",
                            "Eternal accountability: Worldly wealth cannot purchase immunity from divine retribution.",
                            "Enduring torment awaits those who traded eternal salvation for transient rebellion."
                        ]
                    },
                    {
                        "num": "20",
                        "title": "Protecting Communal Wealth: The Penalty of Theft",
                        "bullets": [
                            "Amputation of the hand decreed for male and female thieves as exemplary deterrence.",
                            "Juristic safeguards: Strict threshold (Nisab), secure custody (Hirz), and zero doubt.",
                            "Forgiveness and reform: Sincere repentance and restitution restore spiritual standing."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 6: JUDICIAL INTEGRITY & PROPHETIC EQUANIMITY",
                "sub": "Devourers of Suht, Discretionary Adjudication & Absolute Equity",
                "color": "cyan",
                "cards": [
                    {
                        "num": "21",
                        "title": "Grief Over Willful Disbelief & Distorted Words",
                        "bullets": [
                            "Prophetic heart consoled: Grieve not over those who hasten toward disbelief with their mouths.",
                            "Hearts that believe not: Inward duplicity contrasted with outward verbal declarations.",
                            "Distorting words out of place: Seeking corrupt rulings and abandoning divine statutes."
                        ]
                    },
                    {
                        "num": "22",
                        "title": "Devourers of Illicit Wealth (Akkaluna lis-Suht)",
                        "bullets": [
                            "Severe rebuke of corrupt jurists: Addicted to hearing falsehood and consuming illicit bribes.",
                            "Spiritual pollution: Bribery, usury, and corrupt fees blind the judicial conscience.",
                            "Purification of magistrates: Justice cannot be rendered through hands stained by extortion."
                        ]
                    },
                    {
                        "num": "23",
                        "title": "Judicial Autonomy: Judging Between Disbelievers",
                        "bullets": [
                            "Prophet granted jurisdictional discretion: Turn away from corrupt litigants or judge between them.",
                            "Immunity from harm: If you turn away, they cannot harm you in the slightest.",
                            "Sovereign independence of the Islamic judiciary in handling external minority disputes."
                        ]
                    },
                    {
                        "num": "24",
                        "title": "Equanimity in Judgment: Allah Loves the Equitable",
                        "bullets": [
                            "If judgment is rendered, it must be executed with unbending equity (bil-Qist).",
                            "Divine love confirmed: 'Indeed, Allah loves those who act equitably.'",
                            "Rebuking bad-faith litigation: Coming for arbitration while possessing their own revealed text."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 4,
        "title": "THE PROGRESSION OF SCRIPTURE & THE SUPREME GUARDIAN",
        "desc": "Pillars 7 & 8: The Torah & Injeel, The Qur'an as Muhaymin, Shir'atan wa Minhaja & Rejection of Jahiliyyah",
        "sec": "PLATE 04 : THE CRITERION OF SCRIPTURE",
        "pillars": [
            {
                "name": "PILLAR 7: THE TORAH & INJEEL: GUIDANCE & LIGHT",
                "sub": "Authentic Revelation, Rabbinic Guardianship & Retributive Equity",
                "color": "purple",
                "cards": [
                    {
                        "num": "25",
                        "title": "The Torah Revealed: Guidance & Illuminated Law",
                        "bullets": [
                            "Affirming original Torah: Sent down by Allah containing guidance, illumination, and law.",
                            "Prophets who submitted governed the Jewish community through its divine statutes.",
                            "Whoever does not judge by what Allah has revealed—such are indeed the true disbelievers."
                        ]
                    },
                    {
                        "num": "26",
                        "title": "Rabbis, Scholars & Inviolability of the Text",
                        "bullets": [
                            "Religious leaders and scholars entrusted with safeguarding the written scripture.",
                            "Fear not mankind, fear Allah alone; never barter divine revelation for fleeting worldly price.",
                            "Whoever judges not by Allah's revelation—such are indeed the unjust wrongdoers."
                        ]
                    },
                    {
                        "num": "27",
                        "title": "Retributive Law: An-Nafsa bin-Nafs (Life for Life)",
                        "bullets": [
                            "Prescribed equitable retribution: Life for life, eye for eye, tooth for tooth, equal wounds.",
                            "Mercy and charity elevated: Whoever foregoes retribution as charity gains divine expiation.",
                            "Balancing rigorous civil deterrence with the spiritual virtue of voluntary pardon."
                        ]
                    },
                    {
                        "num": "28",
                        "title": "Isa & The Injeel: Confirming and Softening",
                        "bullets": [
                            "Isa sent in the footsteps of previous prophets, confirming the original Torah before him.",
                            "The Gospel revealed containing guidance, radiant light, and admonition for the righteous.",
                            "Whoever judges not by what Allah has revealed therein—such are the rebellious transgressors."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 8: THE QUR'AN AS MUHAYMIN: GUARDIAN & STANDARD",
                "sub": "Master Criterion, Diverse Dispensations, Moral Race & Truth",
                "color": "emerald",
                "cards": [
                    {
                        "num": "29",
                        "title": "Muhayminan 'Alayh: Master Criterion of Truth",
                        "bullets": [
                            "The Qur'an revealed in truth, confirming previous scriptures and standing as Muhaymin.",
                            "Role of Muhaymin: Incorruptible guardian, witness, corrector, and ultimate ruling criterion.",
                            "Judge between them exclusively by what Allah revealed; follow not arbitrary desires."
                        ]
                    },
                    {
                        "num": "30",
                        "title": "Shir'atan wa Minhaja: Diverse Laws, One Creed",
                        "bullets": [
                            "To each civilization Allah prescribed a distinct legislative code (Shir'ah) and open path.",
                            "Universal Tawhid creed is eternal; historical civil laws adapted to eras and capacities.",
                            "Diversity ordained to test human fidelity in applying divine commandments across ages."
                        ]
                    },
                    {
                        "num": "31",
                        "title": "Fastabiqul-Khayrat: The Dynamic Race in Virtue",
                        "bullets": [
                            "Transcending sectarian paralysis: Compete vigorously with one another in righteous deeds.",
                            "Ultimate return is unto Allah alone, where He will resolve all historical disputes.",
                            "Action-oriented spirituality: Energy channeled into moral excellence rather than futile debate."
                        ]
                    },
                    {
                        "num": "32",
                        "title": "Hukm al-Jahiliyyah: Divine Law vs Pagan Custom",
                        "bullets": [
                            "Stern rhetorical question: 'Do they then seek the judgment of pagan ignorance (Jahiliyyah)?'",
                            "Unrivaled excellence of divine law: 'And who is better than Allah in judgment for the certain?'",
                            "Firm warning against being lured away from even a fraction of what Allah has sent down."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 5,
        "title": "THE GEOMETRY OF ALLIANCE & DIVINE AFFECTION",
        "desc": "Pillars 9 & 10: Wilayah Demarcation, The Loving Vanguard (Yuhibbuhum wa Yuhibboonah) & Hands of Allah",
        "sec": "PLATE 05 : ALLIANCE & DIVINE LOVE",
        "pillars": [
            {
                "name": "PILLAR 9: WILAYAH & THE LOVING VANGUARD",
                "sub": "Political Allegiance, Sickness of Opportunism & The Unbreakable Generation",
                "color": "gold",
                "cards": [
                    {
                        "num": "33",
                        "title": "Dismantling Compromising Alliances of Disloyalty",
                        "bullets": [
                            "Warning against seeking patronal alliances with hostile factions against the believers.",
                            "Self-sufficient community: Subordinating communal sovereignty undermines ideological autonomy.",
                            "Whoever allies with hostile factions compromises their internal belonging to the Ummah."
                        ]
                    },
                    {
                        "num": "34",
                        "title": "Sickness of Heart: Panicking Over Changing Winds",
                        "bullets": [
                            "Those with diseased hearts hasten to make compromises: 'We fear a turn of fortune.'",
                            "Allah promises decisive victory or a direct decree, exposing opportunists in humiliation.",
                            "Hypocritical oaths exposed: Believers will wonder: 'Are these the ones who swore solemn oaths?'"
                        ]
                    },
                    {
                        "num": "35",
                        "title": "The Loving Vanguard: Yuhibbuhum wa Yuhibboonah",
                        "bullets": [
                            "If a generation apostatizes, Allah will replace them with a people He loves and who love Him.",
                            "Four hallmarks: Gentle to believers, firm to deniers, striving in God's path, fearless of blame.",
                            "Immunity to peer pressure: Unshakable adherence to truth without fearing social reproach."
                        ]
                    },
                    {
                        "num": "36",
                        "title": "True Alliance: Allah, His Messenger & Believers",
                        "bullets": [
                            "True Wilayah defined: Exclusively Allah, His Messenger, and the steadfast believers.",
                            "Believers characterized by establishing prayer and paying zakah while bowing in humility.",
                            "The triumphant party: 'And whoever allies with Allah and His Messenger—the party of Allah wins.'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 10: DEFENDING FAITH & THE HANDS OF ALLAH",
                "sub": "Rebuking Mockery, Refuting Slander (Bal Yadahu) & Conveyance",
                "color": "rose",
                "cards": [
                    {
                        "num": "37",
                        "title": "Rebuking Those Who Mock Prayer and Religion",
                        "bullets": [
                            "Prohibition of allying with those who take religion as mockery, entertainment, and play.",
                            "The call to prayer ridiculed: When the Adhan is called, they treat it with derision and jest.",
                            "Cognitive diagnosis: Mockery of divine worship stems from lack of intellect and understanding."
                        ]
                    },
                    {
                        "num": "38",
                        "title": "Refuting the Slander: Bal Yadahu Mabsutatani",
                        "bullets": [
                            "Rebutting the blasphemous statement: 'The Hand of Allah is chained and stingy.'",
                            "Divine affirmation: 'Nay, both His hands are widely outstretched; He spends as He wills.'",
                            "Sunni orthodoxy: Affirming divine attributes without anthropomorphism (Tashbih) or denial."
                        ]
                    },
                    {
                        "num": "39",
                        "title": "Enmity and Malice Cast Until the Day of Rising",
                        "bullets": [
                            "Seditious factions who kindle fires of war find their fires systematically extinguished by God.",
                            "Divine retribution: Sowing enmity and malice among warmongers until Resurrection Day.",
                            "Corrupt striving: Rebuking those who tirelessly strive to spread corruption across the earth."
                        ]
                    },
                    {
                        "num": "40",
                        "title": "Balligh: The Absolute Mandate of Conveyance",
                        "bullets": [
                            "Sovereign command: 'O Messenger, convey all that has been revealed to you from your Lord.'",
                            "Solemn consequence: Failure to convey a single verse equates to failing the entire mission.",
                            "Guaranteed divine protection: 'And Allah will defend you from the people,' dismissing guards."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 6,
        "title": "EXPOSING THEOLOGICAL EXCESS & THE PROPHETIC CYCLE",
        "desc": "Pillars 11 & 12: Refuting Christological Deification, Kana Ya'kulani at-Ta'am, Curse on Silence & Monks' Tears",
        "sec": "PLATE 06 : THEOLOGY & REFORM",
        "pillars": [
            {
                "name": "PILLAR 11: DISMANTLING CHRISTOLOGICAL DEIFICATION",
                "sub": "Rebuttal of Trinity, Mortality of Isa & Maryam & Severe Shirk Warning",
                "color": "cyan",
                "cards": [
                    {
                        "num": "41",
                        "title": "The Universal Standard for Past Peoples of the Book",
                        "bullets": [
                            "Righteous among Jews, Christians, and Sabeans who truly believed and acted righteously have no fear.",
                            "Universal principle: Divine justice judges past communities by their authentic obedience.",
                            "Prophetic mission reaffirmed: Clarifying truths long obscured by sectarian additions."
                        ]
                    },
                    {
                        "num": "42",
                        "title": "Refuting the Deification of the Messiah Isa",
                        "bullets": [
                            "Categorical disbelief: Declaring that Allah is the Messiah, the son of Maryam.",
                            "Isa's own words cited: 'O Children of Israel, worship Allah, my Lord and your Lord!'",
                            "The penalty of Shirk: Whosoever associates partners with Allah is forbidden Paradise."
                        ]
                    },
                    {
                        "num": "43",
                        "title": "Kana Ya'kulani at-Ta'am: Mortality & Need",
                        "bullets": [
                            "The Messiah was nothing but a Messenger; before him passed many noble Messengers.",
                            "Maryam praised as a woman of profound truth (Siddiqah), devoid of divine claims.",
                            "Irrefutable logical proof: 'They both used to eat food!'—contingent beings require nourishment."
                        ]
                    },
                    {
                        "num": "44",
                        "title": "Rebuttal of the Trinity: Innahu man Yushrik",
                        "bullets": [
                            "Disbelieved are those who say: 'Allah is the third of three.' There is no deity but One God.",
                            "Stern warning against persisting: A painful torment awaits those who persist in blasphemy.",
                            "Invitation to repentance: Will they not turn to Allah in sincere repentance and seek forgiveness?"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 12: THE CURSE OF SILENCE & MONKS' TEARS",
                "sub": "Condemnation of Passive Scholars, Kanoo la Yatanahawna & Sincere Faith",
                "color": "purple",
                "cards": [
                    {
                        "num": "45",
                        "title": "The Curse of Dawud & Isa: Leaving Amr bil-Ma'roof",
                        "bullets": [
                            "Disbelievers among Bani Isra'il cursed by the tongues of Dawud and Isa ibn Maryam.",
                            "Cause of the curse: Persistent transgression, rebellion, and moral indifference.",
                            "Historical lesson: Sanctity of prophetic lineage cannot shield a corrupt society from wrath."
                        ]
                    },
                    {
                        "num": "46",
                        "title": "The Corrosive Silence: Kanoo la Yatanahawna",
                        "bullets": [
                            "Core societal crime: 'They did not prevent one another from the wrong actions they committed.'",
                            "Collapse of social immune system: Tolerating public injustice destroys civil morality.",
                            "Mandatory activism: Enjoining good and forbidding wrong is essential to preserve the Ummah."
                        ]
                    },
                    {
                        "num": "47",
                        "title": "Hearts Overflowing With Tears: Righteous Monks",
                        "bullets": [
                            "Nearest in affection to believers are those who say: 'We are Christians.'",
                            "Character of sincere priests and monks: Devoid of arrogance and dedicated to quiet worship.",
                            "Deep emotional response: When they hear revelation, their eyes overflow with tears of recognition."
                        ]
                    },
                    {
                        "num": "48",
                        "title": "The Prayer of the Truthful: Fa-ktubna Ma'ash-Shahideen",
                        "bullets": [
                            "Their heartfelt plea: 'Our Lord, we have believed, so register us among the truthful witnesses!'",
                            "Yearning for divine acceptance: 'Why should we not believe in Allah and the truth that has come?'",
                            "Reward granted: Gardens beneath which rivers flow, abiding therein as the reward of doers of good."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 7,
        "title": "SOCIAL ETHICS, PURITY OF SANCTUARY & OATHS",
        "desc": "Pillars 13 & 14: Decisive Prohibition of Khamr/Maysir, Expiation of Oaths & Sanctity of Ihram/Ka'bah",
        "sec": "PLATE 07 : SANCTITY & CIVIC PURITY",
        "pillars": [
            {
                "name": "PILLAR 13: SANCTITY OF OATHS & DECISIVE PROHIBITION",
                "sub": "Abolition of False Asceticism, Kaffarat al-Yameen & Eradication of Intoxicants",
                "color": "emerald",
                "cards": [
                    {
                        "num": "49",
                        "title": "Do Not Forbid Good Things Allah Made Lawful",
                        "bullets": [
                            "Rebuking self-imposed asceticism: Forbid not wholesome provisions (Tayyibat) Allah made lawful.",
                            "Balance of Islam: Rejecting monastic extremes; partake of lawful sustenance with gratitude.",
                            "Prohibition against transgressing boundaries: Allah loves not those who exceed limits."
                        ]
                    },
                    {
                        "num": "50",
                        "title": "The Expiation of Oaths: Kaffarat al-Yameen",
                        "bullets": [
                            "Allah does not hold you for unintentional oaths, but holds you for deliberate vows.",
                            "Structured expiation: Feeding ten destitute people, clothing them, or freeing a slave.",
                            "Alternative fast: Whoever cannot afford the expiation must observe three consecutive fasts."
                        ]
                    },
                    {
                        "num": "51",
                        "title": "Khamr & Maysir: The Rijs of Shaitan Banished",
                        "bullets": [
                            "Final categorical prohibition: Intoxicants, gambling, altars, and divining arrows declared Rijs.",
                            "Uncompromising command: 'Fajtaneebooh' (Turn completely aside and avoid it) to achieve success.",
                            "Historical obedience: Companions emptied all wine vessels into the streets upon revelation."
                        ]
                    },
                    {
                        "num": "52",
                        "title": "Sow Enmity & Block Remembrance: Shaitan's Goal",
                        "bullets": [
                            "Psychological strategy of Satan: Inciting mutual hatred and malice through intoxicants and gambling.",
                            "Spiritual destruction: Creating cognitive numbness that distracts from Dhikr and prayer.",
                            "The decisive query: 'Will you not then desist?' Believers responded: 'We have desisted!'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 14: THE SANCTITY OF IHRAM & THE KA'BAH",
                "sub": "The Hunting Test, Sacred Ka'bah as Anchor & Eradicating Superstition",
                "color": "gold",
                "cards": [
                    {
                        "num": "53",
                        "title": "The Test of Faith: Game Within Reach of Hands",
                        "bullets": [
                            "Allah tests the pilgrims by sending wild game easily accessible to their hands and spears.",
                            "Divine purpose: To make manifest who fears Allah in the secret, unseen depths of their heart.",
                            "Stern consequence: Whoever transgresses after this warning faces a severe and painful penalty."
                        ]
                    },
                    {
                        "num": "54",
                        "title": "The Sacred Sanctity: Hunting Forbidden in Ihram",
                        "bullets": [
                            "Explicit prohibition: Kill not game while you are in the sacred state of consecration (Ihram).",
                            "Penal expiation: Compensation in an equivalent domestic beast judged by two just arbiters.",
                            "Water game permitted: Catching marine game and sea food made lawful for pilgrims and travelers."
                        ]
                    },
                    {
                        "num": "55",
                        "title": "The Ka'bah: An Enduring Anchor for Humanity",
                        "bullets": [
                            "Allah established the Ka'bah, the Sacred House, as an enduring sanctuary and pivot for mankind.",
                            "Sanctity extended: Sacred months, sacrificial offerings, and garlands preserved for civic stability.",
                            "Cosmic proof: Demonstrating that Allah knows everything in the heavens and the earth."
                        ]
                    },
                    {
                        "num": "56",
                        "title": "Superstitions Abolished: Bahirah, Sa'ibah & Wasilah",
                        "bullets": [
                            "Abolition of pagan animal dedications: Bahirah, Sa'ibah, Wasilah, and Ham fabricated as divine law.",
                            "Rebuttal of traditionalism: Disbelievers cling to ancestors' ways despite ancestral ignorance.",
                            "Personal accountability: Guard your own souls; when you are guided, the astray cannot harm you."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 8,
        "title": "THE ESCHATOLOGICAL CROSS-EXAMINATION & SOVEREIGN SEAL",
        "desc": "Pillars 15 & 16: Miracles of Isa, The Heavenly Table (Al-Ma'idah), Subhanaka Vindication & Cosmic Dominion",
        "sec": "PLATE 08 : THE ESCHATOLOGICAL SEAL",
        "pillars": [
            {
                "name": "PILLAR 15: THE MIRACLES OF ISA & HEAVENLY TABLE",
                "sub": "Wills on Travel, Miracles by Divine Leave & Celestial Repast",
                "color": "rose",
                "cards": [
                    {
                        "num": "57",
                        "title": "Integrity of Wills: Faithful Testimony on Travel",
                        "bullets": [
                            "Judicial protocol: Two just witnesses required when executing wills during terminal illness or travel.",
                            "Solemn oath taken after prayer: Swearing by Allah that testimony is not sold for worldly advantage.",
                            "Preventing perjury: If deception is discovered, closer heirs swear to rectify false claims."
                        ]
                    },
                    {
                        "num": "58",
                        "title": "The Miracles Bi-Idhnillah: Clay, Healing & Life",
                        "bullets": [
                            "Favors upon Isa recalled: Strengthened with Holy Spirit; speaking in cradle and maturity.",
                            "Miracles executed exclusively by divine leave: Fashioning birds from clay, healing blind and leper.",
                            "Raising the dead by His leave, and divine protection when disbelievers sought his execution."
                        ]
                    },
                    {
                        "num": "59",
                        "title": "The Disciples' Request: The Heavenly Table",
                        "bullets": [
                            "The Hawariyyun petition: 'Can your Lord send down upon us a table spread with food from heaven?'",
                            "Isa's admonition: 'Fear Allah, if you are truly believers!' guarding theological propriety.",
                            "Their sincere justification: We desire to eat, reassure our hearts, and witness the truth."
                        ]
                    },
                    {
                        "num": "60",
                        "title": "A Sign for All Generations: Feast of Gratitude",
                        "bullets": [
                            "Isa's profound prayer: 'O Allah, our Lord, send down a table from heaven to be an Eid for us.'",
                            "Divine response: 'I will send it down; but whoever disbelieves after, I will punish uniquely.'",
                            "The Heavenly Table stands as a perpetual sign of divine sustenance and covenant gravity."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 16: THE GREAT INQUIRY & SOVEREIGN EXALTATION",
                "sub": "Isa's Impeccable Defense, In Tu'adhdhibhum & Universal Kingship",
                "color": "cyan",
                "cards": [
                    {
                        "num": "61",
                        "title": "The Great Eschatological Inquiry: Did You Say It?",
                        "bullets": [
                            "Solemn trial on Judgment Day: 'O Isa son of Maryam, did you tell people to take you as a deity?'",
                            "Cosmic confrontation before all creation: Exposing the fabrication of trinitarian worship.",
                            "The pristine monotheistic witness: Demarcating authentic prophetic teaching from human heresy."
                        ]
                    },
                    {
                        "num": "62",
                        "title": "Subhanaka: Isa's Impeccable Theological Defense",
                        "bullets": [
                            "Sublime opening: 'Subhanak! Exalted are You! Never could I say what I had no right to say.'",
                            "Divine omniscience invoked: 'If I had said it, You would know it; You know all unseen.'",
                            "Fidelity confirmed: 'I said nothing to them except what You commanded: Worship Allah alone.'"
                        ]
                    },
                    {
                        "num": "63",
                        "title": "The Sovereign Word: In Tu'adhdhibhum",
                        "bullets": [
                            "The supreme surrender: 'If You punish them, they are Your servants; if You forgive them, You are Wise.'",
                            "Attributes of majesty: Affirming Al-'Azeez (The Mighty) and Al-Hakeem (The All-Wise).",
                            "Prophetic empathy: The Prophet Muhammad wept throughout the night repeating this single verse."
                        ]
                    },
                    {
                        "num": "64",
                        "title": "Lillahil-Mulk: Sovereign Dominion Over All Existence",
                        "bullets": [
                            "The day when truthful hearts benefit from their truthfulness; rewarded with eternal gardens.",
                            "Divine pleasure achieved: 'Radhiyallahu 'anhum wa radhoo 'anh'—the supreme triumph (Al-Fawz).",
                            "Cosmic seal of the Surah: To Allah belongs all dominion of heavens and earth, competent over all."
                        ]
                    }
                ]
            }
        ]
    }
]

# Generate Markdown Document
md_content = """# Surah Al-Ma'idah: Master Landscape Mindmap Cartography
## 8 Master Plates • 16 Thematic Pillars • 64 Structured Cards
**Operating Philosophy:** **READ. REFLECT. RETURN.**  
**Brand Authority:** Huurs Studio Knowledge Architecture  
**Canonical Conspectus:** Imam al-Tabari, Imam al-Jassas, Imam al-Qurtubi, Imam al-Razi, Imam Ibn Kathir  

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
  <title>Surah Al-Ma'idah Master Landscape Mindmap | Huurs Studio</title>
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
        <span>Surah Al-Ma'idah Master Landscape Mindmap Cartography</span>
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
      <p style="font-size:0.75rem; margin-top:4px;">Imam al-Tabari &bull; Imam al-Jassas &bull; Imam al-Qurtubi &bull; Imam al-Razi &bull; Imam Ibn Kathir</p>
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
