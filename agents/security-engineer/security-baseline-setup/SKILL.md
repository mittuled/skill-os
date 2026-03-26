---
name: security-baseline-setup
description: >
  This skill establishes the security baseline configuration for all systems at
  project inception. Use when asked to set up security defaults, harden a new
  environment, or configure initial security controls. Also consider when a new
  project starts without security foundations. Suggest when the user provisions
  infrastructure without hardening.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../security-architecture-reviewer/SKILL.md
  - ../continuous-security-monitoring/SKILL.md
---

# security-baseline-setup

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Establishes the security baseline configuration for all systems at project inception, codifying hardening standards, access controls, and encryption defaults.

## When to Use

- When a new project or environment is being provisioned and requires security foundations.
- When an existing environment lacks documented security baselines and needs retroactive hardening.
- When migrating to a new cloud provider or infrastructure platform that requires baseline configuration.

## Workflow

1. **Baseline Standard Selection**: Select applicable hardening benchmarks (CIS Benchmarks for the target OS/cloud, NIST 800-53 controls, OWASP ASVS for applications). Deliverable: baseline standard selection document with rationale.
2. **Access Control Configuration**: Configure IAM policies enforcing least-privilege, enable MFA for all human accounts, set up service account credential rotation, and define RBAC roles. Deliverable: IAM configuration with role definitions and access review schedule.
3. **Encryption Defaults**: Enable encryption at rest (AES-256) for all data stores, enforce TLS 1.2+ for all in-transit communication, configure certificate management and rotation. Deliverable: encryption configuration with key management procedures.
4. **Network Hardening**: Configure network segmentation, firewall rules (default-deny), VPC peering policies, and disable unnecessary ports and protocols. Deliverable: network security configuration with rule documentation.
5. **Logging and Audit Trail**: Enable audit logging on all services (cloud audit trails, database query logs, application access logs) with tamper-proof storage. Deliverable: logging configuration with retention policies.
6. **Baseline Validation**: Run automated compliance scans (Prowler, ScoutSuite, cloud-native security tools) to verify the baseline is correctly applied. Deliverable: baseline compliance scan report with remediation for any drift.

## Anti-Patterns

- **Default-allow configurations**: Leaving cloud security groups, IAM policies, or network rules in their permissive default state. *Why*: default-allow policies grant attackers broad access from the moment they gain any foothold.
- **Manual baseline application**: Applying security configurations manually without infrastructure-as-code. *Why*: manual configurations drift silently, creating inconsistency across environments that becomes invisible until exploited.
- **One-time setup without drift detection**: Establishing the baseline once without automated drift detection. *Why*: configuration changes by other teams gradually weaken security posture without anyone noticing.

## Output

**On success**: Produces a security baseline package containing IAM configuration, encryption defaults, network hardening rules, logging setup, and a compliance scan report confirming correct application. Delivered as infrastructure-as-code and documentation.

**On failure**: Report which baseline controls could not be applied (e.g., platform limitations, conflicting policies), what partial hardening was achieved, and recommended workarounds.

## Related Skills

- [`security-architecture-reviewer`](../security-architecture-reviewer/SKILL.md) -- Reviews the architecture that the baseline secures.
- [`continuous-security-monitoring`](../continuous-security-monitoring/SKILL.md) -- Monitors for drift from the established baseline.
