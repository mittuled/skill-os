# Unit Test Execution Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD HH:MM UTC] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | unit-test-runner |
| Repository | [Repo name and commit SHA] |
| Branch / PR | [Branch name or PR link] |
| Test Framework | [Jest / pytest / JUnit / Vitest / other] |

## Executive Summary

[2-3 sentences covering the overall pass/fail verdict, coverage status, and any blocking issues.
GUIDANCE: Lead with the verdict. Example: "All 847 unit tests pass. Statement coverage is 88.2%, exceeding the 80% threshold. Two tests exhibit ordering dependencies that will be addressed in the next sprint but do not block this PR."]

## Test Execution Results

[Summary table of pass/fail counts and execution time.

GUIDANCE:
- Good: "847 passed, 0 failed, 3 skipped. Execution time: 42.3 seconds. Slowest test: `UserService.processPayment` at 340ms."
- Bad: "Tests pass mostly."
- Format: Summary table followed by details on any failures]

| Metric | Value |
|--------|-------|
| Total tests | [N] |
| Passed | [N] |
| Failed | [N] |
| Skipped | [N] |
| Execution time | [N seconds] |
| Slowest test | [test name]: [N ms] |

## Coverage Report

[Coverage breakdown by metric and comparison to threshold.

GUIDANCE:
- Good: "Statement: 88.2% (threshold: 80%) ✓. Branch: 82.1% (threshold: 75%) ✓. Uncovered paths: 3 error handlers in `payment.service.ts` lines 145–167."
- Bad: "Coverage is good."
- Format: Table with threshold, actual, delta, and status]

| Coverage Type | Threshold | Actual | Delta vs. Threshold | Status |
|---------------|-----------|--------|---------------------|--------|
| Statements | [X]% | [Y]% | [+/- Z]% | [Pass / Fail] |
| Branches | [X]% | [Y]% | [+/- Z]% | [Pass / Fail] |
| Functions | [X]% | [Y]% | [+/- Z]% | [Pass / Fail] |
| Lines | [X]% | [Y]% | [+/- Z]% | [Pass / Fail] |

### Uncovered Critical Paths

[List code paths that are uncovered and assess risk.

GUIDANCE: Focus on uncovered paths in business-critical code. Trivial uncovered paths (e.g., getters) do not need listing.]

| File | Lines | Description | Risk |
|------|-------|-------------|------|
| [filename] | [L1–L2] | [What this code does] | [Low / Medium / High] |

## Failure Analysis

[Detail each failing test.

GUIDANCE: If no failures, write "No test failures." If failures exist, each must have a triage category.]

| Test Name | Failure Type | Error Message | Affected Code Path | Triage |
|-----------|-------------|---------------|-------------------|--------|
| [Test name] | [Logic error / Stale mock / Ordering dependency / Environment issue] | [Exact error] | [File: line] | [Action required] |

### Failure Triage Categories

- **Logic error**: Code behavior does not match expected behavior — requires code fix
- **Stale mock**: Mock return value no longer matches the real interface — update mock
- **Ordering dependency**: Test passes only when run after another test — fix test isolation
- **Environment issue**: Test relies on environment configuration not present in CI — fix test setup

## Test Quality Observations

[Note any test quality issues observed during the run.

GUIDANCE: Document isolation issues, slow tests, and weak assertions even when tests pass — these are technical debt.]

### Isolation Issues

[Tests that pass in suite but may fail in isolation, or that share mutable state.]

### Slow Tests

[Tests exceeding 200ms with explanation of whether the speed is justified.]

| Test Name | Execution Time | Cause | Action |
|-----------|---------------|-------|--------|
| [Test name] | [N ms] | [Real sleep / network call / heavy computation] | [Acceptable / Fix] |

### Assertion Quality Issues

[Tests with weak assertions that reduce suite confidence.]

## Verdict

| Dimension | Result |
|-----------|--------|
| All tests pass | [Yes / No — N failures] |
| Coverage thresholds met | [Yes / No — specify] |
| No ordering dependencies | [Yes / N issues found] |
| Execution time acceptable | [Yes / No — N seconds] |
| **Overall: Block PR** | **[Yes / No]** |

**Blocking issues**: [None / List of issues that block merging]

## Recommendations

- **P1 — [Action]**: [Specific fix, owner, deadline] — required to unblock this PR
- **P2 — [Action]**: [Technical debt item, owner, target sprint]
- **P3 — [Action]**: [Test quality improvement, owner, backlog]

## Appendices

### A. Full Test Output

[Attach or link to the full test runner output log.]

### B. Coverage Report

[Attach or link to the HTML coverage report.]
