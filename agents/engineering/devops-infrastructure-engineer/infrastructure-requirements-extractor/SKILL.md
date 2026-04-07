---
name: infrastructure-requirements-extractor
description: >
  This skill extracts infrastructure requirements from product and engineering
  specifications. Use when asked to determine infrastructure needs for a new
  feature, estimate resource requirements, or translate product specs into infra
  work. Also consider when architecture decisions are being made without infra
  input. Suggest when the user is designing a system without infrastructure
  planning.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../infrastructure-scaling-executor/SKILL.md
  - ../production-readiness-reviewer/SKILL.md
---

# infrastructure-requirements-extractor

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Extracts infrastructure requirements from product and engineering specifications, translating feature needs into compute, storage, networking, and operational requirements.

## When to Use

- When a new product feature or service is being designed and infrastructure needs must be scoped before development begins.
- When engineering specifications reference performance, availability, or data requirements that imply infrastructure changes.
- When planning a capacity review and need to aggregate upcoming infrastructure demands across multiple initiatives.

## Workflow

1. **Specification Review**: Read product requirements, engineering design documents, and architecture proposals. Identify explicit and implicit infrastructure needs (traffic estimates, data volumes, latency requirements, availability targets). Deliverable: annotated specification with infrastructure call-outs.
2. **Requirement Categorization**: Categorize extracted requirements into compute, storage, networking, security, monitoring, and compliance domains. Quantify where possible (e.g., estimated QPS, storage growth rate, retention period). Deliverable: categorized requirements matrix.
3. **Dependency Mapping**: Identify dependencies on existing infrastructure (shared databases, message queues, CDN, third-party APIs) and new infrastructure that must be provisioned. Deliverable: dependency map with new vs. existing classification.
4. **Cost Estimation**: Estimate the cost impact of required infrastructure using cloud provider pricing. Provide options at different performance tiers. Deliverable: cost estimate with tier options.
5. **Requirements Document**: Compile findings into a structured requirements document for infrastructure planning and provisioning. Flag any requirements that conflict with existing constraints. Deliverable: infrastructure requirements document.

## Anti-Patterns

- **Extracting requirements in isolation**: Deriving infrastructure needs without consulting the engineering team building the feature. *Why*: specifications often omit implicit assumptions about caching, batching, or traffic patterns that dramatically change infrastructure needs.
- **Over-provisioning by default**: Treating every requirement as peak-load and provisioning accordingly. *Why*: premature over-provisioning wastes budget and delays delivery; auto-scaling and right-sizing are more cost-effective approaches.
- **Ignoring operational requirements**: Focusing only on compute and storage while missing monitoring, logging, backup, and disaster recovery needs. *Why*: operational gaps cause outages that are more expensive than the infrastructure they would have required.

## Output

**On success**: Produces an infrastructure requirements document with categorized needs, dependency map, and cost estimates. Delivered to the infrastructure team and project stakeholders.

**On failure**: Report which specifications were incomplete or ambiguous, what assumptions were made, and what additional input is needed from product or engineering. Escalate if the project timeline is at risk.

## Related Skills

- [`infrastructure-scaling-executor`](../infrastructure-scaling-executor/SKILL.md) -- Extracted requirements inform the scaling executor on what to provision.
- [`production-readiness-reviewer`](../production-readiness-reviewer/SKILL.md) -- Requirements extraction feeds into the production readiness checklist.
