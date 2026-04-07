# Scoring Rubric: ai-risk-assessor

Evaluates the completeness and rigour of an AI risk assessment covering regulatory compliance, bias analysis, transparency, and mitigation planning.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Regulatory Coverage | 25% | Completeness of mapping against applicable AI regulations (EU AI Act, NIST AI RMF, state-level AI laws, sector-specific guidance) |
| 2 | Bias and Fairness Analysis | 25% | Depth of discriminatory impact evaluation across protected classes, training data review, and fairness metric assessment |
| 3 | Transparency and Explainability | 20% | Adequacy of user-facing explanations, contestability mechanisms, and model explainability for the regulatory context |
| 4 | Mitigation Quality | 20% | Specificity and implementability of recommended technical, legal, and operational controls |
| 5 | Monitoring Framework | 10% | Completeness of ongoing monitoring plan including drift detection, fairness tracking, and re-assessment triggers |

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
| A+ | 9.0 – 10.0 | Exceptional | All AI regulations mapped, bias analysis covers all protected classes with quantitative metrics, explainability mechanisms tested, mitigations implementation-ready | Approve for launch with standard monitoring cadence |
| A | 8.0 – 8.9 | Strong | Comprehensive regulatory mapping with minor jurisdiction gaps, bias analysis covers primary protected classes, mitigations actionable | Approve with minor enhancements scheduled post-launch |
| B | 7.0 – 7.9 | Good | Major regulations covered, bias analysis present but missing some demographic groups, mitigations identified but need specificity | Approve with conditions: address gaps within 30 days |
| C | 5.0 – 6.9 | Adequate | Core regulations identified but analysis shallow, bias assessment limited to obvious categories, mitigations generic | Conditional approval: remediate gaps before launch in regulated markets |
| D | 3.0 – 4.9 | Weak | Significant regulatory gaps, minimal bias analysis, no explainability assessment, mitigations vague | Block launch: major revision required before re-assessment |
| F | 0.0 – 2.9 | Failing | No regulatory mapping, no bias analysis, no transparency review | Block launch: complete assessment from scratch |

## Signal Tables

### Regulatory Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | EU AI Act risk tier classified with supporting analysis, NIST AI RMF categories mapped, all applicable state-level AI laws identified, sector-specific guidance (FDA, EEOC, CFPB) reviewed where relevant |
| 7-8 | EU AI Act and NIST AI RMF addressed, most relevant state laws identified, minor gaps in sector-specific guidance |
| 5-6 | One major framework (EU AI Act or NIST) addressed, state laws mentioned but not individually analysed |
| 3-4 | Generic reference to "AI regulations" without specific framework mapping or jurisdictional analysis |
| 0-2 | No regulatory mapping performed or only a single regulation mentioned without analysis |

### Bias and Fairness Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Training data composition documented, model performance tested across all legally protected classes, proxy discrimination risks identified, fairness metrics (demographic parity, equalized odds) calculated and compared |
| 7-8 | Training data reviewed, performance tested across major protected classes, fairness metrics calculated for primary groups |
| 5-6 | Training data composition noted, bias assessment covers race and gender but misses age, disability, or other protected classes |
| 3-4 | Generic statement about bias risk without specific demographic analysis or fairness metrics |
| 0-2 | No bias analysis performed or bias dismissed without evidence |

### Transparency and Explainability

| Score | Evidence |
|-------|----------|
| 9-10 | User-facing explanations designed and tested, contestation mechanism specified, model explainability method selected (SHAP, LIME) and validated, regulatory explainability requirements mapped per jurisdiction |
| 7-8 | User explanations drafted, contestation process defined, explainability method identified but not yet validated |
| 5-6 | General transparency commitments documented, explainability approach discussed but not designed |
| 3-4 | Transparency mentioned as a goal without specific mechanisms or explainability assessment |
| 0-2 | No transparency or explainability review performed |

### Mitigation Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Each risk has a specific mitigation with implementation owner, timeline, and success criteria; mitigations span technical (bias testing pipelines), legal (consent mechanisms, appeal processes), and operational (monitoring, audit trails) controls |
| 7-8 | Mitigations specified for high-priority risks with owners assigned, most control types covered |
| 5-6 | Mitigations listed but lack implementation detail, owners, or timelines; some control types missing |
| 3-4 | Generic recommendations ("implement bias testing") without specificity or ownership |
| 0-2 | No mitigations recommended or only a single generic recommendation |

### Monitoring Framework

| Score | Evidence |
|-------|----------|
| 9-10 | Model drift detection metrics defined, fairness metric tracking cadence set, regulatory change alert process established, re-assessment triggers documented with responsible parties |
| 7-8 | Drift detection and fairness tracking planned, re-assessment triggers identified |
| 5-6 | Monitoring mentioned with some metrics identified but no cadence or ownership |
| 3-4 | Generic statement about "ongoing monitoring" without specific metrics or processes |
| 0-2 | No monitoring framework defined |
