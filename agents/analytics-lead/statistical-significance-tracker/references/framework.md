# Framework: Statistical Significance Tracker

Defines the methodology for monitoring A/B test validity, applying statistical corrections, and producing ship/no-ship recommendations grounded in valid inference.

## Experiment Monitoring Stages

| Stage | Trigger | Primary Action | Gate Condition |
|-------|---------|---------------|----------------|
| Pre-launch | Experiment registered | Verify pre-registration: hypothesis, primary metric, MDE, alpha, power | Required sample size computed |
| Active | Daily cadence | Check SRM; compute running p-value with sequential correction | Do not call winner before N reached |
| Decision | Required N reached | Apply multiple comparison correction; assess practical significance | p < alpha AND effect > MDE |
| Post-decision | Ship/no-ship called | Archive results; update north star impact estimate | Report published |

## Sample Ratio Mismatch (SRM) Detection

**Test**: Chi-squared test on observed vs. expected traffic split.

| Ratio Deviation | p-value | Action |
|----------------|---------|--------|
| < 2% | > 0.01 | Pass — proceed with analysis |
| 2–5% | 0.001–0.01 | Investigate — likely attribution lag or partial rollout |
| > 5% | < 0.001 | Invalidate — stop analysis; investigate assignment bug |

**Common SRM root causes**: bot filtering differences, A/A imbalance in feature flags, session vs. user assignment mismatch, bot traffic excluded from one variant only.

## Statistical Test Selection

| Metric Type | Distribution | Recommended Test |
|-------------|-------------|-----------------|
| Conversion rate (binary) | Bernoulli | Two-proportion z-test |
| Revenue per user | Often right-skewed | Mann-Whitney U or bootstrapped t-test |
| Continuous metric (normal) | Normal | Welch's two-sample t-test |
| Count data (clicks, views) | Poisson | Rate ratio test |
| Time-to-event | Survival | Log-rank test |

**Minimum power**: 80% (β = 0.20). **Default alpha**: 0.05 (two-tailed).

## Multiple Comparison Corrections

| Scenario | Method | When to Use |
|----------|--------|-------------|
| Multiple variants (3+) | Bonferroni | Conservative; use when false positives are costly |
| Multiple primary metrics | Benjamini-Hochberg | Controls FDR; preferred for exploratory experiments |
| Sequential peeking | Always-valid p-values (mSPRT) | When experiment must be monitored before target N |
| Family-wise control | Holm-Bonferroni | Stronger than Bonferroni; less conservative |

## Sequential Testing (Peeking Correction)

When stakeholders check results before reaching the required sample size, apply one of:

1. **Group sequential boundaries (O'Brien-Fleming)**: Pre-specify interim analysis times; use alpha-spending function to allocate significance budget across looks.
2. **Always-valid p-values (mSPRT)**: Compute a mixture sequential probability ratio test; valid at any stopping time.
3. **Conservative rule**: Require p < 0.01 for early calls (before 75% of required N) to preserve overall α = 0.05.

## Practical Significance Thresholds

| Metric Category | Minimum Practically Meaningful Effect |
|----------------|--------------------------------------|
| Conversion rate | ≥ 0.5 percentage points absolute |
| Revenue per user | ≥ 3% relative lift |
| Engagement metric (DAU, session length) | ≥ 2% relative lift |
| Latency / error rate | ≥ 10% relative improvement |

Statistical significance without meeting the practical threshold = inconclusive for ship purposes.

## Guardrail Metric Protocol

For every experiment, define at minimum:
- **Primary metric**: The one metric the experiment is designed to move.
- **Guardrail metrics**: 2–4 metrics that must not degrade (latency, error rate, Day-7 retention).

If any guardrail moves negatively with p < 0.05, escalate before shipping even if the primary metric wins.

## Experiment Status Taxonomy

| Status | Definition | Recommended Action |
|--------|-----------|-------------------|
| **Inconclusive** | p ≥ alpha OR sample < required N | Continue running; do not ship variant |
| **Significant — Ship** | p < alpha AND effect > MDE AND no guardrail failures | Ship variant |
| **Significant — No-ship** | p < alpha AND negative direction | Stop experiment; do not ship |
| **Invalid — SRM** | Chi-squared p < 0.01 on traffic split | Restart experiment after fixing assignment bug |
| **Invalid — Peeking** | Called before required N without sequential correction | Recompute with mSPRT; extend if inconclusive |
