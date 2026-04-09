---
name: competitive-deep-diver
description: >
  This skill conducts deep-dive competitive analysis on specific competitors or categories.
  Use when asked to analyse a competitor's product, pricing, or strategy in depth.
  Also consider when a competitor launches a major feature or enters an adjacent market.
  Suggest when sales encounters a new competitor in deal cycles repeatedly.
department: applied-research
agent: applied-research-lead
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "competitive deep dive"
  - "analyse competitors"
  - "deep competitor research"
  - "competitive intelligence"
  - "competitor analysis"
---

# competitive-deep-diver

## Agent: Applied Research Lead

L1 applied research leader (1x) responsible for market research synthesis, technology trend analysis, competitive deep dives, benchmarking, and contributing to the research roadmap.

Department ethos: [ideal-applied-research.md](../../../../departments/applied-research/ideal-applied-research.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The competitive deep diver conducts thorough analysis of specific competitors -- covering product capabilities, pricing, go-to-market strategy, technical architecture, and market positioning -- to inform product strategy and competitive response.

## When to Use

- When a specific competitor launches a major feature, funding round, or market expansion that may impact the company's position.
- When sales reports encountering a new competitor in deal cycles for the first time.
- When product strategy needs a detailed understanding of a competitor's strengths and weaknesses before a build-vs-differentiate decision.
- When the annual strategic planning process requires updated competitive landscape analysis.

## Workflow

1. **Define the scope**: Identify the competitor and the analysis dimensions (product, pricing, GTM, technical, positioning). Deliverable: analysis scope document.
2. **Gather intelligence**: Collect data from public sources (product pages, documentation, pricing, job postings, press releases, reviews, patent filings). Deliverable: raw intelligence dossier.
3. **Analyse product capabilities**: Map the competitor's feature set against the company's product, identifying overlaps, gaps, and unique differentiators. Deliverable: feature comparison matrix.
4. **Assess strategy and positioning**: Analyse the competitor's messaging, target segments, pricing model, and go-to-market approach. Deliverable: strategy assessment.
5. **Identify implications**: Determine what the competitor's moves mean for the company's product roadmap, pricing, and positioning. Deliverable: strategic implications memo.
6. **Distribute findings**: Share the analysis with product, sales, and marketing stakeholders in a format they can act on. Deliverable: competitive deep-dive report with executive summary.

## Anti-Patterns

- **Feature-list comparison only**: Comparing feature checklists without analysing strategic intent, positioning, or market context. *Why*: feature parity does not determine competitive outcomes; strategy and execution matter more.
- **Single-source analysis**: Basing conclusions on one data source (e.g., only the competitor's marketing site). *Why*: marketing claims differ from reality; triangulating multiple sources produces reliable analysis.
- **Analysis without recommendations**: Delivering a competitor profile without stating what the company should do differently. *Why*: intelligence without actionable implications is academic exercise that does not influence decisions.

## Output

**On success**: A competitive deep-dive report containing a feature comparison matrix, strategy assessment, strategic implications, and specific recommendations for product, sales, and marketing.

**On failure**: Report which analysis dimensions could not be completed (e.g., pricing data unavailable, technical architecture opaque), what was analysed, and recommend alternative intelligence-gathering approaches.

## Related Skills

- [`market-research-synthesiser`](../market-research-synthesiser/SKILL.md) -- market research provides the broader context in which competitive analysis sits.
- [`signal-benchmarker`](../signal-benchmarker/SKILL.md) -- benchmarking uses competitor data as one input for comparative analysis.
- [`technology-trend-analyst`](../technology-trend-analyst/SKILL.md) -- technology trends may explain a competitor's strategic direction.
