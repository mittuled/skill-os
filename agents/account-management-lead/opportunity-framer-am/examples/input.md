# Scenario: SaaS Account Approaching Plan Limits Before QBR

Acme Corp is a mid-market SaaS customer on the Growth plan with 180 of 200 licensed seats in use. Their usage data shows core feature adoption at 85% and they recently hired 40 new engineers. A QBR is scheduled in three weeks. The AM lead wants to frame an upsell opportunity for the account manager to present.

## Input Parameters

```json
{
  "account_name": "Acme Corp",
  "expansion_type": "seat_upsell",
  "recommended_timing": "Upcoming QBR in 3 weeks",
  "criteria_ratings": {
    "usage_signal_strength": "approaching_limit",
    "strategic_fit": "direct_business_need",
    "revenue_potential": "medium",
    "account_health": "healthy",
    "close_likelihood": "champion_with_budget"
  }
}
```
