# Framework: Cohort Selection

## Core Model

Cohort selection balances two competing objectives: maximising learning signal quality and minimising blast radius if the feature fails. The optimal cohort is the smallest group that produces statistically meaningful signal while keeping revenue and reputational risk within acceptable bounds.

## Cohort Sizing Formula

Target cohort size must satisfy the minimum detectable effect (MDE) requirement:

- Define the primary adoption metric and its current baseline
- Set the minimum lift you need to observe to declare success (e.g., +5 pp activation rate)
- At 80% power and 95% confidence: cohort size ≈ 16 × σ² / δ² (where δ = MDE, σ = standard deviation)
- Round up to the nearest feature-flag-friendly percentage (e.g., 5%, 10%, 20%)

Heuristic shortcut: For activation rate metrics, plan for at least 400 users per variant to detect a 5 pp difference.

## Segmentation Dimension Priority

| Priority | Dimension | When to Use |
|----------|-----------|-------------|
| 1 | Plan tier | Always — behaviour differs fundamentally by tier |
| 2 | Activation cohort (join date) | When feature relevance depends on user maturity |
| 3 | Usage intensity | When feature targets power users or light users |
| 4 | Geography | When compliance, latency, or language is a factor |
| 5 | Company size | When feature has different enterprise vs SMB implications |

## Risk Tier Rubric

| Risk Tier | Criteria | Maximum Cohort % |
|-----------|----------|-----------------|
| Low | No billing impact; no SLA exposure; no data migration | Up to 50% |
| Medium | Minor UX change; affects non-critical workflow; easily reversible | Up to 20% |
| High | Billing-adjacent; workflow-critical; affects enterprise accounts | Up to 5% |
| Critical | Affects contractual SLAs, payment flows, or data export | Max 1%; requires VP sign-off |

## Representativeness Validation

Compare cohort composition against population on:
- Plan tier distribution (within ±5 pp)
- Geography distribution (within ±10 pp)
- Account age distribution (within ±10 pp)
- MRR concentration (top 10 accounts must not exceed 30% of cohort ARR unless intentional)

Fail the representativeness check if any dimension exceeds these bounds without explicit justification.

## Rollback Trigger Definitions

| Trigger Type | Definition | Example Threshold |
|---|---|---|
| Performance | Server error rate or latency exceeds baseline | >2x baseline p95 latency |
| Revenue | Conversion or upgrade rate drops | >10% below baseline for 48 hours |
| Support | Ticket spike attributable to the feature | >3x normal ticket volume |
| User | Explicit negative signal from key accounts | Any enterprise account submits critical bug |

## Exclusion Rules (Always Apply)

- Exclude users currently in another A/B test affecting the same flow
- Exclude users in onboarding (< 7 days since signup) unless the feature is onboarding-specific
- Exclude accounts flagged as churned, delinquent, or in contract renegotiation
