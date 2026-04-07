# Marketing Attribution Modeller — Example Input

## Scenario

Meridian AI closed 5 deals in Q1 2026 and wants to understand which channels drove revenue. The Marketing Ops Manager is building a W-Shaped attribution model (standard for B2B) to inform the Q2 budget allocation debate between paid search, content, and outbound email.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "model_type": "w_shaped",
  "journeys": [
    {
      "deal_id": "OPP-201",
      "deal_value_usd": 48000,
      "touchpoints": ["organic_search", "content", "webinar", "email", "demo_request"]
    },
    {
      "deal_id": "OPP-202",
      "deal_value_usd": 36000,
      "touchpoints": ["paid_search", "content", "email", "demo_request"]
    },
    {
      "deal_id": "OPP-203",
      "deal_value_usd": 24000,
      "touchpoints": ["referral", "email", "demo_request"]
    },
    {
      "deal_id": "OPP-204",
      "deal_value_usd": 60000,
      "touchpoints": ["paid_social", "organic_search", "content", "webinar", "email", "demo_request"]
    },
    {
      "deal_id": "OPP-205",
      "deal_value_usd": 18000,
      "touchpoints": ["organic_search", "email", "demo_request"]
    }
  ]
}
```
