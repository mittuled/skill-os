---
name: phase-planner
description: >
  This skill plans the activities, deliverables, and sequencing for each product delivery phase.
  Use when asked to create a phase plan, define what happens in discovery vs. build vs. launch,
  or structure a multi-phase initiative. Also consider when a team is conflating discovery and
  delivery work in the same sprint. Suggest when an initiative is approved but has no structured
  breakdown of what each phase will produce and when.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "plan phases"
  - "phase planning"
  - "project phases"
  - "define phases"
  - "phased roadmap"
---

# phase-planner

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Plans the activities, deliverables, and sequencing for each product delivery phase so that teams know exactly what to produce and when to transition between phases.

## When to Use
- When a new initiative has been approved and needs a structured breakdown into discovery, build, and launch phases before work begins
- When a team is mixing exploratory and execution work in the same sprint, causing thrash and unclear accountability
- When a phase transition is approaching and the team needs a concrete plan for the next phase that accounts for what was learned in the current one

## Workflow
1. **Define phase boundaries**: Identify the distinct phases the initiative requires (e.g., discovery, design, build, beta, launch). For each phase, state the entry criteria (what must be true to start) and exit criteria (what must be true to advance). Deliverable: phase list with entry/exit criteria.
2. **Enumerate activities per phase**: For each phase, list the activities that must occur -- customer interviews, design reviews, engineering spikes, QA passes, stakeholder sign-offs. Assign each activity to a responsible role. Deliverable: activity matrix organized by phase and owner.
3. **Define deliverables per phase**: Specify the concrete artifacts each phase must produce (e.g., discovery produces a validated problem statement and user journey map; build produces a deployed feature behind a flag). Deliverable: deliverables checklist per phase.
4. **Sequence and estimate**: Order phases and activities accounting for dependencies. Estimate duration per phase using historical velocity or analogous projects. Identify the critical path. Deliverable: phase timeline with duration estimates and dependency arrows.
5. **Identify phase risks**: For each phase, name the top 1-2 risks that could delay transition to the next phase. Define a mitigation action for each. Deliverable: risk register appended to the phase plan.
6. **Review with cross-functional leads**: Walk engineering, design, and stakeholders through the plan. Confirm that phase boundaries match team capacity and that deliverables are achievable within the estimated windows. Deliverable: approved phase plan or documented revision requests.

## Anti-Patterns
- **Waterfall disguised as phases**: Creating phases that are sequential handoffs (PM writes spec, design mocks, eng builds) with no feedback loops between them. *Why*: This eliminates the learning that phases are meant to produce; late-stage discoveries force costly rework.
- **Phase without exit criteria**: Allowing a phase to end on a calendar date rather than demonstrated outcomes. *Why*: Calendar-driven transitions advance incomplete work into the next phase, compounding quality debt.
- **Over-phasing**: Breaking a two-sprint feature into five phases with formal gates. *Why*: Ceremony overhead exceeds the coordination benefit; the team spends more time in reviews than building.
- **Ignoring carry-over**: Planning the next phase without accounting for incomplete work or open questions from the current phase. *Why*: Unaddressed carry-over silently inflates the next phase's scope and erodes timeline confidence.

## Output
**On success**: A phase plan document containing phase definitions with entry/exit criteria, activity matrix, deliverables checklist, timeline with estimates, and risk register -- formatted for use in a project tracker or initiative brief.

**On failure**: Report which phases could not be fully planned (unclear scope, missing capacity data, unresolved dependencies), what was attempted, and recommend specific decisions or inputs needed to complete the plan.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
