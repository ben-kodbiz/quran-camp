#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Anfal Master Landscape Mindmap PDF CompilerStrict Standardization:
- Title: Surah Al-Anfal — Master Landscape Mindmap
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
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_ANFAL_MASTER_MINDMAP.pdf")
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

def build_al_anfal_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-ANFAL", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
        pdf.text("AUTHENTICATED EXEGESIS (TABARI * IBN KATHIR * QURTUBI * IBN AL-QAYYIM)", w - 355, 11, font="F2", size=7.0, rgb=GOLD)

    # Column geometry
    c1_x = 32
    c2_x = 412
    c1_w = 348
    c2_w = 348
    c1_y = 48
    c1_h = 332

    # =========================================================================
    # PAGE 1: THE SPOILS OF WAR, THE HEART OF FAITH & THE EVE OF BADR
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE SPOILS OF WAR, THE HEART OF FAITH & THE EVE OF BADR",
        "Pillars 1 & 2: Subordination of Spoils, Hallmarks of True Faith, Reluctance for Battle & The 1,000 Angels",
        "PLATE 01 : BADR & PILLARS OF FAITH"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: SPOILS OF WAR & HALLMARKS OF FAITH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Al-Anfal Subordinated, Reconciling Internal Disputes & The Trembling Heart", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. Spoils of War Belong to Allah & Messenger", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Companions inquired concerning the allocation of the spoils of Badr.\n"
        "- Revelation shifts focus: Spoils belong to Allah and His Messenger unconditionally.\n"
        "- Divine command: Cultivate Taqwa and reconcile fraternal disputes among believers."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. The Hallmarks of True Faith (Innamal-Mu'minoon)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believers are those whose hearts tremble with awe when Allah is remembered.\n"
        "- Faith is not static; it increases dynamically upon hearing divine verses recited.\n"
        "- Sincere believers place their unconditional reliance (Tawakkul) exclusively upon Him."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. Pillars of Righteous Practice: Salah & Spending", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- True believers establish regular prayer and spend from divine provision.\n"
        "- Those who embody these traits are the believers in absolute truth and reality.\n"
        "- For them are elevated degrees with their Lord, divine forgiveness, and noble bounty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. Reluctance Before the Decreed Encounter", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- As your Lord brought you forth from your home in truth, a group disliked it.\n"
        "- Disputing concerning the truth after it had become manifest, driven toward death.\n"
        "- Human aversion to hardship contrasted with the divine decree of ultimate triumph."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: THE TWO PARTIES & THE ANGELIC LEGIONS", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Caravan vs Army, Uprooting Falsehood & Seeking Rescue (Istighathah)", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. The Two Parties: Unarmed vs Heavily Armed", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believers wished to intercept the unarmed merchant caravan of Abu Sufyan.\n"
        "- Allah willed to establish the truth through His Words and sever the roots of deniers.\n"
        "- Proving that divine wisdom directs events toward lasting historical triumph."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. To Confirm the Truth & Abolish Falsehood", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The clash was engineered to manifest the supremacy of truth over falsehood.\n"
        "- Even though the stubborn criminals and polytheistic chieftains detested it.\n"
        "- Badr established the independent sovereignty and moral authority of the Ummah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. Seeking Rescue: Reinforcement with 1,000 Angels", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- In the bower at Badr, the Prophet pleaded passionately in desperate Istighathah.\n"
        "- Allah responded: 'I will reinforce you with a thousand angels in succession.'\n"
        "- Made as glad tidings and tranquil reassurance; victory is only from Allah, the Mighty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. The Descending Slumber & Purifying Rain", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine slumber (An-Nu'as) enveloped anxious warriors as a shield of peaceful serenity.\n"
        "- Pure rain descended from heaven to cleanse, remove Satan's whispers, and pack the sand.\n"
        "- Fortifying their beating hearts and establishing their feet firmly upon the battlefield."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: DIVINE INTERVENTION, THE CAST STAFF & PROHIBITIONS OF RETREAT
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "DIVINE INTERVENTION, THE CAST STAFF & PROHIBITIONS OF RETREAT",
        "Pillars 3 & 4: Angelic Battlefield Assistance, Retreat Forbidden, 'Allah Threw' & The Deaf/Dumb Beasts",
        "PLATE 02 : DIVINE INTERVENTION"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: ANGELIC WARFARE & THE CRIME OF RETREAT", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Striking Necks, Defying Revelation & The Mortal Sin of Battlefield Flight", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. Angelic Warfare: Striking Necks & Fingertips", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah inspired the angels: 'I am with you, so strengthen those who have believed.'\n"
        "- 'I will cast terror into the hearts of those who disbelieved; strike above the necks.'\n"
        "- Severing their fingertips because they defied Allah and His Messenger in rebellion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. Severe Retribution for Arrogant Rebellion", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Whoever defies Allah and His Messenger meets the severe punishment of God.\n"
        "- Taste this earthly degradation; for the disbelievers is the torment of the Fire.\n"
        "- Arrogant reliance on superior numbers and military hardware shattered completely."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. Inviolable Law: Never Turn Backs in Battle", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When meeting advancing hostile armies in battle, never turn your backs in flight.\n"
        "- Turning back incurs the wrath of Allah; their final eternal refuge is Hellfire.\n"
        "- Permitted only as a tactical maneuver to reposition or rejoin another detachment."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. The Mortal Sin of Fleeing the Encounter", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Prophet classified fleeing the battlefield as one of seven mortal sins (Mubiqat).\n"
        "- Faith requires unshakeable resolve when defending truth against armed aggression.\n"
        "- The steadfast stand of 313 believers established an eternal benchmark of courage."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: DIVINE CAUSALITY & THE RECEPTIVE EAR", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Handful of Dust, Gracious Examination & The Deaf and Dumb Who Reason Not", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. Divine Causality: 'You Threw Not, But Allah Threw'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'You killed them not, but Allah killed them; you threw not when you threw, but Allah threw.'\n"
        "- The Prophet cast dust toward Quraysh; divine power carried it into every hostile eye.\n"
        "- Human effort is merely an obedient vessel; ultimate triumph belongs to God alone."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. A Gracious Examination for Believers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- That He might test the believers with a gracious, purifying trial of faith.\n"
        "- Indeed, Allah is All-Hearing of supplications and All-Knowing of internal motives.\n"
        "- Divine strategy weakens the plots of the disbelievers and dismantles their schemes."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. Turn Not Away While You Hear Revelation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O you who believe, obey Allah and His Messenger and do not turn away from him.'\n"
        "- Do not be like hypocrites who say 'We hear' while their hearts are completely deaf.\n"
        "- Hypocritical auditory compliance without spiritual obedience is spiritual suicide."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. The Worst of Beasts: Deaf & Dumb Who Reason Not", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The vilest living creatures in Allah's sight are the deaf and dumb who understand not.\n"
        "- Had Allah known any goodness in them, He would have caused them to hear and reflect.\n"
        "- Even if made to hear without sincerity, they would have turned away in stubborn aversion."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE CALL TO LIFE, SPIRITUAL INTERVENTIONS & THE PLOTS OF MAKKAH
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE CALL TO LIFE, SPIRITUAL INTERVENTIONS & THE PLOTS OF MAKKAH",
        "Pillars 5 & 6: Responding to What Gives Life, Sovereignty Over Hearts, Universal Fitnah & Dar an-Nadwah",
        "PLATE 03 : LIFE & INWARD INTERVENTION"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: THE CALL TO LIFE & SOVEREIGNTY OVER HEARTS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Revelation as Vitality, Allah Intervening Between Hearts & Avoiding Fitnah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. Answer the Call to What Grants Authentic Life", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Respond to Allah and to the Messenger when he calls you to that which gives you life.'\n"
        "- Divine commandments are not restrictive shackles, but the fountain of true life.\n"
        "- Living without revelation is spiritual necrosis, reducing man to an empty shell."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. Allah Intervenes Between Man & His Heart", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Know that Allah intervenes between a human being and his most intimate heart.\n"
        "- You do not own your heart; spiritual steadfastness is a continuous divine gift.\n"
        "- To Him you will be gathered; delaying repentance risks permanent spiritual blindness."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. Beware the Fitnah That Afflicts Beyond Wrongdoers", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fear a trial that will not strike the oppressors among you exclusively.\n"
        "- Passive tolerance of corruption and failure to enjoin good invites collective trials.\n"
        "- Society is an interconnected vessel; letting sinners drill holes sinks everyone."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Remember When You Were Few & Oppressed", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Remember when you were a vulnerable, oppressed minority in the lands of Makkah.\n"
        "- Fearing that hostile factions would abduct and destroy you at any moment.\n"
        "- Allah sheltered you, strengthened you with His aid, and provided wholesome tayyibat."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: FIDUCIARY INTEGRITY & THE DAR AN-NADWAH PLOT", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Betraying Trusts, Wealth and Children, Taqwa as Criterion & The Best of Planners", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. Betray Not Allah, Messenger & Your Trusts", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Do not betray Allah and the Messenger, nor betray your mutual trusts knowingly.\n"
        "- Fiduciary purity in commercial, military, and spiritual trusts is a sacred duty.\n"
        "- Believers protect covenants and secrets with utmost integrity and religious honor."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. Wealth & Offspring: A Delicate Cosmic Trial", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Know that your material wealth and your children are an examination (Fitnah).\n"
        "- Excessive love for family and money must never induce compromises in divine law.\n"
        "- With Allah alone is an immense, incomparable, and eternal reward."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. Taqwa as Furqan: The Criterion of Discernment", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If you maintain Taqwa of Allah, He will grant you a Furqan (divine criterion).\n"
        "- Furqan grants razor-sharp moral clarity to discern truth from alluring falsehood.\n"
        "- He will expiate your evil deeds and forgive you; Allah possesses immense grace."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. The Dar an-Nadwah Conspiracy Foiled", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The Makkan council plotted three options: to imprison, assassinate, or exile you.\n"
        "- 'They plot, and Allah plans; and Allah is the best of all planners.'\n"
        "- Divine counter-strategy delivered the Messenger safely to the sanctuary of Madinah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE PRE-ISLAMIC MINDSET, THE SHIELD OF FORGIVENESS & THE CRITERION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE PRE-ISLAMIC MINDSET, THE SHIELD OF FORGIVENESS & THE CRITERION",
        "Pillars 7 & 8: Tales of the Ancients, Imprecation of Brimstone, The Shield of Istighfar & The Fifth Share",
        "PLATE 04 : THE CRITERION & THE DUAL SHIELDS"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: SKEPTICISM, WHISTLING PRAYERS & THE TWO SHIELDS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Pagan Dismissals, The Shield of the Prophet, Power of Istighfar & Empty Rituals", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. Dismissing Revelation as 'Tales of the Ancients'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When divine verses are recited, they dismiss: 'We have heard; these are ancient legends.'\n"
        "- Arrogant intellectual cynicism blinds the soul to moral and metaphysical depth.\n"
        "- Packaging revelation as outdated myths is an ancient, repetitive skeptical tropes."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. Demanding Brimstone: The Arrogance of Imprecation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cynical prayer: 'O Allah, if this is the truth from You, rain upon us stones from heaven!'\n"
        "- Instead of asking for guidance to truth, they demanded catastrophic destruction.\n"
        "- Psychological obstinacy prefers obliteration over humbling the ego before God."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. The Twin Shields of Earthly Security", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah would not punish them while the Prophet walked physically among them.\n"
        "- Nor will Allah punish a people while they actively seek forgiveness (Istighfar).\n"
        "- The second shield remains permanently active in the hands of believers until the Hour."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. Empty Pagan Rituals: Whistling & Clapping", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Their prayer at the Sacred House was nothing but whistling and clapping (Muka'an).\n"
        "- Sensory distraction designed to drown out the recitation of the Holy Qur'an.\n"
        "- Empty ritualism devoid of reverence, humility, and moral transformation."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: SPENDING TO OBSTRUCT & THE FIFTH SHARE (KHUMS)", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Squandering Wealth, Separating Filth from Pure & The Welfare Share", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. Squandering Wealth to Obstruct Truth", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Disbelievers spend their fortunes to hinder humanity from the pathway of Allah.\n"
        "- They will spend it, then it will become a source of bitter, burning regret for them.\n"
        "- Ultimately overcome and vanquished; gathered into the roaring abyss of Hell."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. Separating the Filthy from the Pure", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- That Allah may separate the vile and impure (Al-Khabeeth) from the good and pure.\n"
        "- Piling the impure one upon another, heaping it all together into the Fire.\n"
        "- Ethical polarization: History systematically sifts moral purity from corrupt arrogance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. Ceasing Hostilities: Forgiveness for Past Sins", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Say to those who disbelieved: If they cease hostility, their past will be forgiven.\n"
        "- But if they return to aggression, the precedent of ancient nations has passed.\n"
        "- Islam opens the door of complete redemption even to formerly bitter combatants."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. The Fifth Share (Al-Khums): Social Welfare & State", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- One-fifth of captured spoils is reserved for Allah, Messenger, and public welfare.\n"
        "- Dedicated to the Prophet's kin, orphans, the poor, and destitute wayfarers.\n"
        "- Sanctifying material gains by anchoring them in social justice and public good."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: THE GEOMETRY OF CONFLICT, PROPHETIC DREAMS & PSYCHOLOGICAL ORDER
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE GEOMETRY OF CONFLICT, PROPHETIC DREAMS & PSYCHOLOGICAL ORDER",
        "Pillars 9 & 10: Topography of Badr, Minimizing Dreams, Four Pillars of Victory & Avoiding Disputes",
        "PLATE 05 : STRATEGIC COHESION"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: THE TOPOGRAPHY OF BADR & PROPHETIC VISIONS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Near and Far Slopes, Unplanned Rendezvous, Dreams of Minimization & Divine Decree", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. The Topography of Badr: Near & Far Slopes", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believers on the near slope (Ad-Dunya), pagans on the far slope (Al-Quswa).\n"
        "- The commercial caravan positioned on the coastal plain below them.\n"
        "- An unplanned convergence orchestrated by God to accomplish a decreed reality."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. Prophetic Vision: Minimizing Enemy Force", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah showed the enemy few in the Prophet's dream before the engagement.\n"
        "- Had He shown them numerous, you would have faltered and disputed the decision.\n"
        "- Divine psychological calibration preserved communal resolve and courage."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. The Optical Illusion of Mutual Minimization", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Upon meeting on the sands, Allah made each force appear small in the other's eyes.\n"
        "- That the pagans would not retreat, and the believers would advance with courage.\n"
        "- Executing the predetermined decree: All cosmic affairs return ultimately to Allah."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. The Inevitable Execution of Divine Will", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Neither army operated by random coincidence or independent human calculation.\n"
        "- The watershed encounter was guided by divine design to establish truth on earth.\n"
        "- Badr transformed a struggling faith into an unshakeable geopolitical reality."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: FOUR PILLARS OF VICTORY & DISPUTE PROHIBITION", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Steadfastness, Abundant Dhikr, Obedience & 'Lest You Falter and Lose Strength'", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. Pillar 1 & 2: Firm Steadfastness & Abundant Dhikr", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When meeting a hostile force, stand firm with immovable physical and moral resolve.\n"
        "- Remember Allah abundantly in the crucible of battle that you may achieve triumph.\n"
        "- Prayer and divine mindfulness are the spiritual foundation of martial courage."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. Pillar 3 & 4: Sincere Obedience & No Dispute", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Obey Allah and His Messenger in every tactical and strategic directive.\n"
        "- 'And do not dispute with one another, lest you falter and your strength depart.'\n"
        "- Internal factional arguing causes courage to collapse and the wind of victory to vanish."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. The Shield of Sabr: Allah is with the Patient", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Endure with unwavering patience; indeed, Allah is with those who are patient.\n"
        "- Panic and internal blame destroy armies and organizations faster than enemy weapons.\n"
        "- Sincere patience under fire draws down divine reinforcement and angelic peace."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. Shun Boastful Ostentation: The March of Quraysh", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Do not be like the Makkan chieftains who marched out with vanity, pride, and singing girls.\n"
        "- Seeking public applause and hindering humanity from the sacred path of Allah.\n"
        "- Arrogant self-exaltation before battle is the guaranteed harbinger of humiliating defeat."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE BETRAYAL OF SATAN, THE FATE OF TYRANTS & TREATY ETHICS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE BETRAYAL OF SATAN, THE FATE OF TYRANTS & TREATY ETHICS",
        "Pillars 11 & 12: Cowardice of Iblis, Death Throes of Oppressors, Changing Inward Blessings & Treaty Ethics",
        "PLATE 06 : SATAN'S RETREAT & TREATY LAWS"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: SATAN'S BETRAYAL & THE DEATH THROES OF TYRANTS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Satan Flees in Terror, Hypocrites' Delusion Taunt & Angels Striking Faces and Backs", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. Satan's Deceptive Boast: 'None Can Overcome You!'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Satan beautified their wicked march: 'None among mankind can defeat you today!'\n"
        "- Pledging false protection and brotherhood in the physical guise of Suraqah.\n"
        "- Seducing oppressors into overconfidence through arrogant imperial delusions."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. The Demon Flees: 'I See What You See Not!'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When the two hosts came in sight, Satan turned on his heels and fled into the desert.\n"
        "- He cried in terror: 'I am free of you! I see what you do not see; I fear Allah!'\n"
        "- The arch-seducer abandons his disciples the moment divine power manifests."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. The Hypocrites' Taunt: 'Their Religion Deluded Them'", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Hypocrites and diseased hearts scoffed at the believers: 'Their faith deluded them!'\n"
        "- Judging reality solely by material weapons, physical numbers, and outward armaments.\n"
        "- But whoever relies upon Allah finds that Allah is Mighty, Wise, and Invincible."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. Striking Faces & Backs: Death of Oppressors", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If you could see when the angels take the souls of those who disbelieved at death.\n"
        "- Striking their faces and their backs: 'Taste the punishment of the burning Fire!'\n"
        "- Just retribution for what their hands forwarded; Allah is never unjust to servants."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: THE LAW OF DECLINE & TREATY INTEGRITY", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Pharaoh's Example, Changing Inward States, Habitual Treaty-Breakers & Open Repudiation", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. The Fate of Pharaoh: Denying Signs of Their Lord", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Like the precedent of Pharaoh's dynasty and those who flourished before them.\n"
        "- They rejected the signs of their Lord; He destroyed them for their persistent sins.\n"
        "- Drowning Pharaoh's hosts; every oppressive civilization meets identical ruin."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. The Law of Social Transformation", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Allah does not change a blessing He bestowed until they change what is in themselves.'\n"
        "- Cultural decline and geopolitical ruin begin with internal moral and spiritual decay.\n"
        "- Preserving divine grace requires active preservation of gratitude, justice, and faith."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. The Worst of Beasts: Habitual Treaty-Breakers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The vilest creatures before Allah are those who disbelieve and will not have faith.\n"
        "- Those with whom you establish a solemn treaty, yet they break their pact every time.\n"
        "- Devoid of moral conscience, honor, or fear of God; prioritizing treason over truth."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. Scattering Aggressors: Disciplining Treachery", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If you encounter them in battle, strike them decisively to disperse those behind them.\n"
        "- Creating profound deterrent examples so that future conspirators take heed.\n"
        "- If treachery is feared from an ally, throw their covenant back with strict equity."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: READINESS FOR DEFENSE, THE INCLINATION TO PEACE & DIVINE AFFECTION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "READINESS FOR DEFENSE, THE INCLINATION TO PEACE & DIVINE AFFECTION",
        "Pillars 13 & 14: Preparing Maximum Strength, Incline to Peace, Miracle of Reconciled Hearts & Spiritual Ratios",
        "PLATE 07 : DEFENSIVE DETERRENCE & PEACE"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: STRATEGIC DETERRENCE & THE MANDATE OF PEACE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Mobilizing Capacity, Archery Deterrence, Incline to Peace & Sufficiency of Allah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Mobilize Maximum Capacity: Preparing Deterrence", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Prepare against them whatever strength and cavalry you are capable of mobilizing.'\n"
        "- The goal is deterrence (Turhiboona bihi): Preventing warmongers from attacking.\n"
        "- The Prophet explained from the pulpit: 'Unquestionably, strength is projectile deterrence.'"
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. Whatever You Spend in God's Cause is Repaid", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Whatever wealth, time, and resources you spend in God's path will be fully repaid.\n"
        "- You shall never be wronged or diminished in divine compensation in both realms.\n"
        "- National defense and communal security are sacred collective obligations (Fard Kifayah)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Mandate of Peace: If They Incline, Incline Unto It", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'And if they incline to peace (Silm), incline unto it, and place your trust in Allah.'\n"
        "- Islam prioritizes reconciliation and peaceful coexistence over endless war.\n"
        "- Sincere readiness to accept peace offers, anchoring trust in Allah's protection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. Deceptive Treaties: Sufficient for You is Allah", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If they intend to deceive you through treaties, Allah is completely sufficient for you.\n"
        "- He is the One who supported you with His sovereign aid and with the sincere believers.\n"
        "- The faithful negotiate from a position of moral integrity, unafraid of betrayal."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: UNIFIED HEARTS & THE RATIOS OF ENDURANCE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Miracle of Reconciled Hearts, Prophetic Rousing & The 1:2 Alleviated Standard", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. The Miracle of Reconciled Hearts (Allafa Baynahum)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'If you had spent all that is in the earth, you could not have united their hearts.'\n"
        "- Century-long blood feuds between Aws and Khazraj healed exclusively by divine grace.\n"
        "- Faith is the only transcendent chemistry that dissolves tribal and racial bigotry."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. Sufficiency of Allah for Prophet & Believers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O Prophet, sufficient for you is Allah and whoever follows you of the believers.'\n"
        "- Numbers and weapons are secondary to divine sufficiency and sincere companionship.\n"
        "- Mobilizing the community with pure trust in the Almighty's unassailable protection."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. Rousing to Battle: The 20 vs 200 Standard", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'O Prophet, rouse the believers to battle: If there are twenty steadfast, they overcome two hundred.'\n"
        "- A spiritual asymmetry ratio of 1:10 rooted in superior moral conviction and understanding.\n"
        "- Disbelievers are a people who comprehend not the transcendent reality of existence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. Divine Alleviation: The 100 vs 200 Standard", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Now Allah has lightened your burden, knowing that within you is human weakness.'\n"
        "- If there are one hundred steadfast, they overcome two hundred (1:2 ratio).\n"
        "- Divine realism acknowledging mortal limits: Retreating before twice one's size is forbidden."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: CAPTIVES OF WAR, THE BOND OF BROTHERHOOD & THE PRIMACY OF KIN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "CAPTIVES OF WAR, THE BOND OF BROTHERHOOD & THE PRIMACY OF KIN",
        "Pillars 15 & 16: The Judgment on Captives, Lawful Spoils, The Pact of Wilayah & The Primacy of Blood Kin",
        "PLATE 08 : BROTHERHOOD & CAPTIVES"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: CAPTIVES OF WAR & DIVINE CONSOLATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Ransoms Rebuked, Consolation for Prisoners, Lawful Tayyibat & Rebuffing Treachery", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. The Prophetic Precedent on Captives of War", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rebuking premature taking of ransoms before securing moral authority upon the earth.\n"
        "- You desired worldly goods (ransoms), while Allah desired the Hereafter and justice.\n"
        "- Were it not for a prior divine decree, severe punishment would have touched you."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. Divine Consolation for Prisoners of War", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Say to the captives in your hands: If Allah knows good in your hearts, He will give you better.'\n"
        "- Granting them better than the ransom taken from them, and forgiving their past sins.\n"
        "- Abbas ibn Abd al-Muttalib and other captives embraced Islam and found immense bounty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. Consuming Lawful & Pure Provisions (Halalan Tayyiba)", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'So consume what you took of spoils as lawful and pure (Halalan Tayyiba).'\n"
        "- Fear Allah in all your dealings; indeed, Allah is Most Forgiving, Ever Merciful.\n"
        "- Sanctifying provisions through adherence to divine limits and social justice."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. Dealing with Treachery: Allah Gave Mastery", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If captives intend betrayal, they had already betrayed Allah prior to the encounter.\n"
        "- So He gave the believers mastery over them; Allah is All-Knowing and All-Wise.\n"
        "- Faith provides the psychological shield against being demoralized by bad faith."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: THE PACT OF WILAYAH & INHERITANCE OF KIN", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Muhajiroon and Ansar, Believers Remaining Behind, Global Counter-Alliance & Ulul-Arham", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. The Sacred Alliance: Muhajiroon & Ansar", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who believed, emigrated, and strived with wealth and lives in the path of Allah.\n"
        "- And those who sheltered and aided them—these are the true allies (Awliya') of one another.\n"
        "- The foundation of the Islamic social order based on shared sacrifice and faith."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. Believers Remaining in the Domain of War", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who believed but did not emigrate: You have no obligation of alliance with them.\n"
        "- Until they make the Hijrah; yet if they seek your aid in religion, you must assist them.\n"
        "- Except against a people with whom you have established a binding diplomatic treaty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. The Global Counter-Alliance & Social Chaos", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those who disbelieve are allies and protectors of one another across the earth.\n"
        "- 'If you do not do so (unite in mutual alliance), there will be turmoil and vast corruption.'\n"
        "- Failing to maintain Islamic solidarity abandons the weak to tyrannical oppression."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. The Primacy of Blood Relations (Ulul-Arham)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Believers who emigrated and struggled together are the believers in ultimate truth.\n"
        "- Concluding decree: Blood relatives (Ulul-Arham) have greater priority in inheritance.\n"
        "- Transitioning from wartime adoptive brotherhood to the permanent legal order of the Shari'ah."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Successfully generated Surah Al-Anfal Master Mindmap PDF: {OUTPUT_PDF} ({os.path.getsize(OUTPUT_PDF)} bytes)")

    # Render PNG previews with pdftoppm
    print("Generating page preview renders...")
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "al_anfal_page")]
    subprocess.run(cmd, check=True)

    # Copy previews to brain directory
    for f in sorted(os.listdir(PREVIEWS_DIR)):
        if f.startswith("al_anfal_page") and f.endswith(".png"):
            src = os.path.join(PREVIEWS_DIR, f)
            dst = os.path.join(brain_dir, f)
            shutil.copy2(src, dst)
            print(f"Copied preview to brain: {dst}")

if __name__ == "__main__":
    build_al_anfal_pdf()
