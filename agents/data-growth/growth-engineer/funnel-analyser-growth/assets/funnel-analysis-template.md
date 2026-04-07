# Growth Funnel Analysis

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | funnel-analyser-growth |
| Analysis Window | [YYYY-MM-DD to YYYY-MM-DD] |
| Total users in analysis | [N] |

## Executive Summary

[2-3 sentences identifying the primary bottleneck, its absolute user loss, and the top experiment recommendation.
GUIDANCE: Example — "The highest-leverage bottleneck in the growth funnel is the Onboarding → Activation step, losing 12,400 users/month at 34% conversion. Channel analysis shows referral traffic converts at 52% vs. 28% for paid search at this step, indicating a persona-fit gap. Recommended experiment: reduce the mandatory setup wizard from 6 steps to 2 for paid search traffic."]

## Funnel Overview

[Present step-by-step conversion for the full acquisition-to-activation funnel.
GUIDANCE:
- Good: Specific numbers at each step with absolute loss and percentage conversion clearly labeled.
- Bad: "Conversion drops somewhere in onboarding."
- Format: Table as shown; highlight the top bottleneck row]

| Step | Event | Users Entering | Users Completing | Conversion Rate | Absolute Loss | Bottleneck Rank |
|------|-------|---------------|-----------------|----------------|--------------|----------------|
| 1 → 2 | Landing → Signup | [N] | [N] | [%] | [N users] | [#] |
| 2 → 3 | Signup → Onboarding complete | [N] | [N] | [%] | [N users] | [#] |
| 3 → 4 | Onboarding → Activation | [N] | [N] | [%] | [N users] | **[Top bottleneck]** |
| 4 → 5 | Activation → Paid conversion | [N] | [N] | [%] | [N users] | [#] |

**End-to-end conversion (Landing → Paid)**: [%]

**Top bottleneck**: Step [N → N+1] — [N] absolute users lost per [analysis period]

## Channel Segmentation

[Break the top bottleneck step by acquisition channel. Identify channels with conversion ≥20 pp below the best-performing channel.
GUIDANCE:
- Good: "Paid search converts at 28% at the activation step vs. 52% for referral — a 24 pp gap suggesting the paid search landing experience does not match the user's intent or persona."
- Bad: "Paid search is underperforming."
- Format: Table per channel for the bottleneck step only]

**Bottleneck step analyzed**: Step [N → N+1]

| Channel | Users Entering | Conversion | vs. Best Channel | Flag? |
|---------|---------------|-----------|-----------------|-------|
| Referral | [N] | [%] | Baseline | — |
| Organic SEO | [N] | [%] | [±N pp] | [Yes/No] |
| Paid search | [N] | [%] | [±N pp] | [Yes/No] |
| Direct | [N] | [%] | [±N pp] | [Yes/No] |

## Device and Cohort Analysis

[Identify device-specific conversion gaps and cohort trends at the top bottleneck.
GUIDANCE:
- Good: "Mobile web converts at 18% vs. 41% for desktop at the signup step, indicating a mobile form UX issue. No significant cohort trend in the last 8 weeks (±3 pp variance)."
- Bad: "Mobile might be an issue."]

**Device comparison** (bottleneck step):

| Device | Conversion | Gap vs. Desktop |
|--------|-----------|----------------|
| Desktop | [%] | Baseline |
| Mobile web | [%] | [±N pp] |
| iOS native | [%] | [±N pp] |

**Cohort trend**: [Stable / Improving (N pp over 8 weeks) / Declining (N pp over 8 weeks)]

## Experiment Recommendations

[Top 2–3 experiments targeting the highest-leverage bottleneck steps.
GUIDANCE: Each experiment must have a specific hypothesis, not just a description of the change.]

### Experiment 1 — [Name]

| Field | Value |
|-------|-------|
| Bottleneck step | [Step N → N+1] |
| Current conversion | [%] |
| Root cause hypothesis | [Specific mechanism causing the drop-off] |
| Experiment | [What to test and how] |
| Success metric | [Primary metric, e.g., "Activation rate within 7 days"] |
| Target conversion lift | [+N pp] |
| Expected monthly user gain | [N users] |
| ICE score | Impact [/10] × Confidence [/10] × Ease [/10] = [Score] |
| Required sample size | [N per variant for 80% power at α=0.05] |

### Experiment 2 — [Name]

[Repeat the above structure]

## Recommendations

[Prioritized action list from this analysis.
GUIDANCE: Separate experiment recommendations (ship next sprint) from instrumentation gaps (fix before next analysis).]

| Priority | Action | Owner | Timeline |
|----------|--------|-------|---------|
| P1 | [Top experiment to design and ship] | [Growth Lead] | [Date] |
| P2 | [Second experiment] | [Growth Engineer] | [Date] |
| P3 | [Instrumentation gap to close] | [Growth Engineer] | [Date] |

## Appendices

### A. Methodology

[Data source, query approach, date range, cohort definition, baseline window used for MDE calculation.]

### B. Supporting Data

[Raw funnel tables, channel-level breakdown across all steps, cohort-by-cohort conversion table, and SQL queries used.]
