# Growth Experiment Briefs

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | mvp-definer-growth |

## Executive Summary

[2-3 sentences stating the number of experiments scoped, the assumptions they test, and the total resource commitment. Lead with the priority: "3 experiments targeting the growth model's top 3 assumptions: activation rate, viral coefficient, and paid CAC. Combined budget: $12,000. Expected duration: 4 weeks. Highest-priority experiment: onboarding redesign targeting activation rate (+10pp expected lift)."]

## Assumption Ranking

[List the top growth model assumptions ranked by uncertainty × impact.

GUIDANCE:
- Good: "1. Activation rate (assumed 25%, current 15%, uncertainty High): a 10pp error changes 12-month MAU forecast by 34%. 2. Viral coefficient (assumed 0.20, current 0.05, uncertainty High): ..."
- Bad: "We have some assumptions to test." (no ranking, no quantified impact)
- Format: Table with assumption, current value, assumed value, uncertainty level, and MAU impact of being wrong]

| Rank | Assumption | Current Value | Growth Model Assumption | Uncertainty | MAU Impact if Wrong |
|------|-----------|--------------|------------------------|------------|-------------------|
| 1 | [Assumption name] | [X] | [Y] | High/Med/Low | [±Z% on 12mo MAU] |
| 2 | [Assumption name] | [X] | [Y] | High/Med/Low | [±Z% on 12mo MAU] |
| 3 | [Assumption name] | [X] | [Y] | High/Med/Low | [±Z% on 12mo MAU] |

---

## Experiment 1: [Experiment Name]

[Complete one-page brief per experiment.

GUIDANCE:
- Good: All fields populated with specific, measurable values. Kill criteria are pre-committed. Sample size comes from a power analysis.
- Bad: "We'll test different versions and see what works." (no hypothesis, no sample size, no kill criteria)]

| Field | Value |
|-------|-------|
| Experiment ID | [EXP-YYYY-001] |
| Assumption tested | [Name of assumption from ranking above] |
| ICE Score | Impact [X] × Confidence [Y] × Ease [Z] = [Score] |

**Hypothesis**:
We believe [change] will produce [metric] at [threshold] for [segment] because [rationale], resulting in [business impact].

**Variants**:
- Control: [Description of current experience]
- Treatment: [Description of proposed change]

**Primary Metric**: [Event name] — Target: [threshold] — Direction: [increase/decrease]

**Guardrail Metrics** (monitor for harm):
- [Metric 1]: alert if degrades > [X]%
- [Metric 2]: alert if degrades > [X]%

**Statistical Design**:
- Baseline rate: [X]%
- MDE: [Y]pp
- Required sample per variant: [Z users]
- Power: 80% at 95% confidence

**Budget**: $[X] | **Duration**: [N] weeks | **Traffic Allocation**: [50/50 or X/Y]

**Kill Criteria**:
- Stop if primary metric degrades > [X]% below control
- Stop if CAC exceeds $[Y] after [Z] conversions
- Hard stop at Day [N] regardless of status

**Owner**: [Name] | **Launch**: [YYYY-MM-DD] | **Read Date**: [YYYY-MM-DD]

---

## Experiment 2: [Experiment Name]

[Repeat brief format — one complete brief per experiment]

---

## Experiment 3: [Experiment Name]

[Repeat brief format]

---

## Experiment Roadmap

[Show sequencing and dependencies across all experiments.

GUIDANCE:
- Good: "EXP-001 runs Week 1–4 (requires 400 users/week). EXP-002 starts Week 3 using non-overlapping paid traffic segment. EXP-003 starts only after EXP-001 reads — activation rate result changes EXP-003 sample size estimate."
- Bad: Running all experiments simultaneously on the same audience without noting interaction risks.
- Format: Gantt-style table or dependency map]

| Experiment | Start Week | End Week | Audience Segment | Dependency |
|-----------|-----------|---------|-----------------|-----------|
| EXP-001 | W1 | W4 | [Segment] | None |
| EXP-002 | W2 | W5 | [Segment — non-overlapping] | None |
| EXP-003 | W5 | W8 | [Segment] | After EXP-001 reads |

## Recommendations

[Actions required before experiments launch.
GUIDANCE: Focus on prerequisites that could block experiments.

- P1: [Complete power analysis for EXP-002 based on actual traffic data] — Owner: [Growth Engineer] — By: [date]
- P1: [Instrument tracking events for all three experiments before any launch] — Owner: [Growth Engineer] — By: [date]
- P2: [Brief engineering team on EXP-001 implementation requirements] — Owner: [Growth Lead] — By: [date]]

## Appendices

### A. Power Analysis Detail

[Full calculation for each experiment's sample size, including confidence level, power, and MDE justification.]

### B. Experiment Infrastructure Checklist

[Confirm A/B testing tool is configured, events are tracking, and holdout group is established before any experiment launches.]
