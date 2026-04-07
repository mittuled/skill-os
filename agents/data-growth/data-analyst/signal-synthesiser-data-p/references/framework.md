# Framework: Post-Launch Signal Synthesiser

Defines the structure for synthesising post-launch data signals into a prioritized iteration backlog.

## Post-Launch Signal Categories

| Signal Category | Sources | Analysis Window | Weight in Synthesis |
|----------------|---------|----------------|---------------------|
| Adoption | Feature event data, DAU/WAU by cohort | Days 1–30 | High |
| Funnel conversion | Step-to-step conversion rates | Days 7–30 | High |
| Error and quality | Error logs, crash reports, latency P99 | Days 1–7 (acute), ongoing | High if spikes detected |
| Support signal | Ticket volume, category, CSAT | Days 7–30 | Medium |
| Sentiment | NPS delta, App Store reviews, session recordings | Days 14–30 | Medium |

## Analysis Timeline

| Phase | Day Range | Focus | Decision Gate |
|-------|----------|-------|--------------|
| Acute monitoring | Days 1–3 | Error rates, crash rates, critical funnel drop | Roll back if P0 regression detected |
| Early signal | Days 4–7 | Adoption curve shape, first-use funnel | Decide whether to accelerate hotfixes |
| Pattern confirmation | Days 8–14 | Cohort comparison, support theme analysis | Lock in top 3 iteration candidates |
| Synthesis | Days 15–30 | Full synthesis with retention correlation | Deliver prioritized iteration backlog |

## Metric vs. Target Comparison

For each metric, calculate performance against the pre-defined success criteria:

| Status | Definition | Action |
|--------|-----------|--------|
| Green | Within 10% of target | No intervention required |
| Yellow | 10–25% below target | Flag for investigation; do not add to backlog immediately |
| Red | >25% below target | Immediate root cause investigation; add to P1 iteration backlog |

## Segmentation Protocol

Always break key metrics by:
1. **Cohort** (signup date, acquisition channel)
2. **Platform** (web, iOS, Android)
3. **Plan tier** (free, pro, enterprise)
4. **User type** (new to feature, returning, power user)

A signal that exists only in one segment indicates a targeted intervention; a signal present across all segments indicates a systemic issue.

## Iteration Prioritization Matrix

Score each potential improvement on two axes:

| Axis | Definition | How to Score |
|------|-----------|-------------|
| Expected metric impact | Estimated improvement to the target metric if the change is made | High (>10% lift) = 3 / Medium (5–10%) = 2 / Low (<5%) = 1 |
| Implementation effort | Engineering complexity and analytics rework required | Low (S–M ticket) = 3 / Medium (L ticket) = 2 / High (XL+) = 1 |

Priority score = Impact × Effort. Top 3 by score become the first iteration candidates.

## Root Cause Hypothesis Framework

For each Red metric:
1. State the observed gap (actual vs. target, with % difference).
2. Cross-reference with qualitative signals (support tickets, session recordings) for corroborating evidence.
3. Generate 2–3 hypotheses ranked by plausibility.
4. Propose the minimum viable experiment to test the top hypothesis.
