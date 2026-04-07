# Scoring Rubric: north-star-metric-reviewer-finance

Evaluates whether the company's north star metric aligns with financial outcomes, investor expectations, and long-term business health.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Financial Correlation | 35% | Statistical and logical relationship between the north star metric and ARR, gross margin, or cash flow |
| 2 | Leading Indicator Quality | 25% | Whether the metric predicts future financial outcomes with sufficient lead time to enable action |
| 3 | Investor Stage Alignment | 20% | Whether investors at the company's current stage and sector recognize and value this metric |
| 4 | Measurement Reliability | 10% | Whether the metric can be measured consistently, accurately, and without gaming incentives |
| 5 | Operational Influence | 10% | Whether the company can meaningfully move the metric through its own actions |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = absent/completely broken, 5 = functional with significant gaps, 10 = best-in-class alignment

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | Metric has strong statistical correlation (r > 0.8) with ARR; investors cite it unprompted; measured reliably daily; fully within the company's operational control | Maintain; feature prominently in investor communications and board reporting |
| A | 8.0–8.9 | Strong | Metric correlates with financial outcomes with minor lag; investor-recognized; measured weekly with high confidence | Use as primary KPI; document correlation methodology for investor diligence |
| B | 7.0–7.9 | Good | Metric has logical but unquantified correlation to financial outcomes; investors familiar but not universally cited | Continue using; build a formal correlation study to strengthen the narrative |
| C | 5.0–6.9 | Adequate | Metric shows mixed or lagging correlation to financials; some investors question its relevance | Investigate correlation gaps; consider adding a bridging metric that connects to revenue |
| D | 3.0–4.9 | Weak | Metric is growing but does not translate to financial improvement; investors require extensive explanation | Replace or supplement with a metric that has clearer financial connection; conduct investor survey |
| F | 0.0–2.9 | Failing | Metric is disconnected from financial outcomes; investors actively skeptical; may be a vanity metric | Replace immediately; do not feature in fundraising materials until the financial link is established |

## Signal Tables

### Financial Correlation

| Score | Evidence |
|-------|----------|
| 9–10 | Pearson r ≥ 0.8 between the north star metric and trailing 12-month ARR growth; statistical significance confirmed; correlation holds across cohorts |
| 7–8 | Clear logical relationship documented; directional correlation confirmed over 6+ months of data; some lag or noise present |
| 5–6 | Positive correlation in 3 of the last 6 months; exceptions have explanations but correlation is inconsistent |
| 3–4 | Metric growing while ARR is flat or declining for 2+ consecutive quarters; no structural explanation for the divergence |
| 0–2 | Metric and ARR have moved in opposite directions for 3+ quarters; no causal pathway exists between the metric and revenue |

### Leading Indicator Quality

| Score | Evidence |
|-------|----------|
| 9–10 | Metric leads ARR changes by 60–90 days; company has acted on metric signals and confirmed revenue response within the predicted window |
| 7–8 | Metric leads ARR by 30–60 days with documented examples; company uses it for resource allocation decisions |
| 5–6 | Metric is roughly coincident with ARR changes; some leading quality but insufficient lead time for operational response |
| 3–4 | Metric lags ARR changes; it confirms what already happened rather than predicting what will happen |
| 0–2 | No identifiable lead-lag relationship; metric provides no predictive value for financial planning |

### Investor Stage Alignment

| Score | Evidence |
|-------|----------|
| 9–10 | Three or more investor meetings where investors cited this specific metric as a key diligence focus; metric appears in sector-specific VC frameworks (e.g., a16z, Bessemer benchmarks) |
| 7–8 | Investors acknowledge the metric's relevance without prompting; no investor has challenged the metric's validity during diligence |
| 5–6 | Some investors accept the metric; 1–2 investors have asked for supplementary metrics to contextualize it |
| 3–4 | Multiple investors have questioned whether the metric reflects business health; investors prefer different metrics for the sector or stage |
| 0–2 | Investors consistently redirect to standard financial or product metrics; the north star metric is not recognized as meaningful in the sector |

### Measurement Reliability

| Score | Evidence |
|-------|----------|
| 9–10 | Metric definition documented; automated tracking with daily data freshness; no known gaming incentives; consistent methodology for 12+ months |
| 7–8 | Metric defined and tracked automatically; methodology consistent for 6+ months; minor definitional edge cases documented |
| 5–6 | Metric tracked manually or semi-automatically; occasional definition changes; some teams use slightly different calculations |
| 3–4 | Different teams report different values for the same metric; manual calculation with spreadsheet errors possible; definition disputed internally |
| 0–2 | Metric cannot be reliably measured with current data infrastructure; estimates vary by 20%+ depending on methodology |

### Operational Influence

| Score | Evidence |
|-------|----------|
| 9–10 | Company has run and completed 3+ experiments that directly moved the metric; clear operational levers identified and tested |
| 7–8 | Company can identify 3+ specific actions that influence the metric; at least one experiment has confirmed the causal effect |
| 5–6 | Company believes it can influence the metric but has run fewer than 2 confirmed experiments; levers are hypothetical |
| 3–4 | Metric is largely driven by external factors (market demand, macroeconomic conditions) outside the company's direct control |
| 0–2 | Company cannot identify actions that reliably move the metric; metric is purely a measurement outcome, not a managed variable |
