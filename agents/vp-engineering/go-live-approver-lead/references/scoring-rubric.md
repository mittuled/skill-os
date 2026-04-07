# Scoring Rubric: go-live-approver-lead

Evaluates production readiness across quality, observability, security, and operational preparedness before final VP-level go-live sign-off.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Quality Gates | 25% | Test coverage thresholds met, CI green, no open P0/P1 bugs, regression suite passed |
| 2 | Operational Readiness | 25% | Runbooks exist, alerting configured against SLOs, rollback tested, on-call staffed |
| 3 | Security Posture | 20% | Threat model reviewed, auth flows documented, dependency audit clean, secrets managed |
| 4 | Risk Acceptance | 15% | Open risks in register assessed, mitigations in place or formally accepted |
| 5 | Tech Lead Prerequisites | 15% | Tech lead approval complete with all action items resolved |
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
| A+ | 9.0 – 10.0 | Exceptional | All quality gates green, full operational coverage, security reviewed, all risks mitigated, tech lead approved | Approve go-live; proceed to production deployment |
| A | 8.0 – 8.9 | Strong | Quality gates pass, operational readiness confirmed, minor risk items accepted | Approve with post-launch follow-up items tracked |
| B | 7.0 – 7.9 | Good | Most quality gates pass, operational readiness mostly complete, some risk items open | Conditionally approve; resolve items within 48 hours post-launch |
| C | 5.0 – 6.9 | Adequate | Quality gates partially met, operational gaps present, risk items unresolved | Block go-live; specify remediation criteria and re-evaluate in 3-5 days |
| D | 3.0 – 4.9 | Weak | Multiple quality gates failing, operational readiness incomplete, significant risk | Block go-live; require fundamental remediation before re-evaluation |
| F | 0.0 – 2.9 | Failing | Quality gates not run, no operational preparation, risk register absent | Block go-live; release is not production-ready by any measure |

## Signal Tables

### Quality Gates

| Score | Evidence |
|-------|----------|
| 9-10 | Unit test coverage above 80%, integration tests passing, regression suite green, zero open P0/P1 bugs, CI pipeline fully green across all environments, load test completed at 2x expected traffic |
| 7-8 | Coverage above 70%, CI green, zero P0 bugs, one or two P1 bugs with documented workarounds |
| 5-6 | Coverage above 50%, CI green on most jobs, P1 bugs open without workarounds |
| 3-4 | Coverage below 50%, CI has flaky failures, P0 bugs open |
| 0-2 | No test coverage data, CI not run, multiple P0 bugs unresolved |

### Operational Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | Runbooks cover all failure scenarios, SLO-based alerting configured with burn-rate windows, rollback procedure tested in staging within last 48 hours, on-call rotation staffed with backup, dashboards deployed and verified |
| 7-8 | Runbooks cover primary failure scenarios, alerting configured, rollback documented but not recently tested, on-call staffed |
| 5-6 | Runbooks exist but incomplete, basic alerting in place, rollback procedure documented but untested, on-call assigned |
| 3-4 | No runbooks, alerting basic (uptime only), rollback procedure vague, on-call informally assigned |
| 0-2 | No operational preparation; no runbooks, alerting, rollback plan, or on-call assignment |

### Security Posture

| Score | Evidence |
|-------|----------|
| 9-10 | Threat model reviewed and signed off, authentication and authorization flows documented, dependency audit shows zero known critical CVEs, secrets managed via vault or secret manager, CORS/CSP headers configured |
| 7-8 | Threat model exists, auth flows documented, dependency audit completed with all critical CVEs patched |
| 5-6 | Threat model drafted but not reviewed, auth flows partially documented, dependency audit has medium-severity CVEs unpatched |
| 3-4 | No threat model, auth flows undocumented, dependency audit not performed |
| 0-2 | No security review of any kind performed |

### Risk Acceptance

| Score | Evidence |
|-------|----------|
| 9-10 | Risk register current, all high-severity risks mitigated or formally accepted with documented rationale and executive sign-off |
| 7-8 | Risk register current, high-severity risks mitigated, medium risks documented with acceptance rationale |
| 5-6 | Risk register exists but not updated for this release, some risks without mitigation plans |
| 3-4 | Risk register stale, high-severity risks without mitigations |
| 0-2 | No risk register exists |

### Tech Lead Prerequisites

| Score | Evidence |
|-------|----------|
| 9-10 | Tech lead go-live approval document present, all action items from tech lead review marked resolved with evidence, no outstanding conditions |
| 7-8 | Tech lead approval present, most action items resolved, one or two low-severity items tracked for post-launch |
| 5-6 | Tech lead approval present but conditional, some action items still in progress |
| 3-4 | Tech lead review conducted but no formal approval issued |
| 0-2 | No tech lead review conducted |
