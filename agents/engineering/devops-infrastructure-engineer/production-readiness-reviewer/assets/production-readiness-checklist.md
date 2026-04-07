# Production Readiness Review: [Service / Feature Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Reviewer | DevOps / Infrastructure Engineer |
| Service | [Service name and owning team] |
| Release | [Version / Commit SHA] |
| Skill | production-readiness-reviewer |
| Outcome | [Approved / Blocked / Conditional Approval] |

## Verdict

**Overall status**: [APPROVED / BLOCKED — N critical items / CONDITIONAL — N items due by Date]

---

## Category 1: Deployment and Rollback

- [ ] Deployment is automated (no manual shell commands required)
- [ ] Deployment is idempotent (safe to run twice)
- [ ] Rollback procedure documented and tested (not just described)
- [ ] Feature flags enable instant traffic cutoff without a deploy
- [ ] Database migrations are backward-compatible (old binary runs against new schema)
- [ ] Zero-downtime deploy strategy in place (rolling update / blue-green / canary)
- [ ] Config and secrets injected at runtime (not baked into image)

**Blocking items**: [None / List]

---

## Category 2: Observability

- [ ] Structured logs emitting to central log aggregation (not just stdout to dev)
- [ ] Distributed traces connected to APM (request IDs propagated)
- [ ] Key metrics instrumented: request rate, error rate, latency (p50/p95/p99)
- [ ] Business metrics instrumented (e.g., orders/min, signups/min)
- [ ] Service has a dashboard in monitoring tool (not just global dashboard)
- [ ] Error tracking configured (Sentry / Datadog Error Tracking / equivalent)

**Blocking items**: [None / List]

---

## Category 3: Alerting

- [ ] Alert on error rate > threshold (not just on "service is down")
- [ ] Alert on latency SLO breach (p99 threshold)
- [ ] Alert on upstream dependency failure
- [ ] Alerts have runbook links (not bare metric threshold notifications)
- [ ] Alert noise validated: no alerts that fire > 1/week as false positives
- [ ] On-call rotation includes this service

**Blocking items**: [None / List]

---

## Category 4: Security

- [ ] No secrets in environment variables, source code, or Docker image (use secrets manager)
- [ ] All endpoints with user data require authentication
- [ ] Input validation on all user-supplied fields
- [ ] Dependencies have no unresolved Critical or High CVEs
- [ ] SAST scan passed in CI
- [ ] Security review completed (if touching auth, payments, or PII)
- [ ] HTTPS enforced; no plaintext communication between services in production

**Blocking items**: [None / List]

---

## Category 5: Performance and Scalability

- [ ] Load test completed against expected peak traffic (results attached)
- [ ] Performance meets SLO targets at expected peak load
- [ ] Auto-scaling policy configured and tested
- [ ] Database connection pool sized correctly (not default values)
- [ ] Slow queries identified and indexed (query plan reviewed)
- [ ] Pagination on all endpoints returning collections
- [ ] Rate limiting configured on public-facing endpoints

**Blocking items**: [None / List]

---

## Category 6: Reliability

- [ ] Health check endpoint responds correctly (not just port open)
- [ ] Readiness probe configured (service not routed traffic until ready)
- [ ] Liveness probe configured (service restarted if unhealthy)
- [ ] Circuit breakers configured on calls to upstream services
- [ ] Retry strategy defined (with backoff) for retryable failures
- [ ] Timeouts set on all outbound calls (no system defaults)
- [ ] Graceful shutdown: in-flight requests complete before process exits

**Blocking items**: [None / List]

---

## Category 7: Operational Runbooks

- [ ] Runbook exists for each P1/P2 alert
- [ ] Runbooks reviewed by an engineer who did not write them
- [ ] On-call procedure documented (who to call, what to do first)
- [ ] Incident severity guide updated to include this service
- [ ] Post-deploy smoke test procedure documented

**Blocking items**: [None / List]

---

## Category 8: Data and Storage

- [ ] Data retention policy defined (how long is data stored, when is it purged)
- [ ] PII data fields identified and handling documented
- [ ] Backup schedule configured and restore procedure tested
- [ ] Database migration rollback script exists and tested in staging
- [ ] Storage quota / disk usage monitored with alert

**Blocking items**: [None / List]

---

## Summary: Blocking Items

| # | Category | Blocking Issue | Owner | Required By |
|---|----------|---------------|-------|------------|
| 1 | [Category] | [Specific item not completed] | [Role] | [Date] |

## Conditional Approval Items

Items approved with the condition they are completed by the date below:

| # | Category | Item | Owner | Due |
|---|----------|------|-------|-----|
| 1 | [Category] | [Item] | [Role] | [Date] |

**Signed off by**: DevOps Engineer: [Name] | Date: [YYYY-MM-DD]
