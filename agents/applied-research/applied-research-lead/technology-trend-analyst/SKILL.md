---
name: technology-trend-analyst
description: >
  This skill analyses emerging technology trends and assesses their relevance and timing for the product.
  Use when asked to evaluate a new technology, assess adoption timelines, or identify technology risks.
  Also consider when competitors adopt a new technology and the team needs to understand implications.
  Suggest when roadmap planning needs a technology horizon scan.
department: applied-research
agent: applied-research-lead
version: 1.0.0
complexity: medium
related-skills:
  - research-roadmap-contributor
  - competitive-deep-diver
  - market-research-synthesiser
triggers:
  - "analyse tech trends"
  - "technology trend report"
  - "emerging tech analysis"
  - "tech landscape scan"
  - "technology forecasting"
---

# technology-trend-analyst

## Agent: Applied Research Lead

L1 applied research leader (1x) responsible for market research synthesis, technology trend analysis, competitive deep dives, benchmarking, and contributing to the research roadmap.

Department ethos: [ideal-applied-research.md](../../../../departments/applied-research/ideal-applied-research.md)

## Skill Description

The technology trend analyst evaluates emerging technologies for their relevance to the product, assesses maturity and adoption timelines, and recommends whether to invest, monitor, or ignore each trend.

## When to Use

- When the product roadmap planning cycle needs a technology horizon scan to inform build decisions.
- When a competitor adopts a new technology and the team needs to understand whether to follow or differentiate.
- When a promising technology (AI model, protocol, framework) emerges and leadership asks whether to invest.
- When engineering raises a technology that could enable new product capabilities or reduce costs.

## Workflow

1. **Scan the landscape**: Monitor technology publications, conferences, open-source activity, and patent filings to identify emerging trends. Deliverable: trend candidate list.
2. **Filter for relevance**: Assess each trend's applicability to the company's product domain and customer needs. Deliverable: filtered trend shortlist.
3. **Evaluate maturity**: For each relevant trend, assess current maturity (experimental, early adoption, mainstream) and projected timeline to production readiness. Deliverable: maturity assessment per trend.
4. **Analyse adoption implications**: Determine what adopting the technology would require (engineering effort, infrastructure changes, skill gaps) and what it would enable. Deliverable: adoption impact analysis.
5. **Recommend action**: For each trend, recommend invest now, monitor for trigger, or ignore, with rationale. Deliverable: technology trend report with recommendations.

## Anti-Patterns

- **Hype-driven recommendations**: Recommending adoption because a technology is popular rather than because it solves a real problem. *Why*: hype cycles waste engineering resources on technologies that do not deliver customer value.
- **Analysis paralysis on trends**: Spending months evaluating a technology instead of running a time-boxed experiment. *Why*: some technologies can only be evaluated through hands-on prototyping, not desk research.
- **Ignoring timing**: Recommending a technology without assessing when it will be production-ready. *Why*: investing too early in an immature technology creates maintenance burden and reliability risk.

## Output

**On success**: A technology trend report with a filtered shortlist of relevant trends, maturity assessments, adoption impact analyses, and clear invest/monitor/ignore recommendations with rationale.

**On failure**: Report which trends could not be fully evaluated (e.g., insufficient public information, too early to assess), what partial analysis was completed, and recommend how to continue monitoring.

## Related Skills

- [`research-roadmap-contributor`](../research-roadmap-contributor/SKILL.md) -- technology trend findings feed into roadmap planning as research inputs.
- [`competitive-deep-diver`](../competitive-deep-diver/SKILL.md) -- competitor technology adoption is one signal that trend analysis monitors.
- [`market-research-synthesiser`](../market-research-synthesiser/SKILL.md) -- market research provides demand-side context for technology adoption decisions.
