---
name: sales-signal-synthesizer
description: >
  This skill synthesizes sales signals from prospect conversations into product
  and positioning insights. Use when asked to analyze field data, produce
  signal reports, or identify trends from sales conversations. Also consider
  at end-of-quarter when aggregated deal data is available.
  Suggest when Product requests field input for roadmap planning.
department: sales
agent: account-executive
version: 1.0.0
complexity: medium
related-skills:
  - ../sales-signal-collector/SKILL.md
  - ../../../sales/sales-manager/objection-handler-updater-sales/SKILL.md
  - ../../../sales/solutions-engineering-manager/technical-buyer-signal-extractor/SKILL.md
---

# sales-signal-synthesizer

## Agent: Account Executive

L3 account executive (Nx) responsible for sales signal synthesis, signal collection, and expansion sales motions.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)

## Skill Description

Synthesizes sales signals from prospect conversations into product and positioning insights that inform roadmap priorities, messaging updates, and competitive strategy.

## When to Use

- When enough signals have accumulated (end of quarter, end of campaign) to warrant synthesis into actionable themes.
- When Product requests field input for roadmap prioritization and needs structured signal data.
- When win/loss patterns suggest a positioning or product gap that requires cross-functional action.

## Workflow

1. **Signal Aggregation**: Pull all tagged signals from the CRM for the analysis period. Group by signal type: objections, competitive mentions, feature requests, buying triggers, and deal blockers. Deliverable: signal dataset grouped by type with frequency counts.
2. **Theme Extraction**: Identify the top 5 themes by frequency and deal-value impact. For each theme, document the underlying buyer concern, representative quotes, and affected deal stages. Deliverable: theme analysis with supporting evidence.
3. **Impact Scoring**: Score each theme by revenue impact: total pipeline value of deals where the theme appeared, win rate delta for deals with vs. without the theme, and average deal cycle impact. Deliverable: theme impact scorecard.
4. **Recommendation Drafting**: Draft actionable recommendations for each theme directed to the appropriate team: Product (feature gaps), Marketing (positioning gaps), Sales Management (process gaps), or SE (technical gaps). Deliverable: recommendation brief per theme with owner and urgency.
5. **Stakeholder Distribution**: Distribute the synthesis report to VP Sales, Product, and Marketing stakeholders. Present the top 3 themes in the cross-functional pipeline review. Deliverable: published signal synthesis report.

## Anti-Patterns

- **Cherry-picking signals**: Selecting signals that confirm a pre-existing narrative while ignoring contradictory data. *Why*: biased synthesis produces recommendations that solve the wrong problems and misallocates Product and Marketing resources.
- **Signal without context**: Reporting that "12 prospects mentioned competitor X" without explaining what specifically about competitor X resonated and in what deal stage. *Why*: frequency without context gives stakeholders a headline but no actionable insight.
- **Synthesis without recommendations**: Producing a report that describes themes but does not recommend specific actions or owners. *Why*: insights without action items become interesting reading that changes nothing.

## Output

**On success**: Produces a signal synthesis report containing themed analysis, impact scorecards, and actionable recommendations with assigned owners. Delivered to VP Sales, Product, and Marketing.

**On failure**: Report which themes could not be analyzed (e.g., insufficient signal volume for statistical confidence), what data was available, and recommended additional signal collection focus.

## Related Skills

- [`sales-signal-collector`](../sales-signal-collector/SKILL.md) -- Provides the raw signal data this skill synthesizes.
- [`objection-handler-updater-sales`](../../../sales/sales-manager/objection-handler-updater-sales/SKILL.md) -- Consumes objection themes to update response frameworks.
- [`technical-buyer-signal-extractor`](../../../sales/solutions-engineering-manager/technical-buyer-signal-extractor/SKILL.md) -- Provides technical buyer signals that complement sales signal synthesis.
