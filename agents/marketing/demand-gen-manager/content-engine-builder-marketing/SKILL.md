---
name: content-engine-builder-marketing
description: >
  This skill builds the content production engine that feeds demand generation across channels.
  Use when standing up a repeatable content pipeline, scaling content output for new channels,
  or restructuring content operations after a positioning shift. Also consider when content
  production is ad hoc and inconsistent. Suggest when demand gen plans require content assets
  that no production system exists to deliver.
department: marketing
agent: demand-gen-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../../../marketing/content-marketer/content-marketing-operations/SKILL.md
  - ../channel-signal-analyst/SKILL.md
triggers:
  - "build a content engine"
  - "set up repeatable content production"
  - "scale content output"
  - "create a content pipeline"
---

# content-engine-builder-marketing

## Agent: Demand Gen Manager

L2 demand generation manager (1x) responsible for channel signal analysis, content engine operations, and roadmap timing input for marketing campaigns.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Builds the repeatable content production engine -- editorial calendar, workflow, contributors, and distribution mapping -- that feeds demand generation across all channels.

## When to Use

- When demand gen plans require a steady content pipeline but production is ad hoc or bottlenecked.
- When scaling into new channels (podcast, webinar, community) that need dedicated content streams.
- When a major positioning or ICP shift requires rebuilding the content strategy and production workflow.
- When content output is inconsistent, causing gaps in nurture sequences and campaign calendars.

## Workflow

1. **Map content to funnel stages**: Define content types needed at each funnel stage using the content-to-funnel mapping in [`references/framework.md`](references/framework.md). Every piece must belong to exactly one stage. Deliverable: content-to-funnel mapping matrix.
2. **Build editorial calendar**: Create a rolling 90-day editorial calendar using the cadence structure in [`references/framework.md`](references/framework.md). Align topics to demand gen campaign themes and seasonal patterns. Deliverable: editorial calendar in shared tool.
3. **Design production workflow**: Implement the 8-stage production workflow with SLAs per stage from [`references/framework.md`](references/framework.md). Assign role responsibilities per stage. Deliverable: documented production workflow with SLAs.
4. **Establish contributor network**: Onboard contributors using the tier model and brief standards in [`references/framework.md`](references/framework.md). Deliver brief templates and style guides for each contributor type. Deliverable: contributor roster with brief templates.
5. **Map distribution channels**: Apply the distribution playbook from [`references/framework.md`](references/framework.md) to define primary and repurpose distribution for each content type. Automate distribution where possible. Deliverable: distribution playbook per content type.

## Anti-Patterns

- **Hero-dependent production**: Relying on a single writer or SME for all content without backup or documentation. *Why*: single points of failure create production gaps when that person is unavailable, stalling demand gen campaigns.
- **Publish-and-pray**: Creating content without a distribution plan for each piece. *Why*: undistributed content generates zero demand regardless of quality; the engine must include distribution as a first-class step.
- **Quantity over conversion**: Optimizing the engine for volume of pieces published rather than leads generated per piece. *Why*: a high-output engine producing content that nobody reads or converts on is a cost center, not a demand driver.

## Output

**On success**: Produces a content-to-funnel mapping, 90-day editorial calendar, documented production workflow with SLAs, contributor roster, and distribution playbook. The engine produces content on a predictable cadence that feeds demand gen campaigns. Delivered to VP Marketing and content team.

**On failure**: Report which components of the engine could not be established (contributor gaps, tool limitations, SME availability), what interim workarounds are in place, and recommend specific hires, tools, or process changes to close gaps.

## Related Skills

- [`content-marketing-operations`](../../../marketing/content-marketer/content-marketing-operations/SKILL.md) — Operates the day-to-day content production that this engine enables.
- [`channel-signal-analyst`](../channel-signal-analyst/SKILL.md) — Provides channel performance data that informs which content types and topics to prioritize in the engine.
- [`demand-gen-planner`](../../../marketing/vp-marketing/demand-gen-planner/SKILL.md) — Sets the campaign themes and lead targets that the content engine must support.
