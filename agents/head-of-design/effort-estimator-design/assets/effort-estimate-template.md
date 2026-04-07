# Design Effort Estimate

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Head of Design] |
| Feature / Initiative | [Feature name or initiative title] |
| Product Brief Ref | [Link or ID] |
| Version | [1.0] |
| Status | [Draft / Reviewed / Approved] |

## Executive Summary

[2-3 sentences stating the total estimated design effort in days, the confidence level, and the key assumptions driving the estimate. GUIDANCE: Lead with the headline number — e.g. "Total design effort estimated at 12-16 days at medium confidence. Primary uncertainty is scope of responsive states and the number of edge-case flows requiring coverage."]

## Feature Scope

[Define what is included in this estimate.

GUIDANCE:
- Good: "Covers the checkout redesign flow: cart, address entry, payment selection, order confirmation (4 screens, 2 platforms — web + iOS)"
- Bad: "Checkout redesign"
- List all screens, flows, surfaces, and platforms explicitly. State any out-of-scope items.]

| Surface | Screen / Flow | Platform | Notes |
|---------|---------------|----------|-------|
| [e.g. Web] | [e.g. Cart screen] | [e.g. Desktop + Mobile] | [Any variant notes] |
| | | | |
| | | | |

## Design Phase Breakdown

[Estimate effort by design phase. Use the Double Diamond model as the reference phase structure.]

| Phase | Phase Description | Days (Low) | Days (High) | Key Deliverables |
|-------|------------------|-----------|------------|-----------------|
| Discovery | User research review, stakeholder interviews, problem definition | | | Research synthesis, problem statement |
| Definition | Flow mapping, information architecture, wireframes | | | User flows, wireframes, IA doc |
| Design | Visual design, component application, interaction specs | | | Hi-fi screens, design specs, component inventory |
| Prototype | Interactive prototype for testing or stakeholder review | | | Figma prototype, test plan |
| Review Cycles | Design critiques, stakeholder review rounds, revisions | | | Revised screens, review notes |
| Handoff | Redlines, spec documentation, dev Q&A | | | Figma handoff file, annotation doc |
| **Total** | | **[Sum]** | **[Sum]** | |

## Complexity Drivers

[List the factors that increase or decrease effort relative to a baseline similar-sized feature.]

| Driver | Impact | Rationale |
|--------|--------|-----------|
| [e.g. Multi-platform (web + iOS + Android)] | +[X] days | [Reason] |
| [e.g. Existing design system coverage high] | -[X] days | [Reason] |
| [e.g. High ambiguity — no existing research] | +[X] days | [Reason] |
| [e.g. Accessibility AA compliance required] | +[X] days | [Reason] |
| [e.g. Tight deadline — skip discovery] | Risk note | [Impact of skip] |

## Capacity & Timeline

[Map effort to team capacity and suggest a delivery window.]

| Designer | Allocation | Available Days / Sprint | Estimated Sprints Needed |
|----------|------------|------------------------|--------------------------|
| [Designer name or role] | [%] | [X days] | [X sprints] |
| | | | |

**Suggested start date**: [Date]
**Earliest completion (low estimate)**: [Date]
**Expected completion (high estimate)**: [Date]

## Assumptions & Constraints

[List assumptions that must hold for the estimate to be valid, and constraints that cap flexibility.]

**Assumptions:**
- [ ] [e.g. UX Research data from the previous discovery study is reusable and current]
- [ ] [e.g. Design system has components covering at least 70% of the required patterns]
- [ ] [e.g. No more than two stakeholder review cycles are required]
- [ ] [e.g. Dev Q&A support is budgeted at max 2 hours per sprint]

**Constraints:**
- [ ] [e.g. Must ship by [date] — forces parallel phase execution]
- [ ] [e.g. Only one designer is available for this feature]

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [e.g. Scope creep adds screens mid-flight] | Medium | +3-5 days | Lock scope with PM before design starts |
| [e.g. Research gaps require unplanned interviews] | Low | +2 days | Review existing research library before estimating |
| [e.g. Design system component gaps require new component work] | Medium | +3 days | Run component audit before Definition phase |

## Confidence Level

| Confidence | Definition | When to Use |
|------------|------------|-------------|
| High (±10%) | Scope fully defined, similar precedent, known team | Estimate for signed-off feature briefs |
| Medium (±25%) | Scope mostly defined, some unknowns, partial precedent | Estimate for roadmap sizing |
| Low (±50%) | Early concept, significant unknowns, no precedent | Estimate for annual planning or horizon items |

**This estimate confidence**: [High / Medium / Low]
**Primary uncertainty**: [State the main open question driving uncertainty]

## Approvals

| Role | Name | Date | Notes |
|------|------|------|-------|
| Head of Design | | | |
| Product Manager | | | |
| Engineering Lead | | | |
