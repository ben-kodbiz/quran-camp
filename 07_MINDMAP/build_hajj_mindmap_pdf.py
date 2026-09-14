#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Hajj Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "HAJJ_MASTER_MINDMAP.pdf")
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

def build_hajj_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-HAJJ", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: COSMIC TREMOR & RESURRECTION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE CATACLYSMIC TREMOR & PROOFS OF RESURRECTION",
        "Pillars 1 & 2: The Apocalyptic Earthquake, Stunned Humanity, Embryonic Stages & Soil Revived",
        "PLATE 01 : CATACLYSM & CREATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE COSMIC EARTHQUAKE & DISRUPTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Zalzalat al-Sa'ah, Maternal Abandonment, Intoxicated Terror & Devils", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Immense Tremor of the Hour",
              "The planetary convulsions that shatter terrestrial equilibrium, initiating cosmic reckoning and stripping human composure.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Severance of Maternal Bonds",
              "Nursing mothers abandoning their suckling infants in involuntary panic, dissolving the strongest earthly instincts of love.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Intoxicated Stupor of Dread",
              "Humanity reeling in bewildered incoherence, appearing drunk from metaphysical awe and the terrifying weight of divine majesty.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Disputation Without Divine Knowledge",
              "The intellectual bankruptcy of arguing against divine truth by blindly succumbing to every rebellious, misleading devil.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 02: BIOLOGICAL EMBRYOLOGY & BOTANICAL LIFE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Seven Gestational Stages, Ardhal al-'Umur, Vibrating Earth & Radiant Flora", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Seven-Fold Human Morphogenesis",
              "Sequential creation from dust, reproductive fluid, clinging clot, and tissue shaped and unshaped to manifest sovereign design.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Feeblest Decrepitude (Ardhal al-'Umur)",
              "Cognitive and physical regression where vast worldly knowledge is stripped away into infant-like helplessness before passing.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "The Quivering Barren Soil (Ihtazzat)",
              "Dead parched earth trembling and swelling with biological respiration upon the descent of refreshing, life-giving sky rain.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Radiant Botanical Pairs (Baheej)",
              "Barren dust bursting with flourishing, delightful flora, demonstrating the rational certainty of physical resurrection.")

    # ==========================================
    # PLATE 02: FAITH ON THE PRECIPICE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "FAITH ON THE PRECIPICE & CELESTIAL REALITIES",
        "Pillars 3 & 4: Conditional Devotion, Existential Bankruptcy, Impotent Deities & Divine Decree",
        "PLATE 02 : PRECIPICE & SOVEREIGNTY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: THE ANATOMY OF CONDITIONAL WORSHIP", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("'Ibadah 'Ala Harf, Transactional Devotion, Calamitous Inversion & Ruin", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "Faith Upon the Razor's Edge ('Ala Harf)",
              "Perching religious loyalty upon the unstable rim of temporal comfort, ready to plummet at the slightest breeze of adversity.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Contentment in Temporal Prosperity",
              "Deeming faith valid and rewarding solely when business thrives, health endures, and personal ambitions meet no friction.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Inversion of Calamity (Inqalaba)",
              "Collapsing into bitter resentment and abandoning divine servitude the instant tribulation tests sincere conviction.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Forfeiting Both Worlds (Khasira al-Dunya)",
              "The catastrophic bankruptcy of forfeiting temporal tranquility and eternal salvation through opportunistic, shallow faith.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 04: THE TRIUMPH OF DIVINE DECREE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Impotent Patrons, Evil Protectors, Sovereign Will & The Severed Cord", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Invoking the Impotent Shadows",
              "Calling upon created intermediaries that possess neither intrinsic ability to inflict harm nor sovereign power to grant aid.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Treacherous Patron and Ally",
              "Discovering that reliance upon artificial powers yields only bitter humiliation, hollow promises, and ultimate abandonment.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "The Unstoppable Divine Will",
              "Allah bringing His eternal cosmic determinations into reality with effortless sovereignty across all created dimensions.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Severed Cord of Frustration",
              "The absolute futility of raging against divine decree, where furious mortal scheming cannot halt heavenly fulfillment.")

    # ==========================================
    # PLATE 03: THE ANCIENT SANCTUARY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE ANCIENT SANCTUARY & THE ABRAHAMIC SUMMONS",
        "Pillars 5 & 6: Purifying the Ka'bah, The Liberated House, Global Adhan & Crossing Deep Ravines",
        "PLATE 03 : SANCTUARY & PILGRIMAGE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 05: PURIFYING THE ANCIENT SANCTUARY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Bawwa'na Li-Ibrahim, Purification from Shirk, Four Postures & Al-Bayt al-'Ateeq", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "The Abrahamic Foundation (Bawwa'na)",
              "Appointing the sacred site of the Ka'bah as an unshakeable cosmic anchor of uncompromising, primordial monotheism.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Decontamination from Idolatry",
              "The divine mandate to cleanse the holy precinct from the pollution of idols, pride, commercial greed, and moral decay.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Sanctuary of Four Sacred Postures",
              "Preparing the pure house for those who circumambulate, stand in contemplation, bow in reverence, and prostrate in awe.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Al-Bayt al-'Ateeq (The Liberated House)",
              "The Ancient House liberated by Allah from the proprietary ownership, political vanity, and control of worldly despots.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: THE UNIVERSAL SUMMONS (ADHAN AL-HAJJ)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Adh-dhin Fin-Nas, Lean Mounts, Fajjin 'Ameeq & Witnessing Benefits", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Global Proclamation (Adhan al-Hajj)",
              "Ibrahim commanded to proclaim the pilgrimage, with divine power ensuring the miraculous echo across continents and eras.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Arriving on Foot and Lean Mounts",
              "Longing pilgrims crossing vast arid expanses on foot and atop travel-worn mounts, stripped of luxury and worldly distinction.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "From Every Distant Chasm ('Ameeq)",
              "The global convergence of diverse languages and races funneling through deep mountain ravines toward the sacred precinct.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Witnessing Holistic Benefits (Manafi'a)",
              "Experiencing profound spiritual forgiveness, universal fraternity, and ethical, equitable commerce honoring community life.")

    # ==========================================
    # PLATE 04: SACRIFICE & METAPHYSICS OF TAQWA
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "SACRIFICIAL RITES & THE METAPHYSICS OF TAQWA",
        "Pillars 7 & 8: Veneration of Emblems, Aligned Sacrifices, Feeding Destitute & Transcendence of Flesh",
        "PLATE 04 : SACRIFICE & TAQWA"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 07: SACRED SYMBOLS & ALIGNED OFFERINGS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Appointed Days, Sha'a'ir Allah, Camels in Ranks (Sawaff) & Rites Completed", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Appointed Days of Remembrance",
              "Invoking the holy name of Allah over cattle during designated sacred days in humble gratitude for divine provision.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Veneration of Divine Symbols (Sha'a'ir)",
              "Revering sacred rites and choosing robust, magnificent offerings as a living manifestation of sincere inward piety.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Sacrificial Camels in Ranks (Sawaff)",
              "Lining up magnificent beasts in disciplined rows for sacrifice, bearing witness to human stewardship and ultimate submission.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Fulfilling Vows & The Final Tawaf",
              "Concluding the rites by purifying bodies, fulfilling solemn religious oaths, and circling the Liberated Sanctuary.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 08: SOCIO-SPIRITUAL EQUITY & TAQWA", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Al-Qani', Al-Mu'tarr, Lan Yanalallaha Luhumuha & The Heart's Currency", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Feeding the Contented Poor (Al-Qani')",
              "Distributing wholesome nourishment to the self-respecting needy who maintain quiet dignity and refrain from begging.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Succoring the Destitute (Al-Mu'tarr)",
              "Ensuring immediate compassionate relief reaches those driven by extreme impoverishment to outwardly voice their plea.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Transcending Flesh and Blood",
              "The decisive refutation of pagan notions: neither flesh nor blood ascends to the Divine; Allah is entirely Self-Sufficient.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Taqwa: The Sole Heavenly Currency",
              "Transforming external ritual slaughter into the inward immolation of ego, pride, and greed through sincere God-consciousness.")

    # ==========================================
    # PLATE 05: CHARTER OF DEFENSE & SANCTUARIES
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE CHARTER OF DEFENSE & SACRED ENCLAVES",
        "Pillars 9 & 10: Sanction for Defense, Unjust Expulsion, Countering Tyranny & Multi-Faith Sanctuaries",
        "PLATE 05 : DEFENSE & SANCTITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 09: DIVINE SANCTION AGAINST TYRANNY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Udhina Lilladhina, Unjust Eviction, Rabbunallah & Divine Victory Guaranteed", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Sanction of Defense (Udhina)",
              "Granting constitutional permission for armed struggle specifically because the faithful endured years of cruel, unprovoked wrong.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Expelled Solely for Affirming Tawhid",
              "Believers driven violently from homes and ancestral soil for no crime other than professing: 'Our Lord is Allah alone.'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "The Check on Corruption (Daf'ullah)",
              "The profound sociopolitical law wherein Allah checks destructive aggression through principled defense to preserve civil society.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Guaranteed Divine Assistance",
              "The inviolable heavenly promise that Allah unfailingly supports those who establish prayer, equity, and moral rectitude.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 10: PRESERVING SACRED HOUSES OF WORSHIP", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Sawami', Biya', Salawat, Masajid & Perpetual Remembrance of Allah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Protection of Monastic Cloisters (Sawami')",
              "Preserving the isolated hermitages where Christian monks retreat to spend their days in contemplation and devotional solitude.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Safeguarding Christian Basilicas (Biya')",
              "Shielding churches and cathedral halls where Christian congregations gather to praise the Lord of the heavens and earth.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Defending Synagogues of Prayer (Salawat)",
              "Protecting Jewish houses of worship where the sacred Torah and the name of God are reverently invoked and chanted.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Sanctity of Muslim Mosques (Masajid)",
              "Upholding mosques where bowing, prostration, and the glorification of Allah resound without cease across day and night.")

    # ==========================================
    # PLATE 06: RUINED CITADELS & BLIND HEARTS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "RUINED CITADELS & THE BLINDNESS OF THE HEART",
        "Pillars 11 & 12: Desolated Cities, Dried Wells, Fortress Ruins & The True Blindness Within",
        "PLATE 06 : RUINS & SPIRITUAL SIGHT"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 11: THE DESOLATION OF ANCIENT TYRANNIES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Rebellious Nations, Collapsed Ceilings, Abandoned Wells & Fortresses", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Prophetic Lineage of Denial",
              "Recalling the arrogant rejection faced by Nuh, 'Ad, Thamud, Ibrahim, Lut, and Shu'ayb from their proud civilizations.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Collapsed Ceilings of Fallen Cities",
              "Towns leveled into hollow ruins, their roofs falling inward upon foundations when systemic oppression exceeded bounds.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "The Abandoned Wells (Bi'rin Mu'attalah)",
              "Abundant freshwater sources left desolate and unused after thriving communities vanished under righteous retribution.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Lofty Fortified Palaces (Qasrin Masheed)",
              "Imposing architectural bastions and towering stone fortresses that failed completely to shield tyrants from divine decrees.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 12: SPIRITUAL SIGHT & CELESTIAL TIMELINES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ta'ma al-Qulub, Travelling with Wisdom, Mocking Demands & 1,000 Years", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Journeying with an Awake Heart",
              "Traversing historical landscapes with contemplative discernment to extract moral lessons from civilizational demises.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Blindness of Hearts in the Breasts",
              "Physical retinas perceiving daylight while the spiritual core inside the chest remains utterly blind to eternal truth.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Scoffing Demands for Chastisement",
              "Cynics demanding immediate retribution, misinterpreting divine patience and forbearance as impotence or absence.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "A Divine Day as a Thousand Years",
              "The vast celestial scale of divine patience, granting ample respite to stubborn rebels before justice inevitably falls.")

    # ==========================================
    # PLATE 07: THE PARABLE OF THE FLY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE PARABLE OF THE FLY & ABSOLUTE IMPOTENCE",
        "Pillars 13 & 14: Creating a Single Fly, The Stolen Crumb, Joint Weakness & Unmeasured Majesty",
        "PLATE 07 : PARABLE OF THE FLY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 13: THE PARABLE OF ABSOLUTE IMPOTENCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Mathal adh-Dhubab, Collective Impotence, The Stolen Crumb & Joint Weakness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Universal Parable (Mathal adh-Dhubab)",
              "A devastating challenge directed at all humanity to dismantle the psychological illusion of autonomous created power.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Inability to Create a Single Fly",
              "All false gods and scientific alliances failing utterly to manufacture or animate the organic complexity of a common fly.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Helplessness Against Stolen Crumb",
              "Idols incapable of retrieving even microscopic food particles dissolved and absorbed by an insect's predatory proboscis.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Weak is the Seeker and the Sought",
              "The mutual debility of the deluded mortal worshipper and the inert idol, or the frustrated pursuer and the tiny fly.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 14: THE UNMEASURED GRANDEUR OF ALLAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ma Qadaru Allaha, Al-Qawiyy Al-'Azeez, Chosen Messengers & Total Knowledge", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Failure to Appraise True Grandeur",
              "Humanity drastically underestimating the infinite power, majesty, and unyielding justice of the Lord of all existence.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Al-Qawiyy, Al-'Azeez (The All-Mighty)",
              "The Sovereign of irresistible potency who manages the vast cosmic apparatus without the slightest dependency on creation.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "Chosen Angelic & Mortal Messengers",
              "The divine prerogative of electing noble angels and upright prophets to convey celestial wisdom and moral law to humanity.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Exhaustive Knowledge of Past & Future",
              "Complete divine awareness encompassing all that lies before creation and all that lies behind, with all matters returning to Him.")

    # ==========================================
    # PLATE 08: THE ABRAHAMIC LEGACY & CALL
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE ABRAHAMIC LEGACY & THE NOBLE CALL",
        "Pillars 15 & 16: Four-Fold Liturgy, Religion Without Hardship, The Muslim Identity & The Best Guardian",
        "PLATE 08 : ABRAHAMIC LEGACY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 15: THE FOUR-FOLD LITURGY & RELIGIOUS EASE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Bowing, Prostrating, Doing Good, Haqqa Jihadih & Ma Ja'ala Min Haraj", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Four-Fold Liturgy of Salvation",
              "Bowing in humility, falling in prostration, worshipping the Lord alone, and actively doing good to achieve success.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Striving with Authentic Striving",
              "Dedicating intellect, wealth, and energy with unwavering sincerity for the pleasure of Allah as is truly His right.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Divine Selection (Ijtabakum)",
              "The supreme honor of being hand-picked by Allah to carry the torch of ethical monotheism across human history.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Religion Devoid of Hardship (Haraj)",
              "The profound legal charter establishing that divine commandments are designed for mercy, ease, balance, and human flourishing.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: ABRAHAMIC HERITAGE & SUPREME PATRON", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Millat Ibrahim, Huwa Sammakumu al-Muslimeen, I'tasimu & Ni'ma al-Mawla", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Perennial Creed of Ibrahim",
              "Grounding spiritual identity in the pure, uncompromising, and beautiful monotheistic tradition of patriarch Abraham.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Eternal Title: Muslimoon",
              "The sacred identity bestowed upon believers across generations—those who surrender their will unconditionally to Allah.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Holding Fast to the Sovereign (I'tasimu)",
              "Clinging tightly to the divine rope through regular prayer, generous zakah, and unyielding reliance upon the Creator.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Peerless Guardian and Helper",
              "Resting the soul in the comforting reality that Allah is the ultimate Protector—what an excellent Patron and Helper!")

    pdf.save(OUTPUT_PDF)
    print(f"Generated PDF: {OUTPUT_PDF} ({os.path.getsize(OUTPUT_PDF):,} bytes)")

    # Render PNG previews with pdftoppm
    print("Rendering PNG previews...")
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "hajj_page")]
    subprocess.run(cmd, check=True)

    # Rename and copy to brain_dir
    for i in range(1, 9):
        src_png = os.path.join(PREVIEWS_DIR, f"hajj_page-{i}.png")
        if os.path.exists(src_png):
            dest_hajj = os.path.join(BASE_DIR, f"hajj_hajj_page-{i}.png")
            shutil.copyfile(src_png, dest_hajj)
            dest_brain = os.path.join(brain_dir, f"hajj_hajj_page-{i}.png")
            shutil.copyfile(src_png, dest_brain)
            print(f"  Preview Plate {i} copied to {dest_brain} ({os.path.getsize(dest_brain):,} bytes)")

if __name__ == "__main__":
    build_hajj_pdf()
