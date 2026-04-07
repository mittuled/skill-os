# Checklist: Progressive Rollout Executor

Pre-execution, per-stage, and post-completion checks for canary, blue-green, and percentage-based rollouts.

## Pre-Rollout Checklist

Complete all items before initiating traffic shift. Block the rollout if any P0 item is unchecked.

### Rollback Readiness (P0)

- [ ] Rollback procedure document exists and has been reviewed in the last 7 days
- [ ] Rollback has been rehearsed in staging within the last 30 days (required for complex rollbacks)
- [ ] Rollback trigger thresholds are defined: error rate > [X]%, p99 latency > [X]ms, business metric drop > [X]%
- [ ] Rollback authority is assigned: [on-call engineer / incident commander] has permission to execute
- [ ] Data rollback plan exists if the deployment includes schema changes or data migrations

### Monitoring Readiness (P0)

- [ ] Error rate dashboard is live and showing a stable baseline (last 30 minutes)
- [ ] p95 and p99 latency dashboards are showing a stable baseline
- [ ] SLO burn rate indicator is visible
- [ ] Business metric dashboard is live (conversion rate, order volume, or equivalent)
- [ ] All alert rules are active (not silenced from a previous maintenance window)

### Deployment Configuration (P0)

- [ ] Rollout stages defined: canary %, intermediate stages %, bake times per stage
- [ ] Success criteria defined for each stage (numeric thresholds, not subjective)
- [ ] Rollout configuration reviewed by a second engineer

### Communications (P1)

- [ ] Stakeholders notified of deployment window
- [ ] On-call engineer aware and monitoring during canary phase
- [ ] Incident channel monitored for the duration of the rollout

---

## Canary Stage Gate (1–5% Traffic)

Verify before advancing from canary to first expansion stage. Wait the full configured bake time before evaluating.

- [ ] **Bake time elapsed**: [configured duration] has passed since canary deployment
- [ ] Error rate: canary error rate ≤ baseline error rate + [configured delta, e.g., 0.1%]
- [ ] p99 latency: canary p99 ≤ baseline p99 × [configured multiplier, e.g., 1.1]
- [ ] p95 latency: canary p95 ≤ baseline p95 × [configured multiplier, e.g., 1.1]
- [ ] CPU utilization: canary instances ≤ [threshold, e.g., 80%] CPU
- [ ] Memory utilization: canary instances ≤ [threshold, e.g., 85%] memory
- [ ] Business metric: [conversion/order/API success rate] within [configured range] of baseline
- [ ] No anomalies in logs: no new error types or unexpected log patterns in canary pods
- [ ] No open incidents triggered by canary: check incident management tool

**Decision**: If all checked → advance to next stage. If any unchecked → pause and assess.

---

## Intermediate Stage Gates (10%, 25%, 50%)

Repeat this gate at each configured intermediate stage.

- [ ] Bake time elapsed: [configured duration] at this stage
- [ ] Error rate within threshold: ≤ baseline + [delta]%
- [ ] Latency within threshold: p99 ≤ baseline × [multiplier]
- [ ] No resource saturation: CPU ≤ [%], memory ≤ [%], connection pool ≤ [%]
- [ ] Business metric within acceptable range
- [ ] No new alert firings attributed to this deployment

---

## Full Traffic Stage (100%)

Additional checks when shifting to 100% traffic.

- [ ] All intermediate stage gates passed without anomalies
- [ ] Final bake time elapsed at 100% traffic
- [ ] Old version health checks confirm it can serve as rollback target
- [ ] Error rate stable across 15 minutes at full traffic
- [ ] SLO burn rate normal or improving

---

## Post-Completion Checklist

Complete within 24 hours of successful rollout.

- [ ] Deployment record updated with start time, end time, stage metrics, and completion status
- [ ] Old version resources decommissioned (pods terminated, old AMI unregistered, old containers removed)
- [ ] Feature flags updated if rollout was gated by flags
- [ ] Rollout completion report sent to stakeholders
- [ ] Any anomalies during rollout documented in the post-rollout notes (even if resolved)
- [ ] Runbooks updated if the rollout revealed any gaps in operational documentation

---

## Anomaly Response Protocol

If metrics degrade at any stage, follow this protocol:

| Step | Action | Time Limit |
|------|--------|-----------|
| 1 | Pause rollout — stop advancing traffic | Immediately |
| 2 | Assess causality: is the degradation correlated with this deployment? | 5 minutes |
| 3 | If correlated: execute rollback procedure | Begin within 5 minutes |
| 4 | If ambiguous: extend observation for one additional bake period | Max 15 minutes |
| 5 | If degradation worsens: execute rollback regardless of certainty | Immediately |
| 6 | Document the assessment in the incident log | Within 30 minutes |

**Rollback is always the safe choice when in doubt.** The cost of a rollback is always less than the cost of a production incident.
