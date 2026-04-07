# Feature Adoption Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Analyst name] |
| Feature | [Feature name] |
| Report Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Cohort Scope | [All users / New users since launch / Specific segment] |
| Skill | adoption-tracker-data |

## Executive Summary

[2-3 sentences covering the feature's adoption rate against target, the primary bottleneck in the discovery-to-adoption funnel, and the top recommendation.

GUIDANCE: Example: "Feature X has reached 34% adoption among users who signed up in the past 30 days, against a 50% target. The primary bottleneck is at the trial stage (45% discovery → 22% trial), suggesting a UI placement or awareness issue rather than a feature quality problem. Recommended action is a targeted in-app prompt for users in the discovery state."]

## Adoption Definition

| Parameter | Value |
|-----------|-------|
| Feature | [Feature name] |
| Defining Event | [event_name] |
| Adoption Threshold | [e.g., 3+ uses within 14 days of first use] |
| Time Window | [14 / 30 / 90 days from first exposure or signup] |
| Discovery Event | [event_name — e.g., feature_seen, tooltip_viewed] |
| Trial Event | [event_name — e.g., feature_clicked, feature_started] |

## Adoption Funnel

| Stage | Users | Rate vs. Prior Stage | Benchmark |
|-------|-------|---------------------|-----------|
| Total eligible users | [N] | — | — |
| Discovery (saw feature) | [N] | [X%] | [industry/internal benchmark] |
| Trial (used once) | [N] | [X%] of discoverers | [benchmark] |
| Adoption (met threshold) | [N] | [X%] of triers | [benchmark] |
| Sustained use (30d+ post-adoption) | [N] | [X%] of adopters | [benchmark] |

**Primary Bottleneck**: [Discovery → Trial / Trial → Adoption / Adoption → Sustained] — [gap description]

## Cohort Adoption Curves

[Description of cohort curve data. Embed charts or link to dashboard.]

| Cohort | Cohort Size | D7 Adoption | D14 Adoption | D30 Adoption | Terminal Adoption Rate |
|--------|------------|-------------|-------------|-------------|----------------------|
| [Month 1 signups] | [N] | [X%] | [X%] | [X%] | [X%] |
| [Month 2 signups] | [N] | [X%] | [X%] | [X%] | [X%] |
| [Month 3 signups] | [N] | [X%] | [X%] | [X%] | [X%] |
| [Plan: Free] | [N] | [X%] | [X%] | [X%] | [X%] |
| [Plan: Pro] | [N] | [X%] | [X%] | [X%] | [X%] |

**Key Observation**: [Note the most significant cohort variation — e.g., "Pro-tier users adopt 2.4x faster than free users."]

## Time-to-Adoption Distribution

| Metric | Value |
|--------|-------|
| Median time to first use | [N days] |
| Median time to adoption (threshold met) | [N days] |
| 75th percentile time to adoption | [N days] |
| % of adopters who adopt within 7 days | [X%] |
| % of adopters who adopt within 30 days | [X%] |

## Retention Correlation

[Analysis of whether feature adoption predicts long-term retention.]

| Segment | D30 Retention (Adopters) | D30 Retention (Non-Adopters) | Lift |
|---------|------------------------|------------------------------|------|
| All users | [X%] | [X%] | [+X pp] |
| Free users | [X%] | [X%] | [+X pp] |
| Pro users | [X%] | [X%] | [+X pp] |

Correlation significance: [Statistically significant at p=[value] / Not significant — n=[sample size]]

**Interpretation**: [1-2 sentences on whether this feature is predictive of retention and what it implies for activation strategy.]

## Segmentation Analysis

| Segment Dimension | High-Adoption Segment | Low-Adoption Segment | Gap |
|-------------------|----------------------|---------------------|-----|
| Plan tier | [segment] ([X%]) | [segment] ([X%]) | [X pp] |
| Acquisition channel | [segment] ([X%]) | [segment] ([X%]) | [X pp] |
| Company size / persona | [segment] ([X%]) | [segment] ([X%]) | [X pp] |
| Geographic region | [segment] ([X%]) | [segment] ([X%]) | [X pp] |

## Recommendations

| Priority | Recommendation | Hypothesis | Expected Impact |
|----------|---------------|-----------|----------------|
| P1 | [e.g., Add in-app prompt for users at discovery stage] | [Friction at discovery is the bottleneck] | [+X pp trial rate] |
| P2 | [e.g., Highlight feature in onboarding checklist] | [New users don't know feature exists] | [+X pp discovery rate] |
| P3 | [e.g., Run an experiment with guided walkthrough] | [Trial-to-adoption drop-off is product quality] | [+X pp adoption rate] |

## Instrumentation Notes

[List any gaps or caveats in the underlying data.]

- [e.g., "Discovery event added [date] — cohorts before this date lack discovery data."]
- [e.g., "Android users are not tracked for trial events — Android adoption is estimated."]

## Dashboard Reference

[Link to the live adoption dashboard used as the source for this report.]

Dashboard URL: [link]
Last refreshed: [YYYY-MM-DD HH:MM UTC]
