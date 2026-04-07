# Dependency Resolution Plan: [Project / Sprint Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Tech Lead / PR Reviewer |
| Project | [Project or sprint name] |
| Phase | [Phase N / Sprint N] |
| Skill | dependency-resolver |
| Status | [Draft / Active / Resolved] |

## Dependency Inventory

### External Dependencies (Blocking Unblockable Work)

| ID | Dependency | Type | Depends On | Blocking | Owner | ETA | Status |
|----|-----------|------|-----------|----------|-------|-----|--------|
| D-001 | [Dependency description] | [API / Data / Decision / Resource / Feature] | [Team / Person] | [Ticket IDs blocked] | [Name] | [Date] | [Waiting / In Progress / Resolved] |

### Internal Dependencies (Between Team Members or Services)

| ID | Dependency | From | To | Blocking | ETA | Status |
|----|-----------|------|----|----------|-----|--------|
| D-010 | [e.g., Auth service PR #123 must merge before payment flow] | [Auth team] | [Payments team] | [Ticket IDs] | [Date] | |

## Critical Path Analysis

**Critical path**: [List the chain of dependencies that determines the earliest completion date]

```
D-001 (resolved: Day 3)
  → Task A (starts Day 4, 2 days)
    → D-010 (resolved: Day 5)
      → Task B (starts Day 6, 3 days) → DONE Day 9 ← Earliest completion
```

**Float available**: [N days] — tasks not on the critical path can slip by this amount without affecting the end date.

## Resolution Strategies

### For Each Active Blocker

| Dependency ID | Strategy | Action | Owner | Due |
|--------------|----------|--------|-------|-----|
| D-001 | [Unblock / Parallel work / Scope reduction / Escalate] | [Specific action] | [Name] | [Date] |

**Strategy guide**:
- **Unblock**: Remove the dependency directly (implement the missing piece, make the decision)
- **Parallel work**: Restructure work so the blocked item runs in parallel with non-blocking work
- **Scope reduction**: Deliver a version that avoids the dependency; add dependency-requiring parts later
- **Mock / stub**: Build against a mock interface; integrate when the real dependency resolves
- **Escalate**: Dependency requires executive decision or cross-team commitment

## Escalation Register

Dependencies escalated beyond the tech lead's authority:

| ID | Dependency | Escalated To | Escalation Date | Decision Needed By | Status |
|----|-----------|-------------|----------------|-------------------|--------|
| D-xxx | [Description] | [VP / CTO / Cross-team lead] | [Date] | [Date] | [Pending] |

## Dependency Risk Assessment

| Dependency | Likelihood of Delay | Impact if Delayed | Mitigation |
|-----------|--------------------|--------------------|------------|
| D-001 | [H/M/L] | [H/M/L] | [Contingency or workaround] |

## Resolution Status Tracker

| Date | Dependency ID | Update | Resolved? |
|------|-------------|--------|-----------|
| [Date] | D-001 | [Status update] | [Yes/No] |

## Recommendations for Future Phases

[Systemic dependency issues to address in planning, not just execution:]

1. [e.g., "API contracts between services should be defined in Phase 0 to prevent D-001-type blockers"]
2. [e.g., "Shared infrastructure dependencies should be resolved in the first sprint of each phase"]
