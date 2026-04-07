# Scoring Rubric: Employment Agreement Setup

Evaluates the quality of agent interaction contracts.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Template Completeness | 25% | Coverage of input schema, output format, error handling, timeout, and context passing |
| 2 | Per-Agent Specificity | 25% | Role-specific customization of contracts with SLA expectations |
| 3 | Validation Coverage | 20% | Thoroughness of contract testing with representative inputs |
| 4 | Versioning Discipline | 15% | Version management with migration paths for contract changes |
| 5 | Runtime Enforcement | 15% | Monitoring configuration for detecting contract violations |
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

### Template Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Coverage of input schema, output format, error handling, timeout, and context passing; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Coverage of input schema, output format, error handling, timeout, and context passing; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Coverage of input schema, output format, error handling, timeout, and context passing; significant gaps but core elements present |
| 3-4 | Weakly addresses: Coverage of input schema, output format, error handling, timeout, and context passing; major gaps, core elements missing or vague |
| 0-2 | Does not address: Coverage of input schema, output format, error handling, timeout, and context passing; absent or fundamentally incomplete |

### Per-Agent Specificity

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Role-specific customization of contracts with SLA expectations; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Role-specific customization of contracts with SLA expectations; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Role-specific customization of contracts with SLA expectations; significant gaps but core elements present |
| 3-4 | Weakly addresses: Role-specific customization of contracts with SLA expectations; major gaps, core elements missing or vague |
| 0-2 | Does not address: Role-specific customization of contracts with SLA expectations; absent or fundamentally incomplete |

### Validation Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Thoroughness of contract testing with representative inputs; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Thoroughness of contract testing with representative inputs; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Thoroughness of contract testing with representative inputs; significant gaps but core elements present |
| 3-4 | Weakly addresses: Thoroughness of contract testing with representative inputs; major gaps, core elements missing or vague |
| 0-2 | Does not address: Thoroughness of contract testing with representative inputs; absent or fundamentally incomplete |

### Versioning Discipline

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Version management with migration paths for contract changes; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Version management with migration paths for contract changes; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Version management with migration paths for contract changes; significant gaps but core elements present |
| 3-4 | Weakly addresses: Version management with migration paths for contract changes; major gaps, core elements missing or vague |
| 0-2 | Does not address: Version management with migration paths for contract changes; absent or fundamentally incomplete |

### Runtime Enforcement

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Monitoring configuration for detecting contract violations; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Monitoring configuration for detecting contract violations; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Monitoring configuration for detecting contract violations; significant gaps but core elements present |
| 3-4 | Weakly addresses: Monitoring configuration for detecting contract violations; major gaps, core elements missing or vague |
| 0-2 | Does not address: Monitoring configuration for detecting contract violations; absent or fundamentally incomplete |
