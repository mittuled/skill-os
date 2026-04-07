# Scoring Rubric: Vendor Risk Assessor

Evaluates vendor risk exposure across financial stability, security posture, operational resilience, compliance standing, and concentration risk.

## Criteria

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Financial Stability | 25% | 0-10 | Vendor's financial health: revenue trends, profitability, debt ratios, and funding runway |
| Security Posture | 25% | 0-10 | Maturity of vendor's security controls: certifications, incident history, vulnerability management |
| Operational Resilience | 20% | 0-10 | Business continuity capabilities: disaster recovery, SLA track record, redundancy |
| Compliance Standing | 15% | 0-10 | Regulatory compliance: certifications held, audit findings, data handling practices |
| Concentration Risk | 15% | 0-10 | Dependency exposure: single-source risk, geographic concentration, substitutability |
| **Total** | **100%** | | |

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Financially sound; mature security programme; multi-region resilience; full compliance; low concentration risk | Approve vendor with standard monitoring cadence |
| A | 8.0 – 8.9 | Strong | Stable finances; SOC 2 Type II current; tested DR plan; primary certifications held; alternatives available | Approve with annual risk re-assessment |
| B | 7.0 – 7.9 | Good | Adequate financial health; security programme with minor gaps; DR plan exists but untested; moderate concentration | Approve with enhanced monitoring and contractual risk mitigations |
| C | 5.0 – 6.9 | Adequate | Flat revenue or moderate debt; SOC 2 Type I only; SLA misses in past year; limited alternatives | Approve only with risk acceptance sign-off from business owner |
| D | 3.0 – 4.9 | Weak | Declining financials; material security gaps; no DR plan; missing certifications; deep vendor lock-in | Reject or approve only with executive risk acceptance and exit plan |
| F | 0.0 – 2.9 | Failing | Bankruptcy risk; known breaches; no resilience; regulatory violations; sole source with no migration path | Reject vendor; do not onboard or initiate immediate transition |

## Signal Tables

### Financial Stability
| Score | Evidence |
|-------|----------|
| 9-10 | Profitable with growing revenue, strong balance sheet, investment-grade credit rating or well-funded with 24+ months runway |
| 7-8 | Stable revenue, manageable debt, no recent funding concerns, 12-24 months runway |
| 5-6 | Flat or slightly declining revenue, moderate debt, recent cost-cutting measures |
| 3-4 | Declining revenue, high debt-to-equity, recent layoffs or restructuring, under 6 months runway |
| 1-2 | Operating at significant loss, creditor actions, bankruptcy risk, or unable to provide financial statements |

### Security Posture
| Score | Evidence |
|-------|----------|
| 9-10 | SOC 2 Type II current, ISO 27001 certified, no breaches in 3+ years, mature vulnerability management with SLAs met |
| 7-8 | SOC 2 Type II current, no major breaches in 2 years, documented security program with regular pen tests |
| 5-6 | SOC 2 Type I only, minor security incidents resolved, security program exists but gaps in coverage |
| 3-4 | No SOC 2, security questionnaire reveals material gaps, incident response plan is untested |
| 1-2 | Refuses to share security documentation, known unpatched vulnerabilities, history of data breaches |

### Operational Resilience
| Score | Evidence |
|-------|----------|
| 9-10 | Multi-region redundancy, documented and tested DR plan, 99.99%+ uptime track record, RTO/RPO under 1 hour |
| 7-8 | DR plan documented and tested annually, 99.9%+ uptime, RTO under 4 hours |
| 5-6 | DR plan exists but not recently tested, 99.5%+ uptime, some SLA misses in past year |
| 3-4 | No documented DR plan, multiple SLA breaches, single point of failure in infrastructure |
| 1-2 | No disaster recovery capability, frequent outages, no SLA commitments or consistent SLA violations |

### Compliance Standing
| Score | Evidence |
|-------|----------|
| 9-10 | Multiple relevant certifications current, clean audit history, proactive compliance with emerging regulations |
| 7-8 | Primary certifications current, minor audit findings resolved, compliant with applicable regulations |
| 5-6 | Some certifications in progress, audit findings pending remediation, basic regulatory compliance |
| 3-4 | Key certifications missing, material audit findings unresolved, regulatory gaps identified |
| 1-2 | No relevant certifications, regulatory violations on record, refuses to undergo audits |

### Concentration Risk
| Score | Evidence |
|-------|----------|
| 9-10 | Multiple qualified alternatives exist, vendor handles <10% of critical operations, easy migration path |
| 7-8 | Alternatives available, vendor handles moderate scope, migration feasible within 3 months |
| 5-6 | Limited alternatives, vendor handles significant scope, migration would take 3-6 months |
| 3-4 | Few alternatives, vendor is deeply embedded, migration would take 6-12 months and carry risk |
| 1-2 | Sole source with no viable alternatives, vendor lock-in via proprietary formats, migration would be 12+ months |
