# Scoring Rubric: Sla Definer Cs

Evaluates the quality of CS SLA definitions.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Segmentation Quality | 25% | Appropriateness of tier assignments based on value, complexity, and strategy |
| 2 | SLA Metric Specificity | 25% | Measurability of per-tier commitments with realistic targets |
| 3 | Escalation Matrix Quality | 20% | Completeness of severity levels with response time requirements |
| 4 | Documentation Clarity | 15% | Internal and external SLA documentation quality |
| 5 | Monitoring Setup | 15% | Automated tracking and breach alerting configuration |
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

### Segmentation Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Appropriateness of tier assignments based on value, complexity, and strategy; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Appropriateness of tier assignments based on value, complexity, and strategy; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Appropriateness of tier assignments based on value, complexity, and strategy; significant gaps but core elements present |
| 3-4 | Weakly addresses: Appropriateness of tier assignments based on value, complexity, and strategy; major gaps, core elements missing or vague |
| 0-2 | Does not address: Appropriateness of tier assignments based on value, complexity, and strategy; absent or fundamentally incomplete |

### SLA Metric Specificity

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Measurability of per-tier commitments with realistic targets; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Measurability of per-tier commitments with realistic targets; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Measurability of per-tier commitments with realistic targets; significant gaps but core elements present |
| 3-4 | Weakly addresses: Measurability of per-tier commitments with realistic targets; major gaps, core elements missing or vague |
| 0-2 | Does not address: Measurability of per-tier commitments with realistic targets; absent or fundamentally incomplete |

### Escalation Matrix Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Completeness of severity levels with response time requirements; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Completeness of severity levels with response time requirements; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Completeness of severity levels with response time requirements; significant gaps but core elements present |
| 3-4 | Weakly addresses: Completeness of severity levels with response time requirements; major gaps, core elements missing or vague |
| 0-2 | Does not address: Completeness of severity levels with response time requirements; absent or fundamentally incomplete |

### Documentation Clarity

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Internal and external SLA documentation quality; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Internal and external SLA documentation quality; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Internal and external SLA documentation quality; significant gaps but core elements present |
| 3-4 | Weakly addresses: Internal and external SLA documentation quality; major gaps, core elements missing or vague |
| 0-2 | Does not address: Internal and external SLA documentation quality; absent or fundamentally incomplete |

### Monitoring Setup

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Automated tracking and breach alerting configuration; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Automated tracking and breach alerting configuration; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Automated tracking and breach alerting configuration; significant gaps but core elements present |
| 3-4 | Weakly addresses: Automated tracking and breach alerting configuration; major gaps, core elements missing or vague |
| 0-2 | Does not address: Automated tracking and breach alerting configuration; absent or fundamentally incomplete |
