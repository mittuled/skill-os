# Framework: Activation Signal Definition

Defines the analytical method for identifying, validating, and formalizing the user behaviour that best predicts long-term retention.

## Signal Discovery Method

### Step 1 — Candidate Generation

Interview or survey cohorts with contrasting retention outcomes:
- **Retained users**: Active past Day 30 with ≥3 sessions in the period
- **Churned users**: No session after Day 7

Probe for the first action that felt like value delivery. Combine qualitative themes with a quantitative list of candidate behaviours from product event logs.

### Step 2 — Retention Correlation Analysis

For each candidate behaviour B, compute:

```
activation_rate     = users who completed B within window / total new users
retention_if_done   = Day-30 retention rate for users who completed B
retention_if_not    = Day-30 retention rate for users who did not complete B
retention_lift      = retention_if_done - retention_if_not
```

**Minimum viable signal**: `retention_lift ≥ 10 percentage points`

Rank candidates by `retention_lift`. If multiple candidates clear the threshold, prefer the one with the highest `activation_rate` (widest reachable population).

### Step 3 — Threshold and Window Optimization

For the top candidate, test a grid of (threshold, window) combinations:

| Variable | Typical Range |
|----------|--------------|
| Threshold (times) | 1, 2, 3, 5 |
| Window (days from signup) | 1, 3, 7, 14 |

Select the combination that maximizes `retention_lift` while keeping `activation_rate ≥ 20%`.

**Benchmarks**:
- Consumer apps: activation rate target ≥ 40% within 7 days
- SaaS/B2B tools: activation rate target ≥ 25% within 14 days
- Marketplace / two-sided: activation rate target ≥ 30% within 7 days (supply side may differ)

### Step 4 — Formalization Template

Write the activation signal as a single unambiguous statement:

```
A user is activated when they [event_name] [threshold] times
within [window] days of signup.
```

Include: event name (exact analytics event), threshold (integer), window (integer days), retention lift (percentage points), activation rate (%).

## Discriminative Power Test

A well-formed activation signal must pass all three checks:

| Check | Pass Condition | Fail Condition |
|-------|---------------|---------------|
| Retention lift | ≥10 pp above non-activated users | <10 pp — signal is weak predictor |
| Activation rate | 20–80% of new users reach it | <20%: too hard; >80%: too easy (trivial) |
| Leading indicator | Occurs within first 14 days | Occurs after Day 30: too late to be actionable |

## Common Activation Signal Patterns by Product Type

| Product Type | Common Activation Pattern |
|-------------|--------------------------|
| Collaboration tool | "Invited ≥1 teammate within 7 days" |
| Analytics / BI | "Viewed ≥1 chart they created within 3 days" |
| E-commerce / marketplace | "Completed ≥1 purchase within 7 days" |
| Content creation | "Published ≥1 piece of content within 7 days" |
| Communication | "Sent ≥5 messages within 3 days" |

These are starting hypotheses only — always validate against your own retention data.
