---
name: demand-gen-planner
description: >
  This skill plans the demand generation strategy including lead volume targets, channel investment,
  and MQL definitions. Use when building quarterly demand plans, setting pipeline targets, or
  defining MQL criteria. Also consider when channel ROI shifts require rebalancing spend.
  Suggest when a new quarter is approaching without an updated demand gen plan.
department: marketing
agent: vp-marketing
version: 1.0.0
complexity: complex
related-skills:
  - ../../demand-gen-manager/channel-signal-analyst/SKILL.md
  - ../../marketing-operations-manager/lead-scoring-model-builder/SKILL.md
triggers:
  - "plan demand generation"
  - "set pipeline targets for the quarter"
  - "build the demand gen strategy"
  - "how do we generate more leads"
---

# demand-gen-planner

## Agent: VP Marketing

L1 marketing leader (1x) reporting to the CBO, responsible for GTM planning, demand generation strategy, and marketing activation across all channels.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Plans the demand generation strategy including lead volume targets, channel investment mix, and MQL definitions aligned to pipeline and revenue goals.

## When to Use

- When building or refreshing the quarterly demand generation plan with pipeline targets by channel.
- When finance or sales requests updated lead volume commitments tied to revenue forecasts.
- When channel performance data reveals a significant shift in cost-per-MQL or conversion rates requiring reallocation.
- When entering a new market segment that needs its own demand gen motion and ICP-specific targeting.

## Workflow

1. **Gather revenue targets**: Obtain the quarterly revenue and pipeline targets from CBO and RevOps. Confirm ASP, win rate, and sales cycle assumptions using the waterfall model in [`references/framework.md`](references/framework.md). Deliverable: validated revenue-to-pipeline model.
2. **Back into lead volumes**: Calculate required MQLs, SQLs, and opportunities by working backward from pipeline targets through funnel conversion rates. Deliverable: lead volume waterfall by stage.
3. **Audit channel performance**: Pull historical CPL, conversion rate, and velocity data for each acquisition channel. Compare against the unit economics benchmarks in [`references/framework.md`](references/framework.md). Flag channels above CAC threshold or below volume floor. Deliverable: channel performance scorecard.
4. **Define MQL criteria**: Align with sales on behavioral and firmographic scoring thresholds using the MQL definition standards in [`references/framework.md`](references/framework.md). Document handoff SLA. Deliverable: MQL definition document with sales sign-off.
5. **Allocate channel budget**: Distribute demand gen budget across channels using the allocation model in [`references/framework.md`](references/framework.md). Reserve 15–20% for experimentation on emerging channels. Deliverable: channel investment plan in [`assets/demand-gen-plan-template.md`](assets/demand-gen-plan-template.md).
6. **Set measurement cadence**: Define weekly leading indicators and monthly lagging indicators using the measurement cadence table in [`references/framework.md`](references/framework.md). Assign dashboard ownership. Deliverable: measurement framework and reporting calendar.
7. **Socialize and lock plan**: Present the completed [`assets/demand-gen-plan-template.md`](assets/demand-gen-plan-template.md) to CBO, sales leadership, and RevOps for alignment. Incorporate feedback and lock the plan for the quarter. Deliverable: approved demand gen plan.

## Anti-Patterns

- **Vanity volume targeting**: Setting MQL targets based on lead count rather than pipeline quality. *Why*: high-volume low-quality leads waste sales capacity and erode trust in marketing's contribution to revenue.
- **Peanut-butter budgeting**: Spreading budget evenly across channels regardless of performance data. *Why*: equal allocation ignores that channels have wildly different CPLs, conversion rates, and sales cycle velocities.
- **Static quarterly plans**: Locking the plan and refusing to reallocate mid-quarter when signals change. *Why*: demand gen operates in dynamic markets where a channel can saturate or a competitor can shift the landscape in weeks.
- **MQL definition drift**: Allowing the MQL definition to change informally without sales alignment. *Why*: unilateral changes to qualification criteria break the marketing-sales SLA and poison pipeline reporting.

## Output

**On success**: Produces a demand generation plan document containing revenue-backed lead volume targets by stage, channel investment allocations with expected CPL and yield, MQL definitions with sales-agreed handoff SLA, and a measurement framework. Delivered as a shared document to CBO, sales leadership, and RevOps.

**On failure**: Report which inputs were missing (revenue targets, historical channel data, or sales alignment), what assumptions were used as fallbacks, and recommend specific actions to unblock (e.g., schedule sales-marketing MQL alignment session).

## Related Skills

- [`channel-signal-analyst`](../../demand-gen-manager/channel-signal-analyst/SKILL.md) — Provides the channel performance data that informs budget allocation decisions in this plan.
- [`lead-scoring-model-builder`](../../marketing-operations-manager/lead-scoring-model-builder/SKILL.md) — Operationalizes the MQL definitions established in this plan into the scoring model.
- [`gtm-planner-marketing`](../gtm-planner-marketing/SKILL.md) — The broader GTM plan that this demand gen plan executes against.
- [`campaign-analytics-reporter`](../../marketing-operations-manager/campaign-analytics-reporter/SKILL.md) — Produces the weekly reports that track progress against this plan's targets.
