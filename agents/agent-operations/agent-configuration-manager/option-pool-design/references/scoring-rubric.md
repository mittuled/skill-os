# Scoring Rubric: Option Pool Design

Evaluates the quality of initial compute allocation strategy.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Budget Breakdown Quality | 25% | Completeness of cost category breakdown |
| 2 | Tier Classification Accuracy | 25% | Appropriateness of high/medium/low agent grouping |
| 3 | Allocation Model Design | 25% | Budget distribution with scaling rules and growth headroom |
| 4 | Per-Agent Budget Specificity | 25% | Concrete assignments: model tier, max tokens, requests/day, context limits |
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

### Budget Breakdown Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Completeness of cost category breakdown; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Completeness of cost category breakdown; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Completeness of cost category breakdown; significant gaps but core elements present |
| 3-4 | Weakly addresses: Completeness of cost category breakdown; major gaps, core elements missing or vague |
| 0-2 | Does not address: Completeness of cost category breakdown; absent or fundamentally incomplete |

### Tier Classification Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Appropriateness of high/medium/low agent grouping; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Appropriateness of high/medium/low agent grouping; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Appropriateness of high/medium/low agent grouping; significant gaps but core elements present |
| 3-4 | Weakly addresses: Appropriateness of high/medium/low agent grouping; major gaps, core elements missing or vague |
| 0-2 | Does not address: Appropriateness of high/medium/low agent grouping; absent or fundamentally incomplete |

### Allocation Model Design

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Budget distribution with scaling rules and growth headroom; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Budget distribution with scaling rules and growth headroom; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Budget distribution with scaling rules and growth headroom; significant gaps but core elements present |
| 3-4 | Weakly addresses: Budget distribution with scaling rules and growth headroom; major gaps, core elements missing or vague |
| 0-2 | Does not address: Budget distribution with scaling rules and growth headroom; absent or fundamentally incomplete |

### Per-Agent Budget Specificity

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Concrete assignments: model tier, max tokens, requests/day, context limits; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Concrete assignments: model tier, max tokens, requests/day, context limits; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Concrete assignments: model tier, max tokens, requests/day, context limits; significant gaps but core elements present |
| 3-4 | Weakly addresses: Concrete assignments: model tier, max tokens, requests/day, context limits; major gaps, core elements missing or vague |
| 0-2 | Does not address: Concrete assignments: model tier, max tokens, requests/day, context limits; absent or fundamentally incomplete |
