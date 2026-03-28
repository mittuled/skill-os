# Scoring Rubric: Production Readiness Review

Evaluates whether a service meets production readiness criteria across reliability, observability, security, performance, and operational domains.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Reliability | 25% | Redundancy, failover, disaster recovery, and graceful degradation under partial failures |
| 2 | Observability | 20% | Structured logging, metrics (RED method), distributed tracing, alerting, and dashboard accuracy |
| 3 | Security | 20% | Secrets management, auth enforcement, TLS, vulnerability scanning, and policy compliance |
| 4 | Performance | 20% | Load test validation, auto-scaling, resource limits, capacity headroom, and SLO definition |
| 5 | Operational Readiness | 15% | Runbooks, on-call rotation, deployment/rollback procedures, and failure injection exercises |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All domains pass with comprehensive evidence; game-day exercises completed | Approve for production; schedule quarterly re-review |
| A | 8.0 – 8.9 | Strong | All domains pass; minor documentation gaps or incomplete tracing coverage | Approve with follow-up items tracked in backlog |
| B | 7.0 – 7.9 | Good | Most domains pass; one domain has conditional pass requiring remediation | Approve conditionally; remediate within 2 sprints |
| C | 5.0 – 6.9 | Adequate | Multiple domains have gaps; no critical blockers but significant risk | Delay launch; create remediation plan with deadlines |
| D | 3.0 – 4.9 | Weak | Critical gaps in reliability or security; service is not safe for production | Block launch; escalate to VP Engineering |
| F | 0.0 – 2.9 | Failing | No meaningful production readiness; foundational work required | Halt; reassess architecture and operational posture |

## Signal Tables

### Reliability

| Score | Evidence |
|-------|----------|
| 9-10 | Multi-AZ deployment with automated failover tested; DR runbook executed within RTO; graceful degradation verified under dependency failures |
| 7-8 | Multi-AZ deployment configured; failover documented but not tested end-to-end; basic health checks in place |
| 5-6 | Single-AZ with backup plan documented; health checks exist but no automated failover |
| 3-4 | No redundancy; manual recovery only; health checks missing or non-functional |
| 0-2 | Single instance with no backup, no health checks, no disaster recovery plan |

### Observability

| Score | Evidence |
|-------|----------|
| 9-10 | Structured logging with correlation IDs; RED metrics with SLO burn-rate alerts; distributed tracing across all services; dashboards verified accurate |
| 7-8 | Logging and metrics present; alerting configured for key SLOs; tracing exists but incomplete for some paths |
| 5-6 | Basic logging exists; some metrics collected; no distributed tracing; alerts only for errors |
| 3-4 | Unstructured logging; minimal metrics; no alerting; dashboards absent or stale |
| 0-2 | No logging infrastructure; no metrics collection; no observability of any kind |

### Security

| Score | Evidence |
|-------|----------|
| 9-10 | Secrets in Vault/KMS with rotation; mTLS between services; vulnerability scans green; IAM least-privilege verified; security review completed |
| 7-8 | Secrets managed properly; TLS enforced; vulnerability scanning scheduled; minor IAM permissions to tighten |
| 5-6 | Secrets not hardcoded but rotation not automated; TLS present but not enforced on all paths; scanning not regular |
| 3-4 | Some secrets in environment variables without rotation; no vulnerability scanning; auth present but not enforced consistently |
| 0-2 | Hardcoded secrets; no TLS; no auth between services; no vulnerability management |

### Performance

| Score | Evidence |
|-------|----------|
| 9-10 | Load tested to 2x projected peak; SLOs defined with error budgets; auto-scaling validated; capacity headroom documented |
| 7-8 | Load tested to projected peak; SLOs defined; auto-scaling configured but not stress-tested |
| 5-6 | Basic load testing done; SLOs partially defined; manual scaling only |
| 3-4 | No load testing; SLOs vaguely defined; resource limits not set |
| 0-2 | No performance validation; no SLOs; no understanding of capacity limits |

### Operational Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | Runbooks for all failure modes with tested procedures; on-call rotation with trained responders; deployment and rollback tested; game-day exercise completed |
| 7-8 | Runbooks exist for common failures; on-call rotation established; deployment documented but rollback not rehearsed |
| 5-6 | Some runbooks exist; on-call rotation in place but responders lack training; deployment partially automated |
| 3-4 | No runbooks; ad-hoc on-call; manual deployment without documentation |
| 0-2 | No operational documentation; no on-call; no deployment procedures |
