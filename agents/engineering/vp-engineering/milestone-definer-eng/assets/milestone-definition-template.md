# Milestone Definition: [Project Name] — Phase [N]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | VP Engineering |
| Project | [Project name] |
| Phase | [Phase N] |
| Skill | milestone-definer-eng |
| Status | [Draft / Approved] |

## Phase Goal

**One-sentence objective**: [What must be true when this phase is complete?]

**Why this milestone matters**: [Business or technical outcome unlocked when phase completes]

## Milestones

### Milestone 1: [Name]

| Field | Value |
|-------|-------|
| Target date | [YYYY-MM-DD] |
| Owner | [Team or lead] |
| Type | [External — customer-visible / Internal — team gate] |

**Exit criteria** (all must be true to call this milestone complete):
- [ ] [Specific, verifiable condition 1]
- [ ] [Specific, verifiable condition 2]
- [ ] [Test coverage ≥ 80% for affected code]
- [ ] [Staging validation passed]

**Risk to milestone**: [Top risk and mitigation]

---

### Milestone 2: [Name]

| Field | Value |
|-------|-------|
| Target date | [YYYY-MM-DD] |
| Owner | [Team] |
| Type | [External / Internal] |

**Exit criteria**:
- [ ] [Condition 1]
- [ ] [Condition 2]

---

### Milestone 3: Phase Complete / Go-Live Gate

| Field | Value |
|-------|-------|
| Target date | [YYYY-MM-DD] |
| Owner | VP Engineering |
| Type | External — production launch |

**Exit criteria**:
- [ ] All prior milestones complete
- [ ] Production readiness review passed
- [ ] Runbooks complete and reviewed
- [ ] Monitoring and alerting active
- [ ] Rollback plan documented and tested
- [ ] Go-live approver sign-off obtained

## Milestone Dependency Map

```
Milestone 1 (Date 1) → Milestone 2 (Date 2) → Milestone 3 / Phase Complete (Date 3)
```

**Parallel tracks** (if any):
- [Track A: milestones that can proceed in parallel with Track B]

## Slip Thresholds

| Milestone | Acceptable Slip | Action if Exceeded |
|-----------|----------------|-------------------|
| Milestone 1 | ≤ 3 days | Team-level recovery plan |
| Milestone 2 | ≤ 5 days | Scope reduction review |
| Phase Complete | 0 days | Executive escalation + scope / date negotiation |
