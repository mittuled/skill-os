---
name: instrumentation-verifier-prod-data
description: >
  This skill verifies instrumentation fires correctly in the production environment. Use when asked to validate live tracking, audit production event data, or confirm events are flowing to the data warehouse. Also consider after a production deploy that includes tracking changes. Suggest when dashboards show unexpected data gaps or volume drops.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: simple
related-skills:
  - instrumentation-verifier-data
  - instrumentation-implementer-data
  - alerting-configurator-data
triggers:
  - "verify production data tracking"
  - "production instrumentation QA"
  - "validate live analytics data"
  - "prod event verification data"
  - "QA tracking production data"
---

# instrumentation-verifier-prod-data

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The production instrumentation verifier confirms that tracking events are firing correctly in the live environment by auditing event volumes, sampling payloads, checking data warehouse ingestion, and detecting regressions introduced by production deploys.

## When to Use

- When a production deploy includes new or modified tracking code and post-deploy verification is required.
- When dashboard metrics show unexpected drops or gaps suggesting instrumentation failure.
- When a staging-verified implementation goes live and needs production confirmation.

## Workflow

1. **Baseline event volumes**: Pull hourly event counts for each tracked event over the prior 7 days to establish expected volume ranges.
2. **Post-deploy volume check**: Compare post-deploy event volumes against the baseline. Flag events with volume deviations exceeding 20% that cannot be explained by traffic fluctuation.
3. **Sample payload inspection**: Query 50-100 recent event payloads from the data warehouse. Verify property completeness, type correctness, and value distribution against the spec.
4. **End-to-end pipeline check**: Confirm events flow from the client/server through the event pipeline to the data warehouse within the expected latency window.
5. **Produce verification report**: Document pass/fail per event with volume trends, sample payload analysis, and pipeline health status.

## Anti-Patterns

- **Skipping production verification**: Assuming staging verification is sufficient ignores production-specific factors (ad blockers, CDN caching, feature flags, traffic volume). *Why*: 10-30% of client-side events may be blocked in production by browser extensions that do not exist in staging.
- **Checking only volume, not payload**: Confirming that events fire without inspecting property values misses silent data corruption. *Why*: an event with all null properties still generates volume but produces unusable data.

## Output

**Success:**
- A production verification report confirming event volumes are within expected ranges, sampled payloads match the spec, and the pipeline is ingesting within latency SLAs.

**Failure:**
- Events are missing, malformed, or delayed in production. Report the affected events, observed vs. expected volumes, sample corrupted payloads, and escalation to engineering for hotfix.

## Related Skills

- [`instrumentation-verifier-data`](../instrumentation-verifier-data/SKILL.md) -- the staging verification that precedes this skill.
- [`instrumentation-implementer-data`](../instrumentation-implementer-data/SKILL.md) -- the implementer is the escalation target for production instrumentation failures.
- [`alerting-configurator-data`](../../../data-growth/analytics-lead/alerting-configurator-data/SKILL.md) -- production event volume alerts are a first line of defence that this skill supplements with manual verification.
