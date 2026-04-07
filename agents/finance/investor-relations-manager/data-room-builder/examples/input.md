# Data Room Builder — Example Input

## Scenario

Meridian AI is entering Series A diligence with Sequoia leading. The data room was built at seed stage but needs to be updated and expanded for Series A depth. The IR Manager needs to audit what's present, identify gaps, and flag stale documents before granting Sequoia access.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "round_name": "Series A",
  "documents": [
    {"name": "Certificate of Incorporation", "section": "corporate", "days_since_updated": 30},
    {"name": "Bylaws", "section": "corporate", "days_since_updated": 30},
    {"name": "Board minutes and consents", "section": "corporate", "days_since_updated": 14},
    {"name": "Cap table fully diluted", "section": "corporate", "days_since_updated": 7},
    {"name": "Stock option plan", "section": "corporate", "days_since_updated": 60},
    {"name": "409A valuation", "section": "corporate", "days_since_updated": 210},
    {"name": "Management accounts last 12 months", "section": "financials", "days_since_updated": 7},
    {"name": "Financial model 3-year projection", "section": "financials", "days_since_updated": 14},
    {"name": "ARR MRR bridge", "section": "financials", "days_since_updated": 7},
    {"name": "Burn rate runway analysis", "section": "financials", "days_since_updated": 7},
    {"name": "Top 10 customer contracts", "section": "commercial", "days_since_updated": 30},
    {"name": "Sales pipeline CRM export", "section": "commercial", "days_since_updated": 3},
    {"name": "Churn NRR analysis", "section": "commercial", "days_since_updated": 7},
    {"name": "Product roadmap", "section": "product_tech", "days_since_updated": 21},
    {"name": "Architecture overview", "section": "product_tech", "days_since_updated": 90},
    {"name": "Org chart", "section": "team_hr", "days_since_updated": 14},
    {"name": "Key employee agreements", "section": "team_hr", "days_since_updated": 30},
    {"name": "IP ownership confirmation", "section": "ip", "days_since_updated": 30},
    {"name": "Privacy policy", "section": "regulatory", "days_since_updated": 180}
  ]
}
```
