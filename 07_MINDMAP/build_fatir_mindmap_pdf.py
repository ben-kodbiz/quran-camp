#!/usr/bin/env python3
"""
Huurs Studio - Surah Fatir Master Mindmap Vector PDF Generator
16:9 Landscape Widescreen (792 x 480 pt) • 8 Plates • 16 Pillars • 64 Cards
Strict Brand_Visual_System.md & Absolute Copyright Insulation
The Cosmic Originator, Multi-Winged Angels, Human Faqr vs Divine Ghina, The Three Heirs & Sunnatullah
"""

import os
import sys
import subprocess
import shutil

sys.path.insert(0, "/mnt/AI/ag/Campaign/Portfolio/scripts")
from pdf_engine import PDFDocument

BASE_DIR = "/mnt/AI/ag/Campaign/07_MINDMAP"
OUTPUT_PDF = os.path.join(BASE_DIR, "FATIR_MASTER_MINDMAP.pdf")
PREVIEWS_DIR = os.path.join(BASE_DIR, "previews_fatir")
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

def build_fatir_pdf():
    w, h = 792, 480
    pdf = PDFDocument(page_width=w, page_height=h)

    def draw_chrome(pnum, total_pages, title, subtitle, section_badge):
        pdf.rect(0, 0, w, h, fill_rgb=NAVY_DEEP)

        # Top Header Bar
        pdf.rect(0, h - 42, w, 42, fill_rgb=NAVY_CARD)
        pdf.line(0, h - 42, w, h - 42, stroke_rgb=GOLD, line_width=1.2)
        pdf.text("HUURS STUDIO", 32, h - 26, font="F2", size=11, rgb=GOLD)
        pdf.text(" |  DEEPER THOUGHT CAMPAIGN  -  SURAH FATIR", 122, h - 26, font="F1", size=8.5, rgb=TEXT_MUTED)
        
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
    # PLATE 01: THE COSMIC ORIGINATOR & ANGELIC WINGS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        1, 8,
        "THE COSMIC ORIGINATOR & MULTI-WINGED ANGELS",
        "Pillars 1 & 2: Fatir as-Samawati, Angelic Ranks, Creative Expansion & Sovereign Mercy",
        "PLATE 01 : THE ORIGINATOR"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 01: FATIR & CELESTIAL ARCHITECTURE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Creation Ex Nihilo, Multi-Winged Emissaries & Jibreel's 600 Wings", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 1, "The Cosmic Originator (Fatir)",
              "Al-Hamdu lillahi Fatiri as-samawati wal-ard: cleaving existence out of absolute non-existence without prior model or archetype.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 2, "Appointing Celestial Messengers",
              "Ja'ili al-mala'ikati rusulan: appointing angelic beings as cosmic emissaries traversing interstellar realms with speed and precision.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 3, "Multi-Winged Aerial Architecture",
              "Ulee ajnihatin mathna wa thulatha wa ruba': angels possessing wings in pairs, triads, and quartets reflecting divine ranks.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 4, "Gabriel's 600 Celestial Wings",
              "Prophetic vision of Jibreel with 600 wings spanning from east to west, shedding pearls and rubies of heavenly luminescence.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 02: EXPANSIVE CREATION & MERCY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Continuous Creative Expansion, Unwithholdable Mercy & Sole Sustainer", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 5, "Continuous Creative Expansion",
              "Yazeedu fil-khalqi ma yashaa': Allah continually enriches creation in beauty, vocal resonance, physical scale, and cosmic complexity.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 6, "The Unwithholdable Door of Mercy",
              "Ma yaftahi Allahu lin-nasi min rahmatin fala mumsika laha: whatever mercy Allah opens for humanity, no earthly power can obstruct.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 7, "Protection from Divine Withholding",
              "Wa ma yumsik fala mursila lahu min ba'dih: and whatever door He closes, no human flattery or force can ever pry open.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 8, "Remembering the Sole Sustainer",
              "Ya ayyuha an-nasu udhkooroo ni'mata Allahi 'alaykum: hal min khaliqin ghayru Allah: there is no creator or sustainer besides Him.")

    # ==========================================
    # PLATE 02: THE DECEIVER & THE ASCENT OF SPEECH
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        2, 8,
        "THE DECEIVER & THE ASCENT OF PURE SPEECH",
        "Pillars 3 & 4: Worldly Delusions, The Chief Deceiver (Al-Gharoor), True Glory & Elevating Deeds",
        "PLATE 02 : PURE SPEECH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 03: THE CHIEF DECEIVER & HIS FACTION", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("Worldly Glitter, Complacency Concerning Allah & Satan's Conscription", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 9, "The Seduction of Worldly Glitter",
              "Fala taghurrannakumu al-hayatu ad-dunya: warning against being lulled by transient luxury and temporal material pursuits.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 10, "The Chief Deceiver (Al-Gharoor)",
              "Wa la yaghurrannakum billahi al-gharoor: Satan deceiving people by whispering that Allah will forgive without moral repentance.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 11, "The Consummate Adversary",
              "Inna ash-shaytana lakum 'aduwwun fattakhidhoohu 'aduwwa: conscious vigilance against an active enemy dedicated to human ruin.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 12, "Conscription into the Blaze",
              "Innama yad'oo hizbahu li-yakoonoo min as-habi as-sa'eer: Satan's sole goal is dragging his followers into eternal scorch.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 04: THE PHYSICS OF GLORY & ASCENT", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Honor Belongs to Allah, Kalim Tayyib Rising & The Wings of Action", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 13, "All Glory Belongs to Allah",
              "Man kana yureedu al-'izzata falillahi al-'izzatu jamee'a: true dignity and victory cannot be purchased by compromising with falsehood.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 14, "The Ascent of Pure Words",
              "Ilayhi yas'adu al-kalimu at-tayyib: sincere declarations of monotheism, Tasbeeh, and truth possess inherent spiritual buoyancy.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 15, "The Wings of Righteous Deeds",
              "Wal-'amalu as-salihu yarfa'uh: good deeds serve as the wings carrying pure words upward into divine acceptance; speech verified by action.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 16, "Frustration of Evil Conspiracies",
              "Walladheena yamkuroona as-sayyi'at: lahum 'adhabun shadeedun wa makru ula'ika huwa yaboor: malicious schemes inevitably perish.")

    # ==========================================
    # PLATE 03: MORPHOGENESIS & THE TWO SEAS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        3, 8,
        "MORPHOGENESIS & THE PARABLE OF THE TWO SEAS",
        "Pillars 5 & 6: Dust to Embryo, Preserved Lifespans, Sweet Rivers & Saline Oceans",
        "PLATE 03 : THE TWO SEAS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 05: EMBRYOGENESIS & PRESERVED SPANS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Dust, Sperm-Drop, Sexual Differentiation & Omniscient Maternal Care", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 17, "Dust to Paired Embryos",
              "Wallahu khalaqakum min turabin thumma min nutfah: humanity fashioned from inorganic earth, reproduced through paired sexes.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 18, "Omniscient Maternal Awareness",
              "Wa ma tahmilu min untha wa la tada'u illa bi-'ilmih: not a single womb conceives or gives birth without exhaustive divine knowledge.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 19, "The Calibrated Span of Longevity",
              "Wa ma yu'ammaru min mu'ammarin wa la yunqasu min 'umurih: every extended life or shortened day pre-ordained in an Infallible Book.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 20, "Ease of Universal Governance",
              "Inna dhalika 'ala Allahi yaseer: tracking billions of biological lifespans and embryonic transitions is effortless for the Creator.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 06: FRESH RIVERS & SALINE OCEANS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Chemical Asymmetry, Marine Sustenance, Pearls & Cleaving Vessels", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 21, "The Sweet Palatable River",
              "Hadha 'adhbun furaatun sa'ighun sharabuh: sweet, thirst-quenching river water irrigating land and sustaining continental life.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 22, "The Salty Bitter Ocean",
              "Wa hadha milhun ujaj: dense marine salinity preserving the ocean from putrefaction and cleansing planetary atmospheric currents.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 23, "Fresh Protein & Lustrous Pearls",
              "Wa min kullin ta'kuloona lahman tariyya: extracting nutritious seafood and harvesting lustrous pearls and corals from both realms.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 24, "Cleaving Vessels of Commerce",
              "Wa tara al-fulka feehi mawakhiroo: ships cutting through water to knit continents into cooperative commercial harmony.")

    # ==========================================
    # PLATE 04: PLANETARY TIME & THE DATE-SEED SKIN
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        4, 8,
        "PLANETARY TIME & THE DATE-SEED MEMBRANE",
        "Pillars 7 & 8: Circadian Mechanics, Subjugated Celestial Orbits, The Qitmeer & Deaf Idols",
        "PLATE 04 : THE QITMEER"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 07: CIRCADIAN ROTATION & CELESTIAL ORBITS", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Merging Night and Day, Regulated Solar-Lunar Paths & Undivided Mulk", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 25, "The Intertwining of Time",
              "Yooliju al-layla fin-nahari wa yooliju an-nahara fil-layl: night gradually woven into day and day into night with planetary precision.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 26, "Subjugated Sun and Moon",
              "Sakhkhara ash-shamsa wal-qamar kullun yajree li-ajalin musamma: sun and moon calibrated to run until an appointed cosmic consummation.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 27, "Undivided Divine Sovereignty",
              "Dhalikumu Allahu Rabbukum lahu al-mulk: that is Allah your Lord; to Him alone belongs unshared ownership of the cosmos.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 28, "The Myth of Intermediary Power",
              "Exposing the delusion of turning to created entities for independent benefit, protection, health, or eschatological salvation.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 08: THE QITMEER & SPIRITUAL DEAFNESS", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("The Date-Seed Skin, Sensory Impotence & Renunciation on Judgment Day", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 29, "The Powerlessness of the Qitmeer",
              "Walladheena tad'oona min doonihi ma yamlikoona min qitmeer: false gods possess not even the gossamer membrane enclosing a date-seed.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 30, "Total Sensory Deafness",
              "In tad'oohum la yasma'oo du'a'akum: false deities cannot perceive supplications; carved stone, wood, or dead bones hear nothing.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 31, "Incapacity to Deliver Benefit",
              "Wa law sami'oo ma astajaboo lakum: even if they could hypothetically hear, they have zero agency or power to respond to human cries.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 32, "Betrayal on Judgment Day",
              "Wa yawma al-qiyamati yakfuroona bi-shirkikum: on the Day of Resurrection, false gods will denounce and disown their worshippers.")

    # ==========================================
    # PLATE 05: HUMAN FAQR VS DIVINE GHINA
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        5, 8,
        "HUMAN FAQR VS DIVINE SELF-SUFFICIENCY",
        "Pillars 9 & 10: Ontological Poverty, Divine Ghina, Species Replacement & Unshared Burdens",
        "PLATE 05 : HUMAN FAQR"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 09: THE ONTOLOGICAL POVERTY OF MAN", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Antumu al-Fuqara', Al-Ghaniyy Al-Hameed & The Fragility of Humanity", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 33, "The Universal Human Condition",
              "Ya ayyuha an-nasu antumu al-fuqara'u ila Allah: human beings are fundamentally, permanently dependent for every heartbeat and breath.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 34, "The Absolute Self-Sufficient (Al-Ghaniyy)",
              "Wallahu Huwa al-Ghaniyyu al-Hameed: Allah is totally free of need; human piety adds nothing to Him, and sin subtracts nothing.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 35, "Ease of Species Replacement",
              "In yasha' yudh-hibkum wa ya'ti bi-khalqin jadeed: if He willed, He could extinguish mankind and bring forth an obedient new creation.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 36, "Human Survival as Pure Grace",
              "Wa ma dhalika 'ala Allahi bi-'azeez: human continuance is a gift of divine forbearance, not an ontological necessity for God.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=ROSE, line_width=1.0)
    pdf.text("PILLAR 10: UNSHARED MORAL ACCOUNTABILITY", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=ROSE)
    pdf.text("No Bearer of Another's Burden, The Futile Cry to Kin & Personal Tazkiyah", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 37, "No Bearer of Another's Guilt",
              "Wa la taziru waziratun wizra ukhra: repudiating inherited sin; each soul answers strictly for its own moral agency and choices.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 38, "Futile Pleas to Closest Relatives",
              "Wa in tad'u muthqalatun ila himliha la yuhmal minhu shay': even a mother or child will refuse to bear an atom of another's sins.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 39, "Receptive Solitary Souls",
              "Innama tundhiru alladheena yakhshawna Rabbahum bil-ghayb: warnings only penetrate hearts that revere their Lord in the unseen.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 40, "Self-Benefiting Purification (Tazkiyah)",
              "Wa man tazakka fa-innama yatazakka li-nafsih: moral reform and repentance enrich the soul itself; Allah is independent of our deeds.")

    # ==========================================
    # PLATE 06: SENSORY ASYMMETRIES & GEOLOGY
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        6, 8,
        "SENSORY ASYMMETRIES & GEOLOGICAL STRATA",
        "Pillars 11 & 12: Blind vs Seeing, Shadows vs Light, Reviving Winds & Multi-Colored Mountains",
        "PLATE 06 : COSMIC SIGNS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 11: THE FOUR SPIRITUAL DICHOTOMIES", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Blindness vs Insight, Darkness vs Radiance, Shade vs Scorching Heat", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 41, "The Blind vs The Seeing",
              "Wa ma yastawee al-a'ma wal-baseer: arrogant moral blindness cannot be equated with the clarity of illuminated prophetic vision.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 42, "Darknesses vs Solar Radiance",
              "Wa la adh-dhulumatu wan-noor: the plural confusions of polytheism and nihilism contrasted with the singular beam of Tawhid.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 43, "Protective Shade vs The Scorching Wind",
              "Wa la adh-dhillu wal-haroor: the serene, cool shelter of Paradise contrasted with the suffocating furnace of Hell.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 44, "The Living vs The Dead in Graves",
              "Wa ma yastawee al-ahya'u wal-amwat: the heart alive with the remembrance of Allah contrasted with a corpse walking on earth.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 12: REVIVING WINDS & ROCK STRATA", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("Wind-Driven Hydrologic Revival, Resurrection Proof & Mountain Veins", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 45, "The Wind-Driven Hydrologic Cycle",
              "Wallahu alladhee arsala ar-riyaha fatutheeroo sahaban: winds driving heavy clouds over dead soil to unleash life-giving rainfall.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 46, "Empirical Proof of Resurrection",
              "Fa-ahyayna bihi al-arda ba'da mawtiha kadhalika an-nushoor: botanical rebirth proof that scattered human molecules will reassemble.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 47, "Chromatic Diversity of Flora",
              "Fa-akhrajna bihi thamaratin mukhtalifan alwanuha: single rain source producing countless varieties of colors, flavors, and scents.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 48, "Mountain Highways of Quartz & Basalt",
              "Judadun beedun wa humrun mukhtalifun alwanuha wa gharabeebu sood: layered strata of white quartz, red sandstone, and raven basalt.")

    # ==========================================
    # PLATE 07: REVERENCE OF SCHOLARS & 3 HEIRS
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        7, 8,
        "REVERENCE OF SCHOLARS & THE THREE HEIRS",
        "Pillars 13 & 14: Innamā Yakhshā Allaha al-'Ulamā', Undying Commerce & Three Classes of the Ummah",
        "PLATE 07 : THE THREE HEIRS"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=GOLD, line_width=1.0)
    pdf.text("PILLAR 13: THE AWE OF TRUE SCHOLARSHIP", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=GOLD)
    pdf.text("Knowledge Defined as Reverent Awe, Recitation & Undying Commerce", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 49, "Knowledge Defined as Awe (Khashyah)",
              "Innama yakhsha Allaha min 'ibadihi al-'ulama': true knowledge is not accumulating information; it is deep reverent awe before God.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 50, "The Commerce That Never Perishes",
              "Yatloona Kitaba Allahi wa aqamu as-salata: reciting scripture, establishing prayer, and spending in secret and open without loss.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 51, "Reaping the Full Measure of Reward",
              "Li-yuwaffiyahum ujoorahum wa yazeedahum min fadlih: Allah fulfilling wages in full and adding bonus gifts from His inexhaustible grace.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 52, "Al-Ghafoor Ash-Shakoor",
              "Innahu Ghafoorun Shakoor: He forgives vast shortcomings and expresses divine appreciation by multiplying tiny sincere acts.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=EMERALD, line_width=1.0)
    pdf.text("PILLAR 14: THE THREE HEIRS TO THE BOOK", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=EMERALD)
    pdf.text("The Stumbling Soul, The Moderate, The Foremost & Permanent Relief in 'Adn", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 53, "The Chosen Inheritors of the Qur'an",
              "Thumma awrathna al-kitaba alladheena istafayna min 'ibadina: all three categories are chosen believers of the Ummah of Muhammad ﷺ.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 54, "The One Who Wrongs Himself (Dhalim)",
              "Faminhum dhalimun li-nafsih: the believer who stumbles into minor sins or neglects voluntary acts, yet clings firmly to Tawhid.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 55, "The Moderate & The Foremost",
              "Wa minhum muqtasid wa minhum sabiqun bil-khayrat: the steady believer fulfilling duties, and the spiritual vanguard racing ahead.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 56, "The Extinction of All Grief in Paradise",
              "Jannatu 'adnin yadkhuloonaha: all three groups entering Eden, declaring: Alhamdulillah alladhee adh-haba 'anna al-hazan.")

    # ==========================================
    # PLATE 08: IMMUTABLE SUNNAH & FORBEARING RESPITE
    # ==========================================
    pdf.new_page(w, h)
    draw_chrome(
        8, 8,
        "THE IMMUTABLE SUNNAH & FORBEARING RESPITE",
        "Pillars 15 & 16: The Trap of Evil Plots, Screams of Belated Remorse, Sunnatullah & The Delayed Hour",
        "PLATE 08 : SUNNATULLAH"
    )

    # Column 1
    pdf.rect(c1_x, c1_y, c1_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=PURPLE, line_width=1.0)
    pdf.text("PILLAR 15: EVIL PLOTS & SCREAMS OF REMORSE", c1_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=PURPLE)
    pdf.text("Belated Pleas for Return, Sufficient Lifespan & The Trap of Deceit", c1_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c1_x + 12, c1_y + c1_h - 34, c1_x + c1_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c1_x, c1_y + c1_h - 48, c1_w, 57, "Screams of Belated Remorse",
              "Wa hum yastarikhona feeha Rabbana akhrijna na'mal salihan: condemned souls screaming in agony for another chance on earth.")
    draw_card(c1_x, c1_y + c1_h - 118, c1_w, 58, "Sufficient Lifespan for Reflection",
              "Awa-lam nu'ammirkum ma yatadhakkaru feeh: Allah granted ample decades of youth and maturity to reflect upon prophetic warnings.")
    draw_card(c1_x, c1_y + c1_h - 188, c1_w, 59, "The Rebound of Treachery",
              "Wa la yaheequ al-makru as-sayyi'u illa bi-ahlih: evil plots invariably rebound upon their own architects, trapping conspirators.")
    draw_card(c1_x, c1_y + c1_h - 258, c1_w, 60, "Broken Oaths of Guidance",
              "Polytheists swore solemn oaths that a warner would make them guided, yet revelation increased them only in arrogant flight.")

    # Column 2
    pdf.rect(c2_x, c1_y, c2_w, c1_h, fill_rgb=NAVY_ELEVATED, stroke_rgb=CYAN, line_width=1.0)
    pdf.text("PILLAR 16: THE CONSTANCY OF DIVINE LAW", c2_x + 12, c1_y + c1_h - 16, font="F2", size=8.8, rgb=CYAN)
    pdf.text("Vanished Empires, Sunnatullah Never Altered & The Respite of Mercy", c2_x + 12, c1_y + c1_h - 28, font="F3", size=7.2, rgb=TEXT_MUTED)
    pdf.line(c2_x + 12, c1_y + c1_h - 34, c2_x + c2_w - 12, c1_y + c1_h - 34, stroke_rgb=BORDER_MUTED, line_width=0.6)

    draw_card(c2_x, c1_y + c1_h - 48, c2_w, 61, "Walking Through Vanished Empires",
              "Awa-lam yaseeroo fil-ardi fayanzuroo: observing the silent ruins of ancient civilizations who possessed superior physical power.")
    draw_card(c2_x, c1_y + c1_h - 118, c2_w, 62, "No Alteration in Sunnatullah",
              "Fa-lan tajida li-sunnati Allahi tabdeela wa la tahweela: you will never find in the divine historical law any deviation or diversion.")
    draw_card(c2_x, c1_y + c1_h - 188, c2_w, 63, "The Forbearing Planetary Respite",
              "Wa law yu'akhidhu Allahu an-nasa bima kasaboo ma taraka 'ala dhahriha min dabbah: if seized for sins, no creature would remain.")
    draw_card(c2_x, c1_y + c1_h - 258, c2_w, 64, "The Appointed Final Hour",
              "Yu'akhkhiruhum ila ajalin musamma: delaying judgment until an appointed term; Allah watches over every servant with perfect vision.")

    # Save PDF
    pdf.save(OUTPUT_PDF)
    print(f"[OK] Successfully built Surah Fatir Master Mindmap PDF: {OUTPUT_PDF}")

    # Render Previews
    cmd = ["pdftoppm", "-png", "-r", "150", OUTPUT_PDF, os.path.join(PREVIEWS_DIR, "page")]
    subprocess.run(cmd, check=True)
    print(f"[OK] Rendered preview images in {PREVIEWS_DIR}")

    # Copy to brain dir
    for i in range(1, 9):
        src = os.path.join(PREVIEWS_DIR, f"page-{i}.png")
        dst = os.path.join(brain_dir, f"fatir_mindmap_page_{i}.png")
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[OK] Copied plate {i} preview to {dst}")

if __name__ == "__main__":
    build_fatir_pdf()
