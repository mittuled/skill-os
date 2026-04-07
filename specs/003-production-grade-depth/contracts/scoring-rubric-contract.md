# Contract: Scoring Rubric Format

**Version**: 1.0.0 | **Date**: 2026-03-28

## Location

`<skill>/references/scoring-rubric.md`

## Required For

Every skill that evaluates, assesses, scores, reviews, audits, qualifies, benchmarks, or monitors.

## Structure

```markdown
# Scoring Rubric: <skill-name>

<One sentence: what this rubric evaluates.>

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | <Name> | <N>% | <What this measures> |
| 2 | <Name> | <N>% | <What this measures> |
| 3 | <Name> | <N>% | <What this measures> |
| ... | ... | ... | ... |
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
| A+ | 9.0 – 10.0 | Exceptional | <What this looks like> | <Next step> |
| A | 8.0 – 8.9 | Strong | <What this looks like> | <Next step> |
| B | 7.0 – 7.9 | Good | <What this looks like> | <Next step> |
| C | 5.0 – 6.9 | Adequate | <What this looks like> | <Next step> |
| D | 3.0 – 4.9 | Weak | <What this looks like> | <Next step> |
| F | 0.0 – 2.9 | Failing | <What this looks like> | <Next step> |

## Signal Tables

### <Criterion 1 Name>

| Score | Evidence |
|-------|----------|
| 9-10 | <Specific, observable evidence for this score range> |
| 7-8 | <Specific, observable evidence for this score range> |
| 5-6 | <Specific, observable evidence for this score range> |
| 3-4 | <Specific, observable evidence for this score range> |
| 0-2 | <Specific, observable evidence for this score range> |

### <Criterion 2 Name>

(Repeat signal table for each criterion)
```

## Validation Rules

1. Criteria count: 3-6
2. Weights sum to exactly 100%
3. Scale is 0-10 per criterion
4. Grade bands: exactly 6 (A+, A, B, C, D, F) with non-overlapping score ranges covering 0.0-10.0
5. Signal tables: one per criterion, each with 4-6 rows covering the full 0-10 range
6. Evidence in signal tables must be observable and verifiable (not subjective like "good quality")
7. Grade descriptions and recommended actions must be specific to the skill's domain

## Anti-Patterns

- **Vague signals**: "Good performance" → use "All 5 criteria documented with quantitative targets and measurement cadence"
- **Missing action**: Grade bands without recommended actions are useless for automation
- **Weight inflation**: One criterion at 60%+ indicates the rubric should be simplified or the criterion split
- **Score gaps**: Signal tables must cover 0-10 continuously, no undefined ranges
