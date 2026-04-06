# Activation Signal Definition

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | activation-signal-definer |
| Product | [Product or surface name] |
| Analysis Window | [Date range of retention data used] |

## Executive Summary

[2-3 sentences identifying the activation signal, its retention lift, and the time window. Lead with the final signal definition.
GUIDANCE: Example — "The activation signal for [Product] is defined as 'user creates ≥1 dashboard within 7 days of signup.' Users who complete this action show 42% Day-30 retention vs. 8% for those who do not — a 34 pp retention lift — at an activation rate of 31% of new signups."]

## Candidate Signal Analysis

[Document all candidates tested with their retention lift and activation rate.
GUIDANCE:
- Good: Table with 5–10 specific, instrumentable behaviours, each showing retention_if_done, retention_if_not, retention_lift, and activation_rate.
- Bad: "We looked at several user actions and this one seemed most important."
- Format: Table as shown below]

| # | Candidate Behaviour | Event Name | Threshold | Window (days) | Retention if Done | Retention if Not | Lift (pp) | Activation Rate | Rank |
|---|-------------------|-----------|-----------|--------------|------------------|-----------------|-----------|----------------|------|
| 1 | [e.g., Created dashboard] | [e.g., dashboard_created] | [e.g., 1] | [e.g., 7] | [e.g., 42%] | [e.g., 8%] | [e.g., 34] | [e.g., 31%] | [1st] |
| 2 | [Candidate 2] | | | | | | | | |
| ... | | | | | | | | | |

**Winner**: [Candidate with highest lift above 10 pp minimum threshold]

## Threshold and Window Optimization

[Show the grid analysis for the winning candidate across threshold and window combinations.
GUIDANCE:
- Good: "We tested 1–3 completions × 1, 3, 7, 14-day windows. The 1-completion / 7-day combination maximizes lift at 34 pp while maintaining a 31% activation rate."
- Bad: "7 days seemed like a reasonable window."
- Format: Grid table or heatmap description]

| Threshold | Window: 1 day | Window: 3 days | Window: 7 days | Window: 14 days |
|-----------|-------------|---------------|---------------|----------------|
| 1x | [Lift pp / Act%] | [Lift pp / Act%] | [Lift pp / Act%] | [Lift pp / Act%] |
| 2x | [Lift pp / Act%] | [Lift pp / Act%] | [Lift pp / Act%] | [Lift pp / Act%] |
| 3x | [Lift pp / Act%] | [Lift pp / Act%] | [Lift pp / Act%] | [Lift pp / Act%] |

**Selected combination**: Threshold [N] × Window [N days] — Reason: [highest lift at activation rate ≥ 20%]

## Activation Signal Definition

**Canonical Definition**:

> A user is **activated** when they **[event_name]** **[threshold]** time(s) within **[window]** days of signup.

| Field | Value |
|-------|-------|
| Event name (analytics) | [exact event name as tracked] |
| Threshold | [N completions] |
| Time window | [N days from signup] |
| Day-30 retention (activated) | [%] |
| Day-30 retention (not activated) | [%] |
| Retention lift | [pp] |
| Current activation rate | [%] |
| Activation rate benchmark (category) | [e.g., ≥40% for consumer, ≥25% for SaaS] |
| Benchmark status | [Above / Below / At target] |

## Discriminative Power Validation

| Check | Threshold | Result | Pass/Fail |
|-------|-----------|--------|-----------|
| Retention lift | ≥10 pp | [N pp] | [Pass/Fail] |
| Activation rate | 20–80% | [N%] | [Pass/Fail] |
| Leading indicator (occurs in first 14 days) | Yes | [Median days to activation: N] | [Pass/Fail] |

## Distribution and Publication

[Document where the signal definition has been shared and who has formally accepted it.
GUIDANCE: The signal is only complete when it is accepted by all teams that will use it as a metric target.]

| Team | Recipient | Accepted? | Date |
|------|-----------|-----------|------|
| Growth | [Name] | [Yes/No/Pending] | |
| Product | [Name] | [Yes/No/Pending] | |
| Engineering | [Name] | [Yes/No/Pending] | |

## Recommendations

[Prioritized recommendations for improving the activation rate toward the benchmark target.
GUIDANCE: Each recommendation should be a specific onboarding or product change.
- P1: Changes to the critical path to activation (remove blockers)
- P2: Onboarding improvements to accelerate time-to-activation
- P3: Notification/drip enhancements to recover at-risk users]

| Priority | Recommendation | Expected Impact | Owner |
|----------|---------------|----------------|-------|
| P1 | [e.g., Remove mandatory email verification before dashboard access] | [e.g., +5 pp activation rate] | [Product] |

## Appendices

### A. Methodology

[Data source, date range, cohort size, analysis method. Note if survival analysis or logistic regression was used instead of simple rate comparison.]

### B. Supporting Data

[Raw retention curves, cohort sizes per candidate, and statistical significance test results (chi-squared or Fisher's exact test for each candidate's retention lift).]
