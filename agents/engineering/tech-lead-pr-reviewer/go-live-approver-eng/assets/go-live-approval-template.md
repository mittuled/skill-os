# Go-Live Approval

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Lead / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | go-live-approver-eng |

## Executive Summary

[2-3 sentences stating the release name, the go/no-go decision, and the rationale in one line.
GUIDANCE: The first sentence must be the decision. Example: "Payments v2 is APPROVED for go-live on 2026-04-15. All acceptance criteria are verified, test suites are green, and the rollback procedure was successfully tested in staging. One P2 risk (DB migration timing) is accepted with a DBA on standby during Phase 1 rollout."]

## Decision

| Field | Value |
|-------|-------|
| **Decision** | **GO / NO-GO / CONDITIONAL GO** |
| Release Name | [Feature / release name] |
| Planned Go-Live Date | [YYYY-MM-DD] |
| Decision Date | [YYYY-MM-DD] |
| Tech Lead Sign-Off | [Name] |
| Re-evaluation Date (if No-Go) | [YYYY-MM-DD / N/A] |

## Acceptance Criteria Checklist

[Verification status for every ticket in the release.

GUIDANCE:
- Good: Link to evidence (CI run, demo recording, product owner comment) for each AC item
- Bad: Check boxes without evidence
- Format: Table with evidence links]

| Ticket ID | Feature | AC Status | Evidence | Verified By |
|-----------|---------|-----------|----------|-------------|
| [BE-01] | [Feature name] | Complete / Partial / Incomplete | [Link] | [Name] |

**Summary**: [N] of [N] tickets with fully verified AC. [N] partial or incomplete — see Outstanding Risks.

## Test Coverage Report

[Summary of all test suite results for this release.

GUIDANCE:
- Good: Include the CI run link, overall coverage %, and explicit statement about E2E critical path coverage
- Bad: "Tests are passing"
- Format: Table per suite type]

| Suite | Status | Pass Rate | Coverage % | CI Run Link | Notes |
|-------|--------|-----------|-----------|-------------|-------|
| Unit | Pass / Fail | [N%] | [N%] | [Link] | [Flaky tests noted here] |
| Integration | Pass / Fail | [N%] | [N%] | [Link] | |
| Regression | Pass / Fail | [N%] | N/A | [Link] | |
| E2E (critical paths) | Pass / Fail | [N%] | [N paths of N total] | [Link] | |

## Operational Readiness Checklist

[Confirm each operational prerequisite before approving.

GUIDANCE:
- Every item must be explicitly confirmed with a date or a link — not just checked
- Items marked N/A require justification]

| Item | Status | Confirmed By | Date / Link |
|------|--------|-------------|-------------|
| Monitoring dashboards configured for all key metrics | Confirmed / Not confirmed | [Name] | [Link] |
| Alerts configured and routing tested | Confirmed / Not confirmed | [Name] | [Date tested] |
| Runbooks written and accessible to on-call | Confirmed / Not confirmed | [Name] | [Link] |
| Rollback procedure tested in staging | Confirmed / Not confirmed | [Name] | [Date tested] |
| On-call team briefed on release scope | Confirmed / Not confirmed | [Name] | [Date] |
| Support team briefed on expected user impact | Confirmed / Not confirmed | [Name] | [Date] |

## Risk Assessment

[All known issues, deferred items, and tech debt entering production with this release.

GUIDANCE:
- Good: Every risk has a severity (P1/P2/P3), a mitigation, and an owner
- Bad: "There are some known issues we'll fix later"
- Format: Table; P1 risks with no mitigation = automatic No-Go]

| Risk | Severity | Mitigation | Owner | Resolution Timeline |
|------|----------|-----------|-------|---------------------|
| [Description] | P1 / P2 / P3 | [Specific mitigation action] | [Name] | [Date or "Post-GA Sprint 1"] |

**Risk disposition**: Accepted / Not accepted — [one sentence rationale]

## Blocking Issues (if No-Go)

[If the decision is No-Go, list exactly what must be resolved, by whom, and by when.

GUIDANCE: Be specific enough that the team knows exactly what "done" looks like]

| Blocking Issue | Owner | Required Resolution | Deadline |
|---------------|-------|--------------------|----|
| [Specific unresolved item] | [Name] | [Observable proof of resolution] | [YYYY-MM-DD] |

## Recommendations

[Prioritized actions for the period immediately before and after go-live.
GUIDANCE: P1 items are pre-go-live requirements; P2 are post-go-live follow-ups]

- **P1**: [Must complete before go-live authorization is granted]
- **P2**: [Address in first post-launch sprint]
- **P3**: [Tech debt or improvement to schedule within 30 days]

## Appendices

### A. Methodology

[How AC evidence was collected, which test suites were run and on which build SHA, how operational readiness was assessed (walkthrough, automated check), who participated in the review]

### B. Supporting Data

[Links to full CI run, coverage reports, monitoring dashboards, rollback runbook, risk register, and any previous go-live rejection records for this release]
