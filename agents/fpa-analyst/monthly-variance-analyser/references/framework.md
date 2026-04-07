# Framework: monthly-variance-analyser

Defines the analytical framework for decomposing monthly P&L variances into actionable root causes and forecast implications.

## Variance Taxonomy

### Variance Types

| Type | Definition | Forecast Impact | Example |
|------|------------|-----------------|---------|
| Volume | More or fewer transactions than planned | Permanent — adjust forecast | 20 fewer new logos than budgeted |
| Price/Rate | Unit price or rate differs from plan | Permanent — adjust forecast | ACV 8% below plan due to increased discounting |
| Timing | Revenue recognized or cost incurred in a different period | Temporary — no forecast adjustment | Annual subscription recognized 30 days late due to delayed signature |
| One-time | Non-recurring event not in the plan | Temporary — exclude from trend | Legal settlement, severance payment, one-time marketing event |
| Mix | Composition of business differs from assumptions | Permanent if structural | More SMB deals than enterprise forecast, dragging ARPU below plan |

### Variance Root Cause Framework

For each material variance, determine the cause before writing commentary:

1. **What happened** — The observable fact (e.g., "Sales headcount was 3 below plan")
2. **Why it happened** — The business reason (e.g., "3 planned hires slipped to Q2 due to extended offer negotiations")
3. **Is it permanent or timing?** — Classification determines forecast impact
4. **So what** — Business implication (e.g., "Q1 new ARR will be $180K below plan; we expect to recover in Q2 if hires close by end of January")

## Materiality Thresholds

Apply these thresholds to filter variances worth analyzing:

| Company Stage | Absolute Threshold | Percentage Threshold | Both Required? |
|--------------|-------------------|---------------------|----------------|
| Pre-revenue / Seed | $5K | 5% | Either |
| Series A ($1M–$5M ARR) | $10K | 5% | Both |
| Series B ($5M–$20M ARR) | $25K | 5% | Both |
| Series C+ ($20M+ ARR) | $100K | 3% | Both |

Adjust thresholds at the start of each fiscal year and document the rationale.

## Variance Commentary Structure

### Standard Commentary Template

**[Line item]**: Actuals were $[X] vs. budget of $[Y], a [favorable / unfavorable] variance of $[Z] ([N]%). This was driven by [root cause — volume / price / timing / one-time / mix]. This variance is [permanent — we are adjusting the full-year forecast by $X] / [timing — no forecast adjustment required; expected to normalize in [month]].

### Commentary Quality Test

Before finalizing, apply the "so what" test to each commentary block:
- Does it explain what happened? ✓/✗
- Does it explain why it happened? ✓/✗
- Does it classify the variance (permanent vs. timing)? ✓/✗
- Does it state the business implication or forecast impact? ✓/✗
- Is it under 50 words? ✓/✗

Any "no" is a rewrite requirement.

## P&L Variance Waterfall

Structure the variance waterfall in this order to match the standard P&L:

1. **Revenue**
   - New ARR (volume × price)
   - Expansion MRR (net revenue retention drivers)
   - Churn (gross and net)
   - One-time / professional services
2. **Cost of Revenue**
   - Hosting / infrastructure
   - Support headcount
   - Third-party SaaS in COGS
3. **Gross Profit / Gross Margin %**
4. **Operating Expenses**
   - R&D (headcount, contractors, tools)
   - S&M (headcount, media, events)
   - G&A (headcount, professional fees, office)
5. **EBITDA / Net Operating Loss**
6. **Cash and Runway** (non-GAAP bridge)

## Forecast Adjustment Decision Rules

| Variance Classification | Forecast Adjustment Rule |
|------------------------|--------------------------|
| Volume — demand-driven | Update full remaining-year forecast from current period forward |
| Price — structural discounting | Update ACV assumption for new bookings only |
| Timing — recognized late | Shift the amount to the correct future period; no net change |
| One-time — truly non-recurring | No forecast adjustment; footnote in outlook section |
| Mix — structural segment shift | Adjust segment mix assumptions and recalculate blended metrics |
| Headcount timing — hire slipped | Shift cost and productivity to new hire month |
