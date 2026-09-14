#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-A'raf Master Mindmap HTML & Markdown Generator
8 Landscape Plates • 16 Thematic Pillars • 64 Detailed Analytical Cards
"""

import os, sys, re, json

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
HTML_OUT = os.path.join(BASE_DIR, "AL_ARAF_MASTER_MINDMAP.html")
MD_OUT = os.path.join(BASE_DIR, "AL_ARAF_MASTER_MINDMAP.md")

pages_data = [
    {
        "page": 1,
        "title": "PRIMORDIAL GENESIS, THE REFUSAL OF IBLIS & THE HEAVENLY FALL",
        "desc": "Pillars 1 & 2: Divine Revelation, Weighing in Truth, Pride of Iblis & Ambush on the Straight Path",
        "sec": "PLATE 01 : GENESIS & DISOBEDIENCE",
        "pillars": [
            {
                "name": "PILLAR 1: DIVINE REVELATION & OBJECTIVE ACCOUNTABILITY",
                "sub": "No Constriction in the Chest, Cosmic Scales & Sovereign Seizure",
                "color": "cyan",
                "cards": [
                    {
                        "num": "1",
                        "title": "Revelation: No Constriction in the Chest",
                        "bullets": [
                            "Alif-Lam-Mim-Sad: A divine Book revealed to guide, admonish, and awaken hearts.",
                            "Divine reassurance: Let there be no constriction (Haraj) in the prophetic chest.",
                            "Follow what is revealed from your Lord; follow no patron protectors besides Him."
                        ]
                    },
                    {
                        "num": "2",
                        "title": "Obliteration of Tyrannical Civilizations",
                        "bullets": [
                            "How many cities were annihilated when divine retribution seized them suddenly.",
                            "Struck down in nocturnal slumber or while relaxing in the heat of midday.",
                            "Their only cry when punishment arrived was confession: 'Indeed, we were wrongdoers!'"
                        ]
                    },
                    {
                        "num": "3",
                        "title": "Universal Interrogation of Messengers & Nations",
                        "bullets": [
                            "Every community will be questioned regarding their reception of divine revelation.",
                            "The Messengers will be questioned regarding the conveyance of their trust.",
                            "All deeds recounted with infallible divine knowledge; God was never absent."
                        ]
                    },
                    {
                        "num": "4",
                        "title": "The Scales of Absolute Truth (Al-Wazn)",
                        "bullets": [
                            "The weighing of deeds on that Day is an objective, physical, undeniable reality.",
                            "Those whose scales are heavy with righteous deeds achieve eternal triumph.",
                            "Those whose scales are light ruin their souls through injustice against divine signs."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 2: ADAM, IBLIS & THE ARROGANCE OF FIRE",
                "sub": "Command to Prostrate, Racial Vanity & Seduction of the Tree",
                "color": "purple",
                "cards": [
                    {
                        "num": "5",
                        "title": "Terrestrial Station & Primordial Prostration",
                        "bullets": [
                            "Humanity established upon the earth and granted means of livelihood (Ma'ayish).",
                            "Man created, fashioned, and presented before the assembly of the angelic host.",
                            "Command to prostrate in honor: All angels fell down except Iblis in defiance."
                        ]
                    },
                    {
                        "num": "6",
                        "title": "Arrogance of Fire: The Genesis of False Analogy",
                        "bullets": [
                            "Demanded reason: 'What prevented you from prostrating when I commanded you?'",
                            "Arrogant rationalization: 'I am better than him; You made me of fire and him of clay.'",
                            "Cast down in disgrace: 'Descend from here! It is not for you to be arrogant within it.'"
                        ]
                    },
                    {
                        "num": "7",
                        "title": "The Granted Respite & The Four-Way Ambush",
                        "bullets": [
                            "Iblis petitions respite until Resurrection; granted reprieve by divine decree.",
                            "The swore vendetta: 'I will surely sit in ambush on Your straight path.'",
                            "Assaulting humanity from front, back, right, and left; seeking to make them ungrateful."
                        ]
                    },
                    {
                        "num": "8",
                        "title": "Seduction of the Tree & Exposed Vulnerability",
                        "bullets": [
                            "Dwelling in the Garden with Hawwa; warned never to approach the singular tree.",
                            "Satanic whispering: False swearing that the tree grants eternity and angelic power.",
                            "Tasting the fruit: Garments stripped away; feverishly stitching leaves in shame."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 2,
        "title": "MORTAL CLOTHING, WARNINGS TO HUMANITY & THE ABODE OF PEACE",
        "desc": "Pillars 3 & 4: Libas at-Taqwa, Decorum at the Sanctuary, Rebutting False Taboos & The Appointed Term",
        "sec": "PLATE 02 : MODESTY & SANCTUARY",
        "pillars": [
            {
                "name": "PILLAR 3: THE THREE GARMENTS & REDEMPTIVE CONTRITION",
                "sub": "Rabbana Zalamna, Modesty of Form & The Clothing of Piety",
                "color": "emerald",
                "cards": [
                    {
                        "num": "9",
                        "title": "The Contrite Archetypal Cry: Rabbana Zalamna",
                        "bullets": [
                            "'Our Lord, we have wronged ourselves; if You forgive us not, we are of the losers.'",
                            "Immediate personal responsibility contrasts with Iblis's fatalistic grievance.",
                            "Descending to earth with mutual enmity; life, death, and resurrection terrestrialized."
                        ]
                    },
                    {
                        "num": "10",
                        "title": "Libas at-Taqwa: The Supreme Inner Garment",
                        "bullets": [
                            "Divine gift of clothing: Covering baseline nakedness (Satr) and aesthetic beauty (Reesh).",
                            "'And the garment of righteousness (Libas at-Taqwa)—that is best.'",
                            "Fine silks without Taqwa leave the human interior exposed in spiritual humiliation."
                        ]
                    },
                    {
                        "num": "11",
                        "title": "Satanic Disrobing: Warning to Children of Adam",
                        "bullets": [
                            "Let not Satan deceive you as he expelled your primordial parents from the Garden.",
                            "Stripping away modesty to expose vulnerability is an ancient adversarial strategy.",
                            "Shayateen made allies of those who do not believe, beautifying shameful acts."
                        ]
                    },
                    {
                        "num": "12",
                        "title": "Decisive Rebuttal of Naked Rituals",
                        "bullets": [
                            "Pre-Islamic pagans committed indecency, claiming: 'We found our forefathers doing it.'",
                            "Divine declaration: Allah never commands shameful indecency or immoral rites.",
                            "Say: 'My Lord has commanded justice and directing devotion solely to Him.'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 4: SACRED DECORUM & THE FIVE PROHIBITIONS",
                "sub": "Beauty at the Masjid, Wholesome Provisions & The Fixed Lifespan",
                "color": "gold",
                "cards": [
                    {
                        "num": "13",
                        "title": "Decorum at the Sanctuary: Adornment & Balance",
                        "bullets": [
                            "'O children of Adam, take your adornment (Zeenah) at every place of prayer.'",
                            "Eat and drink in wholesome gratitude; do not commit excess (La tusrifoo).",
                            "Divine rule: Moderation and aesthetic dignity are foundational religious duties."
                        ]
                    },
                    {
                        "num": "14",
                        "title": "Who Has Forbidden Wholesome Provisions?",
                        "bullets": [
                            "Stern rebuke: 'Who has forbidden the adornment of Allah and wholesome food?'",
                            "These blessings are for believers in this worldly life and exclusively theirs in Akhirah.",
                            "Islam annihilates false asceticism and fabricated taboos on lawful pleasures."
                        ]
                    },
                    {
                        "num": "15",
                        "title": "The Five Universal Prohibitions",
                        "bullets": [
                            "Open and secret indecencies (Fawahish), sin, and unprovoked oppression (Baghy).",
                            "Associating partners with Allah without revelatory authority (Shirk).",
                            "Speaking about Allah without knowledge: The ultimate spiritual transgression."
                        ]
                    },
                    {
                        "num": "16",
                        "title": "The Sealed Lifespan of Civilizations (Ajal)",
                        "bullets": [
                            "Every civilization has an immutable appointed term; none escapes its historical hour.",
                            "When their time arrives, it can neither be delayed nor advanced by a single moment.",
                            "Believers who maintain Taqwa and reform have no fear, nor shall they grieve."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 3,
        "title": "THE DIALOGUE OF THE HEIGHTS & THE COSMIC CLEANSING OF HEARTS",
        "desc": "Pillars 5 & 6: Closed Heavenly Gates, Recriminations in the Fire, Ashab al-A'raf & The Vaulted Bridge",
        "sec": "PLATE 03 : THE HEIGHTS & ESCHATOLOGY",
        "pillars": [
            {
                "name": "PILLAR 5: CLOSED GATES & MUTUAL RECRIMINATIONS",
                "sub": "The Eye of the Needle, Beds of Fire & Sister Nations Cursing Sister Nations",
                "color": "rose",
                "cards": [
                    {
                        "num": "17",
                        "title": "The Eye of the Needle: Barred Heavenly Gates",
                        "bullets": [
                            "For those who deny divine signs with arrogance, heavenly gates never open.",
                            "They shall not enter Paradise until a camel passes through the eye of a needle.",
                            "Complete metaphysical impossibility for obstinate deniers of transcendent truth."
                        ]
                    },
                    {
                        "num": "18",
                        "title": "Beds of Torment & Retribution for Tyranny",
                        "bullets": [
                            "For them are couches of Hellfire beneath them and coverings of fire above them.",
                            "Exact retributive justice: Repaying oppressors according to their arrogant tyranny.",
                            "Contrasted with the humble righteous who strive within the limits of their capacity."
                        ]
                    },
                    {
                        "num": "19",
                        "title": "Sister Nations Cursing Sisters in Hell",
                        "bullets": [
                            "Every time a rebellious generation enters the Fire, it curses its predecessor.",
                            "Followers accuse their leaders: 'Our Lord, these misled us; give them doubled torment!'",
                            "Divine response: 'For each there is double, but you do not know.'"
                        ]
                    },
                    {
                        "num": "20",
                        "title": "Denied Intercession: Forgetting Those Who Forgot",
                        "bullets": [
                            "On that Day, the reality of revelation is manifest; former deities vanish into thin air.",
                            "Deniers plead for intercessors or a second worldly trial to act righteously.",
                            "Divine verdict: 'Today We forget them just as they forgot the meeting of this Day.'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 6: ASHAB AL-A'RAF & PURIFIED HEARTS IN JANNAH",
                "sub": "Cleansing Resentment, The Men on the Ramparts & The Cry for Water",
                "color": "cyan",
                "cards": [
                    {
                        "num": "21",
                        "title": "Cleansing Resentment: The Vaulted Bridge",
                        "bullets": [
                            "'And We will remove whatever malice (Ghill) is in their breasts; rivers flowing beneath.'",
                            "Reconciled upon the Qantarah, entering Paradise as loving brothers upon thrones.",
                            "Their eternal gratitude: 'Praise be to Allah who guided us to this blessed abode!'"
                        ]
                    },
                    {
                        "num": "22",
                        "title": "The Great Dialogue Across the Cosmic Divide",
                        "bullets": [
                            "Dwellers of Paradise call out: 'We have found what our Lord promised to be true!'",
                            "Dwellers of the Fire respond in anguish: 'Yes, we have found it true.'",
                            "The caller proclaims between them: 'The curse of Allah is upon the oppressors.'"
                        ]
                    },
                    {
                        "num": "23",
                        "title": "Ashab al-A'raf: The Men upon the Ramparts",
                        "bullets": [
                            "Standing upon the high partition, recognizing residents of both realms by their marks.",
                            "Greeting Jannah with longing peace; looking at Hell and crying: 'Save us from them!'",
                            "Equal deeds balance them in suspense until sovereign grace admits them into bliss."
                        ]
                    },
                    {
                        "num": "24",
                        "title": "The Denied Cry for Water & Nourishment",
                        "bullets": [
                            "Dwellers of the Fire plead: 'Pour upon us some water or what Allah provided you!'",
                            "Inhabitants of Paradise answer: 'Indeed, Allah has forbidden both to the disbelievers.'",
                            "They took religion as distraction and amusement, deceived by worldly illusions."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 4,
        "title": "COSMIC CREATION, HUMBLE SUPPLICATION & THE EARLY MESSENGERS",
        "desc": "Pillars 7 & 8: Hexaemeron Creation, Istawa Transcendent, Adab of Du'a, Nuh & Hud's Struggle",
        "sec": "PLATE 04 : COSMIC CREATION & EARLY PROPHETS",
        "pillars": [
            {
                "name": "PILLAR 7: HEXAEMERON CREATION & SACRED SUPPLICATION",
                "sub": "Six Cosmic Epochs, Sovereign Istawa, Tadarru'an wa Khufyah & Reviving Rain",
                "color": "purple",
                "cards": [
                    {
                        "num": "25",
                        "title": "Six Epochs of Creation & The Solar Veil",
                        "bullets": [
                            "Created heavens and earth in six days; night wraps daylight in swift pursuit.",
                            "Sun, moon, and stars completely subservient to His unchallengeable command.",
                            "'Unquestionably, His is the creation and the command; blessed is Allah, Lord of Worlds.'"
                        ]
                    },
                    {
                        "num": "26",
                        "title": "Istawa 'alal-'Arsh: Transcendent Majesty",
                        "bullets": [
                            "Transcendent establishment over the Throne without physical modality or resemblance.",
                            "Incomprehensible glory affirming sovereignty above all contingent dimensions.",
                            "Sovereign ruler of cosmic order, guiding all creation through purposeful wisdom."
                        ]
                    },
                    {
                        "num": "27",
                        "title": "The Adab of Du'a: Humility & Secrecy",
                        "bullets": [
                            "'Call upon your Lord in broken humility (Tadarru') and in secrecy (Khufyah).'",
                            "Allah does not love transgressors who scream, boast, or demand the impossible.",
                            "Sowing no corruption after earth's reformation; calling in awe and aspiration."
                        ]
                    },
                    {
                        "num": "28",
                        "title": "The Reviving Winds: Parable of Resurrection",
                        "bullets": [
                            "Merciful winds sent as glad tidings, carrying heavy clouds across arid wastelands.",
                            "Rains reviving dead soils to yield produce; exactly thus are the dead resurrected.",
                            "The fertile land yields vegetation by God's leave; corrupt land yields only bitter shrubs."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 8: EARLY PROPHETIC STRUGGLES: NUH & HUD",
                "sub": "Nuh's Compassionate Naseehah, The Deluge & 'Ad's Monolithic Arrogance",
                "color": "emerald",
                "cards": [
                    {
                        "num": "29",
                        "title": "Nuh's Mission: Pure Monotheism & Warning",
                        "bullets": [
                            "'O my people, worship Allah; you have no deity other than Him; I fear for you the Day.'",
                            "Tribal chieftains mock: 'Indeed, we see you in manifest, foolish error.'",
                            "Sincere reply: 'There is no error in me, but I am a Messenger from the Lord of Worlds.'"
                        ]
                    },
                    {
                        "num": "30",
                        "title": "Delivering Sincere Advice (Naseehah)",
                        "bullets": [
                            "Nuh conveys divine messages, offering sincere counsel and knowing what they know not.",
                            "Rebuking wonder: 'Do you marvel that an admonition comes through a man among you?'",
                            "Deniers reject the signs; believers saved in the Ark; the mockers drowned in the flood."
                        ]
                    },
                    {
                        "num": "31",
                        "title": "Hud to 'Ad: Confronting Giant Monoliths",
                        "bullets": [
                            "Sent to the mighty empire of 'Ad: 'O my people, worship Allah; will you not fear Him?'",
                            "Chieftains insult: 'Indeed, we see you in foolishness, and we think you are of the liars.'",
                            "Hud answers with prophetic dignity: 'There is no foolishness in me; I am a faithful adviser.'"
                        ]
                    },
                    {
                        "num": "32",
                        "title": "Remembrance of Blessings & The Gale Retribution",
                        "bullets": [
                            "Reminding them of how God made them successors after Nuh and increased their stature.",
                            "They defiantly clung to ancestral idols; retribution arrived as a furious destructive wind.",
                            "Believers delivered through divine mercy; roots of arrogant tyrants severed completely."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 5,
        "title": "PROPHETIC CONTESTS: SALIH, LUT & SHU'AYB",
        "desc": "Pillars 9 & 10: Thamud & The She-Camel, Lut & The Sodomites, Shu'ayb & Economic Justice",
        "sec": "PLATE 05 : PROPHETIC CRUCIBLES",
        "pillars": [
            {
                "name": "PILLAR 9: THE TRIALS OF THAMUD & THE SODOMITES",
                "sub": "Palaces in Rock, The Miraculous She-Camel, Unnatural Obscenity & Brimstone Rain",
                "color": "gold",
                "cards": [
                    {
                        "num": "33",
                        "title": "Salih to Thamud: Dwelling in Rock Palaces",
                        "bullets": [
                            "Settled in lush plains, carving grand homes out of mountain stone cliffs.",
                            "Remember God's favors; do not commit abuse upon the earth, spreading corruption.",
                            "The arrogant elite mock: 'Do you know that Salih is truly sent from his Lord?'"
                        ]
                    },
                    {
                        "num": "34",
                        "title": "The Miraculous She-Camel (Naqatullah)",
                        "bullets": [
                            "Sent as a manifest sign: 'This is the She-Camel of Allah; leave her to graze freely.'",
                            "Do not touch her with harm, lest a painful punishment seize you without warning.",
                            "The wickedest conspirators hamstrung the camel and defied their Lord's decree."
                        ]
                    },
                    {
                        "num": "35",
                        "title": "The Tremor (Ar-Rajfah) & Salih's Elegy",
                        "bullets": [
                            "Cataclysmic seismic shock struck them; morning found them collapsed lifeless in homes.",
                            "Salih turned away in sorrow: 'I conveyed my Lord's message, but you love not advisers.'",
                            "The proud civilization wiped from history, their monumental stone dwellings desolate."
                        ]
                    },
                    {
                        "num": "36",
                        "title": "Lut's Stand Against Moral Perversion",
                        "bullets": [
                            "Confronting the men of Sodom: 'Do you commit an obscenity none before you committed?'",
                            "Approaching men with carnal lust instead of women; exceeding all human boundaries.",
                            "Their only answer was expulsion: 'Drive them out! They are people who keep pure!'"
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 10: SHU'AYB, MADYAN & ECONOMIC SANCTITY",
                "sub": "Honest Scales, Highway Extortion, Oligarchic Ultimatums & The Snare of Makr Allah",
                "color": "rose",
                "cards": [
                    {
                        "num": "37",
                        "title": "Shu'ayb to Madyan: The Integrity of Commerce",
                        "bullets": [
                            "'Give full measure and weight; do not deprive people of their rightful belongings.'",
                            "Do not cause corruption upon the earth after it has been reformed by divine law.",
                            "Grounding honest business in faith: Honest trade is a sacred covenant with the Lord."
                        ]
                    },
                    {
                        "num": "38",
                        "title": "Rebuking Highway Ambush & Banditry",
                        "bullets": [
                            "Do not sit upon every pathway threatening travelers and hindering from God's way.",
                            "Remember when you were few in numbers and He multiplied your wealth and strength.",
                            "Observe the sobering end of those who spread corruption across neighboring lands."
                        ]
                    },
                    {
                        "num": "39",
                        "title": "The Oligarchic Ultimatum & Firm Faith",
                        "bullets": [
                            "Arrogant chieftains threaten: 'We will expel you and your followers or you must return!'",
                            "Shu'ayb replies: 'Even if we hate it? We would fabricate a lie if we returned to your ways.'",
                            "'Our Lord, decide between us and our people in truth; You are the best of deciders.'"
                        ]
                    },
                    {
                        "num": "40",
                        "title": "The Destruction of Madyan & The Snare of Security",
                        "bullets": [
                            "Struck by the seismic tremor, left prostrate and dead in their luxurious dwellings.",
                            "Those who denied Shu'ayb became as though they had never prospered within them.",
                            "Do they feel secure against the plan of Allah (Makr Allah)? None feels secure except losers."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 6,
        "title": "THE EPIC OF MUSA: CONFRONTING FIR'AWN & THE FALL OF SORCERERS",
        "desc": "Pillars 11 & 12: Manifest Serpent, Prostration of Sorcerers, The Five Plagues & Deliverance at the Sea",
        "sec": "PLATE 06 : MUSA & TYRANNY",
        "pillars": [
            {
                "name": "PILLAR 11: SIGNS BEFORE PHARAOH & DEFIANCE OF FAITH",
                "sub": "Musa's Emissary Mission, Living Python, Illusion Defeated & The Sorcerers' Sujood",
                "color": "cyan",
                "cards": [
                    {
                        "num": "41",
                        "title": "Musa's Declaration: Emissary from Rabb al-'Alameen",
                        "bullets": [
                            "Musa confronts the Pharaoh: 'I am an emissary from the Lord of the worlds.'",
                            "Obligated to speak nothing about Allah except the absolute, unblemished truth.",
                            "'Release with me the Children of Israel from generational enslavement and torment.'"
                        ]
                    },
                    {
                        "num": "42",
                        "title": "The Real Serpent & The Radiant Hand",
                        "bullets": [
                            "Musa casts his staff: It becomes an undeniable, living, devouring python (Thu'ban).",
                            "He draws forth his hand: Radiant, gleaming white to all onlookers without blemish.",
                            "Pharaoh's counsellors panic: 'Indeed, this is a learned, dangerous sorcerer!'"
                        ]
                    },
                    {
                        "num": "43",
                        "title": "The Great Tournament of Egyptian Sorcery",
                        "bullets": [
                            "Magicians summoned from all provinces; promises of riches and royal proximity.",
                            "They cast ropes and staffs, bewitching human eyes and striking terror with illusions.",
                            "God inspires Musa: 'Cast your staff!' It devours every illusory falsehood they fabricated."
                        ]
                    },
                    {
                        "num": "44",
                        "title": "The Prostration of Sorcerers (Sujjada)",
                        "bullets": [
                            "The master magicians fall instantly in prostration: 'We believe in the Lord of the worlds!'",
                            "Unanimous recognition: This was not magic or trickery, but divine omnipotence.",
                            "Truth prevailed; Pharaoh's imperial vanity and spiritual prestige collapsed in a moment."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 12: PHARAOH'S WRATH, PLAGUES & THE SEA DIVIDE",
                "sub": "Threats of Dismemberment, Heroic Patience, Five Inundations & Sea Deliverance",
                "color": "purple",
                "cards": [
                    {
                        "num": "45",
                        "title": "Pharaoh's Raging Threats of Dismemberment",
                        "bullets": [
                            "Pharaoh rages: 'Did you believe before I granted permission? This is a conspiracy!'",
                            "Threats of cross-amputation (hands and feet on opposite sides) and crucifixion.",
                            "The new believers answer with sublime defiance: 'Indeed, to our Lord we return!'"
                        ]
                    },
                    {
                        "num": "46",
                        "title": "The Believers' Prayer for Steadfastness",
                        "bullets": [
                            "'You take vengeance upon us only because we believed in the signs of our Lord.'",
                            "'Rabbana afrigh 'alayna sabran wa tawaffana muslimeen' (Pour upon us patience!).",
                            "Musa counsels his trembling people: 'Seek help through Allah and be steadfast.'"
                        ]
                    },
                    {
                        "num": "47",
                        "title": "The Five Inundations (Ayatin Mufassalat)",
                        "bullets": [
                            "Egypt struck systematically: The flood, locusts, lice, frogs, and water turned to blood.",
                            "Manifest, distinct signs; yet Pharaoh and his lords persisted in haughty criminality.",
                            "Each time relief was granted upon Musa's du'a, they broke their solemn covenants."
                        ]
                    },
                    {
                        "num": "48",
                        "title": "The Splitting of the Sea & Drowning of Fir'awn",
                        "bullets": [
                            "Pharaoh and his hosts pursued the believers; plunged into the deep waters of the sea.",
                            "The dispossessed and oppressed inherited the blessed eastern and western lands.",
                            "Word of divine promise fulfilled for Bani Isra'il because of their enduring patience."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 7,
        "title": "MOUNT SINAI, THE VISION PETITION & THE GOLDEN CALF",
        "desc": "Pillars 13 & 14: The 40 Nights, Rabbi Arini, Pulverized Mountain, Inscribed Tablets & The Golden Calf",
        "sec": "PLATE 07 : SINAI & THE TABLETS",
        "pillars": [
            {
                "name": "PILLAR 13: THEOPHANY AT SINAI & THE INSCRIBED TABLETS",
                "sub": "Forty Nights, Yearning for Divine Sight, Shattered Granite & The Divine Law",
                "color": "emerald",
                "cards": [
                    {
                        "num": "49",
                        "title": "Forty Nights of Sinai & Harun's Deputyship",
                        "bullets": [
                            "Musa appointed thirty nights, completed with ten, culminating in forty holy nights.",
                            "Musa counsels Harun: 'Take my place among my people, act righteously, avoid corruption.'",
                            "Prepared through spiritual retreat to receive the direct Word of the Sovereign Lord."
                        ]
                    },
                    {
                        "num": "50",
                        "title": "The Vision Petition: Rabbi Arini Anzur Ilayk",
                        "bullets": [
                            "Overwhelmed by love after direct speech (Takleem), Musa asks: 'Lord, show me Yourself!'",
                            "Divine response: 'You will never see Me in this mortal realm; but look at the mountain.'",
                            "'If it remains firmly in its place, then you shall behold My transcendent glory.'"
                        ]
                    },
                    {
                        "num": "51",
                        "title": "The Mountain Pulverized & Musa's Swoon",
                        "bullets": [
                            "When Allah revealed His glory to the mountain, it crumbled into fine, swirling dust.",
                            "Musa collapsed in unconscious terror (Kharra Musa sa'iqa) from the awe of the theophany.",
                            "Awakening in repentance: 'Glory be to You! I turn to You, first of the believers.'"
                        ]
                    },
                    {
                        "num": "52",
                        "title": "The Inscribed Tablets of Admonition",
                        "bullets": [
                            "'O Musa, I have chosen you over humankind through My messages and My speech.'",
                            "Bestowed the sacred Tablets inscribed with comprehensive admonition and legal detail.",
                            "Commanded to hold them with unwavering strength and enjoin his people to the best of it."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 14: THE GOLDEN CALF, ANGER & THE UMMI PROPHET",
                "sub": "The Lowing Calf Effigy, Prophetic Indignation, 70 Elders & The Universal Messenger",
                "color": "gold",
                "cards": [
                    {
                        "num": "53",
                        "title": "Seduction of the Lowing Calf Effigy",
                        "bullets": [
                            "In Musa's absence, jewelry melted to form the lifeless body of a lowing golden calf.",
                            "The people worshipped it in folly: 'Did they not see it speaks not nor guides them?'",
                            "Deep spiritual relapse into pagan superstition the moment prophetic leadership paused."
                        ]
                    },
                    {
                        "num": "54",
                        "title": "Musa's Righteous Fury & Harun's Plea",
                        "bullets": [
                            "Musa returns grieving and furious, casting down the Tablets and seizing Harun's beard.",
                            "Harun pleads: 'Son of my mother, the mob overpowered me and almost killed me.'",
                            "Calming, Musa takes up the Tablets: In their inscription was guidance and mercy for the fearful."
                        ]
                    },
                    {
                        "num": "55",
                        "title": "The Seventy Elders & The Seismic Tremor",
                        "bullets": [
                            "Musa chose seventy men of stature for the divine appointment; seized by a violent quake.",
                            "Musa intercedes: 'Would You destroy us for what foolish men did? You are our protector.'",
                            "'Forgive us and have mercy upon us; You are the best of those who forgive.'"
                        ]
                    },
                    {
                        "num": "56",
                        "title": "The Prophesied Ummi Messenger in Scripture",
                        "bullets": [
                            "Mercy decreed for those who follow the unlettered Prophet (An-Nabiyy al-Ummiyy).",
                            "Inscribed in the Torah and Injeel: Enjoining good, forbidding evil, making pure things halal.",
                            "Relieving humanity from crushing burdens and shackles; successful are those who honor him."
                        ]
                    }
                ]
            }
        ]
    },
    {
        "page": 8,
        "title": "THE PRIMORDIAL COVENANT, THE PARABLE OF THE DOG & FINAL PROSTRATION",
        "desc": "Pillars 15 & 16: The Twelve Springs, Sabbath-Breakers, Mithaq Adam, Parable of the Dog & Final Sajdah",
        "sec": "PLATE 08 : THE PRIMORDIAL COVENANT",
        "pillars": [
            {
                "name": "PILLAR 15: THE PRIMORDIAL MITHAQ & SABBATH METAMORPHOSIS",
                "sub": "Twelve Springs, Transgressing the Sabbath, Canopy Mountain & Alastu bi-Rabbikum",
                "color": "rose",
                "cards": [
                    {
                        "num": "57",
                        "title": "Twelve Springs, Manna, Quails & The Altered Word",
                        "bullets": [
                            "Divided into twelve tribes; rock struck to yield twelve distinct gushing springs.",
                            "Manna and quails provided; commanded to enter the city saying 'Hittah' (Forgiveness).",
                            "Transgressors altered the word in mockery, inviting plague for their persistent disobedience."
                        ]
                    },
                    {
                        "num": "58",
                        "title": "The Sabbath-Breakers & The Three Factions",
                        "bullets": [
                            "Tested with swarming fish on the Sabbath; three factions: sinners, preachers, bystanders.",
                            "Bystanders asked: 'Why preach to people Allah will destroy?' Preachers: 'As an excuse to our Lord.'",
                            "The righteous preachers saved; the Sabbath-breakers transformed into despised apes."
                        ]
                    },
                    {
                        "num": "59",
                        "title": "Mount Sinai Shaken Like a Canopy (Zullah)",
                        "bullets": [
                            "Shaking the mountain above them like a dark, towering storm cloud ready to crush them.",
                            "'Hold fast to what We have given you with resolve, and remember what is within it.'",
                            "A terrifying physical testament to the absolute seriousness of the divine covenant."
                        ]
                    },
                    {
                        "num": "60",
                        "title": "The Primordial Covenant: Alastu bi-Rabbikum?",
                        "bullets": [
                            "Progeny extracted from Adam's loins, made to testify: 'Am I not your Lord?'",
                            "Every soul replied: 'Bala, shahidna!' (Yes, we testify!)—inscribing Fitrah in human consciousness.",
                            "Eliminating all excuses on Judgment Day: None can claim heedlessness or inherited Shirk."
                        ]
                    }
                ]
            },
            {
                "name": "PILLAR 16: DIVINE NAMES, PERPETUAL THIRST & THE UNIVERSAL SAJDAH",
                "sub": "Parable of the Panting Dog, Hearts Without Understanding, Al-Asma al-Husna & The Sajdah",
                "color": "cyan",
                "cards": [
                    {
                        "num": "61",
                        "title": "Parable of the Panting Dog: The Apostate Scholar",
                        "bullets": [
                            "The man granted divine verses who stripped them away (Insalakha), pursuing vile lusts.",
                            "His likeness is that of a dog: Drive him away and he pants, leave him and he pants.",
                            "Perpetual, insatiable spiritual thirst of those who sell sacred knowledge for worldliness."
                        ]
                    },
                    {
                        "num": "62",
                        "title": "Created for Jahannam: Deadened Spiritual Faculties",
                        "bullets": [
                            "Hearts that do not understand, eyes that do not see, ears that do not hear.",
                            "'They are like livestock; rather, they are more astray; it is they who are the heedless.'",
                            "Willful rejection of revelatory faculties reduces the human being below the level of animals."
                        ]
                    },
                    {
                        "num": "63",
                        "title": "Al-Asma al-Husna: The Ninety-Nine Beautiful Names",
                        "bullets": [
                            "'And to Allah belong the most beautiful names, so invoke Him by them.'",
                            "Abandon those who practice deviation (Ilhad) concerning His transcendent names.",
                            "Refuge from Satanic whispers: Seek protection in Allah, the All-Hearing, All-Knowing."
                        ]
                    },
                    {
                        "num": "64",
                        "title": "The Adab of Qur'an & The Grand Prostration",
                        "bullets": [
                            "When the Qur'an is recited, listen in silence that you may obtain divine mercy.",
                            "Remember your Lord within yourself with humility, fear, and soft voice morning and night.",
                            "Angels before the Throne glorify Him without fatigue and prostrate: Fall down in Sajdah!"
                        ]
                    }
                ]
            }
        ]
    }
]

# Generate Markdown
md_lines = [
    "# Surah Al-A'raf — Master Landscape Mindmap Documentation",
    "## 8 Landscape Plates • 16 Thematic Pillars • 64 Detailed Analytical Cards",
    "",
    "> **Brand Philosophy:** READ. REFLECT. RETURN.  ",
    "> **Sunni Source Discipline:** Imam at-Tabari, Imam al-Razi, Imam al-Qurtubi, Imam Ibn Kathir  ",
    "> **Design Standards:** 16:9 Landscape Vector Geometry, Zero Ayah Numbers in Headings, Zero Audio Timestamps  ",
    "",
    "---",
    ""
]

for p in pages_data:
    md_lines.append(f"## Plate {p['page']:02d}: {p['title']}")
    md_lines.append(f"**Section Badge:** `[{p['sec']}]`  ")
    md_lines.append(f"**Overview:** {p['desc']}  \n")
    for pil in p['pillars']:
        md_lines.append(f"### {pil['name']}")
        md_lines.append(f"*{pil['sub']}*  \n")
        for c in pil['cards']:
            md_lines.append(f"#### {c['num']}. {c['title']}")
            for b in c['bullets']:
                md_lines.append(f"- {b}")
            md_lines.append("")
    md_lines.append("---\n")

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print(f"MD generated: {MD_OUT}")

# Generate HTML
tabs_html = ""
for p in pages_data:
    active = "active" if p['page'] == 1 else ""
    tabs_html += f"""<button class="tab-btn {active}" onclick="showPage({p['page']})">Plate {p['page']:02d}</button>\n"""

html_plates = ""
for p in pages_data:
    active = "active" if p['page'] == 1 else ""
    pillars_html = ""
    for pil in p['pillars']:
        cards_html = ""
        for c in pil['cards']:
            bullets = "".join(f"<li>{b}</li>" for b in c['bullets'])
            cards_html += f"""
          <div class="card">
            <div class="card-head">
              <span class="card-num">{c['num']}</span>
              <h4>{c['title']}</h4>
            </div>
            <ul>{bullets}</ul>
          </div>"""
        pillars_html += f"""
        <div class="pillar-col">
          <div class="pillar-header {pil['color']}">
            <h3>{pil['name']}</h3>
            <p>{pil['sub']}</p>
          </div>
          <div class="pillar-cards">
            {cards_html}
          </div>
        </div>"""
    
    html_plates += f"""
    <section class="page-container {active}" id="page-{p['page']}">
      <div class="page-header">
        <div>
          <h2>{p['title']}</h2>
          <p class="subtitle">{p['desc']}</p>
        </div>
        <div class="badge-tag">[{p['sec']}]</div>
      </div>
      <div class="pillars-grid">
        {pillars_html}
      </div>
    </section>"""

html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-A'raf — Master Landscape Mindmap | Huurs Studio</title>
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
      padding: 24px;
      line-height: 1.5;
    }}
    .wrapper {{ max-width: 1400px; margin: 0 auto; }}
    header.header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-top: 3px solid var(--gold);
      border-radius: 8px;
      padding: 16px 24px;
      margin-bottom: 24px;
    }}
    header.header h1 {{ font-size: 1.25rem; color: var(--gold); letter-spacing: 0.05em; }}
    header.header span {{ color: var(--text-muted); font-size: 0.88rem; margin-left: 12px; }}
    .tabs-bar {{ display: flex; gap: 8px; margin-bottom: 24px; overflow-x: auto; padding-bottom: 8px; }}
    .tab-btn {{
      background: var(--navy-card);
      color: var(--text-muted);
      border: 1px solid var(--border-muted);
      padding: 10px 18px;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .tab-btn:hover {{ border-color: var(--gold); color: var(--white); }}
    .tab-btn.active {{
      background: var(--navy-elevated);
      color: var(--gold);
      border-color: var(--gold);
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.25);
    }}
    .page-container {{ display: none; }}
    .page-container.active {{ display: block; }}
    .page-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 22px;
      margin-bottom: 20px;
    }}
    .page-header h2 {{ font-size: 1.15rem; color: var(--gold-light); letter-spacing: 0.03em; }}
    .page-header p.subtitle {{ font-size: 0.82rem; color: var(--text-muted); margin-top: 4px; }}
    .badge-tag {{
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .pillars-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
    @media (max-width: 960px) {{ .pillars-grid {{ grid-template-columns: 1fr; }} }}
    .pillar-col {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      overflow: hidden;
    }}
    .pillar-header {{ padding: 14px 18px; border-bottom: 1px solid var(--border-muted); }}
    .pillar-header.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-header.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-header.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-header.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-header.rose {{ border-top: 3px solid var(--rose); }}
    .pillar-header h3 {{ font-size: 0.92rem; color: var(--white); }}
    .pillar-header p {{ font-size: 0.78rem; color: var(--text-muted); margin-top: 2px; }}
    .pillar-cards {{ padding: 16px; display: flex; flex-direction: column; gap: 12px; }}
    .card {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 12px 16px;
      transition: all 0.2s;
    }}
    .card:hover {{ border-color: var(--gold); transform: translateY(-1px); }}
    .card-head {{ display: flex; align-items: baseline; gap: 10px; margin-bottom: 8px; }}
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
        <span>Surah Al-A'raf Master Landscape Mindmap Cartography</span>
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
