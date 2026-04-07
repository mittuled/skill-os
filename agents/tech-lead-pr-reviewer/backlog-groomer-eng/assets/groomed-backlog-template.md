# Groomed Backlog: [Sprint / Phase Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Tech Lead / PR Reviewer |
| Sprint / Phase | [Sprint N / Phase N] |
| Grooming Session | [Date and participants] |
| Skill | backlog-groomer-eng |
| Status | [Draft / Groomed / Sprint-Ready] |

## Grooming Summary

**Items reviewed**: [N total]
**Items sprint-ready**: [N] (all acceptance criteria defined, estimated, unblocked)
**Items needs more work**: [N] (requires design, decisions, or more detail)
**Items deferred**: [N] (moved to future sprint or icebox)
**Items closed / won't do**: [N]

## Sprint-Ready Items

Items that meet the Definition of Ready (DoR) and can be pulled into the next sprint:

### DoR Checklist

An item is sprint-ready when:
- [ ] User story written in standard format (As a / I want / So that)
- [ ] Acceptance criteria written with specific, testable conditions
- [ ] Story points estimated by the team (consensus, not solo)
- [ ] Dependencies identified and either resolved or explicitly managed
- [ ] UI/UX designs available and approved (for frontend work)
- [ ] API contract defined (for backend work requiring integration)
- [ ] Security considerations noted (or confirmed not applicable)
- [ ] No open blocking questions

### Sprint-Ready Backlog

| ID | Title | Type | Points | Priority | Dependencies | Notes |
|----|-------|------|--------|----------|-------------|-------|
| [TICKET-001] | [User story title] | [Feature/Bug/Debt] | [3] | [P1] | [None / Ticket IDs] | |
| [TICKET-002] | | | | | | |

**Total sprint-ready points**: [X pts]
**Recommended sprint commitment**: [X pts] (based on team velocity of [Y] pts)

## Needs More Work

Items that cannot be pulled until issues are resolved:

| ID | Title | Blocking Issue | Owner | Target Resolution |
|----|-------|---------------|-------|------------------|
| [TICKET-010] | [Title] | [Missing design / Open technical decision / Unclear requirements] | [Role] | [Date] |

## Story Card Examples (for sprint-ready items)

### [TICKET-001]: [User Story Title]

**Type**: [Feature / Bug / Tech Debt / Spike]
**Priority**: [P1 / P2 / P3]
**Points**: [X]

**User Story**
As a [user role], I want [capability], so that [benefit].

**Acceptance Criteria**
- [ ] Given [context], when [action], then [expected outcome]
- [ ] Given [context], when [action], then [expected outcome]
- [ ] Error case: Given [error condition], then [error is handled gracefully with message Y]
- [ ] Edge case: [Describe edge case and expected behavior]

**Technical Notes**
[Any implementation guidance, constraints, or design decisions that should inform implementation. Not implementation instructions — just constraints.]

**Definition of Done** (in addition to team standard DoD):
- [ ] [Feature-specific completion criteria]

---

## Deferred Items

Items moved to future sprints with rationale:

| ID | Title | Deferred To | Reason |
|----|-------|------------|--------|
| [TICKET-020] | [Title] | [Sprint N+2 / Icebox] | [Deprioritized / Blocked by external / Scope too large — split required] |

## Grooming Action Items

| Action | Owner | Due |
|--------|-------|-----|
| [Write acceptance criteria for TICKET-010] | [Product / Engineering] | [Date] |
| [Get design sign-off for TICKET-011] | [Design] | [Date] |
| [Spike: investigate auth approach for TICKET-012] | [Backend] | [Date / Points: 2] |
