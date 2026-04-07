# Production Growth Instrumentation Verification Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Verifier | [Growth Engineer name] |
| Deploy Reference | [Deploy ID / Release tag] |
| Feature / Experiment | [Name] |
| Deploy Time | [YYYY-MM-DD HH:MM UTC] |
| Verification Window | [e.g., 4 hours post-deploy] |
| Overall Result | [PASS / FAIL / PARTIAL] |
| Skill | instrumentation-verifier-prod-growth |

## Summary

| Category | Total Verified | Pass | Fail |
|----------|---------------|------|------|
| Growth funnel events | [N] | [N] | [N] |
| Experiment events | [N] | [N] | [N] |
| Loop events | [N] | [N] | [N] |
| Experiment distribution (SRM check) | [N experiments] | [N] | [N] |

## Event Volume Check

| Event | 7d Avg Hourly | Post-Deploy Hourly | Deviation | Status |
|-------|--------------|-------------------|-----------|--------|
| [signup_completed] | [N] | [N] | [+X% / -X%] | [PASS / FAIL] |
| [activation_event] | [N] | [N] | [+X% / -X%] | [PASS / FAIL] |
| [experiment_assigned] | [N] | [N] | [+X% / -X%] | [PASS / FAIL] |
| [referral_link_shared] | [N] | [N] | [+X% / -X%] | [PASS / FAIL] |

Volume deviation threshold: >20% triggers investigation. Consider traffic growth, new feature launch, or time-of-day effects before escalating.

## Payload Sample Analysis

### [signup_completed] — [N events sampled]

| Property | Null Rate | Distribution Notes | Status |
|----------|-----------|-------------------|--------|
| user_id | [X%] | [99.9% populated] | [PASS] |
| utm_source | [X%] | [google: 45%, direct: 30%, referral: 15%, other: 10%] | [PASS] |
| utm_medium | [X%] | [cpc: 40%, organic: 35%, referral: 10%] | [PASS] |
| utm_content | [X%] | [X% null — anomaly if recently added] | [PASS / FAIL] |
| plan | [X%] | [free: 85%, trial: 15%] | [PASS] |

### [experiment_assigned] — [N events sampled]

| Property | Null Rate | Notes | Status |
|----------|-----------|-------|--------|
| experiment_id | [0%] | [All events show valid experiment IDs] | [PASS] |
| variant_id | [0%] | [Values: control, variant_a — no unexpected values] | [PASS] |
| user_id | [X%] | [X% anonymous — expected for pre-login experiments] | [PASS] |

## Experiment Distribution Check (SRM Analysis)

[For each active experiment, verify the variant assignment ratio matches configuration.]

### Experiment: [Experiment Name / ID]

| Variant | Configured % | Actual % (N=[total]) | Chi-Squared | p-value | SRM Detected? |
|---------|-------------|---------------------|------------|---------|--------------|
| control | 50% | [X%] ([N users]) | [χ²=X.XX] | [p=0.XXX] | [No / YES — investigate] |
| variant_a | 50% | [X%] ([N users]) | — | — | — |

SRM threshold: p < 0.01 is a strong signal of systematic assignment bias. **If SRM detected, pause the experiment and investigate.**

## Pipeline Health

| Stage | Status | p50 Latency | p99 Latency |
|-------|--------|------------|------------|
| Client → CDP | [Healthy] | [N ms] | [N ms] |
| CDP → Warehouse | [Healthy] | [N min] | [N min] |
| Warehouse → Growth Dashboard refresh | [Healthy] | [N min] | [N min] |

## Failure Details

[Complete only if failures detected.]

### Failure #1: [Short description]

**Type**: [Volume anomaly / Payload corruption / SRM / Pipeline delay]
**Event(s)**: [event_name]
**Severity**: [Critical / High / Medium]
**Observed**: [Describe]
**Expected**: [Describe]
**Impact**: [Which dashboard metrics or experiments are affected]
**Escalation**: [Growth Lead / Engineering / CDP Support]
**Recommended action**: [Hotfix within 4h / Monitor 24h / Investigate root cause]

## Recommendation

**Verdict**: [VERIFIED / PARTIAL — follow-up required / ESCALATE — critical issue]

[1-2 sentences. Example: "All growth funnel events pass volume and payload checks. No SRM detected in Experiment 23. Pipeline latency is within SLA. Growth dashboard is displaying correct values as of 2h post-deploy. Monitoring active for 48 hours."]

**Next check**: [Standard 24h monitoring / Re-verify after hotfix deploy / Escalated to Engineering]
