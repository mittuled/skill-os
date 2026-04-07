# Checklist: Model Performance Monitoring Setup

Comprehensive checklist for establishing production model monitoring covering data drift, concept drift, inference latency, and alerting. Aligned with statistical drift detection methods (PSI, KS test) and SLO-driven monitoring practices.

## How to Use

Work through each section in sequence. Mark items `[x]` when implemented and verified with evidence in staging or production. Items marked `[REQUIRED]` are non-negotiable for production models. Items marked `[RECOMMENDED]` are best-practice enhancements for high-stakes models.

---

## Section 1: Monitoring Metric Catalog

- [ ] `[REQUIRED]` Define prediction quality proxy metrics (e.g., click-through rate for recommendation models, conversion rate for propensity models, implicit feedback signals)
- [ ] `[REQUIRED]` Define ground truth label pipeline if labels are available with delay (specify expected label lag in hours/days)
- [ ] `[REQUIRED]` Define input distribution statistics to track per feature (mean, std, quantiles, null rate)
- [ ] `[REQUIRED]` Define inference latency metrics: p50, p95, p99 per serving path
- [ ] `[REQUIRED]` Define throughput metrics: requests-per-second at peak and baseline
- [ ] `[REQUIRED]` Set SLA thresholds for each metric: warning threshold and critical threshold
- [ ] `[REQUIRED]` Store baseline statistics from training data distribution for drift comparison

---

## Section 2: Data Drift Detection

- [ ] `[REQUIRED]` Implement per-feature drift detection (do not monitor aggregate only)
- [ ] `[REQUIRED]` Choose drift detection method appropriate to feature type:
  - Continuous features: Population Stability Index (PSI) or Kolmogorov-Smirnov (KS) test
  - Categorical features: Chi-squared test or Jensen-Shannon divergence
  - High-dimensional embeddings: Maximum Mean Discrepancy (MMD)
- [ ] `[REQUIRED]` Configure PSI thresholds:
  - PSI < 0.1: No drift (monitor only)
  - PSI 0.1–0.2: Moderate drift (warning alert)
  - PSI > 0.2: Large drift (critical alert, trigger retraining review)
- [ ] `[REQUIRED]` Set drift detection cadence (e.g., hourly for real-time models, daily for batch)
- [ ] `[REQUIRED]` Store drift detection results with timestamps for trend analysis
- [ ] `[RECOMMENDED]` Implement segment-level drift detection for critical user cohorts
- [ ] `[RECOMMENDED]` Identify the top-10 most predictive features and monitor them with tighter thresholds
- [ ] `[RECOMMENDED]` SHAP feature importance used to prioritize which features to monitor most closely

---

## Section 3: Concept Drift Detection

- [ ] `[REQUIRED]` Define a concept drift detection strategy appropriate to label availability:
  - Delayed labels available: Monitor ground truth performance (F1, AUC-ROC) over rolling window
  - No labels available: Monitor proxy metrics + prediction distribution shift
- [ ] `[REQUIRED]` Configure rolling window size for performance monitoring (e.g., 7-day rolling F1)
- [ ] `[REQUIRED]` Set concept drift alert thresholds (e.g., rolling F1 drops > 5% below training-time F1)
- [ ] `[REQUIRED]` Configure automated retraining trigger when concept drift threshold is breached
- [ ] `[RECOMMENDED]` Implement page-hinkley test or ADWIN for online concept drift detection
- [ ] `[RECOMMENDED]` Monitor prediction confidence distribution — narrowing confidence intervals can indicate concept drift

---

## Section 4: Latency and Throughput Monitoring

- [ ] `[REQUIRED]` Instrument inference latency with histogram: p50, p95, p99, max
- [ ] `[REQUIRED]` Monitor latency broken down by model version (to detect version-specific regressions)
- [ ] `[REQUIRED]` Monitor throughput (requests per second) with peak and sustained rate tracking
- [ ] `[REQUIRED]` Set latency SLA alert: warning at 80% of budget, critical at 100% of budget
- [ ] `[REQUIRED]` Monitor error rates: HTTP 4xx (bad inputs), 5xx (model/serving errors)
- [ ] `[RECOMMENDED]` Correlate latency spikes with input feature complexity (e.g., text length for NLP models)
- [ ] `[RECOMMENDED]` Monitor model server resource utilization: CPU, GPU, memory, queue depth

---

## Section 5: Alerting and Escalation

- [ ] `[REQUIRED]` Configure tiered alerting:
  - Warning: approaching threshold (send to Slack channel)
  - Critical: threshold breached (page on-call ML engineer)
  - Emergency: complete model failure (page ML lead + trigger fallback)
- [ ] `[REQUIRED]` Define escalation path:
  - Level 1: On-call ML engineer — respond within 30 minutes
  - Level 2: ML lead — escalate if not resolved in 1 hour
  - Level 3: Engineering VP — escalate if production impact persists > 2 hours
- [ ] `[REQUIRED]` Configure automated responses where possible:
  - Traffic rerouting to fallback model on complete failure
  - Automatic retraining trigger on concept drift breach
- [ ] `[REQUIRED]` Test all alert paths in staging before production deployment
- [ ] `[REQUIRED]` Document escalation playbook with runbook URLs per alert type
- [ ] `[RECOMMENDED]` Configure alert deduplication to prevent alert storms
- [ ] `[RECOMMENDED]` Implement seasonal baseline adjustment to prevent false alerts during expected distribution shifts

---

## Section 6: Monitoring Infrastructure Validation

- [ ] `[REQUIRED]` All monitoring components deployed in staging and verified with synthetic data
- [ ] `[REQUIRED]` Drift detection confirmed to fire alerts when PSI/KS thresholds are breached (tested with artificially shifted data)
- [ ] `[REQUIRED]` Latency SLA alerts confirmed to fire when latency exceeds threshold
- [ ] `[REQUIRED]` Dashboards show all required metrics and are accessible to ML and on-call engineers
- [ ] `[REQUIRED]` Runbook documented: steps to investigate and respond to each alert type
- [ ] `[RECOMMENDED]` Monitoring configuration stored as code (not manually configured in dashboard UI)
- [ ] `[RECOMMENDED]` Monitoring coverage report produced showing which model dimensions are monitored

---

## Monitoring Readiness Sign-Off

| Section | Status | Coverage | Reviewer |
|---------|--------|----------|---------|
| 1. Metric Catalog | [ ] Complete / [ ] Partial | [X of Y metrics defined] | |
| 2. Data Drift | [ ] Complete / [ ] Partial | [X of Y features monitored] | |
| 3. Concept Drift | [ ] Complete / [ ] Partial | [Strategy: labels / proxy] | |
| 4. Latency & Throughput | [ ] Complete / [ ] Partial | [SLA thresholds set?] | |
| 5. Alerting | [ ] Complete / [ ] Partial | [All alert paths tested?] | |
| 6. Validation | [ ] Complete / [ ] Partial | | |

**Monitoring Status**: `[ ] PRODUCTION READY` `[ ] PARTIAL — see remediation plan` `[ ] NOT READY`

**AI/ML Engineer**: _________________________ Date: _________
