# Pricing Sign-Off Request: Meridian AI Platform Reprice

## Scenario

Meridian AI's product team has proposed a new 3-tier pricing structure to replace the current flat-rate model. The new tiers are Starter ($299/mo), Growth ($899/mo), and Enterprise ($2,499/mo). The CFO needs to evaluate whether the proposed pricing supports the company's margin targets, models the revenue impact across scenarios, and issues a formal sign-off decision before the pricing goes live in 30 days.

## Input

```json
{
  "company": "Meridian AI",
  "product": "Meridian AI Platform",
  "proposed_tiers": [
    {
      "name": "Starter",
      "price_monthly": 299,
      "cogs_per_unit": 95,
      "expected_mix_pct": 45
    },
    {
      "name": "Growth",
      "price_monthly": 899,
      "cogs_per_unit": 210,
      "expected_mix_pct": 40
    },
    {
      "name": "Enterprise",
      "price_monthly": 2499,
      "cogs_per_unit": 480,
      "expected_mix_pct": 15
    }
  ],
  "current_blended_gross_margin_pct": 68,
  "target_gross_margin_pct": 72,
  "max_discount_pct": 20,
  "current_arr": 2800000,
  "projected_new_arr_year1": 1400000,
  "churn_risk_pct": 8,
  "competitive_price_floor": 249
}
```
