# Scoring Rubric: unit-test-runner

Evaluates the quality of a unit test suite across coverage adequacy, test isolation, assertion quality, execution speed, and failure clarity.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Coverage Adequacy | 30% | Statement, branch, and path coverage against configured threshold |
| 2 | Test Isolation | 25% | Tests run independently without side effects or shared mutable state |
| 3 | Assertion Quality | 20% | Assertions verify specific behavior, not just execution |
| 4 | Execution Speed | 15% | Suite runs fast enough to support CI feedback loop requirements |
| 5 | Failure Clarity | 10% | Failing tests produce messages that identify the failure cause without debugging |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent or non-functional, 5 = present with significant gaps, 10 = best-in-class, no gaps.

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | Coverage ≥ 95%, all tests isolated, assertions specific, suite runs in < 30 seconds, failures self-diagnosing | Maintain; use as reference for other services |
| A | 8.0–8.9 | Strong | Coverage ≥ 85%, minor isolation issues, most assertions specific, suite runs in < 60 seconds | Schedule review in next quarter; no blockers |
| B | 7.0–7.9 | Good | Coverage ≥ 80%, a few ordering dependencies, some assertion gaps, suite runs in < 2 minutes | Identify and fix top isolation and assertion gaps next sprint |
| C | 5.0–6.9 | Adequate | Coverage 60–79%, noticeable test interdependencies, broad assertions, suite runs in 2–5 minutes | Coverage and isolation improvement sprint required before new features |
| D | 3.0–4.9 | Weak | Coverage 40–59%, tests regularly fail in different order, assertions only check for no-crash, suite flaky | Urgent test quality improvement; block merging until resolved |
| F | 0.0–2.9 | Failing | Coverage < 40%, suite cannot run in isolation, tests assert nothing meaningful, suite takes > 10 minutes | Do not ship; unit testing foundation must be rebuilt |

## Signal Tables

### Coverage Adequacy

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Statement coverage ≥ 95%; branch coverage ≥ 90%; all critical business logic paths explicitly tested; coverage does not drop on any PR |
| 7–8 | Statement coverage ≥ 85%; branch coverage ≥ 80%; major logic paths covered; occasional uncovered branch in error handling |
| 5–6 | Statement coverage 70–84%; branch coverage 60–79%; happy path covered but many error paths untested |
| 3–4 | Statement coverage 40–69%; branch coverage < 60%; only a subset of modules tested; coverage drops frequently on PRs |
| 0–2 | Statement coverage < 40%; most code has no tests; coverage reports unavailable or disabled |

### Test Isolation

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every test passes when run individually; no shared mutable state between tests; all external dependencies mocked; test order has zero effect on results |
| 7–8 | 95%+ tests pass in isolation; 1–2 tests share database state but are contained within a single module; cleanup hooks present but occasionally miss edge cases |
| 5–6 | 80–94% tests pass in isolation; test ordering occasionally matters; some tests fail when run individually due to missing setup |
| 3–4 | Significant ordering dependencies; tests frequently pass as a suite but fail individually; shared global state mutated without cleanup |
| 0–2 | Tests cannot run individually; suite requires specific execution order to pass; shared database or filesystem state modified without teardown |

### Assertion Quality

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every test has at least one assertion on a specific output value; assertions use deep equality for objects; negative paths assert specific error types and messages |
| 7–8 | Most tests have specific assertions; 1–2 tests per 100 use weak assertions (e.g., `toBeTruthy`); error path assertions check type but not message |
| 5–6 | Mix of specific and weak assertions; 10–20% of tests use only existence or truthy checks; no assertion on error path specifics |
| 3–4 | Majority of tests use weak assertions (`expect(result).toBeTruthy()`); tests pass as long as no exception is thrown; no error path coverage |
| 0–2 | Tests execute code without any assertions; suite "passes" by running without throwing; assertions all check `toBeDefined` or `not.toBeNull` |

### Execution Speed

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Full suite runs in < 30 seconds; no individual test exceeds 100ms; parallelizable with `--runInBand` not required |
| 7–8 | Full suite runs in < 60 seconds; 1–3 tests exceed 500ms (documented as justified); CI feedback < 2 minutes total |
| 5–6 | Full suite runs in 1–3 minutes; 5–10% of tests exceed 500ms; slow tests slow down CI merge queue |
| 3–4 | Full suite runs in 3–8 minutes; many tests have `sleep()` calls or wait for real network; CI feedback loop > 5 minutes |
| 0–2 | Full suite runs > 10 minutes; tests make real network calls or wait on external services; engineers routinely skip tests locally |

### Failure Clarity

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every failure message includes: what was expected, what was received, and which input caused the failure; test names describe behavior in plain language |
| 7–8 | Most failures show expected vs. actual values; test names are descriptive; occasional "expected true, received false" without context |
| 5–6 | Failures show expected vs. actual for some tests; test names are function-name-based (e.g., `test('processPayment')`); engineers need debugger to diagnose failures |
| 3–4 | Failures show only assertion error without context; test names are generic (`test('test1')`); stack traces point into test framework internals |
| 0–2 | Failures produce unreadable output; test names do not indicate what is being tested; engineers cannot determine failure cause from the output alone |
