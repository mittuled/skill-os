# Unit Economics Gate: Meridian AI — SMB Segment

## Scenario

Meridian AI is considering launching a self-serve SMB tier at $299/month. Before committing GTM resources, the CFO needs to run the unit economics gate to determine whether the SMB segment is viable given higher expected churn and lower contract values versus the existing enterprise segment.

The growth team has provided their CAC estimates and churn projections. The CFO will stress-test against churn increases, CAC inflation, and gross margin compression to identify which variable most threatens viability.

## Input

```json
{
  "company": "Meridian AI",
  "segment": "SMB Self-Serve",
  "gross_margin_pct": 71,
  "arpu_monthly": 299,
  "avg_contract_months": 24,
  "cac": 3200,
  "churn_rate_monthly_pct": 2.5,
  "runway_months": 18,
  "target_payback_months": 14,
  "downside_scenarios": {
    "churn_increase_pp": 2,
    "cac_inflation_pct": 25,
    "margin_compression_pp": 5
  }
}
```
