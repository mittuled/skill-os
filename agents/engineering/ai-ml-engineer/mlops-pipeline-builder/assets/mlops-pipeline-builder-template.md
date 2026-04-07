# MLOps Pipeline Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [AI/ML Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | mlops-pipeline-builder |
| Model | [Model name and task] |
| Orchestrator | [Kubeflow / Vertex AI / Airflow / Metaflow] |

## Executive Summary

[2-3 sentences describing the pipeline's purpose, the model it serves, and the automation level achieved.
GUIDANCE: Lead with the automation level and key business outcome. Example: "This pipeline automates training, evaluation, and canary deployment for the churn prediction model (Level 2 MLOps). It reduces deployment cycle time from 5 days manual to 4 hours automated and enforces an evaluation gate requiring 1% F1 improvement before promotion."]

## Pipeline DAG Definition

[Diagram or table showing the pipeline stages, their dependencies, and trigger conditions.

GUIDANCE:
- Good: Include exact stage names, tools used per stage, and failure handling behavior
- Bad: "Data → Train → Deploy" without specifying tools, failure modes, or gate conditions
- Format: Mermaid DAG or table]

```
data_validation → training → evaluation_gate → [PROMOTE → model_registry → deployment] / [REJECT → alert]
```

| Stage | Tool / Framework | Input | Output | On Failure |
|-------|-----------------|-------|--------|-----------|
| Data Validation | [TFDV / Great Expectations] | [Raw feature dataset URI] | [Validation report + statistics] | [Halt + alert data-eng] |
| Training | [MLflow + framework] | [Versioned dataset] | [Model artifact + run ID] | [Halt + notify ML team] |
| Evaluation Gate | [Custom eval + MLflow] | [Candidate model + test set] | [Promote / Reject verdict] | [Reject with report] |
| Model Registry | [MLflow Registry / Vertex AI] | [Approved artifact + metadata] | [Registered model version] | [Halt + notify] |
| Deployment | [Seldon / KServe / Vertex AI] | [Registered model version] | [Serving endpoint] | [Rollback + alert] |
| Monitoring | [Prometheus + Grafana] | [Pipeline execution metrics] | [Health dashboard] | [Alert on breach] |

## Data Validation Stage

[Configuration for the data validation checks.

GUIDANCE:
- Good: Specify exact PSI threshold, schema file path, freshness SLA, and null rate per feature
- Bad: "Check data quality before training"]

| Check | Configuration | Gate Threshold | Action on Failure |
|-------|--------------|---------------|-------------------|
| Schema validation | [Schema file: `schemas/training_schema_v2.json`] | Any schema violation | Halt + alert |
| Distribution drift | [PSI against baseline stats] | PSI > 0.20 (large drift) | Halt + alert data team |
| Data freshness | [Max record age] | Records older than [X hours] | Halt + alert |
| Row count | [Expected range: ± 20%] | Outside [min_rows, max_rows] | Halt + alert |

## Evaluation Gate Configuration

[Promotion criteria applied when evaluating the candidate model.

GUIDANCE:
- Good: Numeric thresholds per metric with comparison type (absolute vs. relative to production model)
- Bad: "Model must be good enough to promote"]

| Metric | Type | Threshold | Comparison | Required to Promote |
|--------|------|-----------|-----------|---------------------|
| [F1 score] | Accuracy | [≥ 0.82] | Absolute floor | Yes |
| [F1 vs. production] | Relative improvement | [≥ production - 0.01] | Relative to prod model | Yes |
| [Demographic parity difference] | Fairness | [≤ 0.05] | Absolute ceiling | Yes |
| [p99 inference latency] | Latency | [≤ 200ms] | Absolute ceiling | Yes |

## Deployment Configuration

[Rollout strategy and rollback triggers.

GUIDANCE:
- Good: Specify exact canary percentages, bake time at each step, and the metric threshold that triggers automatic rollback
- Bad: "Deploy the model with a canary"]

| Rollout Step | Traffic % | Bake Time | Auto-Rollback Trigger |
|-------------|-----------|-----------|----------------------|
| Canary | [5%] | [15 minutes] | Error rate > 1% or p99 > latency budget |
| Partial | [25%] | [1 hour] | Same triggers |
| Full | [100%] | [24 hours monitoring] | Same triggers |

## Recommendations

[Prioritized recommendations for pipeline improvements or identified risks.

GUIDANCE: Each recommendation should be specific and actionable.]

- **P1**: [Critical pipeline gap or risk that must be addressed before production use]
- **P2**: [Important enhancement for next iteration]
- **P3**: [Long-term maturity improvement]

## Appendices

### A. Methodology

[Orchestrator platform, pipeline framework, infrastructure requirements, and any decisions made during pipeline design.]

### B. Environment Configuration

[Python/framework versions, container images, GPU/CPU specifications, and secrets management approach for the pipeline.]
