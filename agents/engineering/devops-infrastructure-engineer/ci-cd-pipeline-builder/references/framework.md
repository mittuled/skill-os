# Framework: CI/CD Pipeline Design

Reference framework for building reliable CI/CD pipelines with deployment strategies.

## Pipeline Stage Reference

| Stage | Purpose | Quality Gate | Typical Duration |
|-------|---------|-------------|-----------------|
| Source Checkout | Fetch code at commit SHA | N/A | <30s |
| Dependency Install | Install with layer caching | Cache hit rate >80% | 1-3m |
| Lint + SAST | Parallel static analysis | Zero critical/high findings | 1-2m |
| Unit Tests | Fast isolated tests | 100% pass, coverage >= baseline | 1-5m |
| Integration Tests | Service-level tests against ephemeral containers | 100% pass | 3-10m |
| Artifact Build | Immutable image tagged with git SHA | Image scanned, no critical CVEs | 2-5m |
| Deploy Staging | Deploy to staging environment | Smoke tests pass | 2-5m |
| Deploy Production | Deploy via selected strategy | Health checks pass, metrics stable | 5-15m |

## Deployment Strategies

### Blue-Green
- **Use when**: Zero-downtime required, stateless services, quick rollback needed
- **Mechanism**: Deploy to inactive environment, run smoke tests, swap load balancer target group
- **Rollback**: Swap target group back (<30s)

### Canary
- **Use when**: High-traffic services, gradual risk exposure, metric-driven decisions
- **Mechanism**: Route 1-5% traffic to new version, monitor 10-15 min, promote or rollback
- **Rollback**: Scale canary to zero, route 100% to stable

### Rolling
- **Use when**: Stateful workloads, Kubernetes-native, resource-constrained
- **Mechanism**: Replace pods incrementally with readiness probes (maxSurge/maxUnavailable)
- **Rollback**: Kubernetes rollout undo

## DORA Metrics Targets

| Metric | Elite | High | Medium | Low |
|--------|-------|------|--------|-----|
| Deployment Frequency | On-demand (multiple/day) | Weekly-daily | Monthly-weekly | Monthly-biannual |
| Lead Time for Changes | <1 hour | 1 day - 1 week | 1 week - 1 month | 1-6 months |
| Change Failure Rate | 0-5% | 5-10% | 10-15% | >15% |
| Mean Time to Recovery | <1 hour | <1 day | <1 week | >1 week |
