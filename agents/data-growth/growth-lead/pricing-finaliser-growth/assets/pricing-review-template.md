# Pricing Growth Review

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | pricing-finaliser-growth |
| Product / Feature | [Name of the pricing structure under review] |
| Review Trigger | [Launch / Pricing change / Conversion drop] |

## Executive Summary

[2-3 sentences with the verdict and key reasons. Lead with the approval status.
GUIDANCE: Example — "Pricing structure is Approved with Conditions. The freemium-to-paid gate appears after the activation moment, but the trial length (7 days) is insufficient for the majority of users (median time-to-activation: 11 days). Extending the trial to 14 days is required before launch."]

## Pre-Activation Friction Assessment

[List every monetization touchpoint that appears before the activation moment.
GUIDANCE:
- Good: "No gates appear before the activation moment (first dashboard creation). The paywall first appears on the 3rd dashboard creation — 2 completions after activation."
- Bad: "The credit card is required at signup before users can access the core dashboard feature."
- Format: Table with columns: Touchpoint | Funnel Position | Blocks Activation? | Verdict]

| Touchpoint | Funnel Position | Blocks Activation? | Verdict |
|-----------|----------------|-------------------|---------|
| [e.g., Credit card at signup] | [e.g., Step 1 of signup] | [Yes/No] | [Pass/Fail/Flag] |

## Conversion Rate Model

[Model the expected signup-to-paid and trial-to-paid conversion rates based on the pricing structure.
GUIDANCE:
- Good: "At a $29/month Pro tier with 14-day opt-in trial, we model 18% trial-to-paid conversion based on comparable PLG SaaS benchmarks (industry range: 15–25%). At 500 trial starts/month, this yields 90 new paid customers/month."
- Bad: "Conversion should be fine based on the price point."
- Format: Table showing conversion assumptions, benchmarks, and monthly impact]

| Metric | Assumption | Industry Benchmark | Projected Value |
|--------|-----------|-------------------|----------------|
| Trial-to-paid conversion | [%] | [15–25% opt-in trial] | [%] |
| Freemium-to-paid conversion | [%] | [2–5% freemium] | [%] |
| Monthly trial starts | [#] | — | [#] |
| Projected new paid/month | — | — | [# = trials × conversion] |

## Expansion Mechanic Evaluation

[Assess whether the pricing structure creates natural expansion triggers that drive NRR > 100%.
GUIDANCE:
- Good: "Seat-based pricing at $15/seat/month creates a natural expansion trigger: when a team adopts the product, each additional invite generates incremental MRR. Historical data from comparable tools shows seat expansion at 40% of accounts within 90 days."
- Bad: "Flat pricing at $99/month with no usage limits or seat differentiation provides no expansion mechanic."
- Format: Describe each mechanic, its NRR impact, and whether it is sufficient for growth targets]

**Pricing model type**: [Freemium / Trial / Seat-based / Usage-based / Flat]

**Natural expansion triggers**:
- [Mechanic 1]: [Expected NRR impact]
- [Mechanic 2 if applicable]: [Expected NRR impact]

**NRR target**: [>100% / >110% / other]
**Assessment**: [Sufficient / Insufficient — explain]

## Tier Boundary Analysis

[Evaluate whether tier boundaries are set at the right funnel positions to maximize conversion without creating premature friction.
GUIDANCE:
- Good: "The Pro tier gate triggers when a user creates their 5th dashboard. Median activated users create 3 dashboards in the first week — placing the gate after activation and after the user has experienced repeated value."
- Bad: "The Pro tier gate triggers immediately on creating the first dashboard, which is the activation moment itself."
- Format: List each tier boundary with its position relative to the activation moment]

| Tier Boundary | Trigger Point | Activation Moment Position | Verdict |
|--------------|--------------|--------------------------|---------|
| Free → Pro | [e.g., 5th dashboard] | [e.g., After activation (activation = 1st dashboard)] | [Pass / Fail] |
| Pro → Enterprise | [e.g., 10 seats] | [e.g., Post-activation, post-adoption] | [Pass / Fail] |

## Verdict and Conditions

**Approval Status**: [Approve / Approve with Conditions / Reject]

**Conditions** (if applicable):
1. [Condition 1 — specific change required, e.g., "Extend trial from 7 to 14 days before launch"]
2. [Condition 2 if applicable]

**Recommended Adjustments** (if rejected):
1. [P1 adjustment with rationale]
2. [P2 adjustment if applicable]

## Recommendations

[Prioritized list of changes required for approval or to improve conversion.
GUIDANCE: Each recommendation must be specific and assignable.
- P1 (Must fix before launch): Items that block approval
- P2 (Fix within 30 days post-launch): Items that reduce conversion but do not block
- P3 (Consider in next pricing cycle): Longer-term improvements]

| Priority | Recommendation | Owner | Timeline |
|----------|---------------|-------|---------|
| P1 | [Specific change] | [Growth Lead / Product] | [Before launch / Date] |
| P2 | [Specific change] | [Growth Lead / Product] | [30 days post-launch] |

## Appendices

### A. Methodology

[Frameworks applied: pre-activation friction check, conversion rate modeling using Reforge PLG benchmarks, expansion mechanic NRR analysis. Data sources: growth model, activation moment definition, pricing documentation.]

### B. Supporting Data

[Include conversion rate benchmarks referenced, activation funnel data used, and any existing conversion data that informed the model.]
