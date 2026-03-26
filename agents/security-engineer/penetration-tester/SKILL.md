---
name: penetration-tester
description: >
  This skill conducts penetration tests against systems to identify exploitable
  vulnerabilities. Use when asked to pen test an application, validate security
  controls, or simulate an attacker. Also consider when a major release ships
  without offensive testing. Suggest when the user relies solely on automated
  scanners for security validation.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../threat-modelling/SKILL.md
  - ../secure-code-reviewer/SKILL.md
  - ../security-architecture-reviewer/SKILL.md
---

# penetration-tester

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Conducts penetration tests against systems to identify exploitable vulnerabilities through simulated adversarial techniques aligned with the threat model.

## When to Use

- When a system or feature approaches production release and requires offensive security validation.
- When the threat model identifies high-risk attack surfaces that automated scanners cannot adequately test.
- When a compliance framework requires periodic penetration testing (PCI-DSS 11.3, SOC 2).

## Workflow

1. **Scoping and Rules of Engagement**: Define the test scope (in-scope hosts, APIs, authentication flows), test type (black-box, grey-box, white-box), and rules of engagement (no-DoS, no-production-data-exfil, notification contacts). Deliverable: signed rules of engagement document.
2. **Reconnaissance**: Enumerate the attack surface: subdomains, exposed ports, API endpoints, technology stack fingerprinting, and publicly leaked credentials. Deliverable: reconnaissance report with attack surface map.
3. **Vulnerability Discovery**: Test for OWASP Top 10 vulnerabilities (injection, broken authentication, SSRF, insecure deserialization), business logic flaws, privilege escalation paths, and API authorization bypasses. Use tools (Burp Suite, Nuclei, sqlmap) combined with manual testing. Deliverable: raw vulnerability list with reproduction steps.
4. **Exploitation and Impact Assessment**: Attempt to exploit discovered vulnerabilities to demonstrate real-world impact: data access, privilege escalation, lateral movement, or service disruption. Classify findings using CVSS v3.1 scoring. Deliverable: exploitation evidence with CVSS scores and business impact statements.
5. **Reporting**: Compile findings into a structured report with executive summary, technical details per finding (description, reproduction steps, evidence, CVSS score, remediation guidance), and a risk-ranked remediation roadmap. Deliverable: penetration test report.
6. **Remediation Verification**: After fixes are applied, re-test each finding to confirm remediation effectiveness. Deliverable: retest results with pass/fail per finding.

## Anti-Patterns

- **Scanner-only testing**: Running automated scanners and reporting output without manual exploitation or business logic testing. *Why*: scanners miss logic flaws, chained vulnerabilities, and context-dependent issues that represent the highest-impact risks.
- **Testing in production without safeguards**: Running exploitation attempts against production systems without rules of engagement or rollback plans. *Why*: exploitation can cause data corruption or service outages that impact real users.
- **Severity inflation**: Reporting theoretical vulnerabilities with maximum severity without demonstrating exploitability. *Why*: inflated findings erode trust in security assessments and cause remediation effort to be misallocated.

## Output

**On success**: Produces a penetration test report containing the attack surface map, risk-ranked vulnerability findings with CVSS scores, exploitation evidence, remediation guidance, and retest results. Delivered as a classified document to the security and engineering leads.

**On failure**: Report which test phases could not be completed (e.g., scope access denied, environment unavailable), what partial findings exist, and recommended steps to enable a complete assessment.

## Related Skills

- [`threat-modelling`](../threat-modelling/SKILL.md) -- Provides the threat scenarios that guide penetration test focus areas.
- [`secure-code-reviewer`](../secure-code-reviewer/SKILL.md) -- Identifies code-level vulnerabilities that complement black-box pen testing.
- [`security-architecture-reviewer`](../security-architecture-reviewer/SKILL.md) -- Reviews architectural weaknesses that pen testing validates empirically.
