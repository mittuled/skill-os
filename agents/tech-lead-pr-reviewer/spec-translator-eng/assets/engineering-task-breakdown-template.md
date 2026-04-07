# Engineering Task Breakdown

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Lead / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | spec-translator-eng |

## Executive Summary

[2-3 sentences stating the spec being translated, the total number of tasks generated, and any blocking open questions that must be resolved before work can begin.
GUIDANCE: Lead with the scope headline. Example: "This breakdown translates the Notifications v2 PRD into 14 engineering tasks across frontend, backend, and infrastructure workstreams. Three open questions require product clarification before Sprint 12 planning. No external dependencies block immediate parallel starts."]

## Open Questions

[List every ambiguity or gap identified during spec parsing. Each item must have an owner and a resolution deadline.

GUIDANCE:
- Good: "Q1: The spec says 'support all notification types' but does not enumerate them. Owner: PM Sarah. Needed by: 2026-04-10 for sprint planning."
- Bad: "Unclear what notification types are supported"
- Format: Numbered list with owner and deadline]

| # | Question | Spec Section | Owner | Needed By |
|---|----------|-------------|-------|-----------|
| 1 | [Specific ambiguity] | [Section/page] | [Name] | [YYYY-MM-DD] |

## Task Breakdown

[All engineering tasks produced by this translation. Group by workstream. Each task must have all five required fields.

GUIDANCE:
- Good: Every task has description, acceptance criteria, estimate, and dependency annotations
- Bad: Tasks with only a title and "TBD" for acceptance criteria
- Format: One subsection per task, grouped by workstream (Backend / Frontend / Infrastructure / Testing)]

### Backend

#### [BE-01] [Task Title]

**Description**: [2-5 sentences describing what must be built, why, and any constraints]

**Acceptance Criteria**:
- Given [precondition], when [action], then [outcome]
- Given [precondition], when [action], then [outcome]

**Size**: [S / M / L / XL] ([N] story points)

**Dependencies**: [DEPENDS-ON: BE-XX / BLOCKS: BE-XX / None]

---

### Frontend

#### [FE-01] [Task Title]

**Description**: [2-5 sentences]

**Acceptance Criteria**:
- Given [precondition], when [action], then [outcome]

**Size**: [S / M / L / XL] ([N] story points)

**Dependencies**: [DEPENDS-ON: BE-XX / None]

---

### Infrastructure

#### [INF-01] [Task Title]

**Description**: [2-5 sentences]

**Acceptance Criteria**:
- Given [precondition], when [action], then [outcome]

**Size**: [S / M / L / XL] ([N] story points)

**Dependencies**: [None / EXT-DEP: DevOps team by YYYY-MM-DD]

---

### Testing

#### [TEST-01] [Task Title]

**Description**: [Test type (unit/integration/E2E), what is being tested, coverage expectation]

**Acceptance Criteria**:
- All [unit/integration/E2E] tests pass in CI
- Coverage for [module/feature] meets the [N%] threshold

**Size**: [S / M / L] ([N] story points)

**Dependencies**: [DEPENDS-ON: BE-XX, FE-XX]

## Dependency Summary

[Visual or tabular representation of key sequencing constraints.

GUIDANCE:
- Good: Table showing which tasks block which, highlighting the critical path
- Bad: Omitting this section because "engineers will figure it out"
- Format: Table with blocker → blocked relationship]

| Blocker Task | Blocked Task(s) | Reason |
|-------------|----------------|--------|
| [BE-01] | [FE-01, FE-02] | [Frontend requires API endpoint to exist] |
| [INF-01] | [BE-01] | [Service requires infrastructure provisioned first] |

## Recommendations

[Prioritized list of actions before sprint planning.
GUIDANCE: Focus on open questions and sizing risks]

- **P1**: [Resolve open question that blocks task creation or estimation]
- **P2**: [Split or re-estimate tasks flagged as > 8 points]
- **P3**: [Identify parallel start candidates to compress schedule]

## Appendices

### A. Methodology

[Source spec version reviewed, tagging approach used, estimation method (team sizing session, reference tasks, planning poker), stakeholders in the review session]

### B. Supporting Data

[Link to source spec, any referenced ADRs, existing similar tasks used as size reference points]
