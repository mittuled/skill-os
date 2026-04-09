---
name: signal-benchmarker
description: >
  This skill benchmarks product and business signals against industry standards and comparable companies.
  Use when asked to compare metrics to peers, validate performance against benchmarks, or assess
  relative market position. Also consider when leadership questions whether a metric is good or bad
  without external context. Suggest when investor updates need benchmark-contextualized metrics.
department: applied-research
agent: applied-research-lead
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "benchmark signals"
  - "compare market signals"
  - "signal benchmarking"
  - "track leading indicators"
  - "signal performance review"
---

# signal-benchmarker

## Agent: Applied Research Lead

L1 applied research leader (1x) responsible for market research synthesis, technology trend analysis, competitive deep dives, benchmarking, and contributing to the research roadmap.

Department ethos: [ideal-applied-research.md](../../../../departments/applied-research/ideal-applied-research.md)

## Skill Description

The signal benchmarker compares the company's product and business metrics against industry standards, peer companies, and comparable-stage benchmarks to provide context for whether performance is strong, average, or concerning.

## When to Use

- When leadership asks whether a key metric (NRR, churn, conversion rate) is "good" and needs external context.
- When investor updates or board materials need benchmark-contextualised performance data.
- When product decisions need evidence of how comparable companies perform on similar metrics.
- When a new metric is introduced and the team lacks intuition for what good looks like.

## Workflow

1. **Identify metrics to benchmark**: Determine which product and business signals need external context. Deliverable: metrics list with current values.
2. **Source benchmarks**: Gather benchmark data from analyst reports, industry surveys, public filings, and peer networks. Deliverable: benchmark dataset with sources.
3. **Normalise for comparability**: Adjust for stage, market, and segment differences to ensure fair comparison. Deliverable: normalised benchmark comparison.
4. **Assess performance**: Rate each metric against benchmarks (above, at, or below benchmark) with confidence level. Deliverable: benchmarking scorecard.
5. **Recommend actions**: For below-benchmark metrics, identify potential causes and suggest improvement levers. Deliverable: benchmarking report with recommendations.

## Anti-Patterns

- **Benchmarking against the wrong cohort**: Comparing an early-stage company to mature enterprises or vice versa. *Why*: stage-inappropriate benchmarks set unrealistic expectations and misguide strategy.
- **Treating benchmarks as targets**: Optimising to match a benchmark rather than understanding the company's unique context. *Why*: benchmarks are reference points, not goals; blindly chasing them ignores company-specific dynamics.

## Output

**On success**: A benchmarking scorecard comparing key metrics against appropriate peer benchmarks, with performance ratings and recommended improvement actions for underperforming metrics.

**On failure**: Report which metrics lacked reliable benchmarks (e.g., niche market with no public comparables), what partial benchmarking was completed, and recommend alternative approaches to obtain context.

## Related Skills

- [`market-research-synthesiser`](../market-research-synthesiser/SKILL.md) -- market research provides contextual data that enriches benchmarking analysis.
- [`competitive-deep-diver`](../competitive-deep-diver/SKILL.md) -- competitor analysis supplies specific peer data for benchmarking.
