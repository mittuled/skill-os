# Infrastructure Requirements Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | infrastructure-requirements-extractor |
| Project | [Project or feature name] |
| Source Specs | [Links to PRD, design doc, architecture proposal] |

## Executive Summary

[2-3 sentences covering the top infrastructure requirements and any blocking constraints.
GUIDANCE: Lead with the most significant infrastructure decision — e.g., "This feature requires a dedicated Postgres read replica due to 500 QPS read load and GDPR data residency. Three new infrastructure components are required before launch; one conflicts with the existing shared cache capacity."]

## Compute Requirements

[List all compute requirements extracted from the specification.

GUIDANCE:
- Good: "API service: 4 vCPU / 8 GB RAM × 3 instances minimum, auto-scale to 12 at 70% CPU. Estimated peak QPS: 2,400 based on 80K DAU × 3 req/session ÷ 8 active hours × 3x peak multiplier."
- Bad: "Needs sufficient compute to handle the load."
- Format: Table with columns: Component, Min Spec, Max Spec (auto-scale), Trigger Metric, Basis for Estimate]

| Component | Min Spec | Max Spec | Scale Trigger | Estimate Basis |
|-----------|----------|----------|---------------|----------------|
| [Service name] | [vCPU/RAM] | [vCPU/RAM] | [CPU/memory %] | [Calculation or source] |

## Storage Requirements

[List all storage requirements with quantified projections.

GUIDANCE:
- Good: "User media: 500 GB initial, 2 TB at 12 months (50K uploads/month × 400 KB avg). S3 Standard with 90-day lifecycle to Glacier. GDPR requires EU-West-1 region only."
- Bad: "Store user files in object storage."
- Format: Table with columns: Store Type, Initial Size, 12-Month Projection, Access Pattern, Retention, Compliance Constraint]

| Store | Initial Size | 12-Month Projection | Access Pattern | Retention | Compliance |
|-------|-------------|---------------------|----------------|-----------|------------|
| [Store name] | [GB/TB] | [GB/TB] | [Read/write ratio] | [Days/years] | [None/GDPR/HIPAA] |

## Networking Requirements

[Describe bandwidth, latency, availability zone, and CDN requirements.

GUIDANCE:
- Good: "Payment service requires < 150ms p99 RTT to Stripe API. Deploy in us-east-1 closest to Stripe. CDN required for static assets — estimated 10 TB/month egress."
- Bad: "Low latency required."
- Format: Bullet list with quantified targets per service boundary]

## Security and Compliance Requirements

[List security infrastructure requirements derived from data classification and regulatory scope.

GUIDANCE:
- Good: "PII stored in user service. GDPR applies: encryption at rest (AES-256), EU data residency, 30-day access log retention, DPA required with RDS instance."
- Bad: "Standard security controls required."
- Format: Table mapping regulation to specific infrastructure control required]

| Regulation | Applicable Data | Required Infrastructure Control | Evidence Artifact |
|------------|----------------|----------------------------------|-------------------|
| [GDPR/HIPAA/PCI] | [Data type] | [Specific control] | [Log/config/report] |

## Dependency Map

[Map all infrastructure dependencies: what exists, what is new, and who owns what.

GUIDANCE:
- Good: "Depends on shared Postgres cluster (owned: platform-eng, current capacity headroom: 20%). Requires 2 new dedicated Redis nodes (owned: this service). Third-party: Stripe webhook delivery — requires inbound allowlist on port 443."
- Bad: "Depends on existing infrastructure."
- Format: Table with columns: Dependency, Type, Owner, Current Status, Action Required]

| Dependency | Type | Owner | Status | Action Required |
|------------|------|-------|--------|-----------------|
| [Name] | [Shared existing / New owned / Third-party] | [Team] | [Active / Needs provisioning] | [None / Request capacity / Provision] |

## Cost Estimate

[Provide tier-based cost estimates with monthly projections.

GUIDANCE:
- Good: "Minimum viable: $1,200/month (3 t3.medium + RDS db.t3.medium + 500 GB S3). Recommended: $2,800/month (3 c5.xlarge + RDS db.r5.large Multi-AZ + 2 TB S3 with CDN). High-availability: $6,500/month adds cross-region replication."
- Bad: "Infrastructure costs will be approximately $2,000/month."
- Format: Table with line-item breakdown per tier]

| Line Item | Minimum Viable | Recommended | High-Availability |
|-----------|---------------|-------------|------------------|
| Compute | [$X/month] | [$X/month] | [$X/month] |
| Storage | [$X/month] | [$X/month] | [$X/month] |
| Networking | [$X/month] | [$X/month] | [$X/month] |
| Monitoring | [$X/month] | [$X/month] | [$X/month] |
| **Total** | **[$X/month]** | **[$X/month]** | **[$X/month]** |

## Conflicts and Constraints

[Identify any requirements that conflict with existing infrastructure or have unresolved dependencies.

GUIDANCE:
- Good: "CONFLICT: Feature requires Postgres 15 with logical replication. Current shared cluster is Postgres 13. Options: upgrade shared cluster (risk to other services) or provision dedicated instance (cost: +$400/month)."
- Bad: "Some database changes may be needed."
- Format: Bullet list with CONFLICT / CONSTRAINT / ASSUMPTION tags]

## Recommendations

[Prioritized list of infrastructure actions required before and after launch.

GUIDANCE: Each recommendation should specify the P1/P2/P3 priority, owner, and deadline relative to the launch date.]

- **P1 — [Action]**: [Specific infrastructure task, owner, deadline, cost impact]
- **P2 — [Action]**: [Specific infrastructure task, owner, deadline, cost impact]
- **P3 — [Action]**: [Specific infrastructure task, owner, deadline, cost impact]

## Appendices

### A. Methodology

[How requirements were derived: which specifications were reviewed, estimation formulas used, assumptions made where specifications were incomplete.]

### B. Supporting Calculations

[Raw calculations for QPS estimates, storage projections, and bandwidth estimates.]
