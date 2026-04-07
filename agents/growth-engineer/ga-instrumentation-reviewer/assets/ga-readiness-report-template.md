# GA Instrumentation Readiness Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Product / Feature | [Product or feature name] |
| GA Target Date | [YYYY-MM-DD] |
| Spec Reference | [Link to growth instrumentation spec] |
| Overall Verdict | [GO / NO-GO — N critical events missing] |
| Skill | ga-instrumentation-reviewer |

## Executive Summary

[2-3 sentences: coverage status, any critical gaps, and the go/no-go verdict.

GUIDANCE: Example: "All 18 acquisition and activation events pass verification in staging. The growth dashboard is fully populated. One A/B test infrastructure check is pending — experiment_assigned events have not been verified for the feature flag integration. Recommend conditional GO pending experiment tracking verification by [date]."]

## AARRR Coverage Audit

### Acquisition Events

| Event | Platform | Status | Verified? | Priority | Notes |
|-------|---------|--------|-----------|----------|-------|
| [signup_started] | [Web] | [Live / Missing / In progress] | [Yes / No] | [Critical] | — |
| [signup_completed] | [Web + Server] | [Live / Missing] | [Yes / No] | [Critical] | — |
| [channel_attribution] | [Web] | [Live / Missing] | [Yes / No] | [Critical] | [UTM params captured?] |
| [landing_page_view] | [Web] | [Live / Missing] | [Yes / No] | [High] | — |

### Activation Events

| Event | Platform | Status | Verified? | Priority | Notes |
|-------|---------|--------|-----------|----------|-------|
| [onboarding_step_completed] | [Web + iOS] | [Live / Missing] | [Yes / No] | [Critical] | [All N steps covered?] |
| [activation_event] | [Web + iOS] | [Live / Missing] | [Yes / No] | [Critical] | [Spec definition matches agreed activation moment?] |
| [feature_first_used] | [Web] | [Live / Missing] | [Yes / No] | [High] | — |

### Retention Events

| Event | Platform | Status | Verified? | Priority | Notes |
|-------|---------|--------|-----------|----------|-------|
| [session_started] | [Web + iOS] | [Live / Missing] | [Yes / No] | [High] | — |
| [feature_used] | [Web + iOS] | [Live / Missing] | [Yes / No] | [High] | — |

### Revenue Events

| Event | Platform | Status | Verified? | Priority | Notes |
|-------|---------|--------|-----------|----------|-------|
| [upgrade_initiated] | [Web] | [Live / Missing] | [Yes / No] | [Critical] | — |
| [subscription_created] | [Server] | [Live / Missing] | [Yes / No] | [Critical] | — |
| [payment_completed] | [Server] | [Live / Missing] | [Yes / No] | [Critical] | — |

### Referral Events

| Event | Platform | Status | Verified? | Priority | Notes |
|-------|---------|--------|-----------|----------|-------|
| [referral_link_shared] | [Web] | [Live / Missing] | [Yes / No] | [Medium] | — |
| [referred_signup] | [Web] | [Live / Missing] | [Yes / No] | [Medium] | — |

## Coverage Summary

| Category | Total Events | Live | Missing | Coverage % |
|----------|-------------|------|---------|------------|
| Acquisition | [N] | [N] | [N] | [X%] |
| Activation | [N] | [N] | [N] | [X%] |
| Retention | [N] | [N] | [N] | [X%] |
| Revenue | [N] | [N] | [N] | [X%] |
| Referral | [N] | [N] | [N] | [X%] |
| **Total** | **[N]** | **[N]** | **[N]** | **[X%]** |

**Critical events missing**: [N] (must all be fixed before GO)

## Growth Dashboard Readiness

| Dashboard Section | Metrics Live? | Correct Values? | Notes |
|------------------|--------------|----------------|-------|
| Acquisition (daily signups by channel) | [Yes / No] | [Yes / No] | — |
| Activation rate by cohort | [Yes / No] | [Yes / No] | — |
| Retention curves (D1/D7/D30) | [Yes / No] | [Yes / No] | — |
| Experiment results view | [Yes / No] | [Yes / No] | — |
| Loop throughput metrics | [Yes / No] | [Yes / No] | — |
| Revenue metrics (MRR, CAC, LTV) | [Yes / No] | [Yes / No] | — |

**Dashboard overall**: [Ready / Partially ready — N sections incomplete / Not ready]

## A/B Test Infrastructure

| Check | Status | Notes |
|-------|--------|-------|
| Experiment framework configured | [Yes / No] | [Framework: e.g., LaunchDarkly / GrowthBook] |
| experiment_assigned event fires | [Yes / No] | [Experiment ID and variant ID present?] |
| Goal events linked to experiment | [Yes / No] | [experiment_id on goal events?] |
| Sample ratio check configured | [Yes / No] | — |
| Experiment analytics view live | [Yes / No] | — |

## Critical Gaps

| Gap | Event | Severity | Estimated Fix Time | Owner | Block GA? |
|-----|-------|----------|-------------------|-------|-----------|
| [e.g., subscription_created missing on server] | subscription_created | [Critical] | [2 days] | [Engineer name] | [Yes] |
| [e.g., experiment_assigned not firing for Feature Flag X] | experiment_assigned | [High] | [1 day] | [Engineer name] | [Conditional] |

## Verdict

**GA Verdict**: [GO / CONDITIONAL GO / NO-GO]

Conditions (if CONDITIONAL GO):
1. [Condition 1 must be met by YYYY-MM-DD]
2. [Condition 2]

**Approved by**: [Growth Lead name]
**Date**: [YYYY-MM-DD]
