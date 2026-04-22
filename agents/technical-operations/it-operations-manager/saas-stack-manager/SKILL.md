---
name: saas-stack-manager
description: >
  This skill manages the company SaaS stack including procurement, configuration, and renewal management.
  Use when asked to evaluate new tools, consolidate SaaS subscriptions, or manage software renewals.
  Also consider when SaaS spend is growing without visibility into utilisation.
  Suggest when annual renewal season approaches and contracts need review.
department: technical-operations
agent: it-operations-manager
version: 1.0.0
complexity: medium
related-skills:
  - identity-access-management
  - access-provisioning-manager
  - vendor-contract-manager
triggers:
  - "manage SaaS stack"
  - "evaluate new SaaS tools"
  - "SaaS tool audit"
  - "software renewal management"
  - "consolidate SaaS subscriptions"
---

# saas-stack-manager

## Agent: IT Operations Manager

L1 IT operations manager (1x) reporting to the COO, responsible for SaaS stack management, access provisioning, hardware lifecycle, and identity and access management.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)

## Skill Description

The SaaS stack manager maintains a registry of all company software subscriptions, tracks utilisation and spend, manages renewals and procurement, and identifies consolidation opportunities to keep the software portfolio efficient and cost-effective.

## When to Use

- When a team requests a new SaaS tool and it needs evaluation against existing stack capabilities.
- When annual renewal season approaches and contracts need review before auto-renewal deadlines.
- When SaaS spend exceeds budget and the organisation needs visibility into utilisation rates.
- When an employee departs and their individual SaaS licences need to be reclaimed or reassigned.

## Workflow

1. **Maintain the SaaS registry**: Keep an up-to-date inventory of all subscriptions including vendor, cost, licence count, renewal date, and owner. Deliverable: current SaaS registry.
2. **Track utilisation**: Monitor login frequency and feature usage for each tool to identify underutilised subscriptions. Deliverable: utilisation report.
3. **Evaluate new requests**: Assess new tool requests against existing capabilities, security requirements, and budget. Deliverable: evaluation recommendation (approve, deny, or suggest alternative).
4. **Manage renewals**: Review upcoming renewals 60 days in advance, assess value, negotiate terms, and process or cancel. Deliverable: renewal decision log.
5. **Identify consolidation**: Flag overlapping tools that serve similar purposes and recommend consolidation. Deliverable: consolidation recommendation report.

## Anti-Patterns

- **Shadow IT tolerance**: Allowing teams to procure SaaS tools outside the managed process. *Why*: untracked subscriptions create security gaps, compliance risk, and redundant spend.
- **Auto-renewal by default**: Letting contracts auto-renew without review. *Why*: underutilised tools renew at full price, and contract terms may have changed unfavourably.
- **Licence hoarding**: Maintaining paid seats for users who no longer use the tool. *Why*: unused licences are pure waste and inflate the SaaS budget.

## Output

**On success**: A current SaaS registry with utilisation data, timely renewal decisions, evaluated new tool requests, and consolidation recommendations that reduce redundancy and cost.

**On failure**: Report which tools could not be assessed (e.g., vendor did not provide usage data), what was completed, and recommend manual audit steps to fill gaps.

## Related Skills

- [`identity-access-management`](../identity-access-management/SKILL.md) -- IAM integrates with the SaaS tools this skill manages.
- [`access-provisioning-manager`](../access-provisioning-manager/SKILL.md) -- access provisioning needs the SaaS registry to know which systems to provision.
- [`vendor-contract-manager`](../../../technical-operations/vendor-management-procurement/vendor-contract-manager/SKILL.md) -- vendor contract management handles the commercial terms of SaaS subscriptions.
