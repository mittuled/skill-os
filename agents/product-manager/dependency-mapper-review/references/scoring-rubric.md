# Scoring Rubric: dependency-mapper-review

Identifies, documents, and reviews cross-team and cross-system dependencies that could block delivery.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Dependency Identification | 25% | Completeness of inbound and outbound dependencies across team, system, and external types |
| 2 | Classification Accuracy | 25% | Correctness of blocking vs non-blocking severity classification |
| 3 | Dependency Map Quality | 25% | Clarity of directed graph with nodes, edges, type, and severity annotations |
| 4 | Risk Mitigation Planning | 25% | Quality of critical-path risk documentation with owners and proposed mitigations |
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
| A+ | 9.0 – 10.0 | Exceptional | Exceptional performance across all criteria | Dependency map ready for sprint planning consumption |
| A | 8.0 – 8.9 | Strong | Strong performance across all criteria | Map usable with minor ownership gaps to fill |
| B | 7.0 – 7.9 | Good | Good performance across all criteria | Validate blocking classifications before sprint planning |
| C | 5.0 – 6.9 | Adequate | Adequate performance across all criteria | Missing several dependencies — schedule mapping session |
| D | 3.0 – 4.9 | Weak | Weak performance across all criteria | Map incomplete — restart with full team input |
| F | 0.0 – 2.9 | Failing | Failing performance across all criteria | No dependency mapping performed |

## Signal Tables

### Dependency Identification

| Score | Evidence |
|-------|----------|
| 9-10 | Completeness of inbound and outbound dependencies across team, system, and external types fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Completeness of inbound and outbound dependencies across team, system, and external types mostly demonstrated with minor gaps |
| 5-6 | Completeness of inbound and outbound dependencies across team, system, and external types partially present with significant gaps |
| 3-4 | Completeness of inbound and outbound dependencies across team, system, and external types attempted but superficial or inconsistent |
| 0-2 | No evidence of dependency identification |

### Classification Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Correctness of blocking vs non-blocking severity classification fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Correctness of blocking vs non-blocking severity classification mostly demonstrated with minor gaps |
| 5-6 | Correctness of blocking vs non-blocking severity classification partially present with significant gaps |
| 3-4 | Correctness of blocking vs non-blocking severity classification attempted but superficial or inconsistent |
| 0-2 | No evidence of classification accuracy |

### Dependency Map Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Clarity of directed graph with nodes, edges, type, and severity annotations fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Clarity of directed graph with nodes, edges, type, and severity annotations mostly demonstrated with minor gaps |
| 5-6 | Clarity of directed graph with nodes, edges, type, and severity annotations partially present with significant gaps |
| 3-4 | Clarity of directed graph with nodes, edges, type, and severity annotations attempted but superficial or inconsistent |
| 0-2 | No evidence of dependency map quality |

### Risk Mitigation Planning

| Score | Evidence |
|-------|----------|
| 9-10 | Quality of critical-path risk documentation with owners and proposed mitigations fully demonstrated with comprehensive evidence and no gaps |
| 7-8 | Quality of critical-path risk documentation with owners and proposed mitigations mostly demonstrated with minor gaps |
| 5-6 | Quality of critical-path risk documentation with owners and proposed mitigations partially present with significant gaps |
| 3-4 | Quality of critical-path risk documentation with owners and proposed mitigations attempted but superficial or inconsistent |
| 0-2 | No evidence of risk mitigation planning |
