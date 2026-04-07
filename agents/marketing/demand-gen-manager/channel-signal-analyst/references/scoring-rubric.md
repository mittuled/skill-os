# Scoring Rubric: channel-signal-analyst

Evaluates the quality of acquisition channel performance analysis and the actionability of reallocation recommendations.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Data Completeness | 25% | Whether all active channels are covered with spend, conversion, and pipeline data for the full analysis period |
| 2 | Unit Economics Accuracy | 25% | Correctness and consistency of CPL, cost-per-MQL, cost-per-SQL, and CAC calculations across channels |
| 3 | Anomaly Detection Quality | 20% | Whether deviations are properly identified, categorized, and supported by root cause analysis |
| 4 | Reallocation Actionability | 20% | Whether budget shift recommendations are specific, quantified, and tied to projected pipeline impact |
| 5 | Attribution Awareness | 10% | Whether the analysis accounts for multi-touch attribution and avoids last-touch bias |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score x weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 - 10.0 | Decision-Ready | All channels analysed with accurate unit economics; reallocation recommendations backed by projected outcomes | Execute recommended reallocations immediately |
| A | 8.0 - 8.9 | Strong | Minor data gaps but fundamentally sound analysis with actionable recommendations | Execute with noted caveats; close data gaps next cycle |
| B | 7.0 - 7.9 | Useful | Most channels covered; recommendations directionally correct but lack precision | Use for directional decisions; request deeper analysis on flagged channels |
| C | 5.0 - 6.9 | Incomplete | Significant channel or metric gaps; recommendations are too vague to act on | Return for additional data collection before making budget decisions |
| D | 3.0 - 4.9 | Unreliable | Major calculation errors or missing channels; conclusions contradict available data | Discard conclusions; investigate data pipeline issues |
| F | 0.0 - 2.9 | No Basis | Analysis missing most channels, no unit economics computed, no recommendations | Restart with complete data extraction; audit tracking infrastructure |

## Signal Tables

### Data Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | All active channels (paid, organic, email, events) included; spend, impressions, clicks, MQLs, SQLs, and pipeline value captured for the full period; cross-platform data reconciled within 5% |
| 7-8 | 80%+ of active channels covered; 1-2 minor channels missing; data covers full period but minor reconciliation discrepancies exist |
| 5-6 | 60-80% of channels covered; one major channel missing data; partial period coverage on some channels |
| 3-4 | Fewer than 60% of channels included; multiple data sources unavailable; analysis period inconsistent across channels |
| 0-2 | Fewer than 3 channels with any data; no spend data available; analysis based on single platform only |

### Unit Economics Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | CPL, cost-per-MQL, cost-per-SQL, and CAC computed for every channel; calculations independently verifiable; benchmarks and prior-period comparisons included |
| 7-8 | All core metrics computed; minor rounding or attribution edge cases noted; prior-period comparison included for most channels |
| 5-6 | CPL computed for all channels but downstream metrics (cost-per-SQL, CAC) missing for 2+ channels; no benchmark comparison |
| 3-4 | Only CPL computed; no downstream conversion economics; calculation methodology inconsistent across channels |
| 0-2 | No unit economics computed; raw spend and lead counts only; no per-channel cost analysis |

### Anomaly Detection Quality

| Score | Evidence |
|-------|----------|
| 9-10 | All deviations >15% from plan flagged; each anomaly categorised as positive or negative with documented root cause; seasonal and competitive context included |
| 7-8 | Most anomalies flagged; root causes identified for high-impact deviations; some minor anomalies lack explanation |
| 5-6 | Anomalies identified but categorisation is incomplete; root causes speculative for 2+ flagged items |
| 3-4 | Only the most obvious anomalies noted; no root cause analysis; positive and negative signals not distinguished |
| 0-2 | No anomaly detection performed; data presented as flat tables without variance analysis |

### Reallocation Actionability

| Score | Evidence |
|-------|----------|
| 9-10 | Specific dollar amounts recommended for reallocation between named channels; projected impact on lead volume and pipeline quantified; implementation timeline included |
| 7-8 | Directional recommendations (increase/decrease) with approximate amounts; projected impact estimated but ranges are wide |
| 5-6 | General recommendations ("shift budget to paid search") without specific amounts or projected impact |
| 3-4 | Vague suggestions ("optimise underperforming channels") with no specificity on which channels or how much |
| 0-2 | No recommendations provided; analysis is descriptive only |

### Attribution Awareness

| Score | Evidence |
|-------|----------|
| 9-10 | Multi-touch attribution data referenced; channel analysis acknowledges assist contributions; first-touch and last-touch views compared |
| 7-8 | Attribution model referenced; at least one alternative attribution view presented alongside primary |
| 5-6 | Single attribution model used; awareness of limitations mentioned but no alternative views provided |
| 3-4 | Last-touch attribution used without acknowledgement of limitations |
| 0-2 | No attribution methodology stated; channel credit assignment methodology unclear |
