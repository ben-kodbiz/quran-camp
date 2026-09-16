import os, sys, re, json
from bs4 import BeautifulSoup

BASE_DIR = "/mnt/AI/ag/Campaign"
MINDMAP_DIR = os.path.join(BASE_DIR, "07_MINDMAP")
PRODUCTS_DIR = os.path.join(BASE_DIR, "12_PRODUCTS")
OUTPUT_HTML = os.path.join(PRODUCTS_DIR, "SURAH_AL_BAQARAH_INTERACTIVE_SUITE.html")

PART_METADATA = [
    {
        "part": 1,
        "title": "Epistemology of Revelation & Three Archetypes",
        "plates": "Plates 03 - 06",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Epistemology & Creed",
        "showcase": None
    },
    {
        "part": 2,
        "title": "Adam, Knowledge & The Primordial Trial",
        "plates": "Plates 07 - 10",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Genesis & Covenant",
        "showcase": None
    },
    {
        "part": 3,
        "title": "Sinai Covenant, Wilderness & The Heifer",
        "plates": "Plates 11 - 14",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Covenant & Law",
        "showcase": None
    },
    {
        "part": 4,
        "title": "Hardened Hearts, Tahreef & Moral Decalogue",
        "plates": "Plates 15 - 18",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Historical Critique",
        "showcase": None
    },
    {
        "part": 5,
        "title": "Tribal Sedition, Solomon & Babylonian Occult",
        "plates": "Plates 19 - 22",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Prophetic Defense",
        "showcase": None
    },
    {
        "part": 6,
        "title": "Linguistic Hygiene, Naskh & Universal Creed",
        "plates": "Plates 23 - 26",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Legal Abrogation",
        "showcase": None
    },
    {
        "part": 7,
        "title": "Trial of Ibrahim & Foundation of the Ka'bah",
        "plates": "Plates 27 - 30",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Abrahamic Heritage",
        "showcase": None
    },
    {
        "part": 8,
        "title": "Legacy of Ya'qub, Millat Ibrahim & Sibghatullah",
        "plates": "Plates 31 - 34",
        "cycle": "CYCLE 1 : THE CREED & ANCIENT NATIONS",
        "tag": "Primordial Baptism",
        "showcase": None
    },
    {
        "part": 9,
        "title": "Qiblah Reorientation & Sacred Martyrdom",
        "plates": "Plates 35 - 38",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Middle Nation",
        "showcase": None
    },
    {
        "part": 10,
        "title": "Safa & Marwah, Concealing Truth & Pure Halal",
        "plates": "Plates 39 - 42",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Sacred Rites",
        "showcase": None
    },
    {
        "part": 11,
        "title": "Dietary Boundaries & The Constitution of Birr",
        "plates": "Plates 43 - 46",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Holistic Piety",
        "showcase": None
    },
    {
        "part": 12,
        "title": "Retribution, Wills & Ramadan Fasting",
        "plates": "Plates 47 - 50",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Civil Governance",
        "showcase": None
    },
    {
        "part": 13,
        "title": "Sacred Defense & Just Warfare Ethics",
        "plates": "Plates 51 - 54",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Sanctity & Restraint",
        "showcase": None
    },
    {
        "part": 14,
        "title": "Pilgrimage Ordinances & Wholehearted Islam",
        "plates": "Plates 55 - 58",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Sacred Assembly",
        "showcase": None
    },
    {
        "part": 15,
        "title": "Adversity, Infaq Categories & Social Governance",
        "plates": "Plates 59 - 62",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Charity & Social Order",
        "showcase": None
    },
    {
        "part": 16,
        "title": "Family Sanctity, Marriage & Talaq Charters",
        "plates": "Plates 63 - 66",
        "cycle": "CYCLE 2 : SACRED LAW & COMMUNITY",
        "tag": "Matrimonial Law",
        "showcase": None
    },
    {
        "part": 17,
        "title": "Talut, Goliath & AYAT AL-KURSI",
        "plates": "Plates 67 - 70",
        "cycle": "CYCLES 2 & 3 : SOVEREIGNTY & VICTORY",
        "tag": "Throne Verse Showcase",
        "showcase": "Ayat al-Kursi"
    },
    {
        "part": 18,
        "title": "Conscience, Resurrection & Infaq Economy",
        "plates": "Plates 71 - 74",
        "cycle": "CYCLE 3 : ECONOMIC JUSTICE & SEAL",
        "tag": "Economic Sanctity",
        "showcase": None
    },
    {
        "part": 19,
        "title": "Usury War, Debt Charter & LAST 2 VERSES",
        "plates": "Plates 75 - 78",
        "cycle": "CYCLE 3 : ECONOMIC JUSTICE & SEAL",
        "tag": "Crowning Seal Showcase",
        "showcase": "The Last Two Verses"
    },
]

def parse_pdf_script(path):
    with open(path) as f:
        text = f.read()
    pages_raw = text.split("pdf.new_page(w, h)")
    pages = []
    for p_idx, p_text in enumerate(pages_raw[1:], 1):
        chrome_match = re.search(r"draw_chrome\s*\(\s*\d+,\s*\d+,\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*\"([^\"]+)\"", p_text)
        p_title = chrome_match.group(1) if chrome_match else f"Page {p_idx}"
        p_desc = chrome_match.group(2) if chrome_match else ""
        p_sec = chrome_match.group(3) if chrome_match else ""
        
        pillar_matches = list(re.finditer(r"pdf\.text\(\"(PILLAR \d+:[^\"]+)\",\s*[^,]+,\s*[^,]+,\s*font=\"F2\",\s*size=[^,]+,\s*rgb=(\w+)\)", p_text))
        pillars = []
        for i, pm in enumerate(pillar_matches):
            p_name = pm.group(1)
            color_var = pm.group(2).lower()
            if color_var not in ["gold", "cyan", "purple", "emerald", "rose"]:
                color_var = "gold"
            start_pos = pm.end()
            end_pos = pillar_matches[i+1].start() if i + 1 < len(pillar_matches) else len(p_text)
            pillar_chunk = p_text[start_pos:end_pos]
            
            sub_m = re.search(r"pdf\.text\(\"([^\"]+)\",\s*[^,]+,\s*[^,]+,\s*font=\"F3\"", pillar_chunk)
            p_sub = sub_m.group(1) if sub_m else ""
            
            cards = []
            card_matches = list(re.finditer(r"pdf\.text\(\"(\d+\.\s*[^\"]+)\",", pillar_chunk))
            for c_i, cm in enumerate(card_matches):
                c_title = cm.group(1)
                c_start = cm.end()
                c_end = card_matches[c_i+1].start() if c_i + 1 < len(card_matches) else len(pillar_chunk)
                card_chunk = pillar_chunk[c_start:c_end]
                
                para_m = re.search(r"t\s*=\s*\((.*?)\)\s*\n\s*pdf\.paragraph", card_chunk, re.DOTALL)
                bullets = []
                if para_m:
                    raw_para = para_m.group(1)
                    str_matches = re.findall(r"\"([^\"]+)\"", raw_para)
                    full_text = "".join(str_matches)
                    lines = [line.strip().lstrip("-*• ").strip() for line in full_text.split("\\n") if line.strip()]
                    bullets = lines
                cards.append({"title": c_title, "bullets": bullets})
            pillars.append({"name": p_name, "sub": p_sub, "color": color_var, "cards": cards})
        pages.append({"page": p_idx, "title": p_title, "desc": p_desc, "sec": p_sec, "pillars": pillars})
    return pages

def parse_html_part(part_num):
    fpath = os.path.join(MINDMAP_DIR, f"BAQARAH_PART_{part_num:02d}_MINDMAP.html")
    with open(fpath) as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    pages = []
    for p_idx, page_div in enumerate(soup.find_all("div", class_="page-section"), 1):
        sec_header = page_div.find("div", class_="section-header")
        p_title = sec_header.find("h2").get_text(strip=True) if sec_header and sec_header.find("h2") else f"Page {p_idx}"
        p_desc = sec_header.find("p").get_text(strip=True) if sec_header and sec_header.find("p") else ""
        meta_part = sec_header.find("div", class_="meta-part").get_text(strip=True) if sec_header and sec_header.find("div", class_="meta-part") else ""
        
        pillars = []
        for pillar_col in page_div.find_all("div", class_="pillar-column"):
            p_header = pillar_col.find("div", class_="pillar-header")
            color_class = "gold"
            if p_header:
                classes = p_header.get("class", [])
                for c in ["gold", "cyan", "purple", "emerald", "rose"]:
                    if c in classes:
                        color_class = c
                        break
            p_title_div = pillar_col.find("div", class_="pillar-title")
            p_name = p_title_div.find("h3").get_text(strip=True) if p_title_div and p_title_div.find("h3") else ""
            p_sub = p_title_div.find("p").get_text(strip=True) if p_title_div and p_title_div.find("p") else ""
            
            cards = []
            for card in pillar_col.find_all("div", class_="info-card"):
                c_num = card.find("div", class_="card-num").get_text(strip=True) if card.find("div", class_="card-num") else ""
                bullets = [li.get_text(strip=True) for li in card.find_all("li")]
                cards.append({"title": c_num, "bullets": bullets})
            pillars.append({"name": p_name, "sub": p_sub, "color": color_class, "cards": cards})
        pages.append({"page": p_idx, "title": p_title, "desc": p_desc, "sec": meta_part, "pillars": pillars})
    return pages

dataset = []
for meta in PART_METADATA:
    p_num = meta["part"]
    if p_num in [1, 2, 3, 5]:
        script_path = os.path.join(MINDMAP_DIR, f"build_baqarah_part{p_num:02d}_pdf.py")
        pages = parse_pdf_script(script_path)
    else:
        pages = parse_html_part(p_num)
    
    dataset.append({
        **meta,
        "pages": pages
    })

dataset_json = json.dumps(dataset, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Surah Al-Baqarah — Master Interactive Digital Compendium | Huurs Studio</title>
  <style>
    :root {{
      --navy-deep: #060a12;
      --navy-card: #0d1422;
      --navy-elevated: #141e32;
      --navy-hover: #1c2a44;
      --gold: #d4af37;
      --gold-light: #e8d194;
      --gold-glow: rgba(212, 175, 55, 0.25);
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.2);
      --purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.2);
      --emerald: #10b981;
      --rose: #f43f5e;
      --white: #f8fafc;
      --text-muted: #adc0d4;
      --border-muted: #243247;
      --border-gold: rgba(212, 175, 55, 0.4);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background-color: var(--navy-deep);
      color: var(--white);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* HEADER */
    header {{
      background: var(--navy-card);
      border-bottom: 2px solid var(--gold);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      gap: 16px;
    }}

    .header-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 280px;
    }}

    .brand-crest {{
      width: 36px;
      height: 36px;
      border: 1.5px solid var(--gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 800;
      color: var(--gold);
      background: rgba(212, 175, 55, 0.08);
      border-radius: 4px;
      box-shadow: 0 0 10px var(--gold-glow);
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .brand-name {{
      font-size: 14px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }}

    .brand-sub {{
      font-size: 11px;
      color: var(--text-muted);
      letter-spacing: 0.5px;
    }}

    /* SEARCH BAR */
    .search-wrapper {{
      flex: 1;
      max-width: 520px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 20px;
      padding: 8px 16px 8px 36px;
      color: var(--white);
      font-size: 13px;
      outline: none;
      transition: all 0.2s ease;
    }}

    .search-input:focus {{
      border-color: var(--gold);
      box-shadow: 0 0 12px var(--gold-glow);
    }}

    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 13px;
      color: var(--text-muted);
      pointer-events: none;
    }}

    .search-clear {{
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 12px;
      color: var(--text-muted);
      cursor: pointer;
      display: none;
    }}

    /* HEADER ACTIONS */
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn {{
      padding: 7px 14px;
      font-size: 12px;
      font-weight: 600;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}

    .btn-gold {{
      background: linear-gradient(135deg, var(--gold), #b8972f);
      color: var(--navy-deep);
      border: none;
    }}

    .btn-gold:hover {{
      background: linear-gradient(135deg, var(--gold-light), var(--gold));
      box-shadow: 0 0 12px var(--gold-glow);
    }}

    .btn-outline {{
      background: transparent;
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
    }}

    .btn-outline:hover {{
      border-color: var(--gold);
      color: var(--white);
      background: rgba(212, 175, 55, 0.08);
    }}

    .btn-showcase-1 {{
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid var(--cyan);
      color: var(--cyan);
    }}

    .btn-showcase-1:hover {{
      background: var(--cyan);
      color: var(--navy-deep);
      box-shadow: 0 0 12px var(--cyan-glow);
    }}

    .btn-showcase-2 {{
      background: rgba(168, 85, 247, 0.12);
      border: 1px solid var(--purple);
      color: var(--purple);
    }}

    .btn-showcase-2:hover {{
      background: var(--purple);
      color: var(--navy-deep);
      box-shadow: 0 0 12px var(--purple-glow);
    }}

    /* APP LAYOUT */
    .app-container {{
      display: flex;
      flex: 1;
      height: calc(100vh - 62px);
      overflow: hidden;
    }}

    /* SIDEBAR */
    .sidebar {{
      width: 320px;
      background: var(--navy-card);
      border-right: 1px solid var(--border-muted);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      overflow: hidden;
    }}

    .sidebar-header {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-deep);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sidebar-title {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      color: var(--gold);
      text-transform: uppercase;
    }}

    .sidebar-badge {{
      font-size: 10px;
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      padding: 2px 6px;
      border-radius: 3px;
      font-weight: 600;
    }}

    .parts-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px 8px;
    }}

    .cycle-divider {{
      padding: 10px 10px 4px 10px;
      font-size: 9.5px;
      font-weight: 700;
      color: var(--gold-light);
      letter-spacing: 1px;
      text-transform: uppercase;
      opacity: 0.8;
    }}

    .part-item {{
      padding: 10px 12px;
      margin-bottom: 4px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 3px;
      border: 1px solid transparent;
      transition: all 0.15s ease;
    }}

    .part-item:hover {{
      background: var(--navy-hover);
      border-color: var(--border-muted);
    }}

    .part-item.active {{
      background: var(--navy-elevated);
      border-color: var(--gold);
      box-shadow: inset 3px 0 0 var(--gold);
    }}

    .part-item-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .part-num {{
      font-size: 10.5px;
      font-weight: 700;
      color: var(--gold);
    }}

    .part-plates {{
      font-size: 9px;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.05);
      padding: 1px 5px;
      border-radius: 2px;
    }}

    .part-title-text {{
      font-size: 12px;
      font-weight: 600;
      color: var(--white);
      line-height: 1.3;
    }}

    .part-item.showcase-1 .part-num {{
      color: var(--cyan);
    }}
    .part-item.showcase-1.active {{
      border-color: var(--cyan);
      box-shadow: inset 3px 0 0 var(--cyan);
    }}

    .part-item.showcase-2 .part-num {{
      color: var(--purple);
    }}
    .part-item.showcase-2.active {{
      border-color: var(--purple);
      box-shadow: inset 3px 0 0 var(--purple);
    }}

    .showcase-tag {{
      display: inline-flex;
      align-items: center;
      gap: 3px;
      font-size: 8.5px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 1px 4px;
      border-radius: 2px;
      margin-top: 2px;
      width: fit-content;
    }}
    .tag-cyan {{ background: rgba(56, 189, 248, 0.15); color: var(--cyan); }}
    .tag-purple {{ background: rgba(168, 85, 247, 0.15); color: var(--purple); }}

    /* MAIN VIEWPORT */
    .main-viewport {{
      flex: 1;
      overflow-y: auto;
      background: var(--navy-deep);
      padding: 20px 28px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    /* PART BANNER */
    .part-banner {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      overflow: hidden;
    }}

    .part-banner::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--gold);
    }}

    .part-banner.showcase-1::before {{ background: var(--cyan); }}
    .part-banner.showcase-2::before {{ background: var(--purple); }}

    .banner-left {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .banner-meta {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .badge-part {{
      font-size: 11px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 1px;
    }}

    .badge-cycle {{
      font-size: 10px;
      color: var(--text-muted);
      background: var(--navy-elevated);
      padding: 2px 8px;
      border-radius: 3px;
      border: 1px solid var(--border-muted);
    }}

    .banner-title {{
      font-size: 20px;
      font-weight: 700;
      color: var(--white);
      letter-spacing: 0.5px;
    }}

    .banner-anchors {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .banner-anchors span {{
      color: var(--gold-light);
      font-weight: 600;
    }}

    .banner-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    /* PAGE TABS */
    .page-nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 8px 14px;
    }}

    .tabs-group {{
      display: flex;
      gap: 8px;
    }}

    .page-tab-btn {{
      padding: 8px 18px;
      font-size: 12px;
      font-weight: 600;
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      color: var(--text-muted);
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .page-tab-btn:hover {{
      color: var(--white);
      border-color: var(--gold);
    }}

    .page-tab-btn.active {{
      background: rgba(212, 175, 55, 0.12);
      border-color: var(--gold);
      color: var(--gold);
      box-shadow: 0 0 10px var(--gold-glow);
    }}

    .view-toggle-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .toggle-btn {{
      font-size: 11.5px;
      color: var(--text-muted);
      background: transparent;
      border: 1px solid var(--border-muted);
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .toggle-btn:hover, .toggle-btn.active {{
      background: var(--navy-elevated);
      color: var(--white);
      border-color: var(--text-muted);
    }}

    /* PAGE CONTAINER */
    .page-display {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .page-card {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .page-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid var(--border-muted);
      padding-bottom: 12px;
    }}

    .page-heading h3 {{
      font-size: 15px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .page-heading p {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .page-sec-badge {{
      font-size: 10.5px;
      font-weight: 700;
      color: var(--gold-light);
      background: var(--navy-elevated);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid var(--border-muted);
    }}

    /* 2 PILLARS GRID */
    .pillars-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}

    @media (max-width: 1024px) {{
      .pillars-container {{ grid-template-columns: 1fr; }}
    }}

    .pillar-box {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .pillar-header {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-muted);
      background: rgba(255, 255, 255, 0.02);
    }}

    .pillar-header.gold {{ border-top: 3px solid var(--gold); }}
    .pillar-header.cyan {{ border-top: 3px solid var(--cyan); }}
    .pillar-header.purple {{ border-top: 3px solid var(--purple); }}
    .pillar-header.emerald {{ border-top: 3px solid var(--emerald); }}
    .pillar-header.rose {{ border-top: 3px solid var(--rose); }}

    .pillar-title {{
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .pillar-header.gold .pillar-title {{ color: var(--gold); }}
    .pillar-header.cyan .pillar-title {{ color: var(--cyan); }}
    .pillar-header.purple .pillar-title {{ color: var(--purple); }}
    .pillar-header.emerald .pillar-title {{ color: var(--emerald); }}
    .pillar-header.rose .pillar-title {{ color: var(--rose); }}

    .pillar-sub {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .cards-stack {{
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .card-item {{
      background: var(--navy-card);
      border: 1px solid var(--border-muted);
      border-radius: 5px;
      padding: 10px 14px;
      transition: all 0.2s ease;
    }}

    .card-item:hover {{
      border-color: var(--border-gold);
      transform: translateY(-1px);
    }}

    .card-item.highlight-pulse {{
      animation: pulseHighlight 2s ease infinite;
    }}

    @keyframes pulseHighlight {{
      0% {{ border-color: var(--gold); box-shadow: 0 0 5px var(--gold-glow); }}
      50% {{ border-color: var(--cyan); box-shadow: 0 0 15px var(--cyan-glow); }}
      100% {{ border-color: var(--gold); box-shadow: 0 0 5px var(--gold-glow); }}
    }}

    .card-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--white);
      margin-bottom: 6px;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }}

    .card-title span.num {{
      color: var(--gold);
      font-size: 11.5px;
    }}

    .card-bullets {{
      list-style-type: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .card-bullets li {{
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.45;
      position: relative;
      padding-left: 14px;
    }}

    .card-bullets li::before {{
      content: "•";
      position: absolute;
      left: 2px;
      color: var(--gold);
      font-size: 12px;
    }}

    /* SEARCH RESULTS MODAL/DROPDOWN */
    .search-results-panel {{
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      margin-top: 6px;
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 8px;
      max-height: 420px;
      overflow-y: auto;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.7);
      z-index: 2000;
      display: none;
    }}

    .search-results-panel.open {{
      display: block;
    }}

    .search-meta-bar {{
      padding: 8px 14px;
      font-size: 11px;
      font-weight: 700;
      color: var(--gold);
      background: var(--navy-elevated);
      border-bottom: 1px solid var(--border-muted);
      display: flex;
      justify-content: space-between;
    }}

    .search-item {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-muted);
      cursor: pointer;
      transition: background 0.15s ease;
    }}

    .search-item:hover {{
      background: var(--navy-hover);
    }}

    .search-item-header {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 2px;
    }}

    .search-item-location {{
      font-size: 9.5px;
      color: var(--cyan);
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .search-item-snippet {{
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.35;
    }}

    .highlight-term {{
      background: rgba(212, 175, 55, 0.35);
      color: var(--white);
      padding: 0 2px;
      border-radius: 2px;
      font-weight: 600;
    }}

    /* FULL MODAL STYLES */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(6, 10, 18, 0.85);
      backdrop-filter: blur(6px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 3000;
      padding: 20px;
    }}

    .modal-backdrop.open {{
      display: flex;
    }}

    .modal-content {{
      background: var(--navy-card);
      border: 1px solid var(--gold);
      border-radius: 10px;
      max-width: 900px;
      width: 100%;
      max-height: 88vh;
      overflow-y: auto;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8);
      position: relative;
      display: flex;
      flex-direction: column;
    }}

    .modal-header {{
      padding: 16px 24px;
      border-bottom: 1px solid var(--border-muted);
      background: var(--navy-elevated);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-title {{
      font-size: 16px;
      font-weight: 700;
      color: var(--gold);
      letter-spacing: 0.5px;
    }}

    .modal-close {{
      background: transparent;
      border: none;
      font-size: 20px;
      color: var(--text-muted);
      cursor: pointer;
      line-height: 1;
    }}

    .modal-close:hover {{
      color: var(--white);
    }}

    .modal-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      font-size: 13px;
      line-height: 1.6;
      color: var(--text-muted);
    }}

    .modal-body h4 {{
      font-size: 14px;
      color: var(--white);
      border-left: 3px solid var(--gold);
      padding-left: 8px;
      margin-bottom: 6px;
    }}

    .modal-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}

    .modal-card {{
      background: var(--navy-elevated);
      border: 1px solid var(--border-muted);
      border-radius: 6px;
      padding: 14px;
    }}

    .modal-card-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 6px;
    }}

    /* FOOTER */
    footer {{
      background: var(--navy-card);
      border-top: 1px solid var(--border-muted);
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--text-muted);
    }}

    .footer-gold {{
      color: var(--gold);
      font-weight: 600;
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="header-brand">
      <div class="brand-crest">H</div>
      <div class="brand-text">
        <div class="brand-name">Huurs Studio</div>
        <div class="brand-sub">Deeper Thought Campaign &bull; Read. Reflect. Return.</div>
      </div>
    </div>

    <!-- GLOBAL SEARCH -->
    <div class="search-wrapper">
      <span class="search-icon">🔍</span>
      <input type="text" id="globalSearch" class="search-input" placeholder="Search across all 608 conceptual cards & 152 pillars..." autocomplete="off">
      <span id="searchClear" class="search-clear">✕</span>
      <div id="searchResults" class="search-results-panel"></div>
    </div>

    <!-- ACTIONS -->
    <div class="header-actions">
      <button class="btn btn-showcase-1" onclick="openModal('modalAyatKursi')">👑 Ayat al-Kursi</button>
      <button class="btn btn-showcase-2" onclick="openModal('modalLastVerses')">🛡️ Last Two Verses</button>
      <button class="btn btn-outline" onclick="openModal('modalSunniAudit')">📜 Sunni Audit</button>
      <a href="./SURAH_AL_BAQARAH_MASTER_COMPENDIUM.pdf" target="_blank" class="btn btn-gold">📥 Master PDF (78 Plates)</a>
    </div>
  </header>

  <!-- APP CONTAINER -->
  <div class="app-container">
    <!-- SIDEBAR -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <span class="sidebar-title">Surah Al-Baqarah Suite</span>
        <span class="sidebar-badge">19 Canonical Parts</span>
      </div>
      <div class="parts-list" id="partsList">
        <!-- Injected via JS -->
      </div>
    </aside>

    <!-- MAIN VIEWPORT -->
    <main class="main-viewport" id="mainViewport">
      <!-- PART BANNER -->
      <section class="part-banner" id="partBanner">
        <div class="banner-left">
          <div class="banner-meta">
            <span class="badge-part" id="bannerPartBadge">PART 01 OF 19</span>
            <span class="badge-cycle" id="bannerCycleBadge">CYCLE 1</span>
            <span class="badge-cycle" id="bannerPlatesBadge">Plates 03 - 06</span>
          </div>
          <h1 class="banner-title" id="bannerTitle">Part Title</h1>
          <div class="banner-anchors">
            Sunni Exegetical Anchors: <span>Tafsir Ibn Kathir &bull; Jami' al-Bayan (Al-Tabari) &bull; Al-Jami' li-Ahkam al-Qur'an (Al-Qurtubi) &bull; Mafatih al-Ghayb (Al-Razi)</span>
          </div>
        </div>
        <div class="banner-right">
          <a id="partPdfBtn" href="#" target="_blank" class="btn btn-outline">📄 Part PDF</a>
        </div>
      </section>

      <!-- PAGE NAV BAR -->
      <div class="page-nav-bar">
        <div class="tabs-group" id="pageTabsGroup">
          <button class="page-tab-btn active" onclick="switchPage(1)">
            <span>Page 01</span>
            <small style="opacity:0.7;">Pillars 1 & 2</small>
          </button>
          <button class="page-tab-btn" onclick="switchPage(2)">
            <span>Page 02</span>
            <small style="opacity:0.7;">Pillars 3 & 4</small>
          </button>
          <button class="page-tab-btn" onclick="switchPage(3)">
            <span>Page 03</span>
            <small style="opacity:0.7;">Pillars 5 & 6</small>
          </button>
          <button class="page-tab-btn" onclick="switchPage(4)">
            <span>Page 04</span>
            <small style="opacity:0.7;">Pillars 7 & 8</small>
          </button>
        </div>
        <div class="view-toggle-group">
          <button id="viewToggleBtn" class="toggle-btn" onclick="toggleExpandAll()">👁️ Show All 4 Pages</button>
        </div>
      </div>

      <!-- PAGE DISPLAY -->
      <section class="page-display" id="pageDisplay">
        <!-- Rendered via JS -->
      </section>
    </main>
  </div>

  <!-- FOOTER -->
  <footer>
    <div>HUURS KNOWLEDGE SYSTEMS &bull; AUTHENTIC SUNNI SOURCE DISCIPLINE &bull; ZERO TIMESTAMPS &bull; ZERO PERSONALITY CULT</div>
    <div class="footer-gold">SURAH AL-BAQARAH MASTER DIGITAL ARCHITECTURE &bull; 78 PLATES &bull; 152 PILLARS &bull; 608 CARDS</div>
  </footer>

  <!-- MODAL: AYAT AL-KURSI -->
  <div class="modal-backdrop" id="modalAyatKursi">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">👑 SHOWCASE I: AYAT AL-KURSI — THE THRONE VERSE (PART 17)</div>
        <button class="modal-close" onclick="closeModal('modalAyatKursi')">&times;</button>
      </div>
      <div class="modal-body">
        <div>
          <h4>The Supreme Ayah of the Holy Qur'an</h4>
          <p>
            When the Prophet (peace be upon him) asked Ubayy ibn Ka'b: <em>"Which ayah in the Book of Allah with you is the greatest?"</em> Ubayy answered: <em>"Allahu la ilaha illa Huwa al-Hayy al-Qayyum."</em> The Prophet struck him upon the chest and said: <em>"May knowledge be joyful and sweet for you, O Abu al-Mundhir!"</em> (Sahih Muslim).
          </p>
        </div>

        <div class="modal-grid">
          <div class="modal-card">
            <div class="modal-card-title">Concentric Ring Composition (Chiasmus)</div>
            <p>Ayat al-Kursi is structured across 10 perfect clauses organized in symmetrical mirror pairs:</p>
            <ul style="margin-top:6px; padding-left:16px; font-size:11.5px; color:var(--text-muted); display:flex; flex-direction:column; gap:4px;">
              <li><strong>A:</strong> Monotheism & Self-Subsistence (Allahu la ilaha illa Huwa al-Hayy al-Qayyum)</li>
              <li><strong>B:</strong> Eternal Wakefulness (Neither slumber nor sleep overtakes Him)</li>
              <li><strong>C:</strong> Absolute Dominion (To Him belongs whatever is in the heavens and earth)</li>
              <li><strong>D:</strong> Sovereign Authorization (Who can intercede except by His permission?)</li>
              <li><strong>E (Center Pivot):</strong> Omniscient Knowledge of past and future</li>
              <li><strong>D':</strong> Human Epistemological Limitation (They encompass none of His knowledge except what He wills)</li>
              <li><strong>C':</strong> Cosmic Throne Expansiveness (His Kursi encompasses the heavens and the earth)</li>
              <li><strong>B':</strong> Effortless Preservation (Their preservation tires Him not)</li>
              <li><strong>A':</strong> Supreme Transcendence (He is the Most High, the Most Great)</li>
            </ul>
          </div>

          <div class="modal-card">
            <div class="modal-card-title">Classical Sunni Exegetical Anchors</div>
            <ul style="padding-left:16px; font-size:11.5px; color:var(--text-muted); display:flex; flex-direction:column; gap:6px;">
              <li><strong>Ibn Kathir:</strong> Confirms that <em>Al-Hayy</em> is the Ever-Living who never dies, and <em>Al-Qayyum</em> is the Self-Sustaining Maintainer of all existing things, without whom nothing could subsist for a fraction of a second.</li>
              <li><strong>Al-Qurtubi:</strong> Details that the <em>Kursi</em> is not a seat of physical resting, but a colossal celestial creation of magnificent grandeur demonstrating divine omnipotence, as Ibn Abbas explained: <em>"The seven heavens compared to the Kursi are like a small coin tossed into a vast desert."</em></li>
              <li><strong>Sahih al-Bukhari:</strong> Abu Hurairah's encounter with the intruder at the charity storehouse, where the Prophet (peace be upon him) confirmed: <em>"When you go to bed, recite Ayat al-Kursi, for Allah will appoint a guardian angel over you, and no devil will approach you until morning."</em></li>
            </ul>
          </div>
        </div>

        <div style="text-align:right;">
          <button class="btn btn-showcase-1" onclick="jumpToPart(17); closeModal('modalAyatKursi');">Explore Part 17 Plates &rarr;</button>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: THE LAST TWO VERSES -->
  <div class="modal-backdrop" id="modalLastVerses">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">🛡️ SHOWCASE II: THE LAST TWO VERSES — AMANAR-RASOOL (PART 19)</div>
        <button class="modal-close" onclick="closeModal('modalLastVerses')">&times;</button>
      </div>
      <div class="modal-body">
        <div>
          <h4>The Crowning Seal & Nocturnal Ascension Gift</h4>
          <p>
            Abdullah ibn Mas'ud narrated that during the Night of Ascension (<em>Al-Isra' wal-Mi'raj</em>), the Messenger of Allah (peace be upon him) was granted three supreme gifts: the five daily prayers, the seal of Surah Al-Baqarah, and forgiveness of major sins for anyone in his nation who does not associate partners with Allah (Sahih Muslim).
          </p>
        </div>

        <div class="modal-grid">
          <div class="modal-card">
            <div class="modal-card-title">The Magna Carta of Human Moral Capacity</div>
            <p>
              When <em>"Whether you reveal what is within yourselves or conceal it, Allah will bring you to account for it"</em> descended, the Companions collapsed to their knees in weeping terror, fearing unintentional thoughts.
            </p>
            <p style="margin-top:8px;">
              The revelation then descended with the ultimate universal relief:
              <br><strong style="color:var(--gold-light);">'La yukallifullahu nafsan illa wus'aha'</strong> — <em>Allah burdens no soul beyond its capacity</em>. Involuntary whispers (*waswasah*) carry zero sin. Sincere striving is recognized, and divine mercy permanently supersedes crushing despair.
            </p>
          </div>

          <div class="modal-card">
            <div class="modal-card-title">Answered Petitions: 'Qad Fa'alt' (I Have Done So)</div>
            <ul style="padding-left:16px; font-size:11.5px; color:var(--text-muted); display:flex; flex-direction:column; gap:6px;">
              <li><strong>Rabbana la tu'akhidhna in naseena aw akhta'na:</strong> "Our Lord, do not take us to task if we forget or err!" &bull; <em>Allah replies: "Qad fa'alt" (I have done so!)</em></li>
              <li><strong>Rabbana wa la tahmil 'alayna isran:</strong> "Our Lord, lay not upon us a burden like that laid upon nations before us!" &bull; <em>Allah replies: "Qad fa'alt" (I have done so!)</em></li>
              <li><strong>Rabbana wa la tuhammilna ma la taqata lana bih:</strong> "Our Lord, burden us not with that which we have no strength to bear!" &bull; <em>Allah replies: "Qad fa'alt" (I have done so!)</em></li>
              <li><strong>Anta Mawlana fansurna 'alal-qawmil-kafirin:</strong> "You are our Protector, so grant us victory over the disbelieving people!"</li>
            </ul>
          </div>
        </div>

        <div style="text-align:right;">
          <button class="btn btn-showcase-2" onclick="jumpToPart(19); closeModal('modalLastVerses');">Explore Part 19 Plates &rarr;</button>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: SUNNI SOURCE AUDIT -->
  <div class="modal-backdrop" id="modalSunniAudit">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">📜 AUTHENTIC SUNNI SOURCE DISCIPLINE & METHODOLOGY</div>
        <button class="modal-close" onclick="closeModal('modalSunniAudit')">&times;</button>
      </div>
      <div class="modal-body">
        <div>
          <h4>Huurs Studio Institutional Verification Guarantee</h4>
          <p>
            All 78 plates, 152 thematic pillars, and 608 conceptual cards across the Surah Al-Baqarah Suite are compiled under the rigorous oversight of <strong>Source Verification (AGENT-03)</strong> and <strong>Islamic QA (AGENT-15)</strong> in strict accordance with classical Sunni orthodoxy.
          </p>
        </div>

        <div class="modal-grid">
          <div class="modal-card">
            <div class="modal-card-title">1. Exegetical Pillars (Tafsir Consensus)</div>
            <p>Every thematic formulation is anchored directly into the classical canonical commentaries:</p>
            <ul style="margin-top:6px; padding-left:16px; font-size:11.5px; color:var(--text-muted); display:flex; flex-direction:column; gap:4px;">
              <li><strong>Al-Tabari (d. 310 AH):</strong> <em>Jami' al-Bayan</em> — The primordial master of narrated transmission (*Tafsir bil-Ma'thur*).</li>
              <li><strong>Ibn Kathir (d. 774 AH):</strong> <em>Tafsir al-Qur'an al-'Azim</em> — Rigorous hadith cross-examination and linguistic clarity.</li>
              <li><strong>Al-Qurtubi (d. 671 AH):</strong> <em>Al-Jami' li-Ahkam al-Qur'an</em> — Unrivaled jurisprudence (*Ahkam*) and legal precision.</li>
              <li><strong>Al-Razi (d. 606 AH):</strong> <em>Mafatih al-Ghayb</em> — Epistemological structure, thematic harmony, and philosophical defense.</li>
            </ul>
          </div>

          <div class="modal-card">
            <div class="modal-card-title">2. Institutional Non-Negotiables</div>
            <ul style="padding-left:16px; font-size:11.5px; color:var(--text-muted); display:flex; flex-direction:column; gap:6px;">
              <li><strong>Zero Personality Cult:</strong> No contemporary speaker names are utilized. The content belongs 100% to the Qur'anic text, the Sunnah, and classical scholarship.</li>
              <li><strong>Zero Audio Timestamps:</strong> Conceptual cards and mindmap plates are designed as timeless educational monuments free from ephemerality.</li>
              <li><strong>Zero Ayah Intrusion:</strong> Titles and headers focus on conceptual meanings without distracting citation clutter.</li>
              <li><strong>Visual Reverence:</strong> High-contrast navy, gold, cyan, and emerald aesthetics governed by negative space, avoiding all distorted AI religious imagery.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- SCRIPT -->
  <script>
    const DATASET = {dataset_json};

    let currentPartIndex = 0; // 0-indexed (Part 1 is index 0)
    let currentPageIndex = 1; // 1-indexed (1, 2, 3, 4)
    let isExpandedAll = false;

    // Initialize sidebar
    function initSidebar() {{
      const list = document.getElementById('partsList');
      list.innerHTML = '';
      let currentCycle = '';

      DATASET.forEach((p, idx) => {{
        if (p.cycle !== currentCycle) {{
          currentCycle = p.cycle;
          const cycleDiv = document.createElement('div');
          cycleDiv.className = 'cycle-divider';
          cycleDiv.textContent = currentCycle;
          list.appendChild(cycleDiv);
        }}

        const item = document.createElement('div');
        item.className = `part-item ${{idx === currentPartIndex ? 'active' : ''}}`;
        if (p.showcase === 'Ayat al-Kursi') item.classList.add('showcase-1');
        if (p.showcase === 'The Last Two Verses') item.classList.add('showcase-2');

        item.onclick = () => selectPart(idx);

        let showcaseBadge = '';
        if (p.showcase === 'Ayat al-Kursi') {{
          showcaseBadge = '<div class="showcase-tag tag-cyan">👑 Ayat al-Kursi Showcase</div>';
        }} else if (p.showcase === 'The Last Two Verses') {{
          showcaseBadge = '<div class="showcase-tag tag-purple">🛡️ Last Two Verses Showcase</div>';
        }}

        item.innerHTML = `
          <div class="part-item-top">
            <span class="part-num">PART ${{String(p.part).padStart(2, '0')}}</span>
            <span class="part-plates">${{p.plates}}</span>
          </div>
          <div class="part-title-text">${{p.title}}</div>
          ${{showcaseBadge}}
        `;
        list.appendChild(item);
      }});
    }}

    // Select Part
    function selectPart(idx) {{
      currentPartIndex = idx;
      const items = document.querySelectorAll('.part-item');
      items.forEach((it, i) => {{
        it.classList.toggle('active', i === idx);
      }});
      updateBanner();
      renderPages();
    }}

    function jumpToPart(partNum) {{
      const idx = DATASET.findIndex(p => p.part === partNum);
      if (idx !== -1) {{
        selectPart(idx);
        document.getElementById('mainViewport').scrollTop = 0;
      }}
    }}

    // Update banner
    function updateBanner() {{
      const p = DATASET[currentPartIndex];
      const banner = document.getElementById('partBanner');
      banner.className = 'part-banner';
      if (p.showcase === 'Ayat al-Kursi') banner.classList.add('showcase-1');
      if (p.showcase === 'The Last Two Verses') banner.classList.add('showcase-2');

      document.getElementById('bannerPartBadge').textContent = `PART ${{String(p.part).padStart(2, '0')}} OF 19`;
      document.getElementById('bannerCycleBadge').textContent = p.cycle.split(':')[0].trim();
      document.getElementById('bannerPlatesBadge').textContent = `${{p.plates}} of 78 Plates`;
      document.getElementById('bannerTitle').textContent = p.title;

      const partPdfLink = `../07_MINDMAP/BAQARAH_PART_${{String(p.part).padStart(2, '0')}}_MINDMAP.pdf`;
      document.getElementById('partPdfBtn').setAttribute('href', partPdfLink);
    }}

    // Switch Page
    function switchPage(pNum) {{
      if (isExpandedAll) {{
        toggleExpandAll(); // toggle back to single page
      }}
      currentPageIndex = pNum;
      document.querySelectorAll('.page-tab-btn').forEach((btn, idx) => {{
        btn.classList.toggle('active', idx === pNum - 1);
      }});
      renderPages();
    }}

    // Toggle expand all pages
    function toggleExpandAll() {{
      isExpandedAll = !isExpandedAll;
      const btn = document.getElementById('viewToggleBtn');
      btn.classList.toggle('active', isExpandedAll);
      btn.textContent = isExpandedAll ? '📄 Single Page View' : '👁️ Show All 4 Pages';

      const tabBtns = document.getElementById('pageTabsGroup');
      if (isExpandedAll) {{
        tabBtns.style.opacity = '0.4';
        tabBtns.style.pointerEvents = 'none';
      }} else {{
        tabBtns.style.opacity = '1';
        tabBtns.style.pointerEvents = 'auto';
      }}
      renderPages();
    }}

    // Render Page Display
    function renderPages() {{
      const display = document.getElementById('pageDisplay');
      display.innerHTML = '';
      const p = DATASET[currentPartIndex];

      const pagesToRender = isExpandedAll 
        ? p.pages 
        : [p.pages[currentPageIndex - 1]];

      pagesToRender.forEach(pg => {{
        const pageCard = document.createElement('div');
        pageCard.className = 'page-card';
        pageCard.id = `rendered-page-${{pg.page}}`;

        let pillarsHtml = '';
        pg.pillars.forEach(pil => {{
          let cardsHtml = '';
          pil.cards.forEach((c, cIdx) => {{
            let bulletsHtml = c.bullets.map(b => `<li>${{b}}</li>`).join('');
            cardsHtml += `
              <div class="card-item" id="card-p${{p.part}}-pg${{pg.page}}-pil${{pil.name.replace(/[^0-9]/g, '')}}-c${{cIdx+1}}">
                <div class="card-title">
                  <span class="num">${{c.title.split('.')[0]}}.</span>
                  <span>${{c.title.replace(/^\\d+\\.\\s*/, '')}}</span>
                </div>
                <ul class="card-bullets">${{bulletsHtml}}</ul>
              </div>
            `;
          }});

          pillarsHtml += `
            <div class="pillar-box">
              <div class="pillar-header ${{pil.color}}">
                <div class="pillar-title">${{pil.name}}</div>
                <div class="pillar-sub">${{pil.sub}}</div>
              </div>
              <div class="cards-stack">
                ${{cardsHtml}}
              </div>
            </div>
          `;
        }});

        pageCard.innerHTML = `
          <div class="page-card-header">
            <div class="page-heading">
              <h3>${{pg.title}}</h3>
              <p>${{pg.desc}}</p>
            </div>
            <span class="page-sec-badge">${{pg.sec || `PAGE ${{pg.page}}`}}</span>
          </div>
          <div class="pillars-container">
            ${{pillarsHtml}}
          </div>
        `;
        display.appendChild(pageCard);
      }});
    }}

    // Search functionality
    const searchInput = document.getElementById('globalSearch');
    const searchResults = document.getElementById('searchResults');
    const searchClear = document.getElementById('searchClear');

    searchInput.addEventListener('input', (e) => {{
      const query = e.target.value.trim().toLowerCase();
      if (query.length < 2) {{
        searchResults.classList.remove('open');
        searchClear.style.display = 'none';
        return;
      }}
      searchClear.style.display = 'block';
      performSearch(query);
    }});

    searchClear.addEventListener('click', () => {{
      searchInput.value = '';
      searchResults.classList.remove('open');
      searchClear.style.display = 'none';
      searchInput.focus();
    }});

    function performSearch(query) {{
      const matches = [];
      DATASET.forEach((p, pIdx) => {{
        p.pages.forEach((pg) => {{
          pg.pillars.forEach((pil) => {{
            pil.cards.forEach((c, cIdx) => {{
              const inTitle = c.title.toLowerCase().includes(query);
              const matchedBullets = c.bullets.filter(b => b.toLowerCase().includes(query));
              if (inTitle || matchedBullets.length > 0) {{
                matches.push({{
                  partIdx: pIdx,
                  partNum: p.part,
                  partTitle: p.title,
                  pageNum: pg.page,
                  pillarName: pil.name,
                  cardTitle: c.title,
                  snippet: matchedBullets[0] || c.title,
                  cardId: `card-p${{p.part}}-pg${{pg.page}}-pil${{pil.name.replace(/[^0-9]/g, '')}}-c${{cIdx+1}}`
                }});
              }}
            }});
          }});
        }});
      }});

      renderSearchResults(matches, query);
    }}

    function renderSearchResults(matches, query) {{
      if (matches.length === 0) {{
        searchResults.innerHTML = `
          <div class="search-meta-bar">
            <span>NO MATCHES FOUND</span>
            <span>0 RESULTS</span>
          </div>
          <div style="padding:16px; font-size:12px; color:var(--text-muted); text-align:center;">
            No cards found matching "${{query}}". Try searching for theological concepts like "taqwa", "kursi", "covenant", "riba", "adam", or "ibrahim".
          </div>
        `;
        searchResults.classList.add('open');
        return;
      }}

      let html = `
        <div class="search-meta-bar">
          <span>SEARCH RESULTS ACROSS 608 CARDS</span>
          <span>${{matches.length}} MATCHES</span>
        </div>
      `;

      const regex = new RegExp(`(${{query}})`, 'gi');

      matches.slice(0, 25).forEach(m => {{
        const hlTitle = m.cardTitle.replace(regex, '<span class="highlight-term">$1</span>');
        const hlSnippet = m.snippet.replace(regex, '<span class="highlight-term">$1</span>');
        html += `
          <div class="search-item" onclick="jumpToSearchResult(${{m.partIdx}}, ${{m.pageNum}}, '${{m.cardId}}')">
            <div class="search-item-location">Part ${{String(m.partNum).padStart(2, '0')}} &bull; Page ${{m.pageNum}} &bull; ${{m.pillarName}}</div>
            <div class="search-item-header">${{hlTitle}}</div>
            <div class="search-item-snippet">${{hlSnippet}}</div>
          </div>
        `;
      }});

      if (matches.length > 25) {{
        html += `<div style="padding:8px 14px; font-size:10.5px; color:var(--gold); text-align:center;">+ ${{matches.length - 25}} more matches. Refine your query for tighter focus.</div>`;
      }}

      searchResults.innerHTML = html;
      searchResults.classList.add('open');
    }}

    function jumpToSearchResult(partIdx, pageNum, cardId) {{
      searchResults.classList.remove('open');
      selectPart(partIdx);
      if (!isExpandedAll) {{
        switchPage(pageNum);
      }}
      setTimeout(() => {{
        const cardElem = document.getElementById(cardId);
        if (cardElem) {{
          cardElem.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          cardElem.classList.add('highlight-pulse');
          setTimeout(() => cardElem.classList.remove('highlight-pulse'), 4500);
        }}
      }}, 200);
    }}

    // Modals
    function openModal(id) {{
      document.getElementById(id).classList.add('open');
    }}

    function closeModal(id) {{
      document.getElementById(id).classList.remove('open');
    }}

    window.onclick = function(event) {{
      if (event.target.classList.contains('modal-backdrop')) {{
        event.target.classList.remove('open');
      }}
      if (!event.target.closest('.search-wrapper')) {{
        searchResults.classList.remove('open');
      }}
    }};

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('open'));
        searchResults.classList.remove('open');
      }}
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {{
        e.preventDefault();
        searchInput.focus();
      }}
    }});

    // Initialize
    initSidebar();
    selectPart(0);
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"SURAH_AL_BAQARAH_INTERACTIVE_SUITE.html successfully generated at {OUTPUT_HTML} (Size: {len(html_template)} bytes)!")
