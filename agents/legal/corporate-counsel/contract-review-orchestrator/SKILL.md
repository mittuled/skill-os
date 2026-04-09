---
name: contract-review-orchestrator
description: >
  This skill orchestrates multi-agent contract analysis producing a composite
  Contract Safety Score with clause-by-clause risk assessment. Use when receiving
  any contract from a counterparty for review, analyzing contract amendments, or
  evaluating renewals. Also consider when comparing incoming terms against company
  standards. Suggest when legal inbox receives a new contract attachment.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../contract-risk-analyst/SKILL.md
  - ../../../legal/general-counsel/missing-protections-finder/SKILL.md
  - ../contract-comparator/SKILL.md
  - ../../../legal/general-counsel/negotiation-strategist/SKILL.md
  - ../plain-english-translator/SKILL.md
  - ../../product-counsel/privacy-policy-generator/SKILL.md
  - ../../product-counsel/terms-of-service-generator/SKILL.md
  - ../../security-compliance-programme-manager/compliance-auditor/SKILL.md
  - ../freelancer-contract-reviewer/SKILL.md
  - ../missing-protections-finder/SKILL.md
  - ../negotiation-strategist/SKILL.md
  - ../business-agreement-generator/SKILL.md
  - ../nda-generator/SKILL.md
triggers:
  - "contract review"
  - "review contract"
  - "legal review"
  - "contract analysis"
---

# contract-review-orchestrator

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Orchestrates multi-agent contract analysis producing a composite Contract Safety Score with clause-by-clause risk assessment, gap analysis, and prioritized negotiation recommendations.

## When to Use

- When the company receives any contract from a counterparty (vendor, customer, partner) that requires legal review before signing.
- When reviewing contract amendments or renewals where terms may have changed from the original agreement.
- When a business team forwards a contract and needs a structured risk assessment with clear action items rather than open-ended legal commentary.

## Workflow

1. **Classify Contract Type**: Identify the contract category (SaaS, services, NDA, employment, partnership, licensing). Determine governing law, counterparty type, and estimated deal value. Tag the contract with metadata for downstream agents. Deliverable: contract classification record with type, jurisdiction, and value tier.

2. **Extract and Map Clauses**: Parse the contract into individual clauses. Map each clause to the standard clause taxonomy (see [clause-taxonomy.md](references/clause-taxonomy.md)). Flag any clauses that do not map to known categories for manual review. Deliverable: structured clause inventory with taxonomy mappings.

3. **[GATE] Dispatch Risk Analysis**: Send the clause inventory to contract-risk-analyst for clause-by-clause scoring across four risk dimensions (financial exposure, operational burden, legal liability, compliance risk). Wait for the completed risk analysis report before proceeding. Deliverable: clause-level risk scores and findings.

4. **Dispatch Gap Analysis**: Send the clause inventory and contract type to missing-protections-finder. Identify standard protections expected for this contract type that are absent from the document. Deliverable: missing protections report with severity ratings.

5. **Dispatch Comparison**: If company standard terms exist for this contract type, send both documents to contract-comparator for side-by-side analysis. Score favorability of each deviation. Deliverable: comparison report with favorability assessments (or skip confirmation if no standard terms exist).

6. **Aggregate Contract Safety Score**: Compute the composite Contract Safety Score using the weighted rubric (see [scoring-rubric.md](references/scoring-rubric.md)). Score each of the five criteria (Liability Exposure, IP Protection, Termination Rights, Data & Privacy, Financial Terms) on a 0-10 scale. Calculate the weighted composite. Deliverable: scored rubric with per-criterion ratings and evidence.

7. **Generate Priority Action List**: Classify every finding into three tiers: must-change (issues that block signing), should-change (material risks worth negotiating), and acceptable (standard terms or low-risk deviations). Order must-change items by severity. Deliverable: tiered action list with specific clause references.

8. **Produce Contract Review Report**: Assemble the final report using the output template (see [contract-review-report-template.md](assets/contract-review-report-template.md)). Include executive summary with Safety Score, clause-by-clause analysis, risk heat map, missing protections, and negotiation recommendations. Route to requesting attorney or business stakeholder. Deliverable: complete contract review report.

## Anti-Patterns

- **Skipping classification**: Jumping directly into clause analysis without first classifying the contract type. *Why*: contract type determines which clauses are expected, which protections are standard, and which risks are elevated — analysis without classification produces generic findings that miss type-specific red flags.

- **Sequential single-agent review**: Performing all analysis in a single pass rather than dispatching specialized agents. *Why*: risk analysis, gap detection, and comparison against standards are distinct disciplines — a generalist pass misses hidden risks that specialized analysis catches (e.g., cross-clause compound risks, subtle missing protections).

- **Score without evidence**: Assigning Contract Safety Score ratings without citing specific clause language. *Why*: stakeholders cannot act on a score they cannot verify — every rating must trace back to exact contract text so business teams can reference specific clauses in negotiation.

- **Binary accept/reject**: Producing a single "approve" or "reject" recommendation instead of a tiered action list. *Why*: contracts are negotiated, not voted on — a tiered approach lets business teams prioritize which battles to fight based on deal importance and counterparty flexibility.

## Output

**On success**: Produces a complete contract review report containing a Contract Safety Score (0-10 composite with letter grade), clause-by-clause risk analysis, missing protections summary, comparison against standard terms (if available), and a prioritized action list with must-change, should-change, and acceptable tiers. Delivered to the requesting attorney or business stakeholder.

**On failure**: Report which analysis stages completed and which failed (e.g., risk analysis completed but comparison could not run due to missing standard terms). Include partial scores with confidence qualifiers, identify what additional information is needed, and recommend whether to proceed with partial analysis or wait for complete inputs.

## Related Skills

- [`contract-risk-analyst`](../contract-risk-analyst/SKILL.md) — Dispatched for clause-by-clause risk scoring across four dimensions; provides the granular risk data that feeds the composite Safety Score.
- [`missing-protections-finder`](../../../legal/general-counsel/missing-protections-finder/SKILL.md) — Dispatched for gap analysis to identify standard protections absent from the contract.
- [`contract-comparator`](../contract-comparator/SKILL.md) — Dispatched to compare counterparty terms against company standard terms when available.
- [`negotiation-strategist`](../../../legal/general-counsel/negotiation-strategist/SKILL.md) — Consumes the priority action list to develop negotiation talking points and fallback positions.
- [`plain-english-translator`](../plain-english-translator/SKILL.md) — Translates the review report into plain English for non-legal stakeholders who need to understand findings.
