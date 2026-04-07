# Integration Test Execution Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD HH:MM UTC] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | integration-test-runner |
| Repository | [Repo name and commit SHA] |
| Branch / PR | [Branch name or PR link] |
| Environment | [CI / Staging / Local] |
| Change Set Summary | [Brief description of what changed] |

## Executive Summary

[2-3 sentences covering the overall pass/fail verdict, component boundaries tested, and any blocking issues.
GUIDANCE: Lead with the verdict and the most significant finding. Example: "All 143 integration tests pass. The payment service to Stripe contract test revealed a response schema change in the `payment_intent` object that will break the consumer in the next Stripe API version. One flaky test in the email service was quarantined and filed as ENG-2341."]

## Test Execution Results

[Summary of pass/fail counts across all component boundaries.

GUIDANCE:
- Good: "143 passed, 0 failed, 2 quarantined (flaky). Boundaries tested: checkout→payments, payments→stripe, users→email, checkout→inventory."
- Bad: "Integration tests completed."
- Format: Summary table followed by per-boundary breakdown]

| Metric | Value |
|--------|-------|
| Total tests | [N] |
| Passed | [N] |
| Failed | [N] |
| Quarantined (flaky) | [N] |
| Execution time | [N minutes] |
| Boundaries covered | [N of M total boundaries] |

### Results by Component Boundary

| Boundary | Tests | Passed | Failed | Coverage |
|----------|-------|--------|--------|----------|
| [Service A → Service B] | [N] | [N] | [N] | [%] |
| [Service B → Database] | [N] | [N] | [N] | [%] |
| [Service C → External API] | [N] | [N] | [N] | [%] |

## Boundary Coverage Analysis

[Map each component boundary to its test coverage status.

GUIDANCE:
- Good: "Checkout→Inventory: 8 tests covering create, update, reservation, timeout, and insufficient stock scenarios. Gap: no test for concurrent reservation conflict."
- Bad: "Most integrations are tested."
- Format: Table with each boundary, scenario coverage, and gap notes]

| Boundary | Covered Scenarios | Missing Scenarios | Risk Assessment |
|----------|------------------|-------------------|----------------|
| [Boundary] | [Happy path, timeout, retry, error X] | [Missing: concurrent conflict] | [Low / Medium / High] |

## Defect Report

[Detail each genuine integration defect found during this run.

GUIDANCE: Distinguish genuine defects from environment issues and flaky tests. Only genuine defects should block the release.]

### Blocking Defects

| ID | Boundary | Defect Description | Severity | Reproduction Steps | Owner |
|----|----------|--------------------|----------|-------------------|-------|
| [JIRA-N] | [Service A → B] | [What broke and how] | [Critical / High] | [Steps] | [Team] |

### Non-Blocking Observations

| Observation | Boundary | Notes | Action |
|-------------|----------|-------|--------|
| [Contract drift detected] | [Boundary] | [What changed] | [Create ticket] |

## Flaky Test Analysis

[Document quarantined flaky tests.

GUIDANCE: Every quarantined test must have a ticket and a root cause hypothesis. Quarantine is temporary — flaky tests must be fixed or deleted within 2 sprints.]

| Test Name | Boundary | Failure Pattern | Hypothesis | Ticket | Deadline |
|-----------|----------|----------------|------------|--------|----------|
| [Test name] | [Boundary] | [Fails 1 in 5 runs on timeout] | [Race condition in async setup] | [Link] | [YYYY-MM-DD] |

## Environment Health

[Report on the state of the test environment.

GUIDANCE: Environment issues must be distinguished from application defects. Document any environment degradation that affected this run.]

| Component | Version | Status | Notes |
|-----------|---------|--------|-------|
| [Service name] | [version] | [Healthy / Degraded] | [Notes if degraded] |
| [Database] | [version/schema] | [Healthy / Schema drift] | [Notes] |
| [External API stub] | [contract version] | [In sync / Drifted] | [Notes] |

## Verdict

| Dimension | Result |
|-----------|--------|
| All tests pass or quarantined | [Yes / No] |
| No blocking defects | [Yes / No — N blockers] |
| Critical boundaries covered | [Yes / No — gaps listed] |
| Environment health acceptable | [Yes / No] |
| **Overall: Block Release** | **[Yes / No]** |

**Blocking issues**: [None / List]

## Recommendations

- **P1 — [Fix]**: [Specific defect to fix before merge, owner, deadline]
- **P2 — [Coverage gap]**: [Missing test scenario, owner, target sprint]
- **P3 — [Environment improvement]**: [Specific environment fidelity improvement, owner, backlog]

## Appendices

### A. Full Test Log

[Link to CI build log with full integration test output.]

### B. Contract Validation Report

[Link to contract test results if using Pact or equivalent contract testing framework.]
