# Regression Test Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD HH:MM UTC] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | regression-test-runner |
| Release Candidate | [Version / tag / branch] |
| Repository | [Repo name and commit SHA] |
| Change Set | [PR / milestone / sprint summary] |
| Test Environment | [Environment name and version] |

## Executive Summary

[2-3 sentences covering the go/no-go recommendation, pass rate, and any blocking defects.
GUIDANCE: Lead with the verdict and the primary justification. Example: "RELEASE HOLD: 2 blocking regressions found in the payment and inventory modules. 891 of 894 tests pass (99.7%). The 2 blocking defects must be resolved and regression re-run before release can proceed. 1 additional high-severity observation filed as a non-blocker."]

## Test Execution Summary

[Aggregate pass/fail metrics.

GUIDANCE:
- Good: "894 total tests. 891 passed, 2 failed (genuine regressions), 1 quarantined (flaky). Execution time: 18 minutes. Scope: full suite covering all 43 features in the release candidate."
- Bad: "Most tests passed."
- Format: Summary table]

| Metric | Value |
|--------|-------|
| Total tests | [N] |
| Passed | [N] |
| Failed — Genuine regression | [N] |
| Failed — Environment issue | [N] |
| Quarantined — Flaky | [N] |
| Skipped | [N] |
| Pass rate | [N]% |
| Execution time | [N minutes] |
| Suite scope | [Full / Targeted — explain scope selection] |

## Blocking Defects

[List defects that must be resolved before release.

GUIDANCE:
- Good: "REGRESSION: `checkout.processOrder` returns HTTP 422 when quantity is 0. Introduced by commit abc123 in ENG-4521. Expected: HTTP 400 with validation error. Actual: HTTP 422 with incorrect error body. Owner: checkout team. Severity: High — affects all checkout flows."
- Bad: "Some tests failed."
- Format: One entry per defect with all required fields]

| # | Defect ID | Module | Description | Introduced By | Severity | Owner |
|---|-----------|--------|-------------|---------------|----------|-------|
| 1 | [JIRA-N] | [Module] | [What regressed and how] | [Commit/PR] | [Critical/High] | [Team] |

### Reproduction Steps

**Defect 1 — [ID]: [Brief title]**

1. [Step 1]
2. [Step 2]
Expected: [Expected behavior]
Actual: [Actual behavior]
Evidence: [Log snippet, screenshot link, or test output]

## Non-Blocking Observations

[Issues that do not block this release but should be addressed.

GUIDANCE: Include severity and a target sprint. "Non-blocking" does not mean "ignore".]

| Observation | Module | Severity | Notes | Recommended Action | Target |
|-------------|--------|----------|-------|-------------------|--------|
| [Description] | [Module] | [Medium/Low] | [Context] | [Specific action] | [Sprint/date] |

## Flaky Test Log

[Document tests quarantined during this run.

GUIDANCE: Every quarantined test is technical debt. Include the ticket and deadline.]

| Test Name | Module | Failure Pattern | Ticket | Fix Deadline |
|-----------|--------|----------------|--------|--------------|
| [Name] | [Module] | [Fails intermittently — describe pattern] | [Link] | [YYYY-MM-DD] |

## Coverage Assessment

[Evaluate whether regression suite covered the change set adequately.

GUIDANCE: A regression suite that passed but didn't cover the change set provides false confidence. Note coverage gaps explicitly.]

| Changed Module | Tests in Suite | Change Set Coverage | Gap Notes |
|----------------|---------------|---------------------|-----------|
| [Module] | [N tests] | [%] | [Any features changed without corresponding regression tests] |

## Release Recommendation

**Verdict**: [GO / HOLD / CONDITIONAL GO]

| Condition for Release | Status |
|----------------------|--------|
| Zero blocking defects | [Met / Not Met — N remaining] |
| Suite scope covers change set | [Met / Not Met — gaps noted above] |
| Environment was stable | [Met / Not Met — describe issues] |
| Flaky tests at acceptable level | [Met / Not Met — N quarantined] |

**Conditions for release (if CONDITIONAL GO)**:
1. [Specific condition that must be met]
2. [Specific verification step after condition is met]

**Re-run required after fix**: [Yes / No]

## Recommendations

- **P1 — Block**: [Defect to fix, owner, fix deadline]
- **P2 — Post-release**: [High-severity observation, owner, target sprint]
- **P3 — Suite improvement**: [Coverage gap to close, owner, backlog item]

## Appendices

### A. Full Test Output

[Link to CI build log with complete regression run output.]

### B. Feature-to-Test Traceability

[Link to the feature coverage matrix mapping features to regression test cases.]

### C. Environment Configuration

[Record of the test environment state: version, database state, and configuration at time of run.]
