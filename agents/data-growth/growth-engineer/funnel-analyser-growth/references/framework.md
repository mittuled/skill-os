# Framework: Growth Funnel Analysis

Defines the method for measuring acquisition-to-activation funnel conversion, identifying bottleneck steps, and prioritizing experiments by impact.

## Funnel Architecture

The growth funnel has 5 canonical stages. Each stage maps to one or more tracking events:

| Stage | Event Signal | Typical Conversion (PLG SaaS) |
|-------|-------------|------------------------------|
| 1. First Touch | Landing page view (UTM captured) | — |
| 2. Signup | signup_completed | 2–8% of landing page visitors |
| 3. Onboarding | onboarding_completed (all required steps) | 40–70% of signups |
| 4. Activation | Activation event (product-defined) | 25–50% of signups |
| 5. Conversion | subscription_created or first_purchase | 2–5% of total signups (freemium) |

These are reference benchmarks. Compute your own baseline before comparing.

## Bottleneck Identification Method

### Step 1 — Compute step-to-step conversion rates

For each consecutive pair (Step N → Step N+1):
```
step_conversion_N = users_entering_step_N+1 / users_entering_step_N
absolute_loss_N = users_entering_step_N - users_entering_step_N+1
```

### Step 2 — Rank by absolute user loss (not lowest conversion rate)

The highest-leverage step is the one with the **largest absolute_loss**, not the lowest percentage conversion.

### Step 3 — Apply segmentation

Repeat the funnel analysis for each dimension:
- **Acquisition channel**: Paid search, organic SEO, referral, direct, email
- **Device**: Mobile web, desktop web, iOS native, Android native
- **Signup cohort**: Weekly cohorts to detect temporal trends

### Step 4 — Calculate experiment value

For the top bottleneck step:
```
potential_users_gained = absolute_loss × improvement_target (e.g., 10%)
revenue_impact = potential_users_gained × trial-to-paid_rate × ARPU
```

## Channel Benchmark Comparison

When channel-segmented analysis is available, flag channels whose conversion at the bottleneck step is ≥20 pp below the best-performing channel. This gap indicates a channel-specific issue (landing page mismatch, audience quality, onboarding friction for that persona).

## Analysis Window Guidelines

| Use Case | Recommended Window |
|---------|-------------------|
| Baseline for new experiment | 4 weeks pre-experiment |
| Cohort trend analysis | 12 weekly cohorts |
| Channel comparison | 4 weeks (enough volume per channel) |
| Seasonal adjustment | Year-over-year same period |

## Experiment Recommendation Template

For each top bottleneck, produce one experiment recommendation:

| Field | Content |
|-------|---------|
| Bottleneck step | [Step N → Step N+1] |
| Current conversion | [X%] |
| Root cause hypothesis | [e.g., "Long form with 8 fields reduces signup completion"] |
| Experiment | [e.g., "Reduce signup to email + password only; defer profile fields to onboarding"] |
| Target conversion | [X + N%] |
| Expected user gain (monthly) | [Absolute users] |
| ICE priority score | Impact × Confidence × Ease |
