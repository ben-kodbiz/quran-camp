#!/usr/bin/env python3
"""
HUURS STUDIO - Email Campaign Exporter & ESP Formatter
======================================================
Parses QURAN-COMEBACK-EMAIL-SERIES-001.md into individual,
production-ready HTML & Markdown templates formatted for:
- Substack
- ConvertKit (Kit)
- Mailchimp / Brevo
- Raw CSV Import

Includes:
- Subject lines, preview pre-headers, trigger offsets
- Responsive email styling with dark-mode compatibility
- Huurs brand design tokens (charcoal #0B0F17, gold #C5A059, serif text)
"""

import os
import re
import json
import csv

SOURCE_FILE = "/mnt/AI/ag/Campaign/15_MARKETING/QURAN-COMEBACK-EMAIL-SERIES-001.md"
OUTPUT_DIR = "/mnt/AI/ag/Campaign/15_MARKETING/email_templates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HTML_WRAPPER = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{subject}</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Georgia, serif;
      background-color: #F8F9FA;
      color: #1E293B;
      margin: 0;
      padding: 0;
      line-height: 1.75;
    }}
    .preheader {{
      display: none !important;
      visibility: hidden;
      mso-hide: all;
      font-size: 1px;
      line-height: 1px;
      max-height: 0;
      max-width: 0;
      opacity: 0;
      overflow: hidden;
    }}
    .email-container {{
      max-width: 600px;
      margin: 30px auto;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      overflow: hidden;
    }}
    .email-header {{
      padding: 24px 32px;
      border-bottom: 1px solid #F1F5F9;
      background-color: #0B0F17;
      text-align: center;
    }}
    .email-brand {{
      font-size: 14px;
      letter-spacing: 0.15em;
      color: #C5A059;
      text-transform: uppercase;
      font-weight: 600;
    }}
    .email-body {{
      padding: 36px 32px;
      font-size: 16px;
      color: #2D3748;
    }}
    .email-body p {{
      margin-bottom: 18px;
    }}
    .email-footer {{
      padding: 24px 32px;
      background: #F8FAFC;
      border-top: 1px solid #E2E8F0;
      font-size: 13px;
      color: #64748B;
      text-align: center;
    }}
    .cta-btn {{
      display: inline-block;
      background-color: #C5A059;
      color: #0B0F17 !important;
      font-weight: 600;
      padding: 12px 24px;
      border-radius: 6px;
      text-decoration: none;
      margin: 16px 0;
    }}
  </style>
</head>
<body>
  <span class="preheader">{preview_text}</span>
  <div class="email-container">
    <div class="email-header">
      <div class="email-brand">Huurs Studio  •  Read. Reflect. Return.</div>
    </div>
    <div class="email-body">
      {body_html}
    </div>
    <div class="email-footer">
      <p>You received this email because you began the "Come Back to the Qur'an" 7-Day Journey.</p>
      <p>© 2026 Huurs Studio  •  A peaceful, non-intrusive contemplation project.</p>
    </div>
  </div>
</body>
</html>
"""

def parse_emails():
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for email definitions
    email_blocks = re.findall(
        r"### Email\s+(\d+)\s*\(([^)]+)\):\s*([^\n]+)\n\*\s*\*\*Trigger:\*\*\s*([^\n]+)\n\*\s*\*\*Subject:\*\*\s*([^\n]+)\n\*\s*\*\*Preview Text:\*\*\s*([^\n]+)\n\*\s*\*\*Body:\*\*\s*\n```text\s*([\s\S]*?)\s*```",
        content
    )

    emails_data = []

    print("===========================================================================")
    print("        HUURS STUDIO - EXPORTING EMAIL AUTOMATION SUITE TEMPLATES          ")
    print("===========================================================================\n")

    for idx, timing, title, trigger, subject, preview, body in email_blocks:
        num = int(idx)
        slug = f"EMAIL_{num:02d}_{re.sub(r'[^a-zA-Z0-9_]+', '_', timing.lower())}"
        
        # Convert plain paragraphs to html paragraphs
        paras = [p.strip() for p in body.strip().split("\n\n") if p.strip()]
        html_paras = []
        for p in paras:
            if p.startswith("-->"):
                link_text = p.replace("-->", "").strip(" []")
                html_paras.append(f'<p style="text-align:center;"><a href="#" class="cta-btn">{link_text}</a></p>')
            elif p.startswith('"') and p.endswith('"'):
                html_paras.append(f'<blockquote style="border-left: 3px solid #C5A059; padding-left: 16px; margin: 16px 0; color: #4A5568; font-style: italic;">{p}</blockquote>')
            else:
                html_paras.append(f'<p>{p.replace("\n", "<br>")}</p>')
        
        body_html = "\n      ".join(html_paras)
        full_html = HTML_WRAPPER.format(
            subject=subject.strip(),
            preview_text=preview.strip(),
            body_html=body_html
        )

        # Write HTML template
        html_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        # Write Markdown template
        md_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"""# {title.strip()}

* **Sequence Number:** {num}
* **Timing / Day:** {timing.strip()}
* **Trigger:** {trigger.strip()}
* **Subject:** {subject.strip()}
* **Preview Text:** {preview.strip()}

---

## Email Body

{body.strip()}
""")

        emails_data.append({
            "email_number": num,
            "slug": slug,
            "timing": timing.strip(),
            "trigger": trigger.strip(),
            "subject": subject.strip(),
            "preview_text": preview.strip(),
            "html_file": f"{slug}.html",
            "md_file": f"{slug}.md"
        })

        print(f"📧 Exported: {slug} | Subject: \"{subject.strip()}\"")

    # Write Manifest JSON
    manifest_path = os.path.join(OUTPUT_DIR, "email_series_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({"total_emails": len(emails_data), "emails": emails_data}, f, indent=2)

    # Write CSV for bulk import into ConvertKit / Mailchimp
    csv_path = os.path.join(OUTPUT_DIR, "email_series_import.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["email_number", "timing", "trigger", "subject", "preview_text", "html_file", "md_file"])
        writer.writeheader()
        for e in emails_data:
            writer.writerow({
                "email_number": e["email_number"],
                "timing": e["timing"],
                "trigger": e["trigger"],
                "subject": e["subject"],
                "preview_text": e["preview_text"],
                "html_file": e["html_file"],
                "md_file": e["md_file"]
            })

    print(f"\n✅ All {len(emails_data)} email templates exported to: {OUTPUT_DIR}")
    print(f"✅ Master JSON manifest: {manifest_path}")
    print(f"✅ ESP Bulk CSV import: {csv_path}")

if __name__ == "__main__":
    parse_emails()
