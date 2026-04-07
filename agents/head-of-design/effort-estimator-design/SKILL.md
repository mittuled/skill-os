---
name: effort-estimator-design
description: >
  This skill estimates design effort required for features and initiatives. Use when asked
  to scope design work, provide time estimates for a product brief, or assess design team
  capacity against a roadmap. Also consider when sprint planning requires design effort
  inputs. Suggest when a product manager is sizing a feature without design representation.
department: design
agent: head-of-design
version: 1.0.0
complexity: simple
related-skills: []
---

# effort-estimator-design

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)

## Skill Description

Estimates design effort required for features and initiatives by decomposing work into design phases, accounting for complexity, review cycles, and team capacity.

## When to Use

- When a product brief or feature request needs a design effort estimate for roadmap planning.
- When sprint or cycle planning requires design capacity commitments.
- When leadership asks for a resource plan to staff a new initiative.

## Workflow

1. **Decompose the design scope**: Break the feature into design deliverables -- user flows, wireframes, visual design, prototypes, design system updates, handoff specs. Use the deliverable inventory in the [estimation framework](references/estimation-framework.md) as a checklist. Deliverable: design work breakdown structure.
2. **Assess complexity factors**: Evaluate each deliverable for novel patterns vs. existing component reuse, number of responsive breakpoints, interaction complexity, accessibility requirements, and expected review cycles. Apply complexity multipliers and review buffers from the [estimation framework](references/estimation-framework.md). Deliverable: complexity assessment per deliverable.
3. **Estimate effort**: Assign T-shirt size or hour ranges to each deliverable based on complexity and historical team velocity. Include buffer for feedback incorporation and review rounds. Declare a confidence level (high/medium/low) per the framework's confidence criteria. Deliverable: effort estimate table with confidence level.
4. **Communicate estimate**: Present the estimate to product and engineering with assumptions, risks, and dependencies explicitly stated. Deliverable: shared estimate document.

## Anti-Patterns

- **Estimating without decomposition**: Giving a single number for an entire feature without breaking it into design phases. *Why*: monolithic estimates hide risk and make it impossible to track progress or identify where delays originate.
- **Ignoring review cycles**: Estimating only production time and omitting design review, stakeholder feedback, and iteration rounds. *Why*: review and revision typically consume 30-50% of total design time; excluding them guarantees the estimate is wrong.
- **Anchoring to engineering timelines**: Compressing design estimates to fit a predetermined engineering schedule rather than stating true effort. *Why*: underestimated design work leads to cut corners, skipped states, and accessibility gaps that cost more to fix post-launch.

## Output

**On success**: Produces a design effort estimate document containing work breakdown, per-deliverable complexity and effort, total estimate with confidence level, assumptions, and risks. Delivered to product and engineering leads.

**On failure**: Report which parts of the scope could not be estimated, the missing information (unclear requirements, undefined user flows, missing design system inventory), and what is needed to produce a reliable estimate.

## Related Skills

- [`spec-translator-design`](../spec-translator-design/SKILL.md) -- Translating specs into design briefs is a prerequisite for accurate effort estimation.
- [`iteration-prioritiser-design`](../iteration-prioritiser-design/SKILL.md) -- Effort estimates inform prioritization of the design iteration backlog.
