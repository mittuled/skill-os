---
name: statistical-significance-tracker
description: >
  This skill tracks statistical significance of experiments and flags when results are conclusive. Use when asked to monitor A/B test progress, assess experiment validity, or determine when to call a winner. Also consider when an experiment has been running without a significance check. Suggest when a team is about to ship a variant based on inconclusive data.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: complex
related-skills:
triggers:
  - "track statistical significance"
  - "check A/B test significance"
  - "experiment significance check"
  - "call experiment winner"
  - "assess test validity"
---

# statistical-significance-tracker

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The statistical significance tracker monitors active experiments to determine when results reach the pre-defined confidence threshold, applying correction for multiple comparisons, checking for sample ratio mismatch, and flagging peeking bias so that ship/no-ship decisions are grounded in valid statistical inference.

## When to Use

- When an A/B test is running and stakeholders want to know if results are conclusive.
- When a team is tempted to call a winner early based on directional trends before reaching the required sample size.
- When multiple experiments run concurrently and results need correction for multiple comparisons.
- When an experiment shows surprising results (positive or negative) and the team needs validation before acting.

## Workflow

1. **Retrieve experiment parameters**: Pull the pre-registered hypothesis, primary metric, minimum detectable effect (MDE), required sample size, significance level (alpha, typically 0.05), and power (typically 0.80).
2. **Check sample ratio**: Compare actual traffic allocation to expected allocation. Flag sample ratio mismatch (SRM) if the chi-squared test yields p < 0.01. SRM invalidates results regardless of effect size.
3. **Compute current statistics**: Calculate the observed effect size, confidence interval, and p-value for the primary metric. Use the appropriate test (z-test for proportions, t-test for continuous metrics, Mann-Whitney for non-normal distributions).
4. **Apply multiple comparison correction**: If the experiment has multiple variants or multiple primary metrics, apply Bonferroni or Benjamini-Hochberg correction to control family-wise error rate.
5. **Check for peeking bias**: If the experiment was checked before reaching the required sample size, apply sequential testing methods (e.g., always-valid p-values or group sequential boundaries) to correct for repeated looks.
6. **Assess practical significance**: Even if statistically significant, evaluate whether the observed effect exceeds the minimum practically meaningful threshold. A 0.01% conversion lift may be real but not worth shipping.
7. **Produce status report**: Deliver a significance status per experiment — inconclusive (keep running), significant (ship/no-ship recommendation), or invalid (SRM or instrumentation issue). Include the confidence interval, days remaining at current traffic, and any caveats.

## Anti-Patterns

- **Peeking and calling early**: Checking results daily and stopping when p < 0.05 inflates false-positive rates to 20-30%. *Why*: repeated testing without correction means the 5% significance level no longer holds.
- **Ignoring sample ratio mismatch**: Proceeding with analysis when traffic allocation is skewed produces biased effect estimates. *Why*: SRM indicates a systematic assignment bug that confounds treatment and control.
- **No pre-registration**: Running an experiment without pre-defining the primary metric, MDE, and sample size enables post-hoc metric shopping. *Why*: choosing the metric that "won" after seeing results inflates false positives.
- **Conflating statistical and practical significance**: Shipping a variant because p < 0.05 when the effect is +0.02% conversion creates engineering and UX debt for negligible gain. *Why*: statistical significance means "not zero," not "worth doing."
- **Single-metric tunnel vision**: Tracking only the primary metric while ignoring guardrail metrics (latency, error rate, engagement) risks shipping a variant that improves conversion but degrades experience. *Why*: local optimization on one metric can harm the overall product.

## Output

**Success:**
- An experiment status report per active test containing: observed effect size, confidence interval, p-value (corrected if applicable), SRM check result, days remaining to reach required sample, and a conclusive/inconclusive/invalid verdict.
- A ship/no-ship/extend recommendation with supporting rationale.

**Failure:**
- An experiment is called before reaching the required sample size without sequential testing correction. Report the peeking bias risk, the corrected p-value, and the additional sample needed.
- SRM is detected. Report the observed vs. expected allocation ratio, likely root causes, and whether the experiment should be restarted.

## Related Skills

- [`goal-framer-data`](../goal-framer-data/SKILL.md) -- experiment metrics derive from the analytics goal framework.
- [`funnel-analyser`](../../../data-growth/data-analyst/funnel-analyser/SKILL.md) -- funnel analysis often identifies the conversion steps that experiments target.
- [`funnel-analyser-growth`](../../../data-growth/growth-engineer/funnel-analyser-growth/SKILL.md) -- growth funnel experiments are a primary consumer of significance tracking.
