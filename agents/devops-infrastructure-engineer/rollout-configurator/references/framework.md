# Framework: rollout-configurator

Defines rollout strategy selection, stage parameter standards, and success criteria baselines for progressive deployments.

## Risk Classification Matrix

Classify each deployment before selecting parameters:

| Risk Factor | Low (1 pt) | Medium (2 pts) | High (3 pts) |
|-------------|-----------|----------------|-------------|
| Services affected | 1 internal | 1 external-facing | Multiple services |
| User blast radius | < 1% of users | 1–20% of users | > 20% of users |
| Reversibility | Code-only, instant rollback | Config change, fast rollback | Schema/data migration, complex rollback |
| Change size | < 100 lines, 1 component | 100–500 lines, 1–3 components | > 500 lines or cross-cutting |

**Total score**: 4–6 = Low Risk, 7–9 = Medium Risk, 10–12 = High Risk

## Rollout Parameter Standards by Risk Level

| Parameter | Low Risk | Medium Risk | High Risk |
|-----------|---------|-------------|-----------|
| Strategy | Rolling update or blue-green | Canary | Canary with manual promotion gates |
| Initial canary % | 10% | 5% | 1% |
| Stage progression | 10% → 100% | 5% → 25% → 50% → 100% | 1% → 5% → 25% → 50% → 100% |
| Bake time per stage | 5 minutes | 15 minutes | 30 minutes |
| Promotion gate | Automated (metrics-based) | Automated with alert | Manual approval at 25% and beyond |
| Rollback trigger | Automated | Automated | Automated (immediate at any stage) |

## Success Criteria Baselines

Before defining success thresholds, collect the 30-day baseline for each metric:

| Metric | Measurement Method | Typical Threshold |
|--------|--------------------|-------------------|
| HTTP error rate | (5xx responses / total requests) × 100 | Canary error rate ≤ baseline + 0.1% |
| p99 request latency | 99th percentile response time | Canary p99 ≤ baseline p99 × 1.1 |
| Throughput | Requests per second | Canary RPS within ±20% of expected |
| Crash rate | Application exceptions / minute | Canary crash rate ≤ baseline |
| Business metric | Conversion rate, checkout success, message delivery | Canary metric ≥ baseline × 0.99 |

**Warning**: Never define success criteria before establishing the baseline. If the current error rate is 0.08%, a threshold of "< 0.1%" provides only 0.02% detection headroom — essentially no signal.

## Tooling Options

| Rollout Controller | Best For | Configuration Mechanism |
|-------------------|---------|------------------------|
| Argo Rollouts | Kubernetes services with Prometheus/Datadog metrics | `Rollout` CRD with `analysis` templates |
| Flagger | GitOps-driven Kubernetes canaries | `Canary` CRD with metric templates |
| Spinnaker | Multi-cloud or VM-based deployments | Pipeline YAML with canary analysis stage |
| AWS CodeDeploy | EC2 or Lambda deployments | `appspec.yml` with lifecycle hooks |
| Custom (weighted ALB) | Simple blue-green on AWS | ALB target group weights via AWS CLI/Terraform |

## Monitoring Integration Requirements

Rollout monitoring must provide:

1. **Canary vs. baseline comparison view** — side-by-side graphs for the key metrics during each stage
2. **SLO burn rate indicator** — tracks whether the error budget is being consumed faster during the canary
3. **Automated analysis webhook** — rollout controller polls the monitoring API at the end of each bake window
4. **Alert suppression during promotion** — suppress "deployment in progress" alert noise while metrics are expected to be in flux
