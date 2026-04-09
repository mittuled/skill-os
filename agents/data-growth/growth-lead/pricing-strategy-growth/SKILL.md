---
name: pricing-strategy-growth
description: >
  This skill contributes the growth perspective to pricing strategy including freemium, trial, and expansion mechanics. Use when asked to design freemium tiers, set trial parameters, or plan expansion revenue mechanics. Also consider when pricing strategy is being developed without growth input. Suggest when the team debates free vs. paid without modelling conversion economics.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "define pricing strategy"
  - "growth pricing plan"
  - "pricing model design"
  - "monetization strategy growth"
  - "pricing approach growth"
---

# pricing-strategy-growth

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The pricing strategist contributes the growth perspective to pricing design by modelling how freemium limits, trial lengths, tier boundaries, and expansion triggers affect acquisition velocity, activation rates, conversion economics, and net revenue retention.

## When to Use

- When the product team is designing the initial pricing structure and needs growth input on freemium/trial mechanics.
- When the team debates free tier generosity and needs data-backed guidance on where to set limits.
- When expansion revenue (upsell, seat-based, usage-based) underperforms and pricing mechanics may be the cause.
- When a competitive pricing change forces a reassessment of the growth impact of current pricing.

## Workflow

1. **Analyse growth model inputs**: Review the growth model's acquisition, activation, and conversion assumptions. Identify which pricing mechanics directly affect each conversion rate.
2. **Design freemium/trial mechanics**: Propose the free tier boundary (which features, usage limits) and trial parameters (length, feature access, credit card requirement). Align the boundary so users can reach the activation moment for free.
3. **Model conversion economics**: Estimate free-to-paid conversion rate under different tier configurations. Model the trade-off between a generous free tier (higher acquisition, lower conversion) and a restrictive free tier (lower acquisition, higher conversion).
4. **Design expansion triggers**: Define the usage thresholds, seat counts, or feature needs that naturally push users to the next tier. Ensure triggers align with value milestones, not arbitrary limits.
5. **Benchmark competitors**: Compare proposed pricing mechanics against 3-5 competitors. Identify where the pricing is differentiated and where it follows category norms.
6. **Deliver pricing recommendation**: Produce a growth pricing brief with recommended tier structure, trial parameters, expansion triggers, conversion model, and competitive comparison.

## Anti-Patterns

- **Free tier as marketing only**: Treating the free tier as a lead-gen tool without ensuring users can experience core value produces sign-ups that never activate. *Why*: users who cannot reach the aha moment on the free tier churn before they ever consider paying.
- **Arbitrary usage limits**: Setting free tier limits based on cost rather than value milestones creates friction at random points in the user journey. *Why*: the paywall should appear when the user has received enough value to justify payment, not when infrastructure cost crosses a threshold.
- **No expansion modelling**: Designing pricing without modelling upsell mechanics leaves net revenue retention below 100%. *Why*: without expansion revenue, revenue growth depends entirely on new acquisition, which is more expensive.

## Output

**Success:**
- A growth pricing brief containing recommended freemium/trial mechanics, tier boundaries, expansion triggers, conversion model with scenario analysis, and competitive benchmarks.

**Failure:**
- The recommended pricing structure cannot achieve the growth model's conversion targets. Report the gap, the conversion rate sensitivity analysis, and alternative pricing configurations to test.

## Related Skills

- [`pricing-finaliser-growth`](../pricing-finaliser-growth/SKILL.md) -- reviews the pricing strategy this skill produces for final growth approval.
- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the growth model's conversion assumptions constrain pricing design.
- [`distribution-viability-check`](../distribution-viability-check/SKILL.md) -- distribution economics interact with pricing; a high-CAC channel requires higher conversion or higher ARPU.
