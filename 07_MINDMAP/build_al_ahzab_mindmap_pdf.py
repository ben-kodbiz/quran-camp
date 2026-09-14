#!/usr/bin/env python3
"""
Huurs Studio - Surah Al-Ahzab Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
Strict Brand_Visual_System.md & Absolute Copyright Insulation
The Siege of the Trench, Uswatun Hasanah, The Household of Prophecy & Al-Amanah
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "AL_AHZAB_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews_al_ahzab")
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

def build_al_ahzab_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH AL-AHZAB", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE INTEGRITY OF HEART & ADOPTION RESTORATION
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE INTEGRITY OF HEART & ABOLITION OF ADOPTION",
        "Pillars 1 & 2: Ma Ja'ala Allahu li-Rajulin min Qalbayn, Zihar & Ud'oohum li-Aba'ihim",
        "PLATE 01 : INTEGRITY OF HEART"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: THE SINGLE HEART & DISMANTLING FICTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("No Two Hearts, Abolition of Zihar & Undivided Allegiance", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "Single Heart in the Chest",
              "Ma ja'ala Allahu li-rajulin min qalbayni fee jawfih: Allah has not made two hearts in any man; rejecting internal hypocrisy.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Abolition of Zihar Falsehood",
              "Repudiating pre-Islamic pagan oaths claiming wives magically become mothers; biological reality cannot be altered by speech.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Undivided Spiritual Allegiance",
              "A single heart cannot harbor sincere divine love while simultaneously serving false gods or worldly vanity.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Divine Law Anchored in Truth",
              "Allah speaks the objective truth and guides to the straight path, cutting through cultural delusions and legal fictions.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: ADOPTION REFORM & PROPHETIC PRIMACY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Ud'oohum li-Aba'ihim, Zayd's Lineage & Ummahat al-Mu'mineen", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Ud'oohum li-Aba'ihim: Biological Fathers",
              "Call adopted children by their biological fathers; that is more just in the sight of Allah, restoring Zayd ibn Harithah's true name.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "Preserving Lineage & Equity",
              "Protecting true genealogical lineage, inheritance rights, and moral relationships from confusing artificial adoptions.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "An-Nabiyyu Awla bil-Mu'mineen",
              "The Prophet is closer and more entitled to the believers than their own souls; his commands transcend all personal desires.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Ummahat al-Mu'mineen: Mothers of Believers",
              "His noble wives are the mothers of the believers in sanctity, honor, deference, and permanent prohibition of marriage.")

    # ==========================================
    # PLATE 02: THE CRUCIBLE OF THE TRENCH (SIEGE OF 10,000)
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE CRUCIBLE OF THE TRENCH: THE SIEGE OF 10,000",
        "Pillars 3 & 4: Ghazwat al-Khandaq, Hearts at Throats & Hypocrisy Unmasked",
        "PLATE 02 : THE SIEGE"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: THE COALITION SIEGE OF MEDINA", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The 10,000 Confederate Army, The Trench & Seismic Shaking", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The 10,000 Confederate Coalition",
              "Pagan Quraysh, Ghatafan, and desert tribes marching with 10,000 warriors seeking to permanently eradicate the Muslim community.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "Excavation of the Northern Trench",
              "Salman al-Farsi proposing the excavation of a deep ditch across Medina's open front, halting enemy cavalry in freezing winter.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "Encircled From Above and Below",
              "Idh ja'ookum min fawqikum wa min asfala minkum: external armies besieging frontlines while Banu Qurayzah conspired from behind.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Hearts Reaching the Throats",
              "Balaghati al-quloobu al-hanajir: physiological terror, near starvation, and freezing nights shaking the believers severely.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 04: HYPOCRISY UNMASKED & COWARDICE", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Mocking Prophetic Visions, Inna Buyootana 'Awrah & Desertion", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "Mocking the Visions of Victory",
              "When the Prophet struck boulders seeing palaces of Rome and Persia fall, hypocrites sneered: 'We cannot even reach the latrine!'")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "Inna Buyootana 'Awrah: False Excuses",
              "Claiming their homes were exposed to sneak away from defense trenches; Allah exposes their true motive as cowardly desertion.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "Treachery of Internal Factions",
              "Banu Qurayzah breaking mutual defense treaties, plotting to massacre women and children in Medina while armies besieged trenches.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "The Sifting of Conviction",
              "Extreme hardship serving as the divine furnace separating hypocritical pretension from unbreakable monotheistic conviction.")

    # ==========================================
    # PLATE 03: USWATUN HASANAH & THE MEN OF COVENANT
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "USWATUN HASANAH & THE MEN OF COVENANT",
        "Pillars 5 & 6: The Prophetic Exemplar, Anas ibn al-Nadr & Unshakeable Conviction",
        "PLATE 03 : THE PARAGON"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 05: USWATUN HASANAH: PROPHETIC PARAGON", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Master Exemplar, Shared Toil, Courage & Abundant Dhikr", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "The Peerless Role Model (Uswah)",
              "Laqad kana lakum fee Rasoolillahi uswatun hasanah: in the Messenger of Allah is the consummate blueprint of leadership and character.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Shared Hardship in the Trenches",
              "Carrying soil, wielding the pickaxe, binding stones to his abdomen against hunger, and sharing every freezing vigil with his companions.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "Unshakeable Courage Under Siege",
              "Never retreating a single step; maintaining serene reliance upon Allah while armies massed on the horizon.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Conditioned on Hoping for Allah & Last Day",
              "This exemplary character is accessed by whoever sincerely hopes for Allah's pleasure, fears the Last Day, and remembers Allah often.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 06: MEN WHO FULFILLED THEIR COVENANT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Rijalun Sadaqoo, Anas ibn al-Nadr & Uncompromising Resolve", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "Rijalun Sadaqoo: Faithful Men",
              "Mina al-mu'mineena rijalun sadaqoo ma 'ahadoo Allaha 'alayh: men who proved completely true to their solemn covenant with Allah.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "Anas ibn al-Nadr: The Scent of Jannah",
              "Sahih al-Bukhari 2805: Plunging into enemy ranks at Uhud, crying: 'I smell the fragrance of Paradise behind Mount Uhud!'")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Minhum Man Qada Nahbah",
              "Of them are those who fulfilled their vow through glorious martyrdom, sealing their faith in blood with steadfast honor.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Minhum Man Yantazir: Patient Vigil",
              "And of them are those who still await their appointed hour, never compromising, wavering, or altering their resolve in the least.")

    # ==========================================
    # PLATE 04: THE FREEZING GALE & INVISIBLE ARMIES
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "THE FREEZING GALE & INVISIBLE ARMIES",
        "Pillars 7 & 8: Reeh Sarsar, Angelic Hosts & Sovereign Deliverance",
        "PLATE 04 : DIVINE TEMPEST"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 07: THE DIVINE HURRICANE & ANGELIC HOSTS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Freezing Winds, Invisible Legions, Overturned Tents & Panic", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "Arsalna 'Alayhim Reehan: Freezing Gale",
              "Allah unleashed a ferocious, freezing northern hurricane upon the confederates, ripping tent pegs and extinguishing campfires.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Junoodan Lam Tarawha: Invisible Hosts",
              "Legions of descending angels casting psychological terror, disarray, and confusion into the heart of the 10,000-man coalition.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Overturned Pots & Blinding Dust",
              "Cauldrons overturned, pack animals panicking, and sand thrown into eyes, rendering military coordination impossible.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "Hudhayfah's Midnight Witness",
              "Sahih Muslim 1788: Infiltrating the freezing camp to see Abu Sufyan leaping upon his camel, shouting: 'Depart, for I am leaving!'")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 08: SOVEREIGN ROUT & PURGING TREASON", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Turning Back in Rage, Spared From Fighting & Banu Qurayzah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "Routed in Humiliated Rage",
              "Wa radda Allahu alladhina kafaroo bi-ghaydhihim: confederates driven back in bitter frustration having gained zero victory.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Kafa Allahu al-Mu'mineena al-Qital",
              "Allah spared the believers actual armed clash; divine atmospheric intervention routed the superpower alliance effortlessly.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "The Reckoning of Banu Qurayzah",
              "Besieging the fortress of internal traitors who plotted massacre; divine judgment enacted according to their own biblical law.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "The Inherited Territory",
              "Granting believers security, land, and fortified dwellings they had never before possessed; Medina established as an inviolable sanctuary.")

    # ==========================================
    # PLATE 05: THE MOTHERS OF THE BELIEVERS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "THE MOTHERS OF THE BELIEVERS: AYAT AL-TAKHYIR & PURIFICATION",
        "Pillars 9 & 10: The Verse of Choice, Domestic Sanctity & Ayat al-Tatheer",
        "PLATE 05 : HOUSEHOLD OF PROPHETS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 09: AYAT AL-TAKHYIR: THE NOBLE CHOICE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("The World vs The Hereafter, 'A'ishah's Precedent & Double Reward", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "Ayat al-Takhyir: The Verse of Choice",
              "Offering the Prophet's wives generous divorce if they desired luxury, or immense eternal reward if they chose Allah and His Messenger.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "'A'ishah's Immediate Surrender",
              "Sahih al-Bukhari 4785: 'Regarding you do I consult parents? I choose Allah, His Messenger, and the Home of the Hereafter!'")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Unanimous Noble Resolve",
              "Every single wife of the Prophet ﷺ followed 'A'ishah, choosing pious austerity and eternal companionship over fleeting wealth.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Double Recompense for the Righteous",
              "Elevated spiritual proximity conferring higher moral responsibility; righteous deeds rewarded with multiplied divine honor.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 10: DOMESTIC SANCTITY & AYAT AL-TATHEER", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Dignified Speech, Home Sanctuary, Shunning Tabarruj & Tatheer", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "Dignified and Direct Speech",
              "Fa-la takhda'na bil-qawl: do not speak with flirtatious softness lest the diseased heart lust; speak with firm, dignified clarity.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Wa Qarna fee Buyootikunna",
              "Settle gracefully in your homes as sanctuaries of prayer and remembrance, establishing a peaceful moral stronghold.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Shunning Jahiliyyah Tabarruj",
              "Rejecting the seductive, ostentatious public display of early pagan ignorance; cultivating modesty and inner spiritual beauty.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Ayat al-Tatheer: Complete Purification",
              "Allah intends to remove all spiritual impurity from the household of the Prophet (Ahl al-Bayt) and purify them completely.")

    # ==========================================
    # PLATE 06: DECALOGUE OF SPIRITUAL PARITY & DIVINE DECREE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "THE DECALOGUE OF SPIRITUAL PARITY & DIVINE DECREE",
        "Pillars 11 & 12: Ten Paired Virtues & No Choice Against Divine Decrees",
        "PLATE 06 : SPIRITUAL PARITY"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: THE DECALOGUE OF SPIRITUAL PARITY", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Ten Paired Virtues for Men and Women, Maghfirah & Great Reward", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "Paired Submission and Faith",
              "Muslims and Believers: outward submission to divine law and inward heart conviction affirmed equally for men and women.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Truthfulness, Patience & Humility",
              "As-Sidq, As-Sabr, and Al-Khushu': moral honesty, endurance under trial, and reverent stillness of heart before God.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Charity, Fasting & Chastity",
              "Mutasaddiqeen, Sa'imeen, and guarding chastity: generous wealth distribution, bodily self-restraint, and moral purity.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "Abundant Dhikr & Divine Reward",
              "Remembering Allah often: identical divine forgiveness (Maghfirah) and immense eternal reward prepared without gender distinction.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 12: ABSOLUTE SURRENDER TO DIVINE DECREES", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("No Choice Against Divine Decree, Zaynab's Marriage & Taboo Broken", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "No Choice Against Divine Command",
              "Wa ma kana li-mu'minin an yakoona lahumu al-khiyarah: when Allah and His Messenger decide a matter, private preference ceases.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Marriage of Zayd & Zaynab",
              "Divinely commanded marriage of the Prophet to Zaynab bint Jahsh after her divorce, permanently shattering adoption taboos.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Dismantling Pre-Islamic Superstition",
              "Li-kay la yakoona 'ala al-mu'mineena haraj: establishing that wives of former adopted sons are lawful to marry under divine law.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Zaynab's Celestial Honor",
              "Sahih al-Bukhari 7420: Zaynab proudly stating: 'Your families married you to the Messenger, but Allah married me from above seven heavens!'")

    # ==========================================
    # PLATE 07: THE SEAL OF THE PROPHETS & THE RADIANT BEACON
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "THE SEAL OF THE PROPHETS & THE RADIANT BEACON",
        "Pillars 13 & 14: Khatam an-Nabiyyeen, Sirajan Muneera & Abundant Dhikr",
        "PLATE 07 : SEAL OF PROPHETS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 13: KHATAM AN-NABIYYEEN (FINAL SEAL)", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Not Father of Any Men, The Final Seal & Sunni Consensus", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Not Father of Any of Your Men",
              "Ma kana Muhammadun aba ahadin min rijalikum: Muhammad is not the biological father of adult men; Zayd was not his biological son.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "Rasool Allahi: Universal Emissary",
              "Sent as the final messenger carrying the comprehensive, preserved divine law for all tribes, nations, and future epochs.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Khatam an-Nabiyyeen: The Final Seal",
              "The definitive seal completing the edifice of divine revelation; the prophetic line is irrevocably culminated.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Unanimous Sunni Consensus on Finality",
              "All classical Sunni authorities affirm that anyone claiming prophethood after Muhammad ﷺ is an absolute impostor.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 14: THE RADIANT BEACON & CONTINUOUS DHIKR", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Sirajan Muneera, The Fivefold Mission & Praise Morning/Eve", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "The Fivefold Prophetic Mission",
              "Shahidan (witness), Mubashshiran (bringer of glad tidings), Nadheera (warner), and Da'iyan ila Allah (inviter to God).")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "Sirajan Muneera: The Illuminating Sun",
              "A radiant celestial beacon illuminating spiritual darkness, cutting through ignorance with crystalline moral clarity.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "Command of Abundant Remembrance",
              "Ya ayyuha alladhina amanoo-dh-kuroo Allaha dhikran katheera: continuous remembrance of Allah keeping heart and tongue alive.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "Praising at Dawn and Dusk",
              "Wa sabbihoohu bukratan wa aseela: framing the daylight hours with structured morning and evening doxology and praise.")

    # ==========================================
    # PLATE 08: SALAT UPON THE PROPHET, JILBAB & THE COSMIC TRUST
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "SALAT UPON THE PROPHET, JILBAB & THE COSMIC TRUST",
        "Pillars 15 & 16: Salat 'ala an-Nabi, Ayat al-Jilbab & The Weight of Al-Amanah",
        "PLATE 08 : THE COSMIC TRUST"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 15: SALAT 'ALA AN-NABI & THE JILBAB", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Divine/Angelic Invocations, Outer Cloak & Words of Truth", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Divine & Angelic Invocations of Grace",
              "Inna Allaha wa mala'ikatahu yusalloona 'ala an-Nabi: Allah elevates His Prophet in the highest assembly; angels ask forgiveness.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "The Believers' Mandate of Peace",
              "Ya ayyuha alladhina amanoo salloo 'alayhi wa sallimoo tasleema: commanded to send continuous blessings and peace upon him.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "Ayat al-Jilbab: Outer Garment of Honor",
              "Yudneena 'alayhinna min jalabeebihinna: drawing outer cloaks over themselves to be recognized as dignified and protected from harassment.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Qawlan Sadeeda: Words Straight to Truth",
              "Fear Allah and speak words of crystalline honesty; He will rectify your actions and forgive your sins.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 16: AL-AMANAH: THE WEIGHT OF THE TRUST", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Heavens and Mountains Shuddering, Man's Bold Undertaking & Mercy", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "The Cosmic Offering of the Trust",
              "Inna 'aradna al-amanata 'ala as-samawat: offering moral agency, reason, and divine commandments to the cosmos.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "The Shudder of Earth and Mountains",
              "Fa-abayna an yahmilnaha wa ashfaqna minha: granite mountains and celestial galaxies declined to bear it in holy dread of falling short.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "Man's Perilous Undertaking",
              "Wa hamalaha al-insan: frail man boldly accepted the covenant, possessing the agency to ascend above angels or sink below beasts.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "Zalooman Jahoola vs Ghafoor Raheem",
              "Prone to injustice and ignorance, yet those who fulfill the trust are wrapped in the boundless forgiveness and mercy of Allah.")

    pdf.save(OUTPUT_PDF)
    print(f"[OK] Generated {OUTPUT_PDF}")

    # Generate preview PNGs
    cmd = f"pdftoppm -png -r 150 {OUTPUT_PDF} {PREVIEWS_DIR}/page"
    subprocess.run(cmd, shell=True, check=True)
    print(f"[OK] Generated preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src = f"{PREVIEWS_DIR}/page-{i:02d}.png" if os.path.exists(f"{PREVIEWS_DIR}/page-{i:02d}.png") else f"{PREVIEWS_DIR}/page-{i}.png"
        dst = f"{brain_dir}/al_ahzab_mindmap_page_{i}.png"
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied preview to {dst}")
        else:
            print(f"Warning: preview file {src} not found")

if __name__ == "__main__":
    build_al_ahzab_pdf()
