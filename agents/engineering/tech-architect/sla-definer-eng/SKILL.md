---
name: sla-definer-eng
description: >
  This skill defines service-level agreements for engineering systems including uptime, latency,
  and error-rate targets. Use when asked to set SLAs, define reliability targets, or establish
  SLOs and SLIs. Also consider when launching a new service without defined availability
  expectations. Suggest when engineers are building without explicit reliability contracts.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-architect/performance-budget-setter-eng/SKILL.md
  - ../../../engineering/tech-architect/scale-infrastructure-planner/SKILL.md
---

# sla-definer-eng

## Agent: Tech Architect

L2 technical architect (1x) responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Defines the service-level agreements, objectives, and indicators that engineering teams target for uptime, latency, error rate, and throughput.

## When to Use

- When a new service or system is being planned and needs explicit reliability and performance targets before development begins.
- When product or business stakeholders request formal availability guarantees for a customer-facing feature.
- When an existing service has no documented SLAs and incidents are being triaged without clear severity definitions.

## Workflow

1. **Inventory services and dependencies**: List all services in scope and their upstream/downstream dependencies. Identify which components are on the critical path. Deliverable: service dependency map with criticality annotations.
2. **Define SLIs**: For each service, select the measurable indicators that reflect user-facing health (e.g., request latency p99, error rate, availability percentage). Deliverable: SLI catalog per service.
3. **Set SLO targets**: Establish target values for each SLI based on business requirements, historical data, and infrastructure constraints. Distinguish between internal SLOs and external SLAs. Deliverable: SLO target table with justification.
4. **Define error budgets**: Calculate the error budget for each SLO (e.g., 99.9% availability = 43.8 min/month of allowed downtime). Document how budget consumption triggers policy changes. Deliverable: error budget policy document.
5. **Establish measurement and alerting**: Specify how each SLI is measured, where dashboards live, and what alert thresholds map to SLO burn rates. Deliverable: monitoring and alerting specification.
6. **Review and ratify**: Present SLAs to engineering, product, and operations stakeholders. Incorporate feedback and get sign-off. Deliverable: ratified SLA document.

## Anti-Patterns

- **Aspirational SLAs**: Setting targets based on wishes rather than measured baselines. *Why*: unrealistic SLAs erode trust when inevitably breached and train teams to ignore alerts.
- **SLA without measurement**: Defining targets without corresponding SLIs or dashboards. *Why*: an SLA you cannot measure is indistinguishable from having no SLA at all.
- **Uniform targets across services**: Applying identical SLAs to every service regardless of criticality. *Why*: non-critical services consume engineering effort maintaining unnecessary nines while critical services may be under-protected.

## Output

**On success**: Produces an SLA document containing SLIs, SLO targets, error budgets, measurement methods, and alerting thresholds for each in-scope service. Delivered to the project repository and shared with engineering, product, and operations stakeholders.

**On failure**: Report which services could not have SLAs defined (e.g., missing baseline metrics, undefined business criticality), what data is needed, and recommended next steps to unblock.

## Related Skills

- [`performance-budget-setter-eng`](../../../engineering/tech-architect/performance-budget-setter-eng/SKILL.md) -- performance budgets constrain the latency and throughput targets that SLAs codify.
- [`scale-infrastructure-planner`](../../../engineering/tech-architect/scale-infrastructure-planner/SKILL.md) -- infrastructure scaling plans must align with the availability and throughput targets defined in SLAs.
