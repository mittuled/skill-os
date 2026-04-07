---
name: missing-protections-finder
description: >
  This skill identifies missing standard protections in contracts by comparing against
  contract-type-specific checklists and universal protection requirements. Use when
  reviewing any contract to ensure all expected protections are present. Also consider
  when evaluating contracts from unfamiliar counterparties or jurisdictions. Suggest
  when contract-review-orchestrator dispatches for gap analysis.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md
  - ../../../legal/corporate-counsel/contract-risk-analyst/SKILL.md
  - ../../../legal/corporate-counsel/negotiation-strategist/SKILL.md
  - ../../../legal/corporate-counsel/compliance-scanner/SKILL.md
triggers:
  - "check missing protections"
  - "contract gap analysis"
  - "what protections are missing"
  - "protection coverage check"
---

# missing-protections-finder

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, risk registers, third-party ToS review, entity formation, bylaws, equity issuance, and contract protection analysis.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Identifies missing standard protections in contracts by comparing against contract-type-specific checklists and universal protection requirements, producing a scored gap report with recommended clause language.

## When to Use

- When reviewing any inbound contract to verify all expected protective clauses are present before signing.
- When evaluating contracts from unfamiliar counterparties or foreign jurisdictions where standard protections may differ.
- When contract-review-orchestrator dispatches for systematic gap analysis as part of a full contract review.
- When onboarding a new vendor or partner and assessing whether their paper adequately protects the company.

## Workflow

1. **Contract Classification**: Classify the contract type (SaaS Agreement, Services Agreement, NDA, Employment Agreement, Partnership Agreement, or other) and select the applicable protection checklist from the [reference checklists](references/checklist.md). If the contract spans multiple types, merge the applicable checklists and deduplicate. Deliverable: classified contract type with selected checklist.

2. **Protection Scan**: Scan the contract clause by clause against each item in the selected checklist plus the universal protections list. For each protection, record status: Present (clause exists and is adequate), Partial (clause exists but is weak, ambiguous, or overly narrow), or Missing (no clause addressing this protection). Deliverable: annotated protection coverage matrix.

3. **Coverage Scoring**: Calculate overall protection coverage as a percentage (present items / total checklist items). Score each category separately (e.g., liability protections: 80%, IP protections: 50%, termination protections: 100%). Deliverable: coverage scorecard with category-level and aggregate scores.

4. **Gap Risk Assessment**: Assess the risk level of each Partial or Missing protection. Critical: business-threatening exposure (e.g., no limitation of liability, no IP ownership clause). High: significant financial or operational exposure. Medium: notable risk that should be addressed but is survivable. Low: best practice that strengthens position but absence is not dangerous. Deliverable: risk-rated gap list.

5. **Gap Report Production**: Compile findings into a structured gap report using the [protections gap report template](assets/protections-gap-report-template.md). For each Critical and High gap, include recommended clause language ready for insertion. For Medium and Low gaps, include a description of what the clause should address. Deliverable: complete protections gap report.

## Anti-Patterns

- **Using a generic checklist for all contract types**: Applying the same protection checklist regardless of whether the contract is an NDA or a SaaS agreement. *Why*: each contract type has distinct risk profiles — an NDA does not need payment terms, and a SaaS agreement needs uptime commitments an NDA does not. Generic checklists produce false positives and miss type-specific gaps.

- **Flagging everything as Critical**: Rating all missing protections at the same risk level. *Why*: this violates the legal department's principle of proportional response and overwhelms the deal team, making it impossible to prioritize negotiation efforts on the gaps that actually matter.

- **Ignoring partial protections**: Marking a protection as "Present" when the clause exists but is weak, ambiguous, or one-sided. *Why*: a liability cap of $100 on a $1M contract technically exists but provides no real protection — partial protections often create more risk than missing ones because they create a false sense of security.

## Output

**On success**: Produces a protections gap report containing the coverage scorecard, risk-rated gap analysis with recommended clause language for Critical and High items, and a prioritized remediation plan. Delivered as a structured document using the [protections gap report template](assets/protections-gap-report-template.md).

**On failure**: Report which aspects of the contract could not be analyzed (e.g., contract type unrecognizable, clauses in foreign language, referenced exhibits missing), what partial analysis was completed, and what must be provided to complete the gap analysis.

## Related Skills

- [`contract-review-orchestrator`](../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md) — Upstream orchestrator that dispatches this skill as part of comprehensive contract review.
- [`contract-risk-analyst`](../../../legal/corporate-counsel/contract-risk-analyst/SKILL.md) — Complements gap analysis with quantitative risk assessment of identified exposures.
- [`negotiation-strategist`](../../../legal/corporate-counsel/negotiation-strategist/SKILL.md) — Downstream consumer that uses identified gaps as must-have negotiation items.
- [`compliance-scanner`](../../../legal/corporate-counsel/compliance-scanner/SKILL.md) — Assesses regulatory compliance, which may surface additional required protections.
