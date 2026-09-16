#!/usr/bin/env python3
"""
Huurs Studio - Surah Luqman Master Mindmap Vector PDF Generator
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
OUTPUT_PDF = os.path.join(BASE_DIR, "LUQMAN_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews_luqman")
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

def build_luqman_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH LUQMAN", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE BOOK OF WISDOM & THE DISTRACTION TRAP
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE BOOK OF WISDOM & THE DISTRACTION TRAP",
        "Pillars 1 & 2: Ayatu al-Kitabi al-Hakeem, Lahw al-Hadith & The Pillars of the Heavens",
        "PLATE 01 : THE WISE BOOK"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: MANUFACTURED DISTRACTIONS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ayatu al-Kitabi al-Hakeem, Lahw al-Hadith & Spiritual Deafness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Book of Transcendent Wisdom",
              "Alif-Lam-Meem. Signs of the Wise Book conferring guidance and mercy upon the Muhsineen who establish prayer and believe with certainty.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "The Commercialization of Lahw al-Hadith",
              "Nadr ibn al-Harith purchasing singing girls and Persian epics to divert seekers from the Qur'an; modern triviality monetizing attention.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Ridicule and Humiliating Torment",
              "Purchasing empty distraction to mislead from Allah's path without knowledge and mocking sacred truth; met with 'Adhab Muheen.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Haughty Turning of the Arrogant",
              "Turning away in aloof self-importance when divine verses are recited, as if possessing heaviness in the ears; spiritually deadened.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: COSMIC ARCHITECTURE & STABILITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Unseen Pillars, Rawasiya Anchors & The Flourishing of Pairs", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Heavens Without Visible Pillars",
              "Created celestial galaxies and orbital expanses without pillars that you see, suspended and sustained by sovereign divine power.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Mountain Pegs (Rawasiya) of Earth",
              "Casting deep subterranean mountain roots into the terrestrial crust lest the tectonic plates shift and convulse beneath humanity.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Biological Pairs Flourished by Rain",
              "Scattering every variety of moving creature across the earth and descending celestial water to sprout noble plant pairs in balance.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Challenge to False Deities",
              "This is the consummate creation of Allah; challenge the idolaters to show what those invoked besides Him have ever created.")

    # ==========================================
    # PLATE 02: ESSENCE OF WISDOM & MONOTHEISTIC REORIENTATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE ESSENCE OF WISDOM & MONOTHEISTIC REORIENTATION",
        "Pillars 3 & 4: Inna Ash-Shirka La-Zulmun 'Azeem, Gratitude to Allah & Consensual Sagehood",
        "PLATE 02 : NATURE OF WISDOM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 03: SAGEHOOD & GRATITUDE OF LUQMAN", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Core of Hikmah, Wali Status & Divine Self-Sufficiency", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Endowment of Divine Hikmah",
              "We granted Luqman wisdom: 'Be grateful to Allah.' Wisdom is not philosophical jargon but acknowledging divine grace through worship.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Gratitude Enriches the Human Soul",
              "Whoever shows gratitude benefits their own soul; thankful alignment brings internal tranquility and elevates human character.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "Consensus on Sagehood (Wali wa Hakim)",
              "Ahl al-Sunnah consensus confirms Luqman was an exceptionally wise saint and sage of Nubian heritage, renowned for silence and reflection.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "The Self-Sufficient & Praiseworthy",
              "And whoever disbelieves, Allah is Al-Ghaniyy (Free of need) and Al-Hameed (Intrinsically Praiseworthy); creation cannot diminish Him.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: THE SUPREME INJUSTICE (ZULM 'AZEEM)", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ya Bunayya Tenderness, Shirk as Injustice & Prophetic Clarification", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Pedagogical Tenderness: Ya Bunayya",
              "Addressing his son with an Arabic diminutive of intense love and compassion, creating a receptive emotional vessel for mentorship.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Foundational Prohibition",
              "Directing his very first instruction to the preservation of Tawheed: 'O my dear son, do not associate any partners with Allah.'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Polytheism as Tremendous Injustice",
              "Inna ash-shirka la-zulmun 'azeem. Zulm is placing a thing outside its rightful place; equating mortal dust to the Eternal Creator.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Prophetic Comfort to the Sahabah",
              "When the Companions feared self-wrongdoing, the Prophet ﷺ cited Luqman's verse, reassuring them that supreme Zulm signifies Shirk.")

    # ==========================================
    # PLATE 03: SACRED DEBT OF MOTHERHOOD & ETHICAL LIMITS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE SACRED DEBT OF MOTHERHOOD & ETHICAL LIMITS",
        "Pillars 5 & 6: Wahnan 'ala Wahn, The Conjoined Gratitude & Worldly Accompaniment",
        "PLATE 03 : FILIAL ETHICS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 05: THE SACRIFICE OF MOTHERHOOD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Wahnan 'ala Wahn, Two Years Weaning & The Paired Mandate", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "The Divine Enjoining of Filial Care",
              "We strictly commanded man devotion to his parents, grounding human societal ethics in intergenerational gratitude and compassion.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Weakness Compounding Weakness",
              "Hamalat-hu ummuhu wahnan 'ala wahn: the bodily toll of gestation, carrying increasing weight through sickness and labor pains.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Two Full Years of Weaning (Fisal)",
              "Fisaluhu fee 'amayn: around-the-clock nourishment and maternal selflessness depleting physical reserves to build infant vitality.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "The Conjoined Command of Gratitude",
              "An-ishkur lee wa li-walidayk. Gratitude to God is paired directly with gratitude to parents; neglecting mothers voids claimed piety.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 06: BOUNDARIES OF OBEDIENCE & COMPASSION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Limits of Submission, Dunya Accompaniment & Penitent Path", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Red Line of Monotheism",
              "If parents exert fierce pressure to compel polytheism or sin: 'Fa-la tuti'huma' (do not obey them); obedience belongs to Allah first.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Worldly Accompaniment with Honor",
              "Wa sahibhuma fid-dunya ma'roofa: accompany them with kindness, gentle speech, financial support, and warm filial presence.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Walking the Path of the Penitent",
              "Follow the spiritual path of those who turn back to Allah in sincere repentance (Inabah), seeking righteous scholarly companions.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "The Final Return and Accounting",
              "To Me is your ultimate destination, and I will inform you of the exact reality of everything you used to do in mortal life.")

    # ==========================================
    # PLATE 04: THE MUSTARD SEED & LIVING MURAQABAH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE MUSTARD SEED OF OMNISCIENCE & LIVING MURAQABAH",
        "Pillars 7 & 8: Habbah min Khardal, Triple Concealment & The Incorruptible Conscience",
        "PLATE 04 : INTERNAL CONSCIENCE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 07: THE MUSTARD SEED IN THE BOULDER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Microscopic Units, Triple Concealment & Effortless Summons", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Microscopic Mustard Seed",
              "Mithqala habbatin min khardal: using an ancient unit of microscopic weight—weightless, minuscule, and easily blown by wind.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Concealment in a Solid Boulder",
              "Fa-takun fee sakhratin: imagine this speck encased inside an opaque, impenetrable boulder, shielded from all external observation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Adrift in Space or Earth Depths",
              "Aw fis-samawati aw fil-ard: drifting in the boundless cosmic void or buried in deep tectonic subterranean strata.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Effortless Summons: Ya'ti biha Allah",
              "No satellite or sensor could detect it, yet Allah's omniscience encompasses it and brings it forth to the scales of judgment.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 08: SUBTLE PENETRATION & MURAQABAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Lateefun Khabeer, Conscience Awakening & The Hidden Deed", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Al-Lateef: Penetrating Subtle Depths",
              "He whose perception penetrates the most microscopic, invisible layers of reality without resistance or obstruction.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Al-Khabeer: Knower of Internal Intent",
              "Intimately acquainted with secret motivations, fleeting glances, internal compromises, and unspoken thoughts of the heart.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Awakening Internal Muraqabah",
              "Training an incorruptible moral compass that remains upright in solitude, when external human surveillance is absent.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Preserving Microscopic Virtues",
              "Reassuring the believer that a hidden tear in the night, a quiet charity, or a restrained impulse of anger is never forgotten.")

    # ==========================================
    # PLATE 05: QUADRUPLE PILLAR OF SOCIAL REFORM & SABR
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE QUADRUPLE PILLAR OF SOCIAL REFORM & SABR",
        "Pillars 9 & 10: Aqimi as-Salah, Amr bil-Ma'roof, Nahy 'an al-Munkar & 'Azm al-Umoor",
        "PLATE 05 : CIVIC REFORM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 09: VERTICAL ANCHOR & CIVIC ACTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Prayer Alignment, Encouraging Good & Confronting Wrong", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Vertical Anchor: Aqimi as-Salah",
              "Establish prayer: anchor personal devotion before public engagement; spiritual discipline is the fuel of societal reform.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Promoting Societal Virtue (Al-Ma'roof)",
              "Wa'mur bil-ma'roof: active civic participation encouraging honesty, compassion, economic justice, and communal welfare.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Confronting Corruption (Al-Munkar)",
              "Wanha 'ani al-munkar: moral courage to oppose tyranny, exploitation, indecency, and ethical decay in the public sphere.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "The Inevitability of Backlash",
              "Moving from passive ritual piety to active reform inevitably triggers resistance, slander, and hostility from entrenched interests.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 10: THE FURNACE OF PATIENT RESILIENCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Wasbir 'ala ma Asabak, 'Azm al-Umoor & Spiritual Spine", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Patient Fortitude (Wasbir)",
              "Wasbir 'ala ma asabak: bear with dignified resilience whatever trials and personal attacks befall you on the path of truth.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Matters of Firm Resolve ('Azm al-Umoor)",
              "Inna dhalika min 'azmi al-umoor: this demanding triad requires true spiritual spine, moral stamina, and unwavering determination.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Transition to Communal Leadership",
              "Transforming a private worshiper into an unshakeable leader who uplifts society without being swayed by popular applause.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Armor Against Cynicism and Burnout",
              "Sabr protects the heart from burning out in bitterness or resorting to unethical shortcuts when facing stubborn resistance.")

    # ==========================================
    # PLATE 06: SOMATIC ARCHITECTURE OF CHARACTER
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE SOMATIC ARCHITECTURE OF CHARACTER",
        "Pillars 11 & 12: La Tusa''ir Khaddak, Moderation of Pace & Vocal Decorum",
        "PLATE 06 : SOMATIC DECORUM"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 11: ERADICATING SNOBBERY & THE PROUD GAIT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Metaphor of Sa'ar, Full Attention & The Pompous Strut", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Warning of Sa'ar (Cheek Contempt)",
              "La tusa''ir khaddaka lin-nas: Sa'ar was a disease twisting a camel's neck; do not twist your face away with haughty elitism.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Full Eye Contact and Humble Warmth",
              "Greet all people—especially the impoverished and vulnerable—with full eye contact, generous presence, and sincere humility.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "The Pompous Strut (La Tamshi Maraha)",
              "Do not walk the earth with ostentatious strutting, seeking to impress spectators with clothing, wealth, or physical posturing.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Disdain for the Boastful Delusion",
              "Allah loves not the Mukhtal (intoxicated with self-delusion) or the Fakhoor (loud, boastful braggart celebrating mortal vanity).")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: INTENTIONAL PACING & VOCAL DECORUM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Iqsid fee Mashyik, Waghdud min Sawtik & The Donkey Metaphor", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "Purposeful Poise (Iqsid fee Mashyik)",
              "Walk with moderation and purposeful dignity: neither dragging feet in lazy slouching nor rushing with aggressive arrogance.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Vocal Modulation (Waghdud min Sawtik)",
              "Lower your voice: shouting and aggressive volume do not signal conviction; true authority speaks with calm, articulate clarity.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Braying Donkey Metaphor",
              "The most disagreeable sound is the braying of donkeys: shrill, jarring, and devoid of intellect; uncontrolled shouting mirrors this.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Somatic Discipline of the Nafs",
              "External body language and speech volume are physical instruments that tame internal ego and cultivate holistic reverence.")

    # ==========================================
    # PLATE 07: SEVEN OCEANS OF INK & COSMIC MAJESTY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE SEVEN OCEANS OF INK & EFFORTLESS RESURRECTION",
        "Pillars 13 & 14: Kalimatu Allah, Infinite Knowledge & Ka-nafsin Wahidah",
        "PLATE 07 : COSMIC MAJESTY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 13: THE LIMITLESS WORDS OF ALLAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Forests Turned to Pens, Eight Oceans of Ink & Divine Majesty", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "All Earthly Trees as Pens",
              "If every tree across all continents were felled and sharpened into pens, and the global ocean turned into liquid writing ink...")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Replenished by Seven Oceans",
              "Wal-bahru yamudduhu min ba'dihi sab'atu abhur: replenished by seven more oceans of ink to write the knowledge and decrees of Allah...")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Exhaustion of Creation vs Infinite Words",
              "All pens would snap and all eight oceans would evaporate completely, yet the words and wisdom of Allah would remain unexhausted.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "The Microscopic Droplet of Human Science",
              "All human universities, supercomputers, and scientific libraries across all ages represent less than a drop from a boundless ocean.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: EFFORTLESS CREATION & COSMIC RHYTHMS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ka-nafsin Wahidah, Merging Day and Night & Maritime Ships", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Resurrection as a Single Soul",
              "Ma khalqukum wa la ba'thukum illa ka-nafsin wahidah: creating and resurrecting billions requires no more effort than a single soul.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Merging Night into Day",
              "Yooliju al-layla fin-nahar: smoothly alternating dark night and radiant daylight through precise planetary rotation.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "Subjugation of Sun and Moon",
              "Each celestial orb gliding in its mathematically governed trajectory for an appointed cosmic term known to the Creator.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Ships Cleaving Oceanic Depths",
              "Vessels gliding through massive waves by Allah's favor, carrying sustenance and commerce as signs for every patient, grateful soul.")

    # ==========================================
    # PLATE 08: DISSOLUTION OF KINSHIP & FIVE KEYS OF UNSEEN
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE DISSOLUTION OF KINSHIP & THE FIVE KEYS OF THE UNSEEN",
        "Pillars 15 & 16: Radical Accountability, Mafatih al-Ghayb & The Eternal Sovereign",
        "PLATE 08 : THE FINAL HORIZON"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 15: RADICAL INDIVIDUAL ACCOUNTABILITY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Dissolution of Blood Pacts, Dunya Illusion & Inviolable Truth", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Universal Summons to God-Consciousness",
              "Ya ayyuha an-nasu-ttaqoo rabbakum: a solemn universal call commanding reverence and preparation for the Day of Standing.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Dissolution of Biological Pacts",
              "A Day when no father will avail his son in the least, nor will any child avail his father; biological loyalties dissolve before justice.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Deception of Dunya and the Deceiver",
              "Let not the fleeting glitter of mortal life delude you, and let not the arch-deceiver (Shaytan) lure you into false security.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "The Inviolable Divine Promise",
              "Inna wa'da Allahi haqqun: Allah's promise of resurrection, recompense, and eternal reality is absolute, undeniable truth.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: THE FIVE KEYS OF THE UNSEEN", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Mafatih al-Ghayb, Tomorrow's Earnings & Final Plot of Soil", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Timing of the Final Hour ('Ilm as-Sa'ah)",
              "Allah alone holds the exact timing of cosmic dissolution and the Day of Judgment; hidden from angels and prophets alike.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Descent of Rain & Womb Realities",
              "Directing the droplet-by-droplet descent of rain, and knowing the ultimate spiritual destiny, lifespan, and rizq of the unborn.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Tomorrow's Earnings & The Final Coordinate",
              "No soul knows what deeds or wealth it will earn tomorrow, and no soul knows in what land its death and grave are decreed.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Omniscient and Acquainted Sovereign",
              "Inna Allaha 'Aleemun Khabeer: Allah is All-Knowing in cosmic totality and Intimately Acquainted with every single heartbeat.")

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate preview PNGs
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"[OK] Generated preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/page-{i}.png"
        dst = f"{brain_dir}/luqman_mindmap_page_{i}.png"
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied preview to {dst}")

if __name__ == "__main__":
    build_luqman_pdf()
