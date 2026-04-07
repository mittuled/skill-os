# Experiment Status Report

## Metadata

| Field | Value |
|-------|-------|
| Report Date | [YYYY-MM-DD] |
| Author | [Analytics Lead name] |
| Reporting Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Active Experiments | [N] |
| Skill | statistical-significance-tracker |

## Summary Dashboard

| Experiment | Status | Verdict | Recommended Action |
|------------|--------|---------|-------------------|
| [Experiment A] | [Running / Concluded] | [Significant / Inconclusive / Invalid] | [Ship / No-ship / Extend / Restart] |
| [Experiment B] | [Running / Concluded] | [Significant / Inconclusive / Invalid] | [Ship / No-ship / Extend / Restart] |
| [Experiment C] | [Running / Concluded] | [Significant / Inconclusive / Invalid] | [Ship / No-ship / Extend / Restart] |

## Experiment Detail Reports

---

### Experiment: [Experiment Name / ID]

**Pre-Registration Parameters**

| Parameter | Value |
|-----------|-------|
| Hypothesis | [H0 / H1 statement] |
| Primary Metric | [metric_name] |
| Minimum Detectable Effect (MDE) | [X%] |
| Required Sample Size (per variant) | [N] |
| Significance Level (α) | [0.05] |
| Power (1−β) | [0.80] |
| Start Date | [YYYY-MM-DD] |
| Pre-registered End Date | [YYYY-MM-DD] |

**Current Statistics**

| Metric | Control | Variant | Observed Effect | Confidence Interval | p-value |
|--------|---------|---------|-----------------|--------------------|---------| 
| [primary_metric] | [value] | [value] | [+X%] | [lower, upper] | [0.XXX] |

| Check | Result | Notes |
|-------|--------|-------|
| Sample Ratio Mismatch (SRM) | [Pass / FAIL — p=0.XXX] | [Explanation if failed] |
| Multiple Comparison Correction | [N/A / Bonferroni applied / BH applied] | [Correction method if applied] |
| Peeking Bias Correction | [N/A / Sequential testing applied] | [Method if applied] |
| Practical Significance | [Yes — exceeds MDE / No — below MDE] | [Observed vs. required effect] |
| Guardrail Metrics | [All green / [metric] degraded by X%] | [Flag any guardrail regressions] |

**Sample Progress**

| | Control | Variant |
|-|---------|---------|
| Required sample | [N] | [N] |
| Current sample | [N] | [N] |
| Completion % | [X%] | [X%] |
| Estimated days remaining | [N days at current traffic] | — |

**Verdict**

Status: **[INCONCLUSIVE / SIGNIFICANT — POSITIVE / SIGNIFICANT — NEGATIVE / INVALID]**

Recommendation: **[Extend to [date] / Ship variant / No-ship — revert / Restart — SRM detected]**

Rationale: [1-2 sentences explaining the verdict. Example: "The primary metric shows a +3.2% lift (95% CI: +1.1% to +5.3%, p=0.003), exceeding the 2% MDE. Guardrail metrics are unaffected. Recommendation is to ship the variant."]

---

### Experiment: [Experiment Name / ID]

[Repeat the block above for each active experiment]

---

## Flagged Issues

[List any cross-experiment issues identified in this review cycle.]

| Issue | Experiment(s) Affected | Severity | Action Required |
|-------|----------------------|----------|----------------|
| [SRM detected in experiment B] | [Experiment B] | [High] | [Restart experiment after fixing assignment logic] |
| [Multiple metrics checked without pre-registration] | [Experiment C] | [Medium] | [Apply post-hoc Bonferroni correction; pre-register future tests] |

## Experiment Health Summary

| Metric | Value |
|--------|-------|
| Total active experiments | [N] |
| Experiments with SRM | [N] |
| Experiments running beyond target duration | [N] |
| Experiments called without reaching required sample | [N] |
| Win rate (significant positive results) | [X%] |
| Average experiment duration (concluded) | [N days] |
