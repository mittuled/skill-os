---
name: platform-scale-preparation
description: >
  This skill prepares the platform for scale by addressing bottlenecks and single
  points of failure. Use when asked to assess platform scalability, plan for traffic
  growth, or eliminate infrastructure bottlenecks. Also consider when the product
  roadmap includes launches expected to significantly increase load. Suggest when
  the user is launching a high-traffic feature without a platform scale review.
department: engineering
agent: platform-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../platform-roadmap-aligner/SKILL.md
  - ../../../engineering/devops-infrastructure-engineer/infrastructure-scaling-executor/SKILL.md
---

# platform-scale-preparation

## Agent: Platform Engineer

L2 platform engineer (1x) responsible for detecting capability gaps, aligning the platform roadmap, defining golden paths, enabling developer experience, and preparing for platform scale.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Prepares the platform for scale by identifying bottlenecks, eliminating single points of failure, validating capacity plans, and ensuring the infrastructure can handle projected growth without degraded performance.

## When to Use

- When projected traffic growth (organic or launch-driven) will exceed current platform capacity within the planning horizon.
- When production incidents reveal bottlenecks or single points of failure that would worsen at higher scale.
- When a major product launch or partnership is expected to drive a step-change in platform load.

## Workflow

1. **Current State Assessment**: Profile the platform's current capacity across all critical dimensions: compute, storage, network, database throughput, API rate limits, and third-party service quotas. Identify the binding constraint for each service. Deliverable: capacity profile with binding constraints.
2. **Growth Modelling**: Model expected growth using product forecasts, historical trends, and planned launches. Translate user growth into infrastructure load (requests/second, storage growth rate, concurrent connections). Identify when current capacity will be exhausted. Deliverable: growth model with capacity exhaustion timeline.
3. **Bottleneck Identification**: Map the system architecture to find components that do not scale horizontally, have hard limits, or degrade non-linearly under load. Prioritize by proximity to exhaustion and blast radius if they fail. Deliverable: bottleneck inventory with risk ranking.
4. **Scale Plan Design**: For each bottleneck, design a remediation: horizontal scaling, sharding, caching, async processing, or architecture change. Estimate cost, effort, and lead time. Sequence remediations by risk and dependency. Deliverable: scale plan with sequenced remediations.
5. **Validation**: Validate the scale plan through load testing, chaos engineering, or staged rollout. Confirm that each remediation achieves the target capacity. Identify new bottlenecks that emerge at higher scale. Deliverable: validation results with updated capacity profile.
6. **Monitoring and Alerting**: Ensure capacity metrics are monitored with alerts set at thresholds that provide sufficient lead time for intervention. Define runbooks for capacity-related incidents. Deliverable: capacity monitoring dashboard and alert configuration.

## Anti-Patterns

- **Scaling without profiling**: Adding capacity (more instances, bigger machines) without understanding the actual bottleneck. *Why*: throwing resources at a non-binding constraint wastes money; the system remains constrained by the actual bottleneck.
- **Planning for peak only**: Designing for peak load without considering cost at normal load. *Why*: over-provisioned infrastructure burns cash during off-peak hours; auto-scaling and right-sizing must be part of the plan.
- **Ignoring third-party limits**: Scaling internal infrastructure without confirming that third-party APIs, payment processors, and SaaS dependencies can handle the increased load. *Why*: third-party rate limits become the binding constraint at scale; discovering this during a launch is catastrophic.
- **One-time scale review**: Treating scale preparation as a one-time project rather than an ongoing practice. *Why*: growth is continuous; a scale plan that is valid today may be exhausted in months.

## Output

**On success**: Produces a capacity profile, growth model, bottleneck inventory, sequenced scale plan, validation results, and monitoring configuration. Delivered ahead of projected capacity exhaustion.

**On failure**: Report which bottlenecks were identified but not remediated, what the current capacity headroom is, and what the estimated time to exhaustion is. Recommend emergency measures if a launch is imminent.

## Related Skills

- [`platform-roadmap-aligner`](../platform-roadmap-aligner/SKILL.md) -- Scale preparation work must be sequenced within the broader platform roadmap.
- [`infrastructure-scaling-executor`](../../../engineering/devops-infrastructure-engineer/infrastructure-scaling-executor/SKILL.md) -- Executes the infrastructure scaling changes that this skill plans.
