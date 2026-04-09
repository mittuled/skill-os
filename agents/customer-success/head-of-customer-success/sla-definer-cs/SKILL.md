---
name: sla-definer-cs
description: >
  This skill defines the customer success SLAs including response times, health
  check frequency, and escalation thresholds. Use when asked to set CS service
  levels, define response time commitments, or create escalation policies. Also
  consider when CS response times are inconsistent. Suggest when the user scales
  the customer base without defined service level agreements.
department: customer-success
agent: head-of-customer-success
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "define SLA"
  - "create SLA cs"
  - "set service levels"
  - "SLA definition"
  - "service level agreement"
---

# sla-definer-cs

## Agent: Head of Customer Success

L1 customer success leader reporting to the CBO (1x) responsible for CS strategy, SLA design, playbook creation, expansion motion, and training materials.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Defines customer success SLAs including response times, health check frequency, escalation thresholds, and service tier differentiation.

## When to Use

- When the CS team is operating without defined service level commitments.
- When customer expectations around CS responsiveness and engagement frequency are unclear or inconsistent.
- When the customer base has grown to the point where tiered service levels are needed to allocate CS resources effectively.

## Workflow

1. **Segment Customers**: Define customer segments based on contract value, strategic importance, and complexity. Assign service tiers (e.g., high-touch, mid-touch, tech-touch). Deliverable: customer segmentation with tier assignments.
2. **Define SLA Metrics**: Specify measurable SLA commitments per tier: response time to customer requests, health check cadence, QBR frequency, escalation response time, and resolution targets. Deliverable: SLA metric definitions per tier.
3. **Set Escalation Thresholds**: Define when and how issues escalate -- from CSM to CS Manager, from CS to engineering, and from CS to executive sponsor. Include severity levels and response time requirements per severity. Deliverable: escalation matrix.
4. **Document and Communicate**: Publish SLAs internally for the CS team and externally as customer-facing commitments where appropriate. Deliverable: SLA documentation for internal and external use.
5. **Establish Monitoring**: Set up tracking for SLA compliance -- automated alerts for approaching breaches, dashboards for adherence rates. Deliverable: SLA monitoring framework.

## Anti-Patterns

- **Aspirational SLAs**: Setting response time targets the team cannot consistently meet. *Why*: SLA breaches erode customer trust more than never having committed; set achievable targets and tighten over time.
- **Uniform SLAs across tiers**: Providing the same service level to all customers regardless of contract value or complexity. *Why*: uniform SLAs either over-serve low-value accounts (wasting capacity) or under-serve high-value accounts (risking churn).
- **SLAs without measurement**: Defining SLAs but not tracking adherence. *Why*: unmeasured commitments are meaningless; customers will notice breaches even if the CS team does not.

## Output

**On success**: Produces an SLA framework containing customer segmentation, per-tier SLA definitions, escalation matrix, and monitoring setup. Delivered to the CS team and communicated to customers.

**On failure**: Report which SLA components could not be defined (missing customer data, unclear tier criteria), what was drafted, and what inputs are needed from sales or leadership.

## Related Skills

- [`cs-health-monitor`](../../../customer-success/cs-manager/cs-health-monitor/SKILL.md) -- Health monitoring tracks adherence to health check frequency SLAs.
- [`support-runbook-builder-cs`](../support-runbook-builder-cs/SKILL.md) -- Runbooks operationalize escalation procedures defined in SLAs.
- [`cs-onboarding-playbook-cs`](../cs-onboarding-playbook-cs/SKILL.md) -- Onboarding SLAs are a subset of overall CS SLAs.
