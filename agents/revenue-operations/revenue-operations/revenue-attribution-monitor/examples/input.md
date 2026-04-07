# Revenue Attribution Monitor — Example Input

## Scenario

The RevOps team is running a Q1 attribution audit ahead of the quarterly business review. Marketing and sales disagree on lead source credit — paid search is claiming 40% of pipeline but operations suspects UTM tags are broken on several campaigns. The team uses a linear multi-touch attribution model.

## Input JSON

```json
{
  "attribution_model": "linear",
  "channels": [
    {
      "name": "Paid Search (Google Ads)",
      "quality_scores": {
        "utm_coverage": 5,
        "crm_source_accuracy": 6,
        "pixel_integrity": 4,
        "dedup_accuracy": 7
      },
      "attribution_coverage_pct": 68,
      "attributed_revenue": 420000,
      "issues": ["UTM tags missing on 3 active campaigns", "Conversion pixel firing on thank-you page only, missing form submit event"]
    },
    {
      "name": "Content / SEO",
      "quality_scores": {
        "utm_coverage": 9,
        "crm_source_accuracy": 8,
        "pixel_integrity": 9,
        "dedup_accuracy": 8
      },
      "attribution_coverage_pct": 92,
      "attributed_revenue": 310000,
      "issues": []
    },
    {
      "name": "Outbound SDR",
      "quality_scores": {
        "utm_coverage": 7,
        "crm_source_accuracy": 9,
        "pixel_integrity": 6,
        "dedup_accuracy": 8
      },
      "attribution_coverage_pct": 88,
      "attributed_revenue": 280000,
      "issues": ["LinkedIn touchpoints not captured in CRM automatically — manual entry required"]
    },
    {
      "name": "Events / Conferences",
      "quality_scores": {
        "utm_coverage": 4,
        "crm_source_accuracy": 5,
        "pixel_integrity": 3,
        "dedup_accuracy": 6
      },
      "attribution_coverage_pct": 55,
      "attributed_revenue": 190000,
      "issues": ["Event badge scans not synced to CRM", "No post-event UTM tracking on follow-up emails", "Pixel not deployed on event landing pages"]
    }
  ]
}
```
