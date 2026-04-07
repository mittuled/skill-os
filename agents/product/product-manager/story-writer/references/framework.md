# Framework: Story Writing

## Core Model

User stories written in standard format with acceptance criteria in Given/When/Then, designed for independent estimation, implementation, and testing.

## Story Statement Format

```
As a [specific persona],
I want [single atomic goal],
so that [measurable business outcome].
```

## Persona Specificity

| Level | Example | Quality |
|-------|---------|---------|
| Too vague | "As a user" | Reject: no targeting possible |
| Acceptable | "As a free-tier user" | OK: identifies segment |
| Ideal | "As a free-tier user who has completed onboarding" | Best: identifies segment and state |

## Acceptance Criteria Rules

Write 3-7 criteria per story using Given/When/Then:

1. **Happy path** (required): The primary success scenario
2. **Edge cases** (min 1): Boundary conditions, empty states, maximum values
3. **Error states** (min 1): Network failure, invalid input, permission denied
4. **Accessibility** (when applicable): Screen reader, keyboard navigation, contrast

## Story Sizing Checklist

A story is ready for estimation when:
- [ ] Story statement follows As a / I want / So that format
- [ ] Persona is specific enough to guide design decisions
- [ ] Goal is atomic (one action; if compound, split into multiple stories)
- [ ] Business outcome is measurable or at least observable
- [ ] 3-7 acceptance criteria exist in Given/When/Then format
- [ ] At least 1 edge case and 1 error state are covered
- [ ] Design references (mockups, wireframes) are linked if applicable
- [ ] Technical constraints and dependencies are documented

## Story Splitting Heuristics

When a story is too large (>8 SP), split by:
1. **Workflow steps**: Each step in a multi-step flow becomes a story
2. **Data variations**: Handle one data type per story (e.g., text input, then file upload)
3. **Business rules**: Each rule becomes a separate story
4. **Platform**: Mobile vs. desktop vs. API
5. **CRUD operations**: Create, read, update, delete as separate stories
