# Scoring Rubric: velocity-monitor

Evaluates team delivery health by assessing DORA metrics, sprint velocity trends, and the quality of root cause analysis and intervention recommendations.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Metric Coverage | 20% | Completeness of collected metrics: velocity, cycle time, lead time, deployment frequency, change failure rate, MTTR |
| 2 | Trend Analysis Quality | 25% | Statistical rigour of trend comparison against rolling averages with variance detection |
| 3 | Root Cause Depth | 25% | Quality of investigation into contributing factors behind flagged deviations |
| 4 | Risk Projection Accuracy | 15% | Reliability of forward projection against milestones and phase deadlines |
| 5 | Intervention Relevance | 15% | Specificity and expected impact of recommended corrective actions |
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
| A+ | 9.0 – 10.0 | Exceptional | All DORA metrics collected, trends analysed with statistical significance, root causes investigated with evidence, projections accurate, interventions specific and actionable | Distribute report; track intervention outcomes |
| A | 8.0 – 8.9 | Strong | Major metrics collected, trends analysed, root causes identified, projections reasonable | Distribute report; schedule intervention review |
| B | 7.0 – 7.9 | Good | Most metrics collected, trends identified, partial root cause analysis, projections directional | Review metric gaps; improve root cause methodology |
| C | 5.0 – 6.9 | Adequate | Some metrics collected, trends noted without statistical backing, root causes speculative | Address metric collection gaps before next report |
| D | 3.0 – 4.9 | Weak | Limited metrics, no trend analysis, no root cause investigation | Establish metric collection infrastructure |
| F | 0.0 – 2.9 | Failing | No metrics collected or analysed | Implement basic sprint tracking and CI/CD metrics collection |

## Signal Tables

### Metric Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Sprint velocity (planned vs. actual), cycle time per task, lead time (commit to deploy), deployment frequency, change failure rate, MTTR all collected from automated sources with no manual entry |
| 7-8 | Five of six metrics collected; one metric requires manual aggregation |
| 5-6 | Three to four metrics collected; DORA metrics partially available |
| 3-4 | Only sprint velocity collected; DORA metrics not available |
| 0-2 | No metrics collected from any source |

### Trend Analysis Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Current sprint compared against 6-sprint rolling average; standard deviation calculated; deviations exceeding 1.5 sigma flagged; seasonal patterns noted; visualization included |
| 7-8 | Comparison against 4-sprint average; significant deviations flagged; trends visualized |
| 5-6 | Current sprint compared to previous sprint only; trends described narratively without statistical backing |
| 3-4 | Metrics reported as single-point values without comparison |
| 0-2 | No trend analysis performed |

### Root Cause Depth

| Score | Evidence |
|-------|----------|
| 9-10 | Each flagged deviation investigated with specific contributing factors identified (scope changes, dependency blocks, tech debt, team changes, incident load); evidence cited (ticket IDs, incident reports, PR data) |
| 7-8 | Major deviations investigated with contributing factors identified; some evidence cited |
| 5-6 | Deviations acknowledged with probable causes hypothesized without evidence |
| 3-4 | Deviations noted without investigation |
| 0-2 | No investigation of any deviation |

### Risk Projection Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Current velocity projected forward against all remaining milestones; at-risk deliverables identified with specific shortfall quantified; projection methodology stated |
| 7-8 | Projection against next milestone; at-risk items identified |
| 5-6 | General statement about timeline risk without quantification |
| 3-4 | No forward projection; report is backward-looking only |
| 0-2 | No risk assessment of any kind |

### Intervention Relevance

| Score | Evidence |
|-------|----------|
| 9-10 | Each intervention tied to a specific root cause; expected impact quantified (e.g., "reallocating 1 engineer recovers 8 points/sprint"); owner and timeline assigned |
| 7-8 | Interventions tied to root causes; impact described qualitatively; owners suggested |
| 5-6 | Generic interventions listed without connection to specific root causes |
| 3-4 | Interventions mentioned in passing without detail |
| 0-2 | No interventions recommended |
