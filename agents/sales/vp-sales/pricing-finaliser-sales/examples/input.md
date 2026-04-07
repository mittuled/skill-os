# Scenario: Validating New Tier Pricing Before Q2 Launch

A B2B SaaS company is introducing a new Professional tier at $18,000/year (list price). The VP Sales must validate sellability before Product confirms the launch pricing and Finance models Q2 revenue. Field data from the last two quarters is available.

## Input Parameters

```json
{
  "proposed_list_price": 18000,
  "avg_selling_price": 13500,
  "avg_discount_pct": 25,
  "objection_frequency_pct": 40,
  "competitor_street_prices": {
    "CompetitorA": 15000,
    "CompetitorB": 12000,
    "CompetitorC": 20000
  },
  "pipeline_deals_at_risk": 8,
  "total_pipeline_deals": 22,
  "tier_name": "Professional",
  "review_period_quarters": 2,
  "notes": "Field reps report buyers consistently push back on price in mid-market deals; AEs are discounting at 25%+ to close"
}
```
