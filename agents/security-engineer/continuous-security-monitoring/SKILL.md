---
name: continuous-security-monitoring
description: >
  This skill operates ongoing security monitoring including SIEM correlation,
  vulnerability scanning, and real-time alerting. Use when asked to set up security
  monitoring, configure SIEM rules, or investigate security alerts. Also consider
  when a new service deploys without security observability. Suggest when the user
  launches infrastructure without detection coverage.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../security-baseline-setup/SKILL.md
  - ../threat-modelling/SKILL.md
---

# continuous-security-monitoring

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Operates ongoing security monitoring including SIEM event correlation, vulnerability scanning, intrusion detection, and real-time alerting across production infrastructure.

## When to Use

- When a new service or infrastructure component deploys to production and requires security observability.
- When security alerts need triage, correlation, or escalation.
- When a compliance framework mandates continuous monitoring controls (e.g., SOC 2 CC7.2, NIST 800-53 SI-4).

## Workflow

1. **Asset Inventory Sync**: Ensure the monitoring scope reflects current production assets including hosts, containers, APIs, databases, and third-party integrations. Deliverable: updated asset inventory mapped to monitoring coverage.
2. **Log Source Onboarding**: Configure log forwarding from application logs, cloud audit trails (CloudTrail, GCP Audit Logs), network flow logs, and authentication systems to the SIEM (Splunk, Sentinel, Elastic Security). Deliverable: log source onboarding checklist with ingestion verification.
3. **Detection Rule Engineering**: Author correlation rules and detection logic for the threat scenarios identified in the threat model: brute-force attempts, privilege escalation, lateral movement, data exfiltration indicators, and anomalous API access patterns. Use MITRE ATT&CK technique IDs for classification. Deliverable: detection rule library mapped to ATT&CK techniques.
4. **Vulnerability Scanning Configuration**: Schedule recurring vulnerability scans (Nessus, Qualys, Trivy for containers) against all production assets. Define severity thresholds and SLA windows for remediation. Deliverable: scanning schedule with remediation SLAs.
5. **Alert Triage Playbook**: Define triage procedures for each alert category: initial assessment, enrichment queries, escalation criteria, and containment actions. Deliverable: alert triage playbook with decision trees.
6. **Dashboard and Reporting**: Build security dashboards showing alert volume trends, mean time to detect (MTTD), mean time to respond (MTTR), vulnerability aging, and coverage gaps. Deliverable: security monitoring dashboard with automated weekly reports.
7. **Tuning Cycle**: Review false positive rates weekly. Suppress noisy rules, refine thresholds, and add context-based exceptions. Deliverable: tuning log with before/after false positive rates.

## Anti-Patterns

- **Alert without context**: Firing alerts that contain only a log line without enrichment (user identity, asset criticality, historical baseline). *Why*: analysts waste triage time reconstructing context that the detection rule could have included.
- **Deploy and forget**: Setting up monitoring once and never tuning detection rules. *Why*: attacker techniques evolve and infrastructure changes; untuned rules accumulate false positives until the team ignores all alerts.
- **Coverage gaps on ephemeral infrastructure**: Excluding containers, serverless functions, or auto-scaled instances from monitoring. *Why*: attackers target unmonitored ephemeral infrastructure precisely because it lacks detection.

## Output

**On success**: Produces a continuous security monitoring system comprising log source integrations, detection rule library (ATT&CK-mapped), vulnerability scanning schedule, alert triage playbooks, security dashboards, and a tuning cadence. Delivered as operational configuration and documentation.

**On failure**: Report which monitoring dimension could not be established (e.g., log source access denied, SIEM capacity limits), what partial coverage exists, and recommended steps to close gaps.

## Related Skills

- [`security-baseline-setup`](../security-baseline-setup/SKILL.md) -- Establishes the baseline configuration that monitoring validates against.
- [`threat-modelling`](../threat-modelling/SKILL.md) -- Identifies the threat scenarios that detection rules must cover.
