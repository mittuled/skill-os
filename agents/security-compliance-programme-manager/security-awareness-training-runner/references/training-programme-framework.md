# Security Awareness Training Programme Framework

Reference framework for designing, deploying, and measuring security awareness training and phishing simulation programmes.

## Regulatory Training Requirements

| Regulation | Training Requirement | Frequency | Evidence Needed |
|-----------|---------------------|-----------|----------------|
| SOC 2 (CC1.4) | Security awareness for all employees | Annual minimum | Completion records, training content |
| GDPR (Art. 39) | Data protection awareness | At hire + annual | Completion records, DPO oversight |
| HIPAA (45 CFR 164.530) | Privacy and security training | At hire + periodic | Training logs, content, attestations |
| PCI-DSS (12.6) | Security awareness for cardholder data handlers | At hire + annual | Completion records |
| ISO 27001 (A.7.2.2) | Information security awareness, education, training | Ongoing | Training plan, records |
| State Privacy Laws | Privacy-specific training for data handlers | Varies | Completion records |

## Core Curriculum Modules

### All-Employee Modules

| Module | Topics | Duration | Frequency |
|--------|--------|----------|-----------|
| Security Fundamentals | Password hygiene, MFA, device security, physical security | 30 min | At hire + annual |
| Phishing Recognition | Email phishing, smishing, vishing, social engineering tactics | 20 min | At hire + quarterly reinforcement |
| Data Classification | Data types, handling requirements, labelling, sharing rules | 20 min | At hire + annual |
| Incident Reporting | What to report, how to report, escalation, non-retaliation | 15 min | At hire + annual |
| Acceptable Use | Company systems use, personal devices, remote work, travel | 15 min | At hire + annual |
| Privacy Awareness | GDPR/CCPA basics, data subject rights, consent, privacy by design | 20 min | At hire + annual |

### Role-Specific Modules

| Module | Target Audience | Topics | Frequency |
|--------|----------------|--------|-----------|
| Secure Coding | Engineering | OWASP Top 10, input validation, authentication, secrets management | At hire + annual |
| BEC/Wire Fraud | Finance, executives | Business email compromise, payment verification, impersonation | At hire + semi-annual |
| Customer Data Handling | Customer-facing roles | Data minimization, consent, DSR handling, breach response | At hire + annual |
| Vendor Security | Procurement | Vendor risk assessment, DPA requirements, security questionnaires | Annual |
| Executive Security | C-suite, board | Targeted attacks, travel security, social media risks, board reporting | Semi-annual |

## Phishing Simulation Programme

### Simulation Design

| Difficulty | Techniques | Target Click Rate |
|-----------|-----------|-------------------|
| Easy | Obvious grammar errors, generic sender, urgent language | <5% |
| Medium | Branded template, plausible sender, contextual pretext | <10% |
| Hard | Spoofed internal sender, current event pretext, personalized | <15% |
| Advanced | Multi-stage (email + phone), business process exploitation | <20% |

### Progression Model
1. **Month 1-3**: Easy simulations to establish baseline
2. **Month 4-6**: Medium simulations, targeted training for repeat clickers
3. **Month 7-9**: Hard simulations, introduce role-specific scenarios
4. **Month 10-12**: Advanced simulations, measure year-over-year improvement

### Response to Failure
| Failure Type | Response |
|-------------|----------|
| Click link | Immediate educational landing page explaining the indicators |
| Enter credentials | Educational page + mandatory remedial training within 7 days |
| Repeat failure (3+) | Manager notification + 1:1 security coaching session |
| Report phishing | Positive recognition (gamification, leaderboard) |

## Metrics and Reporting

| Metric | Target | Measurement Frequency |
|--------|--------|----------------------|
| Training completion rate | >95% within 30 days of assignment | Monthly |
| Phishing click rate | <10% (decreasing trend) | Per simulation |
| Phishing report rate | >60% (increasing trend) | Per simulation |
| Credential submission rate | <3% | Per simulation |
| Time to report | <5 minutes median | Per simulation |
| Assessment pass rate | >90% first attempt | Per module |
| Repeat failure rate | <5% of employees | Quarterly |
