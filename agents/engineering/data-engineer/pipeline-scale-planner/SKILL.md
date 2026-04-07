---
name: pipeline-scale-planner
description: >
  This skill plans pipeline scaling strategies to handle increasing data volumes and
  throughput requirements. Use when asked to capacity-plan a pipeline, forecast
  growth, or design horizontal scaling. Also consider when pipeline run times
  approach SLA limits. Suggest when the user ignores volume growth projections.
department: engineering
agent: data-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../data-pipeline-designer/SKILL.md
  - ../pipeline-reliability-tester/SKILL.md
---

# pipeline-scale-planner

## Agent: Data Engineer

L2 data engineer (Nx) responsible for data pipeline design, data warehouse schema, pipeline building, reliability testing, data quality monitoring, and scale planning.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Plans pipeline scaling strategies to handle increasing data volumes, source proliferation, and throughput requirements while maintaining SLA compliance.

## When to Use

- When pipeline execution time trends upward and approaches the SLA window boundary.
- When business growth projections indicate 3-10x data volume increases within 6-12 months.
- When new source integrations will significantly increase pipeline input volume or complexity.

## Workflow

1. **Current State Profiling**: Measure current pipeline throughput (rows/sec, bytes/sec), resource utilization (CPU, memory, I/O), and execution duration trends. Deliverable: baseline performance profile with trend analysis.
2. **Growth Forecasting**: Project data volume growth using historical trends and business growth plans. Identify the timeline when current capacity will be insufficient. Deliverable: capacity forecast with breach-date projections.
3. **Bottleneck Identification**: Profile the pipeline to identify the scaling bottleneck (e.g., single-threaded extraction, shuffle-heavy transformations, write amplification). Deliverable: bottleneck analysis with flame graphs or execution plan breakdowns.
4. **Scaling Strategy Design**: Design scaling interventions: horizontal partitioning, parallel extraction, incremental processing, materialized views, or infrastructure upgrades. Deliverable: scaling plan with cost-benefit analysis per intervention.
5. **Validation Plan**: Define how to verify the scaling strategy works (load tests, canary deployments, A/B pipeline comparison). Deliverable: validation test plan with success criteria.

## Anti-Patterns

- **Vertical scaling as default**: Always upgrading to bigger machines instead of addressing architectural bottlenecks. *Why*: vertical scaling has hard ceilings and costs grow super-linearly, while architectural fixes (partitioning, incremental processing) provide sustainable scale.
- **Reactive scaling only**: Waiting until SLA breaches occur before planning capacity. *Why*: provisioning infrastructure and re-architecting pipelines takes weeks, during which SLAs remain violated.
- **Ignoring cost efficiency**: Scaling without cost modeling. *Why*: unchecked scaling can 10x infrastructure costs when a targeted optimization (e.g., switching from full reload to CDC) would achieve the same throughput at minimal cost.

## Output

**On success**: Produces a pipeline scaling plan containing the baseline profile, growth forecast, bottleneck analysis, scaling strategy with cost-benefit analysis, and validation test plan. Delivered as a planning document in the project repository.

**On failure**: Report which analysis phase could not be completed (e.g., missing metrics, unclear growth projections), what partial findings exist, and recommended instrumentation to enable complete analysis.

## Related Skills

- [`data-pipeline-designer`](../data-pipeline-designer/SKILL.md) -- May require a redesign if the scaling plan identifies architectural limits.
- [`pipeline-reliability-tester`](../pipeline-reliability-tester/SKILL.md) -- Validates that the scaled pipeline remains reliable under increased load.
