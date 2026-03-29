# Scoring Rubric: performance-budget-setter

Sets performance budgets for load time, API latency, and resource consumption thresholds.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Critical Path Identification | 20% | Top 3-5 user interactions identified and ranked by frequency and business impact |
| 2 | Baseline Measurement | 25% | P50, P95, P99 latency collected from APM tools for each critical path |
| 3 | Budget Threshold Quality | 30% | Targets grounded in user research, competitive benchmarks, or conversion data with rationale |
| 4 | Enforcement Policy | 25% | Monitoring, CI checks, and breach response documented and agreed with engineering |
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
| A+ | 9.0 – 10.0 | Exceptional | Exceptional performance across all criteria | Budget ready for PRD integration and CI enforcement |
| A | 8.0 – 8.9 | Strong | Strong performance across all criteria | Budget viable with minor enforcement setup remaining |
| B | 7.0 – 7.9 | Good | Good performance across all criteria | Validate baseline measurements before finalising targets |
| C | 5.0 – 6.9 | Adequate | Adequate performance across all criteria | Instrumentation gaps — add APM coverage before setting budgets |
| D | 3.0 – 4.9 | Weak | Weak performance across all criteria | Insufficient data — instrument critical paths first |
| F | 0.0 – 2.9 | Failing | Failing performance across all criteria | No performance budget defined |

## Signal Tables

### Critical Path Identification

| Score | Evidence |
|-------|----------|
| 9-10 | Top 3-5 user interactions identified and ranked by frequency and business impact fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Top 3-5 user interactions identified and ranked by frequency and business impact mostly demonstrated with minor gaps |
| 5-6 | Top 3-5 user interactions identified and ranked by frequency and business impact partially present with significant gaps |
| 3-4 | Top 3-5 user interactions identified and ranked by frequency and business impact attempted but superficial or inconsistent |
| 0-2 | No evidence of critical path identification |

### Baseline Measurement

| Score | Evidence |
|-------|----------|
| 9-10 | P50, P95, P99 latency collected from APM tools for each critical path fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | P50, P95, P99 latency collected from APM tools for each critical path mostly demonstrated with minor gaps |
| 5-6 | P50, P95, P99 latency collected from APM tools for each critical path partially present with significant gaps |
| 3-4 | P50, P95, P99 latency collected from APM tools for each critical path attempted but superficial or inconsistent |
| 0-2 | No evidence of baseline measurement |

### Budget Threshold Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Targets grounded in user research, competitive benchmarks, or conversion data with rationale fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Targets grounded in user research, competitive benchmarks, or conversion data with rationale mostly demonstrated with minor gaps |
| 5-6 | Targets grounded in user research, competitive benchmarks, or conversion data with rationale partially present with significant gaps |
| 3-4 | Targets grounded in user research, competitive benchmarks, or conversion data with rationale attempted but superficial or inconsistent |
| 0-2 | No evidence of budget threshold quality |

### Enforcement Policy

| Score | Evidence |
|-------|----------|
| 9-10 | Monitoring, CI checks, and breach response documented and agreed with engineering fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Monitoring, CI checks, and breach response documented and agreed with engineering mostly demonstrated with minor gaps |
| 5-6 | Monitoring, CI checks, and breach response documented and agreed with engineering partially present with significant gaps |
| 3-4 | Monitoring, CI checks, and breach response documented and agreed with engineering attempted but superficial or inconsistent |
| 0-2 | No evidence of enforcement policy |
