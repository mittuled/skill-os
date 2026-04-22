---
name: cs-release-readiness
description: >
  This skill confirms the CS team is ready for a product release including
  training, runbooks, and communication plans. Use when asked to assess CS
  readiness for a launch, create release communication plans, or verify CS
  preparedness. Also consider when releases are planned without CS input.
  Suggest when the user ships features without a CS readiness check.
department: customer-success
agent: cs-manager
version: 1.0.0
complexity: simple
related-skills:
  - training-material-creator-cs
  - support-runbook-builder-cs
  - cohort-selector-cs
triggers:
  - "cs release readiness"
  - "prepare cs for release"
  - "release readiness check"
  - "is cs ready for launch"
  - "support readiness review"
---

# cs-release-readiness

## Agent: CS Manager

L2 customer success manager (1x) responsible for CS cohort selection, release readiness, health monitoring, and case study extraction.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Confirms the CS team is ready for a product release by verifying training completion, runbook updates, and customer communication plans.

## When to Use

- When a product release is approaching and CS readiness needs verification.
- When a major feature launch requires coordinated customer communication from the CS team.
- When past releases have caught the CS team off-guard and a readiness process needs formalization.

## Workflow

1. **Review Release Scope**: Understand what is being released, who it affects, and what changes in customer experience. Deliverable: release impact summary for CS.
2. **Verify CS Preparedness**: Check that training materials are updated, runbooks cover new scenarios, and CSMs have been briefed. Deliverable: readiness checklist with pass/fail per item.
3. **Prepare Communication Plan**: Draft customer-facing communications: release announcements, feature guides, and proactive outreach for affected accounts. Deliverable: communication plan with templates and timeline.
4. **Confirm Go/No-Go**: Issue a CS readiness verdict. If not ready, specify what must be completed before release. Deliverable: go/no-go recommendation with rationale.

## Anti-Patterns

- **Rubber-stamp readiness**: Approving readiness without actually verifying training and runbook updates. *Why*: a false-ready signal leads to CSMs fielding customer questions they cannot answer, damaging credibility.
- **Last-minute readiness checks**: Running the readiness check the day before release. *Why*: finding gaps with no time to fix them means releasing anyway without CS support, or delaying the release.
- **CS-only communication**: Preparing CS team communications without coordinating with marketing and product on messaging consistency. *Why*: customers who receive conflicting messages from different teams lose confidence in the organization.

## Output

**On success**: Produces a CS readiness report containing the readiness checklist, communication plan, and go/no-go recommendation. Delivered to the Head of Customer Success and product team.

**On failure**: Report which readiness items failed (incomplete training, missing runbooks), what can be resolved before release, and the recommended release delay if critical items are unresolved.

## Related Skills

- [`training-material-creator-cs`](../../../customer-success/head-of-customer-success/training-material-creator-cs/SKILL.md) -- Training materials must be complete for release readiness.
- [`support-runbook-builder-cs`](../../../customer-success/head-of-customer-success/support-runbook-builder-cs/SKILL.md) -- Runbooks must cover new release scenarios.
- [`cohort-selector-cs`](../cohort-selector-cs/SKILL.md) -- Phased releases require cohort selection as part of readiness.
