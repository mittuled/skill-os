# Scoring Rubric: Tool Health Checker

Evaluates the quality of a tool health check execution.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Policy Coverage | 25% | Percentage of registered tools probed across all policy levels |
| 2 | Probe Accuracy | 25% | Correctness of health status classification (healthy/degraded/unreachable) |
| 3 | Report Completeness | 25% | Presence of tool name, status, latency, timestamp, and remediation per tool |
| 4 | Critical Alert Quality | 25% | Specificity and actionability of alerts for unreachable tools |
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
| A+ | 9.0 – 10.0 | Exceptional | All criteria fully met with evidence | Approve and schedule next review cycle |
| A | 8.0 – 8.9 | Strong | Minor gaps in 1-2 criteria | Approve with noted improvements for next cycle |
| B | 7.0 – 7.9 | Good | Moderate gaps in 2-3 criteria | Approve for use; address gaps within 30 days |
| C | 5.0 – 6.9 | Adequate | Significant gaps across multiple criteria | Revise before deployment; targeted improvements needed |
| D | 3.0 – 4.9 | Weak | Major gaps; core objectives not met | Return for substantial rework with specific guidance |
| F | 0.0 – 2.9 | Failing | Fundamentally incomplete or missing | Restart from requirements gathering |

## Signal Tables

### Policy Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Percentage of registered tools probed across all policy levels; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Percentage of registered tools probed across all policy levels; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Percentage of registered tools probed across all policy levels; significant gaps but core elements present |
| 3-4 | Weakly addresses: Percentage of registered tools probed across all policy levels; major gaps, core elements missing or vague |
| 0-2 | Does not address: Percentage of registered tools probed across all policy levels; absent or fundamentally incomplete |

### Probe Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Correctness of health status classification (healthy/degraded/unreachable); evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Correctness of health status classification (healthy/degraded/unreachable); minor gaps in completeness or evidence |
| 5-6 | Partially meets: Correctness of health status classification (healthy/degraded/unreachable); significant gaps but core elements present |
| 3-4 | Weakly addresses: Correctness of health status classification (healthy/degraded/unreachable); major gaps, core elements missing or vague |
| 0-2 | Does not address: Correctness of health status classification (healthy/degraded/unreachable); absent or fundamentally incomplete |

### Report Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Presence of tool name, status, latency, timestamp, and remediation per tool; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Presence of tool name, status, latency, timestamp, and remediation per tool; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Presence of tool name, status, latency, timestamp, and remediation per tool; significant gaps but core elements present |
| 3-4 | Weakly addresses: Presence of tool name, status, latency, timestamp, and remediation per tool; major gaps, core elements missing or vague |
| 0-2 | Does not address: Presence of tool name, status, latency, timestamp, and remediation per tool; absent or fundamentally incomplete |

### Critical Alert Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Specificity and actionability of alerts for unreachable tools; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Specificity and actionability of alerts for unreachable tools; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Specificity and actionability of alerts for unreachable tools; significant gaps but core elements present |
| 3-4 | Weakly addresses: Specificity and actionability of alerts for unreachable tools; major gaps, core elements missing or vague |
| 0-2 | Does not address: Specificity and actionability of alerts for unreachable tools; absent or fundamentally incomplete |
