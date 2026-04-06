# Framework: Continuous Security Monitoring

Defines the detection engineering model, MITRE ATT&CK alignment, vulnerability SLA framework, and tuning cadence for continuous security monitoring operations.

## Detection Coverage Model

### MITRE ATT&CK Tactic Coverage Targets

Every production system must have detection coverage for these priority tactics:

| Tactic | Priority | Key Techniques to Detect | Minimum Coverage |
|--------|----------|--------------------------|-----------------|
| Initial Access | P1 | T1190 (Exploit public-facing app), T1078 (Valid accounts) | 100% of internet-facing services |
| Credential Access | P1 | T1110 (Brute force), T1555 (Credentials from stores) | Auth systems and secret stores |
| Privilege Escalation | P1 | T1548 (Abuse elevation control), T1134 (Access token manipulation) | All privileged operations |
| Defense Evasion | P1 | T1070 (Indicator removal), T1562 (Impair defenses) | Log integrity, monitoring health |
| Exfiltration | P1 | T1041 (Exfiltration over C2), T1048 (Exfiltration over alt protocol) | Database egress, bulk export APIs |
| Discovery | P2 | T1046 (Network service scanning), T1087 (Account discovery) | Internal network, admin APIs |
| Lateral Movement | P2 | T1021 (Remote services), T1534 (Internal spearphishing) | Internal service-to-service calls |
| Persistence | P2 | T1136 (Create account), T1078 (Valid accounts) | IAM activity, service accounts |

## Detection Rule Quality Standards

Every detection rule must meet these standards before deployment:

| Standard | Requirement |
|----------|-------------|
| ATT&CK mapping | Each rule maps to ≥ 1 MITRE ATT&CK technique ID |
| True positive rate | False positive rate ≤ 10% measured over first 2 weeks; tune if exceeded |
| Enrichment | Rule fires with: user identity, asset criticality, historical baseline context |
| Triage time | Alert enrichment is sufficient for Level 1 analyst to assess in < 5 minutes |
| Documentation | Rule includes: description, false positive scenarios, triage steps, escalation criteria |

## Vulnerability Remediation SLA Framework

| CVSS Score | Severity | Remediation SLA | Notification |
|------------|----------|----------------|-------------|
| 9.0–10.0 | Critical | 24 hours for temporary mitigation; 7 days for full remediation | Immediate page to security team |
| 7.0–8.9 | High | 7 days temporary mitigation; 30 days full remediation | Same-day ticket, security lead notified |
| 4.0–6.9 | Medium | 90 days full remediation | Sprint backlog ticket |
| 0.1–3.9 | Low | 180 days or next scheduled patching cycle | Backlog, no SLA breach alert |

**Breach escalation**: SLA breaches escalate to VP Engineering with a risk acceptance decision required. Engineering cannot self-extend SLAs without documented risk acceptance.

## Log Source Onboarding Requirements

Every log source must pass these checks before being considered "monitored":

| Check | Requirement |
|-------|-------------|
| Ingestion verified | Logs appear in SIEM within 5 minutes of event |
| Schema normalized | Events parsed to common schema (OCSF, ECS, or custom normalized schema) |
| Retention configured | Retention period configured per compliance requirement (minimum 12 months for PCI/SOC 2) |
| Coverage mapped | Log source mapped to ATT&CK techniques it covers |
| Alert rule deployed | At least 1 detection rule active consuming this source |

## Alert Volume and Tuning Targets

| Metric | Target | Action if Exceeded |
|--------|--------|-------------------|
| False positive rate | < 10% per rule | Tune rule within 1 week |
| Analyst triage time | < 5 min / alert (Level 1) | Add enrichment or suppress known-benign context |
| Alert volume per analyst | < 20 actionable alerts / analyst / day | Suppress low-fidelity rules; add automation for benign patterns |
| Mean time to detect (MTTD) | < 1 hour for P1 threats | Increase detection rule coverage |
| Mean time to respond (MTTR) | < 4 hours for P1 | Improve triage playbooks and automation |

## Monitoring Coverage Health Report Cadence

| Report | Frequency | Audience | Key Metrics |
|--------|-----------|----------|-------------|
| Weekly security digest | Weekly | Security team | Alert volume, MTTD, MTTR, top false positive rules |
| Monthly coverage review | Monthly | Security lead, engineering | ATT&CK coverage gaps, vulnerability aging, SLA compliance |
| Quarterly tuning cycle | Quarterly | Security team | Rule effectiveness metrics, suppression review, new coverage additions |
| Annual monitoring assessment | Annually | CISO, VP Engineering | Full coverage assessment against current threat landscape |
