---
name: technical-buyer-signal-extractor
description: >
  This skill extracts and synthesizes technical objections and requirements from
  buyer conversations. Use when asked to analyze technical feedback from deals,
  identify product gaps from SE engagements, or compile technical win/loss data.
  Also consider when Product needs field input on technical roadmap priorities.
  Suggest when technical loss reasons are not being systematically tracked.
department: sales
agent: solutions-engineering-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../solutions-playbook-builder/SKILL.md
  - ../../account-executive/sales-signal-synthesizer/SKILL.md
  - ../../solutions-engineer/technical-feasibility-for-sales/SKILL.md
---

# technical-buyer-signal-extractor

## Agent: Solutions Engineering Manager

L2 solutions engineering manager (1x) responsible for technical buyer signal extraction and solutions playbook development.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)

## Skill Description

Extracts and synthesizes technical objections, requirements, and integration demands from buyer conversations into structured intelligence that informs Product roadmap and SE enablement.

## When to Use

- When quarterly technical win/loss analysis is due and SE engagement data needs synthesis.
- When Product requests field input on technical roadmap priorities from the SE team's perspective.
- When recurring technical objections are causing deals to stall at the evaluation stage.

## Workflow

1. **Signal Collection**: Gather technical signals from SE deal notes, POC reports, technical discovery recordings, and RFP responses. Categorize by signal type: security requirement, integration demand, scalability concern, feature gap, and architecture objection. Deliverable: categorized technical signal inventory.
2. **Pattern Analysis**: Identify the top technical themes by frequency and pipeline value impact. For each theme, document the buyer's stated requirement, the current product response, and the gap (if any). Deliverable: technical theme analysis with gap assessment.
3. **Revenue Impact Scoring**: Score each technical theme by revenue impact: total pipeline stalled or lost due to the gap, number of affected deals, and average deal size. Prioritize themes by revenue-weighted frequency. Deliverable: revenue-impact-scored technical theme ranking.
4. **Product Recommendation Brief**: Draft recommendations for Product Engineering: which gaps to close, suggested implementation approaches from the field perspective, and estimated pipeline recovery if addressed. Include customer quotes and deal references. Deliverable: technical product recommendation brief.
5. **SE Enablement Update**: Update the solutions playbook with new technical objection responses, workaround documentation, and revised competitive positioning for themes where the gap is known and managed. Deliverable: updated SE enablement materials.

## Anti-Patterns

- **Anecdote-driven escalation**: Escalating a technical gap to Product based on one vocal prospect rather than a pattern across deals. *Why*: single-prospect advocacy distorts roadmap priorities; Product needs revenue-weighted signal data to make sound investment decisions.
- **Technical signals without business context**: Reporting that "prospects want feature X" without explaining the business outcome the feature enables or the revenue at stake. *Why*: Product prioritizes based on business impact; a feature request without revenue context competes poorly for engineering resources.
- **Hoarding signals**: Keeping technical intelligence within the SE team instead of sharing structured data with Product and Sales. *Why*: siloed intelligence means Product builds without field context and Sales sells without awareness of known gaps.

## Output

**On success**: Produces a technical buyer signal report containing categorized signal inventory, theme analysis, revenue-impact scoring, product recommendation brief, and updated SE enablement materials. Delivered to Product Engineering and VP Sales.

**On failure**: Report which signal categories lacked sufficient data (e.g., too few POC reports, incomplete deal notes), what sources were consulted, and recommended improvements to signal capture processes.

## Related Skills

- [`solutions-playbook-builder`](../solutions-playbook-builder/SKILL.md) -- Consumes signal analysis to update technical playbook content.
- [`sales-signal-synthesizer`](../../account-executive/sales-signal-synthesizer/SKILL.md) -- Provides complementary commercial signal synthesis that aligns with technical signals.
- [`technical-feasibility-for-sales`](../../solutions-engineer/technical-feasibility-for-sales/SKILL.md) -- Produces feasibility assessments that generate technical signal data.
