# Scoring Rubric: north-star-metric-reviewer-data

Evaluates the validity and actionability of the current north star metric across correlation to business outcomes, actionability by product teams, measurability, definition clarity, and alignment with the current business model.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Revenue & Retention Correlation | 30% | Pearson r between north star and trailing 90-day revenue and Day-30 retention |
| 2 | Actionability | 25% | Whether product/growth levers demonstrably move the metric |
| 3 | Measurability | 20% | Instrumentation completeness, data quality, and absence of sampling bias |
| 4 | Definition Clarity | 15% | Stakeholder alignment on the metric's exact calculation and cohort scope |
| 5 | Business Model Fit | 10% | Whether the metric reflects the current value proposition and monetization model |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Pearson r > 0.8 with revenue and retention; recent experiments moved the metric; no instrumentation gaps; all stakeholders agree on definition | Retain; schedule next review in 90 days |
| A | 8.0 – 8.9 | Strong | Pearson r 0.7–0.8; most experiments target the metric; minor instrumentation gaps; definitions aligned with one clarification needed | Retain with minor definition cleanup |
| B | 7.0 – 7.9 | Good | Pearson r 0.6–0.7; some experiments do not target the metric; one instrumentation gap; moderate stakeholder definition drift | Refine definition or measurement approach this quarter |
| C | 5.0 – 6.9 | Adequate | Pearson r 0.5–0.6; metric moved in fewer than half of experiments that targeted it; significant instrumentation gaps; stakeholder definitions diverge | Refine or replace candidate identified; launch 30-day transition plan |
| D | 3.0 – 4.9 | Weak | Pearson r < 0.5; metric unmoved by recent product investment; unreliable instrumentation; stakeholders use different definitions | Replace: propose alternative north star with data evidence |
| F | 0.0 – 2.9 | Failing | No correlation analysis possible; metric not tracked; teams operate without reference to north star | Halt north star usage; instrument and redefine from scratch |

## Signal Tables

### Revenue & Retention Correlation

| Score | Evidence |
|-------|----------|
| 9-10 | Pearson r ≥ 0.8 between north star and trailing 90-day revenue AND Day-30 retention; statistically significant (p < 0.05); n ≥ 90 days of data |
| 7-8 | Pearson r 0.65–0.79 with at least one of revenue or retention; p < 0.05; minor confounders identified but controlled for |
| 5-6 | Pearson r 0.5–0.64; p < 0.10; correlation analysis performed but sample is seasonal or confounded; directional relationship apparent |
| 3-4 | Pearson r 0.3–0.49; relationship weak; or analysis performed on fewer than 30 data points; statistical significance not established |
| 0-2 | Pearson r < 0.3 or correlation analysis not possible due to missing data; no relationship between north star and business outcomes demonstrated |

### Actionability

| Score | Evidence |
|-------|----------|
| 9-10 | 3+ recent experiments explicitly targeted this metric; ≥ 2 produced statistically significant movement; top product levers documented and validated |
| 7-8 | 2 experiments targeted the metric in the past 2 quarters; at least 1 produced significant movement; growth team can name 3 levers to move it |
| 5-6 | 1 experiment targeted the metric; inconclusive result; team can hypothesize levers but none validated; or metric moved as a side effect of other work |
| 3-4 | No recent experiments directly targeting this metric; team uncertain which levers influence it; metric movement correlated with external factors |
| 0-2 | No experiments have ever targeted this metric; team cannot identify product levers; metric moves only with market conditions |

### Measurability

| Score | Evidence |
|-------|----------|
| 9-10 | 100% instrumentation coverage across all platforms; zero data quality failures in last 30 days; no sampling bias detected; refreshes on defined SLA |
| 7-8 | ≥ 95% platform coverage; 1–2 minor data quality alerts in last 30 days (resolved); calculation verified against source data |
| 5-6 | 80–94% platform coverage; known sampling gap on 1 platform; periodic data quality issues that require manual correction |
| 3-4 | < 80% platform coverage; significant instrumentation gaps; metric requires manual backfilling or workaround query |
| 0-2 | Metric is not reliably measurable; no verified instrumentation; calculation is approximate or manually computed ad hoc |

### Definition Clarity

| Score | Evidence |
|-------|----------|
| 9-10 | All 5 surveyed stakeholders state identical definition (formula, time window, cohort); definition is documented and linked from all dashboards |
| 7-8 | 4 of 5 stakeholders aligned; one has minor variant (different time window or cohort); written definition exists and is accessible |
| 5-6 | 3 of 5 stakeholders aligned; two use different definitions; written definition exists but is not consistently referenced |
| 3-4 | Fewer than 3 stakeholders agree on definition; conflicting numbers appear in different reports; no authoritative written definition |
| 0-2 | No shared understanding of what the north star metric means; each team computes it differently; widespread distrust of the number |

### Business Model Fit

| Score | Evidence |
|-------|----------|
| 9-10 | Metric directly reflects the unit of value delivery in the current pricing/monetization model; unchanged since last business model review |
| 7-8 | Metric reflects 80%+ of current value proposition; minor product areas not captured; business model has not materially changed |
| 5-6 | Metric reflects the original product hypothesis but the product has evolved; significant new features or segments are not reflected |
| 3-4 | Business model changed (new pricing tier, new segment, pivot) in the last 6 months; metric predates the change and no longer aligns |
| 0-2 | Metric is a vestige of a prior strategy; the product and monetization model have fundamentally changed; metric provides no strategic signal |
