# Rollout Configuration

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | rollout-configurator |
| Service | [Service name] |
| Deployment | [Feature/version description] |

## Executive Summary

[2-3 sentences summarizing the deployment risk level, selected strategy, and key success criteria.
GUIDANCE: Lead with the risk classification outcome — "This deployment modifies the payment processing flow affecting all users, classified as High Risk (11/12). A five-stage canary starting at 1% with 30-minute bake times and manual promotion gates at 25% and beyond is required."]

## Risk Assessment

[Apply the risk classification matrix from `references/framework.md`.

GUIDANCE:
- Good: "Services affected: 2 (payments-api, notifications-service) = 2 pts. User blast radius: 100% of users = 3 pts. Reversibility: code-only rollback = 1 pt. Change size: 312 lines = 2 pts. Total: 8 pts = Medium Risk."
- Bad: "This is a medium-risk deployment."]

| Factor | Assessment | Score |
|--------|-----------|-------|
| Services affected | [description] | [1/2/3] |
| User blast radius | [description] | [1/2/3] |
| Reversibility | [description] | [1/2/3] |
| Change size | [description] | [1/2/3] |
| **Total** | | **[4–12]** |

**Risk Level**: [Low / Medium / High]

## Rollout Stage Configuration

[Define each rollout stage with traffic percentage, bake time, success criteria, and promotion type.

GUIDANCE:
- Good: "Stage 1: 1% canary, 30-minute bake, automated promotion if: error rate ≤ 0.11% AND p99 latency ≤ 220ms AND checkout success rate ≥ 99%"
- Bad: "Start at 1% and increase gradually"]

| Stage | Traffic % | Bake Time | Promotion Type | Success Criteria |
|-------|-----------|-----------|----------------|-----------------|
| 1 | [1/5/10]% | [X min] | [Automated/Manual] | [Specific metric thresholds] |
| 2 | [%] | [X min] | [Automated/Manual] | [Specific metric thresholds] |
| ... | | | | |
| Final | 100% | [X min] | Automated | All metrics within SLO |

## Baseline Metrics

[Document the 30-day baseline for each metric used in success criteria.

GUIDANCE: Never skip this section. Thresholds without baselines are guesses.]

| Metric | 30-Day Baseline | Success Threshold | Rollback Threshold |
|--------|----------------|-------------------|--------------------|
| HTTP error rate | [X.X%] | ≤ [baseline + 0.1%] | > [baseline + 0.5%] |
| p99 latency | [Xms] | ≤ [baseline × 1.1] | > [baseline × 1.5] |
| [Business metric] | [value] | ≥ [baseline × 0.99] | < [baseline × 0.95] |

## Monitoring Configuration

[Specify the monitoring queries and dashboard used during this rollout.

GUIDANCE:
- Good: "Argo Rollouts analysis template: polls Prometheus every 60s querying `rate(http_requests_total{status=~"5..",service="payments"}[5m]) / rate(http_requests_total{service="payments"}[5m])`, fails if result > 0.0011"
- Bad: "Monitor error rates in Grafana"]

## Recommendations

[Actions to take before, during, and after this rollout.

GUIDANCE:
- P1: [Any prerequisite that must be completed before the rollout starts]
- P2: [Any monitoring gap that should be closed before this specific deployment]
- P3: [Post-rollout cleanup — flag cleanup, config consolidation]]

## Appendices

### A. Rollback Procedure

[Specific commands to halt and revert this deployment: e.g., `kubectl argo rollouts abort <name>` or `aws codedeploy stop-deployment --deployment-id <id>`]

### B. Configuration File

[The actual rollout controller configuration (Argo Rollouts YAML, Flagger Canary manifest, etc.) that deploys these settings]
