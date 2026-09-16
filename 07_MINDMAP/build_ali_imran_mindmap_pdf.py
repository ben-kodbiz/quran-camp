#!/usr/bin/env python3
"""
Huurs Studio - Surah Ali-Imran Master Landscape Mindmap PDF CompilerStrict Standardization:
- Title: Surah Ali-Imran — Master Landscape Mindmap
- Zero Ayah Numbers in titles/headers/cards
- Zero mention of external speaker names; 100% Huurs Studio & Sunni source discipline
- Thematic sequence purity
- 8 Landscape Widescreen Pages (792 x 480 pts, 1.65:1 / 16:9 ratio)
- Symmetrical 2-column layout (c1_w = 348, c2_w = 348)
- 16 Thematic Pillars & 64 Structured Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "ALI_IMRAN_MASTER_MINDMAP.pdf")
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

def build_ali_imran_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        # Background
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH ALI-IMRAN", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Sub-title Bar
        pdf.text(title, 32, h - 66, font="F2", size=12, rgb=WHITE)
        pdf.text(subtitle, 32, h - 79, font="F1", size=7.8, rgb=TEXT_MUTED)
        badge_str = f"[{section_badge}]"
        badge_w = len(badge_str) * 6.1
        pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=10.5, rgb=GOLD)
        pdf.line(32, h - 86, w - 32, h - 86, stroke_rgb=BORDER_MUTED, line_width=0.8)

        # Bottom Footer
        pdf.line(32, 25, w - 32, 25, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE  *  READ. REFLECT. RETURN.", 32, 13, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("SURAH ALI-IMRAN FOUNDATION ARCHITECTURE", w - 245, 13, font="F2", size=7.2, rgb=GOLD)

    # Column Coordinates
    c1_x, c1_y, c1_w, c1_h = 32, 35, 348, h - 130
    c2_x = c1_x + c1_w + 32
    c2_w = 348

    # =========================================================================
    # PAGE 1: EPISTEMOLOGY, REVELATION & THE PRIMORDIAL CREED
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "EPISTEMOLOGY, REVELATION & THE PRIMORDIAL CREED",
        "Pillars 1 & 2: Muhkam vs. Mutashabih, Rooted Scholars, Rabbana La Tuzigh, and The Metric of Divine Love",
        "PLATE 01 : FOUNDATION CREED"
    )

    # Column 1: Pillar 1 (Epistemology & Rooted Scholarship)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: EPISTEMOLOGY & ROOTED SCHOLARSHIP", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Muhkam, Mutashabih & Epistemological Humility", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Umm al-Kitab: The Decisive Core of Revelation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Muhkamat: Explicit, unequivocal verses forming the mother/core of the Book.\n"
        "- They establish immutable creed, moral boundaries, and unambiguous law.\n"
        "- They serve as the constitutional anchor that prevents theological drift."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Mutashabihat: The Crucible of Human Humility", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Mutashabihat: Multi-dimensional, allegorical verses regarding the Unseen.\n"
        "- Diseased hearts obsess over ambiguities seeking discord and false interpretation.\n"
        "- Revelation intentionally contains mystery to test intellectual submission."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Al-Rasikhuna fil-'Ilm: Deeply Rooted Wisdom", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rooted scholars interpret the ambiguous strictly in light of the clear core.\n"
        "- Their defining hallmark is not arrogant debate, but reverent surrender.\n"
        "- Their declaration: 'We believe in it; all of it is from our Lord!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Al-Hayyul-Qayyum: The Uncreated Fountainhead", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Opens with the supreme divine names mirroring the crown of Ayat al-Kursi.\n"
        "- The Ever-Living, Self-Sustaining Lord who holds creation in continuous order.\n"
        "- Anchors human epistemology in an absolute, unshakeable ontological source."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2 (Anchored Heart & Prophetic Metric)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE ANCHORED HEART & PROPHETIC METRIC", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Rabbana La Tuzigh & The Verification of Love", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Rabbana La Tuzigh: The Supplication of the Rooted", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Our Lord, let not our hearts deviate after You have guided us.'\n"
        "- Intellectual brilliance cannot safeguard faith without continuous divine grace.\n"
        "- Teaches that deviation is a perpetual hazard requiring daily begging for mercy."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Divine Bestowal: Al-Wahhab and Pure Grace", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Guidance is not an entitlement earned by human intellect, but an unearned gift.\n"
        "- Al-Wahhab bestows spiritual firmness from His immediate presence (Ladunka).\n"
        "- Humility before the Bestower dissolves self-congratulatory spiritual pride."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Prophetic Emulation: The Metric of Love", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Say: If you love Allah, then follow me, and Allah will love you.'\n"
        "- The Divine Love Metric: Divine love is not sentimental emotion or poetry.\n"
        "- True love is verified exclusively through rigorous imitation of the Messenger."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Sovereign Criterion: Warning Against Deviation", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Obey Allah and the Messenger; turning away exposes counterfeit devotion.\n"
        "- Rejects esoteric spiritualities that bypass legal and moral commandments.\n"
        "- Alignment with the Prophetic model is the sole gateway to divine forgiveness."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: THE FAMILY OF IMRAN & THE SANCTUARY OF MARYAM
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE FAMILY OF IMRAN & THE SANCTUARY OF MARYAM",
        "Pillars 3 & 4: Hannah's Dedicated Vow, The Mihrab Miracles, and Zakariyya's Renewal of Hope",
        "PLATE 02 : SANCTUARY & DEVOTION"
    )

    # Column 1: Pillar 3 (Hannah's Vow & Maryam's Sanctuary)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: HANNAH'S VOW & MARYAM'S SANCTUARY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Unconditional Consecration & Out-of-Season Fruits", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Divine Election of the Righteous Lineage", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah chose Adam, Nuh, Ibrahim's family, and Imran's family over all mankind.\n"
        "- A lineage of unbroken devotion where each generation passed the flame of faith.\n"
        "- Spiritual nobility is anchored in moral uprightness, not biological privilege."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Hannah's Consecrated Vow (Muharraran)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Hannah dedicated her unborn child exclusively to divine sanctuary service.\n"
        "- Surrendering personal possessiveness: The child belongs entirely to God.\n"
        "- Sincere maternal intention transforms private birth into a cosmic turning point."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Female Elevated Beyond Expectation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hannah surrendered: 'And the male is not like the female.'\n"
        "- Divine wisdom honored her birth, elevating Maryam above all worldly men.\n"
        "- Protected Maryam and her child from Satan's touch at the instant of birth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Mihrab: Sanctuary of Out-of-Season Fruits", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Secluded in devotion, Maryam received winter fruit in summer and summer in winter.\n"
        "- When asked, she replied: 'It is from Allah; He provides without measure.'\n"
        "- The Mihrab proves that God transcends biological seasons and human limits."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4 (Zakariyya's Petition & Yahya)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: ZAKARIYYA'S PETITION & YAHYA'S PROMISE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Audacious Hope & The Miraculous Conception", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Catalyst: Witnessing Impossible Sustenance", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Witnessing Maryam's out-of-season fruit revived Zakariyya's dormant hope.\n"
        "- If God provides fruit without trees, He can provide a child without youth.\n"
        "- Spiritual fellowship ignites audacious supplication in barren circumstances."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Supplication for Pure Lineage (Dhurriyyatan Tayyibah)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Prayed not for genetic immortality or worldly legacy, but for a pure servant.\n"
        "- Sincere prayer in the Mihrab: 'Indeed, You are the Hearer of all prayer.'\n"
        "- Selfless paternal intention oriented wholly toward divine worship."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Angelic Glad Tidings of Yahya", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Angels called while he stood praying: Allah gives glad tidings of Yahya.\n"
        "- A witness confirming the Word from Allah, noble, chaste, and a prophet.\n"
        "- Divine response breaks biological impossibility in an instant."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Sign of Sacred Silence: Three Days of Dhikr", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Zakariyya's sign: Inability to speak to people for three days except by gesture.\n"
        "- Speech arrested from mundane chatter, yet freed for glorifying God abundantly.\n"
        "- Silence disciplines the tongue and focuses the soul on constant Dhikr."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE REALITY OF ISA & THE DECISIVE THEOLOGICAL PROOF
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE REALITY OF ISA & THE DECISIVE THEOLOGICAL PROOF",
        "Pillars 5 & 6: Creation from Dust, Miracles by Divine Leave, and The Ultimate Proof of Mubahalah",
        "PLATE 03 : PURE MONOTHEISM"
    )

    # Column 1: Pillar 5 (Creation from Dust: Kamathali Adam)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: CREATION FROM DUST: KAMATHALI ADAM", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Demolition of Deification & The Command Kun", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Annunciation & Infancy Miracles", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Maryam chosen above the women of all creation, receiving the Word from Allah.\n"
        "- Isa speaks from the cradle in mature eloquence to exonerate his mother.\n"
        "- Demonstrating prophetic authority from infancy without claiming divinity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Prophetic Signs Subordinated to Divine Will", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Fashioning clay birds, healing the blind and leper, and raising the dead.\n"
        "- Every miracle explicitly bound to 'Bi-Idhnillah' (by Allah's permission).\n"
        "- Signs are instruments of Prophetic vindication, not proofs of godly essence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Kamathali Adam: The Decisive Exegetical Parable", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'The likeness of Isa with Allah is as the likeness of Adam.'\n"
        "- Created from dust without father or mother; if birth without father proved\n"
        "- Divinity, Adam would have greater claim. Both are humble servants made of dust."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Kun Fa-Yakun: Sovereign Transcendent Fiat", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Creation requires no biological mechanism, spouse, or earthly parentage.\n"
        "- When Allah decrees an affair, He merely says 'Be' (Kun) and it is.\n"
        "- Exalts Allah above pagan notions of physical procreation and divine sonship."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6 (Disciples, Ascent & Mubahalah)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: DISCIPLES, ASCENT & MUBAHALAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Hawariyyun, Heavenly Elevation & Decisive Conviction", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Al-Hawariyyun: Helpers of Allah in Faith", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When Isa sensed disbelief, he asked: 'Who are my helpers for Allah?'\n"
        "- The disciples responded: 'We are helpers of Allah; we believe in Him.'\n"
        "- True followers identify themselves as Muslims submitting to one God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Divine Elevation: Refuting Crucifixion & Murder", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- The plotters schemed, but Allah is the best of planners (Makr).\n"
        "- 'I will take you and raise you to Myself and purify you from the deniers.'\n"
        "- Isa was not humiliated on a cross; his honor was preserved by divine rescue."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Event of Mubahalah: Invoking the Curse", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Confronting Najran's dogmatic stubbornness with the ultimate test of truth.\n"
        "- The Prophet was ordered to gather his family and invoke Allah's curse on liars.\n"
        "- Ultimate proof of moral conviction: Liars never risk the destruction of loved ones."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Retreat of Najran & Unquestioned Truth", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- The Najran delegation withdrew from the duel of prayer, seeking peaceful treaty.\n"
        "- Their retreat stands in history as silent admission of Islamic authenticity.\n"
        "- Monotheism stands vindicated on both rational argument and spiritual reality."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE SCRIPTURAL DIALOGUE & THE IBRAHIMIC STANDARD
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE SCRIPTURAL DIALOGUE & THE IBRAHIMIC STANDARD",
        "Pillars 7 & 8: Kalimatin Sawa', Exonerating Ibrahim, The Prophetic Covenant, and The Summit of Charity",
        "PLATE 04 : ABRAHAMIC COVENANT"
    )

    # Column 1: Pillar 7 (The Equitable Word & Ibrahimic Monotheism)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE EQUITABLE WORD & IBRAHIM", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Common Ground, Primordial Islam & Dismantling Sects", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Kalimatin Sawa': The Invitation to Common Ground", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Come to a word that is equitable between us and you.'\n"
        "- That we worship none but Allah and associate no partner with Him.\n"
        "- Establishing that religious unity can only rest on pure Tawhid."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Ma Kana Ibrahimu: Exonerating the Patriarch", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Ibrahim was neither a Jew nor a Christian; he was Hanifan Musliman.'\n"
        "- Torah and Gospel were revealed centuries after Ibrahim's passing.\n"
        "- Exposing retroactive sectarian claims as historically anachronistic."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Hanifan Musliman: Upright Primordial Submission", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hanif: Turning away from all falsehood toward uncompromising Tawhid.\n"
        "- Ibrahim was never of the polytheists in theology or allegiance.\n"
        "- Islam is not a 7th-century novelty, but the primordial religion of all prophets."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Reclaiming Sacred Spiritual Lineage", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- 'Indeed, the closest people to Ibrahim are those who followed him, this Prophet'\n"
        "- Spiritual legitimacy belongs to those who embody the patriarch's monotheism.\n"
        "- Faith in the Final Messenger supersedes biological and tribal genealogies."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8 (Prophetic Covenant & Peak Charity)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: PROPHETIC COVENANT & PEAK CHARITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Mithaq al-Nabiyyeen & Spending What is Beloved", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Mithaq al-Nabiyyeen: The Covenant of All Messengers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Every prophet took a sacred oath to believe in and aid the Final Messenger.\n"
        "- Establishing the cosmic brotherhood and unity of all divine missions.\n"
        "- Rejection of the Prophet Muhammad contradicts the core pledge of past prophets."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Islam: The Sole Divine Deen Accepted by God", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Whoever desires other than Islam as religion, never will it be accepted.'\n"
        "- In the Hereafter he will be among the ultimate losers.\n"
        "- Rejects religious relativism: Truth is unified and singular before Allah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Lan Tanalul-Birr: The Summit of True Righteousness", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Never will you attain true righteousness until you spend from what you love.'\n"
        "- Faith is not verified by discarding excess leftovers or token scraps.\n"
        "- The spiritual summit requires detaching the heart from cherished wealth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Noble Sacrifice of Abu Talha", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Abu Talha gave up Bairuha', his most beloved, freshwater palm garden.\n"
        "- Surrendered instantly upon hearing the verse, asking for nothing in return.\n"
        "- Living proof of how the Companions translated abstract verses into deeds."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: THE GOLDEN ANCHOR OF UNITY & THE BEST NATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE GOLDEN ANCHOR OF UNITY & THE BEST NATION",
        "Pillars 9 & 10: Holding Fast to Hablillah, Reconciliation of the Heart, and The Mandate of Khayra Ummah",
        "PLATE 05 : CHARTER OF UNITY"
    )

    # Column 1: Pillar 9 (Holding the Rope of Allah)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: HOLDING THE ROPE OF ALLAH (HABLILLAH)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Uncompromising Taqwa & Healing Ancient Blood Feuds", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Ittaqu Allaha Haqqa Tuqatih: The Standard of Taqwa", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Fear Allah as He deserves to be feared, and do not die except as Muslims.'\n"
        "- Ibn Mas'ud: Remembered and not forgotten, obeyed and not disobeyed, thanked.\n"
        "- Vigilant God-consciousness must govern every breath until death."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Hablillah: The Unbreakable Divine Lifeline", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Hold fast to the rope of Allah all together, and do not become divided.'\n"
        "- The Qur'an and authentic Sunnah form the sole vertical anchor of community.\n"
        "- Collective survival is impossible when individual strands sever connection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Miraculous Union of Hearts (Aws & Khazraj)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Reminding the Ansar of centuries of tribal civil slaughter and hatred.\n"
        "- Islam bonded their hearts when they stood on the brink of a pit of Fire.\n"
        "- Fraternal unity is a divine miracle that no worldly wealth could buy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Mortal Ruin of Sectarian Fracturing", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Warning against imitating nations who splintered after clear proof came.\n"
        "- Sectarian fracturing invites humiliating punishment in this world and next.\n"
        "- Preservation of community unity is an existential theological duty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10 (Universal Mandate: Khayra Ummah)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: THE UNIVERSAL MANDATE: KHAYRA UMMAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Moral Activism, Civilizational Leadership & Cosmic Dignity", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Dedicated Vanguard of Public Reform", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Let there arise from you a nation inviting to good and enjoining right.'\n"
        "- An institutional core dedicated to spiritual education and social justice.\n"
        "- Civilizations rot from within when moral accountability is abandoned."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Definition of Khayra Ummah: Best Nation", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'You are the best nation brought forth for mankind.'\n"
        "- Superiority is not genetic or tribal; it exists purely as functional service.\n"
        "- Enjoining what is right, forbidding evil, and uncompromising faith in Allah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Moral Activism on Behalf of All Humanity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Ukhrijat lin-Nas': Brought forth outwardly for the benefit of all humanity.\n"
        "- The community exists not for inward tribal enrichment, but universal blessing.\n"
        "- Rescuing humanity from tyranny, exploitation, and spiritual blindness."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Luminous Faces vs. Darkened Faces on the Day", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- The Day when some faces turn radiant white with joy and others turn black.\n"
        "- The radiant: People of unity and Sunnah enveloped in eternal divine mercy.\n"
        "- The darkened: People of sectarian division who bartered truth for discord."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE CRUCIBLE OF UHUD: DISCIPLINE & DIVINE AUDIT
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE CRUCIBLE OF UHUD: DISCIPLINE & DIVINE AUDIT",
        "Pillars 11 & 12: The Archers' Deviation, The Contrast of Badr, Sorrow Upon Sorrow, and The Purifying Fire",
        "PLATE 06 : THE CRUCIBLE OF UHUD"
    )

    # Column 1: Pillar 11 (The Archers' Deviation & The Lure of Dunya)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: ARCHERS' DEVIATION & THE LURE OF DUNYA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Mount Rumah, Strategic Discipline & Exposed Desires", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Contrast: Badr Humility vs. Uhud Complacency", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- At Badr, Muslims were weak, helpless (Adhilla), relying 100% on God: Victory.\n"
        "- At Uhud, tactical confidence and material distraction compromised obedience.\n"
        "- Physical superiority means nothing without total spiritual surrender."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Sacred Order on Mount Rumah", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Fifty archers posted with absolute command: Guard our back under all odds.\n"
        "- Even if you see birds snatching our flesh, do not leave until ordered.\n"
        "- Frontline discipline is the non-negotiable safeguard of the entire body."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Catastrophic Desertion of the Post", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Enemy routed initially; forty archers rushed down to gather spoils.\n"
        "- Leaving only ten defenders exposed the mountain pass to enemy cavalry.\n"
        "- A single lapse in frontline discipline turned absolute triumph into rout."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Divine Diagnostic: Minkum Man Yureedud-Dunya", c1_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- 'Among you are some who desire this world, and some who desire Hereafter.'\n"
        "- God lays bare the hidden motive: A tiny crack of Dunya infected the ranks.\n"
        "- Collective disaster often stems from internal spiritual compromise."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12 (Sorrow Upon Sorrow & The Purifying Fire)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: SORROW UPON SORROW & THE PURIFYING FIRE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ghamman bi-Ghamm, The False Rumor & Purification", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Sorrow Compounded: Ghamman bi-Ghamm", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Loss of spoils, military encirclement, 70 martyrs, and injuries to the Prophet.\n"
        "- Divine pedagogy: Overwhelming sorrow cures attachment to lesser worldly loss.\n"
        "- Pain acts as psychological cauterization, purifying the soul of trivia."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Anchored to the Message, Not the Mortal Messenger", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- False rumor that the Prophet was killed shattered morale on the battlefield.\n"
        "- 'Muhammad is but a messenger; if he dies or is killed, will you turn back?'\n"
        "- Faith must be anchored in the Living, Eternal Creator, not earthly presence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Divine Surgery: Purging Hypocrisy from Ranks", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Adversity acts as divine filtration (Tamhees), separating gold from slag.\n"
        "- Hypocrites deserted before battle; adversity unmasks hidden traitors.\n"
        "- A smaller, purified community is invincible compared to a compromised crowd."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Mandate Against Despair: Wa La Tahinu", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- 'Do not weaken and do not grieve; you will be superior if you are believers.'\n"
        "- History alternates in alternating cycles (Al-Ayyam) to cultivate true patience.\n"
        "- Defeat in battle is not defeat in cosmic reality; true victory is steadfast faith."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: LEADERSHIP IN CRISIS & THE LIVING MARTYRS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "LEADERSHIP IN CRISIS & THE LIVING MARTYRS",
        "Pillars 13 & 14: Prophetic Mildness, Restorative Shura, Tawakkul, and The Emerald Birds of Paradise",
        "PLATE 07 : RESTORATIVE GOVERNANCE"
    )

    # Column 1: Pillar 13 (Prophetic Mildness & Shura)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: PROPHETIC MILDNESS, SHURA & TAWAKKUL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Linta Lahum & The Fourfold Leadership Architecture", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Linta Lahum: Divine Mercy Manifested in Mildness", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'By mercy from Allah, you were gentle with them in the aftermath of defeat.'\n"
        "- Had the Prophet been harsh or hard-hearted, the community would have dispersed.\n"
        "- True leadership heals fractured followers rather than crushing them in blame."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Fa'fu 'Anhum & Wastaghfir Lahum: The Double Pardon", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Step 1: Pardon them personally for tactical errors and battlefield disobedience.\n"
        "- Step 2: Pray for their divine forgiveness before God to remove spiritual guilt.\n"
        "- A leader absorbs personal grief and intercedes for the moral recovery of staff."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Wa Shawirhum fil-Amr: Restoring Dignity Through Shura", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Re-engaging the very men whose advice led to catastrophe in new consultation.\n"
        "- Consultation restores broken dignity, rebuilding confidence and ownership.\n"
        "- Shura prevents autocratic bitterness and reaffirms community solidarity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Fa-Idha 'Azamta Fa-Tawakkal: Resolute Execution", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Once a decision is resolved, move forward with absolute reliance upon Allah.\n"
        "- Eliminating second-guessing, paralyzing 'what-ifs', and post-hoc regret.\n"
        "- Total Tawakkul balances consultative wisdom with decisive moral action."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14 (The Living Martyrs & Serenity)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: THE LIVING MARTYRS & TRANQUILITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ahya'un 'Inda Rabbihim & Serenity Amidst Chaos", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. An-Nu'as: Supernatural Slumber of Serenity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- In the thick of peril, divine peace caused sincere believers to nod in sleep.\n"
        "- Swords slipped from hands in miraculous calm; psychological sign of faith.\n"
        "- Divine tranquility descends precisely when worldly terror peaks."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Torment of Jahiliyyah Suspicion", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- In contrast, hypocrites stayed awake, sweating in self-absorbed anxiety.\n"
        "- Thinking thoughts of Jahiliyyah: 'Had we a say, we would not have been killed.'\n"
        "- Lack of faith traps the soul in paranoid dread and bitter self-pity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Bal Ahya'un: Transcendent Reality of Martyrs", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Do not think of those killed in the path of Allah as dead.'\n"
        "- Rather, they are alive with their Lord, receiving celestial provision.\n"
        "- Death in the path of truth is not termination, but graduation into real life."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Emerald Birds Beneath the Throne of God", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Authentic Hadith: Souls of martyrs inhabit green birds roaming Paradise.\n"
        "- Roosting in golden chandeliers suspended beneath the Divine Throne.\n"
        "- Begging God to return to earth solely to experience the joy of martyrdom again."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE ULUL-ALBAB & THE COSMOLOGICAL SEAL
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE ULUL-ALBAB & THE COSMOLOGICAL SEAL",
        "Pillars 15 & 16: Cosmic Contemplation, Purposeful Creation, Answered Petitions, and The Quadruple Mandate",
        "PLATE 08 : THE COSMOLOGICAL SEAL"
    )

    # Column 1: Pillar 15 (Cosmological Contemplation & Intellect)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: COSMOLOGICAL CONTEMPLATION & INTELLECT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ulul-Albab, Night Architecture & Purposeful Creation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Cosmic Signs for People of Intellect (Ulul-Albab)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- In the creation of heavens, earth, and alternation of night and day are signs.\n"
        "- The Prophet wept until his beard was soaked: 'Woe to him who reads and reflects not!'\n"
        "- Nature is not an inert backdrop, but a dynamic scripture shouting God's glory."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Standing, Sitting, and on Sides: Constant Dhikr", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- The hallmark of the wise: Remembering Allah across all postures of life.\n"
        "- Scientific exploration divorced from divine remembrance produces nihilism.\n"
        "- The Qur'an unifies cosmic observation with deep, trembling worship."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Rabbana Ma Khalaqta Hadha Batila: Cosmic Purpose", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Our Lord, You did not create all this in vain; Glory be to You!'\n"
        "- Teleological conviction: The universe is not an accidental cosmic accident.\n"
        "- Every celestial orbit, atomic particle, and season possesses divine purpose."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Subhanaka Faqina 'Adhaban-Nar: Moral Reflex", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- True cosmological insight does not end in cold intellectual abstraction.\n"
        "- It triggers an immediate moral reflex: Exalt God and beg rescue from Hellfire.\n"
        "- Linking cosmic grandeur directly with personal moral responsibility."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16 (Answered Petitions & Final Mandate)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: ANSWERED PETITIONS & FINAL MANDATE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Fastajaba Lahum & The Quadruple Blueprint for Success", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Fastajaba Lahum Rabbuhum: Divine Confirmation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Their Lord responded: 'I will never lose the deed of any worker among you.'\n"
        "- Whether male or female, you are of one another in moral accountability.\n"
        "- Absolute spiritual equality: Every tear, sacrifice, and action is rewarded."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Expiation & Eternal Gardens Beneath Rivers", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Those who emigrated, were expelled, and harmed in God's path have sins erased.\n"
        "- Admitted into gardens beneath which rivers flow as reward from Allah.\n"
        "- Earthly displacement and battlefield sorrow culminate in eternal triumph."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Illusion of Worldly Material Dominance", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Let not the strutting of the deniers through the lands deceive you.'\n"
        "- Brief worldly enjoyment (Mata'un Qaleel), then their refuge is Hell.\n"
        "- Warning the believers never to measure ultimate truth by temporary wealth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Final Quadruple Mandate for Ultimate Triumph", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- 1. Isbiru (Endure personally)  2. Sabiru (Outvie in collective patience)\n"
        "- 3. Rabitu (Remain steadfast at the posts)  4. Ittaqullah (Fear Allah).\n"
        "- The definitive seal: Internal resilience and constant Taqwa guarantee success."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Successfully generated {OUTPUT_PDF}")

    # Generate PNG previews via pdftoppm
    print("Generating PNG previews...")
    cmd = [
        "pdftoppm", "-png", "-r", "150",
        OUTPUT_PDF,
        os.path.join(PREVIEWS_DIR, "ali_imran_page")
    ]
    subprocess.run(cmd, check=True)
    print(f"Previews saved to {PREVIEWS_DIR}")

    # Copy previews to brain directory
    for f in os.listdir(PREVIEWS_DIR):
        if f.startswith("ali_imran_page-") and f.endswith(".png"):
            src = os.path.join(PREVIEWS_DIR, f)
            dst = os.path.join(brain_dir, f)
            shutil.copy2(src, dst)
            print(f"Copied {f} to brain directory: {dst}")

if __name__ == "__main__":
    build_ali_imran_pdf()
