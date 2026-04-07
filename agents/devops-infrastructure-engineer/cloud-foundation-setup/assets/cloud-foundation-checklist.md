# Cloud Foundation Setup Checklist: [Account / Project Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | DevOps / Infrastructure Engineer |
| Cloud Provider | [AWS / GCP / Azure] |
| Account / Project | [Account ID or project name] |
| Skill | cloud-foundation-setup |
| Status | [In Progress / Complete] |

---

## Category 1: Account Structure and Governance

- [ ] Organization root account created; no workloads run in root
- [ ] Separate accounts/projects for: production, staging, development, security/audit
- [ ] Account naming convention documented and applied
- [ ] Billing alerts configured (alert at 80% and 100% of budget)
- [ ] Cost allocation tags policy enforced
- [ ] Service Control Policies (SCPs) applied to prevent dangerous actions in child accounts

---

## Category 2: Identity and Access Management

- [ ] Root account MFA enabled and root account credentials stored securely
- [ ] No root account access keys exist
- [ ] SSO / Identity provider (Okta / Azure AD / Google Workspace) integrated
- [ ] MFA required for all human accounts
- [ ] Break-glass admin account created, credentials stored in secrets manager, access logged
- [ ] IAM password policy enforced: 14+ chars, rotation every 90 days, no reuse
- [ ] Service accounts use IAM roles (not long-lived keys)
- [ ] Permission boundaries applied to limit blast radius of compromised roles

---

## Category 3: Network Foundation

- [ ] VPC created with documented CIDR range (avoid 10.0.0.0/8 overlaps with corp network)
- [ ] Public, private, and data subnets defined across minimum 3 AZs
- [ ] NAT gateway configured (private subnets outbound via NAT, not internet gateway)
- [ ] VPC Flow Logs enabled
- [ ] DNS resolution enabled (Route 53 Resolver or equivalent)
- [ ] Transit Gateway or VPC Peering planned for multi-account connectivity
- [ ] Network ACLs configured as defense-in-depth layer

---

## Category 4: Security Services

- [ ] CloudTrail / Cloud Audit Logs enabled in all regions, logs to central S3/GCS bucket
- [ ] CloudTrail log file integrity validation enabled
- [ ] GuardDuty / Security Command Center / Defender for Cloud enabled
- [ ] AWS Config / GCP Config / Azure Policy enabled and recording all resources
- [ ] Security Hub / Security Command Center findings reviewed
- [ ] Secrets Manager configured; rotation policy enabled
- [ ] AWS Macie / Cloud DLP enabled for PII detection in storage

---

## Category 5: Logging and Monitoring Foundation

- [ ] Centralized log aggregation account/project established
- [ ] Logs from all accounts flowing to central account
- [ ] Log retention policy defined and configured (e.g., 1 year in S3/GCS with lifecycle to Glacier)
- [ ] CloudWatch / Cloud Monitoring baseline alarms configured:
  - [ ] Root account login
  - [ ] IAM policy changes
  - [ ] Security group changes
  - [ ] Multi-region activity from single principal
- [ ] Cost anomaly detection enabled

---

## Category 6: Infrastructure as Code

- [ ] IaC tool selected and configured: [Terraform / Pulumi / CDK]
- [ ] State backend configured: [S3 + DynamoDB lock / GCS / Azure Blob]
- [ ] State bucket is versioned and access-controlled
- [ ] IaC repository created with branch protection rules
- [ ] CI pipeline applies IaC via PR approval workflow (no manual `apply`)
- [ ] Tagging module enforces required tags on all resources

---

## Category 7: Compliance and Data Residency

- [ ] Data residency requirements documented and regions selected accordingly
- [ ] Compliance framework requirements mapped to cloud controls (SOC 2 / PCI / HIPAA)
- [ ] Data classification policy applied to storage resources
- [ ] Backup policy defined and applied to all stateful resources

---

## Open Items

| # | Category | Item | Owner | Due |
|---|----------|------|-------|-----|
| 1 | [Category] | [Specific item] | [Role] | [Date] |

**Foundation sign-off**: DevOps Engineer: [Name] | Date: [YYYY-MM-DD]
