# Framework: MVP Growth Experiment Definer

Defines the structural methodology for scoping minimum viable growth experiments with proper statistical sizing, hypothesis formatting, and kill criteria.

## Hypothesis Format

Every growth experiment hypothesis must follow this structure:

```
We believe [channel / mechanic / feature change]
will produce [metric] at [target threshold]
for [target user segment]
because [rationale based on data or theory]
resulting in [business impact if hypothesis is true].
```

**Example (good)**:
> "We believe a two-sided referral incentive (both referrer and referee receive 1 free month) will produce a viral coefficient ≥ 0.20 for activated users in the SMB segment, because social reciprocity increases invite acceptance rates, resulting in 15% of new activated users acquired via referral within 60 days."

**Example (bad)**:
> "We think referrals could help us grow." — Not falsifiable, no metric, no threshold, no segment.

## Power Analysis Calculator

For binary conversion metrics (activation rate, conversion rate):

```
Required Sample Size (per variant) = (Z_α/2 + Z_β)² × 2 × p̄(1−p̄) / (MDE)²

Where:
  Z_α/2 = 1.96 (95% confidence, two-tailed)
  Z_β   = 0.84 (80% power)
  p̄     = average of baseline and expected conversion rates
  MDE   = Minimum Detectable Effect (absolute percentage points)
```

**Quick reference table** (80% power, 95% confidence):

| Baseline Rate | MDE | Required Sample (per variant) |
|--------------|-----|------------------------------|
| 10% | 2pp | 2,394 |
| 10% | 5pp | 490 |
| 20% | 3pp | 2,822 |
| 20% | 5pp | 1,021 |
| 30% | 5pp | 1,276 |
| 50% | 5pp | 1,537 |

**Rule**: If required sample exceeds available traffic × 4 weeks, use a proxy test or qualitative validation instead.

## Experiment Prioritization: ICE Scoring

Rate each experiment on:
- **Impact (I)**: Expected MAU or revenue impact if the hypothesis proves true (1 = trivial, 10 = transformative)
- **Confidence (C)**: Evidence quality supporting the hypothesis (10 = multiple data points from similar products, 1 = pure guess)
- **Ease (E)**: Implementation speed and cost (10 = live in 3 days at $0, 1 = months of engineering)

**ICE Score** = (I × C × E)^(1/3) — geometric mean to prevent one extreme score from dominating.

Run the top 2–3 ICE-scored experiments in the next cycle; do not run more simultaneously.

## Kill Criteria Framework

Define kill criteria before the experiment starts:

| Criterion Type | Definition | Example |
|---------------|-----------|---------|
| **Minimum signal threshold** | Stop if cannot reach statistical significance | Stop if p > 0.10 after 4 weeks and 500+ conversions |
| **Directional harm** | Stop immediately if primary metric degrades | Stop if activation rate drops > 5% below control |
| **Budget cap** | Stop if CAC exceeds maximum allowable | Stop if CAC > $300 (2× allowable) after 100 conversions |
| **Time cap** | Stop at fixed date regardless of status | Stop at Day 28; no exceptions |
| **Volume floor** | Do not read results until minimum sample reached | Do not read until 200 conversions per variant |

## Experiment Brief Template (One-Page)

```
Experiment ID:       [EXP-YYYY-NNN]
Hypothesis:          [Formatted hypothesis using the template above]
Primary metric:      [Event name + threshold]
Secondary metrics:   [1-2 guardrail metrics to track for harm]
Minimum sample:      [Per-variant count from power analysis]
Duration:            [N weeks; max 4 weeks]
Budget cap:          $[X]
Kill criteria:       [List all kill criteria]
Variants:            Control: [description]. Treatment: [description]
Owner:               [Name]
Launch date:         [YYYY-MM-DD]
Read date:           [YYYY-MM-DD]
```

## Concurrent Experiment Policy

- **Maximum concurrent experiments**: 3 on overlapping user populations
- **Isolation rule**: Experiments with the same primary metric must use mutually exclusive user segments
- **Hold-out group**: Maintain a 5% holdout from all experiments for baseline comparison
- **Interaction testing**: If two experiments run concurrently, log all users in both experiments for post-hoc interaction analysis
