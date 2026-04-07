# Design Backlog Population Template

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX/UI Designer] |
| Source Brief | [Link to product brief or feature spec] |
| Sprint / Cycle | [Target sprint or cycle] |
| Version | [1.0] |
| Status | [Draft / Ready for sprint planning] |

## Brief Summary

[1-2 sentences summarising the feature or initiative being broken into design backlog items. GUIDANCE: Include the user problem being solved and the scope of design work implied.]

## Design Ticket Template

[Use the following format for each backlog item. Duplicate the block per ticket.]

---

### [DES-XXX] [Ticket Title]

**Type**: [Discovery / Flow / Wireframe / Visual Design / Prototype / Handoff / Iteration]
**Priority**: [P0 Critical / P1 High / P2 Medium / P3 Low]
**Estimate**: [0.5d / 1d / 2d / 3d]
**Sprint**: [Target sprint]
**Assigned to**: [Designer name or TBD]
**Dependencies**: [e.g. DES-XXX must be complete first / Research findings needed first]

**Description**:
[Clear description of what the designer needs to produce. GUIDANCE: Start with "Design..." or "Create..." — imperative voice. Specify deliverable, not process.]

**Acceptance Criteria**:
- [ ] [e.g. Wireframes cover all in-scope screens at mid-fidelity]
- [ ] [e.g. Both mobile (375px) and desktop (1280px) breakpoints included]
- [ ] [e.g. Error and empty states designed for each screen]
- [ ] [e.g. Design reviewed and approved by PM before sprint ends]

**Design Notes**:
[Any constraints, references, or context relevant to this specific ticket. Link to Figma, research docs, or prior art.]

---

## Backlog Overview

[Summary table of all tickets generated from this brief.]

| Ticket ID | Title | Type | Priority | Estimate | Sprint | Status |
|-----------|-------|------|----------|----------|--------|--------|
| DES-001 | [e.g. User flow: checkout redesign] | Flow | P1 | 1d | Sprint 3 | To Do |
| DES-002 | [e.g. Wireframes: cart screen — all states] | Wireframe | P1 | 1.5d | Sprint 3 | To Do |
| DES-003 | [e.g. Wireframes: payment screen — all states] | Wireframe | P1 | 1d | Sprint 3 | To Do |
| DES-004 | [e.g. Visual design: cart screen hi-fi] | Visual Design | P1 | 2d | Sprint 4 | To Do |
| DES-005 | [e.g. Prototype: checkout flow for usability testing] | Prototype | P2 | 1d | Sprint 4 | To Do |
| DES-006 | [e.g. Handoff: cart + payment screens with specs] | Handoff | P2 | 0.5d | Sprint 5 | To Do |

**Total estimated effort**: [X days]
**Phases covered**: [Discovery / Definition / Production / Prototype / Handoff]

## Phase Sequencing

[Show the order in which tickets must be completed to maintain design phase discipline.]

```
Discovery tickets → Definition tickets (flows + wireframes) → Production tickets (hi-fi) → Prototype → Handoff
```

| Phase | Tickets in Phase | Gate |
|-------|-----------------|------|
| Discovery | [DES-00X, ...] | PM + design sign-off on problem statement |
| Definition | [DES-00X, ...] | Wireframe review approved |
| Production | [DES-00X, ...] | Visual design critique passed |
| Prototype | [DES-00X, ...] | Prototype ready for usability test |
| Handoff | [DES-00X, ...] | Engineering confirms spec is buildable |

## Coverage Check

[Confirm the backlog covers all required design work before submitting for sprint planning.]

- [ ] All in-scope screens have at least one wireframe ticket
- [ ] All in-scope screens have a hi-fi visual design ticket
- [ ] Mobile and desktop breakpoints covered per ticket
- [ ] Edge cases (empty, error, loading) included in scope
- [ ] Accessibility requirements noted in relevant tickets
- [ ] Handoff ticket included for engineering
- [ ] No ticket is more than 3 days — split any that are larger
