# Scoring Rubric: Technical Health Monitor

Evaluates the quality of enterprise technical health monitoring.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Metric Definition | 20% | Per-account technical metrics: API errors, uptime, latency, sync rates, auth failures |
| 2 | Monitoring Coverage | 20% | Instrumentation across all enterprise integrations |
| 3 | Review Quality | 25% | Degradation trend identification, capacity concerns, and risk assessment |
| 4 | Resolution Effectiveness | 20% | Root cause investigation quality and communication timeliness |
| 5 | Stakeholder Reporting | 15% | QBR-ready health summaries with risks and recommendations |
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

### Metric Definition

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Per-account technical metrics: API errors, uptime, latency, sync rates, auth failures; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Per-account technical metrics: API errors, uptime, latency, sync rates, auth failures; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Per-account technical metrics: API errors, uptime, latency, sync rates, auth failures; significant gaps but core elements present |
| 3-4 | Weakly addresses: Per-account technical metrics: API errors, uptime, latency, sync rates, auth failures; major gaps, core elements missing or vague |
| 0-2 | Does not address: Per-account technical metrics: API errors, uptime, latency, sync rates, auth failures; absent or fundamentally incomplete |

### Monitoring Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Instrumentation across all enterprise integrations; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Instrumentation across all enterprise integrations; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Instrumentation across all enterprise integrations; significant gaps but core elements present |
| 3-4 | Weakly addresses: Instrumentation across all enterprise integrations; major gaps, core elements missing or vague |
| 0-2 | Does not address: Instrumentation across all enterprise integrations; absent or fundamentally incomplete |

### Review Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Degradation trend identification, capacity concerns, and risk assessment; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Degradation trend identification, capacity concerns, and risk assessment; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Degradation trend identification, capacity concerns, and risk assessment; significant gaps but core elements present |
| 3-4 | Weakly addresses: Degradation trend identification, capacity concerns, and risk assessment; major gaps, core elements missing or vague |
| 0-2 | Does not address: Degradation trend identification, capacity concerns, and risk assessment; absent or fundamentally incomplete |

### Resolution Effectiveness

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Root cause investigation quality and communication timeliness; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Root cause investigation quality and communication timeliness; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Root cause investigation quality and communication timeliness; significant gaps but core elements present |
| 3-4 | Weakly addresses: Root cause investigation quality and communication timeliness; major gaps, core elements missing or vague |
| 0-2 | Does not address: Root cause investigation quality and communication timeliness; absent or fundamentally incomplete |

### Stakeholder Reporting

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: QBR-ready health summaries with risks and recommendations; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: QBR-ready health summaries with risks and recommendations; minor gaps in completeness or evidence |
| 5-6 | Partially meets: QBR-ready health summaries with risks and recommendations; significant gaps but core elements present |
| 3-4 | Weakly addresses: QBR-ready health summaries with risks and recommendations; major gaps, core elements missing or vague |
| 0-2 | Does not address: QBR-ready health summaries with risks and recommendations; absent or fundamentally incomplete |
