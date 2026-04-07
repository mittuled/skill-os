# Scenario: Building Pricing Strategy for a New Analytics Product

A product analytics SaaS company is launching a new "Insights" product tier. No prior pricing exists for this tier. The VP Sales is tasked with building the pricing strategy before Product finalises packaging. Field data from 90 discovery calls and 35 closed-lost records is available.

## Input Parameters

```json
{
  "product_name": "Insights Analytics Platform",
  "pricing_model": "per-seat",
  "recommended_value_metric": "seats",
  "closed_lost_pricing_rate_pct": 30,
  "avg_discount_depth_pct": 18,
  "active_pipeline_deals": 40,
  "segments": [
    {
      "name": "SMB (< 200 employees)",
      "wtp_low": 8000,
      "wtp_high": 20000,
      "competitive_prices": [7500, 12000, 9000]
    },
    {
      "name": "Mid-Market (200–1000 employees)",
      "wtp_low": 25000,
      "wtp_high": 60000,
      "competitive_prices": [28000, 35000, 22000]
    },
    {
      "name": "Enterprise (1000+ employees)",
      "wtp_low": 80000,
      "wtp_high": 200000,
      "competitive_prices": [90000, 120000, 75000]
    }
  ]
}
```
