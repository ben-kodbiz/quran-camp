#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Isra Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "ISRA_MASTER_MINDMAP.pdf")
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

def build_isra_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-ISRA", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: NOCTURNAL ASCENT & CORRUPTION CYCLES
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE CELESTIAL NIGHT JOURNEY & THE TWO CYCLES OF HISTORY",
        "Pillars 1 & 2: Subhana Alladhi Asra, Sacred Al-Aqsa, Bani Isra'il's Two Epochs & Historical Law",
        "PLATE 01 : ASCENT & CYCLES"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE CELESTIAL NIGHT JOURNEY (AL-ISRA)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Cosmic Transcendence, Bodily Ascent & Unity of Sanctuaries", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Doxological Preamble (Subhan)",
              "Opening with Subhan negates all incapacity and limitation from God, shattering human skepticism and establishing that divine omnipotence governs reality above physical laws.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "The Honor of Servitude (Bi-'Abdihi)",
              "Prophet Muhammad ascends the cosmos titled as a humble servant, establishing that perfect servitude to God is humanity's highest rank and guarding against prophetic deification.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "The Bodily & Conscious Ascent",
              "Classical Sunni consensus confirms the journey occurred in both physical body and waking consciousness; had it been a mere dream, Meccan pagans would never have contested it.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Sacred Perimeter (Barakna Hawlahu)",
              "Al-Aqsa is endowed with terrestrial agricultural bounty, fresh waters, and the sacred spiritual legacy of hundreds of monotheistic prophets who walked its holy grounds.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 02: THE TWO PROPHESIED EPOCHS OF CORRUPTION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Cyclical Collapse, Babylonian Scourge & The Iron Law of History", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Decreed Transgressions (Marratayni)",
              "Forewarning Bani Isra'il of two monumental eras where moral corruption and tyrannical arrogance would dismantle their sovereign state and bring civilizational collapse.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Babylonian Incursion (Fa-Jasu)",
              "Formidable conquerors dispatched as instruments of judgment, infiltrating domestic sanctuaries and penetrating homes to execute divine decree upon societal injustice.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "The Second Desecration (Wa'd al-Akhirah)",
              "Renewed corruption triggers hostile invaders who deface dignity, desecrate the Temple sanctuary as occurred before, and destroy what had been patiently erected.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "The Dynamic Universal Law (In 'Uttum 'Udna)",
              "Divine favor is not an ethnic birthright: 'If you return to transgression, We will return to retribution,' establishing an eternal historical axiom for all communities.")

    # ==========================================
    # PLATE 02: UPRIGHT SCRIPTURE & ACCOUNTABILITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE UPRIGHT SCRIPTURE & PERSONAL MORAL LIABILITY",
        "Pillars 3 & 4: Superlative Guidance (Aqwam), The Neck Ledger, Individual Justice & Prophetic Warning",
        "PLATE 02 : GUIDE & ACCOUNTABILITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 03: THE SUPREME BALANCE OF REVELATION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Superlative Path (Aqwam), Glad Tidings & Human Volatility", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Most Upright Guide (Aqwam)",
              "The Qur'an directs humanity to that which is most balanced and upright across theology, legal justice, social harmony, and internal emotional equilibrium.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Dual Cosmic Chronometers: Sun & Moon",
              "Erasing the sign of the night and illuminating the day with radiant light, establishing celestial mechanisms for computing time, seasons, and economic transactions.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "Hasty Supplications & Impulsive Desires",
              "Human impatience causes man to pray for harm in moments of anger just as he prays for good, exposing innate psychological volatility and chronic shortsightedness.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "The Ephemeral Pursuit vs The Eternal",
              "Whoever chases the transient world receives only what is preordained, while those who strive for the eternal world with sincere effort find their strivings appreciated.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: INDIVIDUAL RESPONSIBILITY & SOVEREIGN JUSTICE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Ledger Bound to the Neck, Self-Auditing & Zero Collective Guilt", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "The Moral Collar Fastened (Ta'irahu)",
              "Every person's destiny and deeds are bound inextricably to their own neck like a collar, extinguishing superstitious external omens and fixing ethical accountability.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Unfolded Ledger (Iqra' Kitabak)",
              "On Judgment Day the scroll is unrolled: 'Read your record; your own soul suffices today as an accountant against you,' transforming the individual into their own judge.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Zero Collective Guilt (La Taziru)",
              "Absolute divine equity: no bearer of burdens carries the sin of another; original sin and inherited guilt have no footing in classical monotheistic theology.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Prior Warning Required (Hatta Nab'ath)",
              "Divine retribution is never inflicted without prior notice; punishment is withheld until a messenger establishes clear intellectual and moral proofs upon mankind.")

    # ==========================================
    # PLATE 03: PARENTAL PIETY & SOLIDARITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE ETHICAL DECALOGUE: PARENTAL PIETY & SOLIDARITY",
        "Pillars 5 & 6: Birr al-Walidayn, Forbidding 'Uff', Kinship Rights & The Golden Mean of Wealth",
        "PLATE 03 : FILIAL PIETY & SOLIDARITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 05: THE INVIOLABLE CHARTER OF PARENTAL PIETY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Coupled with Tawhid, The Ban on 'Uff' & The Lowered Wing", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "The Dual Covenant: Tawhid & Parents",
              "Filial devotion is commanded immediately after pure monotheism, elevating honoring parents to the highest moral obligation in interpersonal human ethics.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Absolute Ban on 'Uff'",
              "Criminalizing the slightest audible sigh of impatience, eye-roll, or curt mutter when parents reach old age, demanding total verbal and emotional discipline.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Speech of Nobility (Qawlan Kareema)",
              "Replacing sharpness with honor and tenderness, addressing parents with deferential language that preserves their dignity and soothes physical vulnerability.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "The Lowered Wing of Humility",
              "Inverting the bird metaphor: the adult child lowers the wing of submissive mercy over aging parents, praying for grace as they tenderly nurtured in infancy.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: ECONOMIC SOLIDARITY & ANTI-PRODIGALITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Rights of Kin and Destitute, Condemning Waste & The Balanced Hand", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Right of Kin & Strangers (Haqqah)",
              "Fulfilling the financial claims of relatives, the impoverished, and stranded travelers as an inherent debt of cosmic justice rather than discretionary benevolence.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Brothers of Devils (Ikhwan ash-Shayateen)",
              "Reckless spendthrifts and squanderers are spiritually allied with Satan, corrupting divine economic gifts into instruments of vain ostentation and social disparity.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Gracious Comfort (Qawlan Maysoora)",
              "When unable to extend monetary assistance while awaiting provision, turning away with soothing, gentle words of dignity rather than cold dismissiveness.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "The Golden Mean of Finance",
              "Neither keep your hand chained to your neck in tightfisted parsimony, nor extend it in ruinous extravagance, leaving yourself blameful, destitute, and exhausted.")

    # ==========================================
    # PLATE 04: SANCTITY OF LIFE & COGNITIVE INTEGRITY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE ETHICAL DECALOGUE: LIFE & COGNITIVE TRUTH",
        "Pillars 7 & 8: Outlawing Infanticide, Banning Zina, Orphan Wealth, Straight Scales & Sensory Audit",
        "PLATE 04 : LIFE & SENSORY AUDIT"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 07: SANCTITY OF OFFSPRING, CHASTITY & LIFE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Banning Poverty Infanticide, Sadd al-Dhara'i' in Zina & Due Process", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Banning Child Slaughter (Khashyata Imlaq)",
              "Outlawing infanticide driven by economic panic; the Creator guarantees provision for the child and parent alike, designating child slaughter a grave transgression.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Do Not Approach Zina (La Taqrabu)",
              "Prohibiting not merely the act but all precursors: illicit glances, provocative speech, and seclusion, establishing structural boundaries for societal chastity.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "The Inviolable Soul & Due Process",
              "Forbidding taking life without judicial due process; empowering the victim's heir with legal authority while prohibiting vigilante excess in retribution.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Fiduciary Trust of Orphan Wealth",
              "Approaching the assets of vulnerable orphans solely to protect and enhance their estate until they attain complete intellectual, emotional, and financial maturity.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 08: COMMERCIAL EQUITY & SENSORY COGNITIVE AUDIT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Honest Measures (Al-Qistas), Ban on Conjecture & Modesty in Demeanor", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Straight Scale (Al-Qistas)",
              "Fulfilling measurements with total honesty and weighing with an upright scale, anchoring commercial transactions in transparency and equitable community trust.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Epistemic Integrity (La Taqfu)",
              "Forbidding the pursuit or propagation of unverified rumors, baseless accusations, and subjective conjecture; establishing verification as an intellectual mandate.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Tripartite Sensory Audit",
              "Hearing (As-Sam'), sight (Al-Basar), and the heart (Al-Fu'ad) will all be interrogated; cognitive perception is a moral responsibility, not neutral consumption.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Modesty in Demeanor (La Tamshi Maraha)",
              "Walking upon earth without haughty swagger; human physical fragility can neither penetrate the crust of the earth nor compete with towering mountain peaks.")

    # ==========================================
    # PLATE 05: COSMIC PRAISE & SKEPTIC VEIL
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE COSMIC CHOIR & THE VEIL OVER SKEPTIC HEARTS",
        "Pillars 9 & 10: The Universal Atomic Hymn, Divine Forbearance, The Unseen Barrier & Resurrection",
        "PLATE 05 : COSMIC PRAISE & VEIL"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 09: THE UNIVERSAL HYMN OF CREATION (TASBIH)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Seven Heavens Praising, Inanimate Worship & Divine Forbearance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Universal Choir of Seven Heavens",
              "The seven heavens, the earth, and every being within them hymn the praises of God, transforming the cosmos into an echoing, responsive sanctuary of monotheism.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Liturgy of the Atom (In Min Shay'in)",
              "Not a single atom exists except that it glorifies Him with praise; human sensory limitations fail to decipher the linguistic frequencies of cosmic worship.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Divine Forbearance (Haleeman Ghafoora)",
              "Withholding immediate cosmic retribution despite human arrogance, extending patient respite so souls may awaken and return to divine mercy before the Hour.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Aversion to Pure Monotheism",
              "When Allah alone is invoked, the hearts of skeptics recoil in bitter disdain, exposed by their deep allergy to transcendent singular divine authority.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: THE SPIRITUAL VEIL & RESURRECTION REALITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Invisible Barrier (Hijaban Mastooran), Skeptic Sarcasm & Decayed Bones", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "The Invisible Barrier (Hijaban Mastooran)",
              "When the Qur'an is recited to cynical mockers, an unseen metaphysical barrier falls between them and the truth, insulating the revelation from irreverent comprehension.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Cardiac Coverings & Auditory Locks",
              "Persistent obstinacy encrusts the heart with coverings and afflicts the ears with deafness, rendering spiritual guidance cognitively inaccessible to proud cynics.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "The Sarcasm of Decayed Bones",
              "Skeptics sneer: 'When we are reduced to crumbled bones and dust, shall we truly be resurrected as a new creation?' doubting the sovereign power of the Originator.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Stone, Iron or Inanimate Matter",
              "The decisive divine response: 'Be you stones or iron or whatever seems harder in your breasts!' The One who created you from nothing the first time will recreate you.")

    # ==========================================
    # PLATE 06: HUMAN DIGNITY & IBLIS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "PRIMORDIAL DIGNITY OF ADAM & THE ADVERSARIAL VOW",
        "Pillars 11 & 12: Wa Laqad Karramna, Land and Sea Mastery, Satanic Jealousy & The Shield of Servants",
        "PLATE 06 : HUMAN NOBILITY & IBLIS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: THE PRIMORDIAL NOBILITY OF HUMANITY (KARAMAH)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Universal Honor, Terrestrial & Maritime Mastery & Gracious Sustenance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Inherent Human Dignity (Wa Laqad Karramna)",
              "Bestowing unconditional ontological honor upon every child of Adam, ennobled with an upright stature, articulate intellect, and transcendent moral capacity.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Terrestrial & Maritime Dominance",
              "Subjugating land animals for carriage and enabling vessels to ride oceanic currents, equipping humanity to traverse continents and cultivate global trade.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Wholesome Provisions (At-Tayyibat)",
              "Sustaining humanity with exquisite, wholesome culinary provisions, far elevated above the base, raw foraging instincts of the animal kingdom.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Elevation Above Vast Multitudes",
              "Elevating conscious, moral, obedient human beings above vast ranks of celestial and earthly creation through intentional choice and spiritual struggle.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 12: THE SATANIC AMBUSH & THE FORTRESS OF SERVITUDE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The Vow to Bridle Mankind, Sensory Manipulation & Immunity of Believers", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Spite of Iblis (Ara'aytaka Hadha)",
              "Iblis gazes upon Adam with burning resentment, infuriated that a creation formed of earthen clay was elevated above his primordial fire.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "The Predatory Vow to Bridle (La-Ahtanikanna)",
              "Swearing to bridle Adam's progeny like beasts of burden, pulling their instincts into degradation and moral servitude except for a dedicated minority.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Four-Fold Assault Strategy",
              "Startling with seductive voice, summoning horsemen and foot soldiers, and infiltrating domestic finances and offspring with false promises and vain delusions.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "The Fortress of Sincere Servants",
              "The divine guarantee: Satan possesses zero authority over sincere worshippers; Allah's guardianship provides an impenetrable fortress against every ambush.")

    # ==========================================
    # PLATE 07: THE SPIRIT & TAHAJJUD
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE ENIGMA OF THE SPIRIT & THE NIGHT VIGIL",
        "Pillars 13 & 14: The Secret of Al-Ruh, Qur'anic Shifa', Tahajjud Vigil & The Praised Station",
        "PLATE 07 : SPIRIT & TAHAJJUD"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 13: THE SECRET OF THE SOUL & SCRIPTURAL HEALING", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Realm of Divine Command (Amr), Limited Knowledge & Curative Revelation", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Transcendent Soul (Al-Ruh Min Amr Rabbi)",
              "The soul belongs to the divine realm of command, defying mechanistic material reductionism and preserving the divine mystery at the core of human consciousness.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Scarcity of Human Knowledge",
              "'You have not been granted of knowledge except a little,' humbling human scientific pride and reminding mankind of the vast horizons of divine omniscience.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Curative Healing & Mercy (Shifa')",
              "The Qur'an actively dissolves ideological skepticism, moral corruption, and existential anguish for believers, while unjust rejectors reap only loss.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Human Inconstancy in Affluence & Trial",
              "When showered with blessings, man turns away haughtily; yet when adversity brushes him, he collapses into despair, exposing internal spiritual fragility.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: THE NIGHT VIGIL & THE STATION OF PRAISE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Waking for Tahajjud, Al-Maqam al-Mahmood & The Triumphant Truth", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Diurnal Prayer Rhythms (Aqim as-Salah)",
              "Establishing prayer at the sun's decline until the depth of night, culminating in the dawn recitation witnessed directly by assembled angelic retinues.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "The Solitary Vigil of Tahajjud",
              "Casting off sleep in the stillness of deep night as a voluntary ascent, conversing intimately with God and forging unshakeable spiritual steadfastness.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Praised Station (Maqaman Mahmooda)",
              "The promise of resurrection into the Station of Praise, authenticated as the Prophet's supreme universal intercession when all creation glorifies his noble standing.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "The Evaporation of Falsehood (Zahooqa)",
              "The supplication of righteous entry and exit, and the immortal proclamation: 'Truth has come and falsehood has vanished; falsehood is ever bound to perish.'")

    # ==========================================
    # PLATE 08: NINE SIGNS & PROSTRATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE NINE PROOFS, TEARS OF HUMILITY & CLOSING DOXOLOGY",
        "Pillars 15 & 16: Musa's Nine Signs, Pharaoh's Fall, Spaced Revelation, Weeping Chins & The Final Hymn",
        "PLATE 08 : NINE SIGNS & TEARS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 15: MUSA'S SIGNS & THE COLLAPSE OF TYRANNY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Nine Manifest Proofs, Pharaoh's Slander, The Drowning Abyss & Spaced Text", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "The Nine Clear Proofs of Musa",
              "Cosmic and legislative signs delivered to Pharaoh, validating divine ambassadorship and demonstrating God's sovereign command over natural phenomena.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "The Tyrant's Projection (Mashoora)",
              "Pharaoh haughtily dismisses Musa as a bewitched madman, projecting internal psychological blindness onto the bearer of clear divine enlightenment.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Engulfing Abyss of Pharaoh",
              "Attempting to expel the believers from the land, the tyrant and his legions are drowned in the sea, proving that authoritarian empires cannot outlast God.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Spaced Transmission (Qur'anan Faraqnahu)",
              "Revealing the Qur'an in piecemeal intervals over decades, allowing human hearts to contemplate, absorb, and institutionalize its truths gradually.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: TEARS IN PROSTRATION & THE CLOSING DOXOLOGY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Prostration of the Learned, Unity of Names & The Supreme Takbir", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Weeping Upon the Chins (Yakhirroona)",
              "True scholars collapse upon their chins in prostration when hearing the revelation, tears streaming down their faces as humble devotion deepens.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Unity of Names (Allah & Ar-Rahman)",
              "Whether calling upon Allah or The Most Merciful, to Him belong all Most Beautiful Names, dispelling polytheistic confusion and affirming single essence.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Balanced Voice in Prayer",
              "Neither shouting your prayer aloud to provoke hostility, nor whispering in silence, but seeking a serene, harmonious middle pathway of dignity.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Closing Majestic Doxology",
              "Praise belongs to Allah who has taken neither offspring nor partner in dominion, nor needed any ally out of weakness; and exalt Him with supreme majesty!")

    pdf.save(OUTPUT_PDF)
    print(f"Generated Vector PDF at: {OUTPUT_PDF}")

    # Generate PNG Previews
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/isra_page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Rendered PNG previews in: {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src_prev = f"{PREVIEWS_DIR}/isra_page-{i}.png"
        dst_brain = os.path.join(brain_dir, f"isra_page-{i}.png")
        if os.path.exists(src_prev):
            shutil.copyfile(src_prev, dst_brain)
            print(f"Copied {src_prev} to {dst_brain}")

if __name__ == "__main__":
    build_isra_pdf()
