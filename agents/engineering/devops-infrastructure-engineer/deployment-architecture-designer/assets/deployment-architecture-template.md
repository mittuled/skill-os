# Deployment Architecture Design: [Service / System Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Service | [Service name] |
| Cloud Provider | [AWS / GCP / Azure / Multi-cloud] |
| Skill | deployment-architecture-designer |
| Version | [1.0] |
| Status | [Draft / Approved] |

## Architecture Overview

**Deployment pattern**: [Single region / Multi-region active-active / Multi-region active-passive]
**Availability target**: [99.9% / 99.95% / 99.99%]
**RTO target**: [X minutes]
**RPO target**: [X minutes]

### Architecture Diagram (Description)

```
Internet
    │
[WAF + CDN] (Cloudfront / Cloudflare)
    │
[Load Balancer] (ALB / NLB)
    │
    ├── [App Tier: ECS Fargate / GKE / AKS]
    │       ├── [Service A — 3 replicas across 3 AZs]
    │       └── [Service B — 3 replicas across 3 AZs]
    │
    ├── [Cache Tier: ElastiCache Redis cluster — 3 nodes]
    │
    └── [Data Tier]
            ├── [Primary DB: RDS PostgreSQL Multi-AZ]
            └── [Read Replicas: 2 × RDS PostgreSQL]

[Object Storage: S3 with versioning + cross-region replication]
[Secrets: AWS Secrets Manager]
[Monitoring: Datadog / CloudWatch]
```

## Compute Tier

| Component | Type | Size | Count | Auto-scaling | Notes |
|-----------|------|------|-------|-------------|-------|
| [Service A] | [ECS Fargate / EC2 / GKE Pod] | [2 vCPU / 4 GB] | [Min: 3, Max: 20] | [CPU > 70% → scale out] | |
| [Service B] | | | | | |
| [Background workers] | | | | [Queue depth > 100 → scale out] | |

**Availability zones used**: [3 AZs in region X]
**Deployment strategy**: [Rolling update / Blue-green / Canary — ArgoCD Rollout]

## Network Architecture

### VPC Configuration

| Subnet Type | CIDR | AZ | Contains |
|------------|------|----|---------|
| Public | [10.0.1.0/24] | [us-east-1a] | Load balancer, NAT gateway |
| Private (App) | [10.0.10.0/24] | [us-east-1a] | App tier containers |
| Private (Data) | [10.0.20.0/24] | [us-east-1a] | Database, cache |

### Security Groups

| Group | Inbound | Outbound | Attached To |
|-------|---------|---------|------------|
| ALB SG | 80 (HTTP), 443 (HTTPS) from 0.0.0.0/0 | App SG:8080 | Load balancer |
| App SG | ALB SG:8080 | DB SG:5432, Cache SG:6379, 443 | App tier |
| DB SG | App SG:5432 | None | Database |
| Cache SG | App SG:6379 | None | Redis |

## Data Tier

| Component | Type | Size | HA | Backup | Encryption |
|-----------|------|------|----|--------|-----------|
| [Primary DB] | [RDS PostgreSQL 15] | [db.r6g.2xlarge] | Multi-AZ | Daily snapshot + PITR 7 days | AES-256 at rest |
| [Read replica 1] | | [db.r6g.xlarge] | — | — | |
| [Cache] | [ElastiCache Redis 7] | [cache.r6g.large] | Cluster mode (3 shards) | Daily | At rest |

**Failover procedure**: [Automatic Multi-AZ failover — RDS promotes replica in < 60s]
**Failover RTO**: [< 1 minute (automatic) for database; < 30s for cache (cluster mode)]

## Cost Estimate

| Component | Monthly Cost | Notes |
|-----------|-------------|-------|
| Compute (avg) | $[X] | At typical load |
| Database (primary + replicas) | $[X] | |
| Cache | $[X] | |
| Load balancer | $[X] | |
| Data transfer | $[X] | Estimated |
| Other (secrets, monitoring) | $[X] | |
| **Total** | **$[X]/month** | |
| **At peak (3× normal)** | **$[X]/month** | Auto-scaling engaged |

## Disaster Recovery

| Scenario | Impact | Recovery Action | RTO | RPO |
|----------|--------|----------------|-----|-----|
| Single instance failure | None (auto-replaced by ASG/ECS) | Automatic | < 2 min | 0 |
| AZ failure | Degraded capacity | Load balancer routes to healthy AZs | < 5 min | 0 |
| DB primary failure | Write unavailable | RDS Multi-AZ auto-failover | < 2 min | < 30s |
| Region failure | Full outage | Manual failover to DR region | < [X hr] | < [Y min] |

## Open Questions

1. [Design decision still to be made]
2. [Assumption that needs validation before implementation]
