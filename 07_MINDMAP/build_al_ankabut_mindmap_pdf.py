#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Ankabut Master Mindmap Vector PDF Generator
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
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_ANKABUT_MASTER_MINDMAP.pdf")
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

def build_al_ankabut_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-ANKABUT", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE LAW OF TRIBULATION & PARENTS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE LAW OF TRIBULATION & PARENTAL BOUNDARIES",
        "Pillars 1 & 2: Alif-Lam-Meem, The Testing Ground of Faith, Distinguishing Sincerity & Filial Balance",
        "PLATE 01 : THE CRUCIBLE OF FAITH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE THEOLOGY OF TESTING", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("A-Hasiba An-Nas, Purification of the Soul & Divine Knowledge", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Existential Question (A-Hasiba)",
              "Do people think they will be left to say 'We believe' without being tested? Faith is not an empty claim but a furnace of purification.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "The Melting of Pure Gold (Fitnah)",
              "Like smelting ore to burn away impurities, life trials expose the hidden contents of the soul and separate gold from slag.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Manifestation in Empirical Action",
              "Testing allows pre-eternal divine knowledge to manifest in recorded human choices, leaving humanity without excuse on Judgment Day.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Crucible of Ancient Believers",
              "Every believing community in history was forged in hardship; genuine conviction is proven only when worldly comfort is stripped away.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: PARENTAL DUTY & MONOTHEISM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Filial Excellence (Husna), Sa'd's Trial & Absolute Theological Spine", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Mandatory Filial Excellence (Husna)",
              "Believers are commanded to treat parents with supreme affection, financial support, and gentleness throughout life.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Absolute Limit (Fa-La Tuti'huma)",
              "No obedience to created beings in disobedience to the Creator; if parents coerce toward polytheism, obedience ceases unconditionally.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Sa'd's Unyielding Resoluteness",
              "Facing his mother's emotional hunger strike, Sa'd showed radiant filial honor while standing like granite for monotheism.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Sole Divine Destination",
              "To Allah is the final return; family allegiances will dissolve and all deeds will be unveiled with perfect impartiality.")

    # ==========================================
    # PLATE 02: HYPOCRISY & THE 950 YEARS OF NUH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "HYPOCRISY & THE 950-YEAR ENDURANCE OF NUH",
        "Pillars 3 & 4: The Fair-Weather Believer, The Myth of Sins & Nuh's Millennium of Patient Calling",
        "PLATE 02 : PROPHETIC ENDURANCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: THE FAIR-WEATHER SOUL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Persecution Equated to Hell, Opportunistic Greed & Double Burdens", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "Equating Human Harm to Hellfire",
              "The opportunist declares faith in ease, but when mocked or hurt by people, panics as though suffering the eternal wrath of Allah.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Opportunism in the Hour of Triumph",
              "When divine victory and prosperity arrive, the fair-weather soul rushes forward demanding spoils: 'We were always with you!'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The False Guarantee of Sins",
              "Disbelievers offer empty bargains: 'Follow our way and we carry your sins!' Yet no soul will bear the guilt of another.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "The Heavy Double Burden (Athqalahum)",
              "The misleaders will carry their personal sins alongside the compound weight of all those they deceived and corrupted.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 04: NUH'S 950-YEAR MISSION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Alfa Sanah, Redefining Success & Deliverance in the Ark", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "A Millennium Less Fifty Years",
              "Nuh called his community for 950 years through unbroken mockery, modeling absolute long-term perseverance in divine mission.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Fidelity Above Numerical Volume",
              "Islamic success is measured by uncorrupted truthfulness and effort, not by audience size or majority acceptance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Deliverance in the Ark (Al-Safinah)",
              "When the universal deluge engulfed the arrogant oligarchs, Allah delivered Nuh and the faithful remnants aboard the ark.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "An Enduring Cosmic Sign (Ayah)",
              "The ark was preserved as an eternal sign for humanity: tyrannies perish beneath the waves while faith floats to safety.")

    # ==========================================
    # PLATE 03: IBRAHIM'S FIRE & SACRED HIJRAH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "IBRAHIM'S FURNACE & THE SACRED HIJRAH",
        "Pillars 5 & 6: Denouncing Idols, Sustenance from Allah, The Cooling Furnace & Migration of Faith",
        "PLATE 03 : THE SACRED MIGRATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 05: ECONOMIC TAWHID & FIRE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Denouncing Fabrications, Seeking Rizq from Allah & The Furnace", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Idols as Fabricated Illusions (Ifkan)",
              "Ibrahim unmasks pagan worship: carved idols possess neither creative agency nor power to provide sustenance or hear prayers.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Economic Monotheism (Ibtaghoo ar-Rizq)",
              "Seek your livelihood exclusively from Allah; no corporation, dictator, or patron owns the keys to your provision.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Tyrants' Recourse to Fire",
              "Failing in rational debate, the oligarchs resort to state terrorism: 'Slay him or burn him in the blazing inferno!'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "The Miraculous Cooling (Fa-Anjahu)",
              "Allah commands the fire to become cool peace, demonstrating that physical elements obey their Creator, not human tormentors.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: THE EXILE & SACRED LEGACY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Inni Muhajirun Ila Rabbi, Generational Gifts & Loving Praise", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Migration to the Lord (Inni Muhajir)",
              "Ibrahim initiates the sacred archetype of exile: 'Indeed, I am migrating to my Lord; He is the Exalted in Might, the Wise.'")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Sacrificing Homeland for Faith",
              "Severing ancestral comfort to protect spiritual purity, teaching believers that true home is anywhere Allah is worshiped.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "The Generational Gift of Prophethood",
              "Allah rewards his sacrifice with Ishaq, Ya'qub, and the covenant of prophethood established within his direct lineage.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "The Enduring Tongue of Truth",
              "Granted honorable renown and sincere praise across all succeeding nations, culminating in the highest ranks of the Akhirah.")

    # ==========================================
    # PLATE 04: LUT, MADYAN & FALLEN EMPIRES
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "LUT, MADYAN & THE RETRIBUTION OF TYRANTS",
        "Pillars 7 & 8: Lut's Moral Courage, Shu'ayb's Economic Warning & The Four Distinct Cataclysms",
        "PLATE 04 : THE FALLEN TYRANTS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 07: LUT & THE MORAL FRONTIER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Public Perversion, Road Brigandage & The Angelic Envoys", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Confronting Systemic Indecency",
              "Lut condemned a society that normalized gross sexual perversion, public vulgarity, and highway robbery without shame.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Threat of Totalitarian Banishment",
              "The corrupt mob gave a single ultimatum: 'Expel them from your town!' Sinners cannot tolerate the presence of moral purity.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "The Dawn Angelic Deliverance",
              "Celestial messengers comfort Lut: 'Do not fear; we are here to rescue you and your daughters before morning dawns.'")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Fate of the Treacherous Wife",
              "His wife sympathized with the transgressors and was left behind, proving family ties cannot rescue a soul that chose corruption.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 08: THE FOURFOLD RETRIBUTION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Madyan's Tremor, Satanic Vanity & The Forensic Seizures", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Madyan's Commercial Corruption",
              "Shu'ayb called Madyan to honest weights and the Last Day; denying him, the seismic shock (Al-Rajfah) left them dead in their homes.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "The Delusion of Keen Perception",
              "'Ad and Thamud possessed sharp intellects and advanced masonry, but Satan embellished their sins, leading them to ruin.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Four Specific Cataclysms",
              "Stone showers for Lut, seismic blasts for Thamud, subterranean sinking for Qarun, and drowning for Pharaoh and his hosts.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Justice Without Iniquity (Wa Ma Zalama)",
              "Allah wronged none of them; they dismantled their own civilizations by rejecting prophetic guidance and exalting tyranny.")

    # ==========================================
    # PLATE 05: THE SPIDER'S FRAGILE HOUSE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE PARABLE OF THE SPIDER'S HOUSE",
        "Pillars 9 & 10: Bayt al-Ankabut, The Illusion of Secular Fortresses, Biological Predation & Grounded Wisdom",
        "PLATE 05 : THE SPIDER'S WEB"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 09: THE FLIMSIEST OF DWELLINGS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Awhana al-Buyoot, Structural Vulnerability & Cannibalistic Void", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Archetype of Secular Patrons",
              "Those who seek protection in wealth, political dynasties, or false gods are like the spider constructing an intricate silk web.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Total Physical Fragility",
              "The web appears geometric and clever, yet offers zero defense against driving rain, baking sun, gusting wind, or a passing finger.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Social & Biological Toxicity",
              "The spider's home is devoid of mercy: the female devours the male, and offspring cannibalize each other—a lethal house of betrayal.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Tragic Blindness of Arrogance",
              "'If only they knew!' Secular materialists boast of impenetrable institutions, unaware their foundations are flimsy cobwebs.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 10: COSMIC PARABLES & WISDOM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Insight of Scholars, Weeping of the Salaf & Flawless Creation", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Grasped Only by Men of Knowledge",
              "Allah strikes these deep metaphors for humanity, but none truly comprehend their layered reality except the people of 'Ilm.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "The Weeping of the Early Sages",
              "Whenever the righteous predecessors failed to grasp a Qur'anic parable, they wept, fearing exclusion from the scholars of truth.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Alliances Severed in Eternity",
              "Every mutual pact formed on falsehood will turn to mutual cursing and disavowal on the Day of Resurrection.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Heavens and Earth Created in Truth",
              "The cosmos was crafted with purposeful balance and justice, standing as a living proof of divine oneness for believers.")

    # ==========================================
    # PLATE 06: THE SPIRITUAL ARSENAL & SALAH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE SPIRITUAL ARSENAL: QUR'AN & SALAH",
        "Pillars 11 & 12: Utlu Ma Oohiya, The Restraining Power of Prayer, Supreme Dhikr & Gracious Inter-Faith Adab",
        "PLATE 06 : THE PILLAR OF PRAYER"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 11: PRAYER AS LIVING SHIELD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Tilawah, Establishing Salah & Restraining from Shame and Evil", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Daily Immersion in Revelation",
              "Recite what has been revealed of the Book: daily meditative connection with the Qur'an protects the mind from secular distortions.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Establishing the Living Prayer",
              "Salah is not empty physical motions but an anchored habit of consciousness, re-centering the human soul five times a day.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Restraining Immorality (Fahsha')",
              "A valid, heartfelt prayer actively deters the soul from private indecency, lustful transgressions, and moral corruption.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Combating Injustice (Munkar)",
              "Regular prayer builds an active social conscience that rejects systemic oppression, exploitation, and dishonesty.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: SUPREME DHIKR & CIVILITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Wa La-Dhikrullahi Akbar, Shared Monotheism & Sublime Debate", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Supremacy of Divine Dhikr",
              "The conscious remembrance of Allah is the greatest human act; Allah's remembrance of His servant surpasses all else.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Dialogue in the Best Manner",
              "Debate with the People of the Book with highest intellectual adab and calm gentleness, avoiding harsh polemics and abuse.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Monotheistic Declaration",
              "Proclaim: 'We believe in what was revealed to us and to you; our God and your God is One, and to Him we surrender.'")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Distinction with Injustice (Illa Alladhina)",
              "While gentleness is default, active tyranny, slander, and persecution must be confronted with resolute moral firmness.")

    # ==========================================
    # PLATE 07: PROOF OF REVELATION & BREASTS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "PROOFS OF PROPHETHOOD & SCRIPTURE IN HEARTS",
        "Pillars 13 & 14: The Unlettered Prophet, Preserved in Living Breasts, Vain Miracles & The Sufficiency of Revelation",
        "PLATE 07 : LIVING PRESERVATION"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 13: THE UNLETTERED WITNESS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Ummiyah as Divine Proof, Inscribing Nothing & Hearts of Scholars", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Unlettered Prophet (Ummi)",
              "The Prophet never read prior scriptures nor wrote with his hand, definitively silencing accusations of plagiarizing ancient texts.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Divine Authorship Perfected",
              "If Muhammad had been a literate scholar, doubters would have had room to speculate; his illiteracy highlights pure revelation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Preserved in Living Breasts (Sudoor)",
              "The Qur'an is clear signs preserved inside the hearts and memories of those gifted knowledge, defying parchment decay.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Oral Miraculous Continuum",
              "Preserved across millennia through unbroken oral memorization (Huffadh), fulfilling the divine guarantee of preservation.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 14: THE SUFFICIENT SCRIPTURE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Demands for Physical Portents, The Living Book & Divine Witness", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Superficial Demands for Signs",
              "Skeptics protest: 'Why are signs not sent from his Lord?' Physical spectacles fade, but the living intellect demands eternal truth.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "The Sufficiency of the Qur'an",
              "Is it not sufficient for them that We sent down the Book recited to them? The Book itself is the supreme ongoing miracle.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "Mercy & Remembrance for Believers",
              "Within the Qur'an is healing mercy and profound reminder for receptive hearts who desire truth over theatrical spectacles.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Allah as Infallible Witness (Kafa)",
              "Sufficient is Allah as witness between the Messenger and humanity; He knows all that exists within heavens and earth.")

    # ==========================================
    # PLATE 08: MORTALITY & THE GUIDED PATHWAYS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "UNIVERSAL MORTALITY & THE GUIDED PATHWAYS",
        "Pillars 15 & 16: Tasting Death, The Illusion of Dunya, Jahadoo Feena & The Guarantee of Divine Guidance",
        "PLATE 08 : THE GUIDED PATHWAYS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 15: MORTALITY & TRUE REALITY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Dha'iqatu al-Mawt, Dunya as Amusement & Al-Hayawan", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Universal Equalizer of Death",
              "Every soul will taste death, dissolving all bodily wealth, power, and prestige before returning to the Sovereign Creator.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "The World Unmasked as Amusement",
              "Worldly life is merely fleeting diversion and child's play; investing one's entire purpose in dunya is chasing a fading mirage.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The True Pulsating Life (Al-Hayawan)",
              "The Home of the Hereafter is authentic, immortal life untouched by sickness, fatigue, decay, or ending—if only they knew!")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Hypocrisy on the Stormy Seas",
              "When waves threaten their ship, they cry sincerely to Allah; yet once brought safely ashore, they promptly revert to shirk.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: STRIVING & GUIDANCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Walladhina Jahadoo Feena, Pathways of Light & Divine Accompaniment", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Striving of the Sincere Soul",
              "Those who wage jihad against internal desires, demonic doubts, and worldly injustice purely for Allah's sake (Jahadoo Feena).")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Guarantee: We Will Guide Them",
              "Allah makes a binding oath: We will surely guide them to Our diverse pathways of clarity, spiritual peace, and rectitude.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Guidance Proportionate to Striving",
              "Effort in Allah's path is never lost; taking a single step toward the divine opens boundless doors of wisdom and fortitude.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Divine Accompaniment (Ma'a al-Muhsineen)",
              "Indeed, Allah is personally with the doers of good: encompassing them with protection, victory, and everlasting grace.")

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate preview PNGs
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"[OK] Generated preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/page-{i}.png"
        dst = f"{brain_dir}/al_ankabut_mindmap_page_{i}.png"
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied preview to {dst}")

if __name__ == "__main__":
    build_al_ankabut_pdf()
