# Staging Validation Checklist: [Service / Release Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Validator | QA Test Engineer |
| Service | [Service name] |
| Release | [Version / Build / Git SHA] |
| Environment | Staging |
| Skill | staging-validator |
| Deployment Ticket | [Link] |
| Status | [In Progress / Pass / Fail / Blocked] |

## Pre-Validation Checks

- [ ] Deployment to staging completed without errors
- [ ] Database migrations ran successfully (check migration logs)
- [ ] All dependent services available in staging (verify dependency health endpoints)
- [ ] Test data seeded or confirmed present
- [ ] Feature flags configured to match production baseline (unless testing a new flag)
- [ ] Monitoring and alerting active on staging
- [ ] Previous staging state cleaned up (no residual data from prior release)

## Functional Validation

### Core User Flows

For each critical flow, mark as PASS, FAIL, or SKIP (with reason):

| Flow | Steps | Result | Notes |
|------|-------|--------|-------|
| [User registration] | [1. POST /auth/signup, 2. Email verification, 3. Login] | [PASS/FAIL] | |
| [Core transactional flow] | [Steps] | | |
| [Admin operation] | [Steps] | | |
| [Error recovery flow] | [Steps] | | |

### New Feature Validation

For each feature in this release:

| Feature | Acceptance Criteria | Test Method | Result |
|---------|--------------------|-----------|----|
| [Feature name] | [AC from ticket] | [Manual / Automated] | [PASS/FAIL] |

### Regression Coverage

- [ ] Regression test suite executed: [Test suite name]
- [ ] Pass rate: [X / Y tests passed] ([X%])
- [ ] Failed tests reviewed — all failures confirmed as known issues or new bugs
- [ ] No new failures introduced by this release

## Integration Validation

### Third-Party Integrations

| Integration | Method | Test Case | Result |
|-------------|--------|-----------|--------|
| [Payment provider] | [Stripe test mode] | [Charge $1.00 with test card] | [PASS/FAIL] |
| [Email provider] | [SendGrid sandbox] | [Trigger welcome email] | |
| [Auth provider] | [OAuth flow] | [Login via [provider]] | |
| [Analytics] | [Event inspector] | [Page view event fires] | |

### API Contract Validation

- [ ] All API endpoints return documented status codes
- [ ] Response schemas match API contract (run contract tests or schema validation)
- [ ] Rate limiting headers present on expected endpoints
- [ ] Authentication required on all protected endpoints (verify 401 on unauthenticated request)

## Non-Functional Validation

### Performance

- [ ] Page load time (web): ≤ [X] seconds (target: [≤ 2s for LCP])
- [ ] API response time (p50): ≤ [X] ms
- [ ] API response time (p95): ≤ [X] ms
- [ ] No memory leak observed over [15-minute soak test]

**Measured p95 latency on critical endpoints**:

| Endpoint | p50 | p95 | p99 | Pass? |
|----------|-----|-----|-----|-------|
| [GET /api/products] | [X ms] | [X ms] | [X ms] | |
| [POST /api/orders] | [X ms] | [X ms] | [X ms] | |

### Security

- [ ] HTTPS enforced; HTTP redirects to HTTPS
- [ ] CSP headers present and correct
- [ ] Sensitive endpoints require authentication
- [ ] No PII in URL parameters or logs (spot-check via log query)
- [ ] Dependencies have no new Critical/High CVEs introduced by this release

### Observability

- [ ] Application logs flowing to log aggregation platform
- [ ] Traces visible in APM tool for critical flows
- [ ] Metrics reporting: request rate, error rate, latency visible in dashboard
- [ ] No new unhandled exceptions in error tracking tool

## Data Integrity Validation

- [ ] Database migrations: schema matches expected state (run `diff` against expected schema)
- [ ] Seed data present and correct
- [ ] No orphaned records from migration
- [ ] Rollback migration script tested (optional for low-risk releases, required for schema changes)

## Release Gate Decision

| Category | Status | Notes |
|----------|--------|-------|
| Core user flows | [PASS/FAIL] | |
| New features | [PASS/FAIL] | |
| Regression suite | [PASS/FAIL] | |
| Integrations | [PASS/FAIL] | |
| Performance | [PASS/FAIL] | |
| Security | [PASS/FAIL] | |
| Observability | [PASS/FAIL] | |

**Overall verdict**: [APPROVED FOR PRODUCTION / BLOCKED — reason]

**Blocking issues** (if any):

1. [Issue description, severity, and required resolution]

**Sign-off**: QA Engineer: [Name] | Date: [YYYY-MM-DD]
