---
name: gtm-planner-marketing
description: >
  This skill develops the overall go-to-market plan for the marketing function including channel mix,
  timing, and budget allocation. Use when launching a new product, entering a new market, or resetting
  annual marketing strategy. Also consider when positioning shifts require a revised GTM approach.
  Suggest when product roadmap milestones lack a corresponding marketing plan.
department: marketing
agent: vp-marketing
version: 1.0.0
complexity: complex
related-skills:
  - ../gtm-activation-marketing/SKILL.md
  - ../demand-gen-planner/SKILL.md
triggers:
  - "build the go-to-market plan"
  - "plan the GTM strategy"
  - "how should we launch this to market"
  - "create a marketing launch plan"
---

# gtm-planner-marketing

## Agent: VP Marketing

L1 marketing leader (1x) reporting to the CBO, responsible for GTM planning, demand generation strategy, and marketing activation across all channels.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Develops the overall go-to-market plan for the marketing function including channel mix, timing, budget allocation, and positioning strategy tied to revenue objectives.

## When to Use

- When a new product or major feature launch requires a coordinated marketing plan across all channels.
- When entering a new market segment or geography that needs a tailored GTM motion.
- When annual or semi-annual marketing strategy resets require a fresh plan aligned to updated revenue targets.
- When competitive positioning shifts demand a revised channel mix and messaging framework.

## Workflow

1. **Synthesize market inputs**: Gather ICP definitions, competitive landscape, product positioning, and revenue targets from product marketing, sales, and CBO. Use the ICP-to-channel mapping in [`references/framework.md`](references/framework.md) to structure inputs. Deliverable: market context brief.
2. **Define GTM objectives**: Translate revenue targets into marketing-specific objectives using the KPI framework in [`references/framework.md`](references/framework.md). Assign measurable KPIs per objective. Deliverable: GTM objectives with KPIs.
3. **Select channel mix**: Score and rank channels using the channel priority matrix model in [`references/framework.md`](references/framework.md). Prioritize channels scoring ≥ 14/20. Deliverable: scored channel priority matrix.
4. **Build timeline**: Sequence marketing activities against the GTM phase model in [`references/framework.md`](references/framework.md) — pre-launch, launch, amplification, steady state. Identify phase gates and channel activations per phase. Deliverable: GTM timeline with phase gates.
5. **Allocate budget**: Distribute the marketing budget using the stage-based budget allocation model in [`references/framework.md`](references/framework.md). Tie each allocation to an expected output (leads, pipeline, impressions). Deliverable: budget allocation with ROI projections.
6. **Align cross-functional stakeholders**: Present the GTM plan and work through the sign-off checklist in [`references/framework.md`](references/framework.md). Resolve conflicts on timing, messaging, or resource allocation. Deliverable: cross-functional sign-off document.
7. **Publish and distribute**: Finalize the GTM plan and distribute to all execution teams. Ensure every channel owner has their specific brief, timeline, and budget. Deliverable: published GTM plan with channel-specific briefs.

## Anti-Patterns

- **Product-out planning**: Building the GTM plan around product features rather than buyer problems and market positioning. *Why*: feature-led plans produce messaging that resonates internally but fails to connect with buyer pain points.
- **Channel comfort bias**: Selecting channels based on team expertise rather than ICP behavior data. *Why*: marketers default to channels they know, which may not be where target buyers actually consume information.
- **Budget-before-strategy**: Locking budget allocations before defining objectives and channel priorities. *Why*: budget-first planning forces strategy to fit arbitrary constraints rather than revenue logic.
- **Planning in isolation**: Building the GTM plan without sales, product, and CS input. *Why*: marketing plans that ignore sales capacity, product readiness, or customer feedback produce campaigns that launch into organizational misalignment.

## Output

**On success**: Produces a comprehensive GTM plan document containing market context, objectives with KPIs, channel priority matrix, phased timeline, budget allocations with ROI projections, and channel-specific briefs. Delivered to CBO, sales leadership, product marketing, and all channel execution teams.

**On failure**: Report which strategic inputs were unavailable (ICP data, competitive intelligence, revenue targets), what assumptions were substituted, and recommend steps to fill gaps before plan finalization.

## Related Skills

- [`gtm-activation-marketing`](../gtm-activation-marketing/SKILL.md) — Executes the activation phase of the GTM plan this skill produces.
- [`demand-gen-planner`](../demand-gen-planner/SKILL.md) — Translates the GTM plan's channel strategy into specific lead volume targets and MQL definitions.
- [`channel-signal-analyst`](../../../marketing/demand-gen-manager/channel-signal-analyst/SKILL.md) — Provides historical channel performance data that informs channel mix selection.
- [`marketing-attribution-modeller`](../../../marketing/marketing-operations-manager/marketing-attribution-modeller/SKILL.md) — Supplies the attribution data used to project channel ROI in budget allocation.
