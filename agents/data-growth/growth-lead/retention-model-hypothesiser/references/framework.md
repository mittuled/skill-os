# Framework: Retention Model Hypothesiser

Defines the structural methodology for building a hypothesis-driven retention model including habit loop analysis, re-engagement trigger design, and churn lever taxonomy.

## Retention Benchmarks by Product Category

| Product Category | D1 | D7 | D30 | D90 | Notes |
|-----------------|-----|-----|-----|-----|-------|
| Consumer social | 25–35% | 10–20% | 5–10% | 3–7% | High churn baseline |
| Consumer utility | 40–60% | 20–35% | 10–20% | 7–15% | Value-driven retention |
| SMB SaaS (daily) | 60–75% | 45–60% | 30–45% | 20–35% | Workflow-integrated |
| Enterprise SaaS | 80–90% | 70–85% | 60–75% | 50–65% | Contract + integration lock-in |
| Marketplace | 30–50% | 20–35% | 10–20% | 5–15% | Transaction-frequency dependent |

Source: Reforge retention benchmarks. Use as orientation; actuals vary significantly by ICP and use case.

## Habit Loop Model (Hooked Framework)

Based on Nir Eyal's Hooked model, adapted for retention analysis.

| Component | Definition | Observable Signal | Strengthening Lever |
|-----------|-----------|------------------|-------------------|
| **Trigger** | Cue that initiates the behaviour | External: push/email/social. Internal: emotion/habit | Make external triggers contextual; build toward internal |
| **Action** | Simplest behaviour in anticipation of reward | Core action that delivers value | Reduce steps, time, and cognitive load |
| **Variable Reward** | Reward that is unpredictable enough to compel repeat | Tribal (social), Hunt (search/discovery), Self (achievement) | Increase reward variability; avoid predictable patterns |
| **Investment** | User input that loads future triggers | Data, preferences, connections, content, history | Create irreversible investment that increases switching cost |

## Retention Curve Interpretation

### Inflection Points and What They Mean

| Curve Pattern | Interpretation | Intervention |
|--------------|---------------|-------------|
| Sharp D1 drop, flat after | Onboarding friction — users who pass D1 are committed | Fix first-session experience |
| Gradual linear decline | No habit formation — product lacks a "hook" | Build habit triggers and variable rewards |
| Cliff at D30 | Seasonal or contract-based usage pattern | Design around natural usage cadence |
| Asymptote > 20% (SaaS) | Healthy power user core | Optimize for expansion, not just retention |
| Asymptote near 0% | No retained audience — product lacks sustained value | Product-market fit re-evaluation |

## Churn Lever Taxonomy

### Preventable Churn (Experiment-Addressable)
1. **Activation failure**: User never experienced the core value moment
2. **UX friction**: Product is hard to use, causing abandonment
3. **Missing feature**: Required use case not yet built
4. **Support failure**: Bug or issue went unresolved
5. **Notification fatigue**: Over-communication drove disengagement

### Structural Churn (Not Experiment-Addressable)
1. **Graduated**: User no longer needs the product (student finishes semester)
2. **Competitor switch**: Moved to an alternative that better serves their needs
3. **Budget cut**: Economic constraint, not product dissatisfaction
4. **Out of ICP**: User was never the right customer

**Rule**: Do not run retention experiments on users in structural churn categories — resource waste with zero conversion potential.

## Re-engagement Trigger Design Framework

| Trigger Type | Timing Window | Optimal Channel | Expected Reactivation Rate |
|-------------|--------------|----------------|--------------------------|
| Inactivity nudge (first absence) | Day 3–5 after last activity | Push > Email | 15–25% (consumer), 8–12% (SaaS) |
| Feature announcement | Anytime; new feature relevant to churned segment | Email | 5–12% |
| Social trigger | Within 24h of relevant peer activity | Push + In-app | 20–35% |
| Milestone / anniversary | Day 30, Day 90, annual | Email | 3–8% |
| Incentive offer | Day 14–21 (before structural churn solidifies) | Email | 8–15% |

**Warning**: Re-engagement triggers after Day 30 inactivity have sharply diminishing returns; focus experiment energy on Days 1–14.

## Quantitative Retention Model Structure

```
D30 Retention = f(habit_loop_frequency, re_engagement_effectiveness, structural_churn_rate)

Predicted_D30 = Activation_rate 
              × (1 - preventable_churn_rate)
              × (1 - structural_churn_rate)
              + reactivated_users_rate

Where:
  preventable_churn_rate = Σ (churn_lever_i × prevalence_i)
  structural_churn_rate = estimated from segment ICP analysis
  reactivated_users_rate = (lapsed_users × trigger_reach × trigger_effectiveness)
```

Sensitivity: a 5% reduction in preventable churn at D30 produces approximately 5.5% more monthly active users at steady state.
