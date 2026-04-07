# Example Input: business-model-sketcher

## Context

**Product**: TaskFlow — automated invoice reconciliation for mid-market ops teams.

**Revenue Model**: Monthly SaaS subscription.

**Parameters (JSON)**:
```json
{
  "product_name": "TaskFlow",
  "arpu": 299,
  "cac": 1500,
  "monthly_churn": 0.05,
  "cogs_per_user": 45,
  "fixed_costs_monthly": 50000
}
```

**Source data**: ARPU based on Van Westendorp survey (n=30). CAC estimated from comparable B2B SaaS benchmarks. Churn estimated at 5% monthly for early-stage product. COGS includes hosting ($20/user), API calls ($15/user), and support allocation ($10/user). Fixed costs include 3 engineers + 1 PM + tooling.
