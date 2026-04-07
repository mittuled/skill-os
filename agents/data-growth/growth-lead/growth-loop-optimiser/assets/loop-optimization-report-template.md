# Growth Loop Optimization Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Analysis Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Active Loops Analysed | [N] |
| Skill | growth-loop-optimiser |

## Executive Summary

[2-3 sentences covering which loop is the highest priority optimization target, the primary bottleneck, and the projected compounding impact of the top experiment.

GUIDANCE: Example: "The viral referral loop is the highest-leverage target, with the bottleneck at the invite acceptance step (current: 12% → target: 18%). A 6 percentage point improvement in acceptance rate compounds to 34% more organic signups over 6 months at current cycle time."]

## Active Loop Inventory

| Loop Name | Loop Type | Input Users | Output Users | Throughput Rate | Cycle Time | Status |
|-----------|-----------|------------|-------------|-----------------|------------|--------|
| [Viral referral] | [Viral] | [N/month] | [N/month] | [k=0.XX] | [N days] | [Active / Stalled] |
| [SEO content] | [Content] | [N organic visits] | [N signups] | [X% CVR] | [N weeks] | [Active / Stalled] |
| [Paid reinvestment] | [Paid] | [$N spend] | [N signups] | [ROAS: X] | [N days] | [Active / Stalled] |
| [Product-led/PLG] | [Product-led] | [N free users] | [N paid conversions] | [X% CVR] | [N days] | [Active / Stalled] |

Minimum viable thresholds: Viral k ≥ 0.15 | Content CVR ≥ 1.5% | Paid ROAS ≥ 3x | PLG conversion ≥ 2%

---

## Loop Detail: [Loop Name]

### Loop Map

```
[Trigger Action] → [User Output] → [Distribution Mechanism] → [New User Input] → [Activation Step] → (back to Trigger)
```

Example:
```
User completes project → Shares result → Invite link in shared artifact → New user signs up → Activates within 48h → (loop)
```

### Node-Level Metrics

| Loop Node | Input | Output | Conversion Rate | Benchmark | Gap to Benchmark |
|-----------|-------|--------|----------------|-----------|-----------------|
| Trigger: [action taken] | [N users eligible] | [N who trigger] | [X%] | [X%] | [-X pp / on benchmark] |
| Distribution: [invites sent] | [N who trigger] | [N invites sent] | [X avg invites/user] | [X] | [-X / on benchmark] |
| Acceptance: [invite clicked] | [N invites sent] | [N clicks] | [X%] | [X%] | [-X pp] |
| Signup: [new user created] | [N clicks] | [N signups] | [X%] | [X%] | [-X pp] |
| Activation: [new user activates] | [N signups] | [N activated] | [X%] | [X%] | [-X pp] |

**Viral coefficient (k)**: [invites sent per user × acceptance rate × signup rate] = [k=0.XX]

**Cycle time**: [N days from trigger to new user activation]

**Bottleneck node**: [Node name] — [X pp below benchmark, largest absolute gap]

### Bottleneck Root Cause

[1-3 hypotheses explaining why the bottleneck node underperforms.]

1. [Hypothesis 1: e.g., "Invite prompt appears too late in the user journey — users haven't experienced value before being asked to share."]
2. [Hypothesis 2: e.g., "Invite email subject line is generic and has low open rate (18% vs. 35% benchmark)."]
3. [Hypothesis 3: e.g., "Shared artifact landing page lacks social proof and doesn't communicate value to the invitee."]

### Experiment Designs

#### Experiment A: [Short name]

| Field | Value |
|-------|-------|
| Hypothesis | [If we do X, then metric Y will improve by Z%] |
| Target Node | [Node name] |
| Primary Metric | [metric_name, e.g., invite acceptance rate] |
| Minimum Detectable Effect | [X pp improvement] |
| Implementation Effort | [Low / Medium / High] |
| Expected Impact | [+X pp on bottleneck node] |
| Projected Viral Coefficient After | [k=0.XX, up from current 0.XX] |

#### Experiment B: [Short name]

| Field | Value |
|-------|-------|
| Hypothesis | [If we do X, then metric Y will improve by Z%] |
| Target Node | [Node name] |
| Primary Metric | [metric_name] |
| Minimum Detectable Effect | [X pp] |
| Implementation Effort | [Low / Medium / High] |
| Expected Impact | [+X pp] |

---

## Compounding Impact Model

[Project 6-month user growth impact of top experiment assuming success.]

| Month | Baseline Organic Signups | Projected Organic Signups (Experiment A Success) | Cumulative Uplift |
|-------|------------------------|------------------------------------------------|------------------|
| Month 1 | [N] | [N] | [+N] |
| Month 2 | [N] | [N] | [+N] |
| Month 3 | [N] | [N] | [+N] |
| Month 6 | [N] | [N] | [+N total] |

Assumption: [State the k-value improvement used for projection and cycle time held constant.]

## Experiment Prioritization

| Rank | Loop | Experiment | Expected Impact | Effort | Priority Score |
|------|------|-----------|----------------|--------|----------------|
| 1 | [Viral] | [Experiment A] | [High] | [Low] | [Score] |
| 2 | [Content] | [Experiment B] | [Medium] | [Medium] | [Score] |
| 3 | [PLG] | [Experiment C] | [Medium] | [High] | [Score] |

Priority score = (Expected Impact × Confidence) ÷ Effort (1=low, 3=high for each).

## Recommended Next Actions

1. [Action 1: e.g., "Launch Experiment A on the viral referral loop — target start date [date]."]
2. [Action 2: e.g., "Fix the structural mechanic on the content loop before optimization experiments."]
3. [Action 3: e.g., "Re-measure loop metrics in 30 days after Experiment A concludes."]
