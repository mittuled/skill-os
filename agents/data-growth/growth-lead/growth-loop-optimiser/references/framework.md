# Framework: Growth Loop Optimisation

Defines the method for mapping, measuring, and systematically improving growth loop throughput using viral coefficient analysis and compounding impact modelling.

## Loop Taxonomy

| Loop Type | Core Mechanic | Primary Metric | Typical k-factor Range |
|-----------|--------------|---------------|----------------------|
| Viral / Referral | User invites → new user joins | Viral coefficient (k) | 0.1–0.8 for B2B SaaS; 0.3–2.0 for consumer |
| Content / SEO | User creates content → organic traffic → new signups | Content amplification factor | Variable by domain authority |
| Paid reinvestment | Revenue → paid acquisition → more revenue | ROAS × reinvestment rate | Depends on unit economics |
| Product-led / Collaboration | Feature drives team adoption → more seats | Seat expansion rate | 10–40% account expansion within 90 days |

## Loop Measurement Model

For each active loop, compute at every node:

```
Loop throughput (k-factor for viral) = (users entering loop) × (invites/actions per user) × (conversion per invite)

For a viral loop:
k = invites_sent_per_user × invite_conversion_rate

Cycle time = average days from trigger to new user activation

Compounding model:
users_at_cycle_N = seed_users × k^N
```

**Thresholds**:
- k ≥ 1.0: Super-viral (exponential growth). Rare in B2B.
- k ≥ 0.5: Strong loop. Meaningfully compounding.
- k ≥ 0.15: Viable loop. Contributes 15%+ acquisition lift over 10 cycles.
- k < 0.1: Broken loop. Structural redesign required before optimization.

## Bottleneck Identification Method

Map each loop as a funnel of nodes. At each node compute:
1. Users entering the node
2. Users completing the node's action
3. Conversion rate = (2) / (1)

The bottleneck is the node with the **largest absolute user loss** (not the lowest conversion rate). A 70% → 60% conversion on 100,000 users is a larger absolute loss than 5% → 2% conversion on 1,000 users.

## Experiment Design Framework

For the top bottleneck node, use this ICE-prioritized experiment structure:

| Field | Description |
|-------|-------------|
| Hypothesis | "If we [change X], then [metric Y] will improve by [N%] because [mechanism Z]" |
| Success metric | Specific node conversion rate or loop throughput metric |
| MDE (minimum detectable effect) | Calculate: 2 × σ / √(n) for two-sided test at α=0.05, power=0.8 |
| Sample size | Use: n = 16 × σ² / MDE² per variant |
| ICE score | Impact (1-10) × Confidence (1-10) × Ease (1-10) |

## Compounding Impact Model

Project the 6-month user growth impact of a loop improvement:

```
Improvement scenario: k improves from k_baseline to k_new
Cycle time: T days

Cycles in 6 months = 180 / T
User multiplier (baseline) = 1 / (1 - k_baseline)  [steady-state if k < 1]
User multiplier (improved) = 1 / (1 - k_new)

Incremental user uplift % = (k_new - k_baseline) / (1 - k_baseline) × 100
```

**Important**: A 10% relative improvement in k (e.g., 0.3 → 0.33) compounds across every cycle. Model conservatively: assume 50% of the modelled uplift materializes.

## Prioritization Rule

Rank optimization opportunities by:
`Priority score = (absolute_user_gain_if_fixed / total_users) × confidence × (1 / implementation_effort_weeks)`

Fix structural loops (k < 0.1) before optimizing functioning ones.
