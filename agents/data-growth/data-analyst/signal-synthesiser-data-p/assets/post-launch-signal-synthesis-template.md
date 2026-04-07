# Post-Launch Signal Synthesis

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | signal-synthesiser-data-p |
| Feature | [Feature name] |
| Launch Date | [YYYY-MM-DD] |
| Analysis Window | [Days 1–30 / Days 7–14 / specify] |

## Executive Summary

[2-3 sentences with the headline performance verdict, top finding, and the priority-1 iteration candidate.

GUIDANCE: Lead with the performance verdict. Example: "In the first 21 days post-launch, the [feature name] is tracking below its activation target (actual 12%, target 18%) with the primary drop-off at step 2 of onboarding. The priority-1 iteration candidate is reducing friction in the initial setup flow, which is supported by both funnel data and 47 support tickets referencing configuration confusion."]

## Metric Performance vs. Targets

[All metrics with comparison to pre-defined success criteria.

GUIDANCE:
- Good: Table with actual value, target value, % to target, and status (Green/Yellow/Red).
- Bad: Metrics listed without their pre-defined targets.
- Format: Table.]

| Metric | Target | Actual | % to Target | Status | Notes |
|--------|--------|--------|------------|--------|-------|
| [Metric name] | [value] | [value] | [X%] | [Green / Yellow / Red] | [Cohort or context note] |

## Cohort Analysis

[Key metrics broken down by the primary segmentation dimensions.

GUIDANCE:
- Good: Surface the segment with the most divergent performance and hypothesize why.
- Bad: Showing aggregate metrics only.
- Format: Table per segment dimension showing the highest and lowest performing segments.]

### By Acquisition Channel

| Channel | [Metric 1] | [Metric 2] | Performance vs. Avg |
|---------|-----------|-----------|---------------------|
| [Channel name] | | | [X% above/below avg] |

### By Platform

| Platform | [Metric 1] | [Metric 2] | Performance vs. Avg |
|---------|-----------|-----------|---------------------|
| [Platform] | | | [X% above/below avg] |

## Funnel Analysis

[Step-by-step conversion for the key post-launch flow.

GUIDANCE:
- Good: Show absolute counts and conversion rates; call out the single highest-impact drop-off step.
- Bad: End-to-end conversion only with no step breakdown.
- Format: Funnel table.]

| Step | Step Name | Users Entering | Users Completing | Conversion Rate | vs. Target |
|------|----------|---------------|-----------------|----------------|-----------|
| 1 | [Step name] | [N] | [N] | [X%] | [+/−X pp] |

**Highest-impact drop-off:** Step [N] — [Name] ([X%] conversion, [N] users lost)

## Qualitative Correlation

[Cross-reference of quantitative signals with support tickets, user feedback, and session recordings.

GUIDANCE:
- Good: Specific support ticket themes linked to specific funnel or adoption gaps.
- Bad: "Users are unhappy" without data.
- Format: Table linking signal to data point.]

| Qualitative Signal | Volume / Frequency | Correlated Metric | Hypothesis |
|-------------------|--------------------|------------------|-----------|
| [Support ticket theme / NPS comment / session recording pattern] | [N tickets / mentions] | [Metric with gap] | [Root cause hypothesis] |

## Prioritized Iteration Backlog

[Ranked list of iteration candidates with data justification.

GUIDANCE:
- Good: Each item has a metric impact estimate, effort estimate, and data source.
- Bad: A backlog without priority scores or supporting evidence.
- Format: Numbered list with impact × effort scoring.]

| Rank | Iteration Candidate | Target Metric | Expected Lift | Effort | Priority Score | Evidence |
|------|--------------------|--------------|--------------|----|---------------|---------|
| 1 | [Description] | [Metric] | [X%] | [S/M/L/XL] | [N] | [Funnel step / ticket theme / session insight] |

## Recommendations

[3–5 concrete next steps.

GUIDANCE:
- P1: Highest-scoring iteration items to add to the next sprint backlog.
- P2: Experiments to test root cause hypotheses before committing to full implementation.
- P3: Instrumentation gaps discovered that must be fixed for the next synthesis cycle to be complete.]

## Appendices

### A. Methodology

[Data sources queried, date ranges, cohort definitions, and analysis tools used. Note any instrumentation gaps that constrained the analysis.]

### B. Supporting Data

[Raw metric tables, funnel SQL queries, support ticket category summaries, and session recording references used in the synthesis.]
