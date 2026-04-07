# Phase Gate Decision

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Lead / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | inter-phase-reviewer-eng |

## Executive Summary

[2-3 sentences stating the phase being reviewed, the gate decision, and the most significant finding.
GUIDANCE: Start with the decision. Example: "Phase 2 (Build) receives a Conditional Pass to advance to Phase 3 (Test). 91% of deliverables are complete; the remaining item (database migration script) must be merged within the first 3 days of Phase 3. One ADR for the caching strategy is outstanding and must be reviewed before the Phase 3 architecture session."]

## Decision

| Field | Value |
|-------|-------|
| **Decision** | **PASS / CONDITIONAL PASS / HOLD / FAIL** |
| Phase Reviewed | [Phase name and number] |
| Next Phase | [Phase name and number] |
| Review Date | [YYYY-MM-DD] |
| Tech Lead Sign-Off | [Name] |
| Conditions (if Conditional Pass) | [Specific items and deadline] |
| Re-evaluation Date (if Hold/Fail) | [YYYY-MM-DD / N/A] |

## Deliverables Review

[Assessment of every expected phase deliverable against exit criteria.

GUIDANCE:
- Good: Link to the artifact and state specifically which exit criterion it meets or falls short of
- Bad: "Most deliverables are done"
- Format: Table with pass/fail per deliverable]

| Deliverable | Exit Criterion | Status | Evidence | Gap (if any) |
|------------|---------------|--------|----------|-------------|
| [Deliverable name] | [Specific criterion from phase plan] | Pass / Conditional / Fail | [Link or description] | [Specific gap if not Pass] |

**Summary**: [N] of [N] deliverables pass exit criteria. [N] conditional. [N] failed.

## Quality Assessment

[Test coverage, PR review compliance, and defect status.

GUIDANCE:
- Good: Pull CI report; specify coverage % and any failing checks
- Bad: "Quality looks good"
- Format: Table]

| Quality Metric | Status | Value | Target | Notes |
|---------------|--------|-------|--------|-------|
| Test coverage (changed code) | Pass / Fail | [N%] | ≥ 80% | |
| PR review compliance | Pass / Fail | [N%] reviewed | 100% | [Any unreviewed PRs noted] |
| P1 defects | Pass / Fail | [N] open | 0 | |
| P2 defects | Pass / Fail | [N] open | ≤ 2 with mitigation | |
| CI checks at phase close | Pass / Fail | [All green / N failing] | All green | |

## Documentation Review

[Status of all documentation expected from this phase.

GUIDANCE:
- Each item must have a status and a link — "pending" without a link is not acceptable
- Format: Table]

| Document | Type | Status | Owner | Link |
|----------|------|--------|-------|------|
| [ADR title] | ADR | Complete / Draft / Absent | [Name] | [Link] |
| [API spec name] | API Spec | Complete / Draft / Absent | [Name] | [Link] |
| [Runbook name] | Runbook | Complete / Draft / Absent | [Name] | [Link] |

## Carried-Forward Debt Register

[All incomplete items, deferred decisions, and known technical debt entering the next phase.

GUIDANCE:
- Every item must have a severity, owner, and resolution plan
- P1 items are automatic Hold/Fail triggers
- Format: Table]

| Item | Type | Severity | Impact on Next Phase | Owner | Resolution Plan |
|------|------|----------|---------------------|-------|----------------|
| [Description] | Incomplete deliverable / Deferred decision / Tech debt | P1 / P2 / P3 | [Specific impact] | [Name] | [Ticket link + timeline] |

## Conditions for Advance (if Conditional Pass)

[Explicit list of what must be completed before or within the first week of the next phase.

GUIDANCE:
- Good: Specific, verifiable conditions with a named owner and date
- Bad: "Finish the remaining tasks"
- Format: Table]

| Condition | Owner | Deadline | Verification Method |
|-----------|-------|----------|---------------------|
| [Specific deliverable or action] | [Name] | [YYYY-MM-DD] | [How the tech lead will confirm completion] |

## Recommendations

[Prioritized actions for the team entering the next phase.
GUIDANCE: P1 items must be addressed in the first sprint of the next phase]

- **P1**: [Immediate action — addresses gate condition or critical debt]
- **P2**: [Early-phase action — addresses carried-forward items before they compound]
- **P3**: [Process improvement — reduces likelihood of similar gaps in future phase reviews]

## Appendices

### A. Methodology

[Exit criteria source (phase plan version, date), how deliverables were assessed (walkthrough, automated check, stakeholder sign-off), who participated in the review]

### B. Supporting Data

[Links to phase plan, deliverable artifacts, CI reports, defect log, and previous phase gate decisions for comparison]
