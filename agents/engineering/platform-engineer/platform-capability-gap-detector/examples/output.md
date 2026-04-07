# Platform Capability Assessment — Meridian AI

| Field | Value |
|---|---|
| Team | Meridian AI Platform |
| Overall Score | 57/100 |
| Grade | C |
| Verdict | ACCEPTABLE |
| Critical/High Gaps | 2 (Security, Developer Self-Service) |
| Skill | platform-capability-gap-detector |

## Domain Scores

| Domain | Completeness | Weight | Severity | Missing Capabilities |
|---|---|---|---|---|
| CI/CD | 100% | 30 | LOW | None — fully covered |
| Observability | 50% | 25 | HIGH | Distributed tracing, Alerting with runbooks |
| Security & Compliance | 25% | 25 | CRITICAL | Dependency scanning, Secret scanning in CI, Audit logging |
| Infrastructure | 50% | 5 | MEDIUM | Drift detection, Cost tagging |
| Developer Onboarding | 75% | 10 | LOW | Local dev environment <30 min |
| Developer Self-Service | 0% | 2 | CRITICAL | Portal, service catalogue, feature flags |
| Data Platform | N/A | 3 | — | Not assessed |

## Critical/High Gaps

### Security & Compliance — CRITICAL (25% complete)

**Missing:**
1. **Dependency vulnerability scanning** — No Dependabot or Snyk. Two secret-in-code incidents in Q1 indicate systemic gap.
2. **Secret scanning in CI** — Must prevent secrets from entering codebase. Add gitleaks or detect-secrets as pre-commit hook.
3. **Centralized audit logging** — Required for SOC 2. AWS CloudTrail is likely in place but not aggregated or monitored.

**Investor diligence risk:** Security gaps are the most common Series A technical red flags. Fix before the diligence technical review.

### Developer Self-Service — CRITICAL (0% complete)

**Missing:**
1. **Internal developer portal** — Backstage or similar; teams lack discoverability of services
2. **Service catalogue** — No inventory of services, owners, and runbooks in one place
3. **Feature flag service** — No LaunchDarkly or similar; teams deploy code with if/else flags or full releases

**Note:** Developer self-service is low weight (2%) in the scoring model but is highly visible in Series A technical diligence as a signal of engineering maturity.

### Observability — HIGH (50% complete)

**Missing:**
1. **Distributed tracing** — Only 4/8 services instrumented. OpenTelemetry implementation is required to debug distributed issues.
2. **Alerting runbooks** — Alerts fire but on-call engineers have no documented remediation steps.

## Recommendations by Timeline

### This Sprint (Before Diligence)
1. Enable Dependabot on all repositories (1 hour — GitHub setting)
2. Add gitleaks pre-commit hook to prevent secret commits
3. Enable AWS CloudTrail and configure CloudWatch log aggregation for audit trail

### Q2 Sprint 1 (Weeks 1-2)
4. Instrument remaining 4 services with OpenTelemetry tracing
5. Write runbooks for all P1 Datadog alerts

### Q2 Sprint 2 (Weeks 3-4)
6. Add Terraform drift detection (Atlantis or Spacelift)
7. Implement feature flag service (LaunchDarkly recommended; open-source: Flagsmith)

### Q3
8. Internal developer portal (Backstage — 1-2 engineer sprints to set up)
9. Service catalogue as part of Backstage implementation
