# Checklist: Security Baseline Setup

Comprehensive hardening checklist aligned with CIS Benchmarks, NIST 800-53, and OWASP ASVS for establishing security baselines on new or existing environments.

## How to Use

Work through each section in order. Mark each item `[x]` when verified with evidence. Items marked `[REQUIRED]` are blockers — the baseline is not complete until all required items pass. Items marked `[RECOMMENDED]` are best-practice enhancements.

---

## Section 1: Baseline Standard Selection

- [ ] `[REQUIRED]` Identify applicable CIS Benchmark version for target OS/cloud platform (e.g., CIS AWS Foundations Benchmark v2.0, CIS Ubuntu 22.04 LTS)
- [ ] `[REQUIRED]` Identify applicable NIST 800-53 control families for the environment classification
- [ ] `[RECOMMENDED]` Apply OWASP ASVS Level 2 for application-layer controls
- [ ] `[REQUIRED]` Document baseline standard selection with version numbers and rationale in the baseline record
- [ ] `[REQUIRED]` Get baseline standard selection reviewed and approved by CISO or security lead

---

## Section 2: Access Control and Identity

### IAM Policies

- [ ] `[REQUIRED]` All IAM roles follow least-privilege principle — no wildcard (`*`) actions in production roles
- [ ] `[REQUIRED]` Root/superadmin accounts have no active API keys
- [ ] `[REQUIRED]` All human accounts have individual credentials — no shared accounts
- [ ] `[REQUIRED]` MFA enforced for all human accounts accessing production systems
- [ ] `[REQUIRED]` MFA enforced for all privileged accounts (admin, billing, security)
- [ ] `[RECOMMENDED]` Phishing-resistant MFA (hardware keys, WebAuthn) for admin accounts
- [ ] `[REQUIRED]` RBAC roles defined with documented access scope for each role
- [ ] `[REQUIRED]` Access review scheduled (quarterly minimum) with owner assigned

### Service Accounts

- [ ] `[REQUIRED]` Service accounts have dedicated purpose-specific roles — no shared service accounts across services
- [ ] `[REQUIRED]` Service account credentials stored in a secrets manager (AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager)
- [ ] `[REQUIRED]` Service account credential rotation schedule configured (maximum 90-day rotation)
- [ ] `[RECOMMENDED]` Workload identity federation used instead of long-lived service account keys where platform supports it

---

## Section 3: Encryption Defaults

### Encryption at Rest

- [ ] `[REQUIRED]` Encryption at rest enabled on all databases (AES-256 or platform equivalent)
- [ ] `[REQUIRED]` Encryption at rest enabled on all object storage buckets
- [ ] `[REQUIRED]` Encryption at rest enabled on all block storage volumes
- [ ] `[REQUIRED]` Customer-managed encryption keys (CMEK) configured where regulatory requirement exists
- [ ] `[REQUIRED]` Key management procedure documented with rotation schedule (maximum 365 days)
- [ ] `[RECOMMENDED]` Automatic key rotation enabled in KMS

### Encryption in Transit

- [ ] `[REQUIRED]` TLS 1.2 minimum enforced on all external endpoints
- [ ] `[RECOMMENDED]` TLS 1.3 preferred on all endpoints where clients support it
- [ ] `[REQUIRED]` TLS 1.0 and 1.1 explicitly disabled
- [ ] `[REQUIRED]` Weak cipher suites disabled (RC4, 3DES, export ciphers)
- [ ] `[REQUIRED]` HTTP → HTTPS redirect enforced on all web endpoints
- [ ] `[REQUIRED]` HSTS header configured (min-age: 31536000, includeSubDomains)
- [ ] `[REQUIRED]` Internal service-to-service communication uses TLS or mTLS
- [ ] `[REQUIRED]` Certificate management configured with renewal automation (expiry alert at 30 days)

---

## Section 4: Network Hardening

- [ ] `[REQUIRED]` Default-deny ingress rules on all security groups and firewall policies
- [ ] `[REQUIRED]` Default-deny egress rules with explicit allow-list for outbound traffic
- [ ] `[REQUIRED]` Network segmentation: production, staging, and development in separate VPCs/networks
- [ ] `[REQUIRED]` Database tier accessible only from application tier — no direct internet access
- [ ] `[REQUIRED]` Management ports (SSH 22, RDP 3389) not open to 0.0.0.0/0 — restricted to bastion or VPN CIDR
- [ ] `[REQUIRED]` All unused ports disabled on all compute instances
- [ ] `[RECOMMENDED]` VPC Flow Logs enabled
- [ ] `[RECOMMENDED]` Private endpoints used for cloud service access instead of public internet egress
- [ ] `[RECOMMENDED]` Network ACLs provide secondary defense-in-depth layer

---

## Section 5: Logging and Audit Trail

- [ ] `[REQUIRED]` Cloud audit logs enabled (AWS CloudTrail, GCP Cloud Audit Logs, Azure Activity Logs) in all regions
- [ ] `[REQUIRED]` Database query logging enabled on all production databases
- [ ] `[REQUIRED]` Application access logs capturing: timestamp, user ID, action, resource, source IP, result
- [ ] `[REQUIRED]` Authentication event logging (login, logout, failed attempts, MFA challenges)
- [ ] `[REQUIRED]` Admin and privilege change events logged
- [ ] `[REQUIRED]` Logs shipped to centralized, tamper-proof storage (separate account/project from production)
- [ ] `[REQUIRED]` Log retention meets minimum framework requirement (SOC 2: 1 year; PCI-DSS: 1 year; HIPAA: 6 years)
- [ ] `[REQUIRED]` Log integrity protection enabled (log file validation, immutable storage)
- [ ] `[RECOMMENDED]` Real-time alerting on critical events (root login, IAM policy changes, security group modifications)
- [ ] `[RECOMMENDED]` SIEM integration configured

---

## Section 6: Baseline Validation

- [ ] `[REQUIRED]` Automated compliance scan run using tool appropriate to platform:
  - AWS: Prowler, AWS Security Hub, AWS Config Rules
  - GCP: Security Command Center
  - Azure: Microsoft Defender for Cloud
  - On-premises: OpenSCAP, CIS-CAT
- [ ] `[REQUIRED]` All REQUIRED items in this checklist verified as passing in scan or manual evidence
- [ ] `[REQUIRED]` Drift detection mechanism configured (AWS Config, GCP Organization Policy, Azure Policy)
- [ ] `[REQUIRED]` Baseline compliance scan report stored as evidence artifact
- [ ] `[REQUIRED]` Remediation plan created for any items that could not be applied with owner and deadline
- [ ] `[REQUIRED]` Baseline package delivered as infrastructure-as-code (not manually applied)

---

## Baseline Completion Sign-Off

| Section | Status | Evidence Reference | Reviewer |
|---------|--------|-------------------|---------|
| 1. Standard Selection | [ ] Complete / [ ] Partial / [ ] Not Started | | |
| 2. Access Control | [ ] Complete / [ ] Partial / [ ] Not Started | | |
| 3. Encryption | [ ] Complete / [ ] Partial / [ ] Not Started | | |
| 4. Network Hardening | [ ] Complete / [ ] Partial / [ ] Not Started | | |
| 5. Logging | [ ] Complete / [ ] Partial / [ ] Not Started | | |
| 6. Validation | [ ] Complete / [ ] Partial / [ ] Not Started | | |

**Baseline Status**: `[ ] COMPLETE` `[ ] PARTIAL — see remediation plan` `[ ] FAILED — cannot proceed`

**Security Engineer**: _________________________ Date: _________
