# Framework: Funnel Analyser

Defines the analytical methodology for diagnosing conversion funnels using AARRR and product-level frameworks.

## Funnel Classification

| Funnel Type | Scope | Key Metrics | AARRR Stage |
|------------|-------|------------|------------|
| Acquisition funnel | Ad click → landing page → signup | Click-to-visit, visit-to-signup, CPA | Acquisition |
| Activation funnel | Signup → first key action → "aha moment" | Time-to-activation, activation rate | Activation |
| Core product funnel | Feature discovery → trial → adoption | Discovery-to-trial, trial-to-adoption | Retention |
| Upgrade funnel | Free → upgrade intent → paid | Intent-to-upgrade, checkout completion | Revenue |
| Referral funnel | Invite sent → invite accepted → new user activated | Invite acceptance rate, referral activation | Referral |

## Step Metrics

For each funnel step, compute:

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| Step entry count | COUNT(DISTINCT user_id) WHERE event = step_N | Absolute volume entering the step |
| Step completion count | COUNT(DISTINCT user_id) WHERE event = step_N+1 | Absolute volume completing the step |
| Step conversion rate | completion / entry | % of entrants who proceed |
| Absolute drop-off | entry − completion | Users lost at this step |
| Time-to-next-step (median) | PERCENTILE(50, time_between_step_N and step_N+1) | Latency-driven abandonment signal |
| Time-to-next-step (P90) | PERCENTILE(90, time) | Long tail friction indicator |

## Drop-Off Prioritization

Rank steps by impact score:

```
Impact score = Absolute drop-off volume × (1 − step conversion rate)
```

The step with the highest impact score is the highest-leverage target for optimization. Address steps in impact-score order.

## Segmentation Protocol

Always run the funnel on at least three segmentation dimensions before reporting:

1. **Acquisition channel** (paid search, organic, referral, direct) — reveals channel-quality issues
2. **Device / platform** (desktop web, mobile web, iOS, Android) — reveals UX friction specific to a surface
3. **Cohort date** (week of signup) — reveals whether recent changes affected conversion
4. **Plan tier** (free, trial, paid) — reveals whether the funnel differs by value alignment

Flag any segment where the conversion rate differs from the overall rate by >10 percentage points.

## Time-Based Analysis

Plot 7-day rolling conversion rates for each step to detect:

| Pattern | Signal | Investigation |
|---------|--------|--------------|
| Sudden drop coinciding with a deploy date | Regression introduced by product change | Check deploy logs; compare pre/post conversion |
| Gradual decline over 30+ days | UX entropy or competitor displacement | Benchmark against historical cohort baselines |
| Weekly seasonality | Weekday vs. weekend user behaviour | Segment by day of week before diagnosing |
| Step-specific decline with stable overall rate | Instrumentation failure at the step | Verify event is firing correctly |

## Statistical Significance Check

Before concluding a drop-off is meaningful:
- Minimum 200 users per step per segment
- Run a two-proportion z-test for segment comparisons (p < 0.05 threshold)
- For time-based comparisons, use 7-day rolling averages to reduce day-of-week noise

## Root Cause Hypothesis Categories

| Category | Signals | Experiments |
|---------|---------|------------|
| UX friction | High time-to-next-step P90, session recordings show rage clicks | UX simplification, progressive disclosure |
| Copy / trust | Drop-off at commitment steps (upgrade, signup), exit survey mentions cost | A/B test copy, social proof, trust signals |
| Technical error | Error rate spike at step, console errors, support tickets mentioning failure | Fix bugs, add error recovery flows |
| Wrong audience | Low-intent channel conversion gap vs. high-intent channels | Channel qualification, messaging alignment |
| Feature awareness | High discovery gap (saw feature vs. tried it) | In-app tooltip, onboarding checklist |
