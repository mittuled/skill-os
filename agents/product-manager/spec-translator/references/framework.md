# Framework: Spec Translation

## Core Model

Systematic decomposition of product specifications into engineering-ready tasks with acceptance criteria, edge cases, and technical context. Each task must be independently estimable, buildable, and testable.

## Task Decomposition Rules

1. **Single responsibility**: One task = one behaviour or capability
2. **Independently deliverable**: Task can be completed and verified without other tasks in the same batch
3. **Estimable**: Engineering can assign a point estimate or hour range
4. **Testable**: Every task has acceptance criteria that QA can verify

## Acceptance Criteria Format (Given/When/Then)

```
Given [precondition / context]
When [action / trigger]
Then [expected outcome / observable result]
```

Every task requires:
- 2-5 acceptance criteria
- At least 1 edge case (boundary condition, unusual input, concurrent access)
- At least 1 negative case (what happens when things go wrong)

## Technical Context Template

For each task, document:
- **Affected APIs**: Which endpoints are created, modified, or consumed
- **Data model changes**: New fields, modified schemas, migrations required
- **Integration points**: External services, internal services, or shared libraries involved
- **Known constraints**: Rate limits, performance budgets, backwards compatibility requirements
- **Cross-team dependencies**: Tasks that require coordination with other teams (flagged with team name)

## Spec-to-Task Traceability

| Task ID | Task Title | Spec Section | Acceptance Criteria Count | Edge Cases | Technical Dependencies |
|---------|-----------|-------------|--------------------------|------------|----------------------|
| T-001 | ... | PRD Section 2.1 | 4 | 2 | API v2, User service |

## Quality Checklist

- [ ] Every spec behaviour maps to at least one task
- [ ] No task contains implementation prescriptions (says "what" not "how")
- [ ] All tasks have 2-5 acceptance criteria in Given/When/Then format
- [ ] Edge cases and error states are covered
- [ ] Engineering lead confirms tasks are estimable
- [ ] Cross-team dependencies are flagged
