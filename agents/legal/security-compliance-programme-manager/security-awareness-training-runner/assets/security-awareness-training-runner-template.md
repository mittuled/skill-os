# Security Awareness Training Programme

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Approved] |
| Skill | security-awareness-training-runner |
| Programme Year | [YYYY] |
| LMS / Training Platform | [KnowBe4 / Proofpoint / Curricula / Custom LMS] |
| Compliance Drivers | [SOC 2 CC1.4 / GDPR Art. 39 / HIPAA § 164.308 / ISO 27001 A.7.2] |

## Programme Overview

[2-3 sentences describing the programme objectives, audience, and compliance obligations it satisfies.

GUIDANCE: Example: "This programme provides annual security awareness training to all employees and contractors, supplemented by quarterly phishing simulations and role-specific modules for engineering and finance. It satisfies SOC 2 CC1.4 (security awareness training requirement) and GDPR Article 39 (DPO training mandate). Completion is mandatory and tracked for audit evidence."]

**Total audience:** [N] employees + [N] contractors = [N] total
**Mandatory completion deadline:** [Annual: MM/DD] / [New hires: within 14 days of start date]
**Escalation for non-completion:** Manager notification at 7 days overdue; HR escalation at 14 days overdue

---

## Training Needs Matrix

| Requirement | Source | Audience | Topics Required | Module ID |
|------------|--------|----------|-----------------|-----------|
| Security awareness (general) | SOC 2 CC1.4 / Policy | All employees + contractors | Phishing, passwords, social engineering, incident reporting, acceptable use | MOD-001 |
| Data protection awareness | GDPR Art. 39 / ISO A.7.2 | All employees + contractors | Data classification, GDPR basics, DSR handling, breach reporting | MOD-002 |
| Secure coding practices | SOC 2 CC8.1 / OWASP | Engineering (developers, SREs) | OWASP Top 10, secure SDLC, dependency management, secrets management | MOD-003 |
| Business email compromise | Internal policy | Finance, HR, executives | Wire fraud, BEC, CFO fraud, dual approvals | MOD-004 |
| Physical security | SOC 2 CC6.4 / ISO A.11 | Office-based employees | Tailgating, clean desk, visitor management, device security | MOD-005 |
| Privileged access responsibilities | SOC 2 CC6.1 | IT admins, DevOps, SREs | Least privilege, PAM, credential hygiene, separation of duties | MOD-006 |
| Privacy and data handling (customer data) | CCPA / GDPR / Contract | Customer-facing roles (Sales, Support) | Personal data handling, customer data minimisation, breach reporting | MOD-007 |

---

## Annual Training Calendar

| Month | Activity | Audience | Module / Topic | Delivery Method | Owner |
|-------|----------|----------|----------------|-----------------|-------|
| January | Annual security awareness training launch | All employees | MOD-001: Security Fundamentals | LMS — async video + quiz | [Compliance] |
| January | Annual data protection training launch | All employees | MOD-002: Data Protection | LMS — async video + quiz | [Compliance] |
| February | Phishing simulation — Campaign 1 (basic) | All employees | Credential harvesting | [KnowBe4 / Proofpoint] | [Security] |
| March | Secure coding training | Engineering | MOD-003: OWASP Top 10 | LMS + hands-on lab | [Security Engineering] |
| April | Phishing simulation — Campaign 2 (intermediate) | All employees | Spear phishing + pretexting | [Platform] | [Security] |
| May | BEC / wire fraud training | Finance, HR, Executives | MOD-004: Business Email Compromise | LMS + tabletop exercise | [Compliance] |
| June | Mid-year completion audit — escalate stragglers | All employees | All required modules | Manager notification | [Compliance] |
| July | Phishing simulation — Campaign 3 (advanced) | All employees | Whaling + vishing | [Platform] | [Security] |
| August | Privileged access training | IT / DevOps / SREs | MOD-006: PAM & Secrets | LMS | [Security] |
| September | Privacy training refresh | Customer-facing roles | MOD-007: Customer Data Handling | LMS | [Compliance] |
| October | [Cybersecurity Awareness Month] Special campaign | All employees | Topical security event or threat briefing | Email + LMS | [Security] |
| November | Phishing simulation — Campaign 4 (targeted) | All employees | Industry-specific lure | [Platform] | [Security] |
| December | Annual completion close-out; non-completers escalated to HR | All employees | All modules | HR escalation | [Compliance / HR] |

**New hire onboarding training:** MOD-001 + MOD-002 must be completed within 14 days of start date. Access to production systems is blocked until completion. Triggered automatically by HRIS integration.

---

## Phishing Simulation Programme

| Campaign # | Month | Difficulty | Lure Category | KPIs Tracked | Target Click Rate | Actual Click Rate | Report Rate | Credential Submission Rate |
|-----------|-------|-----------|---------------|--------------|-------------------|-------------------|-------------|---------------------------|
| 1 | February | Basic | Generic credential harvest | Click, Report, Credential submission | < 15% | [N]% | > 30% | < 5% |
| 2 | April | Intermediate | Spear phishing (personalised) | | < 12% | [N]% | | |
| 3 | July | Advanced | Whaling (exec impersonation) | | < 10% | [N]% | | |
| 4 | November | Targeted | Industry-specific lure | | < 8% | [N]% | | |

**Immediate feedback:** Employees who click a simulation link see an immediate educational landing page. No punitive consequences for first failure.
**Repeat offenders:** Employees who fail 2+ simulations are enrolled in targeted remediation training (MOD-001 refresher + 1:1 manager notification).
**Trend target:** Year-over-year reduction in click rate of ≥ 20%.

---

## Training Completion Tracker

| Department | Headcount | MOD-001 Complete | MOD-002 Complete | Role-Specific Complete | Overall Completion % | Overdue (7+ days) |
|-----------|-----------|-----------------|-----------------|----------------------|---------------------|-------------------|
| Engineering | [N] | [N] | [N] | MOD-003: [N] | [N]% | [N] |
| Sales | [N] | [N] | [N] | MOD-007: [N] | [N]% | [N] |
| Customer Success | [N] | [N] | [N] | MOD-007: [N] | [N]% | [N] |
| Finance | [N] | [N] | [N] | MOD-004: [N] | [N]% | [N] |
| HR | [N] | [N] | [N] | MOD-004: [N] | [N]% | [N] |
| IT / DevOps | [N] | [N] | [N] | MOD-006: [N] | [N]% | [N] |
| Executives | [N] | [N] | [N] | MOD-004: [N] | [N]% | [N] |
| Contractors | [N] | [N] | [N] | Role-dependent | [N]% | [N] |
| **Total** | **[N]** | **[N]** | **[N]** | | **[N]%** | **[N]** |

**Reporting period:** [Q1 / Q2 / Q3 / Q4 YYYY] — data exported from LMS on [MM/DD/YYYY]
**SOC 2 audit evidence:** LMS completion report exported and archived at [GDrive / Confluence / GRC tool]

---

## Quarterly Compliance Report

**Quarter:** [Q1 / Q2 / Q3 / Q4 YYYY]

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Annual training completion rate | 100% by [MM/DD] | [N]% | [On track / At risk] |
| New hire onboarding completion within 14 days | 100% | [N]% | |
| Phishing simulation average click rate | < [N]% | [N]% | |
| Phishing report rate | > [N]% | [N]% | |
| Remediation training completion (repeat offenders) | 100% | [N]% | |
| Assessment pass rate (≥ 80% score) | ≥ 95% of completions | [N]% | |

**Notable incidents triggered by training gaps:** [List any security incidents where awareness was a contributing factor]
**Programme improvements planned:** [List based on simulation results, incident patterns, or new threats]
**Next audit evidence package date:** [MM/DD/YYYY — for SOC 2 / GDPR / customer audit]
