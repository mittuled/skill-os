# Framework: Cloud Foundation Setup

Reference framework for establishing a secure, well-structured cloud foundation using IaC principles.

## Account/Project Structure

| Account | Purpose | Access Level |
|---------|---------|-------------|
| Management/Root | Billing, org policies, audit | Admin only (break-glass) |
| Shared Services | DNS, VPN, CI/CD runners, artifact registry | Platform team |
| Production | Production workloads | Deployment pipelines + SRE |
| Staging | Pre-production validation | Engineering teams |
| Development | Developer sandboxes | Individual developers |
| Security/Audit | CloudTrail aggregation, SIEM, security tooling | Security team |

## Networking Foundation

| Component | Standard |
|-----------|----------|
| VPC CIDR | /16 per account, non-overlapping ranges |
| Subnet Strategy | Public + Private + Data subnets per AZ |
| NAT Gateway | One per AZ in production, shared in non-prod |
| DNS | Private hosted zones per account, central resolution |
| Peering | Hub-and-spoke from shared services to each account |
| Flow Logs | Enabled on all VPCs, shipped to security account |

## IAM Principles

1. **Least privilege**: Start with zero permissions, grant only what is needed
2. **Role-based**: Use roles (not users) for all service access
3. **Time-bound**: Temporary credentials via assume-role, no long-lived keys
4. **MFA required**: All human access requires MFA
5. **Service accounts**: Managed identities (IAM roles for EKS pods, workload identity for GKE)

## IaC Standards (Terraform)

```
infrastructure/
├── modules/           # Reusable modules
│   ├── vpc/
│   ├── iam/
│   └── security-baseline/
├── environments/
│   ├── production/
│   ├── staging/
│   └── development/
├── global/            # DNS, IAM, billing
└── backend.tf         # Remote state configuration
```

## Day-One Security Baselines

- [ ] Encryption at rest enabled (default KMS key)
- [ ] Encryption in transit enforced (TLS 1.2+)
- [ ] CloudTrail / audit logging enabled in all accounts
- [ ] Security group defaults: deny-all inbound
- [ ] S3 public access blocked at account level
- [ ] GuardDuty / Security Hub enabled
- [ ] Billing alerts configured at 50%, 80%, 100% of budget
