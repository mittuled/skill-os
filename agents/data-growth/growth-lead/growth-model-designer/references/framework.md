# Framework: Growth Model Designer

Defines the structural methodology for building a quantitative AARRR growth model with loop mechanics, unit economics, and leverage-point analysis.

## Growth Accounting Equation

Growth = Acquisition × Activation Rate × Retention Rate × Expansion Factor

Where:
- **Net MoM growth** = New Activated Users − Churned Users + Reactivated Users
- **Healthy growth** requires Net New > Churned at every time step

## AARRR Stage Map

| Stage | Definition | Key Metric | Typical Benchmark |
|-------|-----------|------------|------------------|
| Acquisition | First-touch to signup | CAC per channel | $10–$500 depending on category |
| Activation | Signup to aha moment | Activation rate | 20–40% for consumer, 30–60% for SaaS |
| Retention | Active at Day 30 | D30 retention | 10–25% consumer, 25–50% SMB SaaS |
| Revenue | Conversion to paid | Free-to-paid rate | 2–5% freemium, 15–25% trial |
| Referral | Viral coefficient | k = invites × conv. | k > 0.1 meaningful, k > 0.5 strong |

## Growth Loop Taxonomy

### Viral Loop
- **Cycle**: User action → invite → new user → activation → next invite
- **Throughput metric**: Viral coefficient (k = invites_sent × invite_to_signup_rate × signup_to_activation_rate)
- **Cycle time**: Median days from trigger to referred activation
- **Minimum viable k**: 0.15 for meaningful compounding; k ≥ 1.0 = exponential (rare)

### Content Loop
- **Cycle**: User creates content → SEO/social distribution → new user discovers → signs up → creates content
- **Throughput metric**: Content amplification factor (new_users_per_piece_of_content)
- **Cycle time**: Days from publish to signup attribution

### Paid Loop
- **Cycle**: Revenue → reinvested in paid acquisition → new users → revenue
- **Throughput metric**: ROAS × reinvestment rate → net new users per dollar
- **Viability gate**: Only compounding if LTV > CAC with positive payback within cash runway

### Product-Led Loop
- **Cycle**: User uses product → invites colleague for collaboration → colleague activates → invites more
- **Throughput metric**: Invites per activated user × invite-to-activation rate
- **Distinguishing factor**: Invitation is embedded in the product workflow, not a separate referral mechanic

## Unit Economics Model

| Metric | Formula | Target |
|--------|---------|--------|
| CAC | Total acquisition spend / New paid customers | < LTV / 3 |
| LTV | ARPU × Gross Margin / Churn Rate | > 3× CAC |
| LTV:CAC ratio | LTV / CAC | ≥ 3:1 |
| CAC payback | CAC / (ARPU × Gross Margin) | ≤ 12 months |
| NRR | (Starting MRR + Expansion − Contraction − Churn) / Starting MRR × 100 | ≥ 100% |

## Sensitivity Analysis Method

For each model variable V, compute the sensitivity score:
- **Impact**: % change in 12-month active users from a 10% improvement in V
- **Confidence**: Current measurement confidence (High / Medium / Low / Estimated)
- **Priority score**: Impact × Confidence

Rank all variables by priority score. The top 3 are the primary leverage points for the next quarter's growth experiments.

## Forecast Model Structure

```
Inputs (monthly):
  - New acquired users (by channel)
  - Activation rate (%)
  - Monthly churn rate (%)
  - Reactivation rate (%)
  - Monthly expansion revenue per user ($)

Outputs:
  - Monthly active users
  - Monthly recurring revenue
  - Cumulative CAC spend
  - Blended CAC
  - LTV:CAC ratio at each time step
```

Scenario toggles: Base (current assumptions), Optimistic (+20% activation, -10% churn), Pessimistic (-20% activation, +10% churn).
