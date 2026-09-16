#!/usr/bin/env python3
"""
Huurs Studio - Surah Hud Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "HUD_MASTER_MINDMAP.pdf")
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

def build_hud_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH HUD", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PAGE 1: THE PERFECTED BOOK, DIVINE SUSTENANCE & THE PRIMORDIAL WATER
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE PERFECTED BOOK, DIVINE SUSTENANCE & THE PRIMORDIAL WATER",
        "Pillars 1 & 2: Perfection of Scripture, Istighfar, Sustenance of Creatures & The Throne Upon Water",
        "PLATE 01 : CREATION & SUSTENANCE"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: PERFECTION OF SCRIPTURE & THE ECONOMY OF ISTIGHFAR", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Uhkimat thumma Fussilat, Noble Provision & Omniscience Behind Garments", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Perfected & Detailed Scripture", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Opening with Alif-Lam-Ra: Fortified against flaw or human corruption (Uhkimat).\n"
        "- Expounded in legal, creedal, and historical detail from One All-Wise (Fussilat).\n"
        "- Demanding devotion solely to Allah as a warner and bearer of glad tidings."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. The Economy of Istighfar & Noble Provision", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Direct linkage between seeking forgiveness (Istighfar) and repentance (Tawbah).\n"
        "- Guarantees dignified, fruitful earthly life (Mata'an Hasanan) without privation.\n"
        "- Awards every possessor of merit and spiritual virtue their deserved bounty (Fadl)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. The Folly of Concealing the Chest", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Evasion of the deniers: physically bending and folding their chests inward.\n"
        "- The childish delusion that bodily contortions can hide thoughts from the Creator.\n"
        "- Exposing the vanity of attempting secrecy in a universe flooded with divine light."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. Omniscience Behind the Veil of Garments", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Even when humans wrap themselves tightly in cloaks in darkened rooms, Allah sees.\n"
        "- Absolute knowledge of what they keep hidden and what they openly manifest.\n"
        "- Fully Cognizant of the innermost secrets of the breasts ('Aleemun bi-Dhati as-Sudoor)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: SUSTENANCE OF ALL CREATURES & THE THRONE UPON WATER", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Guaranteed Rizq, Audited Habitats & The Cosmic Purpose of Conduct", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. Guaranteed Sustenance of Every Moving Creature", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ontological promise: The provision of every crawling creature rests upon Allah.\n"
        "- Liberating the heart from scarcity anxiety; nourishment is divinely distributed.\n"
        "- Combining diligent pursuit of worldly means with absolute reliance upon the Provider."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. Knowledge of the Resting Place & Repository", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine oversight encompasses every creature's nest/grave and foraging grounds.\n"
        "- Mustaqarr (permanent abode) and Mustawda' (temporary transit station) recorded.\n"
        "- Everything audited in an explicit, manifest celestial ledger (Kitabin Mubeen)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. The Primordial Water & The Divine Throne", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Before the creation of heavens and earth in six epochs, His Throne was over Water.\n"
        "- Authenticated in Sahih al-Bukhari: Allah existed before all temporal creation.\n"
        "- Water establishes the fundamental biological and physical cradle of all life."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. Existential Examination of Conduct", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cosmic purpose: Testing which of humanity is finest in conduct (Ahsanu 'Amala).\n"
        "- Fudayl ibn 'Iyad: Defined as most sincere (Akhlasuh) and most Sunnah-compliant (Aswabuh).\n"
        "- Rejection of quantitative pride; moral excellence is the sole divine currency."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: PSYCHOLOGICAL VOLATILITY, PROPHETIC BURDEN & THE TEN SURAHS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "PSYCHOLOGICAL VOLATILITY, PROPHETIC BURDEN & THE TEN SURAHS",
        "Pillars 3 & 4: Despair vs. Boasting, Prophetic Empathy, Inimitable Ten Surahs & The Two Parables",
        "PLATE 02 : PSYCHOLOGY & CHALLENGE"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE POLARIZED HUMAN SOUL: DESPAIR VS. BOASTING", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ya'oosun Kafoor, Farihun Fakhoor & The Anchor of Righteous Patience", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. The Volatile Swings: Despairing Ungratefulness", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When divine bounty is withdrawn, secular man plunges into bitter despair.\n"
        "- Amnesia regarding years of prior ease; adopting a petulant, ungrateful posture.\n"
        "- Showing how absent faith, suffering inevitably breeds cynicism and nihilism."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. The Delusion of Prosperity: Boastful Pride", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When relief arrives, man proclaims: 'Hardship has departed from me!'\n"
        "- Intoxicated with boastful swagger (Farihun Fakhoor), attributing success to himself.\n"
        "- The cycle of human instability: manic arrogance in wealth, depression in trial."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. The Anchored Soul: Patience & Righteous Deeds", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The sole exception: Those who ground themselves in Sabr and righteous action.\n"
        "- Patience cushions the impact of loss; righteous deeds humble during abundance.\n"
        "- Their eternal destiny: divine pardon (Maghfirah) and a tremendous reward (Ajrun Kabeer)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. Constriction of the Prophetic Breast & Reassurance", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine empathy for the Prophet's constricted chest facing insults and mockery.\n"
        "- The Prophet's sorrow stemmed from compassionate agony for blind rejectors.\n"
        "- Establishing boundaries: 'You are only a warner; Allah is Trustee over all things.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: DEMANDS FOR SIGNS & THE INIMITABLE CHALLENGE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Rejection of Sensationalism, Ten Fabricated Surahs & Spiritual Senses", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. Demands for Golden Treasures & Physical Angels", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Skeptics demanding sensational spectacle: chests of gold or visible angelic bodyguards.\n"
        "- Exposing materialistic prejudice: confusing moral truth with vulgar displays of wealth.\n"
        "- Spiritual transformation requires moral awakening, not coercive physical theater."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. The Challenge of Ten Fabricated Surahs", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Accused of inventing the Qur'an; the counter-challenge: produce ten chapters like it.\n"
        "- Permission granted to fabricate content (Muftarayat), yet human capability failed.\n"
        "- Open invitation to summon all poets, scholars, and earthly deities to assist."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. Revealed by the Supreme Omniscience of Allah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Conclusive proof: 'Know that it was revealed solely with the knowledge of Allah.'\n"
        "- Surpassing human literary and metaphysical boundaries across all generations.\n"
        "- The rational outcome: 'And that there is no deity except Him—will you submit?'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. Parable of the Blind/Deaf vs. Seeing/Hearing", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Metaphorical contrast of human faculties: The spiritually blind and deaf.\n"
        "- Juxtaposed against the believer possessing keen spiritual sight and attentive hearing.\n"
        "- The rhetorical inquiry: 'Are the two equal in likeness? Will you not remember?'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE EPIC OF PROPHET NUH: OLIGARCHIC SNEERS & BUILDING THE ARK
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE EPIC OF PROPHET NUH: OLIGARCHIC SNEERS & BUILDING THE ARK",
        "Pillars 5 & 6: Arrogance of Chieftains, Equality of Believers, The Desert Shipyard & Holy Composure",
        "PLATE 03 : NUH & THE ARISTOCRACY"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: CONFRONTING ARISTOCRATIC ARROGANCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Aradhiluna Baadiya ar-Ra'y, Safeguarding the Poor & Prophetic Altruism", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Nuh's Manifest Warning & Monotheistic Proclamation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nuh steps forward as a clear warner: 'Worship none except Allah alone.'\n"
        "- Expressing profound concern: 'Indeed, I fear for you the punishment of a painful day.'\n"
        "- Decades of selfless calling conducted without seeking political power or office."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. The Chieftains' Classist Contempt", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The ruling oligarchy (Al-Mala') sneered: 'We see you as a mere human like us.'\n"
        "- Attacked his followers as the lowest social class (Aradhiluna) of naive intellect.\n"
        "- Claiming systemic social superiority; using wealth as a weapon to reject truth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. Rejecting Aristocratic Bias & Guarding Believers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nuh refused to expel humble followers: 'I will not drive away those who believe.'\n"
        "- Declaring their eternal dignity: 'Indeed, they are to meet their Lord in honor.'\n"
        "- Warning the elites: 'Who would protect me from Allah if I drove them away?'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Independence of Prophetic Integrity: Zero Worldly Wage", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Disclaiming occult powers: 'I do not say I hold Allah's treasuries or unseen.'\n"
        "- Refusing to flatter aristocracy or judge hearts: 'Allah knows what is in souls.'\n"
        "- Total financial independence: 'My reward is not but from Allah alone.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE CRAFTING OF THE ARK UNDER DIVINE WATCH", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Bi-A'yunina wa Wahyina, Desert Shipyard & Sarcasm Returned", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. The Divine Blueprint: Building the Ark Under Our Eyes", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Command to construct the colossal vessel in arid desert: Bi-A'yunina wa Wahyina.\n"
        "- Executed under immediate divine surveillance and revealed engineering design.\n"
        "- Absolute boundary: 'Do not speak to Me regarding the wrongdoers; they are drowned.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. The Mockery of the Passing Chieftains", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Chieftains walking past erupted into derisive mockery at the dry-land shipyard.\n"
        "- Cynical insults: 'Yesterday you claimed prophethood, today you become a carpenter!'\n"
        "- Judging strictly by empirical surfaces, oblivious to the metaphysical tempest brewing."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. Prophetic Composure: Sarcasm Turned Upon Sarcastic", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nuh responds with serene equanimity: 'If you ridicule us, we will ridicule you.'\n"
        "- Psychological supremacy rooted in divine certainty over secular arrogance.\n"
        "- The tables of history will inevitably turn when cosmic reality shatters delusion."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. Absolute Certainty in the Imminent Humiliation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Announcing the impending cataclysm: 'You will soon know who receives doom.'\n"
        "- A punishment that humiliates them in time and an abiding doom across eternity.\n"
        "- Prophetic patience is restrained strength awaiting the divine court's execution."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE COSMIC DELUGE, THE DROWNED SON & RESTING ON MOUNT JUDI
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE COSMIC DELUGE, THE DROWNED SON & RESTING ON MOUNT JUDI",
        "Pillars 7 & 8: Eruption of the Tannoor, The Mountain Sanctuary Fallacy, Calming of the Deep & Severed Bloodlines",
        "PLATE 04 : DELUGE & MOUNT JUDI"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE BOILING TANNOOR, DELUGE & THE WAYWARD SON", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Farat-Tannoor, Bismillahi Majreeha & The Drowning of Nuh's Son", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. Eruption of the Oven as the Cosmic Flood Trigger", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The prearranged signal arrives: The domestic clay baking oven gushes water (Farat-Tannoor).\n"
        "- Total cosmic inversion: Subterranean abyss bursts where fire once burned.\n"
        "- Command to board pairs of every creature (Zawjayni Ithnayn) and believing household."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. The Sacred Embarkation: Bismillahi Majreeha wa Mursaaha", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Boarding formula: 'In the name of Allah is its sailing and its anchorage.'\n"
        "- The vessel had no sails or oars; steered solely by the Divine Name.\n"
        "- Foundational Islamic Sunnah: Invoking Allah at the start of any voyage or endeavor."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. Waves Towering Like Mountains & The Tragic Appeal", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Ark navigating mountainous waves surging like alpine peaks (Mawjin kal-Jibal).\n"
        "- Nuh calls his son standing apart: 'Ya bunayya-rkab ma'ana wa la takun ma'al-kafireen!'\n"
        "- Agonizing collision between tender parental love and divine sovereign reality."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. The Fallacy of the Mountain Sanctuary & Cleaving Wave", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rebellious son relies on topography: 'I will seek refuge on a high mountain.'\n"
        "- Nuh's truth: 'There is no protector today from Allah's decree except whom He mercies.'\n"
        "- A towering wave cleft them apart; the son was swallowed by the dark depths."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: CALMING OF THE WATERS & SEVERANCE OF BLOODLINES", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ya Ardu-bla'ee, Mount Judi Landing & Faith Superseding Biological Kinship", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. The Cosmic Royal Decree: Ya Ardu-bla'ee Maa'aki", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Pinnacle of Arabic eloquence: 'O earth, swallow your water! O sky, withhold!'\n"
        "- Two divine imperative words calm the planetary catastrophe and subside the ocean.\n"
        "- The solemn historical verdict: 'Away with the wrongdoing, unjust people!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. Resting of the Ark upon Mount Judi", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Ark comes to rest upon Mount Judi (Al-Joodiyy) in peace and divine security.\n"
        "- Preserving the pure seed of monotheism reborn from the ruins of corrupt civilization.\n"
        "- A physical geological monument enduring across millennia witnessing faith's triumph."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. The Agonized Paternal Plea: Rabbi Inna-bni min Ahli", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nuh calls his Lord in raw grief: 'My Lord, my son is of my family; Your promise is true.'\n"
        "- Seeking to reconcile initial promise of family salvation with fatherly heartbreak.\n"
        "- Showing prophets are fully human, feeling intense grief while remaining submissive."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. Divine Correction: Spiritual Alignment Supersedes Blood", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Supreme decree: 'O Nuh, indeed he is not of your family; his conduct is unrighteous.'\n"
        "- Spiritual kinship in Tawhid completely obliterates biological pedigree.\n"
        "- Nuh immediately repents, seeking refuge in Allah from asking without knowledge."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: PROPHETIC PERSISTENCE: HUD TO 'AD & SALIH TO THAMUD
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "PROPHETIC PERSISTENCE: HUD TO 'AD & SALIH TO THAMUD",
        "Pillars 9 & 10: Defiance Against 'Ad, Forelock Metaphysics, Earthly Stewardship & The Sonic Blast",
        "PLATE 05 : HUD & SALIH"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: HUD'S DEFIANCE AGAINST 'AD & RELIANCE ON THE FORELOCK", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Midrara Rain, Rebutting Idol Madness & Sovereignty Over Every Forelock", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. The Call to 'Ad: Purity of Worship & Spiritual Rain", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hud sent to towering empire of 'Ad: 'Worship Allah; you have no other god.'\n"
        "- Linking sincere repentance directly to abundant rain (Midrara) and physical strength.\n"
        "- The Islamic worldview: Spiritual rectitude brings environmental and economic blessing."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. Rebutting Accusations of Madness by Lifeless Idols", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Ad claimed their stone gods had seized Hud with madness and brain damage.\n"
        "- Attributing supernatural power to inanimate idols to excuse their moral rebellion.\n"
        "- Hud counters: 'I call Allah as witness, and bear witness that I am free from your idols!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. The Fearless Challenge: Plot Against Me Without Respite!", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Solitary prophet challenging an empire of weaponized giants: 'Plot against me all together!'\n"
        "- Demanding no respite; demonstrating total fearlessness in the face of brute force.\n"
        "- No empire can harm a hair on the believer's head without divine permission."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. Supreme Tawakkul: Holding Every Beast by Its Forelock", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Metaphysical formula: 'Not a moving creature but He holds it by its forelock (Nasiyah).'\n"
        "- The forelock symbolizes complete subjugation, humiliation, and control before God.\n"
        "- Absolute confidence: 'Indeed, my Lord is on a straight path (Siratin Mustaqeem).'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: SALIH TO THAMUD: EARTHLY STEWARDSHIP & THE SHE-CAMEL", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ista'marakum Feeha, Shared Water Rights & The Cataclysmic Sonic Blast", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. Stewards of the Soil: Settled to Cultivate the Earth", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Salih reminds Thamud: 'He brought you from earth and settled you to cultivate it.'\n"
        "- Human purpose includes ecological stewardship and ethical resource development.\n"
        "- Calling them to repent to an intimate, attentive Lord: 'Inna Rabbi Qareebun Mujeeb.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. The Miraculous She-Camel of Allah as Public Test", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Granted a living miraculous sign: Naqatullah (The She-Camel of Allah).\n"
        "- Communal test of sharing water: She drinks on one day, the tribe drinks on the next.\n"
        "- Testing a society's willingness to restrain greed and share public commons."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. Treacherous Hamstringing & The Three-Day Respite", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Corrupt chieftains conspired and slaughtered the She-Camel in open rebellion.\n"
        "- Salih delivers chilling countdown: 'Enjoy in your homes three days; an unlying promise.'\n"
        "- Three days of respite unheeded; cruelty to creation triggers civilizational collapse."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. The Sonic Blast: As Though They Had Never Dwelt There", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- On the fourth dawn, the terrifying sonic Blast (As-Sayhah) tore through Thamud.\n"
        "- Pulverizing internal organs, leaving them lifeless in their sophisticated stone palaces.\n"
        "- Haunting epitaph: 'As though they had never dwelt there (Ka-an lam yaghnaw feeha).'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: ANGELIC EMISSARIES TO IBRAHIM & THE DOOM OF SODOM
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "ANGELIC EMISSARIES TO IBRAHIM & THE DOOM OF SODOM",
        "Pillars 11 & 12: Roasted Calf, Sarah's Wonder, Lut's Agony, The Unshakeable Support & Rain of Sijjeel",
        "PLATE 06 : IBRAHIM & SODOM"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: ABRAHAMIC HOSPITALITY & SARAH'S ASTONISHED JOY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("'Ijlun Haneed, Glad Tidings of Isaac and Jacob & Ibrahim's Empathy", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. Angelic Emissaries & Abrahamic Hospitality", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Celestial emissaries in human guise arrive greeting Ibrahim with peace (Salam).\n"
        "- Without delay, Ibrahim serves elite hospitality: a roasted, fattened calf ('Ijlun Haneed).\n"
        "- Timeless standard of prophetic generosity: honoring strangers with the finest food."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. Untouched Roasted Meat & Dissipated Foreboding", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Observing their hands not touching the meat, Ibrahim felt inward apprehension.\n"
        "- Ancient custom: Refusing to eat signaled hostility; angels consume no mortal food.\n"
        "- Angels dissipate fear: 'Do not fear; we have been sent to the people of Lut.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. Sarah's Astonished Laughter & The Promised Heirs", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sarah laughed in astonishment (Dahikat); angels announce Isaac and Jacob.\n"
        "- Wondering at the biological paradox: 'Shall I bear while an old woman and my husband aged?'\n"
        "- The angelic response: 'Do you wonder at Allah's decree? Mercy and blessings upon you!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. Compassion of Ibrahim: Pleading on Behalf of Sodom", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Once fear passed, Ibrahim pleaded with angels on behalf of Sodom (Yujadiluna).\n"
        "- Praised by God: 'Indeed, Ibrahim was forbearing, tender-hearted, ever-turning (Muneeb).'\n"
        "- Divine closure: 'Turn away from this; your Lord's command has come; doom is irreversible.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: LUT'S ANGUISH, SEEKING THE PILLAR & RAIN OF SIJJEEL", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Yawmun 'Aseeb, Storming Mob, The Cry for Ruknin Shadeed & Sijjeel Mandood", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. Lut's Agony: Hadha Yawmun 'Aseeb (A Harrowing Day)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Angels arrive at Sodom as handsome youths; Lut is filled with suffocating distress.\n"
        "- Recognizing the uncontrollable predatory depravity of his town: 'This is a harrowing day!'\n"
        "- The moral agony of a righteous prophet surrounded by utter societal degeneration."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. The Degenerate Mob Storming the Threshold", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Corrupt men rush frantically to Lut's door; Lut appeals to lawful marriage structures.\n"
        "- Pleading desperately: 'Do not disgrace me before my guests! Is there no right-minded man?'\n"
        "- Illustrating the total extinction of reason in a populace surrendered to hedonism."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. The Cry for Unshakeable Support: Seeking Ruknin Shadeed", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Helpless cry: 'Would that I had power against you or could retreat to a strong support!'\n"
        "- Prophet Muhammad ﷺ: 'May Allah mercy Lut; he was seeking refuge in Allah Himself!'\n"
        "- Angels reveal identity: 'O Lut, we are emissaries of your Lord; they will never reach you!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. The City Overturned & Rain of Layered Baked Clay", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Lut departs at night; at dawn: 'We turned the city upside down (Ja'alna 'aaliyaha safilaha).'\n"
        "- Torrential rain of layered baked clay stones (Sijjeel Mandood), specifically marked.\n"
        "- Universal warning to all corrupt nations: 'And it is not far from the wrongdoers.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: ECONOMIC JUSTICE: SHU'AYB & THE RUINS OF TYRANNY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "ECONOMIC JUSTICE: SHU'AYB & THE RUINS OF TYRANNY",
        "Pillars 13 & 14: Market Ethics, Baqiyyatullah, The Reformer's Creed & Pharaoh Leading Host to Fire",
        "PLATE 07 : ECONOMIC JUSTICE"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: SHU'AYB'S FINANCIAL MANIFESTO & THE DIVINE REMAINDER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Forbidding Market Fraud, Baqiyyatullah & In Ureedu Illal-Islah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Commercial Integrity: Forbidding Fraud in the Scale", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Shu'ayb sent to Madyan: 'Worship Allah... and do not decrease the measure and scale.'\n"
        "- Linking monotheism directly to market justice and honest commercial weights.\n"
        "- Condemning predatory short-changing, fraud, and systematic financial exploitation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. The Divine Remainder (Baqiyyatullah): Sacred Contentment", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Principle of ethical wealth: 'The remainder left by Allah (Baqiyyatullah) is best for you.'\n"
        "- Modest halal profit blessed by God surpasses vast fortunes acquired through deception.\n"
        "- True wealth lies in spiritual Barakah and inner peace, not fraudulent accumulation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Secular Sneer: Does Your Prayer Dictate Our Wealth?", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Merchants sneered: 'Does your prayer command that we stop doing what we will with money?'\n"
        "- The archetypal secular capitalist defense: demanding total autonomy from sacred ethics.\n"
        "- Sarcastic mock: 'Indeed, you are the forbearing, discerning!' using virtue as an insult."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. The Prophetic Reformer: In Ureedu Illal-Islaha Ma-stata'tu", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Eternal reformer's motto: 'I only desire reform to the best of my ability.'\n"
        "- Total humility: 'And my success is not but through Allah; upon Him I rely.'\n"
        "- Genuine reformers commit to continuous ethical striving without self-righteousness."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: THE BLAST OF MADYAN & PHARAOH LEADING HOST TO FIRE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Extinction of Madyan, Blind Bureaucracy & Historical Ruins (Qaa'im wa Haseed)", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. The Shaking Blast of Madyan: Parallel Doom to Thamud", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rejection of commercial ethics brought the Blast (As-Sayhah); fallen lifeless in homes.\n"
        "- Extinguished commercial hubs: 'As though they had never dwelt there.'\n"
        "- The historical refrain: 'Away with Madyan just as Thamud was done away with!'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. Musa's Manifest Authority vs. Pharaoh's Bureaucracy", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Musa sent with clear signs and manifest authority to Pharaoh and his council.\n"
        "- Egyptian officials blindly followed Pharaoh, though 'his command was not discerning.'\n"
        "- Exposing the complicity of bureaucrats who execute tyrannical orders without conscience."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. Pharaoh Leading His Host Down to the Fire Like Cattle", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- On the Day of Standing, Pharaoh marches ahead, leading his people into the Fire.\n"
        "- Driven like a thirsty herd to water (Awrada-humun-Nar); wretched is the destination.\n"
        "- Cursed in this worldly life and cursed on the Day of Resurrection."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. The Ruins of History: Cities Standing and Mown Down", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Lessons of past cities: Some remaining standing (Qaa'im), others mown down (Haseed).\n"
        "- Absolute justice: 'We did not wrong them, but they wronged their own souls.'\n"
        "- False gods and secular systems availed nothing when the sovereign decree arrived."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE GRAYING MANDATE: ISTIQAMAH & THE COSMIC RETURN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE GRAYING MANDATE: ISTIQAMAH & THE COSMIC RETURN",
        "Pillars 15 & 16: The Severity of Fastaqim, Ban on Incline to Tyrants, Active Reformers & Sovereignty Over Unseen",
        "PLATE 08 : ISTIQAMAH & THE RETURN"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: THE COMMAND TO STAND UPRIGHT & BAN ON INCLINE TO TYRANTS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Fastaqim Kama Umirta, Wa La Tarkanoo & Prayers Erasing Minor Evils", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. The Verse that Grayed the Prophet: Fastaqim Kama Umirta", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The supreme imperative: 'Stand firm and upright as commanded, and do not transgress!'\n"
        "- Ibn 'Abbas: No verse across the Qur'an was revealed more severe than this command.\n"
        "- Forbidding both compromise (Tafreet) and extremism (Tughyan); razor-sharp rectitude."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. The Prohibition of Inward Incline to Oppressors", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Strict moral boundary: 'And do not incline toward those who do wrong (Wa La Tarkanoo)!'\n"
        "- Even slight sympathy, flattery, or justification of tyranny invites the Fire.\n"
        "- Severance of aid: 'You will have no protectors besides Allah, then not be helped.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. Cadence of Prayer: Good Deeds Erasing Minor Sins", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Daily spiritual rhythm: Establish prayer at ends of day and approaches of night.\n"
        "- Restorative power of worship: 'Indeed, good deeds erase and eradicate bad deeds.'\n"
        "- Confirmed in Sahih al-Bukhari: The five prayers cleanse hearts of unintentional slips."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. Law of Civilizational Preservation: Presence of Reformers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sociological law: 'Your Lord would never destroy cities while people are reformers.'\n"
        "- Muslihoon (active reformers) provide immunity; passive piety (Salihun) does not.\n"
        "- The civilizational duty: An active vanguard confronting corruption on earth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: DIVINE CADENCE OF PRAYER, REFORMERS & THE FINAL TRUST", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Purpose of Human Variance, Prophetic History as Heart Anchor & Total Tawakkul", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. Purpose of Human Variance & The Exceptions of Mercy", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine wisdom in human diversity: 'Had your Lord willed, He would have made man one.'\n"
        "- Divergent paths and choices are inherent to the existential examination of free will.\n"
        "- The singular eternal exception: 'Except those upon whom your Lord has granted mercy.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. Prophetic Histories as Unshakeable Anchors for Heart", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sacred history as medicine: 'All We narrate to you is to make firm your heart.'\n"
        "- Infusing the soul with verifiable truth (Al-Haqq), admonition, and spiritual strength.\n"
        "- Blueprints of steadfastness: Every previous struggle culminated in divine dawn."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. The Unseen Belongs Exclusively to the Master of Heavens", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cosmic sovereignty: 'To Allah belongs the unseen of the heavens and the earth.'\n"
        "- Every hidden motive and outcome is known: 'And to Him all matters return.'\n"
        "- Earthly power struggles and tyrannies are subordinate to the ultimate Divine Court."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. The Final Commission: Worship Him, Rely Upon Him & Return", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Final commission: 'Worship Him and rely upon Him (Fa'budhu wa Tawakkal 'Alayh).'\n"
        "- The twin pillars: Rigorous devotional obedience paired with unshakeable inner peace.\n"
        "- Parting reassurance: 'And your Lord is not unaware of what you do.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector PDF: {OUTPUT_PDF} (8 pages)")

    # Render PNG previews via pdftoppm
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "hud_page")]
    subprocess.run(cmd, check=True)
    print("Rendered 8 preview PNGs in 07_MINDMAP/previews/")

    # Copy preview PNGs to brain directory for artifact viewing
    for p in range(1, 9):
        src_png = os.path.join(PREVIEWS_DIR, f"hud_page-{p}.png")
        dst_png = os.path.join(brain_dir, f"hud_page-{p}.png")
        if os.path.exists(src_png):
            shutil.copy2(src_png, dst_png)
    print("Copied 8 preview PNGs to brain directory")

if __name__ == "__main__":
    build_hud_pdf()
