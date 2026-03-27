---
name: infrastructure-load-testing
description: >
  This skill runs load tests against infrastructure to validate performance and
  scale targets. Use when asked to load test a service, validate throughput
  capacity, or stress test infrastructure. Also consider when preparing for a
  launch or traffic spike. Suggest when the user is deploying to production
  without performance validation.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../infrastructure-scaling-executor/SKILL.md
  - ../performance-monitor/SKILL.md
---

# infrastructure-load-testing

## Agent: DevOps / Infrastructure Engineer

L2 DevOps and infrastructure engineer (1x) responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Runs load tests against infrastructure to validate that services meet performance, throughput, and latency targets under expected and peak traffic conditions.

## When to Use

- When a new service or major feature is approaching production deployment and needs performance validation against SLOs.
- When the system is being prepared for an anticipated traffic spike (product launch, marketing campaign, seasonal peak).
- When infrastructure changes (scaling configuration, database migration, CDN switch) need validation under realistic load.

## Workflow

1. **Test Planning**: Define load test scenarios based on production traffic patterns. Specify target throughput (RPS), concurrency levels, ramp-up curves, and duration. Identify SLOs to validate (p50/p95/p99 latency, error rate, throughput). Deliverable: load test plan with scenario definitions.
2. **Environment Preparation**: Provision a test environment that mirrors production topology. Seed test data at realistic volumes. Configure monitoring dashboards to observe system behavior during tests. Deliverable: test environment ready with monitoring.
3. **Test Execution**: Execute load test scenarios using appropriate tooling (k6, Locust, Gatling, or cloud-native tools). Start with baseline tests, then ramp to target load, then push to failure to find the breaking point. Deliverable: raw test results with metrics.
4. **Results Analysis**: Analyze latency distributions, error rates, resource utilization (CPU, memory, I/O, network), and bottleneck identification. Compare results against SLOs. Identify the first resource to saturate. Deliverable: analysis report with bottleneck findings.
5. **Remediation Handoff**: Document findings and recommended actions (scaling changes, code optimizations, caching additions). Hand off actionable items to the relevant engineering teams. Deliverable: remediation recommendations with priority.

## Anti-Patterns

- **Testing in isolation**: Running load tests against a single service without including its dependencies (database, cache, downstream APIs). *Why*: real bottlenecks often appear at dependency boundaries, and isolated tests miss cascading failures.
- **Fixed-rate testing only**: Testing at a single throughput level without ramping to failure. *Why*: knowing the system handles 1,000 RPS is less useful than knowing it breaks at 1,200 RPS; the breaking point informs capacity planning.
- **Ignoring warm-up effects**: Starting measurements immediately without allowing JIT compilation, connection pool warm-up, and cache filling. *Why*: cold-start metrics inflate latency numbers and produce misleading results.

## Output

**On success**: Produces a load test report with scenario results, SLO validation, bottleneck analysis, and remediation recommendations. Delivered to the engineering team and stakeholders.

**On failure**: Report which scenarios could not complete (e.g., test environment instability, tooling errors), partial results collected, and what must be resolved before retesting. Escalate if production deployment is blocked.

## Related Skills

- [`infrastructure-scaling-executor`](../infrastructure-scaling-executor/SKILL.md) -- Load test results inform scaling decisions that the scaling executor implements.
- [`performance-monitor`](../performance-monitor/SKILL.md) -- Performance monitoring validates that load test improvements hold in production.
