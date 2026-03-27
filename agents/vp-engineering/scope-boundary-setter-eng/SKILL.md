---
name: scope-boundary-setter-eng
description: >
  This skill defines and enforces scope boundaries to prevent engineering scope creep. Use when
  asked to set scope limits, define what is in and out of scope, or push back on unplanned work
  requests. Also consider when mid-phase feature requests arrive without formal change control.
  Suggest when scope is expanding without corresponding timeline or resource adjustments.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: simple
related-skills:
  - ../../vp-engineering/spec-intake-review/SKILL.md
  - ../../tech-lead-pr-reviewer/phase-scope-adjuster-eng/SKILL.md
---

# scope-boundary-setter-eng

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Defines and enforces engineering scope boundaries to prevent uncontrolled scope creep and protect delivery timelines.

## When to Use

- When a delivery is being planned and in-scope vs. out-of-scope items need explicit documentation.
- When mid-phase requests arrive that were not part of the original specification.
- When velocity data suggests the team is working on items outside the agreed scope.

## Workflow

1. **Define scope boundary**: Document what is in scope and out of scope for the delivery, referencing the approved spec and phase plan. Deliverable: scope boundary document with explicit inclusion/exclusion list.
2. **Establish change control**: Define the process for requesting scope changes -- who can request, who approves, and what impact assessment is required. Deliverable: change control process definition.
3. **Enforce boundaries**: When new requests arrive, evaluate against the boundary document. Approve, defer to a future phase, or reject with rationale. Deliverable: scope change decision log.

## Anti-Patterns

- **Soft boundaries**: Defining scope verbally or vaguely, making it easy to reinterpret. *Why*: ambiguous boundaries invite gradual expansion that no single addition seems to justify blocking.
- **Blanket rejection**: Refusing all scope changes regardless of merit. *Why*: rigid boundaries that ignore critical bug fixes or security issues create worse outcomes than controlled flexibility.

## Output

**On success**: Produces a scope boundary document listing in-scope and out-of-scope items, a change control process, and a scope change decision log. Delivered to all delivery stakeholders.

**On failure**: Report which scope boundaries could not be clearly defined due to ambiguous requirements, and recommend what must be clarified by product or design.

## Related Skills

- [`spec-intake-review`](../../vp-engineering/spec-intake-review/SKILL.md) -- spec review establishes the initial scope that this skill protects.
- [`phase-scope-adjuster-eng`](../../tech-lead-pr-reviewer/phase-scope-adjuster-eng/SKILL.md) -- handles mid-phase scope adjustments within the boundaries set here.
