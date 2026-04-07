# Example Output: business-model-sketcher

## Business Model Sketch: TaskFlow

### Unit Economics

| Metric | Value | Source |
|--------|-------|--------|
| ARPU | $299/month | Van Westendorp survey (n=30) |
| CAC | $1,500 | B2B SaaS benchmark |
| COGS/user | $45/month | Hosting + API + support allocation |
| Gross Margin | 85.0% | Calculated |
| LTV | $5,084.00 | Calculated (ARPU × GM / churn) |
| Payback | 5.9 months | Calculated |
| LTV:CAC | 3.39 | Calculated — viable threshold |

### Break-Even

- Contribution margin per user: $254/month
- Break-even: 197 customers at $50K/month fixed costs

### Sensitivity Analysis

| Scenario | ARPU | Churn | LTV | Break-Even Users |
|----------|------|-------|-----|-----------------|
| Pessimistic | $239.20 | 7.50% | $2,466.93 | 258 |
| Base | $299.00 | 5.00% | $5,084.00 | 197 |
| Optimistic | $358.80 | 3.50% | $8,089.83 | 159 |

### Viability Signal: VIABLE

```json
{
  "skill": "business-model-sketcher",
  "product": "TaskFlow",
  "generated_date": "2026-03-29",
  "unit_economics": {
    "arpu": 299,
    "cac": 1500,
    "cogs_per_user": 45,
    "gross_margin_pct": 85.0,
    "ltv": 5084.0,
    "payback_months": 5.9,
    "ltv_cac_ratio": 3.39,
    "contribution_margin": 254.0,
    "break_even_users": 197,
    "fixed_costs_monthly": 50000
  },
  "viability_signal": "viable"
}
```

### Top 3 Viability Risks

1. **P1**: Monthly churn at 5% is aggressive for early-stage — if actual churn is 7.5%, LTV drops 51% and LTV:CAC falls to 1.64 (at-risk territory)
2. **P2**: ARPU of $299 depends on unvalidated WTP — if actual WTP is $239 (-20%), break-even extends to 258 customers (+31%)
3. **P3**: CAC benchmark may not hold for a new category entrant without brand awareness — early CAC could be 2x estimate
