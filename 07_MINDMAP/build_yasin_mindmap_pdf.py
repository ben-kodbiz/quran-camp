#!/usr/bin/env python3
"""
Huurs Studio - Surah Ya-Sin Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 10 Plates • 20 Pillars • 80 Nodes
Strict Brand_Visual_System.md & Absolute Copyright Insulation
The Epistemic Oath, The Outskirts Martyr, Cosmic Choreography, The Sovereign Blast & "Kun Fayakun"
"""

import os, sys, subprocess, shutil
sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "YASIN_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews_yasin")
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

def build_yasin_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH YA-SIN", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
        # Badges
        pdf.rect(w - 130, h - 32, 98, 20, fill_rgb=NAVY_ELEVATED, stroke_rgb=BORDER_MUTED, line_width=0.8)
        pdf.text(f"PAGE {pnum:02d} / {total_pages:02d}", w - 116, h - 26, font="F2", size=9, rgb=GOLD)

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
        pdf.text("HUURS KNOWLEDGE SYSTEMS  *  AUTHENTIC SUNNI SOURCE DISCIPLINE", 32, 16, font="F1", size=7.2, rgb=TEXT_MUTED)
        pdf.text("SURAH YA-SIN  *  ULTRA-DEEP 10-PLATE EDITION  *  READ. REFLECT. RETURN.", w - 355, 16, font="F2", size=7.0, rgb=GOLD_LIGHT)

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
    # PLATE 01: EPISTEMOLOGY, OATHS & COGNITIVE VEILS (Ayat 1-12)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 10,
        "EPISTEMOLOGY, PROPHETIC OATH & COGNITIVE VEILS",
        "Pillars 01 & 02: Infallible Epistemic Oath, Arrogant Shackles, Dual Barriers & Footsteps Recorded",
        "PLATE 01 : PROPHETIC OATH"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE OATH OF YA-SIN & STRAIGHT PATH", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("The Disconnected Letters, Al-Qur'an al-Hakeem & Apostolic Mandate", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Disconnected Letters (Ya-Sin)",
              "Mystical opening letters addressing the Prophet as the pinnacle of humanity ('O Man!') and establishing transcendent divine origins.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Oath by the Wise Qur'an (Al-Hakeem)",
              "Wal-Qur'ani al-Hakeem: divine oath by the Book infused with decisive wisdom, confirming the Prophet is on Sirat al-Mustaqeem.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Mandate to an Unwarned People",
              "Li-tundhira qawman ma undhira aba'uhum: dispatched with revelation to awaken a community whose ancestors lacked prophetic warning.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "The Eternal Decree Realized",
              "Laqad haqqa al-qawlu 'ala aktharihim: the decree of justice is verified upon those whose obstinate choices permanently sealed their rejection.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: SOMATIC BLINDNESS & DYNAMIC REGISTERS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Iron Collars to Chins, Front-Back Barriers & Footprints Recorded", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "The Girded Iron Collars (Aghlalan)",
              "Aghlalan ila al-adhqani fahum muqmahoon: shackles beneath chins forcing heads rigidly upward, symbolizing arrogant inability to prostrate.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Dual Barricade (Saddan)",
              "Barriers before and behind them: cognitive blindness preventing observation of present cosmic signs or learning from historical ruin.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Warning Only Awakes the Living",
              "Innama tundhiru man ittaba'a adh-dhikra: true warning profits only those who follow the message and fear the Most Merciful in the unseen.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Footprints Recorded (Atharahum)",
              "Wa naktubu ma qaddamu wa atharahum: Banu Salimah's footsteps to the Mosque and every generational legacy preserved in the clear Imam.")

    # ==========================================
    # PLATE 02: THE PARABLE OF THE METROPOLIS (Ayat 13-19)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 10,
        "THE PARABLE OF THE METROPOLIS & THE THREE ENVOYS",
        "Pillars 03 & 04: Mission of Antioch, The Reinforcing Third, Materialist Cynicism & Superstition",
        "PLATE 02 : THE METROPOLIS"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 03: MISSION OF THE THREE EMISSARIES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Antioch Archetype, The Reinforcing Third & The Defense of Wahy", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Archetype of the Metropolis",
              "Wadrib lahum mathalan as-haba al-qaryah: presenting the cautionary historical model of an arrogant civilization visited by divine envoys.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "The Reinforcing Third ('Azzazna)",
              "Two messengers rejected, reinforced with a third: demonstrating divine solidarity and escalating prophetic evidence before accountability.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Materialist Cynical Rebuttal",
              "Ma antum illa basharun mithluna: the shallow argument of deniers reducing transcendent truth to mundane physical equivalence.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Clear Conveyance as Sole Duty",
              "Wa ma 'alayna illa al-balaghu al-mubeen: prophetic mission is not coercive political subjugation, but unblemished illumination of truth.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 04: THE OMENS & MORAL EXTRAVAGANCE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Threats of Stoning, The Superstition of Tatayyur & Moral Diagnosis", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Threats of Public Stoning",
              "La-in lam tantahoo la-narjumannakum: despots lacking rational counter-arguments resort immediately to physical terrorism and stoning.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Superstition of Bad Omens",
              "Inna tatayyarna bikum: blaming external righteous reformers for droughts and misfortunes that stem entirely from their own moral guilt.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "The Rebuttal: 'Your Omen is With You'",
              "Qa'iloo ta'irukum ma'akum: calamity is the natural spiritual harvest of your own actions; the disease resides within your own hearts.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Diagnostic Verdict: Musrifoon",
              "Bal antum qawmun musrifoon: diagnosing the root pathology not as intellectual doubt, but as uncontrolled moral and ethical excess.")

    # ==========================================
    # PLATE 03: THE CHIVALRIC MARTYR: HABIB AL-NAJJAR (Ayat 20-27)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 10,
        "THE CHIVALRIC MARTYR: HABIB AL-NAJJAR",
        "Pillars 05 & 06: Sprint from the Outskirts, Rational Litmus Test, Immediate Jannah & Sublime Mercy",
        "PLATE 03 : HABIB AL-NAJJAR"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 05: THE SPRINT FROM THE PERIMETER", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Outskirts Believer, Asking No Financial Fee & Fitrah Logic", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Running from the Perimeter (Aqsa)",
              "Wa ja'a min aqsa al-madeenati rajulun yas'a: the marginalized laborer running to defend truth while the urban elite spectate.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "The Selflessness of True Guidance",
              "Ittabi'oo man la yas'alukum ajran: the universal litmus test: authentic teachers seek zero financial taxation, prestige, or worldly power.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Fitrah Logic of Devotion (Fatarani)",
              "Wa ma liya la a'budu alladhi fatarani: why should I not worship the One Who brought me into existence and to Whom all return?")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Total Impotence of False Idols",
              "In yuridni ar-Rahmanu bi-durrin la tughni 'anni shafa'atuhum: false gods cannot provide intercession or rescue against divine decree.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 06: IMMEDIATE JANNAH & SUBLIME PRAYER", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Public Declaration, Violent Martyrdom, Instant Welcome & No Rancor", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Public Declaration of Faith",
              "Inni aamantu bi-Rabbikum fasma'oon: declaring unwavering monotheism openly before the hostile mob without terror or compromise.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Instant Welcome: 'Enter Paradise!'",
              "Qeela idkhuli al-jannah: stepping out of the crushed physical body directly into Paradise with zero latency or purgatorial delay.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Sublime Forgiveness: No Rancor",
              "Ya layta qawmi ya'lamoon: beholding Paradise, he harbors zero vindictiveness, yearning that his murderers could only witness the truth.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Rank Among the Honored (Mukrameen)",
              "Bima ghafara li Rabbi wa ja'alani mina al-mukrameen: honoring the sincere martyr with total absolution and noble eternal station.")

    # ==========================================
    # PLATE 04: THE ACOUSTIC BLAST & HUMAN MOCKERY (Ayat 28-32)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 10,
        "ACOUSTIC RETRIBUTION & THE TRAGEDY OF MOCKERY",
        "Pillars 07 & 08: Destruction without Armies, The Single Shockwave, Extinguished Ash & Cosmic Grief",
        "PLATE 04 : ACOUSTIC RETRIBUTION"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 07: DESTRUCTION WITHOUT HEAVENLY ARMIES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("No Need for Angelic Legions, The Sonic Cry & Extinguished Ash", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Dispensing with Angelic Armies",
              "Wa ma anzalna 'ala qawmihi min jundin mina as-sama': creation is too insignificant to require divine military mobilization.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "The Single Sonic Shockwave",
              "In kanat illa sayhatan wahidah: a solitary acoustic cry commanded through Gabriel that ruptured vessels and seized all hearts.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Extinguished Like Cold Ash (Khamidoon)",
              "Fa-idha hum khamidoon: the thriving metropolitan city reduced in a split second to silent, dead, motionless cold embers.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Instantaneous Civilizational Erasure",
              "Demonstrating the absolute vulnerability of human architecture when divine cosmic laws withdraw sustenance.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 08: THE TRAGEDY OF HUMAN MOCKERY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Cosmic Lamentation, The Pattern of Ridicule & History's Lessons", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Universal Cosmic Sigh (Hasratan)",
              "Ya hasratan 'ala al-'ibad: divine lamentation over fallen mankind, repeatedly sabotaging their own eternal salvation.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "The Invariable Pattern of Mockery",
              "Ma ya'teehim min rasoolin illa kanoo bihi yastahzi'oon: every messenger sent with divine compassion is met with cynical ridicule.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Historical Blindness to Ruin",
              "A-lam yaraw kam ahlakna qablahum mina al-qurooni annahum ilayhim la yarji'oon: past empires erased that never return.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Inevitable Universal Gathering",
              "Wa in kullun lamma jamee'un ladayna muhdaroon: all generations across time will be marshaled together before the Sovereign Judge.")

    # ==========================================
    # PLATE 05: BOTANICAL REVIVAL & HYDRAULIC DESIGN (Ayat 33-36)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 10,
        "BOTANICAL REVIVAL & UNIVERSAL PAIRS",
        "Pillars 09 & 10: Parched Earth Revived, Gushing Aquifers, Human Technological Limits & Dualities",
        "PLATE 05 : BOTANICAL DESIGN"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 09: BOTANICAL ECOLOGICAL GENESIS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Dead Soil Revived, Sustaining Grains & Subterranean Springs", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Sign of the Dead Soil (Al-Maytah)",
              "Wa ayatun lahumu al-ardu al-maytah: barren desert soil reviving upon rain is empirical proof that dead bones can be animated.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "Germination & Nourishing Grains",
              "Ahyaynaha wa akhrajna minha habban faminhu ya'kuloon: cellular germination yielding carbohydrates essential for biological life.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Orchards of Dates and Vineyards",
              "Jannatin min nakheelin wa a'nab: rich perennial agriculture offering sugars, nutrients, and economic stability across generations.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Gushing Subterranean Aquifers",
              "Wa fajjarna feeha mina al-'uyoon: hydro-geological balance feeding root networks through pressurized artesian spring waters.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 10: DOXOLOGY & UNIVERSAL DUALITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Biological Humility, Hand Creation Denied & Universal Paired Physics", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Sustenance Without Human Authorship",
              "Li-ya'kuloo min thamarih: harvesting fruit synthesized through solar radiation and soil minerals without human intellectual patent.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "'Their Hands Did Not Make It'",
              "Wa ma 'amilat-hu aydeehim afala yashkuroon: reminding mankind that technology can cultivate, but cannot program seed biology.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Doxology of Universal Pairs",
              "Subhanalladhi khalaqa al-azwaja kullaha: glory to the Originator Who structured reality upon complementary paired architectures.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Duality Across All Dimensions",
              "Mating across flora, animal sexuality, electrical polarities (positive-negative), and physics dimensions yet undiscovered.")

    # ==========================================
    # PLATE 06: CELESTIAL CLOCKS & BALANCED ORBITS (Ayat 37-40)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 10,
        "CELESTIAL CHRONOMETRY & BALANCED ORBITS",
        "Pillars 11 & 12: Flaying Daylight, Solar Apex Velocity, Lunar Mansions & The Law of Non-Collision",
        "PLATE 06 : CELESTIAL CLOCKS"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: FLAYING DAYLIGHT & SOLAR APEX", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Flaying the Atmospheric Skin, Oceanic Dark & Solar Velocity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Flaying the Day from Night",
              "Wa ayatun lahumu al-laylu naslakhu minhu an-nahar: stripping the paper-thin atmospheric sheath of sunlight off the spinning globe.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Plunging into Primordial Darkness",
              "Fa-idha hum muzlimoon: revealing that pitch-black darkness is the default cosmic matrix, and daylight is a localized temporary gift.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Solar Trajectory to Appointed Apex",
              "Wash-shamsu tajri li-mustaqarrin laha: the sun hurtling through galactic space toward its apex in the constellation Hercules.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "The Decree of the Almighty, All-Knowing",
              "Dhalika taqdeeru al-'Azeezi al-'Aleem: celestial mechanics governed with mathematical calibration by Supreme Power and Wisdom.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: LUNAR PHASES & COSMIC EQUILIBRIUM", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Lunar Mansions, The Curved Stalk & The Law of Non-Collision", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Lunar Mansions (Manazila)",
              "Wal-qamara qaddarnahu manazila: determining 28 precise nightly stations that serve as humanity's natural cosmic calendar.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Waning to the Ancient Palm Stalk",
              "Hatta 'ada kal-'urjooni al-qadeem: waning until the crescent matches the delicate, bent, yellowed arc of a dried date-cluster branch.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "The Law of Non-Collision",
              "La ash-shamsu yanbaghee laha an tudrika al-qamar: calibrated gravitational equilibrium preventing planetary catastrophic collisions.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Floating in Frictionless Orbits",
              "Wa kullun fee falakin yasbahoon: celestial bodies swimming smoothly through space without mechanical friction or deviation.")

    # ==========================================
    # PLATE 07: MARITIME SOVEREIGNTY & THE TRUMPET (Ayat 41-54)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 10,
        "MARITIME VULNERABILITY & THE TRUMPET BLAST",
        "Pillars 13 & 14: The Laden Ark, Ocean Vulnerability, Acoustic Arrest in Marketplaces & Graves Hastening",
        "PLATE 07 : THE TRUMPET"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 13: OCEAN SOVEREIGNTY & THE ARK", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Noah's Seed in the Laden Ark, Modern Shipping & Sinking at Will", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "The Ancestral Laden Ark (Al-Fulk)",
              "Wa ayatun lahum anna hamalna dhurriyyatahum fee al-fulki al-mashhoon: preserving the human lineage through Noah's buoyant vessel.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Maritime Transport Architecture",
              "Wa khalaqna lahum min mithlihi ma yarkaboon: designing materials and buoyancy physics enabling global commercial sea voyages.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Hydrodynamic Vulnerability",
              "Wa in nasha' nughriqhum fala sareekha lahum: were water's surface tension removed, the greatest ships would plunge with no rescuer.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Mercy & Respite for an Appointed Hour",
              "Illa rahmatan minna wa mata'an ila heen: marine travel is preserved purely as divine mercy and transient earthly provision.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 14: ACOUSTIC ARREST & THE TRUMPET", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Cynical Deadlines, Market Seizure, Bequest Impossibility & Graves", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "Cynical Demands for the Hour",
              "Wa yaqooloona mata hadha al-wa'du in kuntum sadiqeen: mocking the reality of judgment because of divine patience and delay.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Seized Amidst Market Disputes",
              "Ma yanthuroona illa sayhatan wahidatan ta'khudhuhum wa hum yakhissimoon: the final blast strikes while they haggle in shops.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "No Bequest nor Return Home",
              "Fala yastatee'oona tawsiyatan wa la ila ahlihim yarji'oon: sudden paralysis preventing even the utterance of a will or reaching home.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "The Second Trumpet: Graves Hastening",
              "Wa nufeekha fee as-soori fa-idha hum mina al-ajdathi ila Rabbihim yansiloon: bodies reconstructed pouring from graves to their Lord.")

    # ==========================================
    # PLATE 08: ESCHATOLOGICAL HARVEST (Ayat 55-67)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 10,
        "THE ESCHATOLOGICAL HARVEST: SALAM VS DISGRACE",
        "Pillars 15 & 16: Joyous Inmates of Jannah, Divine Greeting (Salam), Criminal Separation & Testifying Limbs",
        "PLATE 08 : THE ESCHATOLOGY"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 15: INMATES OF PARADISE & DIVINE SALAM", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Joyful Absorption, Shaded Couches, Instant Delights & The Lord's Word", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Inmates of Jannah in Joyous Repose",
              "Inna as-haba al-jannati al-yawma fee shughulin fakihoon: absorbed in pure sublime delights with no fatigue, anxiety, or grief.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Adorned Couches in Shaded Canopies",
              "Hum wa azwajuhum fee dhilalin 'ala al-ara'iki muttaki'oon: reclining peacefully with pure companions upon elevated couches.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Every Longing Manifested",
              "Lahum feeha fakihatun wa lahum ma yadda'oon: all fruits and whatever the soul desires are granted instantaneously upon thought.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "The Supreme Zenith: Divine Salam",
              "Salamun qawlan min Rabbin Raheem: the beatific salutation of Peace spoken directly from the Merciful Lord to His beloved servants.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: SEVERING CRIMINALS & SPEAKING LIMBS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Criminal Banishment, Satanic Covenant Recalled & Sealed Mouths", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "'Stand Apart Today, You Criminals!'",
              "Wamtazoo al-yawma ayyuha al-mujrimoon: the terrifying command severing hypocrites and oppressors away from righteous ranks.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Broken Covenant with Adam's Progeny",
              "A-lam a'had ilaykum ya banee Adama an la ta'budoo ash-Shaytan: reminding mankind of their breach of covenant with the clear enemy.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Tasting the Denied Hellfire",
              "Hadhihi jahannamu allatee kuntum too'adoon; islawha al-yawma: entering the fire as the inevitable harvest of their persistent denial.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Sealed Mouths & Testifying Limbs",
              "Al-yawma nakhtimu 'ala afwahihim wa tukallimuna aydeehim wa tashhadu arjuluhum: tongues locked; hands and feet testify to every deed.")

    # ==========================================
    # PLATE 09: SOMATIC WITNESS & THE CRUMBLING BONE (Ayat 68-79)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        9, 10,
        "BIOLOGICAL INVERSION & THE CRUMBLING BONE",
        "Pillars 17 & 18: Inversion of Old Age, Refutation of Poetry, Cattle Subjugation & First Genesis",
        "PLATE 09 : THE CRUMBLING BONE"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 17: BIOLOGICAL INVERSION & TRUE REMEMBRANCE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Inversion in Age, Poetry Refuted, Warning the Living & Cattle", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 65, "Inversion of Physical Vitality",
              "Wa man nu'ammirhu nunakkis-hu fee al-khalq: whoever reaches advanced age has strength inverted back to infant weakness and fragility.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 66, "Absolute Refutation of Poetry",
              "Wa ma 'allamnahu ash-shi'ra wa ma yanbaghee lah: the Prophet was not taught poetry; revelation is immutable, crystalline divine truth.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 67, "Awakening the Truly Living",
              "Li-yundhira man kana hayyan: the Qur'an operates as an existential beacon sent to awaken living consciences before judgment falls.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 68, "The Subjugation of Cattle (Al-An'am)",
              "Fa-dhallalnaha lahum faminha rakoobuhum wa minha ya'kuloon: mighty livestock subdued by human hands for riding, milk, and warmth.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 18: UBAYY'S CRUMBLING BONE & FIRST CREATION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Sperm-Drop to Adversary, Decomposed Dust, Initiating Creator & Fire", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 69, "From Sperm-Drop to Arrogant Adversary",
              "Khalaqnahu min nutfatin fa-idha huwa khaseemun mubeen: created from a humble fluid droplet, yet strutting as an open debater against God.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 70, "The Skeptic: 'Who Will Revive Bones?'",
              "Man yuhyee al-'idhama wa hiya rameem: Ubayy crumbling dry bone into dust, denying resurrection based on materialist decay.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 71, "Revived by the Initiating Originator",
              "Qul yuhyeeha alladhi ansha'aha awwala marrah: He who assembled human form from absolute non-existence easily reconstructs dust.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 72, "Omniscient of Every Atom",
              "Wa Huwa bi-kulli khalqin 'aleem: divine tracking of every scattered calcium, carbon, and water molecule across earth and ocean.")

    # ==========================================
    # PLATE 10: KUN FAYAKUN & SOVEREIGN DOXOLOGY (Ayat 80-83)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        10, 10,
        "KUN FAYAKUN & THE SOVEREIGN CLIMAX",
        "Pillars 19 & 20: Green Wood Yielding Fire, Macrocosm Creation, Instant Decree (Kun) & Sovereign Hand",
        "PLATE 10 : SOVEREIGN DOXOLOGY"
    )

    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 19: THE GREEN FIRE & THE ALL-CREATOR", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Fire from Moisture, Cosmic Creation Power & Al-Khallaq al-'Aleem", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 73, "Fire from the Moisture-Laden Tree",
              "Alladhi ja'ala lakum mina ash-shajari al-akhdari naran: extracting blazing combustion from wet Markh and 'Afar branches.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 74, "Macrocosmic Deduction",
              "A-wa-laysa alladhi khalaqa as-samawati wal-arda bi-qadirin 'ala an yakhluqa mithlahum: Creator of galaxies easily recreates mortal man.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 75, "The Supreme Creator (Al-Khallaq)",
              "Bala wa Huwa al-Khallaqu al-'Aleem: affirmative response; He is the continuous Supreme Originator and Omniscient Master.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 76, "Effortless Creative Sovereignty",
              "Creation requires no labor, physical tools, or elapsed duration; all existence bows instantaneously before divine authority.")

    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 20: KUN FAYAKUN & SOVEREIGN DOMINION", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("The Fiat of 'BE', The Hand of Total Ownership & Universal Return", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 77, "The Sovereign Decree Formula",
              "Innama amruhu idha arada shay'an: the divine mechanism of intent: when He wills an outcome, His resolve is immediate and absolute.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 78, "The Command of 'KUN' (BE)",
              "An yaqoola lahu KUN FA-YAKOON: He merely says to it 'BE,' and reality crystallizes into existence without latency or resistance.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 79, "Total Ownership of All Things (Malakoot)",
              "Fa-subhanalladhi bi-yadihi malakootu kulli shay': transcendent glory to Him in whose hand rests absolute sovereign custody of the cosmos.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 80, "The Final Return: 'Unto Him You Return'",
              "Wa ilayhi turja'oon: closing with eternal ontological certainty: all souls shall be brought back to their Lord for absolute recompense.")

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"Generated 10-Plate Master Vector PDF: {OUTPUT_PDF}")

    # Generate Previews
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "page")]
    subprocess.run(cmd, check=True)
    print(f"Generated PNG previews in {PREVIEWS_DIR}")

    # Copy previews to brain directory
    for f in os.listdir(PREVIEWS_DIR):
        if f.endswith(".png"):
            src = os.path.join(PREVIEWS_DIR, f)
            dest = os.path.join(brain_dir, f"yasin_mindmap_{f}")
            shutil.copy2(src, dest)
    print(f"Copied previews to brain directory: {brain_dir}")

if __name__ == "__main__":
    build_yasin_pdf()
