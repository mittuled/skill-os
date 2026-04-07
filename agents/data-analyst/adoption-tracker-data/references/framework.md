# Framework: Adoption Tracker

Defines the methodology for measuring feature adoption using behavioural event data and cohort analysis.

## Adoption Criteria Definition

An "adopted" user must meet a frequency and time-window threshold, not just a first-use event:

| Definition Type | Formula | Example |
|----------------|---------|---------|
| Threshold-based | Used feature ≥ N times within first M days | "Exported file ≥ 3 times in first 14 days" |
| Habit-based | Used feature in ≥ X of any 4 consecutive weeks | "Viewed reports in 3 of any 4 weeks" |
| Value milestone | Completed a defined outcome event | "Sent first campaign and received ≥ 1 open" |

The adoption definition must be documented before analysis begins — do not reverse-engineer a definition from the data.

## Adoption Funnel Stages

| Stage | Definition | Event |
|-------|-----------|-------|
| Reached (eligible) | User was in a state where feature discovery was possible | `feature_eligible` or derived from plan/onboarding step |
| Discovered | User saw or was shown the feature | `feature_viewed`, `tooltip_shown`, or `menu_item_visible` |
| Tried | User performed the feature's primary action at least once | `[feature]_used` (first occurrence) |
| Adopted | User met the adoption criteria (threshold or habit) | Derived from repeated `[feature]_used` events |
| Churned from feature | Previously adopted user has not used feature in 30 days | Derived: no `[feature]_used` in last 30 days after adoption |

## Adoption Curve Metrics

For each cohort, compute and plot over time (Days 1–90 post-exposure):

| Metric | Formula |
|--------|---------|
| Cumulative adoption rate | adopted users / eligible users at day N (cumulative) |
| Time-to-first-use (median) | PERCENTILE(50, days from eligible to first use) |
| Time-to-adoption (median) | PERCENTILE(50, days from eligible to adoption criteria met) |
| Terminal adoption rate | adoption rate at Day 90 (or last point of observable data) |

## Retention Correlation Analysis

Correlate feature adoption with Day 7/30/90 retention using:

1. Split users into "adopted" and "not adopted" groups (as of Day 30 post-exposure).
2. Compute retention rate for each group at Day 7, 30, and 90.
3. If the adoption group retains significantly better (>10pp difference), the feature is an activation / retention driver.
4. Run statistical significance test: two-proportion z-test, p < 0.05, minimum 200 users per group.

**Caution:** This is correlation, not causation. High-intent users may adopt more features AND retain better. Use holdout experiments to confirm causation.

## Cohort Segmentation Protocol

Segment adoption by:

| Dimension | Why | What to Flag |
|-----------|-----|-------------|
| Signup cohort (week) | Detects whether recent product changes improved adoption | >5pp difference between recent and older cohorts |
| Acquisition channel | Detects channel-quality and message-fit issues | Channel with <50% of average adoption rate |
| Plan tier | Detects pricing/feature-gate alignment | If paid adoption >> free adoption, consider gating or nudging |
| Platform (web/mobile) | Detects platform-specific UX friction | >10pp platform gap signals platform-specific issue |

## Bottleneck Identification Rule

The primary adoption bottleneck is the stage with the largest absolute gap:

```
Gap at stage = users_entering_stage − users_completing_stage
Primary bottleneck = stage with MAX(gap)
```

Distinguish between:
- **Discovery problem**: Large gap at Reached → Discovered (users are not seeing the feature)
- **Value problem**: Large gap at Tried → Adopted (users try once but do not find enough value to return)
- **Awareness problem**: Large gap at Discovered → Tried (users see the feature but do not engage)
