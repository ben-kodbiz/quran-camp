#!/usr/bin/env python3
"""
Huurs Studio - Surah Yusuf Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "YUSUF_MASTER_MINDMAP.pdf")
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

def build_yusuf_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH YUSUF", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-header Title Area
        pdf.text(title, 32, h - 66, font="F2", size=12.5, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)

        # Right Section Badge
        badge_str = f"[{section_badge}]"
        badge_w = len(badge_str) * 6.1
        pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=10.5, rgb=GOLD)

        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Footer Bar
        pdf.line(32, 36, w - 32, 36, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS STUDIO  *  READ. REFLECT. RETURN.  *  SUNNI SOURCE DISCIPLINE (TABARI, IBN KATHIR, QURTUBI, RAZI, BAGHAWI)", 32, 22, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("PROPRIETARY CARTOGRAPHY  *  STRICTLY VERIFIED TIER-1", w - 275, 22, font="F2", size=7.2, rgb=GOLD)

    c1_x = 32
    c2_x = 412
    c1_w = 348
    c2_w = 348
    c1_y = 48
    c1_h = 332

    # =========================================================================
    # PAGE 1: THE CELESTIAL DREAM & PATERNAL WISDOM
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE CELESTIAL DREAM & PATERNAL WISDOM",
        "Pillars 1 & 2: Ahsan al-Qasas, Arabic Scripture, The Vision of Eleven Stars & Paternal Discretion",
        "PLATE 01 : VISION & DISCRETION"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: AHSAN AL-QASAS & THE ARABIC QURAN", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Supreme Literary Mastery, Prophetic Consolation & The Chosen Lineage", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Alif-Lam-Ra: The Manifest Arabic Scripture", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Disjointed letters asserting divine provenance and linguistic supremacy.\n"
        "- Revealed as an Arabic Qur'an so that human intellect may comprehend and reason.\n"
        "- Engaging the cognitive faculties through rigorous historical narrative and theology."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. Ahsan al-Qasas: The Best of All Narratives", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Crowned 'the best of stories' combining comprehensive psychological and moral depth.\n"
        "- Unveiling intricate historical realities previously unknown to mortal minds.\n"
        "- Engineered as divine medicine for grief during the Prophet's Year of Sorrow."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. Prophetic Heritage: Ibrahim, Ishaq & Ya'qub", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Locating young Yusuf within the golden genealogical chain of Abrahamic prophets.\n"
        "- Continuation of the divine covenant and spiritual blessing bestowed on ancestors.\n"
        "- Prophethood as a sacred trust of service, sacrifice, and uncompromising Tawhid."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. Consolation for Grieving Hearts in the Crucible", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Demonstrating that even God's most beloved elect endure severe betrayal and loss.\n"
        "- Reassuring the Prophet ﷺ that fraternal hostility in Makkah will culminate in dawn.\n"
        "- Transforming personal sorrow into an enduring universal classroom for resilience."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE VISION OF ELEVEN STARS & PATERNAL DISCRETION", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Eleven Stars, Sun and Moon & Guarding Blessings from Envy", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. The Celestial Vision: Eleven Stars, Sun and Moon", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Young Yusuf confides in his father: Eleven stars, sun, and moon prostrating to him.\n"
        "- Prostration symbolizing profound honor and future spiritual/temporal elevation.\n"
        "- Planting an innocent childhood vision realized decades later in imperial Egypt."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. Paternal Discernment: The Danger of Envy", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ya'qub immediately grasps the momentous weight: 'Do not relate your vision to brothers.'\n"
        "- Recognizing that sibling jealousy can corrupt even sincere hearts when ungrounded.\n"
        "- Unmasking the metaphysical instigator: 'Indeed, Shaytan to man is a manifest enemy.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. The Wisdom of Discretion: Concealing Emerging Gifts", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The psychological law of Kitman: Concealing blessings until firmly established.\n"
        "- Prophetic maxim: 'Seek assistance in fulfilling needs through quiet discretion.'\n"
        "- Maturity in communication: Not every vision or gift is fit for public exposure."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. Divine Election: Interpreting Narratives (Ta'weel)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Paternal prophecy: 'Your Lord will choose you and teach you the interpretation of events.'\n"
        "- Ta'weel al-Ahadith: Discerning the ultimate inner reality of dreams and world events.\n"
        "- Prophetic insight penetrating beneath surfaces into the sovereign tapestry of decree."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: FRATERNAL ENVY, THE WELL & FALSE BLOOD
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "FRATERNAL ENVY, THE WELL & FALSE BLOOD",
        "Pillars 3 & 4: Conspiracy of the Brothers, The Well of Ghayabah, False Blood & Sabrun Jameel",
        "PLATE 02 : THE WELL & SABR"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE CONSPIRACY OF THE BROTHERS & MONOPOLIZING LOVE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Pathology of Jealousy, Rationalizing Sin & The Pitiful Compromise", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. The Pathology of Toxic Fraternal Jealousy", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Resentment of the brothers: 'Yusuf and his brother are more beloved than we.'\n"
        "- Relying on physical utility and collective strength ('Usbah) to demand affection.\n"
        "- The ego rationalizing malice when spiritual beauty threatens insecure vanity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. The Rationalized Sin: Kill Yusuf and Repent Later", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Chilling proposal: 'Kill Yusuf or exile him so father's face may be yours alone.'\n"
        "- The classic trap of pre-planned repentance: 'And after that be righteous people!'\n"
        "- The absurdity of attempting to purchase parental love through fratricidal crime."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. The Compromise: Casting Him into the Deep Well", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Moderating violence: 'Do not kill Yusuf, but throw him into the bottom of the well.'\n"
        "- Hoping passing caravans will enslave him far away; reducing murder to kidnapping.\n"
        "- Divine decree utilizing their compromise to preserve Yusuf's life for Egypt."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. The Deceptive Plea: Feigning Care for the Youth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Manipulating Ya'qub: 'Why do you not trust us with Yusuf? We are sincere advisers.'\n"
        "- Pleading to take him to play; Ya'qub voices fear: 'I fear a wolf may devour him.'\n"
        "- The brothers seizing their father's voiced anxiety to construct their manufactured alibi."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE WELL OF GHAYABAH, FALSE BLOOD & SABRUN JAMEEL", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Divine Reassurance in the Dark, Theatrical Tears & Undamaged Garment", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. Abandonment in the Well & Divine Reassurance", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Stripping Yusuf's garment and casting the youth into the dark, watery well abyss.\n"
        "- Divine revelation descends in the dark: 'You will inform them of this while they know not.'\n"
        "- Imparting absolute certainty: The well is not your grave, but your conduit to power."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. Theatrical Grief: Weeping at Nightfall", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Returning at nightfall with manufactured tears: 'Wa ja'oo abahum 'ishaa'an yabkoon.'\n"
        "- Weeping is not proof of innocence; emotional theatrics often mask deep guilt.\n"
        "- Fabricated claim: 'A wolf consumed him while we were racing; you will not believe us.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. False Blood on the Undamaged Shirt (Bi-Damin Kadhib)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Presenting the shirt stained with animal blood as fraudulent forensic proof.\n"
        "- Ya'qub notices the intact garment: 'How merciful was the wolf who forgot to tear the shirt!'\n"
        "- Crime inevitably leaves flaws; physical deception fails before spiritual discernment."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. The Master Station: Sabrun Jameel & Al-Musta'an", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Immortal manifesto: 'Nay, your souls enticed you to an evil deed; so Sabrun Jameel.'\n"
        "- Beautiful Patience: Enduring pain without despair, bitterness, or complaining to creation.\n"
        "- Anchoring the soul in Allah: 'And Allah is the One whose help is sought (Al-Musta'an).'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE CRUCIBLE OF SEDUCTION & THE BURHAN OF THE LORD
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE CRUCIBLE OF SEDUCTION & THE BURHAN OF THE LORD",
        "Pillars 5 & 6: Egyptian Sanctuary, Shatr al-Husn, Bolted Doors, Ma'adhallah & The Torn Shirt",
        "PLATE 03 : CHASTITY & BURHAN"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: THE EGYPTIAN HOUSEHOLD & REACHING MATURITY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sold for Counted Dirhams, Divine Subtlety (Lutf) & Half of All Beauty", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Extracted from the Well: Sold for Counted Dirhams", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Caravan draws the bucket: 'O good news, here is a boy!' Sold as a slave for dirhams.\n"
        "- Ignorance despising what is precious; treating a prophet as cheap merchandise.\n"
        "- Enduring human trafficking; transitioning from free son to enslaved property."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. The Egyptian Sanctuary: Household of Al-'Azeez", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Purchased by Egyptian minister instructing wife: 'Honor his stay (Akrimee mathwah).'\n"
        "- Divine Lutf positioning a slave boy in the administrative palace of the empire.\n"
        "- 'And Allah is predominant over His affair (Ghalibun 'ala amrih), but most know not.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. Physical Radiance & Maturity: Hukm and 'Ilm", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Reaching full maturity (Balagha ashuddah): Bestowed with wisdom and sacred knowledge.\n"
        "- Granted half of all human beauty (Shatr al-husn), pairing outer light with inner purity.\n"
        "- 'And thus do We reward the doers of excellence (Al-Muhsineen).'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. The Looming Crisis of Domestic Palace Temptation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Secluded palace luxury exposing Yusuf to unprecedented domestic moral pressure.\n"
        "- The minister's wife captivated by his radiance, systematically plotting seduction.\n"
        "- The vulnerability of an alien slave boy facing the demands of an elite mistress."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: LOCKED DOORS, MA'ADHALLAH & THE TORN SHIRT", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Hayta Lak, Seeking Refuge in Allah, The Divine Proof & Forensic Tear", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. The Closed Doors & The Bold Seduction: Hayta Lak", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Bolting palace doors, demanding: 'Hayta lak!' (Come, I am ready for you!).\n"
        "- Total privacy, power imbalance, prime physical youth, zero fear of earthly eyes.\n"
        "- The ultimate crucible: Solitary temptation where every secular condition favored sin."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. The Prophetic Fortress: Ma'adhallah & Ethical Duty", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Instant monotheistic reflex: 'Ma'adhallah!' (I seek refuge in Allah!).\n"
        "- Ethical loyalty: 'Indeed, my master made good my dwelling; wrongdoers never prosper.'\n"
        "- Conscience remembering obligations of gratitude and divine accountability."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. Spiritual Climax: Seeing the Burhan of the Lord", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Realism: He felt mortal inclination, but saw the Burhan (Clear Proof) of his Lord.\n"
        "- The luminous awe of God turning away evil; preserving his status among Al-Mukhliseen.\n"
        "- Prophetic infallibility: Instinct disciplined by transcendent divine vision."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. Race to the Door & Forensic Evidence: Qudda min Dubur", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fleeing to the door; she grabs his shirt, tearing it from behind (Qudda min dubur).\n"
        "- Confronting the minister; she accuses Yusuf: 'Imprison him or painful punishment!'\n"
        "- Wise witness deduces: Tear in the back proves flight and unmasks her deceit."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE BANQUET OF KNIVES & CHOOSING PRISON OVER SIN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE BANQUET OF KNIVES & CHOOSING PRISON OVER SIN",
        "Pillars 7 & 8: City Gossip, Sliced Hands in Trance, The Heroic Prayer & Prison as Sanctuary",
        "PLATE 04 : THE BANQUET & PRISON"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE GOSSIP OF THE CITY & THE SLICED HANDS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Scandal of High Society, The Reclining Couches & In Hadha Illa Malak", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. The Scandal & Gossip of the Capital's Elite", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- City women gossiping: 'The Azeez's wife seeks to seduce her slave; love pierced her!'\n"
        "- High society hypocrisy: Mocking her lack of aristocratic decorum and composure.\n"
        "- She constructs an elaborate psychological trap to silence their arrogant rumors."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. Luxurious Banquet, Reclining Couches & Fruit Knives", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Seating the noblewomen upon elegant couches, handing each ripe fruit and sharp knife.\n"
        "- Commanding Yusuf: 'Come forth before them!' A calculated theatrical reveal.\n"
        "- Orchestrating a physical demonstration of Yusuf's paralyzing, majestic beauty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. Stunned Agony: Slicing Hands in Bewildered Awe", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Looking upon Yusuf, struck with aesthetic shock; slicing fingers without feeling pain.\n"
        "- Involuntary awe: 'Hasha lillah! This is no human! This is none but a noble angel!'\n"
        "- Physical pain eclipsed by overwhelming cognitive and aesthetic reverence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. The Shameless Ultimatum: Submission or Prison", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Emboldened mistress boasts: 'That is he about whom you blamed me; he saved himself.'\n"
        "- Public ultimatum: 'If he obeys not my command, he will be imprisoned in humiliation!'\n"
        "- The elite assembly joining her predatory pressure against a solitary righteous soul."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: THE PRAYER FOR PRISON & SPIRITUAL SANCTUARY", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("As-Sijnu Ahabbu Ilayya, Begging for Divine Shield & Dungeon Integrity", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. The Heroic Supplication: Prison Over Moral Sin", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Historic prayer: 'My Lord, prison is more beloved to me than what they call me to.'\n"
        "- Ultimate spiritual hierarchy: Physical dungeon is superior to moral captivity.\n"
        "- The believer choosing material deprivation over contamination of faith."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. Absolute Vulnerability: Acknowledging Human Frailty", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Humility: 'Unless You turn their plot from me, I will incline and be of the ignorant.'\n"
        "- Refusing to boast in personal willpower; moral chastity is a gift of divine protection.\n"
        "- 'So his Lord answered him and turned away their plot; He is Hearing, Knowing.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. The Injustice of Power: Incarceration to Save Face", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Acknowledging his innocence, the regime imprisons him to bury the domestic scandal.\n"
        "- The pathology of oligarchies: Sacrificing the innocent to preserve elite prestige.\n"
        "- Yusuf entering the dungeon with a pure heart while the palace festers in guilt."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. The Dungeon as a Sacred Sanctuary of Maturation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- An apparent defeat serving as a protected divine retreat for spiritual elevation.\n"
        "- Isolated from court distraction, forging character for future national leadership.\n"
        "- Divine decree transforming prison walls into the launching pad of salvation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: PRISON DA'WAH & THE KING'S VISIONARY DREAM
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "PRISON DA'WAH & THE KING'S VISIONARY DREAM",
        "Pillars 9 & 10: Preaching Tawhid to Inmates, Cupbearer's Amnesia, Seven Cows & 14-Year Strategy",
        "PLATE 05 : DA'WAH & THE DREAM"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: MONOTHEISM IN INCARCERATION & THE CELLMATES' DREAMS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Reputation of Excellence (Muhsineen), A-Arbabun Mutafarriqoon & Amnesia", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. Two Royal Youths & The Reputation of Excellence", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Royal cupbearer and baker enter prison; observing Yusuf's radiant character.\n"
        "- Testimony of cellmates: 'Indeed, we see you as one of the Muhsineen.'\n"
        "- Moral excellence shines through prison uniforms; integrity cannot be obscured."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. The Dreams of Wine and Bread Decoded", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cupbearer dreamt of pressing wine; baker dreamt of birds scavenging bread from head.\n"
        "- Yusuf promises interpretation before their food arrives, grounding insight in God.\n"
        "- Emphasizing his wisdom is a divine gift because he rejected polytheism."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. The Prison Khutbah: The Supreme Primacy of Tawhid", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Teaching moment: 'Are separate diverse lords better, or Allah, the One, the Subduer?'\n"
        "- Demonstrating the intellectual chaos of polytheism vs. cosmic harmony of Tawhid.\n"
        "- Prophetic duty never pauses; da'wah illuminates dungeons just as it guides palaces."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. Sober Interpretation & The Cupbearer's Amnesia", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Interpretation fulfilled: Cupbearer restored to court; baker crucified.\n"
        "- Yusuf appeals: 'Mention me to your master.' But Shaytan caused him to forget.\n"
        "- Yusuf remains forgotten for several years, awaiting the exact divine appointment."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: THE SEVEN FAT COWS & THE FOURTEEN-YEAR PLAN", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Royal Nightmares, Storing in the Ear (Fee Sunbulihi) & Agrarian Genius", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. The King's Perplexing Dream: Seven Fat & Lean Cows", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- King awakens in terror: Seven fat cows eaten by seven lean; seven green and dry ears.\n"
        "- Court sorcerers confess impotence: 'These are muddled nightmares (Adghathu ahlam).'\n"
        "- Human worldly wisdom collapsing before a divinely dispatched prophetic dream."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. Awakening of Memory: The Cupbearer Remembers Yusuf", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Years of amnesia shattered: Cupbearer recalls the righteous prisoner in the dungeon.\n"
        "- Rushing to prison: 'Yusuf, O truthful one (Ayyuhas-Siddeeq)! Explain to us...'\n"
        "- Divine timing: Remembered at the precise hour when the entire kingdom faced ruin."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. Visionary 14-Year Agrarian Plan: Fee Sunbulihi", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 7 years of planting: 'Leave what you harvest in its ear (Fee sunbulihi) except a little.'\n"
        "- Agrarian foresight: Keeping grain in the husk prevents rot, weevils, and moisture loss.\n"
        "- Followed by 7 years of devastating famine, then a year of abundant rain and pressing."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. The Economic Architect of Middle Eastern Survival", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Formulating a macroeconomic strategy: Strategic reserves, rationing, price controls.\n"
        "- Sacred 'Ilm incorporating technical administrative and economic competence.\n"
        "- The king astonished: An imprisoned foreign slave holds the survival of the empire."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: EXONERATION, HIGH OFFICE & THE BROTHERS' ARRIVAL
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "EXONERATION, HIGH OFFICE & THE BROTHERS' ARRIVAL",
        "Pillars 11 & 12: Demanding Clean Name, Al-Haqq Unveiled, Hafeezun 'Aleem & The Brothers at the Gate",
        "PLATE 06 : EXONERATION & POWER"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: DEMANDING EXONERATION & AL-HAQQ UNVEILED", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Refusing Royal Pardon, Hashasa al-Haqq & Nafs Ammarah bis-Soo'", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. Royal Pardon Rejected: Demanding Official Clearance", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- King orders release: 'Bring him to me!' Yusuf refuses to leave as a pardoned convict.\n"
        "- Demanding judicial review: 'Ask the king: What was the condition of the women?'\n"
        "- Guarding moral integrity: Refusing to assume office under lingering suspicion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. Re-Opened Judicial Inquiry & Public Confession", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- King interrogates women: 'What was your affair when you sought to seduce Yusuf?'\n"
        "- Noblewomen swear: 'God forbid! We know no evil of him!' The mistress confesses:\n"
        "- 'Al-ana hashasa al-haqq! I sought to seduce him, and indeed he is of the truthful!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. Complete Moral Vindication & Sincerity of Yusuf", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Yusuf's honor inscribed in official imperial records; truth buried for years resurfaces.\n"
        "- Yusuf clarifies: 'So my master knows I betrayed him not in secret; Allah guides no plot.'\n"
        "- Righteous patience compelling even former accusers to testify to his purity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. The Soul Inclined to Evil: Nafs Ammarah bis-Soo'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Spiritual humility: 'I do not acquit myself; the soul persistently commands evil.'\n"
        "- Nafs Ammarah conquered only through divine mercy; rejecting self-righteous pride.\n"
        "- Prophetic nobility: At the moment of total vindication, the ego is crushed before God."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: CUSTODIAN OF THE STOREHOUSES & THE FAMINE RELIEF", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Makeenun Ameen, Innee Hafeezun 'Aleem & The Unrecognized Sovereign", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. Royal Elevation: Established and Trusted (Makeen Ameen)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- King meets Yusuf: 'You are today established, trusted, and empowered (Makeen Ameen).'\n"
        "- Transition of state: From pit, to slave block, to prison, to prime minister of Egypt.\n"
        "- 'And thus We established Yusuf in the land to settle wherever he willed.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. Assuming High Office: Innee Hafeezun 'Aleem", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Seeking office for service: 'Appoint me over storehouses; I am Hafeezun 'Aleem.'\n"
        "- Permissibility of seeking office when uniquely qualified to avert national catastrophe.\n"
        "- The twin qualifications: Incorruptible moral integrity paired with technical expertise."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. The Great Regional Famine & Equitable Grain Relief", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Famine strikes the Near East; nations migrate to Egypt where Yusuf manages relief.\n"
        "- Distributing grain with flawless equity; preventing hoarding and black-market greed.\n"
        "- Prophetic power deployed exclusively for universal human preservation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. The Arrival of the Ten Brothers: Recognized Unaware", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Starving in Canaan, Ya'qub sends ten sons to Egypt to purchase emergency grain.\n"
        "- Dramatic encounter: 'Yusuf recognized them, but they recognized him not!'\n"
        "- Seeing an Egyptian ruler in robes; never dreaming their sold brother sat on the throne."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE STRATAGEM OF BENJAMIN & THE AGONY OF YA'QUB
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE STRATAGEM OF BENJAMIN & THE AGONY OF YA'QUB",
        "Pillars 13 & 14: Separate Gates, The Goblet in the Saddlebag, Sibling Guilt & Weeping to Blindness",
        "PLATE 07 : BENJAMIN & YA'QUB"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: SEPARATE GATES, THE GOLDEN CUP & SIBLING GUILT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Oath of Ya'qub, Ana Akhook, Royal Goblet in Bag & Accusations", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Condition of Return: Bringing the Younger Brother", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Demanding Benjamin as proof of honesty; returning their currency secretly in bags.\n"
        "- Brothers appeal to Ya'qub; father's grief: 'Can I trust you as I trusted with Yusuf?'\n"
        "- Economic necessity forcing brothers to negotiate under divine orchestration."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. Sacred Oath & Paternal Counsel: Separate Gates", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Demanding a covenant in Allah's Name before releasing Benjamin.\n"
        "- Counsel: 'Enter not from one gate, but from separate gates (Min abwabin mutafarriqah).'\n"
        "- Protecting against evil eye and suspicion; judgment belongs only to Allah."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Secret Palace Reunion: Innee Ana Akhook", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Yusuf brings Benjamin privately into chambers: 'Indeed, I am your brother!'\n"
        "- Comforting him: 'Grieve not over what they did!' Decades of separation dissolve.\n"
        "- Formulating a strategic divine plan to retain his full brother in Egypt."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. The Royal Goblet Placed in Benjamin's Saddlebag", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Placing the king's golden drinking cup (Siqayah) in Benjamin's luggage.\n"
        "- Guard halts caravan: 'You are thieves!' Penalty under Canaanite law: Enslavement.\n"
        "- Searching elder bags first; extracted from Benjamin's sack! Sibling guilt exposed."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: EYES WHITE WITH GRIEF & COMPLAINING ONLY TO GOD", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Lingering Slander, Eldest Brother's Refusal, Baththee wa Huznee & Zero Despair", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. Lingering Slander: Accusing the Lost Brother", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Deflecting shame: 'If he steals, a brother of his [Yusuf] stole before!'\n"
        "- Decades later, unresolved jealousy persists; projecting crime onto the absent.\n"
        "- Yusuf conceals his identity: 'You are in a worse position; Allah knows what you describe.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. Eldest Brother's Refusal to Face Grieving Father", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Facing loss of Benjamin and broken oath, the eldest brother refuses to return to Canaan.\n"
        "- 'I will not leave Egypt until father permits or Allah decides; He is the best judge.'\n"
        "- Remembering the crime of the well; sibling guilt reaching catastrophic collapse."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. The Agony of Ya'qub: Eyes Turned Milky White with Grief", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sons return reporting Benjamin's loss; Ya'qub cries: 'Ya asafa 'ala Yusuf!'\n"
        "- His eyes turned milky white with blindness from chronic weeping (Ibyaddat 'aynahu).\n"
        "- Sons rebuke him: 'You will not stop until fatally ill!' Suffering held in suppression."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. The Sublime Complaint: Baththee wa Huznee ila Allah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Defining formula: 'I only complain of my anguish and grief to Allah alone!'\n"
        "- Complaining to creation brings humiliation; pouring grief to God brings healing.\n"
        "- Prophetic defiance of despair: 'Never despair of Allah's mercy; only deniers despair.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE GRAND RECONCILIATION & REALIZATION OF THE STARS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE GRAND RECONCILIATION & REALIZATION OF THE STARS",
        "Pillars 15 & 16: Ana Yusuf, La Tathreeb, Restored Sight, Prostration of Eleven Stars & Tawaffanee Musliman",
        "PLATE 08 : RECONCILIATION & DREAMS"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: ANA YUSUF, THE SHIRT OF VISION & LA TATHREEB", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Brothers Humbled, Grand Revelation, Immortal Pardon & Scent of Yusuf", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. The Desperate Return & Begging for Imperial Charity", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Brothers return to Egypt begging: 'Adversity has touched our family; be charitable!'\n"
        "- The once formidable clan humbled to desperate mendicants before the sold boy.\n"
        "- Complete reversal of status engineered by sovereign divine decree."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. The Grand Revelation: Ana Yusufu wa Hadha Akhee", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Yusuf asks: 'Do you know what you did with Yusuf and brother in ignorance?'\n"
        "- Brothers recognize his eyes: 'Are you indeed Yusuf?!' Declaration: 'Ana Yusuf!'\n"
        "- 'Whoever fears Allah and is patient, Allah wastes not the reward of the Muhsineen.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. Immortal Prophetic Pardon: La Tathreeba 'Alaykum", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Brothers confess: 'By Allah, Allah favored you; we were sinners!'\n"
        "- Supreme pardon: 'La tathreeba 'alaykumul-yawm, yaghfirullahu lakum!' (No blame today!).\n"
        "- Recited verbatim by Prophet Muhammad ﷺ upon the historic Conquest of Mecca."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. The Shirt of Vision: Eyesight Miraculously Restored", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Cast this shirt over my father's face; he will regain sight.' Caravan departs.\n"
        "- In Canaan, Ya'qub perceives: 'Innee la-ajidu reeha Yusuf' (I smell the scent of Yusuf!).\n"
        "- The shirt that brought false tears now brings miraculous vision and healing."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: ELEVATION TO THE THRONE, DREAM REALIZED & FINAL PRAYER", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Household Migration, Prostration of Eleven Stars, Divine Lutf & Dying as a Muslim", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. Royal Welcome into Egypt: Enter in Safety (Aamineen)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Entire household of Ya'qub migrates from Canaan's famine into lush Egypt.\n"
        "- Royal greeting: 'Enter Egypt, if Allah wills, in safety and security (Aamineen).'\n"
        "- Elevating parents upon imperial throne (Rafa'a abawayhi 'alal-'arsh)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. Fulfillment of Celestial Vision: Ya Abati Hadha Ta'weel", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Eleven brothers and parents fall prostrate in honor before Yusuf.\n"
        "- Tearful awe: 'O father, this is the interpretation of my dream of old; my Lord made it real!'\n"
        "- Decades of slavery and prison culminate in the exact vision of the eleven stars."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. The Subtle Symphony of Divine Grace (Inna Rabbee Lateef)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Gracious speech omitting mention of the well to spare brothers' feelings.\n"
        "- Theological summary: 'Indeed, my Lord is Subtle in fulfilling what He wills (Lateef).'\n"
        "- Divine decree working invisibly through reversals to produce triumphant outcomes."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. Ultimate Prophetic Aspiration: Tawaffanee Musliman", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- At the peak of worldly empire, Yusuf turns to God: 'You gave me sovereignty...'\n"
        "- Final prayer: 'Cause me to die as a Muslim, and join me with the righteous!'\n"
        "- Mortal power is fleeting; the ultimate victory is dying in pure submission to Allah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector PDF: {OUTPUT_PDF} (8 pages)")

    # Render PNG previews via pdftoppm
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "yusuf_page")]
    subprocess.run(cmd, check=True)
    print("Rendered 8 preview PNGs in 07_MINDMAP/previews/")

    # Copy preview PNGs to brain directory for artifact viewing
    for p in range(1, 9):
        src_png = os.path.join(PREVIEWS_DIR, f"yusuf_page-{p}.png")
        dst_png = os.path.join(brain_dir, f"yusuf_page-{p}.png")
        if os.path.exists(src_png):
            shutil.copy2(src_png, dst_png)
    print("Copied 8 preview PNGs to brain directory")

if __name__ == "__main__":
    build_yusuf_pdf()
