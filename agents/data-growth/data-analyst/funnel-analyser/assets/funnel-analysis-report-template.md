# Funnel Analysis Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | funnel-analyser |
| Funnel | [Funnel name, e.g., Activation funnel] |
| Analysis Window | [YYYY-MM-DD to YYYY-MM-DD] |

## Executive Summary

[2-3 sentences with the end-to-end conversion rate, the highest-impact drop-off step, and the priority recommendation.

GUIDANCE: Lead with the number. Example: "End-to-end activation funnel conversion is 14.3% (target: 20%) over the 30-day analysis window. The highest-impact drop-off is Step 3 (connect integration), where 42% of entrants abandon, representing 1,840 users per week. Priority recommendation: investigate the integration setup UX, where session recordings show users spending an average of 8 minutes before abandoning."]

**End-to-end conversion:** [X%] (target: [Y%])
**Primary drop-off step:** Step [N] — [Step name] ([X%] conversion)
**Analysis window:** [YYYY-MM-DD to YYYY-MM-DD]

## Funnel Step Analysis

[Step-by-step conversion table.

GUIDANCE:
- Good: Every step has entry count, completion count, conversion rate, absolute drop-off, and time-to-next-step.
- Bad: Only showing end-to-end conversion.
- Format: Table with impact score ranking.]

| Step | Name | Entrants | Completions | Conversion Rate | Drop-off (abs.) | Median Time-to-Next | Impact Score | Rank |
|------|------|----------|------------|----------------|----------------|---------------------|-------------|------|
| 1 | [Step name] | [N] | [N] | [X%] | [N] | [Xm Ys] | [N] | [N] |

**Instrumentation status:** All step events verified / [List any unverified steps with gap note]

## Cohort Segmentation

[Conversion breakdown by key segments.

GUIDANCE:
- Good: Show at least acquisition channel and platform segments. Call out the most divergent segment.
- Bad: One aggregate conversion rate presented as representative.
- Format: One table per segmentation dimension.]

### By Acquisition Channel

| Channel | End-to-End Conversion | Step [N] Conversion | vs. Overall | Note |
|---------|----------------------|---------------------|------------|------|
| [Channel] | [X%] | [X%] | [+/−Xpp] | |

### By Platform

| Platform | End-to-End Conversion | Step [N] Conversion | vs. Overall | Note |
|---------|----------------------|---------------------|------------|------|
| [Platform] | [X%] | [X%] | [+/−Xpp] | |

## Time-Series Trends

[Conversion rates over the analysis window with change annotations.

GUIDANCE:
- Good: Plot weekly conversion rate for the top 2 drop-off steps; annotate product deploy dates.
- Bad: Single period snapshot with no trend context.
- Format: Table of weekly conversion rates with key dates annotated.]

| Week | Step [N] Conversion | Step [N+1] Conversion | Notable Events |
|------|--------------------|-----------------------|---------------|
| [YYYY-Wxx] | [X%] | [X%] | [Deploy / experiment / none] |

## Root Cause Analysis

[Hypotheses for top drop-off steps with supporting evidence.

GUIDANCE:
- Good: Each hypothesis is linked to a specific data signal (session recording observation, support ticket theme, error rate spike).
- Bad: Hypotheses without data backing.
- Format: Table per high-impact step.]

### Step [N] — [Step Name]

| Hypothesis | Category | Supporting Evidence | Confidence |
|-----------|---------|--------------------|-----------:|
| [Hypothesis] | [UX friction / Copy / Technical / Audience] | [Signal + source] | [High/Med/Low] |

## Recommendations

[Prioritized experiments and fixes.

GUIDANCE:
- P1: Highest impact-score drop-off with a specific experiment proposal (hypothesis, variant, success metric, minimum sample size).
- P2: Second priority; include effort estimate.
- P3: Monitoring improvements or instrumentation gaps that must be addressed for the next analysis cycle.
- Format: Numbered list.]

1. **[P1]** [Step N] — [Experiment or fix] — Expected lift: [X pp] — Effort: [S/M/L] — Success metric: [metric at significance p<0.05, n=[X] per variant]
2. **[P2]** [Step N] — [Experiment or fix]
3. **[P3]** [Instrumentation or monitoring improvement]

## Appendices

### A. Methodology

[Query approach, session window definition, deduplication logic, instrumentation verification status for each step event.]

### B. Supporting Data

[Raw step count tables by day, SQL queries used for the analysis, session recording session IDs referenced, support ticket export by theme.]
