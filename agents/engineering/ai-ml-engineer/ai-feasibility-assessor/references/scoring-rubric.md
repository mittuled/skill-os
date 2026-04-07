# Scoring Rubric: ai-feasibility-assessor

Evaluates the rigor and completeness of an AI/ML feasibility assessment for a proposed problem, covering data readiness, compute viability, baseline estimation, and risk identification.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Data Readiness Assessment | 30% | Volume, label quality, feature coverage, and distribution analysis of available data |
| 2 | Problem Framing Clarity | 20% | Precision of task type definition, success criteria, and business impact quantification |
| 3 | Baseline Estimation | 20% | Quality of non-ML baseline benchmarks used to establish the minimum bar ML must beat |
| 4 | Compute and Cost Analysis | 15% | Training compute estimate, inference latency analysis, and infrastructure cost projection |
| 5 | Risk and Timeline Assessment | 15% | Identification of data drift, regulatory, and adversarial risks; timeline realism |
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
| A+ | 9.0 – 10.0 | Exceptional | All dimensions thoroughly assessed; data profiled; compute estimated with cost; baselines run; risks quantified | Issue go verdict; proceed to model requirements definition |
| A | 8.0 – 8.9 | Strong | All primary dimensions assessed; 1 minor gap with documented assumption | Issue go verdict with documented assumption; proceed with monitoring plan |
| B | 7.0 – 7.9 | Good | Data profiled and baselines established; compute rough estimate; 1-2 risks not fully analyzed | Conditional go; resolve flagged risks within 2-week data exploration sprint |
| C | 5.0 – 6.9 | Adequate | Data volume assessed but quality not verified; no running baselines; timeline vague | Request data quality audit and baseline run before re-assessment |
| D | 3.0 – 4.9 | Weak | Data availability assumed without profiling; problem framing imprecise; no baselines | Do not proceed; return for full data audit and problem scoping workshop |
| F | 0.0 – 2.9 | Failing | No data profiling; no baselines; ML recommended without evidence it will work | Block ML investment; require business case re-evaluation |

## Signal Tables

### Data Readiness Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Data profiled for volume (row counts, growth rate), label quality (noise rate, inter-annotator agreement), feature coverage (null rates per feature), class balance, and temporal relevance; minimum viable sample size estimated from power analysis; distribution shift risk assessed |
| 7-8 | Volume and label quality profiled; null rates checked; class balance reported; temporal coverage noted; no statistical power analysis |
| 5-6 | Volume estimated from stakeholder input; labels described as "available" without quality measurement; null rates not assessed |
| 3-4 | Data described as existing without profiling; label availability unclear; volume is a rough guess without verification |
| 0-2 | No data audit conducted; data assumed to exist; no quality, volume, or coverage assessment |

### Problem Framing Clarity

| Score | Evidence |
|-------|----------|
| 9-10 | Task type specified (classification/regression/ranking/generation/anomaly detection); success metric defined with numeric target; business impact quantified (e.g., "0.1 improvement in F1 → $2M annual revenue from reduced manual review"); ML vs. heuristic comparison explicitly addressed |
| 7-8 | Task type specified; success metric defined; business impact described qualitatively; ML necessity justified |
| 5-6 | Task type identified; success metric exists but is vague (e.g., "good accuracy"); business impact not quantified |
| 3-4 | Task type implied but not specified; success defined as "better than current" without measurable target |
| 0-2 | No problem framing; "we need AI for this" without specifying task type or success criteria |

### Baseline Estimation

| Score | Evidence |
|-------|----------|
| 9-10 | Baselines computed with actual data: majority class, rule-based system, simple heuristic (logistic regression or decision tree); all baselines evaluated on the same held-out set with the same metric as the proposed ML model; performance gap between baseline and ML target quantified |
| 7-8 | 2 baselines computed on actual data; metrics computed on held-out set; gap to ML target quantified |
| 5-6 | 1 baseline run; current system performance used as benchmark; same metric as proposed model |
| 3-4 | Baseline described but not run; performance estimated from stakeholder knowledge of current system |
| 0-2 | No baselines established; ML performance target set without reference to what non-ML systems achieve |

### Compute and Cost Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Training compute estimated in GPU-hours with cost (e.g., "$450 per training run at 8× A100 for 6 hours"); inference latency estimated at p50 and p99 for target serving scenario; infrastructure monthly cost projected for training + serving at expected volume; compared against available budget |
| 7-8 | Training compute and cost estimated; inference latency estimated for primary serving scenario; total cost projected |
| 5-6 | Training compute estimated without cost; inference latency categorized (fast/slow) but not measured; cost rough order of magnitude only |
| 3-4 | Compute requirements mentioned without estimation; cost not addressed; latency not analyzed |
| 0-2 | No compute or cost analysis; feasibility declared without infrastructure consideration |

### Risk and Timeline Assessment

| Score | Evidence |
|-------|----------|
| 9-10 | Risk register includes: data drift risk (with monitoring plan), adversarial input risk, regulatory constraints (with specific requirements), model bias risk (with mitigation); timeline estimates each phase (data prep, feature engineering, training, evaluation, MLOps setup) with 80th-percentile estimates; 60-80% overhead for non-modeling work explicitly accounted for |
| 7-8 | 3-4 risks identified with mitigations; timeline covers main phases; data preparation overhead noted |
| 5-6 | 2 risks identified without mitigations; timeline covers training phase but omits MLOps and data prep time |
| 3-4 | Risks mentioned without specificity; timeline is "training will take 2 weeks" without data prep or deployment |
| 0-2 | No risks identified; timeline is optimistic single-phase estimate; no acknowledgment of MLOps overhead |
