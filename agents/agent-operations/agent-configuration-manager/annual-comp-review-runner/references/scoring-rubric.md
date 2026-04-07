# Scoring Rubric: Annual Comp Review Runner

Evaluates the quality of an annual configuration review.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Configuration Completeness | 20% | Coverage of model, compute, context window, tool access, and API scope per agent |
| 2 | Data-Driven Analysis | 25% | Use of actual performance and cost data vs assumptions |
| 3 | Right-Sizing Accuracy | 25% | Identification of over/under-provisioned agents with evidence |
| 4 | Change Proposal Quality | 15% | Specificity of proposals with cost impact estimates |
| 5 | Post-Change Validation | 15% | Verification that changes did not regress performance |
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

### Configuration Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Coverage of model, compute, context window, tool access, and API scope per agent; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Coverage of model, compute, context window, tool access, and API scope per agent; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Coverage of model, compute, context window, tool access, and API scope per agent; significant gaps but core elements present |
| 3-4 | Weakly addresses: Coverage of model, compute, context window, tool access, and API scope per agent; major gaps, core elements missing or vague |
| 0-2 | Does not address: Coverage of model, compute, context window, tool access, and API scope per agent; absent or fundamentally incomplete |

### Data-Driven Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Use of actual performance and cost data vs assumptions; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Use of actual performance and cost data vs assumptions; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Use of actual performance and cost data vs assumptions; significant gaps but core elements present |
| 3-4 | Weakly addresses: Use of actual performance and cost data vs assumptions; major gaps, core elements missing or vague |
| 0-2 | Does not address: Use of actual performance and cost data vs assumptions; absent or fundamentally incomplete |

### Right-Sizing Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Identification of over/under-provisioned agents with evidence; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Identification of over/under-provisioned agents with evidence; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Identification of over/under-provisioned agents with evidence; significant gaps but core elements present |
| 3-4 | Weakly addresses: Identification of over/under-provisioned agents with evidence; major gaps, core elements missing or vague |
| 0-2 | Does not address: Identification of over/under-provisioned agents with evidence; absent or fundamentally incomplete |

### Change Proposal Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Specificity of proposals with cost impact estimates; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Specificity of proposals with cost impact estimates; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Specificity of proposals with cost impact estimates; significant gaps but core elements present |
| 3-4 | Weakly addresses: Specificity of proposals with cost impact estimates; major gaps, core elements missing or vague |
| 0-2 | Does not address: Specificity of proposals with cost impact estimates; absent or fundamentally incomplete |

### Post-Change Validation

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Verification that changes did not regress performance; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Verification that changes did not regress performance; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Verification that changes did not regress performance; significant gaps but core elements present |
| 3-4 | Weakly addresses: Verification that changes did not regress performance; major gaps, core elements missing or vague |
| 0-2 | Does not address: Verification that changes did not regress performance; absent or fundamentally incomplete |
