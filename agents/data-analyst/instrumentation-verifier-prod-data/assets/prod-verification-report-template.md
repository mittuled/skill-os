# Production Instrumentation Verification Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Verifier | [Data Analyst name] |
| Deploy Reference | [Deploy ID / PR / Release tag] |
| Feature / Surface | [Feature name] |
| Deploy Time | [YYYY-MM-DD HH:MM UTC] |
| Verification Window | [e.g., 2 hours post-deploy] |
| Overall Result | [PASS / FAIL / PARTIAL] |
| Skill | instrumentation-verifier-prod-data |

## Summary

| Category | Count |
|----------|-------|
| Events verified | [N] |
| Events passing volume check | [N] |
| Events failing volume check | [N] |
| Events passing payload check | [N] |
| Events failing payload check | [N] |
| Pipeline latency: within SLA | [Yes / No] |

## Event Volume Check

[Compare post-deploy hourly event counts against 7-day baseline. Flag deviations >20%.]

| Event Name | Platform | 7d Avg Hourly Volume | Post-Deploy Hourly Volume | Deviation % | Status |
|-----------|----------|---------------------|--------------------------|-------------|--------|
| [event_name] | Web | [N] | [N] | [+X% / -X%] | [PASS / FAIL] |
| [event_name] | iOS | [N] | [N] | [+X% / -X%] | [PASS / FAIL] |
| [event_name] | Server | [N] | [N] | [+X% / -X%] | [PASS / FAIL] |

**Notes on volume anomalies**: [Explain any deviations — traffic spike, ad blocker prevalence, deployment lag, new feature driving genuine volume increase.]

## Payload Sample Analysis

[Sample 50-100 recent events from the data warehouse per event type. Report property completeness and value distribution.]

### [event_name]

Sample size: [N events] from [YYYY-MM-DD HH:MM] to [YYYY-MM-DD HH:MM UTC]

| Property | Expected Type | Null Rate | Value Distribution | Status |
|----------|--------------|-----------|-------------------|--------|
| prop1 | string | [X%] | [top values: "a" (55%), "b" (30%), "c" (15%)] | [PASS / FAIL] |
| prop2 | integer | [X%] | [min: N, max: N, median: N] | [PASS / FAIL] |
| user_id | string | [X%] | [99.9% populated — 0.1% anonymous sessions] | [PASS / FAIL] |

**Spec alignment**: [All properties present and correctly typed / Failures: list deviations]

### [event_name]

Sample size: [N events]

| Property | Expected Type | Null Rate | Value Distribution | Status |
|----------|--------------|-----------|-------------------|--------|
| prop1 | string | [X%] | [values] | [PASS / FAIL] |

## End-to-End Pipeline Health

| Stage | Status | Latency (p50) | Latency (p99) | Notes |
|-------|--------|--------------|--------------|-------|
| Client → CDP ingestion | [Healthy / Degraded] | [N ms] | [N ms] | — |
| CDP → Warehouse load | [Healthy / Degraded] | [N min] | [N min] | — |
| Warehouse → Dashboard refresh | [Healthy / Degraded] | [N min] | [N min] | — |

Pipeline SLA: Events visible in data warehouse within [15 / 30 / 60] minutes of firing.

## Failure Details

[Complete only if failures were identified above.]

### Failure #1: [Short description]

**Event**: [event_name]
**Type**: [Volume anomaly / Payload corruption / Pipeline delay]
**Observed**: [describe what was observed]
**Expected**: [describe what was expected per spec or baseline]
**Impact**: [Affected metrics or dashboards]
**Severity**: [Critical / High / Medium]
**Escalation**: [Engineer team / CDP support / Analytics Lead]
**Action**: [Immediate hotfix / Monitor 24h / Investigate root cause]

## Recommendation

**Verdict**: [VERIFIED — all events healthy in production / PARTIAL — N events require follow-up / ESCALATE — critical failure, hotfix required]

[1-2 sentences. Example: "All 12 events pass volume and payload checks. Pipeline latency is within SLA. No action required — monitoring alerts are active for the next 48 hours."]

**Follow-up monitoring**: Set volume deviation alert for [N days] post-deploy. Reference alert configuration at `alerting-configurator-data`.
