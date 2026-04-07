# Growth Model

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | growth-model-designer |

## Executive Summary

[2-3 sentences identifying the primary growth lever, the highest-risk assumption, and the 12-month active user forecast under base-case assumptions.
GUIDANCE: Lead with the leverage point finding — e.g., "A 10% improvement in activation rate produces 34% more 12-month active users than a 10% improvement in acquisition volume, making onboarding the primary growth priority." Do not restate the methodology.]

## AARRR Stage Definitions

[Map each stage to the specific user action and threshold in this product.

GUIDANCE:
- Good: "Activation: User creates their first project and invites at least one teammate within 7 days of signup. Event: `project_created` + `teammate_invited`. Data source: product analytics."
- Bad: "Activation: User becomes active." (no event, no threshold, not measurable)
- Format: Table with Stage, User Action, Tracking Event, Time Window, Current Rate, Benchmark]

| Stage | User Action | Tracking Event | Time Window | Current Rate | Category Benchmark |
|-------|------------|----------------|-------------|-------------|-------------------|
| Acquisition | [e.g., Signs up via any channel] | `user_signed_up` | — | [X%] | [Y%] |
| Activation | [e.g., Completes first value action] | `activation_event` | Day 0-7 | [X%] | [Y%] |
| Retention | [e.g., Returns and completes core action] | `core_action` | Monthly | [X%] | [Y%] |
| Revenue | [e.g., Upgrades to paid plan] | `plan_upgraded` | — | [X%] | [Y%] |
| Referral | [e.g., Invites a new user who activates] | `referral_activated` | — | k = [X] | k = [Y] |

## Growth Loops

[Document each active growth loop with node-level throughput metrics.

GUIDANCE:
- Good: "Viral loop k = 0.18 (invites_sent=2.3/user × invite_to_signup=12% × signup_to_activation=65%). Cycle time: 8 days. Bottleneck: invite_to_signup conversion is 3× below category benchmark."
- Bad: "Users share the product with friends." (no metrics, no bottleneck identification)
- Format: One subsection per loop with a node table and throughput summary]

### Loop 1: [Loop Name — e.g., Viral Invite Loop]

| Node | Metric | Current Value | Benchmark | Gap |
|------|--------|--------------|-----------|-----|
| Trigger impression | Impressions / activated user / month | [X] | [Y] | [±Z] |
| Trigger action rate | % who act on trigger | [X%] | [Y%] | [±Z] |
| Distribution conversion | Invites sent / trigger action | [X] | [Y] | [±Z] |
| Referred signup rate | Signups / invite | [X%] | [Y%] | [±Z] |
| Referred activation rate | Activation / referred signup | [X%] | [Y%] | [±Z] |
| **Viral coefficient (k)** | Product of above conversion rates | **[k]** | **[k_benchmark]** | |
| Cycle time | Median days trigger→referred activation | [X] days | [Y] days | |

### Loop 2: [Loop Name]

[Repeat node table format]

## Unit Economics

[Model CAC, LTV, and ratio per channel and overall.

GUIDANCE:
- Good: "Paid search CAC: $180. LTV: $720 (ARPU $30 × 24-month avg. tenure × 100% gross margin). LTV:CAC: 4:1. Payback: 6 months. Scenario at 2× spend: estimated CAC $240 (CPM inflation), LTV:CAC drops to 3:1, still viable."
- Bad: "Our LTV:CAC is good." (no numbers, no channel breakdown)
- Format: Table per channel plus aggregate, with 2× and 5× scaling scenarios]

| Channel | CAC | LTV | LTV:CAC | Payback | 2× Scale CAC | Status |
|---------|-----|-----|---------|---------|-------------|--------|
| [Channel 1] | $[X] | $[Y] | [Z]:1 | [N] mo | $[X2] | [Go/Caution/No-Go] |
| [Channel 2] | $[X] | $[Y] | [Z]:1 | [N] mo | $[X2] | [Go/Caution/No-Go] |
| **Blended** | $[X] | $[Y] | [Z]:1 | [N] mo | — | — |

## 12-Month Forecast

[Present base, optimistic, and pessimistic scenarios.

GUIDANCE:
- Good: Spreadsheet-backed projections with distinct assumption sets per scenario and sensitivity toggle for each key variable.
- Bad: Single line graph with no scenario variation or assumption documentation.
- Format: Monthly table for each scenario with the 3 most sensitive assumptions called out]

| Month | Base MAU | Optimistic MAU | Pessimistic MAU | Base MRR |
|-------|----------|---------------|----------------|---------|
| M1 | | | | |
| M3 | | | | |
| M6 | | | | |
| M12 | | | | |

**Key assumptions (Base):** Activation rate [X]%, Monthly churn [Y]%, New acquisition/mo [Z]

## Leverage Point Analysis

[Rank all conversion rates by sensitivity — 10% improvement impact on 12-month MAU.

GUIDANCE:
- Good: "1. Activation rate (+10%): +34% MAU. 2. D30 churn (-10%): +28% MAU. 3. Acquisition volume (+10%): +10% MAU." Sorted by impact, confidence noted.
- Bad: A list of things to improve without quantified impact ranking.]

| Rank | Variable | Current Value | +10% Impact on 12mo MAU | Measurement Confidence | Priority |
|------|----------|--------------|------------------------|----------------------|---------|
| 1 | [Highest leverage variable] | [X] | +[Y]% | [High/Med/Low] | P1 |
| 2 | [Second leverage variable] | [X] | +[Y]% | [High/Med/Low] | P1 |
| 3 | [Third leverage variable] | [X] | +[Y]% | [High/Med/Low] | P2 |

## Recommendations

[Prioritized actions based on leverage point analysis.
GUIDANCE: Each recommendation must be specific (name the variable and experiment), actionable (own it with a person/team), and sequenced (P1 = do now, P2 = do next quarter, P3 = monitor).

- P1: [Specific experiment targeting leverage point #1] — Owner: [team/person] — Expected impact: [X]% MAU lift — Timeline: [4–6 weeks]
- P1: [Specific experiment targeting leverage point #2] — Owner: [team/person] — Expected impact: [Y]% MAU lift — Timeline: [4–6 weeks]
- P2: [Experiment targeting leverage point #3] — Owner: [team/person] — Timeline: [Next quarter]]

## Appendices

### A. Methodology

[Data sources used, analysis window, confidence level per assumption, and link to supporting spreadsheet model.]

### B. Data Gaps and Placeholder Assumptions

[List each assumption that was estimated rather than measured, the confidence level, and the validation plan.]
