# Retention Model

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | retention-model-hypothesiser |

## Executive Summary

[2-3 sentences identifying the steepest retention drop-off point, the primary churn hypothesis, and the highest-priority retention experiment. Lead with the finding: "Day 7 retention (12%) is the steepest drop-off, driven primarily by activation failure (45% of churned users never completed a core action). The highest-priority experiment is redesigning the D1 onboarding flow to double activation rate, predicted to improve D30 retention from 18% to 24%.".]

## Retention Curve Analysis

[Plot and interpret retention curves by cohort.

GUIDANCE:
- Good: "D7: 28%, D30: 15%, D90: 9%. Primary drop: D1–D7 (–58% of D1 cohort). Inflection at D30 — curve flattens, indicating a power-user core. Segment analysis: mobile users retain at 2× desktop rate due to push notification habit loop."
- Bad: "Our retention is around 15%." (single number, no curve shape, no segmentation)
- Format: Retention table by cohort + inflection point commentary]

| Cohort | D1 | D7 | D30 | D60 | D90 | Steepest Drop |
|--------|----|----|-----|-----|-----|--------------|
| [Month 1 cohort] | | | | | | D[X]–D[Y] |
| [Month 2 cohort] | | | | | | D[X]–D[Y] |
| [Month 3 cohort] | | | | | | D[X]–D[Y] |

**Benchmark**: Category D30 target: [X]%. Current: [Y]%. Gap: [Z]pp.

## Habit Loop Hypotheses

[Map the habit loops that drive recurring usage.

GUIDANCE:
- Good: "Habit loop 1: External trigger (daily digest email at 8am) → opens app → sees new activity from connections (variable social reward) → comments/reacts (investment increases network value). Cycle: daily. Hypothesis: users who establish this loop by D7 retain at 3× base rate."
- Bad: "Users come back because the product is useful." (no mechanism, untestable)
- Format: One table per hypothesized habit loop with all four Hooked components]

### Habit Loop [N]: [Name]

| Component | Description | Measurable Signal | Current Strength |
|-----------|-------------|-----------------|-----------------|
| Trigger | [External/internal trigger description] | [Event name] | [Frequency metric] |
| Action | [Core action taken] | [Event name] | [Completion rate] |
| Variable Reward | [Reward type and mechanism] | [Observable outcome] | [Reward rate] |
| Investment | [How the user loads future triggers] | [Investment depth metric] | [Investment rate] |

**Hypothesis**: Users who complete [N] cycles of this loop within Day [X] will show D30 retention ≥ [Y]%.
**Validation experiment**: [Brief experiment description]

## Churn Lever Taxonomy

[Classify churn reasons as preventable or structural.

GUIDANCE:
- Good: "Preventable (68%): Activation failure 40%, UX friction 18%, missing integration 10%. Structural (32%): Project ended 20%, budget cut 12%. Focus experiments on activation failure — largest preventable lever."
- Bad: "People leave for various reasons." (no data, no classification, no prioritization)
- Format: Table with lever, estimated prevalence (% of churned users), evidence source, and addressability]

| Churn Lever | Est. % of Churned Users | Evidence Source | Addressable? | Intervention |
|------------|------------------------|----------------|-------------|-------------|
| Activation failure | [X]% | Churn survey / cohort analysis | Yes | Onboarding redesign |
| UX friction | [X]% | Support tickets / session recordings | Yes | UX improvements |
| Missing feature | [X]% | Churn survey | Yes | Roadmap item |
| Competitor switch | [X]% | Exit survey | Partial | Win-back + positioning |
| Project/use case ended | [X]% | Exit survey | No | ICP refinement |

## Re-engagement Trigger Designs

[Design triggers for each major preventable churn category.

GUIDANCE:
- Good: "Trigger 1: Day 3 inactivity email — 'Your project is waiting' — sent to users who signed up but never completed activation step. Expected reactivation: 18%. A/B test: personalized reminder (treatment) vs. generic nudge (control)."
- Bad: "Send an email to inactive users." (no timing, no targeting, no expected impact)
- Format: One row per trigger with timing, channel, target segment, and expected reactivation rate]

| Trigger | Timing | Channel | Target Segment | Expected Reactivation | Experiment Design |
|---------|--------|---------|---------------|----------------------|-----------------|
| [Trigger 1] | Day [N] after last activity | [Channel] | [Segment description] | [X]% | [Treatment vs. control] |
| [Trigger 2] | [Condition] | [Channel] | [Segment description] | [X]% | [Treatment vs. control] |

## Quantitative Retention Model

[Sensitivity analysis for each retention lever.

GUIDANCE:
- Good: "If activation rate improves from 22% to 30% (+8pp), predicted D30 retention improves from 15% to 20.4% (+5.4pp). If D7 reactivation trigger achieves 18% reactivation rate, adds +1.8pp to D30 retention."
- Bad: "Improving retention will help." (no quantification)
- Format: Sensitivity table ranking interventions by predicted D30 retention impact]

| Intervention | Baseline Value | Improved Value | Predicted D30 Retention Impact | Implementation Effort |
|-------------|--------------|---------------|------------------------------|----------------------|
| [Intervention 1] | [X] | [Y] | +[Z]pp | [High/Med/Low] |
| [Intervention 2] | [X] | [Y] | +[Z]pp | [High/Med/Low] |
| [Intervention 3] | [X] | [Y] | +[Z]pp | [High/Med/Low] |

## Recommendations

[Prioritized retention experiments sorted by expected impact.
GUIDANCE: Lead with the highest-impact preventable churn lever. Each recommendation must name the experiment, the metric it improves, and the expected lift.

- P1: [Experiment name targeting primary preventable churn lever] — Expected D30 lift: +[X]pp — Owner: [team] — Timeline: [sprint]
- P1: [Re-engagement trigger experiment for largest inactive segment] — Expected reactivation rate: [Y]% — Owner: [team] — Timeline: [sprint]
- P2: [Habit loop strengthening experiment] — Expected D7 lift: +[Z]pp — Owner: [team] — Timeline: [next quarter]]

## Appendices

### A. Data Sources

[Churn survey methodology, cohort size per time point, retention analysis tool, and observation window.]

### B. Segment Retention Detail

[Retention curves broken out by key segments: channel, device, user type, pricing tier.]
