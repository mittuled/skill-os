# Scoring Rubric: Tool Policy Manager

Evaluates the quality of tool policy management execution.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Policy Parse Accuracy | 20% | Correct loading of all policy levels from allowed-tools.yaml |
| 2 | Request Validation | 25% | Completeness of change request validation with conflict detection |
| 3 | Change Application Quality | 25% | Correct modification preserving YAML structure and comments |
| 4 | Schema Validation | 15% | Passing validation script post-change |
| 5 | Reporting Quality | 15% | Clear change summary with before/after diff |
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

### Policy Parse Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Correct loading of all policy levels from allowed-tools.yaml; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Correct loading of all policy levels from allowed-tools.yaml; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Correct loading of all policy levels from allowed-tools.yaml; significant gaps but core elements present |
| 3-4 | Weakly addresses: Correct loading of all policy levels from allowed-tools.yaml; major gaps, core elements missing or vague |
| 0-2 | Does not address: Correct loading of all policy levels from allowed-tools.yaml; absent or fundamentally incomplete |

### Request Validation

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Completeness of change request validation with conflict detection; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Completeness of change request validation with conflict detection; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Completeness of change request validation with conflict detection; significant gaps but core elements present |
| 3-4 | Weakly addresses: Completeness of change request validation with conflict detection; major gaps, core elements missing or vague |
| 0-2 | Does not address: Completeness of change request validation with conflict detection; absent or fundamentally incomplete |

### Change Application Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Correct modification preserving YAML structure and comments; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Correct modification preserving YAML structure and comments; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Correct modification preserving YAML structure and comments; significant gaps but core elements present |
| 3-4 | Weakly addresses: Correct modification preserving YAML structure and comments; major gaps, core elements missing or vague |
| 0-2 | Does not address: Correct modification preserving YAML structure and comments; absent or fundamentally incomplete |

### Schema Validation

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Passing validation script post-change; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Passing validation script post-change; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Passing validation script post-change; significant gaps but core elements present |
| 3-4 | Weakly addresses: Passing validation script post-change; major gaps, core elements missing or vague |
| 0-2 | Does not address: Passing validation script post-change; absent or fundamentally incomplete |

### Reporting Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Clear change summary with before/after diff; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Clear change summary with before/after diff; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Clear change summary with before/after diff; significant gaps but core elements present |
| 3-4 | Weakly addresses: Clear change summary with before/after diff; major gaps, core elements missing or vague |
| 0-2 | Does not address: Clear change summary with before/after diff; absent or fundamentally incomplete |
