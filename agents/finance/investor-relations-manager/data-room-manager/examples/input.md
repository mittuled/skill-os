# Data Room Manager — Example Input

## Scenario

Meridian AI is in active Series A diligence with three investors at different stages. One investor has signed the NDA and has full access; another has limited access pending NDA; a third has full access and has been most active. The IR Manager needs to audit document freshness and investor access levels before a partner call next week.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "action": "audit",
  "investors": [
    {
      "name": "Jane Wu",
      "firm": "Sequoia Capital",
      "nda_signed": true,
      "access_level": "full",
      "last_viewed": "2026-03-30",
      "documents_viewed": 28
    },
    {
      "name": "David Park",
      "firm": "Andreessen Horowitz",
      "nda_signed": true,
      "access_level": "limited",
      "last_viewed": "2026-03-25",
      "documents_viewed": 9
    },
    {
      "name": "Rachel Kim",
      "firm": "Founders Fund",
      "nda_signed": false,
      "access_level": "nda_only",
      "last_viewed": "2026-03-28",
      "documents_viewed": 2
    }
  ],
  "documents": [
    {"name": "Cap table fully diluted", "type": "critical", "days_since_updated": 7},
    {"name": "Board minutes Q1 2026", "type": "critical", "days_since_updated": 14},
    {"name": "409A valuation", "type": "critical", "days_since_updated": 210},
    {"name": "Management accounts March 2026", "type": "financials", "days_since_updated": 7},
    {"name": "Financial model", "type": "financials", "days_since_updated": 14},
    {"name": "Management accounts January 2026", "type": "financials", "days_since_updated": 75},
    {"name": "Top 10 customer contracts", "type": "commercial", "days_since_updated": 45},
    {"name": "Sales pipeline", "type": "commercial", "days_since_updated": 3},
    {"name": "Standard MSA template", "type": "commercial", "days_since_updated": 180}
  ]
}
```
