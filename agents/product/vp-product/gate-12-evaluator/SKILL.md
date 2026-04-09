---
name: gate-12-evaluator
description: >
  This skill evaluates whether a product has met the defined gate criteria to
  proceed from one development phase to the next. Use when a product reaches a
  phase boundary (e.g., discovery-to-build, build-to-beta, beta-to-GA).
  Also consider when a stalled initiative needs a formal go/no-go decision to
  unblock resources. Suggest when milestone slippage or scope creep signals
  that a gate review is overdue.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "gate 12 evaluation"
  - "evaluate gate 12"
  - "gate review 12"
  - "launch gate check"
  - "phase gate evaluation"
---

# gate-12-evaluator

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Evaluates whether the product has met the gate criteria to proceed to the next phase.

## When to Use
- When a product reaches a phase transition point and requires a formal go/no-go decision
- When leadership needs an objective assessment of readiness before committing additional resources
- When scope creep or timeline slippage suggests the initiative may not meet exit criteria for the current phase
- When cross-functional dependencies (engineering, design, legal, compliance) need synchronized sign-off

## Workflow
1. **Retrieve gate criteria**: Pull the pre-defined exit criteria for the current phase from the PRD or phase-gate framework. Confirm the criteria are still relevant and complete. Deliverable: gate criteria checklist.
2. **Collect evidence**: Gather artefacts that demonstrate whether each criterion is met — demo recordings, test results, design-partner feedback, security review sign-offs, performance benchmarks, and documentation status. Deliverable: evidence inventory.
3. **Assess each criterion**: Evaluate every gate criterion as pass, conditional-pass, or fail. For conditional passes, document the specific conditions and deadlines for resolution. Deliverable: criterion-level assessment matrix.
4. **Identify blockers and risks**: Surface any unresolved blockers that would prevent a pass, and catalogue risks that could materialize in the next phase if the gate is passed conditionally. Deliverable: blocker and risk register.
5. **Convene the gate review**: Present the assessment to the gate review panel (typically VP Product, engineering lead, design lead, and any impacted GTM stakeholders). Facilitate the go/no-go/conditional-go decision. Deliverable: gate review meeting notes with decision.
6. **Document the outcome**: Record the decision, any conditions attached, owners for open items, and the timeline for the next gate. Distribute to all stakeholders. Deliverable: gate decision record.

## Anti-Patterns
- **Rubber-stamp gates**: Passing every gate review without rigorous evidence review because the team is eager to move forward. *Why*: Unearned phase transitions accumulate technical and market risk that compounds in later, more expensive phases.
- **Moving the goalposts**: Changing gate criteria during the review to justify a pass. *Why*: Retroactive criteria changes undermine the integrity of the phase-gate process and erode team trust.
- **Incomplete evidence**: Accepting verbal assurances instead of artefacts as proof of criterion completion. *Why*: Verbal claims are unreliable at scale; written evidence creates accountability and an audit trail.
- **Skipping conditional follow-up**: Granting a conditional pass and never revisiting the conditions. *Why*: Unresolved conditions become hidden debt that surfaces as launch blockers or post-GA incidents.

## Output
**On success**: A gate decision record containing the pass/conditional-pass/fail verdict for each criterion, the overall go/no-go decision, conditions and owners for any open items, and the timeline for the next phase gate.
**On failure**: Report which criteria were not met, the evidence gaps, what remediation is required, an estimated timeline to re-evaluate, and a recommendation on whether to pause, pivot, or de-scope.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
