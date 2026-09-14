#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Anbiya Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "ANBIYA_MASTER_MINDMAP.pdf")
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

def build_anbiya_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-ANBIYA", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: RECKONING & TRUTH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE IMMINENT RECKONING & THE CRUSHING OF FALSEHOOD",
        "Pillars 1 & 2: Approaching Accounting, The Heedless Trance, Cosmic Purpose & Skull-Crushing Truth",
        "PLATE 01 : RECKONING & TRUTH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE IMMINENT ACCOUNTING & HEEDLESSNESS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Iqtaraba Lin-Nasi Hisabuhum, Ghaflah, Play & Accusations of Sorcery", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Approaching Accounting (Iqtaraba)",
              "Humanity's reckoning draws rapidly nearer with each passing day, yet people remain paralyzed in spiritual heedlessness.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "The Trance of Worldly Amusement",
              "Receiving divine reminders as casual entertainment, consuming sacred truth as trivial diversion without internal reform.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Accusations of Sorcery & Poetry",
              "Deniers attempting to evade moral accountability by slandering the Messenger as an ordinary man practicing sensory deception.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Destruction of Past Rebellious Cities",
              "Ancient civilizations demanding tangible miracles, only to face immediate annihilation when they persisted in defiance.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: COSMIC TELEOLOGY & CRUSHING FALSEHOOD", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("No Idle Play, The Hurl of Truth, Skull-Crushing Blow & Angelic Praise", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Cosmos Not Created in Play (La'ibeen)",
              "The heavens and earth were engineered with profound moral purpose, completely free from frivolous entertainment or vanity.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Skull-Crushing Blow (Fa-Yadmaghuhu)",
              "Divine truth hurled against falsehood like a catastrophic projectile, fracturing its structural brain so it vanishes into dust.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Ceaseless Angelic Glorification",
              "Sublime celestial beings in divine presence glorifying Allah night and day without fatigue, slackening, or pride.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Absurdity of Multiple Deities",
              "If multiple gods ruled the heavens and earth, cosmic order would collapse in catastrophic chaos and structural ruin.")

    # ==========================================
    # PLATE 02: COSMIC ARCHITECTURE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "COSMIC ARCHITECTURE & THE ORIGIN OF LIFE",
        "Pillars 3 & 4: The Primordial Singularity, Water Matrix, Stabilizing Pegs & Celestial Orbits",
        "PLATE 02 : COSMIC ARCHITECTURE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: THE PRIMORDIAL SINGULARITY & WATER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ratqan Fa-Fataqnahuma, Expansion & Water as Universal Matrix", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Primordial Fused Mass (Ratq)",
              "The heavens and earth initially existed as a singular continuous entity before divine omnipotence cleaved them apart.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Water as the Matrix of Life",
              "Establishing the universal biological law that every living organism is biochemically constituted of and sustained by water.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "Stabilizing Mountain Pegs (Rawasiya)",
              "Deeply rooted geological formations balancing planetary crusts, preventing the earth from violent seismic shaking.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Highways Through Mountain Passes",
              "Carving accessible mountain valleys and geographical conduits so humanity may navigate and traverse the globe.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: CELESTIAL CANOPY & UNIVERSAL MORTALITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Saqfan Mahfoodha, Celestial Orbits, Kullu Nafsin Dha'iqah & Fitnah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Protected Ceiling (Saqfan Mahfoodha)",
              "Atmospheric and magnetospheric vault shielding terrestrial life from lethal cosmic radiation and solar projectiles.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Celestial Bodies Swimming in Orbits",
              "The sun and moon navigating precise celestial paths, swimming in cosmic orbits governed by mathematical harmony.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Universal Mortality (Dha'iqatu al-Mawt)",
              "Every single soul without exception is destined to taste biological death, stripping away illusions of permanence.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Testing Through Ease & Adversity",
              "Life structured as a comprehensive moral crucible, trying humanity through hardship, wealth, health, and temptation.")

    # ==========================================
    # PLATE 03: SCALES & ICONOCLASM
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE SCALES OF JUSTICE & IBRAHIM'S ICONOCLASM",
        "Pillars 5 & 6: Mawazeena al-Qist, The Mustard Seed, Ibrahim's Discernment & Smashed Statues",
        "PLATE 03 : SCALES & ICONOCLASM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 05: THE SCALES OF ABSOLUTE JUSTICE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Mawazeena al-Qist, The Mustard Seed & Humanity Created of Haste", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Humanity Created of Haste ('Ajal)",
              "Human nature plagued by impatience, demanding immediate outcomes and mocking the timing of divine judgment.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Sudden Surrounding of Retribution",
              "The punishment they mockingly demanded arriving unexpectedly, paralyzing deniers in speechless shock.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Scales of Equity (Mawazeena al-Qist)",
              "Objective balances established on Judgment Day, measuring deeds with infallible divine justice without bias.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Accounting Down to the Mustard Seed",
              "Even an action, thought, or deed weighing no more than a tiny mustard seed is retrieved and placed upon the scale.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 06: IBRAHIM'S SOCRATIC REBELLION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Rushd in Youth, Socratic Interrogation & Shattering the Idols", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Spiritual Discernment in Youth (Rushd)",
              "Ibrahim endowed with innate monotheistic maturity, recognizing the irrationality of bowing before carved wood and stone.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Challenging Paternal Idolatry",
              "Courageously interrogating his father and elders regarding statues that possess zero sensory or spiritual reality.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Shattering the Statues (Jadhadhan)",
              "Entering the pagan temple during their holiday and smashing the idols into rubble, sparing only the colossal chief idol.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Dialectical Irony with the Axe",
              "Placing the axe on the chief idol's shoulder, challenging worshippers to interrogate their gods if they can speak.")

    # ==========================================
    # PLATE 04: COOL FIRE & DYNASTY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE TEMPERATE FIRE & THE LINEAGE OF IMAMS",
        "Pillars 7 & 8: Bardan wa Salaman, Delivering Ibrahim and Lut, Nafilah & Imams Guiding by Command",
        "PLATE 04 : COOL FIRE & DYNASTY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 07: THE TRANQUIL FURNACE & BLESSED EXILE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Burning Furnace, Bardan wa Salaman & Migration to Sham", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Babylonian Furnace",
              "Enraged idolaters building a massive bonfire, attempting to destroy the young iconoclast in an imperial inferno.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Coolness and Peace (Bardan wa Salaman)",
              "Divine command suspending the burning properties of fire, transforming flames into a meadow of tranquil safety.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Confounders of the Plot (Al-Akhsareen)",
              "The plotters rendered the ultimate losers, witnessing their roaring flames fail against divine protection.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Migration to the Blessed Land",
              "Delivering Ibrahim and Lut from persecution to the fertile Levant, establishing the geography of prophetic monotheism.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: PROPHETIC IMAMS GUIDING BY DECREE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ishaq, Ya'qub Nafilah, Yahdoona bi-Amrina & Active Virtue", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Posterity as Additional Gift (Nafilah)",
              "Blessing Ibrahim with Ishaq and grandson Ya'qub as an extra bounty, cementing righteous generational lineage.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Leaders Guiding by Divine Command",
              "Defining authentic prophetic leadership: guiding humanity strictly by divine authorization, not public trends.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Inspiration of Righteous Action",
              "Divinely inspired to perform charitable deeds, establish regular prayer, and distribute social purifying zakah.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Deliverance of Lut and Nuh",
              "Lut rescued from the depraved city of abominations, and ancient Nuh delivered from the catastrophic global deluge.")

    # ==========================================
    # PLATE 05: JURISPRUDENCE & METALLURGY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "RESTORATIVE JUSTICE & CELESTIAL METALLURGY",
        "Pillars 9 & 10: The Night Flock Case, Flexible Chainmail, Dawud's Chorus & Sulayman's Sovereignty",
        "PLATE 05 : JURISPRUDENCE & METALLURGY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 09: JURISPRUDENTIAL HARMONY OF TWO KINGS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Midnight Vineyard Flock, Dawud's Judgment & Sulayman's Insight", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Midnight Flock in the Vineyard",
              "Sheep grazing unattended into an enclosed vineyard at night, consuming crops and damaging trellises.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Dawud's Compensatory Ruling",
              "Dawud awarding the entire flock to the vineyard owner as equal financial compensation for the destroyed harvest.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Sulayman's Restorative Justice",
              "Sulayman proposing temporary usufruct of sheep while the shepherd rehabilitates the vineyard, healing both parties.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Divine Praise for Both Jurists",
              "Affirming both prophets possessed wisdom and knowledge, honoring sincere ijtihad even across varying levels of insight.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 10: NATURE SUBORDINATED & FLEXIBLE ARMOR", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Mountains Singing Praises, Interlocking Chainmail & Tempest Winds", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Singing Chorus of Mountains",
              "Subordinating towering peaks and migrating birds to echo morning and evening glorifications alongside Dawud's voice.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "The Invention of Chainmail (Laboos)",
              "Teaching Dawud the craft of weaving interlocking iron rings into flexible armor that shields life in battle.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Sovereignty Over the Tempest (Sulayman)",
              "Raging desert winds harnessed to blow peacefully under Sulayman's command toward the blessed land.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Subjugation of the Diving Jinn",
              "Supernatural beings subordinated under state authority to dive for ocean treasures and construct public monuments.")

    # ==========================================
    # PLATE 06: PATIENCE & DELIVERANCE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "AYYUB'S AFFLICTION & DHUN-NUN'S LITANY",
        "Pillars 11 & 12: Ayyub's Courteous Plea, Removal of Harm, Whale's Belly & La Ilaha Illa Anta",
        "PLATE 06 : PATIENCE & DELIVERANCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 11: AYYUB'S COURTESY IN AFFLICTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Massaniya ad-Durr, Supreme Modesty & Complete Restoration", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Touch of Adversity (Massaniya ad-Durr)",
              "Ayyub phrasing eighteen years of agony as a mere touch, refusing to complain or express bitterness toward God.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Appealing to the Most Merciful",
              "Invoking Ar-Rahman's supreme compassion rather than dictating solutions, displaying sublime spiritual courtesy.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Immediate Removal of Harm (Kashafna)",
              "Divine response stripping away all disease, restoring vibrant physical vitality and spiritual wholeness.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Restoring the Doubled Family",
              "Rebuilding his family and wealth twofold as a tangible divine mercy and eternal reminder for all worshippers.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: DHUN-NUN'S DELIVERANCE FROM THE ABYSS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Triple Darkness, Tripartite Formula & Universal Shield for Believers", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Departing in Anger & The Whale",
              "Yunus departing in frustration, swallowed by a giant sea beast into the pitch black of the ocean depths.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Cry from the Triple Darkness",
              "Calling out from the belly of the whale, beneath ocean currents, under the starless night, stripped of all ego.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Tripartite Formula of Liberation",
              "Proclaiming Tawhid, declaring God's absolute freedom from injustice (Subhanaka), and confessing personal wrongdoing.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Universal Guarantee for Believers",
              "The divine promise: 'Thus do We deliver the believers'—an eternal formula rescuing any desperate soul in crisis.")

    # ==========================================
    # PLATE 07: INHERITANCE & PURITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "ZAKARIYYA'S HEIR & THE SANCTITY OF MARYAM",
        "Pillars 13 & 14: Rabbi La Tadharni Fardan, Healing Barrenness, Maryam's Purity & The Single Ummah",
        "PLATE 07 : INHERITANCE & PURITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 13: ZAKARIYYA & THE CURED BARRENNESS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Not Leaving Alone, Khayr al-Waritheen, Healing Wife & Racing to Good", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Solitary Plea (La Tadharni Fardan)",
              "Zakariyya supplicating: 'My Lord, leave me not childless, while You are the best of inheritors.'")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Healing the Barren Wife",
              "Divine physiological intervention correcting biological infertility in elderly spouse to conceive Yahya.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Racing to Righteous Deeds",
              "Defining the spiritual psychology of the household: hastily competing in charitable works and noble deeds.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Supplicating in Hope & Awe (Raghaban)",
              "Balancing heartfelt yearning for divine bounty with trembling reverence, living in constant humble submission.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 14: MARYAM'S CHASTITY & THE UNIFIED UMMAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Chaste Fortress, Breathing of the Spirit, Universal Sign & Single Ummah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Guarding Her Chastity (Ahsanat Farjaha)",
              "Maryam guarding her absolute purity, establishing an unshakeable fortress of virtue against societal corruption.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Breathing of the Divine Spirit",
              "Archangel Jibril breathing the divine command, inaugurating the fatherless miraculous conception of Isa.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "An Eternal Sign for Creation",
              "Making Maryam and her virgin-born son a cosmic sign of omnipotence and mercy across human generations.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "The Single Unified Nation (Ummatan Wahidah)",
              "Proclaiming that all prophets brought one identical monotheistic community, condemned when humans splinter.")

    # ==========================================
    # PLATE 08: ESCHATOLOGY & MERCY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "GOG AND MAGOG & THE UNIVERSAL MERCY",
        "Pillars 15 & 16: Yajuj and Majuj, Righteous Heirs in Psalms, Rolling Heavens & Rahmatan lil-'Alameen",
        "PLATE 08 : ESCHATOLOGY & MERCY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 15: ESCHATOLOGICAL SWARMS & RIGHTEOUS HEIRS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Yajuj and Majuj Swarming, Staring Eyes, Psalms Promise & Earth Inheritance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Swarming of Yajuj and Majuj",
              "The barrier breached as the Hour nears, ferocious hordes surging down from every elevated ridge.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "The Staring Eyes of Terror",
              "The true promise drawing near, paralyzing deniers with unblinking staring eyes of overwhelming dread.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Rolled Celestial Scrolls",
              "The heavens folded on the Day of Resurrection like a scribe rolling up parchment scrolls, recreating all.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "The Righteous Inherit the Earth",
              "Eternal decree inscribed in the Psalms and divine tablets: the ultimate inheritance belongs to righteous servants.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: THE UNIVERSAL EMBRACE OF MERCY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Rahmatan lil-'Alameen, Sufficiency of Worship, Invocations of Truth & Ar-Rahman", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "A Message for Sincere Worshippers",
              "The Qur'an serving as a sufficient proclamation and roadmap of salvation for those committed to divine worship.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "Mercy to All the Worlds (Rahmatan)",
              "The supreme commission of Muhammad: an all-encompassing, tender mercy embracing humanity, animals, and cosmos.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Rejection of Forced Faith",
              "Announcing clear truth without coercion: 'I have proclaimed to you all equally, though I know not when the Hour strikes.'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Judge with Truth (Ihkum bil-Haqq)",
              "The concluding prayer: 'My Lord, judge with truth! And our Lord is Ar-Rahman, whose help is sought against all slander.'")

    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF successfully compiled at: {OUTPUT_PDF}")

    # Generate Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/anbiya_page"
    subprocess.run(cmd, shell=True, check=True)
    print("PNG Previews rendered in previews directory.")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/anbiya_page-{i}.png"
        dst = os.path.join(brain_dir, f"anbiya_page-{i}.png")
        if os.path.exists(src):
            shutil.copyfile(src, dst)
    print("PNG Previews successfully copied to brain directory.")

if __name__ == "__main__":
    build_anbiya_pdf()
