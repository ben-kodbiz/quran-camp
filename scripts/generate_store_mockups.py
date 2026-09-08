#!/usr/bin/env python3
"""
HUURS STUDIO - Digital Storefront Product Mockup Generator
===========================================================
Generates ultra-high-resolution, editorial product display cards and
3D-style book mockups for Gumroad and Lemon Squeezy.

Conforms strictly to:
- Brand_Visual_System.md (Nature + Knowledge + Reflection + Tranquility)
- Slate `#0B0F17`, Card `#131A26`, Warm Gold `#C5A059`, Cream `#E2E8F0`
- Typography: IBM Plex Serif & IBM Plex Sans
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = "/mnt/AI/ag/Campaign/12_PRODUCTS/store/assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SERIF_BOLD = "/usr/share/fonts/truetype/ibm-plex/IBMPlexSerif-Bold.ttf"
SERIF_MED = "/usr/share/fonts/truetype/ibm-plex/IBMPlexSerif-Medium.ttf"
SERIF_REG = "/usr/share/fonts/truetype/ibm-plex/IBMPlexSerif-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/ibm-plex/IBMPlexSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/ibm-plex/IBMPlexSans-Regular.ttf"

# Color Palette
BG_DARK = (11, 15, 23)        # #0B0F17
BG_CARD = (19, 26, 38)        # #131A26
BG_LIGHT_CARD = (26, 35, 51)  # #1A2333
GOLD_ACCENT = (197, 160, 89)  # #C5A059
GOLD_LIGHT = (229, 195, 132)  # #E5C384
TEXT_MAIN = (226, 232, 240)   # #E2E8F0
TEXT_MUTED = (148, 163, 184)  # #94A3B8
BORDER_COL = (35, 45, 63)     # #232D3F

def create_product_card(title, subtitle, badge_text, tag_text, price_str, output_filename, is_wide=False):
    width, height = (1280, 720) if is_wide else (800, 1100)
    img = Image.new("RGBA", (width, height), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Ambient subtle gradient / border frame
    margin = 35
    draw.rectangle([margin, margin, width - margin, height - margin], fill=BG_CARD, outline=BORDER_COL, width=2)
    
    # Elegant inner gold hairline
    inner_margin = margin + 12
    draw.rectangle([inner_margin, inner_margin, width - inner_margin, height - inner_margin], outline=(GOLD_ACCENT[0], GOLD_ACCENT[1], GOLD_ACCENT[2], 80), width=1)

    # Top Brand Header
    font_brand = ImageFont.truetype(SERIF_MED, 18)
    brand_text = "HUURS STUDIO  •  COME BACK TO THE QUR'AN"
    draw.text((width // 2, margin + 45), brand_text, fill=GOLD_ACCENT, font=font_brand, anchor="mm")

    # Category Tag / Badge
    font_badge = ImageFont.truetype(SANS_BOLD, 14)
    badge_bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = badge_bbox[2] - badge_bbox[0] + 30
    bh = badge_bbox[3] - badge_bbox[1] + 16
    bx = (width - bw) // 2
    by = margin + 85
    draw.rectangle([bx, by, bx + bw, by + bh], fill=BG_LIGHT_CARD, outline=GOLD_ACCENT, width=1)
    draw.text((bx + bw // 2, by + bh // 2), badge_text, fill=GOLD_LIGHT, font=font_badge, anchor="mm")

    # Central Book Spine / Geometry Accent (Decorative Book Silhouette)
    book_w = 340 if not is_wide else 420
    book_h = 440 if not is_wide else 320
    book_x = (width - book_w) // 2
    book_y = (height - book_h) // 2 - 20 if not is_wide else (height - book_h) // 2 + 10

    # Draw simulated book shadow
    shadow_offset = 12
    draw.rectangle([book_x + shadow_offset, book_y + shadow_offset, book_x + book_w + shadow_offset, book_y + book_h + shadow_offset], fill=(5, 8, 12, 180))
    # Draw book surface
    draw.rectangle([book_x, book_y, book_x + book_w, book_y + book_h], fill=(15, 20, 30), outline=GOLD_ACCENT, width=2)
    # Book spine line
    draw.line([(book_x + 30, book_y), (book_x + 30, book_y + book_h)], fill=BORDER_COL, width=2)

    # Book Title on Cover
    font_cover_title = ImageFont.truetype(SERIF_BOLD, 26 if not is_wide else 30)
    font_cover_sub = ImageFont.truetype(SERIF_REG, 15)
    
    draw.text((book_x + 45 + (book_w - 45)//2, book_y + 80), title, fill=TEXT_MAIN, font=font_cover_title, anchor="mm", align="center")
    
    # Gold decorative divider
    div_y = book_y + 130
    cx = book_x + 45 + (book_w - 45)//2
    draw.line([(cx - 40, div_y), (cx + 40, div_y)], fill=GOLD_ACCENT, width=1)
    
    # Subtitle on Book
    draw.text((cx, div_y + 40), subtitle, fill=TEXT_MUTED, font=font_cover_sub, anchor="mm", align="center")

    # Lower Badge on Book
    draw.text((cx, book_y + book_h - 40), tag_text, fill=GOLD_ACCENT, font=font_brand, anchor="mm")

    # Bottom Metadata & Price Tag
    if not is_wide:
        price_y = height - margin - 80
        font_price = ImageFont.truetype(SERIF_BOLD, 36)
        font_license = ImageFont.truetype(SANS_REG, 13)
        draw.text((width // 2, price_y), price_str, fill=GOLD_LIGHT, font=font_price, anchor="mm")
        draw.text((width // 2, price_y + 40), "Instant Digital Download  •  Kindle, Apple Books, PDF & Notion Ready", fill=TEXT_MUTED, font=font_license, anchor="mm")
    else:
        # For wide card: metadata on side
        font_price = ImageFont.truetype(SERIF_BOLD, 38)
        font_license = ImageFont.truetype(SANS_REG, 14)
        draw.text((width // 2, height - margin - 50), f"{price_str}  •  Instant Lifetime Access", fill=GOLD_LIGHT, font=font_price, anchor="mm")

    out_path = os.path.join(OUTPUT_DIR, output_filename)
    img.save(out_path, "PNG")
    print(f"✅ Generated Mockup: {output_filename} ({width}x{height})")

def main():
    print("===========================================================================")
    print("      HUURS STUDIO - GENERATING STOREFRONT PRODUCT DISPLAY MOCKUPS         ")
    print("===========================================================================\n")

    # 1. Master Ebook Cover
    create_product_card(
        title="COME BACK TO\nTHE QUR'AN",
        subtitle="114 Surahs Unveiled\nOne Day at a Time",
        badge_text="OFFICIAL MASTER EDITION",
        tag_text="COMPLETE 114-SURAH MANUSCRIPT",
        price_str="$19 USD",
        output_filename="cover_ebook_master.png"
    )

    # 2. 30-Day Guided Workbook Cover
    create_product_card(
        title="30 DAYS BACK TO\nTHE QUR'AN",
        subtitle="A Guided Contemplation Journal\n& Daily Habit Tracker",
        badge_text="WORKBOOK & HABIT SYSTEM",
        tag_text="PRINT-READY A4 + DIGITAL",
        price_str="$9 USD",
        output_filename="cover_journal_30d.png"
    )

    # 3. 7-Day Free Guide Lead Magnet
    create_product_card(
        title="7 DAYS BACK TO\nTHE QUR'AN",
        subtitle="A Quiet Journey to\nReconnect Your Heart",
        badge_text="FREE LEAD MAGNET",
        tag_text="100% FREE INTRODUCTORY GUIDE",
        price_str="FREE DOWNLOAD ($0)",
        output_filename="cover_guide_7d.png"
    )

    # 4. VIP Complete Master Ecosystem Card (Wide format 1280x720)
    create_product_card(
        title="THE COMPLETE MASTER\nECOSYSTEM BUNDLE",
        subtitle="EPUB 3 + Manuscript + 30-Day Workbook + 7-Day Guide\nOffline Web Reader + Audio Narration Guides",
        badge_text="VIP LIFETIME ACCESS",
        tag_text="ALL 4 DIGITAL PRODUCTS INCLUDED",
        price_str="$47 USD",
        output_filename="bundle_vip_card.png",
        is_wide=True
    )

    print(f"\nAll 4 storefront mockups successfully rendered in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
