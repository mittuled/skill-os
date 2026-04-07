# Activation Moment Validation Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Product | [Product / Feature area] |
| Analysis Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Current Activation Definition | [event_name, threshold, time window] |
| Verdict | [VALIDATED / INVALIDATED / INCONCLUSIVE] |
| Skill | activation-moment-validator |

## Executive Summary

[2-3 sentences: current activation definition, whether it shows statistically significant retention lift, and the recommended action.

GUIDANCE: Example: "The current activation moment — completing first project within 48 hours of signup — shows a 28 percentage point D30 retention lift (activated: 62%, non-activated: 34%, p<0.001). Survival curves are statistically separated. The activation definition is VALIDATED and should be retained as the north star for onboarding optimization."]

## Current Activation Definition

| Parameter | Value |
|-----------|-------|
| Activation Event | [event_name] |
| Threshold | [e.g., 1 occurrence / 3+ occurrences] |
| Time Window | [e.g., within 48 hours of signup / within 7 days] |
| Cohort Size (activated) | [N users] |
| Cohort Size (non-activated) | [N users] |
| Statistical Validity | [Valid — N ≥ 500 per group / Insufficient — see note] |

## Retention Cohort Analysis

| Retention Milestone | Activated Cohort | Non-Activated Cohort | Retention Lift | Significance |
|--------------------|-----------------|---------------------|----------------|--------------|
| Day 7 | [X%] | [X%] | [+X pp] | [p=0.XXX] |
| Day 30 | [X%] | [X%] | [+X pp] | [p=0.XXX] |
| Day 90 | [X%] | [X%] | [+X pp] | [p=0.XXX] |

Minimum meaningful lift threshold: **10 percentage points at D30** (below this, the signal has weak predictive power).

## Survival Analysis

[Kaplan-Meier survival curves for activated vs. non-activated cohorts.]

| Test | Result |
|------|--------|
| Log-rank test statistic | [χ²=X.XX] |
| p-value | [p=0.XXX] |
| Significant separation (p < 0.05)? | [Yes / No] |

**Curve interpretation**: [1 sentence. Example: "Survival curves diverge sharply at Day 3, suggesting early activation is the critical determinant of long-term retention."]

## Alternative Signal Testing

[Tested only if current signal shows weak predictive power (D30 lift < 10 pp). Rank by D30 retention lift.]

| Rank | Candidate Action | Event | Threshold | Time Window | D30 Lift | p-value | Recommendation |
|------|-----------------|-------|-----------|-------------|----------|---------|---------------|
| 1 | [e.g., Invited a team member] | [event_name] | [1+] | [7 days] | [+X pp] | [p=0.XXX] | [New activation moment] |
| 2 | [e.g., Completed 3+ tasks] | [event_name] | [3+] | [14 days] | [+X pp] | [p=0.XXX] | [Secondary candidate] |
| 3 | [e.g., Integrated external tool] | [event_name] | [1+] | [7 days] | [+X pp] | [p=0.XXX] | [Explore] |

## Causal Interpretation Note

[Address the correlation vs. causation question.]

Activated users may have higher retention because: [a) The activation event delivers genuine value that causes retention, b) High-intent users both activate and retain due to inherent motivation, c) Both.]

Evidence for causation: [List supporting evidence — e.g., "Activation experiments that increased activation rate also increased D30 retention, supporting a causal relationship."]

Evidence against causation: [List — e.g., "The effect is concentrated in users who also completed onboarding, suggesting onboarding may be the causal driver."]

## Verdict and Recommendation

**Verdict**: [VALIDATED / INVALIDATED / INCONCLUSIVE]

| Criterion | Met? |
|-----------|------|
| Cohort size ≥ 500 per group | [Yes / No] |
| D30 retention lift ≥ 10 pp | [Yes / No — actual: X pp] |
| Survival curve separation significant (p < 0.05) | [Yes / No — actual: p=0.XXX] |

**Recommendation**: 
- If VALIDATED: Retain current activation definition. Prioritize onboarding experiments that drive users to [activation event] within [time window].
- If INVALIDATED: Replace activation definition with [candidate rank 1 from alternative testing]. Update the growth model's activation rate assumption.
- If INCONCLUSIVE: Extend the analysis to a larger cohort and re-run in [N weeks].

## Methodology Notes

- Cohorts are defined at signup date to avoid survivorship bias.
- Users who were not exposed to the activation opportunity (e.g., feature behind a paywall they didn't see) are excluded from the non-activated cohort.
- Analysis excludes the first [N days] of a cohort to allow sufficient retention observation window.
