---
name: product-feedback-ingestion
description: >
  This skill ingests, normalizes, and structures qualitative and quantitative
  product feedback for roadmap review cycles. Use when preparing for quarterly
  planning or roadmap prioritization. Also consider when a spike in support
  tickets or churn signals undetected product issues. Suggest when feedback
  channels exist but no systematic synthesis is feeding product decisions.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills:
  - business-model-sketcher
  - competitive-response-monitor
  - goal-framer
triggers:
  - "ingest product feedback vp"
  - "product feedback review"
  - "process feedback vp"
  - "feedback ingestion"
  - "collect feedback vp"
---

# product-feedback-ingestion

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Ingests and structures qualitative and quantitative product feedback for review cycles.

## When to Use
- When preparing for a roadmap review cycle and need a consolidated view of customer and internal feedback
- When NPS scores drop, churn ticks up, or support ticket volume spikes without a clear root cause
- When multiple feedback channels (support, sales calls, design partners, in-app surveys) exist but are not being synthesized
- When launching a post-GA retrospective and need structured signal on what shipped versus what customers expected

## Workflow
1. **Inventory feedback sources**: Catalogue all active feedback channels — support tickets, CRM call notes, NPS/CSAT surveys, in-app feedback widgets, design-partner session notes, community forums, and sales win/loss reports. Deliverable: feedback source registry.
2. **Define taxonomy**: Create a tagging schema for feedback — category (bug, feature request, UX friction, performance), severity, affected persona, product area, and frequency. Deliverable: feedback taxonomy document.
3. **Extract and normalize**: Pull feedback from each source into a central repository, applying the taxonomy tags. Normalize free-text entries into structured records with consistent fields. Deliverable: normalized feedback dataset.
4. **Deduplicate and cluster**: Group related feedback items into themes (e.g., "onboarding friction," "reporting gaps," "API rate-limit complaints"). Merge duplicates and count occurrences. Deliverable: themed feedback clusters with frequency counts.
5. **Quantify impact**: Attach business signals to each cluster — ARR at risk, number of accounts affected, deal-stage correlation, and support cost. Deliverable: impact-weighted feedback summary.
6. **Synthesize for review**: Produce a digest that highlights the top themes by impact, includes representative customer quotes, and maps themes to existing roadmap items or gaps. Deliverable: feedback synthesis report for roadmap review.
7. **Distribute and archive**: Share the synthesis with Product, Engineering, Design, and GTM stakeholders. Archive the raw dataset for longitudinal trend analysis. Deliverable: distribution confirmation and archived dataset.

## Anti-Patterns
- **Loudest-voice bias**: Prioritizing feedback from the most vocal customer or the largest logo without weighting by frequency and breadth. *Why*: Single-customer feedback skews the roadmap toward bespoke needs rather than market-wide demand.
- **Ingestion without synthesis**: Collecting feedback into a repository but never producing a structured summary. *Why*: Raw feedback is unusable for decision-making; without synthesis, the ingestion effort is wasted.
- **Stale feedback loops**: Running ingestion once and never refreshing the dataset. *Why*: Customer needs evolve; quarterly or continuous ingestion is required to keep roadmap decisions grounded in current reality.
- **Ignoring internal feedback**: Excluding input from Sales, CS, and Support who interact with customers daily. *Why*: Internal teams surface patterns that customers may not articulate directly, especially around adoption friction and competitive displacement.

## Output
**On success**: A feedback synthesis report containing impact-weighted theme clusters, representative quotes, frequency data, and mapping to roadmap items — ready for consumption in the next roadmap review cycle.
**On failure**: Report which sources could not be accessed or normalized, the coverage gap as a percentage of known channels, what partial synthesis is available, and a recommendation on whether to proceed with incomplete data or delay the review.

## Related Skills
- [`business-model-sketcher`](../business-model-sketcher/SKILL.md) — sibling skill under the same agent — combine with business-model-sketcher for end-to-end coverage
- [`competitive-response-monitor`](../competitive-response-monitor/SKILL.md) — sibling skill under the same agent — combine with competitive-response-monitor for end-to-end coverage
- [`goal-framer`](../goal-framer/SKILL.md) — sibling skill under the same agent — combine with goal-framer for end-to-end coverage
