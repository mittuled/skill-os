# Golden Path Audit — Meridian AI Platform Engineering

| Field | Value |
|---|---|
| Team | Meridian AI Platform Engineering |
| Domains Audited | 5 |
| Domains Enforced | 1 (Deployment) |
| Enforcement Rate | 20% |
| Gaps Requiring Action | 2 (New Service, Security) |
| Missing Standard Domains | 1 (API Design) |
| Skill | golden-path-definer |

## Domain Status

| Domain | Maturity | Tools | Gap? |
|---|---|---|---|
| New Service Creation | Draft | GitHub template (partial), Docker Compose | YES |
| Deployment | Enforced | GitHub Actions, ArgoCD, Terraform | No |
| Observability | Active | Datadog APM, Datadog Logs, PagerDuty | Partial |
| Database Access | Active | PostgreSQL, Prisma ORM, PgBouncer | Partial |
| Security | Not Started | None | YES |

## Gaps — Action Required

### New Service Creation (Draft → Active required)
**Problem:** Template exists but is 6 months old. No CI/CD, observability, or secret management pre-wired. New engineers diverge on setup.

**Standard Components Required:**
1. Update GitHub template repo with current stack (ArgoCD, Datadog, Vault)
2. Pre-wire GitHub Actions workflow in template
3. Include Datadog structured logging config out of the box
4. Include Vault/AWS Secrets Manager integration example
5. Add local devcontainer setup
6. Add README template with runbook link placeholder

**Owner:** Platform Team | **Target:** 2-week sprint

---

### Security (Not Started — highest priority)
**Problem:** No automated dependency scanning. Secret-in-code incidents occurred twice in Q1. This is a SOC 2 requirement and a P0 platform gap.

**Standard Components Required:**
1. Dependabot or Snyk — enable on all repos this week
2. Semgrep — add to CI/CD pipeline for static analysis
3. Pre-commit hook to block secrets (gitleaks or detect-secrets)
4. IAM role policy per service (document in golden path)
5. HTTPS enforcement checklist

**Owner:** Platform Team + CTO | **Target:** 1 week for Dependabot + pre-commit hook; 1 month for full implementation

## Partial Coverage — Improvement Actions

### Observability (Active → Enforced)
- Require structured JSON logging in all services (add to new service template)
- Instrument remaining 4 services with OpenTelemetry tracing
- Standardize on OpenTelemetry collector rather than per-library integrations
- Document alerting runbooks for all P1 alert types

### Database Access (Active → Enforced)
- Enforce read replica routing via ORM config — document pattern in golden path
- Add migration review step to PR checklist for schema changes
- Consider connection pool monitoring in Datadog to catch pool exhaustion

## Missing Domain: API Design
The API design golden path has not been addressed. With 3 engineering teams building services, this will create integration inconsistencies without a standard.

**Recommend defining:**
1. REST vs. gRPC decision tree
2. OpenAPI spec generation from code (e.g., FastAPI/NestJS native, or Spectral linting)
3. Auth pattern (Bearer token via identity service)
4. Versioning strategy (/v1/ URL prefix standard)

## Q2 Golden Path Roadmap

| Priority | Domain | Work | Target |
|---|---|---|---|
| P0 | Security | Dependabot + pre-commit hooks | April 14 |
| P1 | New Service Template | Refresh template with full stack | April 28 |
| P2 | Observability | Enforce tracing in all services | May 15 |
| P3 | API Design | Define and publish golden path | May 30 |
| P4 | Database Access | Enforce read replica routing | June 15 |
