---
name: security-reviewer
description: >
  This skill reviews backend code for security vulnerabilities including injection, auth flaws, and data exposure. Use when asked to perform a security review, audit authentication logic, or check for OWASP Top 10 issues. Also consider when a service handles PII or payment data. Suggest when a PR modifies authentication, authorization, or data-handling code.
department: engineering
agent: sr-backend-developer
version: 1.0.0
complexity: medium
related-skills:
  - ../builder/SKILL.md
  - ../third-party-integrator/SKILL.md
triggers:
  - "security review"
  - "review for security issues"
  - "code security review"
  - "backend security check"
  - "security vulnerability review"
---

# security-reviewer

## Agent: Sr. Backend Developer

L3 senior backend developer (Nx) responsible for third-party integrations, instrumentation, building backend services, and security review.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Reviews backend code for security vulnerabilities including injection attacks, authentication and authorization flaws, data exposure, and insecure dependency usage, producing a findings report with severity ratings and remediation guidance.

## When to Use

- A PR modifies authentication, authorization, session management, or cryptographic code.
- A new service handles personally identifiable information (PII), payment data, or API secrets.
- A third-party integration introduces new attack surface through external data ingestion.
- A scheduled security review cycle is due per team policy.
- An incident or vulnerability disclosure triggers a targeted review of affected code paths.

## Workflow

1. **Define review scope**: Identify the code paths, services, and data flows under review. Prioritize code handling authentication, authorization, input processing, and data storage. Deliverable: scoped review checklist.
2. **Run static analysis**: Execute SAST tools (e.g., Semgrep, CodeQL, Bandit) against the target codebase. Deliverable: raw static analysis report with flagged issues.
3. **Review OWASP Top 10**: Manually inspect code for each OWASP Top 10 category: injection, broken auth, sensitive data exposure, XXE, broken access control, misconfiguration, XSS, insecure deserialization, vulnerable components, insufficient logging. Deliverable: OWASP checklist with pass/fail per category.
4. **Audit dependency chain**: Check direct and transitive dependencies against known vulnerability databases (CVE, GitHub Advisory). Deliverable: dependency audit report with vulnerable packages and upgrade paths.
5. **Assess data handling**: Verify that PII is encrypted at rest and in transit, secrets are not hardcoded, and sensitive data is excluded from logs. Deliverable: data-handling compliance checklist.
6. **Classify findings**: Rate each finding by severity (critical, high, medium, low) using CVSS or equivalent scoring. Deliverable: classified findings list.
7. **Write remediation guidance**: For each finding, provide a specific fix recommendation with code examples where applicable. Deliverable: security review report with remediation plan.

## Anti-Patterns

- **Reviewing only new code.** Focusing exclusively on the diff ignores vulnerabilities in the existing code that the change interacts with. *Why*: attackers exploit the weakest link in the call chain, not just the newest code.
- **Tool-only review.** Treating SAST output as the complete review misses logic-level vulnerabilities (broken access control, business logic bypass) that tools cannot detect. *Why*: security tooling catches patterns, not intent; human review catches design flaws.
- **Severity inflation.** Marking every finding as critical desensitizes developers and delays remediation of actual critical issues. *Why*: accurate severity ratings enable risk-based prioritization of fixes.
- **No remediation guidance.** Reporting vulnerabilities without specific fix recommendations leaves developers to guess at solutions. *Why*: vague reports produce vague fixes that may introduce new vulnerabilities.

## Output

**On success**: Produces a security review report containing static analysis results, OWASP Top 10 checklist outcomes, dependency audit findings, data-handling compliance results, and severity-classified findings with remediation guidance. Delivered to the code author and engineering lead.

**On failure**: Report which code paths could not be reviewed (e.g., obfuscated third-party code, missing test environment), what partial coverage was achieved, and what access or context is needed to complete the review.

## Related Skills

- [`builder`](../builder/SKILL.md) -- builds the code that this skill reviews for security.
- [`third-party-integrator`](../third-party-integrator/SKILL.md) -- integrates external services that introduce attack surface reviewed by this skill.
