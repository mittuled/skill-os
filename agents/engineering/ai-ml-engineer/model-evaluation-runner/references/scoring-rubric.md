# Scoring Rubric: model-evaluation-runner

Evaluates the quality, completeness, and rigor of an ML model evaluation against defined requirements and production promotion standards.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Accuracy Metric Coverage | 25% | Completeness of task-appropriate metrics (F1/AUC-ROC/NDCG) with confidence intervals |
| 2 | Fairness Assessment | 20% | Coverage of protected attributes with quantitative disparity measurements |
| 3 | Robustness Testing | 20% | OOD performance, adversarial inputs, missing features, and noisy data tests |
| 4 | Baseline Comparison | 20% | Statistical significance of improvement over rule-based, previous model, and heuristic baselines |
| 5 | Evaluation Dataset Quality | 15% | Stratification, leakage prevention, and segment coverage of the test set |
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
| A+ | 9.0 – 10.0 | Exceptional | All metrics computed with confidence intervals; full fairness coverage; robustness tested across 5+ perturbation types; statistically significant improvement over all baselines | Promote to production; register full evaluation report in model registry |
| A | 8.0 – 8.9 | Strong | All primary metrics present; 1 protected attribute not evaluated; robustness tested across 3 types; statistically significant improvement over main baseline | Promote with accepted risk for minor gaps; log gaps in model registry |
| B | 7.0 – 7.9 | Good | Primary metrics complete; fairness assessed but missing 2+ protected attributes; OOD tested; comparison to production model only | Promote with P2 ticket to complete missing fairness evaluation in next cycle |
| C | 5.0 – 6.9 | Adequate | Primary metrics computed without confidence intervals; no fairness assessment; no robustness testing; compared to only one baseline | Do not promote; require fairness and robustness evaluation before re-review |
| D | 3.0 – 4.9 | Weak | Only accuracy computed; no confidence intervals; no baseline comparison; test set quality unknown | Reject; return to ML engineer for comprehensive evaluation rerun |
| F | 0.0 – 2.9 | Failing | No evaluation report; metrics computed on training data; no holdout set; no baselines | Reject; block model registration; mandatory full re-evaluation from scratch |

## Signal Tables

### Accuracy Metric Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Task-appropriate primary metric (F1/AUC-ROC/NDCG@K/RMSE) reported with 95% confidence intervals from bootstrap or exact methods; secondary metric constraint verified (e.g., recall ≥ 0.70 at precision ≥ 0.85); precision-recall curve and ROC curve included |
| 7-8 | Primary metric reported with confidence intervals; secondary metric present; curve analysis present but 1-2 required metrics missing |
| 5-6 | Primary metric reported as point estimate only (no confidence intervals); secondary metric reported; no curve analysis |
| 3-4 | Only accuracy (not task-appropriate for imbalanced classification) reported; no confidence intervals; missing curves |
| 0-2 | Metrics computed on training set or validation set used for tuning; no held-out test set; point estimates only with no secondary metrics |

### Fairness Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | All applicable protected attributes evaluated (gender, age, race where applicable); demographic parity difference, equalized odds, and predictive parity computed; disparity ≤ defined threshold for all groups; disaggregated metric tables included |
| 7-8 | 80%+ protected attributes evaluated; at least 2 fairness metrics computed per attribute; 1 attribute missing without documented rationale |
| 5-6 | Protected attributes identified but only 1 fairness metric computed; missing intersection analysis for correlated attributes |
| 3-4 | Fairness mentioned in report but only performance disaggregated by single demographic; no formal fairness metric computed |
| 0-2 | No fairness assessment; protected attributes not identified; no disaggregated metrics |

### Robustness Testing

| Score | Evidence |
|-------|----------|
| 9-10 | Tests conducted on: OOD samples (different distribution from training), adversarial inputs, missing features (nulls injected at 10%/30%/50% rates), noisy labels, and temporal generalization (test set from future time period); failure case catalog documented |
| 7-8 | OOD performance tested; 2-3 perturbation types evaluated; failure cases identified but not fully cataloged |
| 5-6 | OOD test set used; missing feature test conducted; adversarial testing not performed |
| 3-4 | Only OOD testing; no perturbation testing; no failure case analysis |
| 0-2 | No robustness testing; evaluation only on in-distribution test samples; no perturbation analysis |

### Baseline Comparison

| Score | Evidence |
|-------|----------|
| 9-10 | Candidate model compared against 3+ baselines (rule-based, previous production model, simple heuristic); improvement is statistically significant (p < 0.05) on primary metric; comparative table with all metrics per baseline; McNemar's test or bootstrap significance applied |
| 7-8 | Compared against previous production model and 1 other baseline; statistical significance test applied; comparative table present |
| 5-6 | Compared against 1 baseline only; statistical significance not reported; improvement is numerically present but not verified |
| 3-4 | Baseline comparison mentioned but no statistical test; only compared against majority-class predictor |
| 0-2 | No baseline comparison; model accuracy reported in isolation; improvement claim unverified |

### Evaluation Dataset Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Test set is stratified by critical segments (class, user cohort, data source); no overlap with training or validation set (confirmed by hash or time-based split); test set size meets minimum statistical power requirements; temporal split used where time-series data involved |
| 7-8 | Test set stratified by main class; no leakage confirmed; size adequate for primary metric but potentially underpowered for subgroup analysis |
| 5-6 | Test set is random split without stratification; leakage not explicitly verified; adequate size for primary metric |
| 3-4 | Test set is a small random split; possible leakage from shared preprocessing; segments not represented proportionally |
| 0-2 | Test set not described; evaluation conducted on same data as training; or test set is validation set used during tuning |
