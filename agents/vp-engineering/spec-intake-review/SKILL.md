---
name: spec-intake-review
description: >
  This skill reviews incoming feature specifications to assess completeness and readiness before
  engineering work begins. Use when asked to review a PRD, evaluate a spec for engineering handoff,
  or check if a feature request is ready for development. Also consider when product submits a new
  spec to the engineering intake queue. Suggest when engineering is about to start work on an
  unreviewed specification.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../vp-engineering/scope-boundary-setter-eng/SKILL.md
  - ../../vp-engineering/backlog-populator-eng/SKILL.md
---

# spec-intake-review

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Reviews incoming feature specifications to assess completeness, technical feasibility, and readiness for engineering execution.

## When to Use

- When a product specification or PRD is submitted to engineering for implementation.
- When a previously rejected spec has been revised and resubmitted.
- When an urgent request bypasses normal intake and needs rapid feasibility and completeness review.

## Workflow

1. **Completeness check**: Verify the spec contains user stories or jobs-to-be-done, acceptance criteria, success metrics, edge cases, and non-functional requirements (performance, security, accessibility). Deliverable: completeness scorecard.
2. **Feasibility triage**: Assess whether the spec is technically feasible within stated constraints. Flag items requiring spikes, architecture changes, or third-party dependencies. Deliverable: feasibility notes with blocker flags.
3. **Ambiguity identification**: Highlight vague requirements, contradictory statements, or missing decisions that would force engineers to guess. Deliverable: list of open questions for product.
4. **Scope assessment**: Confirm the spec defines clear boundaries -- what is included and excluded. Deliverable: scope clarity rating.
5. **Verdict**: Accept the spec for engineering planning, return it for revision with specific feedback, or escalate if it requires cross-functional alignment. Deliverable: intake decision with action items.

## Anti-Patterns

- **Accepting incomplete specs**: Letting vague specs through to avoid confrontation with product. *Why*: ambiguous specs cause rework, scope disputes, and engineering frustration that costs more than the review delay.
- **Gold-plating the review**: Demanding perfection in the spec beyond what engineering needs to start planning. *Why*: over-scrutiny creates bottlenecks and signals that engineering is a blocker rather than a partner.
- **Skipping non-functional requirements**: Reviewing only feature behavior without checking performance, security, and observability requirements. *Why*: missing NFRs surface late as production issues that are expensive to retrofit.

## Output

**On success**: Produces an intake review document containing the completeness scorecard, feasibility notes, open questions, scope assessment, and a verdict (accepted / returned for revision / escalated). Delivered to product and engineering planning teams.

**On failure**: Report which review criteria could not be assessed (e.g., missing design mockups, undefined integration points), what is needed to complete the review, and a recommended timeline.

## Related Skills

- [`scope-boundary-setter-eng`](../../vp-engineering/scope-boundary-setter-eng/SKILL.md) -- scope boundaries are informed by the intake review findings.
- [`backlog-populator-eng`](../../vp-engineering/backlog-populator-eng/SKILL.md) -- accepted specs flow into backlog population.
