---
artifact:
  artifact_id: QURAN-COMEBACK-CHECKOUT-FUNNELS-001
  artifact_type: checkout_funnel_specification
  artifact_version: 1.0.0
  project_id: HUURS-QURAN
  campaign_id: COME-BACK-TO-QURAN
  title: "Come Back to the Qur'an — Technical Checkout Architecture & Funnel Logic (Lemon Squeezy / Gumroad)"
  description: "Technical configuration rules, webhook routing, checkout bumps, upsell flows, discount matrices, and tax/VAT compliance for commercial sales."
  topic: "E-Commerce Checkout Architecture & Conversion Optimization"
  language: en-US
  audience: "Store administrators, operations managers, growth engineers"

provenance:
  parent_artifacts:
    - "file:///mnt/AI/ag/Campaign/Brand_Campaign.md"
    - "file:///mnt/AI/ag/Campaign/15_MARKETING/QURAN-COMEBACK-FUNNEL-001.md"
    - "file:///mnt/AI/ag/Campaign/12_PRODUCTS/store/PRODUCT_LISTINGS_GUMROAD.md"

lifecycle:
  status: approved
  created_by: AGENT-14
  created_at: 2026-09-07T21:45:00Z
  updated_at: 2026-09-07T21:45:00Z

verification:
  verification_status: verified
  verified_by: AGENT-14
  qa_status: passed
  human_review_status: approved

storage:
  repository: huurs-studio
  path: 12_PRODUCTS/store/
  filename: CHECKOUT_FUNNELS_LEMONSQUEEZY.md
---

# Checkout Architecture & Funnel Logic (`QURAN-COMEBACK-CHECKOUT-FUNNELS-001`)

**E-Commerce Engine:** Lemon Squeezy (Merchant of Record) / Gumroad  
**Currency:** USD (with localized multi-currency display: GBP, EUR, CAD, AUD, SAR, AED, MYR, IDR)  
**Tax & Compliance:** Automated global VAT / GST handling via Merchant of Record.  

---

## 1. Funnel Flow & Upsell Architecture

```mermaid
graph TD
    A[Visitor Arrives via YouTube / Social / Search] --> B{Entry Point}
    
    B -->|Free Path| C[Tier 0: Free 7-Day Guide Opt-in]
    B -->|Paid Path| D[Tier 2: Master 114-Surah Book ($27)]
    
    C --> E[Checkout Thank You Page]
    E -->|One-Time Offer| F["Order Bump: 30-Day Journal ($9 vs $14)"]
    F -->|Accepted| G[Customer Enters 30-Day Nurture Email Sequence]
    F -->|Declined| H[Customer Enters 7-Day Lead Magnet Sequence]
    
    D --> I[Checkout Page]
    I -->|Checkout Bump| J["Add 30-Day Journal (+ $9)"]
    I -->|One-Click Post-Purchase Upsell| K["Upgrade to Complete Ecosystem Bundle (+ $22)"]
    
    K -->|Accepted| L[Bundle Delivery: All 5 Products]
    K -->|Declined| M[Standard Book Delivery: EPUB + PDF + MD]
```

---

## 2. Product Variant & Pricing Matrix

| SKU Code | Product Title | Retail Price | Launch Price | Min Pay-What-You-Want |
|---|---|---|---|---|
| `HUURS-GUIDE-001` | 7-Day Guided Contemplation Journal | **$0.00** | **$0.00** | $0.00 |
| `HUURS-JRNL-030` | 30-Day Guided Contemplation Journal Workbook | **$14.00** | **$9.00** | N/A (Fixed) |
| `HUURS-BOOK-114` | Master Digital Book (114 Surahs EPUB + PDF) | **$27.00** | **$19.00** | N/A (Fixed) |
| `HUURS-BNDL-ALL` | Complete Come Back to the Qur'an Ecosystem | **$118.00** | **$49.00** | N/A (Fixed) |

---

## 3. Webhook Integration Rules (ConvertKit / Substack / ActiveCampaign)

When an order is created on Lemon Squeezy / Gumroad, the platform dispatches a webhook `order_created`:

```json
{
  "event_name": "order_created",
  "data": {
    "attributes": {
      "user_email": "customer@example.com",
      "user_name": "Abdullah",
      "first_order_item": {
        "product_id": "HUURS-BNDL-ALL",
        "product_name": "The Complete Come Back to the Qur'an Ecosystem Bundle"
      },
      "total_formatted": "$49.00"
    }
  }
}
```

### Automation Routing Table:
* **If `product_id` == `HUURS-GUIDE-001`:**
  * Tag subscriber: `lead_magnet_7day`
  * Trigger: `15_MARKETING/QURAN-COMEBACK-EMAIL-SERIES-001.md` (Sequence 1: Emails 1 to 7).
* **If `product_id` == `HUURS-JRNL-030`:**
  * Tag subscriber: `customer_30day_journal`
  * Remove tag: `lead_magnet_7day`
  * Trigger: `CUSTOMER_ONBOARDING_WORKFLOW.md` (Journal Onboarding) + 30-Day Milestone Sequence.
* **If `product_id` == `HUURS-BOOK-114`:**
  * Tag subscriber: `customer_114_surahs_book`
  * Trigger: `CUSTOMER_ONBOARDING_WORKFLOW.md` (Ebook Delivery & Kindle Setup).
* **If `product_id` == `HUURS-BNDL-ALL`:**
  * Tag subscriber: `customer_master_bundle_vip`
  * Trigger: VIP Master Bundle Welcome Sequence + Instant Download Hub Link.

---
