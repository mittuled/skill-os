# Scoring Rubric: Company Tooling Onboarder

Evaluates the quality of company tool onboarding execution.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Discovery Completeness | 20% | Coverage of all organizational tool categories in the manifest |
| 2 | MCP Availability Assessment | 15% | Accuracy of MCP/CLI/API classification per tool |
| 3 | Authentication Security | 25% | Credential storage in secret store, never in repo |
| 4 | Connection Validation | 20% | End-to-end connectivity testing for every tool |
| 5 | Policy Generation Quality | 20% | Completeness and accuracy of generated allowed-tools.yaml |
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

### Discovery Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Coverage of all organizational tool categories in the manifest; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Coverage of all organizational tool categories in the manifest; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Coverage of all organizational tool categories in the manifest; significant gaps but core elements present |
| 3-4 | Weakly addresses: Coverage of all organizational tool categories in the manifest; major gaps, core elements missing or vague |
| 0-2 | Does not address: Coverage of all organizational tool categories in the manifest; absent or fundamentally incomplete |

### MCP Availability Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Accuracy of MCP/CLI/API classification per tool; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Accuracy of MCP/CLI/API classification per tool; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Accuracy of MCP/CLI/API classification per tool; significant gaps but core elements present |
| 3-4 | Weakly addresses: Accuracy of MCP/CLI/API classification per tool; major gaps, core elements missing or vague |
| 0-2 | Does not address: Accuracy of MCP/CLI/API classification per tool; absent or fundamentally incomplete |

### Authentication Security

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Credential storage in secret store, never in repo; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Credential storage in secret store, never in repo; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Credential storage in secret store, never in repo; significant gaps but core elements present |
| 3-4 | Weakly addresses: Credential storage in secret store, never in repo; major gaps, core elements missing or vague |
| 0-2 | Does not address: Credential storage in secret store, never in repo; absent or fundamentally incomplete |

### Connection Validation

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: End-to-end connectivity testing for every tool; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: End-to-end connectivity testing for every tool; minor gaps in completeness or evidence |
| 5-6 | Partially meets: End-to-end connectivity testing for every tool; significant gaps but core elements present |
| 3-4 | Weakly addresses: End-to-end connectivity testing for every tool; major gaps, core elements missing or vague |
| 0-2 | Does not address: End-to-end connectivity testing for every tool; absent or fundamentally incomplete |

### Policy Generation Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Completeness and accuracy of generated allowed-tools.yaml; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Completeness and accuracy of generated allowed-tools.yaml; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Completeness and accuracy of generated allowed-tools.yaml; significant gaps but core elements present |
| 3-4 | Weakly addresses: Completeness and accuracy of generated allowed-tools.yaml; major gaps, core elements missing or vague |
| 0-2 | Does not address: Completeness and accuracy of generated allowed-tools.yaml; absent or fundamentally incomplete |
