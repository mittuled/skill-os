# Scoring Rubric: instrumentation-verifier-prod-data

Evaluates production instrumentation health after a deploy, covering event volume integrity, payload quality, and end-to-end pipeline delivery.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Event Volume Integrity | 35% | Post-deploy event volumes are within expected ranges for each tracked event, with no unexplained drops or spikes |
| 2 | Payload Quality | 35% | Sampled production payloads match the spec: correct property names, types, and value distributions |
| 3 | Pipeline Delivery | 30% | Events flow from client/server through the ingestion pipeline to the data warehouse within the expected latency SLA |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0–10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Verified | All volumes within ±10% of baseline, sampled payloads match spec, pipeline latency within SLA | Production instrumentation healthy; enable alerting and close verification |
| A | 8.0 – 8.9 | Near-verified | Volume deviations explained by traffic change; 1–2 minor payload issues; pipeline latency at SLA boundary | Monitor for 24h; alert on degradation |
| B | 7.0 – 7.9 | Conditionally verified | 1 event with unexplained volume deviation <30%; 1–2 property type issues in sampled payloads | Investigate volume anomaly; notify implementer of payload issues |
| C | 5.0 – 6.9 | Degraded | 1 event with >30% unexplained volume drop; multiple payload quality issues; pipeline latency occasionally exceeds SLA | Escalate to data engineering; consider reverting deploy if metric-critical event is affected |
| D | 3.0 – 4.9 | Significant failure | Multiple events with >30% volume deviation; systematic payload corruption; pipeline delays >2× SLA | Initiate hotfix; block any dependent dashboard updates |
| F | 0.0 – 2.9 | Critical failure | Multiple high-criticality events absent or near-zero volume; payloads unrecognizable from spec; pipeline not delivering to warehouse | Escalate to P0; revert deploy or issue immediate hotfix; notify data consumers of outage |

## Signal Tables

### Event Volume Integrity

| Score | Evidence |
|-------|----------|
| 9–10 | All events within ±10% of 7-day baseline volume after adjusting for observed traffic delta; no events with zero post-deploy volume; volume trend consistent with pre-deploy trajectory |
| 7–8 | 1–2 events with 10–20% volume deviation; deviation correlates with feature flag rollout percentage or traffic change; no zero-volume events |
| 5–6 | 1 event with 20–30% unexplained volume drop; 1 event with volume spike >2× baseline without a traffic explanation |
| 3–4 | 1 high-criticality event (funnel step, conversion event) with >30% volume drop; or 1 event with sustained near-zero volume for >2 hours post-deploy |
| 0–2 | Multiple events at near-zero volume; 1 north-star or revenue-critical event absent from production data for >1 hour; pipeline not receiving events from client |

### Payload Quality

| Score | Evidence |
|-------|----------|
| 9–10 | 50-sample payload inspection shows 100% spec compliance: correct property names (snake_case, no typos), types (integer/string/boolean as specified), enum values within allowed list, required properties never null |
| 7–8 | 95–99% of sampled properties correct; 1–2 optional properties absent in some payloads; no required properties null or wrong type |
| 5–6 | 80–94% compliance; 1–3 properties with type mismatch (e.g., numeric ID as string); 1 enum property sending values outside the allowed list |
| 3–4 | 60–79% compliance; required properties null in >10% of sample; systematic type error on a shared property affecting multiple events |
| 0–2 | <60% compliance; property names differ from spec; payloads missing multiple required properties; data in warehouse is largely unusable |

### Pipeline Delivery

| Score | Evidence |
|-------|----------|
| 9–10 | Events appear in data warehouse within defined latency SLA (e.g., <5 min for near-real-time, <24h for batch); event counts in warehouse match client/server send counts within 2%; no dead-letter queue accumulation |
| 7–8 | 90–95% of events delivered within SLA; <5% delivery delay (e.g., P99 latency 10% above SLA); dead-letter queue empty |
| 5–6 | 80–89% delivery within SLA; P99 latency 10–50% above SLA; 5–10% of events in warehouse with processing delay |
| 3–4 | 60–79% delivery within SLA; dead-letter queue accumulating; P99 latency >2× SLA; some events arriving late and missing from time-based dashboard windows |
| 0–2 | <60% delivery within SLA; significant dead-letter queue backlog; events not appearing in warehouse for >2 hours; dashboard metrics showing gaps consistent with pipeline failure |
