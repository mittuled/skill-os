# Framework: environment-parity-planner

Defines parity dimensions, intentional variance rules, and drift detection standards for multi-environment infrastructure.

## Parity Dimensions

| Dimension | Must Be Identical | May Vary with Justification | Common Intentional Differences |
|-----------|------------------|-----------------------------|-------------------------------|
| Infrastructure configuration | IaC templates (same modules, same versions) | Variable values (instance sizes, replica counts) | Dev: t3.medium, Prod: m5.4xlarge |
| Runtime versions | OS version, language runtime, container base image | None — runtime drift is always unintentional | — |
| Application configuration | Config key names and types | Config values (credentials, endpoints, feature flags) | Dev uses localhost DB, Prod uses RDS |
| Network topology | Subnet structure, security group rules (names and rules) | CIDR ranges | Dev uses /24, Prod uses /20 |
| Security controls | TLS version, encryption at rest, IAM role names | Key ARNs, certificate ARNs | — |
| Monitoring and logging | Log schema, metric names, alert rule names | Thresholds and routing (Prod pages, Dev notifies) | Prod: PagerDuty, Dev: Slack |
| Dependencies | Same versions of internal service dependencies | None — dependency drift is always a risk | — |

## Environment Tier Model

| Environment | Purpose | Parity Target | Scale Factor |
|-------------|---------|---------------|-------------|
| development | Local or shared dev exploration | Config-identical, resource-reduced | 0.1× (single replicas, small instances) |
| staging | Pre-production validation, load testing | Production-identical configuration | 0.3–0.5× (realistic but cost-managed) |
| production | Serving users | Reference environment | 1.0× |
| canary/shadow | Progressive rollout or traffic mirroring | Production-identical | Proportional to canary % |

## Drift Classification

| Drift Type | Risk Level | Remediation Priority | Detection Method |
|------------|-----------|---------------------|-----------------|
| Runtime version difference | Critical | Immediate | `terraform plan` diff, container image digest comparison |
| Security group rule difference | High | Within 24 hours | Prowler, cloud config audit |
| IaC module version difference | High | Within 48 hours | `terraform providers lock` diff |
| Instance size difference | Low | Next sprint (if intentional) | Cost explorer + IaC comparison |
| Feature flag state difference | Medium | Within 1 week | Feature flag platform audit log |
| Config key missing in one env | High | Immediate | Environment variable audit |

## IaC Shared-Template Pattern

Structure Terraform or Pulumi to enforce parity through shared modules:

```
infrastructure/
├── modules/
│   ├── web-service/        # Shared module (identical across envs)
│   ├── database/           # Shared module
│   └── monitoring/         # Shared module
├── environments/
│   ├── dev/
│   │   └── main.tf         # Calls shared modules with dev vars
│   ├── staging/
│   │   └── main.tf         # Calls shared modules with staging vars
│   └── production/
│       └── main.tf         # Calls shared modules with prod vars
└── variables/
    ├── dev.tfvars
    ├── staging.tfvars
    └── production.tfvars
```

Environment-specific differences belong **only** in `.tfvars` files. Any difference in module code is a parity violation.

## Drift Detection Cadence

| Frequency | Scope | Tool | Alert Destination |
|-----------|-------|------|------------------|
| On every PR merge | Changed modules | `terraform plan` in CI | PR status check |
| Daily | Full environment comparison | Driftctl or Terragrunt plan | Slack #infra-drift |
| Weekly | Security configuration | Prowler or ScoutSuite | Security team email |
| On every deployment | Application config keys | Custom script comparing env var keys | Deployment gate |
