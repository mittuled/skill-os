# Scoring Rubric: Infrastructure Load Testing

Evaluates the thoroughness and quality of load testing execution against infrastructure performance targets.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Test Planning | 20% | Scenario coverage, realistic traffic patterns, and clear SLO targets |
| 2 | Environment Fidelity | 20% | How closely the test environment mirrors production topology and data |
| 3 | Execution Rigour | 25% | Proper ramp-up, baseline establishment, and break-point identification |
| 4 | Analysis Depth | 20% | Bottleneck identification, percentile-based latency analysis, and resource correlation |
| 5 | Actionability | 15% | Specificity of remediation recommendations with priority and ownership |
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
| A+ | 9.0 – 10.0 | Exceptional | Comprehensive testing with break-point analysis, actionable findings, and validated SLO compliance | Approve for production deployment |
| A | 8.0 – 8.9 | Strong | Thorough testing with minor gaps in edge-case coverage or remediation detail | Approve with follow-up testing for flagged scenarios |
| B | 7.0 – 7.9 | Good | Solid testing but missing break-point analysis or dependency load inclusion | Approve conditionally; complete missing test dimensions |
| C | 5.0 – 6.9 | Adequate | Basic load testing done but environment fidelity low or analysis superficial | Retest with improved environment and deeper analysis |
| D | 3.0 – 4.9 | Weak | Single-rate testing only; no bottleneck identification; results not actionable | Redesign test plan and re-execute |
| F | 0.0 – 2.9 | Failing | No meaningful load testing; performance characteristics unknown | Block deployment until load testing completes |

## Signal Tables

### Test Planning

| Score | Evidence |
|-------|----------|
| 9-10 | Scenarios based on production traffic analysis; multiple load profiles (steady, spike, soak); SLOs mapped to specific metrics with thresholds |
| 7-8 | Scenarios cover primary user journeys; steady and peak profiles defined; SLOs stated but some metrics lack thresholds |
| 5-6 | Single scenario based on estimated traffic; only one load profile; SLOs partially defined |
| 3-4 | Ad-hoc scenario without traffic analysis; no defined SLOs; arbitrary load levels |
| 0-2 | No test plan; load testing executed without scenario definition |

### Environment Fidelity

| Score | Evidence |
|-------|----------|
| 9-10 | Production-mirror topology; realistic data volumes; all dependencies included; monitoring identical to production |
| 7-8 | Production-like topology with minor differences documented; most dependencies included; monitoring configured |
| 5-6 | Scaled-down environment with documented differences; some dependencies stubbed; basic monitoring |
| 3-4 | Significantly different topology; most dependencies mocked; minimal monitoring |
| 0-2 | Local or developer environment; no resemblance to production |

### Execution Rigour

| Score | Evidence |
|-------|----------|
| 9-10 | Warm-up phase, steady-state baseline, ramp to target, ramp to break-point; multiple iterations for consistency |
| 7-8 | Warm-up and ramp included; break-point identified; single iteration |
| 5-6 | Ramp to target only; no break-point testing; no warm-up consideration |
| 3-4 | Fixed-rate test only; no ramp; cold-start measurements included |
| 0-2 | Single request batch with no load pattern |

### Analysis Depth

| Score | Evidence |
|-------|----------|
| 9-10 | Percentile latency distributions (p50/p95/p99); resource utilization correlation (CPU, memory, I/O, network); first bottleneck identified; cascading failure analysis |
| 7-8 | Percentile latencies reported; resource utilization tracked; bottleneck identified but no cascading analysis |
| 5-6 | Average latency and error rates reported; some resource metrics; bottleneck suspected but not confirmed |
| 3-4 | Only success/failure counts; no latency distribution; no resource correlation |
| 0-2 | No analysis; raw tool output only |

### Actionability

| Score | Evidence |
|-------|----------|
| 9-10 | Specific recommendations with code/config changes, priority ranking, estimated impact, and assigned owners |
| 7-8 | Recommendations with specific changes and priority; ownership not yet assigned |
| 5-6 | General recommendations ("add caching", "scale horizontally") without specific implementation guidance |
| 3-4 | Observations without recommendations |
| 0-2 | No findings communicated |
