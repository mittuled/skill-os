# Framework: Retention Email Designer

Defines the structural framework for building churn-prevention and re-engagement email sequences.

## Churn Risk Signal Model

| Signal Category | Examples | Severity | Response Window |
|----------------|----------|----------|----------------|
| Usage decline | Login frequency drops >50% over 14 days | Medium | 48 hours |
| Feature abandonment | Core feature usage drops to zero for 7+ days | High | 24 hours |
| Support escalation | 3+ tickets in 7 days or CSAT < 3 | High | Immediate |
| Billing warning | Failed payment, downgrade inquiry | Critical | Immediate |
| Competitive signal | Competitor login detected, export of data | Critical | Immediate |

## Intervention Tiers

| Tier | Risk Level | Approach | Example |
|------|-----------|----------|---------|
| 1 — Nudge | Low (early signal) | Value reminder, feature highlight | "You haven't used [feature] in 2 weeks — here's what teams are building with it" |
| 2 — Re-engage | Medium (sustained decline) | Personalised usage summary, success story | "Your team processed 1,240 records last month — here's how to get more value" |
| 3 — Rescue | High (pre-churn) | Human touchpoint, premium offer | "Your account manager wants to help — book a 15-min call" |
| 4 — Win-back | Churned | Return incentive, product update | "We've shipped 3 features you asked for — come back and see" |

## Sequence Design Rules

1. **Lead with value delivered**: remind users what they have built or achieved, not what they are missing
2. **Escalate intervention, not frequency**: more emails does not equal more retention; escalate the type of touchpoint instead
3. **Segment by account value**: high-ACV accounts get human touchpoints earlier; low-ACV accounts follow automated sequences longer
4. **Validate signals before triggering**: confirm the risk signal is sustained (2+ data points) before entering a user into the sequence to avoid false positives
5. **Never lead with discounts**: discounts are tier-3 interventions for high-value accounts only, never tier-1
