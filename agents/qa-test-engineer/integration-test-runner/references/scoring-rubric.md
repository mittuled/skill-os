# Scoring Rubric: integration-test-runner

Evaluates the quality of an integration test suite across boundary coverage, environment fidelity, contract validation, error path coverage, and defect traceability.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Boundary Coverage | 30% | Percentage of cross-component interaction paths covered by tests |
| 2 | Environment Fidelity | 25% | How closely the test environment matches production service behavior |
| 3 | Contract Validation | 20% | Tests verify API contracts, response schemas, and SLA boundaries |
| 4 | Error Path Coverage | 15% | Tests cover failure modes: timeouts, retries, malformed payloads, downstream failures |
| 5 | Defect Traceability | 10% | Failing tests identify the component boundary and failure type without manual investigation |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent or non-functional, 5 = present with significant gaps, 10 = best-in-class, no gaps.

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | All critical boundaries covered with real services, contracts validated against spec, all error paths tested, failures self-diagnosing | Maintain; use as CI gate |
| A | 8.0–8.9 | Strong | 90%+ critical boundaries covered, minor contract gaps, most error paths covered, clear failure messages | Schedule quarterly review; no blockers |
| B | 7.0–7.9 | Good | 75–89% boundaries covered, 1–2 mocked where real should be used, error paths mostly covered | Add missing error path coverage next sprint |
| C | 5.0–6.9 | Adequate | 50–74% boundaries covered, environment uses heavy mocking, happy paths only | Integration coverage improvement sprint required |
| D | 3.0–4.9 | Weak | < 50% boundaries covered, test environment not representative, no error path tests | Major gaps — do not use as CI release gate |
| F | 0.0–2.9 | Failing | Integration tests provide no meaningful signal — all happy path, fully mocked, or not running | Rebuild integration test strategy from scratch |

## Signal Tables

### Boundary Coverage

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every API contract between components has at least one test; new boundaries added to the change set are all covered; test matrix maps each boundary to at least 1 test case |
| 7–8 | 90%+ of API contracts between components covered; 1–2 internal service-to-service interactions untested; coverage matrix exists but has minor gaps |
| 5–6 | 60–89% of component boundaries have test coverage; some services tested only via the primary consumer, not directly; cross-service coverage map is informal |
| 3–4 | 30–59% of boundaries covered; major integrations (database, messaging queue, critical downstream API) untested in integration suite |
| 0–2 | < 30% of boundaries covered; integration tests exercise only the same code paths as unit tests; no cross-service tests present |

### Environment Fidelity

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Tests use real service instances or contract-verified stubs; no live external SaaS (uses test accounts or contract doubles); database state matches production schema version exactly |
| 7–8 | Real services for owned components; contract-verified stubs for third-party APIs; database migrations match production; occasional Docker image version drift (< 1 week) |
| 5–6 | Mix of real and hand-rolled mock services; some database operations against in-memory or simplified schema; test environment requires manual setup steps |
| 3–4 | Most dependencies mocked with hardcoded return values; database uses a different schema version than production; tests pass in CI but behavior diverges from production |
| 0–2 | All dependencies mocked without contract verification; no database; tests exercise application-layer logic only — indistinguishable from unit tests |

### Contract Validation

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Consumer-driven contracts (Pact or equivalent) defined for all API interactions; contract tests run in CI on both consumer and provider side; schema drift detected within 1 day |
| 7–8 | Response schemas validated for 80%+ of API interactions; breaking changes caught in CI; minor fields (metadata, optional) not validated |
| 5–6 | Response bodies spot-checked for key fields; no formal contract framework; breaking changes occasionally discovered in staging, not CI |
| 3–4 | Tests assert HTTP status codes only, not response schema or content; API contract changes discovered in production |
| 0–2 | No response validation; tests assert only that the request did not throw an exception |

### Error Path Coverage

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Tests cover: timeout handling, retry behavior, circuit breaker activation, malformed payload rejection, downstream 4xx and 5xx responses, and connection failure recovery |
| 7–8 | Tests cover: timeout handling, downstream 4xx and 5xx, malformed payload rejection; retry and circuit breaker tested for critical paths only |
| 5–6 | Tests cover downstream 5xx for primary paths; timeout and malformed payload not explicitly tested; retry behavior untested |
| 3–4 | 1–2 error path tests present; most tests are happy-path only; error paths discovered manually during staging |
| 0–2 | No error path tests; suite covers only successful responses |

### Defect Traceability

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Failure message identifies: which component failed, which boundary was crossed, what was expected vs. received, and the test input that caused it |
| 7–8 | Failure message shows component and expected vs. actual; test names indicate the integration scenario; occasional ambiguity requiring 1 log check |
| 5–6 | Failure message shows assertion mismatch; component not identified in message; developer must check integration logs to find which service failed |
| 3–4 | Failures produce generic assertion errors without component context; test names do not describe integration scenario; debugging requires running test locally |
| 0–2 | Failures produce stack traces from internal framework code; impossible to identify failed boundary from test output alone |
