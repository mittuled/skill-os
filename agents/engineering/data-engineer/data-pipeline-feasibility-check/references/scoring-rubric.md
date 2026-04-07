# Scoring Rubric: data-pipeline-feasibility-check

Evaluates the rigor and completeness of a data pipeline feasibility assessment covering source access, volume estimation, infrastructure readiness, and risk identification.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Source Access Verification | 35% | Actual connectivity, authentication, rate limit, and schema verification for each proposed source |
| 2 | Volume and Growth Estimation | 25% | Data volume profiled from actual samples with confidence intervals and growth projections |
| 3 | Infrastructure Gap Analysis | 20% | Compute, storage, and network requirements compared against available capacity with cost estimates |
| 4 | SLA Feasibility Assessment | 20% | Freshness SLA validated against source latency, pipeline compute time, and infrastructure constraints |
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
| A+ | 9.0 – 10.0 | Exceptional | All sources probed and verified; volume profiled with confidence intervals; infrastructure gap identified and costed; SLA validated end-to-end | Issue go verdict; proceed to pipeline design |
| A | 8.0 – 8.9 | Strong | All sources verified; volume estimated from samples; infrastructure gap identified; SLA achievable with minor provisioning | Issue conditional go; provision infrastructure gap before design starts |
| B | 7.0 – 7.9 | Good | Sources verified; volume estimated from partial sample; infrastructure adequate; SLA might require negotiation | Proceed with conditions: negotiate SLA buffer and complete volume profiling |
| C | 5.0 – 6.9 | Adequate | Sources partially verified; volume based on stakeholder estimate; infrastructure not checked; SLA not validated | Request full source verification and volume profile before re-assessment |
| D | 3.0 – 4.9 | Weak | 1-2 sources unverified; volume assumed; infrastructure check outstanding; SLA feasibility unknown | Do not proceed; block pipeline design until source access and volume are verified |
| F | 0.0 – 2.9 | Failing | No sources probed; volume and SLA based on assumptions only; no infrastructure analysis | Stop; return to stakeholder for requirements validation before any engineering work |

## Signal Tables

### Source Access Verification

| Score | Evidence |
|-------|----------|
| 9-10 | All sources probed programmatically: API call returns data, auth mechanism verified, rate limit measured (requests/min), response schema documented and compared against specification, pagination behavior confirmed |
| 7-8 | All sources probed; auth verified; rate limits documented from API docs or probing; minor schema discrepancy noted with workaround |
| 5-6 | All sources probed; auth confirmed; rate limits not verified through probing (using vendor documentation only); schema not fully validated |
| 3-4 | 50-79% sources probed; remaining sources assumed accessible based on previous integration or vendor claims |
| 0-2 | Less than 50% sources probed; access based on stakeholder assertion; no programmatic verification |

### Volume and Growth Estimation

| Score | Evidence |
|-------|----------|
| 9-10 | Volume profiled from actual data samples for each source: row counts per time window, payload size distribution (p50, p95), growth rate from historical data with 12-month projection and confidence intervals |
| 7-8 | Volume profiled from samples for primary sources; growth rate estimated from 3+ months of historical data; confidence intervals provided |
| 5-6 | Volume estimated from samples but without confidence intervals; growth rate is linear extrapolation without historical basis |
| 3-4 | Volume estimated from single sample snapshot; no growth analysis; order-of-magnitude only |
| 0-2 | Volume based on stakeholder statement ("a few million rows") without any data sampling or measurement |

### Infrastructure Gap Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Compute requirements estimated (CPU/memory/GPU per pipeline stage), storage requirements projected for 12 months, network bandwidth estimated for peak throughput, gap against current capacity identified, provisioning cost estimated and compared to budget |
| 7-8 | Compute and storage requirements estimated; gap identified; cost rough estimate; network bandwidth not analyzed |
| 5-6 | Compute requirements estimated; storage not analyzed; no cost estimate; gap identified but not quantified |
| 3-4 | Infrastructure requirements mentioned without estimation; current capacity not assessed; no gap analysis |
| 0-2 | No infrastructure analysis; pipeline assumed to fit within existing capacity without verification |

### SLA Feasibility Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | End-to-end latency budget computed: source extraction time + transformation time + load time vs. required freshness SLA; margin documented; worst-case scenario (source latency spike) analyzed; dependency SLAs from upstream sources documented |
| 7-8 | Latency budget estimated for primary path; SLA achievable under normal conditions; dependency SLAs referenced |
| 5-6 | SLA stated as feasible based on estimated pipeline runtime; worst-case not analyzed; no upstream dependency assessment |
| 3-4 | SLA requirement noted but feasibility not assessed against technical constraints; runtime not estimated |
| 0-2 | SLA accepted without any technical validation; no latency analysis |
