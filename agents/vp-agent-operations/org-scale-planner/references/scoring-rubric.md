# Scoring Rubric: Org Scale Planner

Evaluates the quality of an agent fleet scale plan.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Demand Assessment | 20% | Completeness of capability-to-requirement mapping with gap identification |
| 2 | Current State Audit | 15% | Accuracy of existing topology with utilization data |
| 3 | Topology Design | 25% | Clarity of target roles, boundaries, and coordination patterns |
| 4 | Provisioning Feasibility | 20% | Realism of sequencing, resources, and timeline |
| 5 | Migration Risk Management | 20% | Runbook quality including rollback triggers |
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

### Demand Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Completeness of capability-to-requirement mapping with gap identification; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Completeness of capability-to-requirement mapping with gap identification; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Completeness of capability-to-requirement mapping with gap identification; significant gaps but core elements present |
| 3-4 | Weakly addresses: Completeness of capability-to-requirement mapping with gap identification; major gaps, core elements missing or vague |
| 0-2 | Does not address: Completeness of capability-to-requirement mapping with gap identification; absent or fundamentally incomplete |

### Current State Audit

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Accuracy of existing topology with utilization data; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Accuracy of existing topology with utilization data; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Accuracy of existing topology with utilization data; significant gaps but core elements present |
| 3-4 | Weakly addresses: Accuracy of existing topology with utilization data; major gaps, core elements missing or vague |
| 0-2 | Does not address: Accuracy of existing topology with utilization data; absent or fundamentally incomplete |

### Topology Design

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Clarity of target roles, boundaries, and coordination patterns; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Clarity of target roles, boundaries, and coordination patterns; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Clarity of target roles, boundaries, and coordination patterns; significant gaps but core elements present |
| 3-4 | Weakly addresses: Clarity of target roles, boundaries, and coordination patterns; major gaps, core elements missing or vague |
| 0-2 | Does not address: Clarity of target roles, boundaries, and coordination patterns; absent or fundamentally incomplete |

### Provisioning Feasibility

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Realism of sequencing, resources, and timeline; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Realism of sequencing, resources, and timeline; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Realism of sequencing, resources, and timeline; significant gaps but core elements present |
| 3-4 | Weakly addresses: Realism of sequencing, resources, and timeline; major gaps, core elements missing or vague |
| 0-2 | Does not address: Realism of sequencing, resources, and timeline; absent or fundamentally incomplete |

### Migration Risk Management

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Runbook quality including rollback triggers; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Runbook quality including rollback triggers; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Runbook quality including rollback triggers; significant gaps but core elements present |
| 3-4 | Weakly addresses: Runbook quality including rollback triggers; major gaps, core elements missing or vague |
| 0-2 | Does not address: Runbook quality including rollback triggers; absent or fundamentally incomplete |
