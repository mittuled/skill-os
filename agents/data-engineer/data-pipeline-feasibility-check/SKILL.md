---
name: data-pipeline-feasibility-check
description: >
  This skill assesses whether a proposed data pipeline is feasible given available
  data sources and infrastructure. Use when asked to validate a pipeline idea, check
  source availability, or evaluate infrastructure readiness. Also consider when
  stakeholders propose tight SLAs on untested sources. Suggest when the user is about
  to commit engineering effort to a pipeline without validating assumptions.
department: engineering
agent: data-engineer
version: 1.0.0
complexity: simple
related-skills:
  - ../data-pipeline-designer/SKILL.md
---

# data-pipeline-feasibility-check

## Agent: Data Engineer

L2 data engineer (Nx) responsible for data pipeline design, data warehouse schema, pipeline building, reliability testing, data quality monitoring, and scale planning.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Assesses whether a proposed data pipeline is feasible given available data sources, infrastructure capacity, and timeline constraints.

## When to Use

- When a new pipeline request arrives and source connectivity has not been verified.
- When stakeholders propose freshness SLAs that may exceed infrastructure capabilities.
- When a pipeline depends on third-party APIs with unknown rate limits or reliability.

## Workflow

1. **Source Probe**: Connect to each proposed source system and verify API availability, authentication, rate limits, and data format. Deliverable: source access verification report.
2. **Volume Estimation**: Profile source data to estimate row counts, payload sizes, and growth rates. Deliverable: volume forecast with confidence intervals.
3. **Infrastructure Gap Analysis**: Compare pipeline compute, storage, and network requirements against current capacity. Deliverable: gap analysis with cost estimates for any required provisioning.
4. **Feasibility Verdict**: Synthesize findings into a go/no-go recommendation with conditions and risks. Deliverable: feasibility assessment document.

## Anti-Patterns

- **Assuming API stability**: Treating third-party API schemas and rate limits as fixed without contractual guarantees. *Why*: unannounced API changes cause silent pipeline failures that propagate bad data downstream.
- **Skipping the volume profile**: Estimating data volume from stakeholder guesses instead of sampling. *Why*: order-of-magnitude errors in volume estimates lead to under-provisioned infrastructure and missed SLAs.

## Output

**On success**: Produces a feasibility assessment document with go/no-go verdict, source verification results, volume forecasts, and infrastructure gap analysis. Delivered as a markdown artifact.

**On failure**: Report which feasibility dimension failed (source access, volume, infrastructure), what was tested, and recommended remediation steps.

## Related Skills

- [`data-pipeline-designer`](../data-pipeline-designer/SKILL.md) -- Proceeds with full design once feasibility is confirmed.
