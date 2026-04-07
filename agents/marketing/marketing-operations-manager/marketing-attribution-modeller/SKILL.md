---
name: marketing-attribution-modeller
description: >
  This skill builds and maintains the multi-touch attribution model that credits marketing
  touchpoints for pipeline and revenue. Use when establishing attribution methodology, when
  channel budget decisions need attribution-backed data, or when attribution accuracy is
  questioned. Also consider when new channels are added that lack attribution coverage.
  Suggest when budget allocation debates lack data-driven grounding.
department: marketing
agent: marketing-operations-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../campaign-analytics-reporter/SKILL.md
  - ../../../marketing/demand-gen-manager/channel-signal-analyst/SKILL.md
---

# marketing-attribution-modeller

## Agent: Marketing Operations Manager

L2 marketing operations manager (1x) responsible for martech stack, lead scoring, campaign analytics, attribution modelling, and email deliverability.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Builds and maintains the multi-touch attribution model that assigns pipeline and revenue credit to marketing touchpoints across the buyer journey, enabling data-backed budget allocation.

## When to Use

- When establishing or replacing the company's marketing attribution methodology.
- When channel budget allocation decisions require attribution-backed pipeline contribution data.
- When stakeholders question attribution accuracy or dispute channel credit assignments.
- When new marketing channels or touchpoints are added and need integration into the attribution model.

## Workflow

1. **Audit touchpoint tracking**: Inventory all marketing touchpoints against the tracking requirements in [`references/framework.md`](references/framework.md). Verify each touchpoint captures UTMs, pixels, or CRM activity records. Flag any channel with < 90% coverage. Deliverable: touchpoint tracking audit with gap analysis.
2. **Select attribution methodology**: Use the model comparison table and decision tree in [`references/framework.md`](references/framework.md) to select the model that matches the company's sales cycle length and data maturity. Deliverable: attribution methodology recommendation with rationale.
3. **Implement the model**: Configure the attribution model following the data pipeline architecture in [`references/framework.md`](references/framework.md). Map touchpoints to attribution credit rules. Build integrations from ad platforms, MAP, and CRM into the attribution engine. Deliverable: live attribution model with data flowing.
4. **Validate accuracy**: Run the accuracy validation checks from [`references/framework.md`](references/framework.md) — touchpoint coverage, double-counting check, missing touchpoint audit, and revenue reconciliation. Deliverable: validation report with accuracy assessment against thresholds.
5. **Build attribution reporting**: Create dashboards across the reporting dimensions in [`references/framework.md`](references/framework.md) — channel, campaign, content, and stage. Deliverable: attribution dashboard accessible to marketing leadership.
6. **Establish governance**: Document methodology and implement governance standards from [`references/framework.md`](references/framework.md). Schedule quarterly reviews. Deliverable: attribution governance document.

## Anti-Patterns

- **Last-touch worship**: Defaulting to last-touch attribution because it is simplest to implement. *Why*: last-touch over-credits bottom-of-funnel channels and starves awareness and consideration channels of budget, eventually collapsing the top of the funnel.
- **Attribution without action**: Building a sophisticated model that produces reports nobody uses for budget decisions. *Why*: attribution models that do not influence allocation are cost centers; the model must connect to the budget process.
- **Ignoring offline touchpoints**: Only attributing digital touchpoints while ignoring events, direct mail, and sales-assisted touches. *Why*: incomplete models misrepresent the buyer journey and systematically undervalue high-touch, high-conversion channels.
- **False precision**: Presenting attribution percentages to decimal places when the underlying data has significant gaps. *Why*: over-precise numbers create false confidence and lead to budget decisions based on spurious accuracy.

## Output

**On success**: Produces a live multi-touch attribution model with validated accuracy, attribution dashboards showing pipeline and revenue by channel, and a governance document. Attribution data is actively used in budget allocation decisions. Delivered to VP Marketing, demand gen, and finance.

**On failure**: Report which touchpoints lack tracking coverage, what data pipeline issues prevent accurate attribution, and recommend specific instrumentation or tool changes to close gaps. Provide interim single-touch attribution as a fallback.

## Related Skills

- [`campaign-analytics-reporter`](../campaign-analytics-reporter/SKILL.md) — Consumes attribution data to report channel-level pipeline contribution in weekly reports.
- [`channel-signal-analyst`](../../../marketing/demand-gen-manager/channel-signal-analyst/SKILL.md) — Uses attribution output to recommend budget reallocation across channels.
- [`martech-stack-manager`](../martech-stack-manager/SKILL.md) — Manages the platforms and integrations that capture the touchpoint data attribution depends on.
- [`gtm-planner-marketing`](../../../marketing/vp-marketing/gtm-planner-marketing/SKILL.md) — Uses attribution data to project channel ROI when building GTM plans.
