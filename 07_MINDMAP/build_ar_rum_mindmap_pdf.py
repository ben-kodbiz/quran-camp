#!/usr/bin/env python3
"""
Huurs Studio - Surah Ar-Rum Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
Strict Brand_Visual_System.md & Absolute Copyright Insulation
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AR_RUM_MASTER_MINDMAP.pdf")
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

def build_ar_rum_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AR-RUM", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: GEOPOLITICAL PROPHECY & SOVEREIGNTY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE GEOPOLITICAL PROPHECY & DIVINE SOVEREIGNTY",
        "Pillars 1 & 2: Ghulibati ar-Room, Lowest Land Elevation, Bid'i Sineen & Synchronized Joy of Badr",
        "PLATE 01 : THE ROMAN LEVANT"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: BYZANTINE DEFEAT & REVERSAL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ghulibati ar-Room, Adna al-Ard & The Exact Time Window", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Fall of Byzantine Rome",
              "Alif-Lam-Meem. The Romans were routed by Sasanian Persia, losing Jerusalem and the Levant, causing pagan Quraysh to gloat in Mecca.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Lowest Land on Earth (Adna al-Ard)",
              "Fought in the nearest Levantine frontier, precisely in the Dead Sea depression representing the lowest terrestrial elevation on earth.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Definite Timeline: Bid'i Sineen",
              "A miraculous prophecy predicting the total reversal and Roman victory within Bid' (3 to 9 years) when Rome seemed utterly destroyed.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Sovereignty of the Divine Command",
              "To Allah belongs the entire command before and after; worldly superpowers rise and fall strictly by divine appointment.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: SYNCHRONIZED JOY & HEEDLESSNESS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Badr Concurrence, Surface Knowledge & The Eternal Reality", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Synchronized Victory at Badr",
              "Heraclius crushed the Persians at Nineveh precisely as the vulnerable Muslims triumphed at Badr, fulfilling the joy of the believers.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Rejoicing in Divine Assistance",
              "The believers rejoiced not in Roman imperialism, but in the manifest victory of divine truth and the vindication of prophecy.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Surface Mechanics of Dunya (Zahiran)",
              "Secular minds master the external engineering of technology and trade, yet remain entirely heedless of the metaphysical Hereafter.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Inviolable Divine Promise",
              "Allah never breaches His covenant; the superficial cycles of history unfold toward the ultimate accountability of the soul.")

    # ==========================================
    # PLATE 02: LITURGICAL PRAISE & DUST GENESIS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "LITURGICAL PRAISE & THE GENESIS FROM DUST",
        "Pillars 3 & 4: Daily Liturgical Stations of Prayer, Extracting Living from Dead & Creation from Soil",
        "PLATE 02 : THE LITURGICAL RHYTHM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: THE LITURGICAL CYCLE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Heena Tumsoon wa Tusbihoon, The Five Daily Prayers & Life/Death", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "Doxology at Evening & Morning",
              "Glorify Allah at twilight (Maghrib/Isha) and dawn (Fajr), anchoring human existence in the astronomical rhythms of the cosmos.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Praise at Midday & Late Afternoon",
              "Praise Him in the heavens and earth, in the late afternoon ('Asr) and at high noon (Dhuhr), weaving prayer through worldly toil.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "Extracting the Living from the Dead",
              "He brings the living bird from an inanimate egg, the faithful believer from a disbelieving lineage, and green shoots from arid earth.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Extracting the Dead from the Living",
              "He causes mortality to emerge from vitality, demonstrating absolute divine mastery over biological and spiritual lifecycles.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 04: SIGN 1: GENESIS FROM DUST", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Common Soil, The Inbreathing of Spirit & Multiplying Humanity", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Created from Inanimate Soil (Turab)",
              "Human physical architecture is formed of ordinary terrestrial clay minerals—carbon, calcium, and water—possessing zero self-will.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Explosion of Sentient Beings",
              "Then behold: you become dynamic, articulate, reproducing human beings dispersing across continents, nations, and oceans.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Biological Complexity from Clay",
              "The synthesis of nervous systems, consciousness, emotion, and intellect from silent soil stands as an undeniable empirical sign.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Fallacy of Random Emergence",
              "Inanimate soil cannot engineer consciousness or purposeful reproduction; human existence is an intentional divine design.")

    # ==========================================
    # PLATE 03: MATRIMONIAL SANCTUARY & DIVERSITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "MATRIMONIAL SANCTUARY & LINGUISTIC WONDERS",
        "Pillars 5 & 6: Signs 2 & 3: Spouses for Tranquility, Mawaddah & Rahmah, Languages & Racial Pigments",
        "PLATE 03 : SANCTUARY & DIVERSITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 05: SIGN 2: MATRIMONY & SAKINAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Mates from Yourselves, Soul Sanctuary, Mawaddah & Rahmah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Spouses from Common Essence",
              "Created mates from your own species and nature so that neither feels alienated, establishing intrinsic emotional resonance.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Sanctuary of Tranquility (Sakinah)",
              "Marriage is designed as a peaceful psychological shelter where souls decompress from the exhaustion and coldness of the world.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Divine Seed of Love (Mawaddah)",
              "Active affection, warmth, and joy personally placed by Allah between hearts, elevating marriage beyond a sterile legal contract.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Self-Sacrificing Mercy (Rahmah)",
              "When youth and health fade, compassion and gentle forgiveness sustain the bond through illness, hardship, and old age.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: SIGN 3: TONGUES & COMPLEXIONS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Heavens & Earth, Diversity of Tongues & Complexions as Divine Art", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Vast Cosmic Canvas",
              "The creation of celestial heavens and the terrestrial earth sets the stage for the flourishing of human anthropological wonders.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Miraculous Diversity of Tongues",
              "From identical vocal cords and alphabets emerge thousands of distinct spoken languages, idioms, and expressive musicalities.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "The Spectrum of Human Colors",
              "Endless variations in melanin, skin pigments, and facial features dismantle racist supremacy, standing as signs of divine artistry.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Signs for People of Sound Knowledge",
              "Diversity is not a curse of division, but a masterpiece to be studied and celebrated by the enlightened mind.")

    # ==========================================
    # PLATE 04: SLEEP, LIGHTNING & THE SUMMONS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "SLEEP, LIGHTNING & THE COSMIC SUMMONS",
        "Pillars 7 & 8: Signs 4, 5 & 6: Circadian Reset, Lightning for Fear & Hope, Pillars of Sky & The Resurrection Summons",
        "PLATE 04 : COSMIC CYCLES"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 07: SIGN 4: CIRCADIAN RESTORATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sleep by Night and Day, Neurobiological Reset & Seeking Bounty", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Restorative Sleep (Manamukum)",
              "The biological miracle of sleep: voluntary muscles surrender, consciousness pauses, and the body regenerates without conscious effort.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Minor Death (Al-Wafat as-Sughra)",
              "Every night the soul enters a temporary suspension, foreshadowing the final departure and teaching human dependence.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Awakening to Divine Bounty",
              "Re-emerging into waking consciousness to pursue honest trade, creative work, and worship as stewards of divine provision.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "A Sign for Those Who Listen",
              "The delicate biological balance of day and night rhythms offers profound guidance for those who genuinely pay heed.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 08: SIGNS 5 & 6: LIGHTNING & SUMMONS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Atmospheric Flash, Rain Revival, Sky Stability & The Single Call", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Lightning in Fear and Hope (Barq)",
              "The blinding electrical strike balances terror of devastation with eager anticipation of life-giving agricultural rain.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Reviving the Desiccated Earth",
              "Dead, cracked desert soil awakens with vibrant botanical life within hours of rainfall, demonstrating effortless revival.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Pillars of Divine Command (Amr)",
              "Planetary bodies and the vast sky remain in precise equilibrium without visible pillars, held purely by divine ordinance.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Single Summons (Da'watan)",
              "At the appointed hour, a single celestial call from the earth causes billions of slumbering dead to emerge instantaneously.")

    # ==========================================
    # PLATE 05: THE PRIMORDIAL FITRAH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE PRIMORDIAL FITRAH & UNALTERED NATURE",
        "Pillars 9 & 10: Directing Face to Upright Deen, Fitrata Allah, Unalterable Design & The Born Monotheist",
        "PLATE 05 : THE PRIMORDIAL FITRAH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 09: THE FACTORY SETTING OF FAITH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Aqim Wajhaka Haneefan, Fitrata Allah & Intrinsic Monotheism", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Direct Your Face Upright (Haneefan)",
              "Align your total consciousness toward the true faith; Islam is not an alien cultural construct but your soul's native home.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Primordial Disposition (Fitrah)",
              "The innate moral and spiritual constitution upon which Allah created all human beings, intuitively acknowledging one Creator.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Unalterable Design (La Tabdeela)",
              "No alteration can erase the divine creation; though sins and ideologies veil it, the Fitrah remains indelible beneath the surface.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Correct & Enduring Religion",
              "This is the upright, permanent Deen matching reality itself, though the majority of secular humanity lives in ignorance.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 10: THE PRISTINE INFANT & VEILS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Every Child on Fitrah, Cultural Amputations & Turning in Repentance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Born Upon Unblemished Purity",
              "The Prophet affirmed: Every newborn enters existence upon the pure Fitrah, free of inherent corruption, original sin, or taint.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "External Societal Amputations",
              "Parental and cultural indoctrination impose false dogmas upon the child, like mutilating the ears of a whole, healthy beast.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Turning Constantly in Tawbah (Munibeen)",
              "The call to re-awaken the Fitrah by turning back to Allah in sincere repentance, establishing prayer and guarding God-consciousness.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "The Cure for Modern Alienation",
              "Spiritual emptiness and consumer anxiety are symptoms of Fitrah-homesickness; peace is found only in returning to the Source.")

    # ==========================================
    # PLATE 06: SECTARIANISM & MARITIME DELUSION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "SECTARIAN TRIBALISM & THE MARITIME CRISIS",
        "Pillars 11 & 12: Fragmented Religion, Factions Rejoicing in Dogma, The Ship in Tempest & Coastal Denial",
        "PLATE 06 : SECTARIAN FRAGMENTATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 11: THE SECTARIAN BLIGHT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Prohibition of Shirk, Fragmenting Deen & Factions in Vanity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Prohibition of Hidden Shirk",
              "Do not associate partners with Allah, which includes elevating partisan tribal agendas above universal divine truth.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Splintering into Hostile Sects (Shiya'an)",
              "Severe condemnation of those who tear religious brotherhood into competing, mutually excommunicating sects.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Each Faction Boasting in Its Dogma",
              "Every party rejoices in its narrow factional opinions (Kullu Hizbin Farihoon), blinded by self-righteous arrogance.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "The Universal Quranic Umbrella",
              "True faith dissolves insular tribalism, uniting humanity upon the expansive foundation of the Qur'an and authentic Sunnah.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: THE MARITIME REALITY CHECK", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Affliction at Sea, Pure Monotheistic Sincerity & Coastal Reversion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Tempest of Sincerity",
              "When roaring ocean waves threaten to swallow their vessel, human arrogance dissolves; they cry out with unadulterated monotheism.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "The Temporary Collapse of Atheism",
              "In extreme mortal peril, artificial philosophical doubts vanish; the Fitrah awakens and begs the One True God for deliverance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Coastal Reversion to Shirk",
              "The moment their feet touch safe dry shore, they attribute rescue to captains, luck, or idols, reverting to heedless polytheism.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "The Disease of Ingratitude (Kufur)",
              "Disbelieving humanity enjoys divine mercy while actively denying the Giver, building their lives on selective memory.")

    # ==========================================
    # PLATE 07: ECOLOGICAL RUIN & AWAKENING
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "ANTHROPOGENIC ECOLOGICAL RUIN & AWAKENING",
        "Pillars 13 & 14: Zahara al-Fasad fil-Barr wal-Bahr, What Hands Have Earned, Tasting Consequences & The Return",
        "PLATE 07 : ECOLOGICAL IMBALANCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 13: ANTHROPOGENIC CORRUPTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Zahara al-Fasad, Land and Sea Degradation & Human Greed", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Corruption on Land and Sea (Zahara al-Fasad)",
              "Environmental degradation, resource depletion, toxic pollution, and social breakdown appear openly across the globe.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Direct Anthropogenic Cause (Bima Kasabat)",
              "These crises are not natural design flaws, but the direct consequence of what human hands have earned through greed and sin.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Breaking the Ecological Equilibrium",
              "Plundering natural resources, polluting oceans, and poisoning skies violate the sacred trust of earthly stewardship (Khilafah).")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Mirror of Moral Corruption",
              "Outer environmental chaos directly mirrors inner human spiritual corruption; abandoning God leads to destroying the earth.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 14: DIVINE PEDAGOGY & AWAKENING", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Tasting Consequences (Ba'da Alladhi 'Amiloo) & That They May Return", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Tasting a Fraction of Consequences (Ba'da)",
              "In mercy, Allah lets humanity taste only a small fraction of their misdeeds, withholding total annihilation to allow repentance.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Crises as Merciful Alarm Bells",
              "Droughts, famines, and ecological breakdowns serve as divine wake-up calls, breaking the trance of consumer arrogance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Ultimate Goal: That They Return",
              "The sole purpose of divine trials is spiritual restoration: La'allahum Yarji'oon—that humanity might return to justice and worship.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Witnessing the Ruins of Prior Exploiters",
              "Travel the earth and observe the end of those before: civilizations with greater military and economic might were erased.")

    # ==========================================
    # PLATE 08: ATMOSPHERIC RAIN & UNSHAKEABLE SABR
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "ATMOSPHERIC REVIVAL & THE SEASONS OF LIFE",
        "Pillars 15 & 16: Winds of Mercy, Resurrection from the Soil, Three Stages of Biology & Unshakeable Sabr",
        "PLATE 08 : THE FINAL STEADFASTNESS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 15: THE ATMOSPHERIC ENGINE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Winds as Heralds, Cloud Physics & The Vegetation Rebirth", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Winds as Joyous Heralds (Mubashshirat)",
              "Atmospheric wind systems circulate oceanic vapors across planetary latitudes, orchestrating the global water distribution system.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "The Thermodynamic Miracle of Rain",
              "Clouds spread, stack in fragments, and release soft raindrops rather than destructive deluges, nurturing delicate seedlings.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Living Analogy of Resurrection",
              "Observe the effects of Allah's mercy: how He revives dead earth; exactly thus will He reassemble and resurrect the dead.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "The Deafness of the Willfully Blind",
              "You cannot make the dead in heart hear the call, nor guide the blind when their spiritual perception is deadened by pride.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: HUMAN SEASONS & GRANITE SABR", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Infant Weakness, Peak Strength, Gray Hair & Unshakeable Certainty", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Cycle of Human Frailty (Da'f)",
              "Created in helpless infant weakness, ascending to brief youthful vigor (Quwwah), then returning to second childhood and gray hair.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Message of Gray Hair (Shaybah)",
              "Physical aging is a divine messenger warning the soul that earthly departure is imminent; arrogance in mortal flesh is absurd.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Command to Granite Sabr (Fa-sbir)",
              "Endure with majestic patience; the promise of Allah is absolute truth, regardless of geopolitical turbulence or mockery.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Never Shaken by the Uncertain",
              "Let not those who lack unwavering certainty (La Yooqinoon) shake your footing; stand like an unyielding rock upon the Fitrah.")

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate preview PNGs
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"[OK] Generated preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/page-{i}.png"
        dst = f"{brain_dir}/ar_rum_mindmap_page_{i}.png"
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied preview to {dst}")

if __name__ == "__main__":
    build_ar_rum_pdf()
