# Framework: Alerting Configurator

Defines the structural approach for designing metric alert systems that surface real anomalies while suppressing predictable noise.

## Alert Architecture

### Threshold Taxonomy

| Alert Type | When to Use | Detection Method | Example |
|------------|-------------|-----------------|---------|
| Static threshold | Absolute business floor/ceiling; hard SLAs | Fixed value comparison | DAU < 1,000 = P0 |
| Dynamic threshold | Metrics with growth trends or drift | Rolling average ± N×σ (z-score) | Conversion rate drops > 2σ below 30-day mean |
| Anomaly detection | Seasonal or high-cardinality metrics | STL decomposition, CUSUM | Weekend DAU spike or holiday suppression |
| Rate-of-change | Rapid deterioration (e.g., error spikes) | % change over N minutes | Error rate +50% in 15 min |

### Severity Tiers

| Tier | Label | Definition | Response SLA | Escalation Path |
|------|-------|-----------|-------------|----------------|
| P0 | Critical | North star metric or revenue-impacting regression | 15 min | On-call engineer + Analytics Lead |
| P1 | High | Funnel conversion drops > 10% from baseline | 1 hour | Analytics Lead |
| P2 | Medium | Secondary KPI deviates > 2σ with no known cause | 4 hours | Owning analyst |
| P3 | Low | Metric approaches threshold but has not crossed | Next business day | Owning analyst |

### Metric Criticality Tiers

| Tier | Description | Alert Types Required |
|------|-------------|---------------------|
| North star | Single defining business metric | Static + dynamic + anomaly |
| Primary KPIs | Top 5 business-facing metrics | Static + dynamic |
| Secondary KPIs | Supporting metrics, funnel steps | Dynamic |
| Operational | Pipeline health, event volume | Static |

## Threshold Calibration Protocol

1. Pull trailing 30-day daily values for the metric.
2. Calculate mean (μ) and standard deviation (σ).
3. Set warning threshold at μ − 1.5σ; critical threshold at μ − 2.5σ.
4. For seasonal metrics: run STL decomposition to extract trend and residual; apply thresholds to the residual component.
5. Backtest against 90-day history: count false positives (alerts on normal variance) and false negatives (missed events).
6. Tune until FP rate < 10% and FN rate < 5% for P0/P1 metrics.

## Escalation Design

```
Alert fires
  └── P0/P1 → PagerDuty → on-call rotation → if unacknowledged 15 min → manager escalation
  └── P2 → Slack #data-alerts → owning analyst DM → 4-hour resolve SLA
  └── P3 → Slack #data-health → weekly triage queue
```

## Ownership Rules

- Every alert must have exactly one named owner (not a team — a person).
- Owner is responsible for acknowledgement within SLA and root-cause documentation.
- Ownership transfers with role changes; no orphaned alerts permitted.
- Review ownership quarterly during the data team retrospective.
