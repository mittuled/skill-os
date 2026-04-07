---
name: activation-moment-validator
description: >
  This skill validates that the defined activation moment predicts long-term retention through data analysis. Use when asked to verify an activation metric, correlate activation with retention, or assess whether the aha moment definition is correct. Also consider when retention curves flatten without explanation. Suggest when the activation signal was defined qualitatively without quantitative validation.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: medium
related-skills:
  - activation-signal-definer
  - retention-model-hypothesiser
  - funnel-analyser-growth
---

# activation-moment-validator

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The activation moment validator tests whether the defined activation event actually predicts long-term retention by running correlation and survival analyses between the activation signal and Day 7/30/90 retention cohorts, ensuring the growth team optimizes toward the right behavioural milestone.

## When to Use

- When the activation signal has been defined but not yet validated with retention data.
- When retention rates decline despite stable or improving activation rates, suggesting a misaligned definition.
- When a product pivot changes the core value proposition and the existing activation moment may no longer apply.
- When the team debates which user action best represents the "aha moment."

## Workflow

1. **Retrieve activation definition**: Pull the current activation signal definition including the event, threshold, and time window (e.g., "completed first project within 48 hours of signup").
2. **Build cohorts**: Segment users into activated vs. non-activated cohorts using the defined signal. Ensure cohorts are large enough for statistical validity (minimum 500 users per group).
3. **Run retention analysis**: Compute Day 7, Day 30, and Day 90 retention rates for each cohort. Calculate the retention lift (activated retention minus non-activated retention).
4. **Survival analysis**: Plot Kaplan-Meier survival curves for both cohorts. Test for significant separation using the log-rank test. A valid activation moment should produce a statistically significant (p < 0.05) separation in survival curves.
5. **Test alternative signals**: If the current signal shows weak predictive power (retention lift < 10 percentage points), test 3-5 alternative candidate actions. Rank by retention lift and statistical significance.
6. **Deliver validation report**: Produce a report with retention cohort analysis, survival curves, p-values, and a validated/invalidated verdict. If invalidated, recommend the strongest alternative signal.

## Anti-Patterns

- **Validating with small cohorts**: Running the analysis on fewer than 500 users per group produces unreliable results. *Why*: small samples amplify noise and produce confidence intervals too wide to act on.
- **Confusing correlation with causation**: A high correlation between an action and retention does not prove the action causes retention. *Why*: power users both activate and retain because of inherent motivation, not because the activation event drove retention.
- **One-time validation**: Treating validation as a one-time exercise ignores that the relationship between activation and retention evolves as the product and user base change. *Why*: what predicted retention at 1,000 users may not predict retention at 100,000 users.

## Output

**Success:**
- A validation report containing cohort retention rates, retention lift, survival curves with log-rank test results, and a validated/invalidated verdict with recommended next steps.

**Failure:**
- The activation signal shows no statistically significant correlation with retention. Report the analysis, the tested alternatives, and recommend the strongest candidate for re-definition.

## Related Skills

- [`activation-signal-definer`](../activation-signal-definer/SKILL.md) -- defines the activation signal that this skill validates.
- [`retention-model-hypothesiser`](../retention-model-hypothesiser/SKILL.md) -- the retention model depends on a validated activation moment as its entry point.
- [`funnel-analyser-growth`](../../../data-growth/growth-engineer/funnel-analyser-growth/SKILL.md) -- funnel analysis of the activation flow provides context for why users do or do not reach the activation moment.
