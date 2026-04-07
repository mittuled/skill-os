# Product Health Synthesis Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Analyst name] |
| Version | [1.0] |
| Status | [Draft / Final] |
| Skill | signal-synthesiser-data |
| Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Cadence | [Weekly / Monthly / Ad-hoc] |

## Executive Summary

[1–2 sentences stating the headline product health status and the most important change this period.

GUIDANCE: Example: "Product health is mixed this week: activation rate improved 3pp to 16% (target: 18%) while support ticket volume spiked 34% above baseline, concentrated in the new export feature. Root cause investigation is underway."]

**Health status:** [Healthy / Mixed / Degraded / Critical]

## Signal Summary

[Key signals from each source with anomaly flags.

GUIDANCE:
- Good: Each signal includes source, current value, WoW or MoM change, anomaly status (Z-score if flagged), and a one-line interpretation.
- Bad: A list of numbers without direction or anomaly context.
- Format: Table grouped by source category.]

### Product Analytics

| Metric | Current Value | Prior Period | Change | Anomaly? | Interpretation |
|--------|-------------|-------------|--------|---------|---------------|
| [Metric] | [value] | [value] | [+/−X%] | [Yes (Z=[N.N]) / No] | [One-line interpretation] |

### Revenue

| Metric | Current Value | Prior Period | Change | Anomaly? | Interpretation |
|--------|-------------|-------------|--------|---------|---------------|
| [Metric] | [value] | [value] | [+/−X%] | [Yes (Z=[N.N]) / No] | [One-line interpretation] |

### Support

| Metric | Current Value | Prior Period | Change | Anomaly? | Interpretation |
|--------|-------------|-------------|--------|---------|---------------|
| [Metric] | [value] | [value] | [+/−X%] | [Yes (Z=[N.N]) / No] | [One-line interpretation] |

### Infrastructure

| Metric | Current Value | Prior Period | Change | Anomaly? | Interpretation |
|--------|-------------|-------------|--------|---------|---------------|
| [Metric] | [value] | [value] | [+/−X%] | [Yes (Z=[N.N]) / No] | [One-line interpretation] |

## Cross-Source Correlations

[Patterns connecting signals from different sources.

GUIDANCE:
- Good: "Support ticket volume (Zendesk) and error rate (Sentry) both spiked on [date], with the error rate leading by ~4 hours, suggesting the error triggered the support volume."
- Bad: "Support is up and errors are up."
- Format: Prose with explicit temporal relationship and causal hypothesis or correlation caveat.]

| Signal A | Signal B | Direction | Temporal Relationship | Hypothesis |
|---------|---------|-----------|----------------------|-----------|
| [Signal from source A] | [Signal from source B] | [Both up / A up B down / etc.] | [A led B by Nh / Simultaneous / Unknown] | [Causal hypothesis or "correlation without confirmed causation"] |

## Root Cause Analysis

[For each flagged anomaly, the leading hypothesis with evidence.

GUIDANCE:
- Good: State the anomaly, list 2 hypotheses ranked by plausibility, and the data supporting each.
- Bad: "Something changed in the product." Be specific.
- Format: One section per anomaly.]

### [Anomaly: metric name, direction, magnitude]

**Observed:** [Metric] changed from [X] to [Y] ([Z%]) between [date A] and [date B].

**Supporting cross-source signals:**
- [Signal from source B that correlates]

**Hypothesis 1 (most likely):** [Explanation] — supported by [evidence]
**Hypothesis 2:** [Explanation] — supported by [evidence]

**Recommended investigation:** [Specific query, session recordings to review, or team to consult]

## Action Items

[2–3 concrete next steps with owner and timeline.

GUIDANCE:
- Each item must have: the signal driving the action, the hypothesis, the recommended action, the owner, and the due date.
- Format: Table.]

| # | Signal | Hypothesis | Action | Owner | Due |
|---|--------|-----------|--------|-------|-----|
| 1 | [Signal] | [Hypothesis] | [Specific action] | [Name / Team] | [Date] |

## Stable Metrics (No Action Required)

[Metrics that are healthy or at baseline — document to prevent false alarm follow-ups.

GUIDANCE: List metrics that were checked and are within normal range. This prevents "why didn't you mention X" questions.]

| Metric | Value | Status |
|--------|-------|--------|
| [Metric] | [value] | Within normal range (Z = [N.N]) |

## Appendices

### A. Methodology

[Data sources queried, date ranges, anomaly detection method (Z-score threshold, seasonality adjustments), and tools used.]

### B. Supporting Data

[Raw metric tables, anomaly detection calculations, correlation analysis queries, and any raw data exports used in the synthesis.]
