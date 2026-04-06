# Scoring Rubric: go-live-approver-eng

Evaluates engineering readiness for production go-live across acceptance criteria completeness, test coverage, operational readiness, and outstanding risk posture.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Acceptance Criteria Completion | 30% | Percentage of release tickets with all acceptance criteria verified and evidenced |
| 2 | Test Coverage | 25% | Unit, integration, and regression test suite completeness and pass rate for the release |
| 3 | Operational Readiness | 25% | Presence and tested state of monitoring, alerts, runbooks, and rollback procedures |
| 4 | Outstanding Risk Posture | 20% | Volume, severity, and disposition of known issues, deferred items, and tech debt entering production |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent or failed, 5 = partially present with significant gaps, 10 = fully present with no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Go — Exceptional | 100% AC verified; all test suites green; monitoring and rollback tested; zero unmitigated risks | Approve go-live; proceed with rollout plan |
| A | 8.0–8.9 | Go — Strong | ≥ 95% AC verified; minor test gap in non-critical path; operational readiness confirmed; risks documented and accepted | Approve with monitoring focus on flagged risk areas |
| B | 7.0–7.9 | Conditional Go | 85–94% AC verified; test suite green but coverage gaps in edge cases; rollback untested but procedure documented | Conditional approval; require rollback test and gap remediation within 24h |
| C | 5.0–6.9 | No-Go — Significant Gaps | 70–84% AC verified; test failures or critical coverage gaps; monitoring not fully configured; unmitigated P1 risks | No-go until C-level issues resolved; re-evaluate within 48–72h |
| D | 3.0–4.9 | No-Go — Weak | < 70% AC verified; multiple test failures; operational readiness incomplete; multiple unmitigated risks | No-go; schedule structured remediation sprint; re-evaluate in 1 week |
| F | 0.0–2.9 | No-Go — Failing | Critical AC unverified; test suite failing or nonexistent; no operational readiness; unacceptable risk posture | No-go; do not reschedule until each criterion scores ≥ 5 |

## Signal Tables

### Acceptance Criteria Completion

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | 100% of release tickets have AC marked complete with linked evidence (test results, demo recording, or product owner sign-off); no AC marked done without verification |
| 7–8 | 95–99% of tickets AC-complete; 1–2 minor tasks have partial verification; no user-facing features with unverified AC |
| 5–6 | 85–94% of tickets AC-complete; 3–5 tasks with unverified or ambiguous AC; at least one user-facing feature partially unverified |
| 3–4 | 70–84% complete; multiple user-facing features with unverified AC; evidence not collected or inconsistently applied |
| 0–2 | < 70% of tickets have verified AC; AC either absent from many tickets or marked done without verification; release scope unclear |

### Test Coverage

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All test suites (unit, integration, regression, E2E for critical paths) pass at 100%; coverage ≥ 80% across all changed modules; no flaky tests in the suite |
| 7–8 | All suites pass; coverage 70–79% overall; 1–2 flaky tests isolated and documented; E2E covers all critical user paths |
| 5–6 | Unit and integration suites pass; E2E coverage incomplete (critical paths only partially covered); coverage 60–69%; known flaky tests in suite |
| 3–4 | Some test failures in non-critical paths; coverage 50–59%; E2E tests absent or covering < 50% of critical paths |
| 0–2 | Test suite failing; coverage < 50%; no E2E coverage; test results unavailable or not run on current build |

### Operational Readiness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Monitoring dashboards live with all key metrics; alerts tested and routing confirmed; runbooks reviewed and accessible to on-call; rollback procedure executed successfully in staging |
| 7–8 | Dashboards live; alerts configured but not load-tested; runbooks written and accessible; rollback procedure documented but not staged-tested |
| 5–6 | Dashboards partially configured; some alerts missing for non-primary metrics; runbook drafted but not reviewed; rollback procedure undocumented |
| 3–4 | Monitoring reactive only (no proactive alerts); no runbook; rollback procedure is "manually revert the deploy" with no tested steps |
| 0–2 | No monitoring beyond platform defaults; no alerts; no runbook; no rollback plan; on-call team not briefed |

### Outstanding Risk Posture

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Zero unmitigated P1 or P2 risks; all known issues documented in the risk register with accepted mitigations; no deferred must-have items |
| 7–8 | Zero P1 risks; 1–2 P2 risks with accepted mitigation and monitoring plan; deferred items are explicitly non-blocking and tracked |
| 5–6 | Zero P1 risks; 3–5 P2 risks with partial mitigation; some deferred items lack tracking tickets |
| 3–4 | One unmitigated P1 risk present; multiple P2 risks with no mitigation plan; deferred items include items originally scoped as required |
| 0–2 | Multiple unmitigated P1 risks (security vulnerabilities, data loss potential, or SLA-breaking behavior); release scope unclear; risk register absent |
