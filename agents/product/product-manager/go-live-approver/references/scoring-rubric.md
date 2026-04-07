# Scoring Rubric: go-live-approver

Provides product management sign-off for production go-live as the final gate before users are exposed.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Release Manifest Accuracy | 15% | Completeness of feature/fix list cross-referenced against sprint plan |
| 2 | Acceptance Criteria Verification | 25% | Pass/partial/fail status per story with QA evidence |
| 3 | Cross-Functional Readiness | 25% | Sign-off status from support, sales, marketing, and operations |
| 4 | Rollback and Risk Assessment | 20% | Tested rollback procedure, monitoring configuration, and open risk register |
| 5 | Decision Documentation | 15% | Formal go/no-go record with rationale, conditions, and distribution |
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
| A+ | 9.0 – 10.0 | Exceptional | Exceptional performance across all criteria | Authorise immediate deployment |
| A | 8.0 – 8.9 | Strong | Strong performance across all criteria | Authorise with monitoring heightened for 48 hours |
| B | 7.0 – 7.9 | Good | Good performance across all criteria | Conditional go — resolve specified items before deploy |
| C | 5.0 – 6.9 | Adequate | Adequate performance across all criteria | Defer — significant readiness gaps require remediation |
| D | 3.0 – 4.9 | Weak | Weak performance across all criteria | No-go — multiple blocking issues unresolved |
| F | 0.0 – 2.9 | Failing | Failing performance across all criteria | No go-live assessment performed |

## Signal Tables

### Release Manifest Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Completeness of feature/fix list cross-referenced against sprint plan fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Completeness of feature/fix list cross-referenced against sprint plan mostly demonstrated with minor gaps |
| 5-6 | Completeness of feature/fix list cross-referenced against sprint plan partially present with significant gaps |
| 3-4 | Completeness of feature/fix list cross-referenced against sprint plan attempted but superficial or inconsistent |
| 0-2 | No evidence of release manifest accuracy |

### Acceptance Criteria Verification

| Score | Evidence |
|-------|----------|
| 9-10 | Pass/partial/fail status per story with QA evidence fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Pass/partial/fail status per story with QA evidence mostly demonstrated with minor gaps |
| 5-6 | Pass/partial/fail status per story with QA evidence partially present with significant gaps |
| 3-4 | Pass/partial/fail status per story with QA evidence attempted but superficial or inconsistent |
| 0-2 | No evidence of acceptance criteria verification |

### Cross-Functional Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | Sign-off status from support, sales, marketing, and operations fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Sign-off status from support, sales, marketing, and operations mostly demonstrated with minor gaps |
| 5-6 | Sign-off status from support, sales, marketing, and operations partially present with significant gaps |
| 3-4 | Sign-off status from support, sales, marketing, and operations attempted but superficial or inconsistent |
| 0-2 | No evidence of cross-functional readiness |

### Rollback and Risk Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Tested rollback procedure, monitoring configuration, and open risk register fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Tested rollback procedure, monitoring configuration, and open risk register mostly demonstrated with minor gaps |
| 5-6 | Tested rollback procedure, monitoring configuration, and open risk register partially present with significant gaps |
| 3-4 | Tested rollback procedure, monitoring configuration, and open risk register attempted but superficial or inconsistent |
| 0-2 | No evidence of rollback and risk assessment |

### Decision Documentation

| Score | Evidence |
|-------|----------|
| 9-10 | Formal go/no-go record with rationale, conditions, and distribution fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Formal go/no-go record with rationale, conditions, and distribution mostly demonstrated with minor gaps |
| 5-6 | Formal go/no-go record with rationale, conditions, and distribution partially present with significant gaps |
| 3-4 | Formal go/no-go record with rationale, conditions, and distribution attempted but superficial or inconsistent |
| 0-2 | No evidence of decision documentation |
