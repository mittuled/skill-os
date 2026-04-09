---
name: contract-risk-analyst
description: >
  This skill performs clause-by-clause risk scoring with hidden risk detection
  and severity classification for individual contract clauses. Use when detailed
  risk analysis is needed beyond high-level review, when a contract contains
  unusual or custom clauses, or when contract-review-orchestrator dispatches for
  deep analysis. Suggest when a counterparty pushes back on standard terms with
  custom language.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../contract-review-orchestrator/SKILL.md
  - ../../../legal/general-counsel/missing-protections-finder/SKILL.md
  - ../contract-comparator/SKILL.md
  - ../../../legal/general-counsel/negotiation-strategist/SKILL.md
  - ../missing-protections-finder/SKILL.md
  - ../negotiation-strategist/SKILL.md
  - ../plain-english-translator/SKILL.md
triggers:
  - "analyze contract risks"
  - "clause-by-clause review"
  - "hidden risk detection"
  - "risk scoring needed"
---

# contract-risk-analyst

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Performs clause-by-clause risk scoring across four dimensions with hidden risk detection, compound risk identification, and severity-ranked findings for individual contract clauses.

## When to Use

- When the contract-review-orchestrator dispatches a clause inventory for deep risk analysis as part of a full contract review.
- When a contract contains unusual, heavily negotiated, or custom clauses that require analysis beyond template-matching.
- When a business team needs to understand the specific risk profile of individual clauses before entering negotiation.

## Workflow

1. **Parse Contract into Clauses**: Break the contract into discrete clause units. Preserve section numbering and cross-references. Tag each clause with its parent section for context. Deliverable: numbered clause list with section references and full text.

2. **Classify Each Clause**: Map each clause to its risk category (financial, IP, data, termination, indemnification, liability, compliance, operational) using the risk taxonomy (see [risk-categories.md](references/risk-categories.md)). Assign sub-categories where applicable. Flag clauses that span multiple categories. Deliverable: classified clause inventory with category and sub-category tags.

3. **Score Risk Dimensions**: Evaluate each clause on four risk dimensions using the scoring rubric (see [scoring-rubric.md](references/scoring-rubric.md)): financial exposure (30%), operational burden (20%), legal liability (30%), and compliance risk (20%). Score each dimension 0-10 with specific evidence from the clause text. Deliverable: per-clause dimension scores with supporting evidence.

4. **Detect Hidden Risks**: Analyze clauses for non-obvious risks: cross-reference clauses that create obligations in other sections, implied obligations not stated explicitly, missing standard protections that should accompany the clause type, ambiguous language that could be interpreted unfavorably. Review defined terms for scope expansion. Deliverable: hidden risk inventory with clause references and risk descriptions.

5. **Identify Compound Risks**: Map clause interactions where two or more clauses combine to create risk greater than either individually. Examples: an unlimited liability clause combined with a broad indemnification obligation; a non-compete clause combined with an IP assignment clause. Score compound risk severity. Deliverable: compound risk map with interaction descriptions and combined severity ratings.

6. **Rank by Severity**: Calculate composite risk score per clause (weighted sum of four dimensions). Rank all findings by severity multiplied by likelihood. Classify each finding as Critical (blocks signing), High (requires negotiation), Medium (should be flagged), or Low (acceptable with awareness). Deliverable: severity-ranked findings list.

7. **Produce Risk Analysis Report**: Assemble the complete report using the output template (see [risk-analysis-report-template.md](assets/risk-analysis-report-template.md)). Include executive summary, risk heat map, clause-by-clause analysis, hidden risks, compound risks, and prioritized action items. Deliverable: risk analysis report.

## Anti-Patterns

- **Surface-level scanning**: Reading clauses in isolation without analyzing cross-references and defined terms. *Why*: contracts are interconnected documents — a benign-looking clause may reference a definition that dramatically expands its scope, and surface scanning misses these interactions entirely.

- **Ignoring boilerplate**: Skipping standard clauses (governing law, notices, entire agreement) as "not risky." *Why*: boilerplate clauses frequently contain consequential terms (e.g., a governing law clause selecting a jurisdiction hostile to your position, or an entire agreement clause that eliminates reliance on pre-contractual representations).

- **Scoring without evidence**: Assigning risk scores based on clause type rather than actual clause language. *Why*: two liability cap clauses can have radically different risk profiles depending on the cap amount, carve-outs, and trigger conditions — the score must reflect the specific language, not the category.

- **Missing compound risks**: Analyzing each clause independently without mapping interactions. *Why*: the most dangerous contract risks often emerge from clause combinations — e.g., an unlimited liability clause alone is bad, but combined with broad indemnification and no insurance requirement, it becomes catastrophic.

## Output

**On success**: Produces a risk analysis report containing per-clause scores across four dimensions, hidden risk inventory, compound risk map, and severity-ranked findings classified as Critical, High, Medium, or Low. Delivered to contract-review-orchestrator for aggregation or directly to requesting attorney.

**On failure**: Report which clauses could not be analyzed (e.g., references to external documents not provided, defined terms not found in the contract), what partial analysis was completed, and what additional materials are needed. Flag any clauses where risk could not be determined as "Unscored — requires manual review."

## Related Skills

- [`contract-review-orchestrator`](../contract-review-orchestrator/SKILL.md) — Primary consumer of risk analysis output; dispatches this skill and aggregates results into the composite Contract Safety Score.
- [`missing-protections-finder`](../../../legal/general-counsel/missing-protections-finder/SKILL.md) — Complements risk analysis by identifying absent protections rather than scoring present clauses.
- [`contract-comparator`](../contract-comparator/SKILL.md) — Provides context on how clauses deviate from standard terms, informing whether risk scores reflect intentional negotiation or oversight.
- [`negotiation-strategist`](../../../legal/general-counsel/negotiation-strategist/SKILL.md) — Consumes severity-ranked findings to develop negotiation positions for high-risk clauses.
