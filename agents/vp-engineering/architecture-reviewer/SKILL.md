---
name: architecture-reviewer
description: >
  This skill reviews proposed system architectures for soundness, scalability, and alignment with
  engineering standards. Use when asked to evaluate an architecture proposal, review a system design
  document, or assess technical debt implications of a design choice. Also consider when a new ADR
  is submitted for approval. Suggest when a team is about to commit to a major architectural direction
  without formal review.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../tech-architect/architecture-designer/SKILL.md
  - ../../tech-architect/technical-feasibility-check/SKILL.md
triggers:
  - "review this architecture"
  - "evaluate this system design"
  - "is this architecture sound"
  - "check the design doc"
---

# architecture-reviewer

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Reviews proposed system architectures for soundness, scalability, and alignment with organizational engineering standards.

## When to Use

- When a Tech Architect submits a new architecture design or ADR for leadership sign-off.
- When a proposed system change crosses service boundaries or introduces a new runtime dependency.
- When an existing architecture is being reconsidered due to scaling bottlenecks, reliability incidents, or acquisition of new infrastructure.

## Workflow

1. **Gather context**: Collect the architecture proposal, ADR, or design document along with the product requirements it addresses. Deliverable: a review checklist scoped to the proposal.
2. **Assess structural soundness**: Evaluate component boundaries, data flow paths, failure domains, and blast radius. Verify the design follows separation of concerns and avoids single points of failure. Deliverable: annotated architecture assessment with structural risk findings.
3. **Evaluate scalability posture**: Check horizontal and vertical scaling assumptions against projected load. Verify capacity planning accounts for 3x headroom beyond stated SLOs. Deliverable: scalability assessment with identified ceilings.
4. **Check standards alignment**: Confirm the proposal adheres to existing technology radar choices, observability requirements (structured logging, metrics, distributed tracing), and security posture (threat model present, auth flows documented). Deliverable: standards compliance checklist.
5. **Identify operational risks**: Assess deployment complexity, rollback strategy, data migration paths, and on-call burden. Deliverable: operational risk summary.
6. **Render verdict**: Approve, request changes, or reject with explicit rationale tied to principles. Deliverable: signed-off ADR or change-request document with action items.

## Anti-Patterns

- **Rubber-stamping**: Approving architectures without verifying observability, security, or failure-mode coverage. *Why*: unreviewed designs accumulate hidden operational debt that surfaces as production incidents.
- **Scope overreach**: Redesigning the architecture instead of reviewing it. *Why*: the reviewer role is to validate, not to architect; overreach delays delivery and undermines the architect's ownership.
- **Bias toward novelty**: Favoring new technologies without evidence they solve a problem existing tools cannot. *Why*: every novel dependency multiplies onboarding cost, debugging surface, and operational risk.

## Output

**On success**: Produces an architecture review document containing the verdict (approved / changes-requested / rejected), annotated risk findings, standards compliance status, and any required follow-up actions. Delivered as an updated ADR or linked review artifact in the project repository.

**On failure**: Report which review criteria could not be evaluated (e.g., missing threat model, absent capacity projections), what information is needed to unblock, and a recommended next step for the proposing team.

## Related Skills

- [`architecture-designer`](../../tech-architect/architecture-designer/SKILL.md) -- produces the architecture proposals this skill reviews.
- [`technical-feasibility-check`](../../tech-architect/technical-feasibility-check/SKILL.md) -- feasibility assessment often precedes or feeds into architecture review.
