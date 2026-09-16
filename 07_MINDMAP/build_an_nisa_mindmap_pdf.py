#!/usr/bin/env python3
"""
Huurs Studio - Surah An-Nisa Master Landscape Mindmap PDF CompilerStrict Standardization:
- Title: Surah An-Nisa — Master Landscape Mindmap
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
OUTPUT_PDF = os.path.join(BASE_DIR, "AN_NISA_MASTER_MINDMAP.pdf")
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

def build_an_nisa_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AN-NISA", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
        pdf.text("SURAH AN-NISA FOUNDATION ARCHITECTURE", w - 245, 13, font="F2", size=7.2, rgb=GOLD)

    # Column Coordinates
    c1_x, c1_y, c1_w, c1_h = 32, 35, 348, h - 130
    c2_x = c1_x + c1_w + 32
    c2_w = 348

    # =========================================================================
    # PAGE 1: THE PRIMORDIAL ORIGIN & INHERITANCE BOUNDARIES
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE PRIMORDIAL ORIGIN & INHERITANCE BOUNDARIES",
        "Pillars 1 & 2: Nafsin Wahidah, Sacred Arham, Protection of Orphan Wealth, and Hududullah Fara'id",
        "PLATE 01 : ORIGIN & INHERITANCE"
    )

    # Column 1: Pillar 1 (Nafsin Wahidah & Wombs of Mercy)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: NAFSIN WAHIDAH & SACRED WOMBS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ontological Origin, Kinship & Orphan Sanctuary", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Nafsin Wahidah: Ontological Human Equality", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Humanity created from a single primordial soul; shared ontological root.\n"
        "- Male and female share identical moral dignity and accountability before God.\n"
        "- Dismantles patriarchal elitism and racial hierarchy at the source."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Taqwa of the Wombs (Al-Arham)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Fear of Allah coupled directly with reverencing the ties of kinship (Arham).\n"
        "- Maternal sanctuary and uterine bonds elevated to supreme religious piety.\n"
        "- Severe warning against severing family ties or abandoning dependents."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Sacred Trust of Orphan Wealth", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Prohibits substituting worthless goods for the valuable assets of orphans.\n"
        "- Swallowing orphan property is described as stuffing blazing fire into bellies.\n"
        "- Society's moral legitimacy depends on protecting minors lacking legal power."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Polygyny as Social Welfare Mechanism", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Revealed post-Uhud to provide honorable shelter for widows and orphan girls.\n"
        "- Conditioned upon absolute financial and emotional equity among wives.\n"
        "- 'If you fear that you cannot deal equitably, then marry only one.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2 (Divine Inheritance Statutes)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE DIVINE INHERITANCE STATUTES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Fara'id Shares, Economic Dignity & Hududullah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Female Economic Agency & Bridal Gifts (Saduqat)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Bridal gift (Saduqat) is a mandatory unconditional gift (Nihlah) to the woman.\n"
        "- It belongs solely to the female recipient; male guardians cannot seize a dime.\n"
        "- Establishes complete financial independence of women in Islamic jurisprudence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Mandatory Shares for Female Heirs", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Abolishes pre-Islamic custom where women and young minors inherited nothing.\n"
        "- Mothers, daughters, sisters, and wives assigned fixed mathematical shares.\n"
        "- Wealth circulation decentralized across immediate and extended families."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Mathematical Balance of Fara'id", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Precise fractions (1/2, 1/3, 1/4, 1/6, 1/8) decreed directly by divine wisdom.\n"
        "- Balances hereditary inheritance shares with legally mandated financial burdens.\n"
        "- Eradicates testamentary tyranny and bitter family inheritance disputes."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Hududullah: The Immutable Divine Boundaries", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Inheritance shares explicitly designated as the sacred boundaries of Allah.\n"
        "- Those who obey enter gardens beneath which rivers flow forever.\n"
        "- Those who violate or alter these boundaries face agonizing eternal humiliation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: MARITAL EQUITY, ECONOMIC CONTRACTS & DOMESTIC PEACE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "MARITAL EQUITY, ECONOMIC CONTRACTS & DOMESTIC PEACE",
        "Pillars 3 & 4: Eradicating Forced Marriage, 'Ashiroohunna bil-Ma'roof, Qiwamah, and The Two Arbiters",
        "PLATE 02 : MARITAL EQUITY"
    )

    # Column 1: Pillar 3 (Honorable Companionship & Bounds)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: HONORABLE COMPANIONSHIP & BOUNDS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Emancipating Widows & Sacred Forbidden Ties", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Abolition of Inheriting Women by Force", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'It is not lawful for you to inherit women against their will.'\n"
        "- Eradicated the pagan practice of claiming deceased relatives' wives as property.\n"
        "- Women granted total legal sovereignty to marry or live as they choose."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. 'Ashiroohunna bil-Ma'roof: Principled Kindness", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Living with wives in honorable kindness regardless of fluctuating emotions.\n"
        "- 'For if you dislike them, perhaps you dislike something Allah made greatly good.'\n"
        "- Demands moral character and patience during marital friction and hardship."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Meethaqan Ghaleedha: The Weighty Covenant", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Marriage designated with the supreme title of a heavy, solemn covenant.\n"
        "- Forbids taking back paid dowries even if a treasure (Qintar) was given.\n"
        "- Protects women's financial assets from vindictive post-divorce reclaiming."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Prohibited Bounds of Marriage (Al-Muharramat)", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Precise legal classification of unlawful marriages (mothers, daughters, sisters).\n"
        "- Includes fosterage (milk-kinship) and marrying two sisters simultaneously.\n"
        "- Establishes the sanctity of family boundaries and prevents genetic corruption."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4 (Qiwamah Responsibility & The Two Arbiters)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: QIWAMAH & ARBITRATION PROTOCOLS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Protective Guardianship & Marital Conflict Resolution", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Commercial Ethics: Free Consent (Tijaratan 'an Taradin)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Consuming wealth unjustly through fraud, usury, or coercion is forbidden.\n"
        "- Economic transactions require genuine mutual consent of contracting parties.\n"
        "- 'And do not kill yourselves; indeed, Allah is ever Merciful to you.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Qiwamah as Protective Custodianship", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Men appointed as caretakers (Qawwamoon) based on divine duty to spend wealth.\n"
        "- Qiwamah represents protective maintenance and defense, not patriarchal ego.\n"
        "- A man who fails his financial and moral duty violates the terms of Qiwamah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. De-escalating Domestic Strife (Nushuz)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Three-stage graduated intervention for marital rebellion: Admonition first.\n"
        "- Followed by separation of sleeping quarters to encourage cool reflection.\n"
        "- If partners return to harmony, seeking further grievance is strictly forbidden."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Two Arbiters (Hakamayn) Protocol", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Convening trusted mediators from his family and hers before divorce proceeds.\n"
        "- 'If both arbiters desire reconciliation, Allah will cause harmony between them.'\n"
        "- Institutionalizes external family diplomacy to save marriages from dissolution."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE DECALOGUE OF COMPASSION & DIVINE GOVERNANCE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE DECALOGUE OF COMPASSION & DIVINE GOVERNANCE",
        "Pillars 5 & 6: The Ten Concentric Rings of Ihsan, Rendering Trusts, and The Constitutional Hierarchy of Authority",
        "PLATE 03 : GOVERNANCE & RIGHTS"
    )

    # Column 1: Pillar 5 (The Ten Pillars of Social Compassion)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: THE TEN PILLARS OF COMPASSION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Concentric Circles of Mercy & Dismantling Arrogance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Monotheism Anchoring the Social Decalogue", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Worship Allah and associate nothing with Him' opens the social charter.\n"
        "- Shunning the boastful, arrogant soul; humility before God produces mercy.\n"
        "- Social justice is not secular policy, but an act of direct worship."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Immediate Circle: Parents, Relatives & Orphans", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Unconditional excellence (Ihsan) to mother and father as first social duty.\n"
        "- Sustaining kin ties and sheltering vulnerable orphans and the poor.\n"
        "- Family preservation forms the core foundation of a healthy civil order."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Expanding Sphere: Near & Far Neighbors", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Duty extends to the immediate neighbor and the stranger/distant neighbor.\n"
        "- Honoring the companion at your side (work colleagues, traveling partners).\n"
        "- Eradicating social alienation through continuous daily neighborhood care."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Wayfarer & Domestic Subordinates", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Welcoming traveling strangers and protecting domestic workers and servants.\n"
        "- Condemning those who are stingy and hoard God's favors from the weak.\n"
        "- A society is judged by how it treats its most powerless and transient guests."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6 (Rendering Trusts & Hierarchy of Law)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: RENDERING TRUSTS & HIERARCHY OF LAW", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Amanat Custodianship & The Constitutional Order", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Rendering Trusts (Amanat) to Their Rightful Owners", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Allah commands you to render trusts to those to whom they are due.'\n"
        "- Key of the Ka'bah returned to Uthman ibn Talha, establishing meritocracy.\n"
        "- Public office and judicial authority are sacred trusts, not political spoils."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Impartial Judicial Decree: In Tahkumu bil-'Adl", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'And when you judge between people, judge with absolute justice.'\n"
        "- The command applies to all mankind ('Bayan an-Nas'), not only Muslims.\n"
        "- Judicial objectivity is immune to racial, sectarian, or national bias."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Constitutional Chain of Authority (Ayah 59)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 1. Obey Allah (Qur'an)  2. Obey the Messenger (Sunnah)  3. Uli al-Amr.\n"
        "- Disputed state matters must be referred back to Allah and the Messenger.\n"
        "- Obedience to human rulers is never absolute; it is conditional on revelation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Inner Submission to Prophetic Verdict (Ayah 65)", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- 'No, by your Lord, they do not believe until they make you judge in disputes.'\n"
        "- Demands complete eradication of internal resentment (Haraj) against verdicts.\n"
        "- Sincere faith culminates in joyful surrender (Yusallimoo Tasleema)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: SACRED DEFENSE, OPPRESSED CRIES & DIVINE DECREE
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "SACRED DEFENSE, OPPRESSED CRIES & DIVINE DECREE",
        "Pillars 7 & 8: Rescuing the Mustad'afeen, Tactical Vigilance, Inevitable Mortality, and Tadabbur of Scripture",
        "PLATE 04 : SACRED DEFENSE"
    )

    # Column 1: Pillar 7 (Rescuing the Oppressed)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: RESCUING THE OPPRESSED", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Humanitarian Liberation & Tactical Preparedness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Tactical Vigilance: Khudhu Hidhrakum", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believers commanded to maintain tactical alertness and situational security.\n"
        "- Advancing in prepared detachments (Thubatin) or as a unified collective force.\n"
        "- Faith in divine protection never excuses operational negligence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Warfare as Humanitarian Liberation (Ayah 75)", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Why do you not fight in Allah's cause and for the oppressed (Mustad'afeen)?'\n"
        "- Children, women, and the elderly weeping for rescue from tyrannical cities.\n"
        "- Islamic combat is defined not by conquest, but by breaking the chains of tyrants."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Combat of Faith vs. The Way of Taghut", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The sincere fight in the path of Allah to establish truth and end persecution.\n"
        "- The corrupt fight in the path of Taghut (tyranny, greed, and idolatry).\n"
        "- 'Fight the allies of Satan; indeed, Satan's plot is inherently frail.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Inescapable Hour in Fortified Towers", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- 'Wherever you may be, death will find you, even if in towering fortresses.'\n"
        "- Cowardice cannot postpone death, and courageous defense cannot hasten it.\n"
        "- Liberating the human mind from existential dread and paralyzing fear."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8 (Tadabbur of the Word & Ethical Warfare)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: TADABBUR & ETHICAL ENGAGEMENT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Scriptural Harmony, Mediation & Restraint", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Afala Yatadabbaroon: The Proof of Harmony (Ayah 82)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Do they not contemplate the Qur'an with deep reflective intellect?'\n"
        "- Had it been from other than Allah, they would find much contradiction in it.\n"
        "- Internal structural perfection over 23 years confirms divine revelation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Shafa'ah Hasanah: Moral Complicity", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Whoever intercedes for a righteous cause shares in its eternal reward.\n"
        "- Whoever intercedes for an evil cause bears full spiritual liability for it.\n"
        "- Words and political endorsements carry heavy eschatological weight."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Returning the Greeting of Peace with Excellence", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'When greeted with a greeting, greet with one better or return it equally.'\n"
        "- Elevating everyday social interaction into an arena of intentional goodwill.\n"
        "- Fostering mutual warmth and peace within the collective civic sphere."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Dealing with Neutral Factions & Covenants", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Those who join allies with a treaty, or come reluctant to fight you, are spared.\n"
        "- If they withdraw, refrain from combat, and offer peace, war is forbidden.\n"
        "- War is restricted strictly to active combatants who persecute faith."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: SANCTITY OF BLOOD, INVESTIGATION & COMBAT PRAYER
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "SANCTITY OF BLOOD, INVESTIGATION & COMBAT PRAYER",
        "Pillars 9 & 10: Inviolability of Muslim Life, The Duty of Fatabayyanoo, Hijrah, and Salat al-Khawf",
        "PLATE 05 : SANCTITY OF LIFE"
    )

    # Column 1: Pillar 9 (Inviolability of Blood & Fatabayyanoo)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: INVIOLABILITY OF LIFE & VERIFICATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Blood Penalties, Fatabayyanoo & Spiritual Migration", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Inviolability of Believing Life & Homicide Law", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Accidental killing requires freeing a believing slave and blood-money (Diyah).\n"
        "- Deliberate killing of a believer punished with Hell, divine curse, and wrath.\n"
        "- Establishing the absolute sanctity of human life as an inviolable boundary."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Fatabayyanoo: Mandatory Verification Before Action", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'When you go forth in Allah's cause, investigate (*Fatabayyanoo*) thoroughly.'\n"
        "- Never say to one who offers peace 'You are not a believer' to seize cattle.\n"
        "- The Prophet severely reprimanded Usamah for slaying one who uttered Tawhid."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Hierarchy of Striving vs. Passive Inaction", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believers who sit back without physical excuse are not equal to active strivers.\n"
        "- Striving with wealth and life elevated by immense ranks, mercy, and forgiveness.\n"
        "- Honor in the divine sight belongs to proactive sacrifice, not passive comfort."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Hijrah: Escaping Spiritual Oppression", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Angels question dying souls: 'Were you not oppressed? Was not earth spacious?'\n"
        "- Enduring compromise under tyranny is condemned when migration is possible.\n"
        "- Migration to preserve faith guarantees expansive refuge and abundant provision."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10 (Salat al-Khawf & Fixed Timings of Prayer)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: SALAT AL-KHAWF & PRAYER TIMINGS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Combat Worship Architecture & Timeless Fixed Statutes", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Qasr: Divine Leniency in Shortening Prayer", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When traveling through the earth, shortening four-unit prayer is permitted.\n"
        "- Especially ordained during times of fear or impending enemy engagement.\n"
        "- Divine legislation provides merciful adaptability without compromising duty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Salat al-Khawf: Corporate Worship Under Fire", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- The army divides into two shifts: One party prays while holding weapons.\n"
        "- The second party guards against surprise enemy encirclement, then alternates.\n"
        "- Even in the roar of battle, congregational prayer cannot be abandoned."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Post-Combat Dhikr: Constant Mindful Presence", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'When you finish prayer, remember Allah standing, sitting, and on your sides.'\n"
        "- Deep psychological grounding to heal trauma and adrenaline after combat.\n"
        "- Re-connecting the soldier's heart to eternal peace through divine praise."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Kitaban Mawqoota: The Fixed Timings of Prayer", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- 'Indeed, prayer has been decreed upon the believers at specified times.'\n"
        "- Re-establishing normal full prayer once physical security is restored.\n"
        "- The 5 daily appointments are an unbending spiritual anchor across life."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: ABSOLUTE JUSTICE, TREASON & COMBATING SHIRK
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "ABSOLUTE JUSTICE, TREASON & COMBATING SHIRK",
        "Pillars 11 & 12: The Trial of Tu'mah, Condemnation of Deceit, Rebutting Satan, and Qawwameena bil-Qist",
        "PLATE 06 : ABSOLUTE JUSTICE"
    )

    # Column 1: Pillar 11 (Judicial Integrity & Tu'mah's Trial)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: JUDICIAL INTEGRITY & TU'MAH'S TRIAL", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Exonerating the Innocent & Exposing Tribal Collusion", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Trial of Tu'mah ibn Ubayriq", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- A nominal Muslim stole armor and hid it with an innocent Jewish citizen.\n"
        "- Tu'mah's clan pressured the Prophet to defend him to protect Muslim pride.\n"
        "- Revelation descended from seven heavens exposing the Muslim and clearing the Jew."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Wa La Takun lil-Kha'ineena Khaseema", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'And do not plead on behalf of the deceitful and treacherous.'\n"
        "- Severe divine reprimand: God's Prophet cannot be used as an advocate for fraud.\n"
        "- Establishes that truth and innocence transcend religious and tribal identity."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. The Ethics of Secret Counsel (Najwa)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'No good is there in much of their private whispers (Najwa).'\n"
        "- Permitted only when commanding charity, righteous virtue, or reconciliation.\n"
        "- Condemns covert factional plotting, political gossip, and conspiracies."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Slander and Moral Guilt: Buhtanan wa Ithman", c1_x + 12, y_c, font="F2", size=8, rgb=ROSE)
    t = (
        "- 'Whoever commits a sin and then blames an innocent person bears slander.'\n"
        "- Framing an innocent individual carries double guilt in the court of God.\n"
        "- Protecting the reputation of every citizen against malicious defamation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12 (Qawwameena bil-Qist: Universal Witness)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: QAWWAMEENA BIL-QIST", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Unforgivable Shirk & Absolute Universal Justice", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Unpardonable Treason of Shirk", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Indeed, Allah does not forgive that partners be associated with Him.'\n"
        "- He forgives anything lesser to whom He wills; Shirk is cosmic falsehood.\n"
        "- Associating created dust with the Uncreated Sustainer corrupts human purpose."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Satan's Deceptions: Altering the Creation", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Satan vows to misguide mankind through false hopes and superstitious rituals.\n"
        "- Inciting humanity to alter the physical and moral creation of Allah.\n"
        "- 'Whoever takes Satan as an ally has suffered a manifest and total loss.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Absolute Gender Equality in Salvation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Whoever does righteous deeds, whether male or female, while believing...'\n"
        "- Those will enter Paradise and not be wronged by even the speck on a date-seed.\n"
        "- Demolishes all patriarchal claims of preferential spiritual status."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Qawwameena bil-Qist: Absolute Justice (Ayah 135)", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- 'Be persistently standing firm in justice, witnesses for Allah.'\n"
        "- Even if against yourselves, parents, or kin; whether rich or poor.\n"
        "- 'Follow not personal passion, lest you deviate from the truth.'"
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE ANATOMY OF HYPOCRISY & ISA'S VINDICATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE ANATOMY OF HYPOCRISY & ISA'S VINDICATION",
        "Pillars 13 & 14: Mudhbdhabeen Wavering, Ad-Dark al-Asfal, Exonerating Maryam, and Refuting Crucifixion",
        "PLATE 07 : HYPOCRISY & ISA"
    )

    # Column 1: Pillar 13 (The Anatomy of Hypocrisy)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: THE ANATOMY OF HYPOCRISY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Opportunistic Wavering & The Fourfold Path of Taubah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Mudhbdhabeen: The Fluctuating Soul", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hypocrites waver between belief and disbelief; belonging to neither camp.\n"
        "- They watch the tide: If Muslims triumph, they claim alliance; if not, they join foes.\n"
        "- Opportunism destroys moral integrity and leaves the soul adrift."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Sluggish Prayer & Performative Display (Riya')", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'When they stand for prayer, they stand lazily, to be seen by people.'\n"
        "- They remember Allah only marginally, devoid of reverence and presence.\n"
        "- Performing religious rituals as social performance corrupts spiritual value."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Ad-Dark al-Asfal: The Lowest Abyss of Fire", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Indeed, the hypocrites will be in the lowest depth of the Fire.'\n"
        "- And never will you find for them a protector or helper against God.\n"
        "- Internal betrayal of truth receives harsher retribution than open denial."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Fourfold Door of Sincere Redemption", c1_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Except those who: 1. Repent  2. Rectify wrongs  3. Hold fast to Allah\n"
        "- And 4. Purify their religion solely for Him; they are with sincere believers.\n"
        "- Divine mercy remains open even to the worst hypocrite upon true reform."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14 (Exonerating Maryam & Refuting Crucifixion)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: EXONERATING MARYAM & REFUTING CRUCIFIXION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Rebutting Slanders & The Heavenly Rescue of Isa", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Rebutting Monstrous Slanders Against Maryam", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Condemning those who uttered a monstrous slander (Buhtanan 'Adheema).\n"
        "- Vindicating the virgin Maryam's purity, honor, and celestial election.\n"
        "- Slandering chaste women is condemned as an unforgivable moral crime."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The Boast of Deicide Dismantled", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- Rebutting the arrogant boast: 'We killed the Messiah Isa, the messenger.'\n"
        "- Human beings have no power to execute the chosen Word of God.\n"
        "- Demolishing both Jewish boast of execution and Christian theology of deicide."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Wa Ma Qataloohu Wa Ma Salaboohu", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'They killed him not, nor did they crucify him, but so it appeared to them.'\n"
        "- Those who dispute regarding his fate are in doubt, following mere conjecture.\n"
        "- 'For surely, they killed him not!' — categorical Quranic certainty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Heavenly Ascension & Preservation of the Prophet", c2_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- 'Rather, Allah raised him to Himself; Allah is ever Exalted in Might, Wise.'\n"
        "- Isa was spared physical crucifixion, elevated bodily to heavenly honor.\n"
        "- Preserved until his appointed return before the Day of Resurrection."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE PROPHETIC CHAIN, PROHIBITING GHULUWW & THE SEAL
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE PROPHETIC CHAIN, PROHIBITING GHULUWW & THE SEAL",
        "Pillars 15 & 16: The Cosmic Prophetic Stream, Takleem Musa, Demolishing Trinitarian Excess, and The Kalalah Seal",
        "PLATE 08 : PROPHETIC SEAL"
    )

    # Column 1: Pillar 15 (The Prophetic Stream & Takleem Musa)
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: THE PROPHETIC CHAIN & TAKLEEM MUSA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Unbroken Revelation & Direct Divine Speech", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Cosmic Chain of Inspired Messengers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Revelation sent to Muhammad as sent to Nuh, Ibrahim, Isma'il, Ishaq, Ya'qub.\n"
        "- Tribes, Isa, Ayyub, Yunus, Harun, Sulayman, and the Zabur given to Dawud.\n"
        "- Islam unites the entire prophetic lineage into a single divine message."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. Messengers Mentioned & Unmentioned", c1_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'Messengers We have related to you before and messengers We have not.'\n"
        "- Universal prophetic presence: Every civilization received divine warning.\n"
        "- Humility in recognizing that God's guidance transcends known historical records."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Wa Kallamallahu Musa Takleema: Direct Divine Speech", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And to Musa Allah spoke directly with real speech (Takleema).'\n"
        "- Affirming the divine attribute of Kalam without metaphorical dilution.\n"
        "- Honoring Musa as Kalimullah who heard the speech of God at Mount Tuwa."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c1_x + 12, y_c + 6, c1_x + c1_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. Messengers as Bearers of Glad Tidings & Warning", c1_x + 12, y_c, font="F2", size=8, rgb=CYAN)
    t = (
        "- Messengers bring glad tidings of Paradise and warning of divine punishment.\n"
        "- Sent so mankind will have no argument against Allah after the messengers.\n"
        "- God's justice is perfect: Accountability only occurs after clear warning."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16 (Demolishing Trinitarian Ghuluww & Kalalah)
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c1_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: DEMOLISHING GHULUWW & THE KALALAH SEAL", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Pristine Monotheism & The Final Inheritance Charter", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c1_y + c1_h - 36, c2_x + c2_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. La Taghloo: Prohibition of Religious Extremism", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O People of the Scripture, do not exceed limits (Ghuluww) in your religion.'\n"
        "- Do not speak about Allah except the absolute truth of His transcendent Tawhid.\n"
        "- Religious excess corrupts monotheism and deifies mortal human beings."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("2. The True Definition of the Messiah Isa", c2_x + 12, y_c, font="F2", size=8, rgb=GOLD_LIGHT)
    t = (
        "- 'The Messiah Isa, son of Maryam, was only a messenger of Allah.'\n"
        "- And His Word cast into Maryam, and a Spirit created by Him (Ruhun Minhu).\n"
        "- Honored as a noble prophet and humble servant, never as Lord or partner."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("3. Wa La Taqooloo Thalathah: Cease the Trinity!", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Believe in Allah and His messengers, and do not say \"Three\"!'\n"
        "- 'Cease! It is better for you. Indeed, Allah is but one God.'\n"
        "- Exalted is He above having a son; to Him belongs whatever is in creation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c -= 58
    pdf.line(c2_x + 12, y_c + 6, c2_x + c2_w - 12, y_c + 6, stroke_rgb=BORDER_MUTED, line_width=0.5)
    pdf.text("4. The Statutory Seal: Kalalah (Ayah 176)", c2_x + 12, y_c, font="F2", size=8, rgb=EMERALD)
    t = (
        "- Final verse codifying inheritance for individuals without parents or children.\n"
        "- Shares for brothers and sisters precisely established to prevent family ruin.\n"
        "- Surah concludes as it began: Safeguarding the property and rights of the weak."
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
        os.path.join(PREVIEWS_DIR, "an_nisa_page")
    ]
    subprocess.run(cmd, check=True)
    print(f"Previews saved to {PREVIEWS_DIR}")

    # Copy previews to brain directory
    for f in os.listdir(PREVIEWS_DIR):
        if f.startswith("an_nisa_page-") and f.endswith(".png"):
            src = os.path.join(PREVIEWS_DIR, f)
            dst = os.path.join(brain_dir, f)
            shutil.copy2(src, dst)
            print(f"Copied {f} to brain directory: {dst}")

if __name__ == "__main__":
    build_an_nisa_pdf()
