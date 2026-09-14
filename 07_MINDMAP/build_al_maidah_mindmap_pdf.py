#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Ma'idah Master Landscape Mindmap PDF CompilerStrict Standardization:
- Title: Surah Al-Ma'idah — Master Landscape Mindmap
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
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_MAIDAH_MASTER_MINDMAP.pdf")
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

def build_al_maidah_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-MA'IDAH", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 280, h - 32, 175, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 85, h - 26, font="F2", size=9, rgb=GOLD)

        # Title Sub-header
        pdf.text(title, 32, h - 68, font="F2", size=13.5, rgb=GOLD_LIGHT)
        badge_str = f"[{section_badge}]"
        badge_w = len(badge_str) * 6.1
        pdf.text(badge_str, (w - 32) - badge_w, h - 68, font="F2", size=10.5, rgb=GOLD)
        
        pdf.text(subtitle, 32, h - 84, font="F1", size=8.5, rgb=TEXT_MUTED)
        pdf.line(32, h - 92, w - 32, h - 92, stroke_rgb=BORDER_MUTED, line_width=0.7)

        # Bottom Footer Bar
        pdf.rect(0, 0, w, 28, fill_rgb=NAVY_CARD)
        pdf.line(0, 28, w, 28, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text("READ. REFLECT. RETURN.  *  SUNNI ISLAMIC SOURCE DISCIPLINE  *  MUTAWATIR TRANSMISSION", 32, 11, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("AUTHENTICATED EXEGESIS (TABARI * IBN KATHIR * QURTUBI * RAZI * AL-JASSAS)", w - 370, 11, font="F2", size=7.0, rgb=GOLD)

    # Column geometry
    c1_x = 32
    c2_x = 412
    c1_w = 348
    c2_w = 348
    c1_y = 48
    c1_h = 332

    # =========================================================================
    # PAGE 1: THE INVIOLABILITY OF COVENANTS & SACRED BOUNDARIES
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE INVIOLABILITY OF COVENANTS & SACRED BOUNDARIES",
        "Pillars 1 & 2: Awfoo bil-'Uqud, Completion of Deen, Ritual Taharah & Objective Justice Toward Antagonists",
        "PLATE 01 : COVENANTS & PURITY"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: AWFOO BIL-'UQUD & HALAL PROVISIONS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Supreme Contractual Mandate, Sacramental Boundaries & Wholesome Diet", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Awfoo bil-'Uqud: Supreme Contractual Mandate", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Uncompromising divine injunction to honor all covenants, pacts, and contracts.\n"
        "- Encompasses vertical oaths with Allah, civil treaties, and commercial agreements.\n"
        "- Foundational legal maxim: Binding force of contracts is the primary Islamic default."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Sanctity of Sacred Symbols (Sha'a'irullah)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Reverence commanded for sacred precincts, pilgrimage signs, and sacrificial offerings.\n"
        "- Severe prohibition against desecrating sacred months or hindering pilgrims.\n"
        "- Righteous cooperation mandate: Co-operate in Birr and Taqwa, never in sin."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Completion of Deen: Al-Yawma Akmaltu Lakum", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Revealed on the Day of Arafah during Farewell Pilgrimage sealing prophetic legislation.\n"
        "- Islam declared jurisprudentially complete and perfected; zero legislative innovation.\n"
        "- Divine self-sufficiency: Guidance is fully realized, leaving no moral ambiguity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Wholesome Provisions (At-Tayyibat) & Trained Hunt", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Decisive dietary boundary: Maytah, flowing blood, swine, and unslaughtered beasts forbidden.\n"
        "- Lawful utilization of trained hunting animals (Jawarih) mentioning Allah's name.\n"
        "- Food of the People of the Book made permissible, expanding civil interaction."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: PURIFICATION & OBJECTIVE EQUITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Bodily Sanctity, Hearing-Obeying & Justice Beyond Enmity", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("5. Structural Purification: Wudu, Ghusl & Tayammum", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Comprehensive hygiene protocol: Washing face, arms, wiping head, washing feet.\n"
        "- Divine facilitation of Tayammum using clean earth when water is absent.\n"
        "- Spiritual purpose revealed: Allah intends purity and completion of favor, not hardship."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("6. The Primordial Pledge: Sami'na wa Ata'na", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Remembering the divine favor and solemn pledge taken with the Messenger of Allah.\n"
        "- Unconditional submission: We have heard and we have obeyed in public and private.\n"
        "- Continuous Taqwa reminder: Allah is fully aware of all secrets within human chests."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("7. Objective Equity: I'diloo Huwa Aqrabu lit-Taqwa", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Persistent establishment of divine equity: Standing as truthful witnesses for Allah.\n"
        "- Transcendent legal maxim: Justice is the closest practical manifestation of Taqwa.\n"
        "- Impartiality enforced: Favoritism and subjective bias strictly excised from judgment."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("8. Enmity Transcended: Justice Toward Antagonists", c2_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- Hatred of a hostile people must never induce believers to commit legal injustice.\n"
        "- Enemies entitled to absolute fairness in judicial rulings, treaties, and testimony.\n"
        "- Supreme standard of Islamic statecraft: Ethical righteousness outranks resentment."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: HISTORICAL COVENANTS & THE SANCTITY OF LIFE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "HISTORICAL COVENANTS & THE SANCTITY OF LIFE",
        "Pillars 3 & 4: The Twelve Chieftains, Broken Pacts, Fratricide of Habil/Qabil & Cosmic Sanctity of Existence",
        "PLATE 02 : PACTS & SANCTITY OF LIFE"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE BROKEN PACTS OF BANI ISRA'IL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Twelve Chieftains, Hardened Hearts & Wilderness Cowardice", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. The Twelve Chieftains (Ithnay 'Ashara Naqeeba)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- God commissioned twelve leaders to govern the twelve tribes under divine covenant.\n"
        "- Covenant conditions: Establishing prayer, giving zakah, honoring messengers, loaning to God.\n"
        "- Historical archetype of collective leadership bound to divine accountability."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("10. Hardened Hearts & Textual Distortion (Yuharrifoon)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Breaking covenants resulted in divine curses and spiritual calcification of hearts.\n"
        "- Distortion of revelation: Displacing words from their rightful context and forgetting.\n"
        "- Treasonous betrayals encountered continuously, yet Prophetic pardon commanded."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("11. Noorun wa Kitabun Mubeen: Pathways of Peace", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A radiant light and clear Book sent to humanity from the Divine Throne.\n"
        "- Guiding whoever seeks His pleasure to Subul as-Salam (pathways of inner and outer peace).\n"
        "- Extracting consciousness from suffocating darkness into illuminated guidance."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("12. The Desert Wilderness: Cowardice Before Holy Land", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Command to enter Holy Land defied: 'Go, you and your Lord, and fight! We sit here!'\n"
        "- Two God-fearing men urge faith: 'Enter through the gate; when you enter, you will overcome.'\n"
        "- Forty-year wandering in wilderness (Fee al-ardi yateehoon) as consequence of rebellion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: HABIL, QABIL & THE INVIOLABILITY OF LIFE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sincerity vs Envy, First Fratricide & Cosmic Value of Soul", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("13. The First Fratricide: Sincerity vs Envy", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Two sons of Adam offer sacrifice; accepted from one, rejected from the other.\n"
        "- Universal truth revealed: Allah accepts solely from those who possess authentic Taqwa.\n"
        "- Envy triggers the murderous threat: 'I will surely kill you!' out of wounded pride."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("14. The Ethics of Non-Violence: Habil's Restraint", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Habil refuses reciprocal violence: 'If you stretch your hand to kill me, I shall not strike.'\n"
        "- Unshakable fear of the Lord of the worlds governs moral restraint under lethal assault.\n"
        "- Willingness to let the aggressor bear the double burden of original sin and fratricide."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("15. The Raven's Lesson: Awakening Remorse", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Qabil murders his brother, overwhelmed by his soul's impulse, becoming a total loser.\n"
        "- Allah sends a raven scratching the earth to teach the killer how to conceal the corpse.\n"
        "- The agony of late remorse: 'Woe to me! Am I unable to be like this raven?'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("16. Cosmic Sanctity of Life: Saving One is Saving All", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD)
    t = (
        "- Murdering an innocent soul is cosmically equivalent to murdering all of humanity.\n"
        "- Preserving a single life from destruction is cosmically equivalent to saving all mankind.\n"
        "- Absolute divine sanctity placed upon the human soul, forbidding vigilantism and slaughter."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: SOCIAL ORDER, PENAL JUSTICE & PURIFIED DEVOTION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "SOCIAL ORDER, PENAL JUSTICE & PURIFIED DEVOTION",
        "Pillars 5 & 6: Deterring Chaos (Hirabah), Seeking Al-Wasilah, Protecting Wealth & Judicial Autonomy",
        "PLATE 03 : PENAL JUSTICE & ORDER"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: HIRABAH, SARIQAH & SEEKING AL-WASILAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Deterring Armed Insurrection, Drawing Near via Obedience & Safeguarding Wealth", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Deterring Chaos: The Law of Hirabah (Terrorism)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Severe penalties for armed banditry, terrorizing highways, and spreading civil corruption.\n"
        "- Judicial discretion: Execution, crucifixion, cross-amputation, or exile based on crime.\n"
        "- Repentance door: Those who repent before apprehension are granted divine forgiveness."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("18. Seeking Al-Wasilah: Drawing Near via Obedience", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Command to attain Taqwa and seek Al-Wasilah (the means of near approach to Allah).\n"
        "- Sunni consensus: Wasilah is righteous deeds, worship, and obedience, not deceased intercessors.\n"
        "- Striving in His path (Jihad) as the highest active instrument of spiritual elevation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("19. Futility of Earthly Ransom on the Last Day", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Disbelievers possessing everything on earth and double its quantity cannot ransom themselves.\n"
        "- Eternal accountability: Worldly wealth cannot purchase immunity from divine retribution.\n"
        "- Enduring torment awaits those who traded eternal salvation for transient rebellion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("20. Protecting Communal Wealth: The Penalty of Theft", c1_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- Amputation of the hand decreed for male and female thieves as exemplary deterrence.\n"
        "- Juristic safeguards: Strict threshold (Nisab), secure custody (Hirz), and zero doubt.\n"
        "- Forgiveness and reform: Sincere repentance and restitution restore spiritual standing."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: JUDICIAL INTEGRITY & PROPHETIC EQUANIMITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Devourers of Suht, Discretionary Adjudication & Absolute Equity", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("21. Grief Over Willful Disbelief & Distorted Words", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prophetic heart consoled: Grieve not over those who hasten toward disbelief with their mouths.\n"
        "- Hearts that believe not: Inward duplicity contrasted with outward verbal declarations.\n"
        "- Distorting words out of place: Seeking corrupt rulings and abandoning divine statutes."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("22. Devourers of Illicit Wealth (Akkaluna lis-Suht)", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Severe rebuke of corrupt jurists: Addicted to hearing falsehood and consuming illicit bribes.\n"
        "- Spiritual pollution: Bribery, usury, and corrupt fees blind the judicial conscience.\n"
        "- Purification of magistrates: Justice cannot be rendered through hands stained by extortion."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("23. Judicial Autonomy: Judging Between Disbelievers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prophet granted jurisdictional discretion: Turn away from corrupt litigants or judge between them.\n"
        "- Immunity from harm: If you turn away, they cannot harm you in the slightest.\n"
        "- Sovereign independence of the Islamic judiciary in handling external minority disputes."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("24. Equanimity in Judgment: Allah Loves the Equitable", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- If judgment is rendered, it must be executed with unbending equity (bil-Qist).\n"
        "- Divine love confirmed: 'Indeed, Allah loves those who act equitably.'\n"
        "- Rebuking bad-faith litigation: Coming for arbitration while possessing their own revealed text."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: PROGRESSION OF SCRIPTURE & THE SUPREME GUARDIAN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE PROGRESSION OF SCRIPTURE & THE SUPREME GUARDIAN",
        "Pillars 7 & 8: The Torah & Injeel, The Qur'an as Muhaymin, Shir'atan wa Minhaja & Rejection of Jahiliyyah",
        "PLATE 04 : THE CRITERION OF SCRIPTURE"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE TORAH & INJEEL: GUIDANCE & LIGHT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Authentic Revelation, Rabbinic Guardianship & Retributive Equity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. The Torah Revealed: Guidance & Illuminated Law", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Affirming original Torah: Sent down by Allah containing guidance, illumination, and law.\n"
        "- Prophets who submitted governed the Jewish community through its divine statutes.\n"
        "- Whoever does not judge by what Allah has revealed—such are indeed the true disbelievers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("26. Rabbis, Scholars & Inviolability of the Text", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Religious leaders and scholars entrusted with safeguarding the written scripture.\n"
        "- Fear not mankind, fear Allah alone; never barter divine revelation for fleeting worldly price.\n"
        "- Whoever judges not by Allah's revelation—such are indeed the unjust wrongdoers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("27. Retributive Law: An-Nafsa bin-Nafs (Life for Life)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prescribed equitable retribution: Life for life, eye for eye, tooth for tooth, equal wounds.\n"
        "- Mercy and charity elevated: Whoever foregoes retribution as charity gains divine expiation.\n"
        "- Balancing rigorous civil deterrence with the spiritual virtue of voluntary pardon."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("28. Isa & The Injeel: Confirming and Softening", c1_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- Isa sent in the footsteps of previous prophets, confirming the original Torah before him.\n"
        "- The Gospel revealed containing guidance, radiant light, and admonition for the righteous.\n"
        "- Whoever judges not by what Allah has revealed therein—such are the rebellious transgressors."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: THE QUR'AN AS MUHAYMIN: GUARDIAN & STANDARD", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Master Criterion, Diverse Dispensations, Moral Race & Truth", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("29. Muhayminan 'Alayh: Master Criterion of Truth", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Qur'an revealed in truth, confirming previous scriptures and standing as Muhaymin.\n"
        "- Role of Muhaymin: Incorruptible guardian, witness, corrector, and ultimate ruling criterion.\n"
        "- Judge between them exclusively by what Allah revealed; follow not arbitrary desires."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("30. Shir'atan wa Minhaja: Diverse Laws, One Creed", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- To each civilization Allah prescribed a distinct legislative code (Shir'ah) and open path.\n"
        "- Universal Tawhid creed is eternal; historical civil laws adapted to eras and capacities.\n"
        "- Diversity ordained to test human fidelity in applying divine commandments across ages."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("31. Fastabiqul-Khayrat: The Dynamic Race in Virtue", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Transcending sectarian paralysis: Compete vigorously with one another in righteous deeds.\n"
        "- Ultimate return is unto Allah alone, where He will resolve all historical disputes.\n"
        "- Action-oriented spirituality: Energy channeled into moral excellence rather than futile debate."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("32. Hukm al-Jahiliyyah: Divine Law vs Pagan Custom", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Stern rhetorical question: 'Do they then seek the judgment of pagan ignorance (Jahiliyyah)?'\n"
        "- Unrivaled excellence of divine law: 'And who is better than Allah in judgment for the certain?'\n"
        "- Firm warning against being lured away from even a fraction of what Allah has sent down."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: THE GEOMETRY OF ALLIANCE & DIVINE AFFECTION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE GEOMETRY OF ALLIANCE & DIVINE AFFECTION",
        "Pillars 9 & 10: Wilayah Demarcation, The Loving Vanguard (Yuhibbuhum wa Yuhibboonah) & Hands of Allah",
        "PLATE 05 : ALLIANCE & DIVINE LOVE"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: WILAYAH & THE LOVING VANGUARD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Political Allegiance, Sickness of Opportunism & The Unbreakable Generation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. Dismantling Compromising Alliances of Disloyalty", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Warning against seeking patronal alliances with hostile factions against the believers.\n"
        "- Self-sufficient community: Subordinating communal sovereignty undermines ideological autonomy.\n"
        "- Whoever allies with hostile factions compromises their internal belonging to the Ummah."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("34. Sickness of Heart: Panicking Over Changing Winds", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Those with diseased hearts hasten to make compromises: 'We fear a turn of fortune.'\n"
        "- Allah promises decisive victory or a direct decree, exposing opportunists in humiliation.\n"
        "- Hypocritical oaths exposed: Believers will wonder: 'Are these the ones who swore solemn oaths?'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("35. The Loving Vanguard: Yuhibbuhum wa Yuhibboonah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If a generation apostatizes, Allah will replace them with a people He loves and who love Him.\n"
        "- Four hallmarks: Gentle to believers, firm to deniers, striving in God's path, fearless of blame.\n"
        "- Immunity to peer pressure: Unshakable adherence to truth without fearing social reproach."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("36. True Alliance: Allah, His Messenger & Believers", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD)
    t = (
        "- True Wilayah defined: Exclusively Allah, His Messenger, and the steadfast believers.\n"
        "- Believers characterized by establishing prayer and paying zakah while bowing in humility.\n"
        "- The triumphant party: 'And whoever allies with Allah and His Messenger—the party of Allah wins.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: DEFENDING FAITH & THE HANDS OF ALLAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Rebuking Mockery, Refuting Slander (Bal Yadahu) & Conveyance", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("37. Rebuking Those Who Mock Prayer and Religion", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prohibition of allying with those who take religion as mockery, entertainment, and play.\n"
        "- The call to prayer ridiculed: When the Adhan is called, they treat it with derision and jest.\n"
        "- Cognitive diagnosis: Mockery of divine worship stems from lack of intellect and understanding."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("38. Refuting the Slander: Bal Yadahu Mabsutatani", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Rebutting the blasphemous statement: 'The Hand of Allah is chained and stingy.'\n"
        "- Divine affirmation: 'Nay, both His hands are widely outstretched; He spends as He wills.'\n"
        "- Sunni orthodoxy: Affirming divine attributes without anthropomorphism (Tashbih) or denial."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("39. Enmity and Malice Cast Until the Day of Rising", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Seditious factions who kindle fires of war find their fires systematically extinguished by God.\n"
        "- Divine retribution: Sowing enmity and malice among warmongers until Resurrection Day.\n"
        "- Corrupt striving: Rebuking those who tirelessly strive to spread corruption across the earth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("40. Balligh: The Absolute Mandate of Conveyance", c2_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- Sovereign command: 'O Messenger, convey all that has been revealed to you from your Lord.'\n"
        "- Solemn consequence: Failure to convey a single verse equates to failing the entire mission.\n"
        "- Guaranteed divine protection: 'And Allah will defend you from the people,' dismissing guards."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: EXPOSING THEOLOGICAL EXCESS & THE PROPHETIC CYCLE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "EXPOSING THEOLOGICAL EXCESS & THE PROPHETIC CYCLE",
        "Pillars 11 & 12: Refuting Christological Deification, Kana Ya'kulani at-Ta'am, Curse on Silence & Monks' Tears",
        "PLATE 06 : THEOLOGY & REFORM"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: DISMANTLING CHRISTOLOGICAL DEIFICATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Rebuttal of Trinity, Mortality of Isa & Maryam & Severe Shirk Warning", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. The Universal Standard for Past Peoples of the Book", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Righteous among Jews, Christians, and Sabeans who truly believed and acted righteously have no fear.\n"
        "- Universal principle: Divine justice judges past communities by their authentic obedience.\n"
        "- Prophetic mission reaffirmed: Clarifying truths long obscured by sectarian additions."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("42. Refuting the Deification of the Messiah Isa", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Categorical disbelief: Declaring that Allah is the Messiah, the son of Maryam.\n"
        "- Isa's own words cited: 'O Children of Israel, worship Allah, my Lord and your Lord!'\n"
        "- The penalty of Shirk: Whosoever associates partners with Allah is forbidden Paradise."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("43. Kana Ya'kulani at-Ta'am: Mortality & Need", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Messiah was nothing but a Messenger; before him passed many noble Messengers.\n"
        "- Maryam praised as a woman of profound truth (Siddiqah), devoid of divine claims.\n"
        "- Irrefutable logical proof: 'They both used to eat food!'—contingent beings require nourishment."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("44. Rebuttal of the Trinity: Innahu man Yushrik", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Disbelieved are those who say: 'Allah is the third of three.' There is no deity but One God.\n"
        "- Stern warning against persisting: A painful torment awaits those who persist in blasphemy.\n"
        "- Invitation to repentance: Will they not turn to Allah in sincere repentance and seek forgiveness?"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: THE CURSE OF SILENCE & MONKS' TEARS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Condemnation of Passive Scholars, Kanoo la Yatanahawna & Sincere Faith", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("45. The Curse of Dawud & Isa: Leaving Amr bil-Ma'roof", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Disbelievers among Bani Isra'il cursed by the tongues of Dawud and Isa ibn Maryam.\n"
        "- Cause of the curse: Persistent transgression, rebellion, and moral indifference.\n"
        "- Historical lesson: Sanctity of prophetic lineage cannot shield a corrupt society from wrath."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("46. The Corrosive Silence: Kanoo la Yatanahawna", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Core societal crime: 'They did not prevent one another from the wrong actions they committed.'\n"
        "- Collapse of social immune system: Tolerating public injustice destroys civil morality.\n"
        "- Mandatory activism: Enjoining good and forbidding wrong is essential to preserve the Ummah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("47. Hearts Overflowing With Tears: Righteous Monks", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Nearest in affection to believers are those who say: 'We are Christians.'\n"
        "- Character of sincere priests and monks: Devoid of arrogance and dedicated to quiet worship.\n"
        "- Deep emotional response: When they hear revelation, their eyes overflow with tears of recognition."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("48. The Prayer of the Truthful: Fa-ktubna Ma'ash-Shahideen", c2_x + 12, y_c, font="F2", size=8, rgb=PURPLE)
    t = (
        "- Their heartfelt plea: 'Our Lord, we have believed, so register us among the truthful witnesses!'\n"
        "- Yearning for divine acceptance: 'Why should we not believe in Allah and the truth that has come?'\n"
        "- Reward granted: Gardens beneath which rivers flow, abiding therein as the reward of doers of good."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: SOCIAL ETHICS, PURITY OF SANCTUARY & OATHS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "SOCIAL ETHICS, PURITY OF SANCTUARY & OATHS",
        "Pillars 13 & 14: Decisive Prohibition of Khamr/Maysir, Expiation of Oaths & Sanctity of Ihram/Ka'bah",
        "PLATE 07 : SANCTITY & CIVIC PURITY"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: SANCTITY OF OATHS & DECISIVE PROHIBITION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Abolition of False Asceticism, Kaffarat al-Yameen & Eradication of Intoxicants", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Do Not Forbid Good Things Allah Made Lawful", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rebuking self-imposed asceticism: Forbid not wholesome provisions (Tayyibat) Allah made lawful.\n"
        "- Balance of Islam: Rejecting monastic extremes; partake of lawful sustenance with gratitude.\n"
        "- Prohibition against transgressing boundaries: Allah loves not those who exceed limits."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("50. The Expiation of Oaths: Kaffarat al-Yameen", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Allah does not hold you for unintentional oaths, but holds you for deliberate vows.\n"
        "- Structured expiation: Feeding ten destitute people, clothing them, or freeing a slave.\n"
        "- Alternative fast: Whoever cannot afford the expiation must observe three consecutive fasts."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("51. Khamr & Maysir: The Rijs of Shaitan Banished", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Final categorical prohibition: Intoxicants, gambling, altars, and divining arrows declared Rijs.\n"
        "- Uncompromising command: 'Fajtaneebooh' (Turn completely aside and avoid it) to achieve success.\n"
        "- Historical obedience: Companions emptied all wine vessels into the streets upon revelation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("52. Sow Enmity & Block Remembrance: Shaitan's Goal", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Psychological strategy of Satan: Inciting mutual hatred and malice through intoxicants and gambling.\n"
        "- Spiritual destruction: Creating cognitive numbness that distracts from Dhikr and prayer.\n"
        "- The decisive query: 'Will you not then desist?' Believers responded: 'We have desisted!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: THE SANCTITY OF IHRAM & THE KA'BAH", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Hunting Test, Sacred Ka'bah as Anchor & Eradicating Superstition", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("53. The Test of Faith: Game Within Reach of Hands", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah tests the pilgrims by sending wild game easily accessible to their hands and spears.\n"
        "- Divine purpose: To make manifest who fears Allah in the secret, unseen depths of their heart.\n"
        "- Stern consequence: Whoever transgresses after this warning faces a severe and painful penalty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("54. The Sacred Sanctity: Hunting Forbidden in Ihram", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Explicit prohibition: Kill not game while you are in the sacred state of consecration (Ihram).\n"
        "- Penal expiation: Compensation in an equivalent domestic beast judged by two just arbiters.\n"
        "- Water game permitted: Catching marine game and sea food made lawful for pilgrims and travelers."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("55. The Ka'bah: An Enduring Anchor for Humanity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah established the Ka'bah, the Sacred House, as an enduring sanctuary and pivot for mankind.\n"
        "- Sanctity extended: Sacred months, sacrificial offerings, and garlands preserved for civic stability.\n"
        "- Cosmic proof: Demonstrating that Allah knows everything in the heavens and the earth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("56. Superstitions Abolished: Bahirah, Sa'ibah & Wasilah", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD)
    t = (
        "- Abolition of pagan animal dedications: Bahirah, Sa'ibah, Wasilah, and Ham fabricated as divine law.\n"
        "- Rebuttal of traditionalism: Disbelievers cling to ancestors' ways despite ancestral ignorance.\n"
        "- Personal accountability: Guard your own souls; when you are guided, the astray cannot harm you."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: ESCHATOLOGICAL CROSS-EXAMINATION & SOVEREIGN SEAL
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE ESCHATOLOGICAL CROSS-EXAMINATION & SOVEREIGN SEAL",
        "Pillars 15 & 16: Miracles of Isa, The Heavenly Table (Al-Ma'idah), Subhanaka Vindication & Cosmic Dominion",
        "PLATE 08 : THE ESCHATOLOGICAL SEAL"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: THE MIRACLES OF ISA & HEAVENLY TABLE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Wills on Travel, Miracles by Divine Leave & Celestial Repast", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. Integrity of Wills: Faithful Testimony on Travel", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Judicial protocol: Two just witnesses required when executing wills during terminal illness or travel.\n"
        "- Solemn oath taken after prayer: Swearing by Allah that testimony is not sold for worldly advantage.\n"
        "- Preventing perjury: If deception is discovered, closer heirs swear to rectify false claims."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("58. The Miracles Bi-Idhnillah: Clay, Healing & Life", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Favors upon Isa recalled: Strengthened with Holy Spirit; speaking in cradle and maturity.\n"
        "- Miracles executed exclusively by divine leave: Fashioning birds from clay, healing blind and leper.\n"
        "- Raising the dead by His leave, and divine protection when disbelievers sought his execution."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("59. The Disciples' Request: The Heavenly Table", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Hawariyyun petition: 'Can your Lord send down upon us a table spread with food from heaven?'\n"
        "- Isa's admonition: 'Fear Allah, if you are truly believers!' guarding theological propriety.\n"
        "- Their sincere justification: We desire to eat, reassure our hearts, and witness the truth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("60. A Sign for All Generations: Feast of Gratitude", c1_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- Isa's profound prayer: 'O Allah, our Lord, send down a table from heaven to be an Eid for us.'\n"
        "- Divine response: 'I will send it down; but whoever disbelieves after, I will punish uniquely.'\n"
        "- The Heavenly Table stands as a perpetual sign of divine sustenance and covenant gravity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: THE GREAT INQUIRY & SOVEREIGN EXALTATION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Isa's Impeccable Defense, In Tu'adhdhibhum & Universal Kingship", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("61. The Great Eschatological Inquiry: Did You Say It?", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Solemn trial on Judgment Day: 'O Isa son of Maryam, did you tell people to take you as a deity?'\n"
        "- Cosmic confrontation before all creation: Exposing the fabrication of trinitarian worship.\n"
        "- The pristine monotheistic witness: Demarcating authentic prophetic teaching from human heresy."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("62. Subhanaka: Isa's Impeccable Theological Defense", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Sublime opening: 'Subhanak! Exalted are You! Never could I say what I had no right to say.'\n"
        "- Divine omniscience invoked: 'If I had said it, You would know it; You know all unseen.'\n"
        "- Fidelity confirmed: 'I said nothing to them except what You commanded: Worship Allah alone.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("63. The Sovereign Word: In Tu'adhdhibhum", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The supreme surrender: 'If You punish them, they are Your servants; if You forgive them, You are Wise.'\n"
        "- Attributes of majesty: Affirming Al-'Azeez (The Mighty) and Al-Hakeem (The All-Wise).\n"
        "- Prophetic empathy: The Prophet Muhammad wept throughout the night repeating this single verse."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("64. Lillahil-Mulk: Sovereign Dominion Over All Existence", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- The day when truthful hearts benefit from their truthfulness; rewarded with eternal gardens.\n"
        "- Divine pleasure achieved: 'Radhiyallahu 'anhum wa radhoo 'anh'—the supreme triumph (Al-Fawz).\n"
        "- Cosmic seal of the Surah: To Allah belongs all dominion of heavens and earth, competent over all."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    pdf.save(OUTPUT_PDF)
    print(f"Successfully generated Surah Al-Ma'idah Master Mindmap PDF: {OUTPUT_PDF}")

    # Generate PNG page previews using pdftoppm
    print("Generating PNG previews...")
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "al_maidah_page")]
    subprocess.run(cmd, check=True)
    print("PNG previews generated in:", PREVIEWS_DIR)

    # Copy previews to brain directory
    print("Copying previews to brain directory...")
    for f in os.listdir(PREVIEWS_DIR):
        if f.startswith("al_maidah_page") and f.endswith(".png"):
            src = os.path.join(PREVIEWS_DIR, f)
            dst = os.path.join(brain_dir, f)
            shutil.copy2(src, dst)
            print(f"  Copied {f} to brain directory.")

if __name__ == "__main__":
    build_al_maidah_pdf()
