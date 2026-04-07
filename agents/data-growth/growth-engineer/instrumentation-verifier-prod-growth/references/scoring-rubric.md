# Scoring Rubric: instrumentation-verifier-prod-growth

Evaluates the health of growth instrumentation in the production environment across event volume stability, payload correctness, experiment distribution validity, and data warehouse ingestion.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Event Volume Stability | 30% | Production event volumes are within expected ranges versus 7-day baseline |
| 2 | Payload Correctness | 25% | Sampled event payloads contain correct and complete properties per spec |
| 3 | Experiment Distribution Validity | 25% | Active experiment variant assignments match configured allocation ratios |
| 4 | Data Warehouse Ingestion | 20% | Events are landing in the warehouse with acceptable latency and completeness |
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
| A+ | 9.0 – 10.0 | Exceptional | All events within ±5% of baseline; 100% payload compliance; variant splits within 1% of target; DW ingestion < 15 min lag | Ship experiment; no action needed |
| A | 8.0 – 8.9 | Strong | All critical events within ±20% of baseline; ≥95% payload compliance; variant splits within 2% of target; DW lag < 30 min | Monitor for 24h; proceed with confidence |
| B | 7.0 – 7.9 | Good | Most events within ±20%; 85–94% payload compliance; variant splits within 5%; DW lag < 1 hour | Log issues; fix within 48h; proceed with caution |
| C | 5.0 – 6.9 | Adequate | Some critical events ±20–40% from baseline; 70–84% payload compliance; minor SRM detected; DW lag 1–4 hours | Hold experiment launch; fix before proceeding |
| D | 3.0 – 4.9 | Weak | Critical events missing or >40% off baseline; <70% payload compliance; SRM exceeds 5%; DW lag >4 hours | Stop experiment; escalate hotfix; do not proceed |
| F | 0.0 – 2.9 | Failing | Critical growth events (signup, activation, purchase) completely absent; payloads corrupted; no variant assignment data; DW ingestion broken | Immediate hotfix; revert deploy if needed |

## Signal Tables

### Event Volume Stability

| Score | Evidence |
|-------|----------|
| 9-10 | All tracked growth events within ±5% of 7-day rolling average; no new zero-volume events; no unexplained spikes |
| 7-8 | All critical events (signup, activation, purchase) within ±20%; non-critical events have minor deviations with root cause identified |
| 5-6 | Critical events within ±20–30% of baseline; 1–2 non-critical events at zero volume; deviations partially explained |
| 3-4 | At least one critical event >30% off baseline or at zero volume for >1 hour; multiple unexplained deviations |
| 0-2 | Core growth events (signup completed, activation event, revenue event) completely absent or producing zero volume in production |

### Payload Correctness

| Score | Evidence |
|-------|----------|
| 9-10 | 50 sampled payloads: 100% have correct event names, all required properties present, UTM attribution populated, no null experiment_id where expected |
| 7-8 | ≥95% of sampled payloads spec-compliant; missing properties are non-critical (e.g., optional enrichment fields); UTM populated for ≥90% of events |
| 5-6 | 85–94% payload compliance; 1–2 required properties missing on minority of events; experiment_id missing on <10% of experiment events |
| 3-4 | 70–84% payload compliance; required properties (user_id, timestamp, variant_id) missing on >10% of events; UTM populated for <70% |
| 0-2 | <70% payload compliance; core properties (user_id, event_name) absent or corrupted; experiment events missing variant_id entirely |

### Experiment Distribution Validity

| Score | Evidence |
|-------|----------|
| 9-10 | All active experiments: variant assignment ratios within ±1% of configured allocation; chi-squared p-value > 0.5 for all experiments |
| 7-8 | All experiments within ±2% of target allocation; chi-squared p-value > 0.1; no evidence of systematic SRM |
| 5-6 | Most experiments within ±5% of allocation; 1 experiment shows chi-squared p < 0.1 but >0.05; investigated and explained by known technical cause |
| 3-4 | At least 1 experiment shows SRM (chi-squared p < 0.05, split >5% off target); cause unknown; experiment results unreliable |
| 0-2 | Multiple experiments show SRM; variant assignment events missing for active experiments; experiment data cannot be used for decision-making |

### Data Warehouse Ingestion

| Score | Evidence |
|-------|----------|
| 9-10 | All growth events present in DW within 15 minutes; row counts match source event counts within 0.1%; no duplicate rows |
| 7-8 | All growth events in DW within 30 minutes; row count match within 0.5%; <0.1% duplicate rows detected and filtered |
| 5-6 | Critical events in DW within 1 hour; row count match within 2%; minor duplicate issue flagged for investigation |
| 3-4 | Ingestion lag 1–4 hours for some critical events; row count discrepancy 2–10%; duplicate issue impacting metrics |
| 0-2 | Critical events missing from DW entirely or lag >4 hours; row count discrepancy >10%; growth dashboard metrics unreliable |
