# Risk Assessment Framework

Reference framework for identifying, assessing, rating, and tracking security and compliance risks.

## Risk Rating Methodology

### Likelihood Scale

| Rating | Score | Definition | Frequency Indicator |
|--------|-------|-----------|-------------------|
| Almost Certain | 5 | Expected to occur in most circumstances | Multiple times per year |
| Likely | 4 | Will probably occur in most circumstances | Once per year |
| Possible | 3 | Could occur at some time | Once every 2-3 years |
| Unlikely | 2 | Could occur but not expected | Once every 5-10 years |
| Rare | 1 | May occur only in exceptional circumstances | Less than once per decade |

### Impact Scale

| Rating | Score | Financial | Operational | Reputational | Regulatory |
|--------|-------|-----------|-------------|-------------|-----------|
| Critical | 5 | >$1M loss | Service outage >24 hours | National media coverage | Regulatory action, licence revocation |
| Major | 4 | $250K-$1M | Service outage 4-24 hours | Industry press coverage | Formal regulatory investigation |
| Moderate | 3 | $50K-$250K | Service degradation <4 hours | Customer complaints, social media | Regulatory inquiry |
| Minor | 2 | $10K-$50K | Minor disruption, workaround available | Limited customer awareness | Regulatory correspondence |
| Insignificant | 1 | <$10K | No operational impact | No external awareness | No regulatory attention |

### Risk Rating Matrix

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---------|---------|---------|---------|---------|
| **Likelihood 5** | 5 (Medium) | 10 (High) | 15 (High) | 20 (Critical) | 25 (Critical) |
| **Likelihood 4** | 4 (Low) | 8 (Medium) | 12 (High) | 16 (High) | 20 (Critical) |
| **Likelihood 3** | 3 (Low) | 6 (Medium) | 9 (Medium) | 12 (High) | 15 (High) |
| **Likelihood 2** | 2 (Low) | 4 (Low) | 6 (Medium) | 8 (Medium) | 10 (High) |
| **Likelihood 1** | 1 (Low) | 2 (Low) | 3 (Low) | 4 (Low) | 5 (Medium) |

### Risk Appetite Thresholds

| Risk Level | Score Range | Treatment |
|-----------|-----------|----------|
| Critical | 20-25 | Immediate mitigation required; executive escalation within 24 hours |
| High | 10-16 | Mitigation plan required within 30 days; CISO review |
| Medium | 5-9 | Mitigation planned for next quarter; tracked in register |
| Low | 1-4 | Accept or monitor; document acceptance rationale |

## Risk Categories

| Category | Description | Common Risks |
|----------|-------------|-------------|
| Technical | Infrastructure, application, and data security | Unpatched vulnerabilities, misconfigurations, data exposure |
| Operational | Process and people risks | Key person dependency, process failure, human error |
| Compliance | Regulatory and contractual | GDPR non-compliance, SOC 2 exceptions, contractual breach |
| Third-Party | Vendor and supply chain | Vendor breach, sub-processor non-compliance, SaaS outage |
| Strategic | Business model and market | Regulatory change, market shift affecting compliance requirements |

## Risk Register Entry Template

| Field | Description |
|-------|-------------|
| Risk ID | Unique identifier (e.g., RISK-2026-001) |
| Title | Short descriptive title |
| Category | Technical / Operational / Compliance / Third-Party / Strategic |
| Description | Detailed threat scenario: threat actor, vulnerability, impact |
| Affected Assets | Systems, data, or processes at risk |
| Existing Controls | Current mitigations in place |
| Inherent Risk | Likelihood x Impact before controls |
| Residual Risk | Likelihood x Impact after existing controls |
| Treatment | Mitigate / Accept / Transfer / Avoid |
| Mitigation Plan | Specific actions to reduce risk (if mitigate) |
| Owner | Person accountable for risk management |
| Review Date | Next scheduled review |
| Status | Open / In Mitigation / Accepted / Closed |

## Quarterly Review Process

1. **Preparation**: Export current register, compile new risk inputs (incidents, audit findings, threat intel, vulnerability scans)
2. **New risk assessment**: Rate and add new risks identified since last review
3. **Re-rating**: Re-assess existing risks for changed conditions (new controls, incidents, threat landscape changes)
4. **Mitigation progress**: Review status of open mitigation actions
5. **Risk acceptance review**: Verify accepted risks remain within appetite and acceptance rationale still valid
6. **Closure**: Close fully mitigated risks with evidence of control effectiveness
7. **Reporting**: Produce risk summary for executive leadership with trends and recommendations
