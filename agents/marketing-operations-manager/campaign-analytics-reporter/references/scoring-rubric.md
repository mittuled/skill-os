# Scoring Rubric: campaign-analytics-reporter

Evaluates the quality of the weekly campaign performance report including data accuracy, insight depth, and recommendation actionability.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Data Accuracy | 25% | Whether campaign metrics are correctly extracted, reconciled, and computed across platforms |
| 2 | Variance Analysis | 25% | Whether performance deviations from targets and prior periods are identified and contextualised |
| 3 | Insight Quality | 20% | Whether the report moves beyond data description to explain why metrics moved |
| 4 | Recommendation Specificity | 20% | Whether action recommendations are concrete, assignable, and tied to metric improvement |
| 5 | Report Clarity | 10% | Whether the executive summary and format enable quick decision-making |
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
| A+ | 9.0 - 10.0 | Decision-Ready | Accurate data, clear insights, specific recommendations ready for immediate action | Distribute and execute recommendations |
| A | 8.0 - 8.9 | Strong | Reliable metrics with useful insights; minor gaps in recommendation specificity | Distribute; request clarification on vague recommendations |
| B | 7.0 - 7.9 | Adequate | Metrics directionally correct; insights present but surface-level | Use for status tracking; request deeper analysis on outliers |
| C | 5.0 - 6.9 | Incomplete | Significant metric gaps or reconciliation issues; insights are speculative | Hold distribution; resolve data discrepancies first |
| D | 3.0 - 4.9 | Unreliable | Major calculation errors or missing campaigns; conclusions not supported by data | Reject; investigate data pipeline and recalculate |
| F | 0.0 - 2.9 | No Basis | Report not produced or contains fundamentally flawed data | Escalate data infrastructure issues; produce manual interim report |

## Signal Tables

### Data Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | All campaign platforms reconciled within 2% variance; spend, leads, MQLs, SQLs, and pipeline values verified; UTM tracking intact across all campaigns |
| 7-8 | 90%+ of data reconciled; minor discrepancies documented; 1-2 small campaigns have incomplete tracking |
| 5-6 | Major platform data pulled but reconciliation shows 5-10% variance; some campaigns missing downstream conversion data |
| 3-4 | Multiple platforms show irreconcilable discrepancies; spend data does not match finance records; conversion tracking broken on 2+ campaigns |
| 0-2 | Data not extracted from 1+ major platforms; no reconciliation attempted; metrics are estimates |

### Variance Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Every metric compared against target and prior period; variances >5% annotated with context (budget change, creative refresh, seasonal factor); trend direction indicated |
| 7-8 | Key metrics compared against targets; most variances annotated; some minor deviations lack context |
| 5-6 | Metrics reported alongside targets but variance percentages not calculated; context provided only for largest deviations |
| 3-4 | Metrics reported without target comparison; prior period included but not analysed |
| 0-2 | Single-period metrics only; no target or prior period comparison |

### Insight Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Report explains causal factors behind 3+ metric movements; connects campaign changes to outcome shifts; identifies emerging patterns |
| 7-8 | Key movements explained with plausible causes; 1-2 insights connect actions to outcomes |
| 5-6 | Insights are observational ("CPL increased 15%") without causal explanation |
| 3-4 | No analysis beyond metric presentation; data speaks for itself approach |
| 0-2 | Raw data tables only; no narrative or interpretation |

### Recommendation Specificity

| Score | Evidence |
|-------|----------|
| 9-10 | Each recommendation names the campaign/channel, specific action, expected impact, owner, and timeline; prioritised by impact |
| 7-8 | Recommendations name the campaign and action; impact estimates are directional; most have owners |
| 5-6 | General recommendations ("increase budget on high-performing channels") without naming specifics |
| 3-4 | Vague suggestions ("optimise campaigns") that could apply to any report |
| 0-2 | No recommendations; report ends with data presentation |

### Report Clarity

| Score | Evidence |
|-------|----------|
| 9-10 | One-paragraph executive summary leads with the most important finding; format is consistent week-over-week; decision-makers can act within 5 minutes of reading |
| 7-8 | Executive summary present and useful; format mostly consistent; minor readability issues |
| 5-6 | Summary present but buries the lead; format changes between reports; takes 15+ minutes to extract key findings |
| 3-4 | No executive summary; report starts with detailed data; format inconsistent |
| 0-2 | Report is an unformatted data dump; no structure or narrative |
