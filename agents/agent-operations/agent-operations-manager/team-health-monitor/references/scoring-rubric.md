# Scoring Rubric: Team Health Monitor

Evaluates the quality of a fleet health monitoring system.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Metric Definition Quality | 25% | Completeness of per-role metrics with thresholds for healthy/warning/critical |
| 2 | Instrumentation Coverage | 20% | Data collection setup across all agents with sufficient granularity |
| 3 | Anomaly Detection | 25% | Effectiveness of threshold-based and trend-based anomaly identification |
| 4 | Diagnosis Depth | 15% | Root cause analysis quality for detected anomalies |
| 5 | Escalation Effectiveness | 15% | Timeliness and appropriateness of escalation with actionable context |
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

### Metric Definition Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Completeness of per-role metrics with thresholds for healthy/warning/critical; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Completeness of per-role metrics with thresholds for healthy/warning/critical; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Completeness of per-role metrics with thresholds for healthy/warning/critical; significant gaps but core elements present |
| 3-4 | Weakly addresses: Completeness of per-role metrics with thresholds for healthy/warning/critical; major gaps, core elements missing or vague |
| 0-2 | Does not address: Completeness of per-role metrics with thresholds for healthy/warning/critical; absent or fundamentally incomplete |

### Instrumentation Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Data collection setup across all agents with sufficient granularity; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Data collection setup across all agents with sufficient granularity; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Data collection setup across all agents with sufficient granularity; significant gaps but core elements present |
| 3-4 | Weakly addresses: Data collection setup across all agents with sufficient granularity; major gaps, core elements missing or vague |
| 0-2 | Does not address: Data collection setup across all agents with sufficient granularity; absent or fundamentally incomplete |

### Anomaly Detection

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Effectiveness of threshold-based and trend-based anomaly identification; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Effectiveness of threshold-based and trend-based anomaly identification; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Effectiveness of threshold-based and trend-based anomaly identification; significant gaps but core elements present |
| 3-4 | Weakly addresses: Effectiveness of threshold-based and trend-based anomaly identification; major gaps, core elements missing or vague |
| 0-2 | Does not address: Effectiveness of threshold-based and trend-based anomaly identification; absent or fundamentally incomplete |

### Diagnosis Depth

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Root cause analysis quality for detected anomalies; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Root cause analysis quality for detected anomalies; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Root cause analysis quality for detected anomalies; significant gaps but core elements present |
| 3-4 | Weakly addresses: Root cause analysis quality for detected anomalies; major gaps, core elements missing or vague |
| 0-2 | Does not address: Root cause analysis quality for detected anomalies; absent or fundamentally incomplete |

### Escalation Effectiveness

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Timeliness and appropriateness of escalation with actionable context; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Timeliness and appropriateness of escalation with actionable context; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Timeliness and appropriateness of escalation with actionable context; significant gaps but core elements present |
| 3-4 | Weakly addresses: Timeliness and appropriateness of escalation with actionable context; major gaps, core elements missing or vague |
| 0-2 | Does not address: Timeliness and appropriateness of escalation with actionable context; absent or fundamentally incomplete |
