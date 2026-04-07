---
name: lead-scoring-model-builder
description: >
  This skill designs and calibrates the lead scoring model that determines MQL to SQL handoff.
  Use when building a new scoring model, recalibrating an existing model against conversion data,
  or when sales rejects a high percentage of MQLs. Also consider when ICP changes require
  updated firmographic scoring. Suggest when MQL-to-SQL conversion rates drop below 30%.
department: marketing
agent: marketing-operations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../../../marketing/vp-marketing/demand-gen-planner/SKILL.md
  - ../marketing-attribution-modeller/SKILL.md
---

# lead-scoring-model-builder

## Agent: Marketing Operations Manager

L2 marketing operations manager (1x) responsible for martech stack, lead scoring, campaign analytics, attribution modelling, and email deliverability.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Designs and calibrates the lead scoring model that combines behavioral and firmographic signals to determine MQL threshold and automate marketing-to-sales handoff.

## When to Use

- When building a lead scoring model for a new product line, segment, or market.
- When MQL-to-SQL conversion rates drop below acceptable thresholds, indicating miscalibration.
- When sales consistently rejects MQLs as unqualified, signaling a scoring-reality gap.
- When ICP definitions change and firmographic scoring weights need updating.

## Workflow

1. **Analyze historical conversions**: Pull closed-won and closed-lost data to identify which behavioral and firmographic attributes correlate with conversion. Use the two-axis scoring architecture from [`references/framework.md`](references/framework.md) to structure the analysis. Deliverable: attribute correlation analysis.
2. **Define scoring dimensions**: Build the fit score using the BANT dimensions table and the engagement score using the behavioral signals table in [`references/framework.md`](references/framework.md). Apply decay rules per signal. Deliverable: scoring model specification with attribute weights.
3. **Set MQL threshold**: Apply the calibration methodology in [`references/framework.md`](references/framework.md) — map historical closed-won leads against the model, set threshold at P80, and validate ≥ 25% MQL-to-SQL conversion. [GATE] — threshold requires sales sign-off before activation. Deliverable: MQL threshold with back-test results.
4. **Implement in marketing automation**: Configure the scoring model in the marketing automation platform. Set up automatic MQL status assignment, CRM sync, and sales notification workflows. Follow the governance standards in [`references/framework.md`](references/framework.md). Deliverable: live scoring model with automation rules.
5. **Calibrate and iterate**: Follow the calibration cadence in [`references/framework.md`](references/framework.md). After 30 days, compare actual MQL-to-SQL conversion against target. Adjust weights per governance process. Deliverable: calibration report with model adjustments.

## Anti-Patterns

- **Over-weighting content downloads**: Assigning high scores to every content download regardless of content type or funnel stage. *Why*: TOFU downloads like general industry reports indicate curiosity, not purchase intent; treating them equally inflates MQL counts with low-quality leads.
- **Firmographic-only scoring**: Scoring leads purely on company attributes without behavioral signals. *Why*: a perfect-fit company with zero engagement is not a qualified lead; intent signals are essential for timing the handoff.
- **Set-and-forget models**: Building the scoring model once and never recalibrating. *Why*: buyer behavior, ICP definitions, and product positioning evolve; a static model degrades in accuracy every quarter.

## Output

**On success**: Produces a lead scoring model specification, configured automation rules, and a calibration report. MQL-to-SQL conversion rates meet or exceed the agreed threshold. Delivered to VP Marketing, demand gen, and sales operations.

**On failure**: Report which data gaps prevented model building (insufficient conversion history, missing firmographic data), what interim scoring rules are in place, and recommend data collection steps to enable a full model.

## Related Skills

- [`demand-gen-planner`](../../../marketing/vp-marketing/demand-gen-planner/SKILL.md) — Defines the MQL criteria that this model operationalizes into automated scoring.
- [`marketing-attribution-modeller`](../marketing-attribution-modeller/SKILL.md) — Attribution data informs which touchpoints should receive higher behavioral scores.
- [`email-deliverability-manager`](../email-deliverability-manager/SKILL.md) — Email engagement signals are a key behavioral input to the scoring model.
