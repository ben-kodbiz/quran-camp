#!/usr/bin/env python3
"""
Huurs Studio - Surah At-Tawbah Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AT_TAWBAH_MASTER_MINDMAP.pdf")
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

def build_at_tawbah_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AT-TAWBAH", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PAGE 1: THE DIVINE ULTIMATUM & THE SACRED SANCTUARY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE DIVINE ULTIMATUM & THE SACRED SANCTUARY",
        "Pillars 1 & 2: Disavowal of Polytheism, Four Months Respite, Treaty Terms & Asylum for Seekers of Truth",
        "PLATE 01 : ULTIMATUM & TREATIES"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: DISAVOWAL OF POLYTHEISM & THE GRAND PROCLAMATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Bara'ah, The Four-Month Respite & Proclamation on Yawm al-Hajj al-Akbar", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Omission of the Basmalah & The Sword of Truth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Revealed without Basmalah; Ali: Basmalah is security (Aman), while Bara'ah revokes false peace.\n"
        "- A stern declaration demanding absolute moral accountability and terminating pagan deceit.\n"
        "- Dividing the insincere opportunists from those of steadfast monotheistic faith."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. Proclamation on Yawm al-Hajj al-Akbar", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ali dispatched to Mina on the Prophet's camel to announce the decree to assembled tribes.\n"
        "- No polytheist shall perform pilgrimage after this year, nor circumambulate naked.\n"
        "- Restoring the pristine Abrahamic purity of the Ka'bah as the monotheistic sanctuary."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. The Four-Month Respite (Faseehoo)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A grace period granted to treaty-violators to travel freely and contemplate their state.\n"
        "- Proclaiming that the deniers can never frustrate the divine will or escape accountability.\n"
        "- A balanced transition combining unyielding truth with generous temporal reprieve."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. Asylum for Seekers of Truth (Istajaraka)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If an enemy combatant seeks protection, grant him asylum immediately without condition.\n"
        "- Allow him to hear the recited Word of Allah so truth becomes clear without coercion.\n"
        "- Safely escort him to his place of absolute security if he chooses not to embrace faith."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: TREATY ETHICS & SANCTITY OF COVENANTS", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Honoring Unbroken Pacts, Perfidy Rebuked & Maintenance of Sanctuaries", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. Honoring Treaties to Their Appointed Term", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Tribes who never breached covenants nor aided enemies are strictly protected.\n"
        "- Fulfill all agreements until their designated expiration; Allah loves the righteous.\n"
        "- Islamic law holds sworn covenants sacred even amidst active international tensions."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. The Elapse of the Sacred Months (Al-Ashhur al-Hurum)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Once the sacred months elapse, confront persistent aggressors who broke sworn pacts.\n"
        "- Yet if they sincerely repent, establish regular prayer, and give Zakah, clear their way.\n"
        "- Affirming that repentance restores full fraternal equality within the community."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. Treacherous Disregard of Kinship & Oaths", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Polytheistic chieftains observe neither kinship ties nor sworn treaties when dominant.\n"
        "- They flatter with sweet words while their hearts harbor deep animosity and treachery.\n"
        "- Exposing the hypocrisy of those who trade away divine signs for petty worldly advantage."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. The True Maintainers of the Sacred Sanctuaries", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- It is not for idolaters to maintain the Masajid while witnessing against their own disbelief.\n"
        "- True custodianship belongs exclusively to those who believe, pray, give Zakah, and fear Allah alone.\n"
        "- Mere blood lineage or providing water to pilgrims cannot equal true faith and spiritual striving."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: FALSE SECURITY, THE LESSON OF HUNAYN & THE CAVE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "FALSE SECURITY, THE LESSON OF HUNAYN & THE CAVE",
        "Pillars 3 & 4: Battle of Hunayn, The Pitfall of Numbers, Descent of Sakinah & The Cave of Thawr",
        "PLATE 02 : HUNAYN & THE CAVE"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: THE CRUCIBLE OF HUNAYN & VANITY OF NUMBERS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Battle of Hunayn, Illusion of Abundance & Descent of Divine Sakinah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. The Illusion of Abundance ('Ajabatkum Kathratukum)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- At Hunayn, 12,000 Muslim warriors took pride in their unprecedented military size.\n"
        "- Hawazin's archers ambushed the columns, shattering overconfident human pride.\n"
        "- Proving that military mass is worthless without divine assistance and humble hearts."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. The Constriction of the Vast Earth (Daqat 'Alaykumul-Ard)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The battlefield felt suffocatingly narrow despite its vast geographical expanse.\n"
        "- Believers retreated in disorder, testing the resilience and sincerity of the ranks.\n"
        "- Squeezing the soul until it recognizes that all strength belongs solely to Allah."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. Descent of Divine Tranquility (As-Sakinah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah sent down tranquil composure upon His Messenger and the steadfast believers.\n"
        "- Reinforced by invisible angelic legions that turned the tide of conflict.\n"
        "- Transforming chaotic rout into decisive victory through divine intervention."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. Barring Polytheism from the Sacred Sanctuary", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Idolatrous beliefs are spiritually impure; let them not approach the Ka'bah after this year.\n"
        "- Reassuring believers who feared economic loss: Allah will enrich you from His bounty.\n"
        "- Material sustenance is guaranteed by the Creator; religious purity must never be compromised."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE CAVE OF THAWR & PROPHETIC RELIANCE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Thani Ithnayn, 'Do Not Grieve' & The Divine Inscription of History", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. If You Do Not Aid Him, Allah Has Already Aided Him", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Reminding the community that the Prophet's mission does not rely on mortal armies.\n"
        "- Allah protected him when disbelievers drove him out with neither troops nor weapons.\n"
        "- The divine decree operates independently of human numbers and worldly calculations."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. The Solitary Two in the Cave (Thani Ithnayn)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Prophet and Abu Bakr sheltered in the dark cave of Thawr, surrounded by trackers.\n"
        "- Abu Bakr wept out of concern: 'If one of them looks under his feet, he will see us.'\n"
        "- The sublime prophetic response: 'What do you think of two when Allah is their Third?'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. 'Do Not Grieve; Indeed Allah is with Us'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- La Tahzan inna Allaha Ma'ana: The eternal formula of absolute reliance (Tawakkul).\n"
        "- Divine Sakinah descended upon him, backed by unseen heavenly legions.\n"
        "- True peace is granted during the height of the trial, not merely after its resolution."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. The Word of Disbelief Made the Lowest", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah cast the plots and proclamations of the deniers into the lowest abyss.\n"
        "- The Word of Allah remains supreme, exalted, and victoriously transcendent.\n"
        "- He is the All-Mighty, the All-Wise, governing history with flawless justice."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE CRUCIBLE OF TABUK & UNMASKING HYPOCRISY
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE CRUCIBLE OF TABUK & UNMASKING HYPOCRISY",
        "Pillars 5 & 6: The Call to March, Clinging to the Earth, Hypocrisy Unmasked & Mockery Exposed",
        "PLATE 03 : TABUK & HYPOCRISY"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: THE CALL TO MARCH & WORLDLY HESITATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Infiroo Khifafan wa Thiqaalan, Love of Ease & The Divine Reprimand", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Clinging Heavily to the Earth (Ith-thaqaltum)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Why is it that when told to march in Allah's cause, you cling heavily to the earth?'\n"
        "- Testing attachment: Preferring transient worldly shade over eternal felicity in the Hereafter.\n"
        "- The pleasure of this mortal existence is infinitesimally brief compared to the next life."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. March Forth Light & Heavy (Infiroo Khifafan wa Thiqaalan)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Mobilize regardless of worldly condition: young or old, wealthy or poor, busy or free.\n"
        "- Strive with your wealth and lives; that is far better for you if you only knew.\n"
        "- Overcoming comfort and convenience to answer the call of divine truth."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. The Pretexts of the Insincere (Law Kana 'Aradan Qareeban)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Had it been immediate worldly profit and an easy journey, they would have followed.\n"
        "- But the long, scorching distance toward the Byzantine frontier seemed too far.\n"
        "- Swearing false oaths: 'Had we been able, we would have marched with you!'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Divine Clemency & The Litmus Test ('Afallahu 'Ank)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'May Allah pardon you! Why did you grant them leave before the truthful were distinguished?'\n"
        "- A loving divine inquiry highlighting the Prophet's compassionate nature.\n"
        "- The crucible of hardship clarifies the sincere from the fabricators of false excuses."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE ANATOMY OF HYPOCRISY (NIFAQ)", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Mockery of Revelation, False Oaths & The Sickness of the Inward", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. Those Who Seek Exemption are Those Who Doubt", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sincere believers never request exemption from striving with their wealth and lives.\n"
        "- Only those whose hearts harbor deep doubt and hesitation ask to be excused.\n"
        "- Lingering in uncertainty, their spiritual paralysis prevents righteous action."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. Subversive Rejoicing at Calamity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If good fortune touches the believers, it grieves the hypocrites to their core.\n"
        "- If difficulty strikes, they gloat: 'We took our precaution beforehand!' and turn away.\n"
        "- Sincere believers reply: 'Nothing will afflict us except what Allah has decreed for us.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. Mockery Under the Mask of Jest (Innama Kunna Nal'ab)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Exposed mocking the Prophet and Companions, they claim: 'We were only jesting!'\n"
        "- Proclaim: 'Was it at Allah, His signs, and His Messenger you were mocking?'\n"
        "- 'Make no excuses; you have disbelieved after your belief!' Mockery dissolves faith."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. Invalidation of Reluctant Charity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Their financial donations are utterly rejected and unprofitable in the sight of God.\n"
        "- Because they come to prayer only sluggishly and spend in charity only with resentment.\n"
        "- Exterior acts of worship are void when disconnected from inward sincerity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE SOCIAL ARCHITECTURE OF HYPOCRISY VS TRUE FAITH
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE SOCIAL ARCHITECTURE OF HYPOCRISY VS TRUE FAITH",
        "Pillars 7 & 8: Networks of Nifaq, Forgetting God, Mutual Alliance of Believers & The 8 Recipients of Zakah",
        "PLATE 04 : SOCIAL ARCHITECTURE & ZAKAH"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE NETWORK OF HYPOCRISY & FORGETTING GOD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Munafiqoon Enjoin Evil, Withhold Hands & Receive the Divine Curse", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. Homogeneity of the Hypocrites", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The hypocrite men and hypocrite women are of one another: unified in spiritual pathology.\n"
        "- They enjoin what is wrong, forbid what is right, and close their fists in stinginess.\n"
        "- A toxic collective network operating to undermine the moral health of society."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. They Forgot Allah, So He Forgot Them (Nasu Allaha)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Deliberately ignoring divine guidance resulted in divine abandonment.\n"
        "- The hypocrites are the truly defiant transgressors, alienated from spiritual peace.\n"
        "- Stripped of divine light, their souls wander in existential darkness."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. The Ruined Civilizations of the Past", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Reminding them of prior nations: 'Ad, Thamud, people of Ibrahim, and Madyan.\n"
        "- They were mightier in strength and possessed greater wealth and children, yet were destroyed.\n"
        "- They enjoyed their fleeting earthly portion, then vanished into historical disgrace."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. The Eternal Fire of Jahannam", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah has promised the hypocrites and disbelievers the blazing fire of Hell eternally.\n"
        "- An inescapable consequence matching the duplicity and betrayal of their earthly lives.\n"
        "- For them is an enduring torment and the total revocation of divine mercy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: THE BELIEVING COMMUNITY & THE EIGHT RECIPIENTS OF ZAKAH", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Awliya of One Another, Enjoining Right, Gardens of Eden & Zakah Distribution", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. Believers as Mutual Allies (Awliya)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believing men and believing women are protective allies and guardians of one another.\n"
        "- They enjoin all that is virtuous, forbid vice, establish prayer, and pay Zakah.\n"
        "- Bound by transcendent love and divine purpose, they obey Allah and His Messenger."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. Divine Mercy & Gardens of Perpetual Bliss ('Adn)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Upon this sincere community Allah will shower His boundless, transformational mercy.\n"
        "- Promised gardens beneath which rivers flow and glorious dwellings in Gardens of Eden.\n"
        "- Eternal peace prepared for souls that remained loyal to their divine pledge."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. Ridwanullah: The Supreme Achievement", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Wa Ridwanun min Allahi Akbar: The good pleasure of Allah is greater than all Paradise.\n"
        "- Beyond rivers, palaces, and garments, the highest joy is divine acceptance.\n"
        "- That is the supreme triumph, where the soul rests eternally in the Lord's love."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. The Eight Exclusive Recipients of Zakah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Innamas-Sadaqatu: Zakah is divinely allocated exclusively across eight categories.\n"
        "- The poor (Fuqara), needy (Masakeen), administrators, reconciled hearts, freeing captives.\n"
        "- The debt-burdened, in the cause of Allah, and the stranded wayfarer; an ordained decree."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: THE SINS OF MISERLINESS, TAUNTING CHARITY & FALSE SANCTUARIES
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE SINS OF MISERLINESS, TAUNTING CHARITY & FALSE SANCTUARIES",
        "Pillars 9 & 10: Broken Pledges of Wealth, Taunting the Poor & The Subversion of Masjid ad-Dirar",
        "PLATE 05 : WEALTH & FALSE SANCTUARIES"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: THE BROKEN PLEDGES OF THE MISERLY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Pledging to Spend, Backtracking in Greed & Inward Hypocrisy Seeded", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. The False Vow: 'If He Enriches Us, We Will Give Charity'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who swore solemnly that if Allah granted them wealth, they would be righteous spenders.\n"
        "- Yet when divine bounty enriched them, they grew stingy and turned away defiantly.\n"
        "- Worldly abundance exposing the hollow deceit of their pre-wealth declarations."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. Hypocrisy Sealed in the Heart (Fa A'qabahum Nifaqan)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Because they broke their promise to Allah and lied, hypocrisy was sealed in their hearts.\n"
        "- A permanent spiritual disease festering within until the Day they meet their Creator.\n"
        "- Warning that broken vows to God alter the inward spiritual reality irrevocably."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. Mocking Generous Donors & Sneering at the Poor", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hypocrites sneer at wealthy believers who give large donations, accusing them of show.\n"
        "- And when the poor donate their humble day's labor, the hypocrites mock their meager gift.\n"
        "- Allah mocks their arrogance, and for them is an excruciating, humiliating punishment."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. Banning Funeral Prayer for the Arch-Hypocrite", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Commanded never to pray the funeral prayer over deceased hypocrites who died in defiance.\n"
        "- Nor stand beside their graves; their outward claims cannot sanitize inward rebellion.\n"
        "- Demarcating the ultimate boundary between sincere faith and obstinate duplicity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: THE MOSQUE OF SUBVERSION (MASJID AD-DIRAR)", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Counterfeit Sanctuaries, Sowing Discord & The Mosque Founded on Taqwa", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. The Counterfeit Mosque of Subversion", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Built by hypocrites intending harm, disbelief, and division among the Muslim ranks.\n"
        "- Serving as an intelligence outpost for hostile forces plotting against Islam.\n"
        "- Cloaking treacherous sectarian sabotage in the guise of religious devotion."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. False Oaths of Benevolent Intent", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The conspirators swear solemnly: 'We intended nothing but the absolute best and charity!'\n"
        "- Yet Allah testifies that they are unvarnished, deceitful liars.\n"
        "- Exposing that religious structures built on malicious intent are abhorrent to God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. 'Never Stand to Pray Within It!' (La Taqum Feehi Abada)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Prophet is commanded never to enter or pray within that subversive structure.\n"
        "- Its foundations are built upon the crumbling brink of a precipice falling into Hell.\n"
        "- Demolished and burned to preserve the sacred cohesion of the believing community."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. The Sanctuary Founded Upon Piety (Masjid Quba)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A mosque founded upon God-consciousness from its first day is truly worthy of prayer.\n"
        "- Within it are believers who love to purify themselves physically and spiritually.\n"
        "- And Allah loves those who continuously cleanse their hearts, bodies, and intentions."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE SACRED TRANSACTION & THE RECTITUDE OF SOULS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE SACRED TRANSACTION & THE RECTITUDE OF SOULS",
        "Pillars 11 & 12: The Divine Purchase of Lives, Nine Hallmarks of the Redeemed & Ibrahim's Disassociation",
        "PLATE 06 : THE DIVINE PURCHASE"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: THE DIVINE PURCHASE OF LIVES & WEALTH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Inna Allaha-shtara, The Covenant of Scripture & The Nine Transcendent Hallmarks", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. The Supreme Commerce: Lives & Wealth for Jannah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Inna Allaha-shtara: Allah has purchased from the believers their lives and their wealth.\n"
        "- Decreeing in exchange the ultimate price: eternal inheritance of the Gardens of Paradise.\n"
        "- A sacred transaction transferring mortal selfhood into divine custodianship."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. The Tripartite Covenant of Truth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A binding promise inscribed in truth across the Torah, the Gospel, and the Holy Qur'an.\n"
        "- Who is truer to his covenant than the Creator of the heavens and the earth?\n"
        "- An unshakeable divine guarantee celebrated across all authentic prophetic dispensations."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. 'Rejoice in the Bargain You Have Struck!'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fastabshiroo bi-bay'ikum: Rejoice in the magnificent contract you have concluded.\n"
        "- That is indeed the supreme, incomparable triumph (Al-Fawz al-'Azeem).\n"
        "- Transforming human struggle into eternal celebration in the divine presence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. The Nine Hallmarks of the Redeemed", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The repentant, worshippers, praisers, journeyers, the bowing, and the prostrating.\n"
        "- Enforcers of virtue, restrainers of evil, and vigilant guardians of divine limits.\n"
        "- Give glad tidings to these sincere believers who embody this comprehensive rectitude."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: SEPARATION OF TIES & THE EXAMPLE OF IBRAHIM", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Prohibition of Istighfar for Polytheists & Ibrahim's Conditional Promise", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. Prohibition of Praying for Unrepentant Polytheists", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- It is not for the Prophet and believers to pray for forgiveness for idolatrous kin.\n"
        "- Once it has become evident that they died upon rejection as companions of Hell.\n"
        "- Loyalty to the divine covenant takes precedence over biological sentimentality."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. Ibrahim's Supplication: A Conditional Promise", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Ibrahim sought forgiveness for his father Azar only because of an explicit prior vow.\n"
        "- But when it became manifest that Azar was an enemy to Allah, he disassociated from him.\n"
        "- Clarifying prophetic behavior: absolute submission to Tawhid eclipses family ties."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. Ibrahim: Tender-Hearted & Forbearing (Awwahun Haleem)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Despite his unwavering monotheistic stance, Ibrahim's heart was intensely compassionate.\n"
        "- Awwah: One who sighs frequently out of deep reverent sorrow, love, and fear of God.\n"
        "- Combining intellectual strength and theological clarity with emotional tenderness."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. Divine Justice: Never Misleading After Guidance", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah would never cause a people to stray after guiding them until He clarifies all boundaries.\n"
        "- Accountability is predicated upon clear, uncorrupted knowledge and fair warning.\n"
        "- Indeed, Allah is Knower of all things, ruling creation with immaculate equity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE TRIAL OF TABUK & THE THREE WHO STAYED BEHIND
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE TRIAL OF TABUK & THE THREE WHO STAYED BEHIND",
        "Pillars 13 & 14: The Agony of the Three, The Constricted Earth, Truthfulness & Divine Acceptance",
        "PLATE 07 : TAWBAH & THE THREE"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: THE AGONY OF THE THREE & THE CONSTRICTED EARTH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Ath-Thalathat alladhina Khullifoo, Boycott of Madinah & The Suffocation of Souls", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Divine Pardon for the Prophet, Muhajiroon & Ansar", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah pardoned the Prophet, Emigrants, and Helpers who followed in the hour of hardship.\n"
        "- When the hearts of a faction nearly wavered under the immense trial of Tabuk.\n"
        "- He accepted their repentance; indeed, He is to them full of kindness and mercy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. The Three Who Were Left Behind (Ka'b, Hilal, Murarah)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sincere believers who had no excuse yet refused to fabricate lies like the hypocrites.\n"
        "- Their case was deferred: subject to a complete social boycott for fifty agonizing days.\n"
        "- Choosing painful worldly truth over the transient comfort of a fraudulent excuse."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Vast Earth Constricted (Daqat 'Alayhimul-Ard)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The earth grew suffocatingly narrow despite its vastness; their own souls felt alien.\n"
        "- Cut off from community, ignored by friends, and tested by foreign royal temptations.\n"
        "- An intense spiritual crucible designed to cleanse every trace of complacency."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. No Refuge from Allah Except Unto Him", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The profound realization of absolute Tawhid: Wa zannoo an la malja'a min Allahi illa ilayh.\n"
        "- You cannot flee from God; you can only flee to God in broken, weeping contrition.\n"
        "- The essential breakthrough that unlocks the gates of transformative divine mercy."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: THE DIVINE ACCEPTANCE OF REPENTANCE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Thumma Taba 'Alayhim li-Yatooboo, Truthfulness & The Inscribed Hardships", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. He Turned to Them That They Might Repent", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Thumma taba 'alayhim li-yatooboo: Divine grace precedes and enables human repentance.\n"
        "- At dawn after fifty days, revelation descended announcing their total forgiveness.\n"
        "- The Prophet's face shone like the full moon as he gave Ka'b the joyous news."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. Accompany the Truthful (Koonoo Ma'as-Sadiqeen)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O you who have believed, fear Allah and align yourselves always with the truthful.'\n"
        "- Truthfulness in speech, action, and covenant is the bedrock of moral survival.\n"
        "- The enduring lesson of Ka'b: Truth brings temporary trial but eternal salvation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. Loyalty to the Person of the Messenger", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- It was never fitting for the people of Madinah to lag behind the Messenger of Allah.\n"
        "- Nor to prefer their own mortal lives, comfort, or safety over his sacred mission.\n"
        "- The standard of prophetic companionship requires selfless devotion and sacrifice."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. Every Thirst, Fatigue & Step Recorded", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- No thirst, hunger, or exhaustion afflicts them in Allah's cause except it is inscribed.\n"
        "- Every step that challenges oppression and every spent coin is written as a righteous deed.\n"
        "- Allah will reward them for the very best of what they accomplished with sincerity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: SCHOLARSHIP, INNER PURIFICATION & PROPHETIC COMPASSION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "SCHOLARSHIP, INNER PURIFICATION & PROPHETIC COMPASSION",
        "Pillars 15 & 16: Tafaqquh fid-Deen, The Litmus Test of Revelation, Prophetic Mercy & Hasbiyallah",
        "PLATE 08 : SCHOLARSHIP & HASBIYALLAH"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: THE EXPEDITION OF SACRED KNOWLEDGE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Tafaqquh fid-Deen, Admonishing Communities & The Litmus Test of New Surahs", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. Civilizational Mandate: Tafaqquh fid-Deen", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- It is not proper for all believers to go forth simultaneously to physical battle.\n"
        "- A dedicated contingent must remain to gain deep, verified understanding of religion.\n"
        "- Establishing scholarship and legal knowledge as an indispensable pillar of society."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. Admonishing Communities Upon Return", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Scholars and jurists are commissioned to instruct and guide returning communities.\n"
        "- Warning them of spiritual pitfalls and grounding society in verified divine ethics.\n"
        "- Knowledge is not an ivory-tower indulgence, but an active communal protection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. New Revelation as a Litmus Test of Hearts", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Whenever a new Surah is revealed, the hypocrites mock: 'Whom did this increase in faith?'\n"
        "- For the believers, it dynamically increases their faith and they rejoice in guidance.\n"
        "- For those with diseased hearts, it adds filth upon filth, dying in stubborn denial."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. The Blindness of Chronic Disregard", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Do they not see they are tested with trials once or twice every single year?\n"
        "- Yet they neither turn in repentance nor do they take heed and remember.\n"
        "- Turning away from truth, Allah turns their hearts because they refuse to comprehend."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: THE PROPHETIC HEART & THE SUFFICIENCY OF GOD", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Azeezun 'Alayhi Ma 'Anittum, Ra'oofun Raheem & The Fortress of Hasbiyallah", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. A Messenger from Among Yourselves (Min Anfusikum)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A noble Messenger has arrived from within your human reality, walking among you.\n"
        "- Familiar with your trials, flaws, and hopes, embodying perfection of prophetic adab.\n"
        "- Bridging divine transcendence and earthly existence with supreme moral beauty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. Pained by Your Hardships ('Azeezun 'Alayhi)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Azeezun 'alayhi ma 'anittum: He feels profound internal anguish over whatever harms you.\n"
        "- Any physical difficulty, moral failure, or spiritual torment that afflicts you pains his soul.\n"
        "- The supreme empathy of a shepherd who weeps for the vulnerability of his flock."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. Ardently Devoted & Full of Mercy (Ra'oofun Raheem)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hareesun 'alaykum: Intensely, passionately concerned for your salvation and guidance.\n"
        "- Bestowed two of Allah's own names: Ra'oof (Tenderly Pitying) and Raheem (Merciful).\n"
        "- A boundless fountain of love and gentleness toward all who believe in the truth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. The Ultimate Fortress: Hasbiyallah", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If the entire world turns away in rejection, stand firm upon this solitary mountain:\n"
        "- 'Hasbiyallahu la ilaha illa Huwa, 'alayhi tawakkaltu wa Huwa Rabbul-'Arshil-'Azeem!'\n"
        "- Allah alone suffices; upon Him I rely, and He is the Lord of the Magnificent Throne."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF generated: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/at_tawbah_page"
    subprocess.run(cmd, shell=True, check=True)
    print("Previews generated in previews dir.")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/at_tawbah_page-{i}.png"
        dst = os.path.join(brain_dir, f"at_tawbah_page-{i}.png")
        shutil.copyfile(src, dst)
    print("Previews copied to brain dir successfully.")

if __name__ == "__main__":
    build_at_tawbah_pdf()
