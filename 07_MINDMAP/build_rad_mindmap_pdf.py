#!/usr/bin/env python3
"""
Huurs Studio - Surah Ar-Ra'd Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "RAD_MASTER_MINDMAP.pdf")
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

def build_rad_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AR-RA'D", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PAGE 1: THE INVISIBLE PILLARS OF THE COSMOS & THE DIVERSITY OF CREATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE INVISIBLE PILLARS OF THE COSMOS & THE DIVERSITY OF CREATION",
        "Pillars 1 & 2: Heavens Without Pillars, Celestial Mechanics & The Miracle of One Water",
        "PLATE 01 : COSMOLOGY & BOTANY"
    )

    # Column 1: Pillar 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 1: HEAVENS WITHOUT VISIBLE PILLARS & CELESTIAL MECHANICS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Bighayri 'Amad, Precise Astronomical Orbits & Terrestrial Mountain Anchors", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("1. The Disjointed Letters & Truth of Revelation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Opening with Alif-Lam-Meem-Ra: Signs of the verified scripture from the Lord.\n"
        "- The tragic human paradox: Divine truth revealed, yet majority persist in denial.\n"
        "- Establishing the divine origin of revelation as the immutable standard of reality."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("2. The Celestial Canopy Without Visible Pillars", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Raising the vast heavens without any visible physical columns (Bighayri 'Amadin).\n"
        "- Cosmic equilibrium, gravitational tension, and sovereign divine governance.\n"
        "- Establishing sovereignty above the Throne (Istawa 'alal-'Arsh) in supreme majesty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("3. The Mathematical Cycles of Sun and Moon", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Subjugating the sun and moon to traverse calibrated orbits (Kullun yajree).\n"
        "- Appointed terms (Ajalim Musamma) governing cosmic physics and celestial time.\n"
        "- Directing all cosmic affairs (Yudabbirul-amr) to grant certainty in resurrection."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("4. Terrestrial Anchors, Rivers & Conjugate Pairs", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Spreading the continental plates, stabilized by immovable mountains (Rawasiya).\n"
        "- Flowing river arteries and every botanical species created in conjugate pairs.\n"
        "- Draping the veil of night over the day in unbroken astronomical equilibrium."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 2
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 2: ADJACENT PLOTS OF SOIL & THE MIRACLE OF ONE WATER", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Qita'un Mutajawirat, Clustered Date Palms & The Demise of Materialism", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("5. The Microcosm of Adjacent Soil Plots", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Contiguous tracts of agricultural soil (Qita'un Mutajawirat) side by side.\n"
        "- Sharing identical geography, solar radiation, minerals, and atmospheric climate.\n"
        "- Displaying radical variations in botanical suitability, output, and flora."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("6. Clustered Palms & The Single Hydrological Source", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Vineyards, grain, and date palms growing clustered (Sinwan) or solitary.\n"
        "- Irrigated by the exact same chemical water (Yusqa bi-ma'in wahid).\n"
        "- Conclusive empirical proof that nature is not a blind mechanical engine."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("7. The Sovereign Determination of Flavors & Forms", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Causing one plant to excel others in taste, texture, aroma, and medicine.\n"
        "- Refuting accidental materialism: identical inputs producing diverse outputs.\n"
        "- The manifestation of an intentional choosing Creator (Al-Fa'il al-Mukhtar)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("8. Empirical Signs for the People of Reason", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Closing signature: Signs for a people who utilize intellect (Li-qawmin ya'qiloon).\n"
        "- Demanding rational humility before the intricate engineering of creation.\n"
        "- Transition from empirical observation of nature to spiritual certitude in God."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 2: RESURRECTIVE DOUBTS, THE HIDDEN SOUL & ANGELIC GUARDIANS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "RESURRECTIVE DOUBTS, THE HIDDEN SOUL & ANGELIC GUARDIANS",
        "Pillars 3 & 4: Skepticism of the Dust, Divine Mercy, Omniscience & The Mu'aqqibat",
        "PLATE 02 : RESURRECTION & GUARDS"
    )

    # Column 1: Pillar 3
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 3: SKEPTICISM OF THE DUST & MERCY ALONGSIDE RETRIBUTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Astonishing Cynicism, Collars of Blindness & The Balance of Forgiveness", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("9. The Baffling Denial of Bodily Resurrection", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Astonishment at the deniers: accepting cosmic creation while rejecting re-creation.\n"
        "- The cynical question: 'When we become dust, will we be in a new creation?'\n"
        "- Exposing the irrationality of doubting the Maker who initiated primal existence."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("10. Iron Collars Around the Skeptical Neck", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Spiritual diagnosis: obstinate denial shackles the heart in metaphysical chains.\n"
        "- Iron collars (Aghlal) encircling their necks in this world and the Hereafter.\n"
        "- Destined for prolonged alienation from divine light as dwellers of the Fire."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("11. The Arrogant Demand to Hasten Retribution", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cynics insolently demanding the swift arrival of doom before seeking good.\n"
        "- Forgetting the historical ruins of vanished societies (Al-Mathulat).\n"
        "- Demonic audacity mocking the patient forbearance of the Almighty."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("12. Vast Forgiveness Tempered by Severe Justice", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine attribution: Possessor of boundless forgiveness despite human wrongdoing.\n"
        "- Simultaneously severe in ultimate penalty (Lashadeedu al-'iqab) for the arrogant.\n"
        "- The essential Sunni balance between awe-inspired vigilance and radiant hope."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 4
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 4: THE OPEN AND SECRET WORD & THE GUARDIAN MU'AQQIBAT", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Role of Warners, Measurements of the Womb & The Angelic Escort", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("13. The Demands for Spectacular Supernatural Wonders", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Secular complaints: 'Why is not a physical wonder sent down from his Lord?'\n"
        "- Defining prophetic scope: You are solely a warner (Innama anta mundhir).\n"
        "- Every civilization and historical epoch receives an authorized divine guide."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("14. Omniscience Over Every Womb & Precise Calibration", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Complete knowledge of what every female conceives across all biological life.\n"
        "- Auditing gestation that falls short or exceeds in days, viability, and health.\n"
        "- Everything in existence calibrated to an exact predetermined measure (Bi-miqdar)."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("15. The Identity of Whispered and Shouted Words", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Equal before His hearing: the whisperer at midnight and the daytime orator.\n"
        "- Knower of the unseen and seen, the Transcendent, the Most High (Al-Kabeer).\n"
        "- Total destruction of hypocrisy; no thought can hide in the folds of the breast."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("16. The Alternating Guardian Angels (Al-Mu'aqqibat)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Successive ranks of angels shadowing every human before and behind.\n"
        "- Shielding from undecreed perils by the sovereign command of Allah (Min amrillah).\n"
        "- Recording daily deeds and stepping aside only when the divine decree arrives."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 3: THE SOCIOLOGICAL LAW OF CHANGE & THE THUNDER HYMN
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "THE SOCIOLOGICAL LAW OF CHANGE & THE THUNDER HYMN",
        "Pillars 5 & 6: The Axiom of Internal Transformation, The Sentient Thunder & Lightning",
        "PLATE 03 : TRANSFORMATION & THUNDER"
    )

    # Column 1: Pillar 5
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=ROSE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 5: THE AXIOM OF INTERNAL TRANSFORMATION (HATTA YUGHAYYIROO)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Societal Renewal, Moral Preconditions & The Irresistibility of Decrees", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=ROSE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("17. The Master Axiom of Sociological Transformation", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah does not alter a people's condition until they change what is in themselves.\n"
        "- Linking outer political/economic fortunes directly to internal moral health.\n"
        "- The foundation of Qur'anic philosophy: internal reform precedes external renewal."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("18. Moral Rupture as Cause of Civilizational Fall", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine grace is baseline; blessings are never withdrawn without moral corruption.\n"
        "- External subjugation and decay are symptoms of abandoned sacred covenants.\n"
        "- Mere political restructuring cannot revive a community corrupted from within."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("19. The Irresistible Momentum of Decreed Trial", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- When Allah wills adversity upon an unrepentant people, none can turn it away.\n"
        "- No force, fortress, or treaty can delay the consequence of persistent evil.\n"
        "- Demolishing false securities built upon material weapons and pride."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("20. Total Absence of Any Protecting Patron", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Humanity possesses no guardian patron (Wali) against sovereign divine decrees.\n"
        "- Stripping humanity of arrogance and directing all reliance back to God.\n"
        "- The urgency of immediate collective repentance before the threshold is crossed."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 6
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 6: THE HYMN OF THE THUNDER & THE PHYSICS OF LIGHTNING", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Sentient Glorification, Fear and Hope & Thunderbolts Striking Disputants", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("21. Lightning Manifested in Fear and Hope", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Showing lightning simultaneously generating terror (Khawf) and hope (Tama').\n"
        "- Fear of devastating strikes and fires; hope for life-reviving agrarian rain.\n"
        "- Assembling towering storm clouds laden with millions of tons of freshwater."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("22. The Sentient Praise of the Atmospheric Thunder", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The cosmic reality: Thunder hymns His praise (Wa yusabbihu ar-ra'du bi-hamdih).\n"
        "- Heavenly angels trembling in perpetual awe and reverence of the Creator.\n"
        "- Stripping nature of secular sterility; the elements are sentient worshipers."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("23. Precision Thunderbolts Striking Disputants", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Discharging lightning bolts (Sawa'iq) hitting targets with decreed accuracy.\n"
        "- Striking while obstinate humans arrogantly debate the existence of Allah.\n"
        "- Historical destruction of blasphemous plotters by instantaneous cosmic fire."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("24. Severe in Unfathomable Cosmic Might (Shadeed al-Mihal)", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Closing divine attribute: Allah is invincible in cosmic power (Shadeedul-Mihal).\n"
        "- Shattering human illusions of autonomous strength and technical supremacy.\n"
        "- The call to awe-inspired veneration before the Lord of thunder and storm."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 4: THE PARABLE OF THE FOAM & THE ENDURING TRUTH
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE PARABLE OF THE FOAM & THE ENDURING TRUTH",
        "Pillars 7 & 8: The Parched Hands, The Flash Flood & The Vanishing Scum",
        "PLATE 04 : THE PARABLE OF FOAM"
    )

    # Column 1: Pillar 7
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 7: THE SUPPLICATION OF THE PARCHED & FUTILITY OF FALSE GODS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Da'wat al-Haqq, Phantom Hands & The Universal Cosmic Prostration", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("25. The True Invocation Belonging to Him Alone", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Unto Him alone belongs the supplication of truth (Lahu da'watul-haqq).\n"
        "- Petitioning false lords yields only hollow echoes and absolute cosmic silence.\n"
        "- True prayer connects the mortal creature directly to the living Creator."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("26. The Parable of the Parched Outstretched Hands", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- False idols are like water to one stretching hands from afar to reach his lips.\n"
        "- The tragic physics of delusion: the water will never reach his parched mouth.\n"
        "- Illustrating the utter impotence of polytheism and secular self-worship."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("27. Invocations of Deniers Lost in Cosmic Futility", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The rituals and prayers of deniers wander in aimless delusion (Fee dalal).\n"
        "- Effort without Tawhid is empty toil dissipating into spiritual nothingness.\n"
        "- True efficacy in worship requires alignment with divine command and reality."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("28. The Universal Cosmic Prostration: Willing and Unwilling", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Unto Allah prostrates everything in the heavens and earth, willingly or by law.\n"
        "- Believers prostrate in joyful love; nature submits to unalterable physical decrees.\n"
        "- Lengthening shadows bowing low across dawn and twilight in perpetual homage."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 8
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 8: THE FLASH FLOOD, SMELTED ORE & THE SCUM THAT VANISHES", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Valleys of Revelation, The Floating Slag & That Which Benefits Humanity", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("29. Rains Descending in Calibrated Valleys", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Water sent from sky, flowing through ravines according to measure (Bi-qadariha).\n"
        "- The valleys represent human hearts: grand hearts hold oceans, small hold drops.\n"
        "- Pure revelation descending from above to revive dead spiritual lands."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("30. The Swelling Froth of the Flash Flood", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The rushing torrent carrying bubbling, floating, swelling foam (Zabadan rabiya).\n"
        "- Foam represents doubts and base desires bubbling to the surface during trial.\n"
        "- Dramatic, bloated, and prominent on top, yet completely devoid of substance."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("31. Smelted Metallic Ore & The Surface Slag", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Parallel metaphor: Gold, silver, and iron melted in furnaces for ornaments or tools.\n"
        "- The intense heat separating the precious metal from worthless dross and scum.\n"
        "- The crucible of adversity revealing who is pure gold and who is empty dross."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("32. Scum Dissipates & The Beneficial Remains Rooted", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The foam is cast away into nothingness (Fa-amma az-zabadu fayadh-habu jufaa').\n"
        "- That which benefits humanity remains anchored in the earth (Fayamkuthu fil-ard).\n"
        "- Eternal law: Falsehood makes temporary noise; truth remains permanently rooted."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 5: THE EIGHT HALLMARKS OF THE PEOPLE OF INTELLECT (ULUL-ALBAB)
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE EIGHT HALLMARKS OF THE PEOPLE OF INTELLECT (ULUL-ALBAB)",
        "Pillars 9 & 10: Covenant Fidelity, Cosmic Connectivity, Sacred Reverence & Sabr",
        "PLATE 05 : HALLMARKS OF INTELLECT"
    )

    # Column 1: Pillar 9
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 9: FULFILLING THE COVENANT & UNITING WHAT ALLAH COMMANDED", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sight vs. Blindness, Unbroken Treaties & Maintaining Sacred Ties", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("33. The Epistemic Contrast: Seeing vs. Blindness", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Can the one who recognizes revelation as truth be equated to the blind?\n"
        "- Spiritual vision is an intellectual awakening; denial is self-inflicted blindness.\n"
        "- Only the possessors of profound intellect take heed (Innama yatadhakkaru)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("34. Attribute One: Unbroken Fidelity to Covenants", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Fulfilling the primordial covenant of Tawhid and all sacred earthly contracts.\n"
        "- Refusing to violate treaties (La yanqudoon al-meethaq) for temporal gain.\n"
        "- Absolute trustworthiness and integrity as the foundational hallmark of faith."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("35. Attribute Two: Joining What Allah Commanded Joined", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Preserving the ties of blood kinship, brotherhood, and community cohesion.\n"
        "- Uniting faith with ethical conduct; refusing sectarian fracturing and strife.\n"
        "- Active peacemaking and reconciliation across fractured human relationships."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("36. Attribute Three: Sacred Reverence for the Lord", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Living in profound reverential awe (Khashyah) of the majesty of their Lord.\n"
        "- Internalizing divine greatness so deeply that sinful impulses dissolve.\n"
        "- Reverence that transforms casual worship into deep, trembling devotion."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 10
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 10: REVERENCE, DREAD OF RECKONING & STEADFAST ENDURANCE", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Severe Reckoning, Patience for the Divine Face & The Eight Pillars", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("37. Attribute Four: Dread of the Severe Reckoning", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Maintaining active vigilance regarding the Day of Judgment (Soo' al-Hisab).\n"
        "- Auditing personal deeds, speech, and transactions before the cosmic audit.\n"
        "- Fear of standing exposed before the Creator with unpaid moral debts."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("38. Attribute Five: Patience Exclusively for God's Face", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Enduring adversity, illness, and persecution seeking solely God's Face.\n"
        "- Free of desire for human praise, public victimhood, or temporal sympathy.\n"
        "- Patient persistence in doing good even when surrounded by ingratitude."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("39. Attribute Six: Establishing Regular Prayer", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Structuring daily existence around the rhythmic pillars of prayer (As-Salah).\n"
        "- Approaching prayer not as a lifeless burden, but as celestial ascension.\n"
        "- Generating spiritual power that shields against moral degradation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("40. Attribute Seven: Secret and Public Charity", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Spending from divine sustenance both secretly to protect dignity and openly.\n"
        "- Open charity to inspire communal solidarity; secret charity for pure sincerity.\n"
        "- Liberating the heart from hoarding wealth and materialistic avarice."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 6: THE ETHICS OF VIRTUE & THE WELCOME OF THE ANGELS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE ETHICS OF VIRTUE & THE WELCOME OF THE ANGELS",
        "Pillars 11 & 12: Repelling Evil with Good, The Eternal Abode & The Angelic Greeting",
        "PLATE 06 : VIRTUE & SALAM"
    )

    # Column 1: Pillar 11
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 11: PRAYER, GENEROSITY & OVERCOMING EVIL WITH GOOD", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Moral Alchemy, The Ultimate Abode & The Curse of Covenant-Breakers", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("41. Attribute Eight: Repelling Evil With Proactive Goodness", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The pinnacle of moral refinement: Meeting malice with benevolent grace.\n"
        "- Repelling harsh insults with gentle wisdom and cruelty with active forgiveness.\n"
        "- Transforming bitter adversaries into intimate, loyal allies through nobility."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("42. The Eternal Inheritance of the Ultimate Abode", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Those embodying these eight hallmarks inherit the final home ('Uqba ad-Dar).\n"
        "- Worldly struggle crowned with permanent celestial dignity and sovereign peace.\n"
        "- The ultimate triumph of moral rectitude over transient worldly power."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("43. The Curse Upon Breakers of Covenants", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Severe warning: Those who violate covenants and sever sacred bonds of kinship.\n"
        "- Sowing systemic corruption in the earth reaps divine expulsion (Al-La'nah).\n"
        "- Inheriting the wretched home of misery and eschatological ruin (Soo'u ad-dar)."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("44. Provision Expanded and Constricted by Divine Will", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah expands provision for whom He wills and restricts it according to wisdom.\n"
        "- The foolishness of exulting in worldly wealth; earthly life is mere trinkets (Mata').\n"
        "- Material abundance is a moral examination, never proof of divine favor."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 12
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 12: THE ABODE OF ULTIMATE DESTINY & THE ANGELIC GREETING", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Gardens of Eden, Righteous Families Reunited & The Eternal Salam", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("45. Gardens of Eden Entered in Righteous Kinship", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Entering perpetual Gardens of Eden (Jannatu 'Adn) in everlasting splendor.\n"
        "- Reunited with righteous parents, spouses, and children in unbroken companionship.\n"
        "- Divine grace elevating family members to share the highest celestial ranks."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("46. Angels Entering From Every Gateway", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Majestic angels arriving from every gate of Paradise to greet the persevering.\n"
        "- Divine ceremony honoring the quiet, unsung endurance of worldly trials.\n"
        "- Moving from the realm of testing into the palace of eternal celebration."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("47. Peace Upon You for That Which You Endured", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The eternal greeting: 'Salamun 'alaykum bima sabartum, fani'ma 'uqba ad-dar.'\n"
        "- Peace bestowed upon you because of your patient steadfastness in the world.\n"
        "- How magnificent and glorious is the final celestial home of the persevering."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("48. The Permanent Immunity of the Patient Soul", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Complete erasure of fatigue, sickness, defamation, anxiety, and heartbreak.\n"
        "- Settled in absolute security beneath the Throne of the Most Merciful.\n"
        "- The realization that a lifetime of patient endurance was worth every second."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 7: THE TRANQUILITY OF DHIKR & THE COSMIC RECITATION
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE TRANQUILITY OF DHIKR & THE COSMIC RECITATION",
        "Pillars 13 & 14: Rest for Anxious Hearts, Tooba & The Qur'an Moving Mountains",
        "PLATE 07 : TRANQUILITY & SCRIPTURE"
    )

    # Column 1: Pillar 13
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=GOLD, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 13: WORLDLY DELUSION & THE ANTIDOTE OF DHIKRULLAH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Demands for Signs, Guidance for the Repentant & Ala Bi-Dhikrillah", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=GOLD, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("49. Secular Demands for Spectacular Sensory Signs", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Cynics repeating: 'Why is not an external physical sign sent down to him?'\n"
        "- Blindness to the millions of signs woven into biology, clouds, and astronomy.\n"
        "- Those with hardened hearts would deny truth even if skies rained wonders."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("50. Divine Guidance Bestowed Upon the Repentant", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah leaves to stray those who deliberately choose arrogance and pride.\n"
        "- Guiding directly toward Himself whoever turns back in humble repentance (Anab).\n"
        "- The sincere turning of the heart is the sole prerequisite for illumination."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("51. The Anchor of Rest: Ala Bi-Dhikrillahi Tatma'inn", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The universal medicine: 'Unquestionably, by the remembrance of Allah hearts rest.'\n"
        "- The existential ache of humanity can never be satisfied by temporal pleasures.\n"
        "- Intrinsic peace arrives only when the soul connects to its uncreated Lord."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("52. Tooba: The Celestial Tree & Splendid Return", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- For those who believe and work righteousness: Tooba and a glorious homecoming.\n"
        "- Tooba is celestial delight, spiritual sweetness, and a grand tree in Paradise.\n"
        "- The final destination that transforms all worldly hardships into sweet memory."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 14
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=CYAN, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 14: TOOBA FOR THE STEADFAST & RECITATION MOVING MOUNTAINS", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Continuity of Revelation, The Ultimate Scripture & Disasters on the Horizon", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=CYAN, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("53. The Prophet Sent Among Preceding Civilizations", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Sending the Messenger ﷺ to a nation preceded by vanished world empires.\n"
        "- Reciting what is revealed while deniers persist in ingratitude to Ar-Rahman.\n"
        "- Reaffirming the oneness of God and total reliance upon the Divine Sustainer."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("54. The Hypothetical Recitation Moving Mountains", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- If any scripture could make mountains march, tear earth, or speak to the dead...\n"
        "- The Qur'an possesses supreme spiritual potency exceeding all ancient signs.\n"
        "- Rejection is due to rebellious pride, never to lack of scriptural majesty."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("55. The Sovereignty of the Entire Cosmic Affair", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- 'Nay, unto Allah belongs the entire affair wholly' (Bal lillahil-amru jamee'an).\n"
        "- If Allah had willed, He could have guided all humanity without exception.\n"
        "- Preserving human moral choice as the divine purpose of earthly existence."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("56. Calamities Circling the Dwellings of Deniers", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Catastrophic strikes (Qari'ah) continuously descending near homes of the unjust.\n"
        "- Historical and geopolitical warnings unfolding until the final promise arrives.\n"
        "- Allah never fails in His solemn, declared appointment with human history."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # =========================================================================
    # PAGE 8: THE SOVEREIGNTY OF DECREES & THE CONCLUSIVE WITNESS
    # =========================================================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE SOVEREIGNTY OF DECREES & THE CONCLUSIVE WITNESS",
        "Pillars 15 & 16: Messengers Mocked, The Mother of the Book & The Conclusive Witness",
        "PLATE 08 : DECREES & WITNESS"
    )

    # Column 1: Pillar 15
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=PURPLE, line_width=1.2)
    pdf.rect(c1_x, c1_y + c1_h - 36, c1_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 15: MESSENGERS BEFORE YOU & THE MOTHER OF THE BOOK", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Historical Consolation, The Overseer of Souls & Erasing Decrees", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x, c1_y + c1_h - 36, c1_x + c1_w, c1_y + c1_h - 36, stroke_rgb=PURPLE, line_width=0.8)

    y_c = c1_y + c1_h - 48
    pdf.text("57. The Mockery of Messengers in Human History", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Divine comfort: Messengers before you were ridiculed by arrogant contemporaries.\n"
        "- Respite was granted to mockers until divine justice seized them with rigor.\n"
        "- Steadfast patience in the face of modern skepticism and online mockery."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 118
    pdf.text("58. He Who Stands Sovereign Over Every Single Soul", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Rhetorical challenge: Is He who watches every deed comparable to false idols?\n"
        "- Naming hollow idols that have no power to create, sustain, or resurrect.\n"
        "- Revealing the absurdity of equating created objects with the Eternal Maker."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 188
    pdf.text("59. Erasing and Confirming: The Mother of the Book", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Allah erases what He wills and confirms in the angel records (Yamhoo wa yuthbit).\n"
        "- With Him is the immutable Preserved Tablet (Ummul-Kitab / Lawh Mahfooz).\n"
        "- Supplication and ties of kinship altering angelic scrolls by divine decree."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c1_y + c1_h - 258
    pdf.text("60. Retraction of the Land at Its Outer Borders", c1_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Do they not observe the divine power curtailing the land from its borders?\n"
        "- Civilizations shrinking, empires collapsing, and truth steadily expanding.\n"
        "- Allah decrees with absolute authority; none can overturn His sovereign verdict."
    )
    pdf.paragraph(t, c1_x + 12, y_c - 10, c1_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    # Column 2: Pillar 16
    pdf.rect(c2_x, c2_y := c1_y, c2_w, c1_h, fill_rgb=NAVY_CARD, stroke_rgb=EMERALD, line_width=1.2)
    pdf.rect(c2_x, c2_y + c1_h - 36, c2_w, 36, fill_rgb=NAVY_ELEVATED)
    pdf.text("PILLAR 16: RETRIBUTION ON THE HORIZON & THE SUFFICIENCY OF ALLAH", c2_x + 12, c2_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Plots Decimated, The Charge of Inauthenticity & The Scriptural Scholars", c2_x + 12, c2_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x, c2_y + c1_h - 36, c2_x + c2_w, c2_y + c1_h - 36, stroke_rgb=EMERALD, line_width=0.8)

    y_c = c2_y + c1_h - 48
    pdf.text("61. The Conspiracies of Antiquity Decimated", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Past tyrannies engineered vast conspiracies against divine messengers.\n"
        "- Yet all plotting belongs solely to Allah; He knows what every soul earns.\n"
        "- Deniers will soon discover who inherits the final, triumphant home."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 118
    pdf.text("62. The Cynics' Cry: 'You Are Not a Messenger!'", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The stubborn rejection of tribal elites: 'Lasta mursala' (You are no prophet).\n"
        "- Accusing truth-bearers of fabrication when truth challenges corrupt power.\n"
        "- Prophetic serenity remaining unshaken by insults and political smear campaigns."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 188
    pdf.text("63. The Supreme Sufficiency of Divine Testimony", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- The prophetic response: 'Sufficient is Allah as a witness between me and you.'\n"
        "- Divine validation renders human rejection entirely inconsequential and hollow.\n"
        "- Resting in the absolute certitude of the Creator's eternal testimony."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    y_c = c2_y + c1_h - 258
    pdf.text("64. The Conclusive Testimony of Scriptural Scholars", c2_x + 12, y_c, font="F2", size=8, rgb=WHITE)
    t = (
        "- Concluding tribute: 'And those who possess knowledge of the Scripture.'\n"
        "- Authentic scholars of Torah and Gospel recognizing the signs of Prophethood.\n"
        "- Sealing Surah Ar-Ra'd with the immutable harmony of divine revelation."
    )
    pdf.paragraph(t, c2_x + 12, y_c - 10, c2_w - 24, line_height=10.5, font="F1", size=6.8, rgb=TEXT_MUTED)

    pdf.save(OUTPUT_PDF)
    print(f"Master Mindmap PDF successfully written to: {OUTPUT_PDF}")

    # Generate preview images for each plate
    print("Generating preview PNGs via pdftoppm...")
    cmd = [
        "pdftoppm",
        "-png",
        "-r", "150",
        OUTPUT_PDF,
        os.path.join(PREVIEWS_DIR, "rad_page")
    ]
    subprocess.run(cmd, check=True)

    # Copy to brain dir
    for i in range(1, 9):
        src_pattern = os.path.join(PREVIEWS_DIR, f"rad_page-{i}.png")
        if not os.path.exists(src_pattern):
            src_pattern = os.path.join(PREVIEWS_DIR, f"rad_page-0{i}.png")
        if os.path.exists(src_pattern):
            dst = os.path.join(brain_dir, f"rad_page-{i}.png")
            shutil.copyfile(src_pattern, dst)
            print(f"Copied {src_pattern} -> {dst}")

if __name__ == "__main__":
    build_rad_pdf()
