# Scoring Rubric: flow-designer-review

Reviews proposed user flows for completeness, usability, and alignment with product requirements.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Requirements Coverage | 25% | Story-to-step mapping completeness with gap and scope-creep annotations |
| 2 | Persona Path Coverage | 25% | Verification that each persona's path through the flow is traced and validated |
| 3 | Error State Handling | 25% | Inventory of failure points with documented recovery paths and fallback states |
| 4 | Flow Coherence | 25% | Consistency of navigation, terminology, and justified step count |
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
| A+ | 9.0 – 10.0 | Exceptional | Exceptional performance across all criteria | Flow approved — proceed to implementation |
| A | 8.0 – 8.9 | Strong | Strong performance across all criteria | Approved with minor coherence improvements |
| B | 7.0 – 7.9 | Good | Good performance across all criteria | Revisions needed on error states or persona paths |
| C | 5.0 – 6.9 | Adequate | Adequate performance across all criteria | Significant gaps in requirements coverage |
| D | 3.0 – 4.9 | Weak | Weak performance across all criteria | Major rework needed — flow does not satisfy stories |
| F | 0.0 – 2.9 | Failing | Failing performance across all criteria | No flow review performed |

## Signal Tables

### Requirements Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Story-to-step mapping completeness with gap and scope-creep annotations fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Story-to-step mapping completeness with gap and scope-creep annotations mostly demonstrated with minor gaps |
| 5-6 | Story-to-step mapping completeness with gap and scope-creep annotations partially present with significant gaps |
| 3-4 | Story-to-step mapping completeness with gap and scope-creep annotations attempted but superficial or inconsistent |
| 0-2 | No evidence of requirements coverage |

### Persona Path Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Verification that each persona's path through the flow is traced and validated fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Verification that each persona's path through the flow is traced and validated mostly demonstrated with minor gaps |
| 5-6 | Verification that each persona's path through the flow is traced and validated partially present with significant gaps |
| 3-4 | Verification that each persona's path through the flow is traced and validated attempted but superficial or inconsistent |
| 0-2 | No evidence of persona path coverage |

### Error State Handling

| Score | Evidence |
|-------|----------|
| 9-10 | Inventory of failure points with documented recovery paths and fallback states fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Inventory of failure points with documented recovery paths and fallback states mostly demonstrated with minor gaps |
| 5-6 | Inventory of failure points with documented recovery paths and fallback states partially present with significant gaps |
| 3-4 | Inventory of failure points with documented recovery paths and fallback states attempted but superficial or inconsistent |
| 0-2 | No evidence of error state handling |

### Flow Coherence

| Score | Evidence |
|-------|----------|
| 9-10 | Consistency of navigation, terminology, and justified step count fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Consistency of navigation, terminology, and justified step count mostly demonstrated with minor gaps |
| 5-6 | Consistency of navigation, terminology, and justified step count partially present with significant gaps |
| 3-4 | Consistency of navigation, terminology, and justified step count attempted but superficial or inconsistent |
| 0-2 | No evidence of flow coherence |
