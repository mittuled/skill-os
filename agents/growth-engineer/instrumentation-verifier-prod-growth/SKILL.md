---
name: instrumentation-verifier-prod-growth
description: >
  This skill verifies growth instrumentation fires correctly in production. Use when asked to audit live growth tracking, validate production experiment data, or confirm growth events are flowing to the warehouse. Also consider after a production deploy that includes growth tracking changes. Suggest when growth dashboards show unexpected data gaps.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: simple
related-skills:
  - instrumentation-verifier-growth
  - instrumentation-implementer-growth
  - metrics-dashboard-growth
---

# instrumentation-verifier-prod-growth

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The production growth instrumentation verifier confirms that growth tracking events fire correctly in the live environment by auditing event volumes, sampling payloads, verifying experiment assignment distribution, and checking data warehouse ingestion for growth-specific events.

## When to Use

- When a production deploy includes new or modified growth tracking and needs post-deploy verification.
- When growth dashboard metrics show unexpected drops suggesting instrumentation failure.
- When a new experiment goes live and the team needs to confirm variant assignment events are flowing.

## Workflow

1. **Baseline event volumes**: Pull hourly event counts for growth events over the prior 7 days to establish expected volume ranges.
2. **Post-deploy volume check**: Compare post-deploy volumes to baselines. Flag deviations exceeding 20%.
3. **Sample payload inspection**: Query 50-100 recent growth event payloads. Verify property completeness, UTM attribution, and experiment_id/variant_id correctness.
4. **Verify experiment distribution**: For active experiments, check that variant assignment ratios match the configured allocation (e.g., 50/50 split). Flag sample ratio mismatch using chi-squared test.
5. **Produce verification report**: Document pass/fail per event with volume trends, payload samples, and experiment distribution analysis.

## Anti-Patterns

- **No experiment distribution check**: Verifying event volume without checking variant assignment distribution misses SRM (sample ratio mismatch) that invalidates experiment results. *Why*: an experiment with a 60/40 split instead of 50/50 produces biased effect estimates.
- **Verifying only new events**: Checking new events without re-verifying existing events that may be affected by the deploy misses regressions. *Why*: code changes can break existing tracking as a side effect.

## Output

**Success:**
- A production verification report confirming growth event volumes are within expected ranges, payloads match the spec, and experiment variant distributions are balanced.

**Failure:**
- Growth events are missing, malformed, or show SRM in production. Report the affected events, observed issues, and escalation path for hotfix.

## Related Skills

- [`instrumentation-verifier-growth`](../instrumentation-verifier-growth/SKILL.md) -- the staging verification that precedes this skill.
- [`instrumentation-implementer-growth`](../instrumentation-implementer-growth/SKILL.md) -- the implementer is the escalation target for production issues.
- [`metrics-dashboard-growth`](../metrics-dashboard-growth/SKILL.md) -- the growth dashboard is the first place data gaps become visible.
