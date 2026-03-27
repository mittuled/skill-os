---
name: technical-feasibility-for-sales
description: >
  This skill assesses technical feasibility of a prospect's requirements against
  the product's current capabilities. Use when asked to evaluate whether a deal
  is technically viable, review prospect requirements, or assess integration
  complexity. Also consider before committing to a POC.
  Suggest when an AE is advancing a deal without technical validation.
department: sales
agent: solutions-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../proof-of-concept-runner/SKILL.md
  - ../../solutions-engineering-manager/technical-buyer-signal-extractor/SKILL.md
---

# technical-feasibility-for-sales

## Agent: Solutions Engineer

L3 solutions engineer (Nx) responsible for technical feasibility assessment for sales opportunities and proof-of-concept execution.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)

## Skill Description

Assesses technical feasibility of a prospect's requirements against the product's current capabilities, identifying gaps, workarounds, and roadmap dependencies before the deal advances.

## When to Use

- When a prospect's RFP or requirements document needs technical evaluation before the AE commits to a timeline or scope.
- When a deal involves custom integration, non-standard deployment, or edge-case usage that may exceed current product capabilities.
- When deciding whether to invest SE time in a POC by first validating that the core requirements are achievable.

## Workflow

1. **Requirements Intake**: Collect the prospect's technical requirements from RFP responses, discovery call notes, and direct technical conversations. Categorize each requirement as: functional (what the product must do), non-functional (performance, security, compliance), and integration (APIs, data flows, third-party systems). Deliverable: categorized requirements matrix.
2. **Capability Mapping**: Map each requirement to the product's current capabilities. Classify as: fully supported, partially supported (workaround available), on roadmap (with expected delivery date), or not supported. Deliverable: requirements-to-capability map with gap analysis.
3. **Gap Assessment**: For each gap, determine severity: dealbreaker (requirement is must-have with no workaround), manageable (workaround exists that meets the spirit of the requirement), or deferrable (nice-to-have that can be addressed post-sale). Deliverable: gap severity assessment with workaround documentation.
4. **Risk and Recommendation**: Produce a feasibility verdict: green (fully feasible), yellow (feasible with documented workarounds or roadmap dependencies), or red (dealbreaker gaps that cannot be addressed). Recommend whether to proceed, proceed with conditions, or disqualify. Deliverable: feasibility assessment with go/no-go recommendation.
5. **AE Briefing**: Brief the AE on the feasibility outcome, including which requirements to highlight in the proposal, which gaps to manage proactively with the prospect, and what commitments to avoid. Deliverable: AE briefing document with positioning guidance.

## Anti-Patterns

- **Optimistic feasibility**: Marking gaps as "on roadmap" without confirmed delivery dates or product commitment. *Why*: selling unconfirmed roadmap items creates post-sale implementation failures and erodes trust with both the customer and the internal team.
- **Binary assessment**: Classifying requirements as only "yes" or "no" without exploring workarounds or partial solutions. *Why*: many requirements can be met through configuration, integration, or workflow adjustments; binary assessment loses winnable deals unnecessarily.
- **Skipping the AE briefing**: Completing the assessment but not briefing the AE on how to position gaps and workarounds. *Why*: AEs without positioning guidance either overpromise to close or avoid discussing gaps, both of which create post-sale problems.

## Output

**On success**: Produces a categorized requirements matrix, capability map with gap analysis, gap severity assessment, feasibility verdict with go/no-go recommendation, and AE briefing document. Delivered to the AE and deal team.

**On failure**: Report which requirements could not be assessed (e.g., insufficient product documentation, ambiguous prospect requirements), what was evaluated, and recommended steps to complete the assessment.

## Related Skills

- [`proof-of-concept-runner`](../proof-of-concept-runner/SKILL.md) -- Executes POCs for deals that pass feasibility assessment.
- [`technical-buyer-signal-extractor`](../../solutions-engineering-manager/technical-buyer-signal-extractor/SKILL.md) -- Consumes feasibility gaps as technical buyer signals for Product.
