# Framework: business-model-sketcher

Guides the construction of a first-pass business model covering value exchange, unit economics, cost structure, and break-even analysis.

## Framework: Business Model Canvas (Lean Variant)

### Value Exchange Mapping

1. **Value delivered**: What outcome does the user get?
2. **Value captured**: What does the user give in return (money, data, attention, network)?
3. **Revenue streams**: Primary (subscription, usage, take-rate) and secondary (upsell, add-ons, data monetisation)

### Unit Economics Model

| Metric | Formula | Inputs Needed |
|--------|---------|--------------|
| CAC | Total acquisition spend / New customers | Marketing spend, sales cost, time period |
| LTV | ARPU × Gross margin % × (1 / Monthly churn rate) | ARPU, COGS, churn |
| Gross Margin | (Revenue - COGS) / Revenue | Revenue per unit, variable costs |
| Payback Period | CAC / (ARPU × Gross margin %) | CAC, ARPU, gross margin |
| LTV:CAC Ratio | LTV / CAC | LTV, CAC — target >3:1 |

### Cost Structure Framework

| Category | Examples | Scaling Behaviour |
|----------|----------|------------------|
| Fixed | Engineering headcount, office, tooling licences | Step function — grows at hiring thresholds |
| Variable | Hosting, API calls, support per user, payment processing | Linear or sub-linear with usage |
| Semi-variable | Customer success, onboarding | Grows with customer count at lower rate |

### Break-Even Analysis

1. Contribution margin per unit = ARPU - Variable cost per unit
2. Break-even users = Fixed costs / Contribution margin per unit
3. Sensitivity: vary the top 2 assumptions (ARPU, churn) by ±20% and recalculate

### Three-Scenario Planning

| Scenario | Adoption Rate | ARPU | Churn | Notes |
|----------|--------------|------|-------|-------|
| Pessimistic | 50% of base | -20% | +50% | What breaks the model? |
| Base | As modelled | As modelled | As modelled | Expected case |
| Optimistic | 150% of base | +20% | -30% | What accelerates viability? |

## Quality Checklist

- [ ] All assumptions stated explicitly with source or "assumption" tag
- [ ] Unit economics use comparable company data where direct data unavailable
- [ ] Cost structure modelled at three scale points (launch, 1K users, 10K users)
- [ ] Break-even analysis includes sensitivity on top 2 variables
- [ ] Top 3 viability risks identified with mitigation paths
