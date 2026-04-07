# Scoring Rubric: Performance Tester

Evaluates the quality and thoroughness of performance and load testing against defined performance budgets.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Traffic Realism | 20% | How closely test traffic patterns match production access patterns |
| 2 | Budget Coverage | 25% | Completeness of metrics compared against performance budgets (P50/P95/P99, throughput, error rate) |
| 3 | Environment Parity | 20% | How closely the test environment matches production in provisioning and configuration |
| 4 | Diagnostic Depth | 15% | Quality of supporting data (flame graphs, slow queries, resource utilization) for regression analysis |
| 5 | Regression Detection | 20% | Accuracy of comparison against previous baseline with clear pass/fail verdict |
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
| A+ | 9.0 – 10.0 | Exceptional | Realistic traffic; all budgets measured at P50/P95/P99; production-like env; flame graphs captured; clear baseline comparison | Approve release; performance verified |
| A | 8.0 – 8.9 | Strong | Realistic traffic profiles; budgets checked; minor env differences documented; regressions identified | Approve with monitoring for flagged latency areas |
| B | 7.0 – 7.9 | Good | Good traffic patterns; most budgets checked; diagnostics available for regressions | Approve with caveats; address budget gaps next cycle |
| C | 5.0 – 6.9 | Adequate | Synthetic traffic; some budgets checked; averages reported instead of percentiles | Block; retest with realistic profiles and percentile reporting |
| D | 3.0 – 4.9 | Weak | Trivial load test; no budget comparison; under-provisioned environment | Block; full performance test required |
| F | 0.0 – 2.9 | Failing | No performance testing performed | Reject; performance validation mandatory for this release |

## Signal Tables

### Traffic Realism
| Score | Evidence |
|-------|----------|
| 9-10 | Traffic patterns derived from production access logs; ramp-up profile matches organic growth; concurrent user mix reflects real usage segments; data volumes match production |
| 7-8 | Traffic patterns based on production analytics; ramp-up reasonable; user mix approximated |
| 5-6 | Generic load profile (constant N users); no production-derived traffic shaping |
| 3-4 | Single endpoint hammered with fixed concurrency; no realistic scenario |
| 0-2 | No load generation or trivial single-request test |

### Budget Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | P50, P95, P99 latency measured for all critical flows; throughput (RPS) and error rate captured; all compared against documented budgets |
| 7-8 | P50 and P95 measured for critical flows; throughput captured; most budgets compared |
| 5-6 | Average latency reported; some percentiles for top endpoints; budgets partially compared |
| 3-4 | Only average response time reported; no percentile breakdown; no budget comparison |
| 0-2 | No metrics collected or metrics not compared to any budget |

### Environment Parity
| Score | Evidence |
|-------|----------|
| 9-10 | Test environment matches production in instance count, instance type, database size, and configuration; differences documented and impact assessed |
| 7-8 | Core infrastructure matches production; minor differences documented (e.g., reduced replica count) |
| 5-6 | Same stack but significantly under-provisioned; differences acknowledged but impact not assessed |
| 3-4 | Different infrastructure or configuration from production; results may not be comparable |
| 0-2 | Local development environment or no environment documentation |

### Diagnostic Depth
| Score | Evidence |
|-------|----------|
| 9-10 | CPU, memory, I/O, and network utilization captured; flame graphs for hot paths; slow query logs analyzed; GC pauses measured |
| 7-8 | Resource utilization captured; slow queries identified; flame graphs available for top bottlenecks |
| 5-6 | Basic CPU and memory metrics; no flame graphs or query analysis |
| 3-4 | Latency numbers only; no resource utilization data |
| 0-2 | No diagnostic data captured |

### Regression Detection
| Score | Evidence |
|-------|----------|
| 9-10 | Current results compared to documented baseline; regressions flagged with percentage change; statistical significance assessed; clear pass/fail verdict issued |
| 7-8 | Baseline comparison performed; regressions identified with magnitude; verdict provided |
| 5-6 | Previous results available but comparison is informal or incomplete |
| 3-4 | No baseline for comparison; results reported in isolation |
| 0-2 | No regression analysis performed |
