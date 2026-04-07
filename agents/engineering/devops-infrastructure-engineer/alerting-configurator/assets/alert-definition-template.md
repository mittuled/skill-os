# Alert Definition: [Alert Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Service | [Service name] |
| Alert Name | [Exact name as it appears in monitoring tool] |
| Monitoring Tool | [Datadog / Prometheus / Grafana / CloudWatch] |
| Skill | alerting-configurator |
| Status | [Draft / Active / Deprecated] |

## Alert Purpose

**What condition does this alert detect?**
[One sentence: what goes wrong, on which component, measured by what signal.]

**Why does this condition matter?**
[Business or operational impact: user experience degraded, SLO breached, data at risk, etc.]

**Linked SLO**: [SLO name and target, e.g., "API availability SLO: 99.9% over 30 days"]

## Alert Specification

### Query

```
[Exact alert query in the monitoring tool's language — PromQL, Datadog metric query, CloudWatch Expression, etc.]

Example (Prometheus):
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
```

### Thresholds

| Level | Condition | Action |
|-------|-----------|--------|
| Warning | [Threshold, e.g., error rate > 2% for 5 min] | Notify Slack channel; no page |
| Critical | [Threshold, e.g., error rate > 5% for 2 min] | Page on-call engineer via PagerDuty |
| Auto-resolve | [Condition clears for X min] | Auto-close alert; post resolution to Slack |

**Evaluation window**: [5 min rolling / 1 min instant / 15 min average]
**Evaluation frequency**: [Every 1 min / 30 sec]

### Severity Classification

| Criterion | Value |
|-----------|-------|
| Severity | [P1 / P2 / P3 / P4] |
| User-facing impact | [Yes / No — describe] |
| SLO budget consumed | [Estimated burn rate at this threshold] |
| Action required | [Immediate / Within business hours / Informational] |

## Baseline and Calibration

| Metric | 30-Day Baseline | P50 | P95 | P99 | Alert Threshold |
|--------|----------------|-----|-----|-----|----------------|
| [Metric name] | [value] | [value] | [value] | [value] | [threshold] |

**Threshold rationale**: [Why this specific number — e.g., "5% error rate is 2× the 30-day P99 of 2.4% — chosen to alert before SLO budget is materially consumed while avoiding noise from normal traffic spikes."]

## Runbook Reference

**Runbook link**: [Link to runbook in wiki / runbook-drafter output]
**Expected MTTR**: [X minutes for a trained on-call engineer]

### Quick Triage Steps

1. [First action on receiving this alert — e.g., "Check Datadog dashboard: link"]
2. [Second action — e.g., "Check deployment history: was a deploy in the last 30 min?"]
3. [Third action — e.g., "Check upstream dependency health: link"]
4. [Escalation trigger — e.g., "If not resolved in 15 min, escalate to [Team]"]

## Noise Control

### Known False Positive Scenarios

| Scenario | Distinguishing Signal | Action |
|----------|----------------------|--------|
| [Scenario, e.g., "Scheduled maintenance window"] | [Monitoring tag / suppression window] | [Suppress alert or acknowledge] |
| [Scenario, e.g., "Canary deploy phase — expected elevated error rate"] | [Deploy marker in Datadog event stream] | [Acknowledge during deploy window] |

**Historical false positive rate**: [X% of triggers over last 30 days]
**Suppression rules**: [Maintenance window schedule or deployment suppression config]

### Anti-Noise Measures Applied

- [ ] Multi-window evaluation (avoid single-spike triggers)
- [ ] Minimum sample size before triggering (avoid low-traffic false positives)
- [ ] Anomaly detection vs. static threshold (specify which and why)
- [ ] Flap detection enabled (prevents alert storm during unstable transitions)

## Ownership and Review

| Role | Name / Team |
|------|-------------|
| Alert owner | [Team] |
| On-call rotation | [PagerDuty schedule link] |
| Last reviewed | [YYYY-MM-DD] |
| Next review due | [YYYY-MM-DD or "On next SLO review"] |

## Related Alerts

| Alert Name | Relationship |
|------------|-------------|
| [Alert] | [Correlated — fires together during database degradation] |
| [Alert] | [Upstream — triggers before this alert; check first] |
