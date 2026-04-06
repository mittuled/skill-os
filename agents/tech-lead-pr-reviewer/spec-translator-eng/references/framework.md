# Framework: spec-translator-eng

Defines the methodology for translating product specifications into engineering tasks with precise acceptance criteria and dependency annotations.

## Decomposition Model

### Spec Parsing Taxonomy

Tag every requirement in the spec before generating tasks:

| Tag | Meaning | Task Type Generated |
|-----|---------|-------------------|
| `[FUNC]` | Functional requirement | Feature task (FE/BE/infra) |
| `[NFR]` | Non-functional requirement | Performance, security, or reliability task |
| `[EDGE]` | Edge case or error state | Acceptance criteria addition + test task |
| `[OPEN]` | Ambiguous or missing information | Clarification required before task creation |
| `[DEP]` | External dependency | Dependency annotation on affected task |

### Task Anatomy

Every engineering task must contain all five fields before it is considered complete:

| Field | Description | Example |
|-------|-------------|---------|
| **Title** | One-line summary (verb + noun) | "Add pagination to /users endpoint" |
| **Description** | 2–5 sentences: what, why, constraints | "The /users endpoint returns all records. Add cursor-based pagination with `limit` (max 100) and `cursor` parameters to support the mobile client's scroll behavior." |
| **Acceptance Criteria** | Testable given/when/then statements | "Given a request with limit=10, when 200 records exist, then the response includes exactly 10 records and a `next_cursor` field" |
| **Size Estimate** | Story points or t-shirt (S/M/L/XL) | M (3 points) |
| **Dependencies** | Upstream tasks this depends on | `BE-42: Auth middleware must merge before this lands` |

### Decomposition Rules

1. **One deployable unit per task**: If a task cannot be merged and deployed independently, split it further.
2. **One team per task**: Cross-team work must be separate tasks with an explicit handoff dependency.
3. **Max 8 points per task**: Tasks sized > 8 points are candidates for further decomposition.
4. **Test tasks are first-class**: Unit tests, integration tests, and E2E tests are separate tasks with their own acceptance criteria.

## Given/When/Then Template

```
Given [system state or precondition],
When [user or system action],
Then [observable, testable outcome].
```

**Multiple conditions example**:
```
Given a logged-in user with role "admin",
  AND the feature flag "new-dashboard" is enabled,
When the user navigates to /dashboard,
Then the new dashboard layout renders within 500ms,
  AND the legacy dashboard is not visible,
  AND the page title reads "Dashboard (Beta)".
```

## Dependency Annotation Types

| Type | Annotation Format | Meaning |
|------|------------------|---------|
| Hard block | `BLOCKS: [task-id]` | This task cannot start until the referenced task is complete |
| Hard dependency | `DEPENDS-ON: [task-id]` | The current task requires the referenced task to complete first |
| Soft dependency | `PREFERS-AFTER: [task-id]` | Better to sequence after, but not strictly required |
| External | `EXT-DEP: [team/system] by [date]` | Blocked on a team or third party outside this project |

## Review Checklist

Before handing the task breakdown to product for approval:
- [ ] Every `[FUNC]` requirement has at least one task
- [ ] Every `[EDGE]` requirement has an acceptance criterion on a relevant task
- [ ] All `[OPEN]` items are listed with the named owner responsible for resolution
- [ ] No task exceeds 8 story points
- [ ] All cross-team dependencies have named owners
- [ ] Test tasks exist for every new user-facing feature
