# Scoring Rubric: launch-checklist-runner

Runs through the launch checklist confirming all go-live criteria across engineering, QA, support, marketing, and operations.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Checklist Completeness | 25% | All categories covered: engineering, QA, docs, support, marketing, legal, infrastructure |
| 2 | Verification Rigour | 30% | Each item genuinely verified (not rubber-stamped) with evidence |
| 3 | Blocker Escalation | 25% | Failed items documented with owners, ETAs, and escalation status |
| 4 | Readiness Recommendation | 20% | Clear go/conditional-go/no-go with rationale and conditions |
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
| A+ | 9.0 – 10.0 | Exceptional | Exceptional performance across all criteria | All items pass — authorise launch |
| A | 8.0 – 8.9 | Strong | Strong performance across all criteria | Minor non-blocking items open — authorise with monitoring |
| B | 7.0 – 7.9 | Good | Good performance across all criteria | Conditional go — resolve flagged items within 48 hours |
| C | 5.0 – 6.9 | Adequate | Adequate performance across all criteria | Multiple failures — schedule re-run after remediation |
| D | 3.0 – 4.9 | Weak | Weak performance across all criteria | Critical blockers — no-go until resolved |
| F | 0.0 – 2.9 | Failing | Failing performance across all criteria | No checklist run performed |

## Signal Tables

### Checklist Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | All categories covered: engineering, QA, docs, support, marketing, legal, infrastructure fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | All categories covered: engineering, QA, docs, support, marketing, legal, infrastructure mostly demonstrated with minor gaps |
| 5-6 | All categories covered: engineering, QA, docs, support, marketing, legal, infrastructure partially present with significant gaps |
| 3-4 | All categories covered: engineering, QA, docs, support, marketing, legal, infrastructure attempted but superficial or inconsistent |
| 0-2 | No evidence of checklist completeness |

### Verification Rigour

| Score | Evidence |
|-------|----------|
| 9-10 | Each item genuinely verified (not rubber-stamped) with evidence fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Each item genuinely verified (not rubber-stamped) with evidence mostly demonstrated with minor gaps |
| 5-6 | Each item genuinely verified (not rubber-stamped) with evidence partially present with significant gaps |
| 3-4 | Each item genuinely verified (not rubber-stamped) with evidence attempted but superficial or inconsistent |
| 0-2 | No evidence of verification rigour |

### Blocker Escalation

| Score | Evidence |
|-------|----------|
| 9-10 | Failed items documented with owners, ETAs, and escalation status fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Failed items documented with owners, ETAs, and escalation status mostly demonstrated with minor gaps |
| 5-6 | Failed items documented with owners, ETAs, and escalation status partially present with significant gaps |
| 3-4 | Failed items documented with owners, ETAs, and escalation status attempted but superficial or inconsistent |
| 0-2 | No evidence of blocker escalation |

### Readiness Recommendation

| Score | Evidence |
|-------|----------|
| 9-10 | Clear go/conditional-go/no-go with rationale and conditions fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Clear go/conditional-go/no-go with rationale and conditions mostly demonstrated with minor gaps |
| 5-6 | Clear go/conditional-go/no-go with rationale and conditions partially present with significant gaps |
| 3-4 | Clear go/conditional-go/no-go with rationale and conditions attempted but superficial or inconsistent |
| 0-2 | No evidence of readiness recommendation |
