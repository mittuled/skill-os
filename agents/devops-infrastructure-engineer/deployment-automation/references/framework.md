# Framework: deployment-automation

Defines deployment patterns, health check standards, and gate policies for automated deployment pipelines.

## Deployment Strategy Selection

| Strategy | Best For | Traffic Control | Rollback Speed | Complexity |
|----------|----------|-----------------|----------------|------------|
| Blue-Green | Stateless services, instant cutover required | ALB target group swap or Kubernetes service selector | Instant (swap back) | Medium |
| Canary | High-traffic services, gradual exposure | Istio weight split or AWS weighted target groups (1% → 5% → 25% → 100%) | Fast (canary to 0%) | High |
| Rolling Update | Stateful workloads, no spare capacity | Kubernetes maxSurge/maxUnavailable | Minutes (depends on replica count) | Low |
| Feature Flag | Business logic changes, decoupled from deploy | Application-level, user segment targeting | Instant (toggle) | Low |
| Recreate | Dev environments, downtime acceptable | Full replacement | Redeploy required | Low |

## Pre-Deployment Gate Criteria

All gates must pass before the deployment execution stage begins:

| Gate | Verification Method | Failure Action |
|------|--------------------|--------------  |
| Artifact integrity | SHA-tagged immutable image (never `latest`), digest matches CI output | Block deploy |
| Dependency health | Database connectivity probe, downstream API availability check | Block deploy |
| Environment drift | `terraform plan` diff = zero unexpected changes | Require approval |
| Capacity headroom | Available CPU/memory > 30% headroom on all nodes | Alert + scale first |
| Config parity | Environment variables match approved config manifest | Block deploy |

## Health Check Standards

### Kubernetes Probe Configuration

```
Readiness probe:  GET /healthz → 200 OK (checks DB connectivity, cache reachability)
Liveness probe:   GET /livez → 200 OK (checks process health, detects deadlocks)
Startup probe:    GET /startupz → 200 OK with failureThreshold=30 for slow-starting services

Timing defaults:
  initialDelaySeconds: 10
  periodSeconds: 5
  failureThreshold: 3 (readiness), 6 (liveness)
```

### Non-Kubernetes Health Checks

- HTTP target groups: health check path `/healthz`, healthy threshold 2, unhealthy threshold 3
- TCP listeners: connection check on service port with 10-second timeout

## Post-Deployment Validation Suite

| Check | Tool | Pass Threshold | Bake Window |
|-------|------|----------------|-------------|
| Smoke tests | Critical user journey HTTP assertions | 100% pass | Immediate |
| Error rate comparison | p95 error rate ≤ previous 30-min baseline + 0.1% | Within SLO | 10 minutes |
| Latency comparison | p99 latency ≤ previous 30-min baseline × 1.1 | Within SLO | 10 minutes |
| Throughput baseline | RPS within ±20% of expected | Nominal | 5 minutes |

If any post-deployment check fails within the bake window, trigger automatic rollback immediately.

## Human Gate Policy

| Deployment Type | Gate Required | Approval Channel |
|-----------------|--------------|------------------|
| Database schema migration (backward-incompatible) | Mandatory | Slack approval workflow (DBA + lead engineer) |
| Breaking API version deprecation | Mandatory | Slack approval workflow (API owner + consumers) |
| Production data transformation | Mandatory | Slack approval workflow (data engineering lead) |
| Compliance-sensitive change (auth, encryption) | Mandatory | Slack approval workflow (security engineer) |
| Standard feature deployment | Automated | None (automated gates only) |
| Hotfix to production | Expedited | Slack approval (on-call lead only) |
