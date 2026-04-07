# Framework: backlog-populator-eng

Guides the decomposition of approved specifications into well-structured engineering backlog items using consistent task definition standards.

## Task Definition Standard

Every backlog item must contain these fields:

| Field | Required | Format |
|-------|----------|--------|
| Title | Yes | Verb-noun phrase (e.g., "Implement user authentication endpoint") |
| Description | Yes | 2-5 sentences covering what, why, and technical approach |
| Acceptance Criteria | Yes | Given/When/Then or checklist format; minimum 2 criteria per task |
| Size Estimate | Yes | T-shirt (XS/S/M/L/XL) or story points (1/2/3/5/8/13) |
| Priority | Yes | P1 (critical path) / P2 (important) / P3 (nice-to-have) |
| Dependencies | Yes | List of blocking task IDs or "none" |
| Source Spec Reference | Yes | Link to the spec section this task implements |
| Labels | Recommended | Layer (frontend/backend/infra/test), type (feature/bug/chore) |

## Decomposition Rules

1. **Single-sprint completable**: No task should exceed one sprint. If it does, split further.
2. **Independently testable**: Each task must be verifiable in isolation without requiring other tasks to be done first (unless explicitly dependency-linked).
3. **Layer-aligned**: Separate frontend, backend, infrastructure, and testing tasks rather than bundling them into full-stack tasks.
4. **Edge-case explicit**: If the spec mentions edge cases, create tasks or acceptance criteria for them explicitly.
5. **Non-functional coverage**: Create dedicated tasks for performance testing, security hardening, observability setup, and documentation.

## Dependency Tagging Convention

| Tag | Meaning |
|-----|---------|
| `blocks: [TASK-ID]` | This task must complete before the referenced task can start |
| `blocked-by: [TASK-ID]` | This task cannot start until the referenced task completes |
| `external: [TEAM/SERVICE]` | This task depends on a deliverable from another team |
| `infra: [RESOURCE]` | This task requires infrastructure provisioning |

## Priority Framework

| Priority | Definition | Scheduling Rule |
|----------|-----------|-----------------|
| P1 | On the critical path; blocks other tasks | Must be in the first sprint that has capacity |
| P2 | Important but not blocking; contributes to milestone | Schedule within the phase |
| P3 | Desirable but deferrable; typically polish or optimization | Schedule if capacity allows |

## Quality Checklist

Before marking backlog population as complete:

- [ ] Every spec requirement maps to at least one task
- [ ] Every task maps back to a spec section
- [ ] No task exceeds one sprint in estimated size
- [ ] All cross-team dependencies flagged with owners
- [ ] Critical path tasks identified and marked P1
- [ ] At least one task covers observability setup
- [ ] At least one task covers documentation
