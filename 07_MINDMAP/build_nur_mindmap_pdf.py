#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Nur Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "NUR_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews")
os.makedirs(PREVIEWS_DIR, exist_ok=True)

brain_dir = "/home/ben/.gemini/antigravity/brain/1d535f8c-0b01-42ad-8e78-fc566134377c"

# Palette (Strict Brand_Visual_System.md)
NAVY_DEEP = (0.024, 0.039, 0.071)      # #060A12
NAVY_CARD = (0.051, 0.078, 0.133)      # #0D1422
NAVY_ELEVATED = (0.078, 0.118, 0.196)  # #141E32
GOLD = (0.831, 0.686, 0.353)           # #D4AF59
GOLD_LIGHT = (0.910, 0.820, 0.580)
CYAN = (0.220, 0.740, 0.970)           # #38BDF8
PURPLE = (0.659, 0.333, 0.969)         # #A855F7
EMERALD = (0.063, 0.725, 0.506)        # #10B981
ROSE = (0.920, 0.350, 0.450)
WHITE = (0.973, 0.980, 0.988)
TEXT_MUTED = (0.680, 0.730, 0.800)
BORDER_MUTED = (0.160, 0.220, 0.310)

def build_nur_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AN-NUR", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-header Title Area
        pdf.text(title, 32, h - 66, font="F2", size=12.5, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)

        # Right Section Badge
        badge_str = f"[{section_badge}]"
        badge_w = len(badge_str) * 6.1
        pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=9.5, rgb=GOLD)

        # Divider Rule
        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Bottom Footer
        pdf.line(32, 30, w - 32, 30, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 16, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("AUTHENTIC SUNNI SOURCE DISCIPLINE  *  THEMATIC SEQUENCE PURITY  *  READ. REFLECT. RETURN.", w - 465, 16, font="F2", size=7.0, rgb=GOLD_LIGHT)

    def draw_card(c_x, y_c, c_w, card_num, title, text):
        pdf.rect(c_x + 6, y_c - 52, c_w - 12, 62, fill_rgb=NAVY_CARD, stroke_rgb=BORDER_MUTED, line_width=0.6)
        pdf.rect(c_x + 12, y_c - 6, 22, 12, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.5)
        pdf.text(f"{card_num:02d}", c_x + 16, y_c + 2, font="F2", size=6.8, rgb=GOLD)
        pdf.text(title, c_x + 38, y_c + 2, font="F2", size=7.8, rgb=WHITE)
        pdf.paragraph(text, c_x + 12, y_c - 10, c_w - 24, line_height=10.2, font="F1", size=6.8, rgb=TEXT_MUTED)

    c1_w, c2_w = 348, 348
    c1_x, c2_x = 32, 412
    c1_y, c1_h = 48, 332

    # ==========================================
    # PLATE 01: LEGISLATIVE BASTION & SANCTITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE LEGISLATIVE BASTION & SANCTITY OF LINEAGE",
        "Pillars 1 & 2: Mandatory Statutes, Deterrence of Zina, Four Eyewitnesses & The Li'an Procedure",
        "PLATE 01 : SANCTITY & PROCEDURE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: MANDATORY ORDINANCES & DEFENSE OF HONOR", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Faradhnaha, Deterrence of Immorality, Four Witnesses & Triple Sanction", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Obligatory Descent (Faradhnaha)",
              "The solemn divine preface establishing the surah's legal statues as mandatory foundations for societal preservation.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Deterrence of Immorality",
              "Enforcing rigorous judicial sanctions against public promiscuity to safeguard marital fidelity and family lineage.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Evidentiary Rigor of Four Witnesses",
              "Mandating four upright eyewitnesses to permanently shield innocent reputations from malicious, unsubstantiated slander.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Triple Sanction of Qadhf",
              "Eighty lashes, lifelong disqualification of testimony, and moral censure for anyone who broadcasts unproven accusations.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: JUDICIAL RESOLUTION & SOLEMN OATHS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Li'an Institution, Four Oaths of Truth, The Fifth Curse & Divine Grace", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Institution of Li'an",
              "A dignified judicial procedure for spouses where external eyewitnesses cannot exist, resolving accusations with solemn oaths.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Four Oaths of Solemn Testimony",
              "Swearing four times by Allah to the veracity of the claim, establishing judicial equality between husband and wife.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "The Fifth Oath of Divine Curse and Wrath",
              "Invoking the wrath or curse of Allah upon oneself if untruthful, piercing false claims with terrifying spiritual weight.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Cushion of Divine Compassion",
              "Remembering that without divine grace and mercy, human households would unravel under suspicion and mutual enmity.")

    # ==========================================
    # PLATE 02: THE ORDEAL OF SLANDER
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE ORDEAL OF SLANDER & COMMUNAL ETHICS",
        "Pillars 3 & 4: Hadith al-Ifk, Bal Huwa Khayrun Lakum, Wholesome Presumption & Abu Bakr's Pardon",
        "PLATE 02 : SLANDER & FORGIVENESS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: HADITH AL-IFK & ETHICAL VINDICATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Hypocrites' Smear, Bal Huwa Khayrun Lakum, Presumption of Good & Buhtan", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Smear Campaign of the Hypocrites",
              "An engineered lie manufactured by Abdullah ibn Ubayy to strike the prophetic household and destabilize community trust.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Divine Re-Evaluation (Khayrun Lakum)",
              "The profound axiom that severe spiritual crucibles expose hypocrisy, purify faith, and elevate the righteous eternally.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Duty of Wholesome Presumption",
              "The mandatory obligation upon hearing rumors to think well of fellow believers and uphold their pristine honor.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Subhanaka Hadha Buhtanun 'Adheem",
              "The required verbal defense: glorifying Allah and rejecting unverified gossip as a monstrous and colossal falsehood.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: TOXIC TONGUES & ABU BAKR'S PARDON", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Casual Gossip, Spreading Scandals, Ala Tuhibboon & Returning Good for Evil", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Poison of the Casual Tongue",
              "Denouncing the careless repetition of gossip, treating as trivial on the tongue what is monumental and grave with Allah.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Warning Against Love of Scandals",
              "Severe condemnation for those who relish circulating rumors and broadcasting moral scandals among the faithful.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Abu Bakr's Supreme Pardon (Ala Tuhibboon)",
              "Restoring financial charity to a slanderer upon hearing the divine question: 'Do you not love that Allah forgive you?'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Returning Grace for Grievance",
              "Reaching the pinnacle of Ihsan: overcoming personal hurt to pardon those who wronged family, earning divine forgiveness.")

    # ==========================================
    # PLATE 03: DOMESTIC PRIVACY & MODESTY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "DOMESTIC PRIVACY & PROTOCOLS OF MODESTY",
        "Pillars 5 & 6: Etiquettes of Isti'dhan, Turning Back Gracefully, Lowering the Gaze & The Veil",
        "PLATE 03 : PRIVACY & MODESTY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 05: INVIOLABILITY OF THE HOME (ISTI'DHAN)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Seeking Permission, Greetings of Peace, Turning Back & Domestic Sanctity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Etiquette of Entering Dwellings",
              "Seeking explicit permission and extending warm greetings of peace before crossing the threshold of any residence.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Graceful Acceptance of Refusal",
              "Departing immediately without offense, wounded pride, or resentment when informed that hosts are unable to receive.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Safeguarding Domestic Solitude",
              "Establishing the private household as a sacred sanctuary of emotional security, moral safety, and family intimacy.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Sensible Public Exemptions",
              "Clarifying legal exemptions for entering uninhabited structures, trade depots, and public accommodations without prior notice.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 06: LOWERING THE GAZE & NOBLE MODESTY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ghadhdh al-Basar, Purity of Soul, Drawing Khumur & Facilitating Marriage", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Lowering the Gaze for Men",
              "Restraining visual curiosity as the primary defense against lust, cultivating profound internal tranquility and sweetness of faith.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Lowering the Gaze for Women",
              "Commanding believing women to protect their modesty, restrain their sight, and preserve the sanctity of their hearts.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Drawing the Outer Veil (Khumur)",
              "Draping head-coverings over bodices to conceal adornments from non-mahram eyes, defending female dignity against objectification.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Facilitating Virtuous Marriages",
              "Urging the community to marry the single and righteous servants, trusting Allah to enrich them from His boundless bounty.")

    # ==========================================
    # PLATE 04: AYAH AN-NUR (LIGHT UPON LIGHT)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "AYAH AN-NUR : THE METAPHYSICS OF LIGHT",
        "Pillars 7 & 8: The Niche, The Crystal Glass, The Radiant Lamp, The Blessed Olive Tree & Light Upon Light",
        "PLATE 04 : LIGHT UPON LIGHT"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 07: THE PARABLE OF DIVINE ILLUMINATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Noorus-Samawati, Mishkat of the Chest, Zujajah Heart & The Blessed Olive", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Light of the Heavens and Earth",
              "Allah is the Creator and Illuminator of the cosmos, the ultimate Source of physical radiance and spiritual revelation.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Niche and the Crystal Glass",
              "The believer's chest providing sanctuary for the crystal heart, clear and untainted by worldly corruption and pride.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "The Lamp of Eternal Revelation",
              "The radiant flame of monotheism and prophetic guidance burning brightly within the vessel of the pure heart.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Blessed Unshaded Olive Tree",
              "Primordial uncorrupted fitrah receiving cosmic light from dawn to dusk, producing oil of peerless clarity and refinement.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 08: LIGHT UPON LIGHT & DIVINE GUIDANCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Glowing Without Fire, Noorun 'Ala Noor, Guided Souls & Master of Parables", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Spontaneous Glow Without Fire",
              "The innate fitrah so instinctively aligned with truth that its oil nearly radiates before external revelation touches it.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Noorun 'Ala Noor (Light Upon Light)",
              "The sublime ignition of uncorrupted human nature by divine scripture, generating blazing, multi-layered spiritual brilliance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Selection for Divine Illumination",
              "Allah guiding to His transcendent light whoever approaches with sincere repentance, humility, and moral readiness.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Omniscient Master of Parables",
              "God illuminating human intellects through profound metaphors, possessing exhaustive knowledge of all dimensions.")

    # ==========================================
    # PLATE 05: HOUSES OF LIGHT & DARKNESS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "HOUSES OF LIGHT & PARABLES OF DARKNESS",
        "Pillars 9 & 10: Sanctuaries of Dhikr, Men Undistracted, The Desert Mirage & The Oceanic Abyss",
        "PLATE 05 : SANCTUARIES & SHADOWS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 09: SANCTUARIES OF ELEVATED REMEMBRANCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Buyutin Adhina Allah, Unbroken Remembrance, Overturning Day & Bounty", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Houses Elevated for Divine Praise",
              "Sacred mosques authorized by Allah to elevate His holy name, resounding with glorification at morning and evening.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Men Undistracted by Commerce",
              "Marketplace professionals and merchants whose trade, sales, and wealth never divert them from prayer and zakah.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Awe of the Overturning Day",
              "Living with reverent vigilance, mindful of the Day when hearts and eyes will overturn in terror before the Sovereign.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Reward Beyond Human Calculation",
              "The divine guarantee to reward the sincere for their finest deeds and multiply blessings beyond all human measure.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 10: THE TWIN PARABLES OF DISBELIEF", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Desert Mirage, Immediate Reckoning, The Oceanic Abyss & Deprived of Light", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Mirage of Disbelievers' Deeds",
              "Earthly works performed without Tawhid appearing like shimmering water, evaporating completely upon arrival into eternity.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Immediate Divine Accounting",
              "The shocking reality of the deluded traveler finding Allah present at the mirage, settling accounts with rigorous justice.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "The Oceanic Abyss of Darkness",
              "Deep-sea darkness enveloped in sub-surface waves, surface swells, and storm clouds, producing layered intellectual blindness.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Deprived of Divine Illumination",
              "The definitive spiritual verdict: whomever Allah grants no light possesses no guidance or illumination anywhere in reality.")

    # ==========================================
    # PLATE 06: COSMIC LITURGY & RAIN
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "COSMIC LITURGY & METEOROLOGICAL WONDERS",
        "Pillars 11 & 12: Winged Flocks in Prayer, Cloud Factory, Blinding Lightning & The Matrix of Water",
        "PLATE 06 : COSMOS & ATMOSPHERE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: THE UNIVERSAL HYMN OF CREATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Cosmic Praise, Winged Flocks, Unique Liturgy & Sovereign Return", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Cosmic Glorification Across Realms",
              "Every celestial orb, atom, and living organism engaged in unceasing, conscious glorification of their Maker.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Winged Flocks in Synchronized Praise",
              "Birds soaring in disciplined flight patterns across the sky, each entity fully cognizant of its prayer and glorification.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Sovereign Ownership of the Cosmos",
              "To Allah alone belongs the absolute dominion of the heavens and earth, and to Him all creation journeys home.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Total Omniscient Awareness",
              "Exhaustive divine consciousness tracking every flutter of wings, falling drop, and whispered prayer across all worlds.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 12: ATMOSPHERIC DYNAMICS & WATER MATRIX", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Cloud Herding, Stacked Rukaman, Blinding Flash & Every Beast from Water", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Herding and Joining Cloud Masses",
              "Gently driving dispersed atmospheric vapor, weaving it together, and piling it into towering cumulus mountains.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Rain and Hail from Mountain Clouds",
              "Releasing life-giving showers from cloud chasms while striking or withholding frozen hail by sovereign decree.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Blinding Flash of Lightning",
              "Electrifying atmospheric flashes illuminating night skies, nearly snatching away human eyesight in trembling awe.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Creation of Every Beast from Water",
              "The universal biological law: all animal life generated from water, manifesting across diverse locomotive designs.")

    # ==========================================
    # PLATE 07: ARBITRATION & ISTIKHLAF
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "ARBITRATION OF TRUTH & AYAT AL-ISTIKHLAF",
        "Pillars 13 & 14: Sickness of Hypocrites, Sami'na wa Ata'na, The Charter of Succession & Security Exchanged",
        "PLATE 07 : ARBITRATION & ISTIKHLAF"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 13: HYPOCRISY VS SAMI'NA WA ATA'NA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Evasion of Rulings, Sickness of Hearts, Unconditional Hearing & True Success", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Selective Evasion of Divine Law",
              "Hypocrites fleeing from divine arbitration when truth challenges their self-interest, but rushing forward if it benefits them.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Chronic Sickness of Corrupt Hearts",
              "Exposing the internal disease of those who harbor unfounded suspicions that Allah and His Messenger will judge unfairly.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "The Believers' Call: Sami'na wa Ata'na",
              "The sole response of the faithful upon summons to divine law: 'We hear and we obey' with unconditional loyalty.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Truly Triumphant (Al-Muflihoon)",
              "Attaining ultimate cosmic flourishing and paradise through sincere obedience, reverent fear, and constant taqwa.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: THE DIVINE CHARTER OF SUCCESSION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ayat al-Istikhlaf, Consolidating Religion, Fear to Security & Pure Tawhid", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "The Divine Promise of Succession",
              "The inviolable covenant granting righteous believers leadership and ethical stewardship upon the earth.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Consolidation of the Chosen Religion",
              "Firmly establishing the Islamic way of life, empowering institutions of justice, compassion, and divine order.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "Exchanging Fear for Enduring Security",
              "Transforming historical persecution and vulnerability into lasting peace, civilizational stability, and safety.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Condition of Pure Monotheism",
              "Succession conditioned exclusively upon worshipping Allah alone, purging every trace of idolatry and compromise.")

    # ==========================================
    # PLATE 08: DOMESTIC ETIQUETTE & DECORUM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "DOMESTIC ETIQUETTE & PROPHETIC REVERENCE",
        "Pillars 15 & 16: Three Hours of Privacy, Communal Dining, Decorum of the Assembly & Sovereign Omniscience",
        "PLATE 08 : ETIQUETTE & REVERENCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 15: THREE HOURS OF HOUSEHOLD PRIVACY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Pre-Dawn Fajr, Midday Undress, After 'Isha & Communal Dining Ease", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Three Hours of Domestic Privacy",
              "Requiring young children and servants to seek permission before entering private chambers during sensitive hours.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Before Dawn and Midday Rest",
              "Protecting marital modesty before the Fajr prayer and during afternoon rest when outer garments are removed.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "After the Night Prayer of 'Isha",
              "Shielding master bedrooms during nighttime retirement, embedding intuitive modesty across the family culture.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Social Dining Without Constraint",
              "Removing artificial barriers around sharing food with family, friends, and the vulnerable in warmth and fraternity.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: PROPHETIC DECORUM & FINAL WARNING", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sacred Address, No Stealthy Departures, Danger of Dissent & Total Knowledge", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Sacred Address of the Messenger",
              "Forbidding the faithful from calling upon the Prophet casually as they call one another, upholding transcendent respect.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "Stealthy Departures Censured",
              "Censuring those who slip away secretly from communal consultations under false pretenses without formal leave.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Peril of Opposing His Command",
              "A grave warning to anyone who dissents from the Prophet's orders, risking severe spiritual trials and painful torment.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Sovereign Knowledge of All Affairs",
              "The closing seal: to Allah belongs all that is in the heavens and earth, and to Him all souls return for accounting.")

    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF successfully compiled at: {OUTPUT_PDF}")

    # Generate Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/nur_page"
    subprocess.run(cmd, shell=True, check=True)
    print("PNG Previews rendered in previews directory.")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/nur_page-{i}.png"
        dst = os.path.join(brain_dir, f"nur_page-{i}.png")
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"  Copied {src} -> {dst} ({os.path.getsize(dst):,} bytes)")

if __name__ == "__main__":
    build_nur_pdf()
