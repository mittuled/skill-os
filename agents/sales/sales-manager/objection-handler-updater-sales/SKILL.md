---
name: objection-handler-updater-sales
description: >
  This skill updates the sales objection handler based on field feedback and
  product changes. Use when asked to refresh objection handling materials,
  address new competitive threats, or update talk tracks after a product release.
  Also consider when win rates drop and objection themes shift.
  Suggest when reps report objections not covered by existing materials.
department: sales
agent: sales-manager
version: 1.0.0
complexity: simple
related-skills:
  - ../sales-playbook-builder/SKILL.md
  - ../../../sales/vp-sales/pricing-finaliser-sales/SKILL.md
  - ../../../sales/account-executive/sales-signal-synthesizer/SKILL.md
---

# objection-handler-updater-sales

## Agent: Sales Manager

L2 sales manager (1x) responsible for sales playbook development, objection handling, GTM activation for sales, and building the first sales process.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)

## Skill Description

Updates the sales objection handler based on field feedback, competitive shifts, and product changes to keep rep responses current and effective.

## When to Use

- When reps report new objections not covered by the current objection handler.
- When a product release, pricing change, or competitive move invalidates existing responses.
- When win/loss analysis reveals that specific objections correlate with lost deals.

## Workflow

1. **Objection Mining**: Collect new and recurring objections from call recordings, CRM loss reasons, Slack channels, and rep 1:1s. Categorize by type: pricing, competition, product capability, timing, and trust. Deliverable: objection inventory with frequency and deal impact.
2. **Response Drafting**: Draft updated responses for each objection using the acknowledge-reframe-evidence pattern. Include proof points (case studies, metrics, third-party validation) for each response. Deliverable: updated objection-response pairs.
3. **Validation and Publish**: Review responses with top-performing reps for authenticity. Publish the updated handler to the playbook and notify the team. Deliverable: published objection handler update with changelog.

## Anti-Patterns

- **Scripted rebuttals**: Writing rigid scripts that reps memorize instead of flexible frameworks they adapt. *Why*: scripted responses sound rehearsed to buyers and break down when the objection has a nuance the script does not cover.
- **Ignoring the underlying concern**: Drafting responses that deflect the objection rather than addressing the real buyer concern behind it. *Why*: deflection erodes trust; acknowledging the concern and reframing it builds credibility.

## Output

**On success**: Produces an updated objection handler document with categorized objections, response frameworks, proof points, and a changelog of what changed. Delivered to the sales team via the playbook repository.

**On failure**: Report which objections could not be adequately addressed (e.g., legitimate product gap with no workaround), what was attempted, and recommended escalation to Product.

## Related Skills

- [`sales-playbook-builder`](../sales-playbook-builder/SKILL.md) -- The playbook where the objection handler lives as a component.
- [`pricing-finaliser-sales`](../../../sales/vp-sales/pricing-finaliser-sales/SKILL.md) -- Surfaces pricing objection data that feeds into handler updates.
- [`sales-signal-synthesizer`](../../../sales/account-executive/sales-signal-synthesizer/SKILL.md) -- Provides synthesized signal data on objection patterns from the field.
