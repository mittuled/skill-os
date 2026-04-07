# Framework: Pipeline Scale Planner

Defines the methodology for capacity planning, bottleneck analysis, and scaling strategy design for data pipelines.

## Scaling Strategy Taxonomy

| Strategy | Applies To | Complexity | Cost Model |
|---------|-----------|-----------|-----------|
| Horizontal partitioning | Extract and load phases with large row volumes | Low-Medium | Linear with partition count |
| Parallel extraction | Multi-endpoint or multi-tenant sources | Low | Linear with source count |
| Incremental processing (CDC / watermark) | Full-reload pipelines that process data that has not changed | Low | Reduces compute by 80-95% vs. full reload |
| Pre-aggregation / materialized views | Transformation bottlenecks on analytical queries | Medium | Storage cost for materialized data |
| Infrastructure upgrade (vertical) | CPU/memory-bound transforms as a short-term fix only | Low effort, high cost ceiling | Super-linear cost growth |
| Stream processing migration | Pipelines where batch SLA cannot be met at scale | High | Higher infrastructure; lower latency |

## Capacity Forecast Model

### Data Growth Estimation

```
Projected daily volume (day N) = current_daily_volume × (1 + daily_growth_rate)^N

Where:
  daily_growth_rate = (total_growth_rate)^(1/365) − 1
  total_growth_rate sourced from:
    - Historical trend: CAGR over last 12 months
    - Business plan: expected user/transaction growth from finance
    - Whichever is higher = conservative assumption
```

### SLA Breach Date Projection

```
SLA breach date = today + log(SLA_window / current_duration) / log(1 + daily_growth_rate)
```

If SLA breach < 90 days: urgent; begin scaling now.
If SLA breach 90–180 days: plan scaling; start implementation next sprint.
If SLA breach > 180 days: monitor; re-assess quarterly.

## Bottleneck Classification

| Bottleneck Type | Diagnostic Signal | Scaling Intervention |
|----------------|-----------------|---------------------|
| I/O bound (extraction) | Source API rate limiting; extraction occupies >60% of pipeline duration | Parallel extraction with partition keys; increase connection pool |
| Shuffle-heavy (Spark) | Spill-to-disk in execution plan; OOM errors | Repartition before heavy joins; broadcast small tables |
| Write amplification (load) | Load task takes longer than transform despite fewer rows | Switch from INSERT to MERGE; partition target table by load date |
| Memory-bound transform | OOM errors on executor nodes; GC overhead in logs | Increase executor memory (short-term); refactor to avoid full-table in-memory operations |
| SQL query performance | Transform SQL has full table scans; execution plan shows sort without index | Add clustering keys or materialized views; rewrite joins |

## Cost-Benefit Analysis Template

For each scaling intervention, evaluate:

| Factor | Questions to Answer |
|--------|-------------------|
| Cost delta | What is the monthly infrastructure cost change? |
| SLA extension | How many additional months of SLA compliance does this provide? |
| Engineering effort | How many engineer-days to implement? |
| Reversibility | Can this be undone if it creates new problems? |
| Debt risk | Does this create architectural debt that must be paid later? |

**Decision rule**: Choose the intervention with the best (SLA extension in months / cost delta in $/month) ratio, where engineering effort ≤ 2 sprints.

## Validation Protocol

| Test Type | Method | Pass Criteria |
|-----------|--------|--------------|
| Load test | Run pipeline against a 3× volume test dataset | Completes within SLA window |
| Canary deployment | Route 10% of pipeline load to new architecture | No data quality regressions; latency within target |
| A/B comparison | Run old and new pipeline in parallel; compare outputs | Row counts match within 0.1%; aggregates match within rounding |
| Regression test | Re-run historical week against expected output | Outputs identical to pre-scaling baseline |
