---
name: security-auditor
description: Finds vulnerabilities in code and configuration before attackers do, protecting the product and its users.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "audit security"
  - "security audit"
  - "run security checks"
  - "application security audit"
  - "security vulnerability scan"
---

# security-auditor

## Agent

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The QA / Test Engineer conducts security audits of code and configurations to identify vulnerabilities.

## When to Use

- A feature handles user input, authentication, authorization, or sensitive data.
- A new third-party dependency has been introduced.
- The team is preparing for a security review or compliance audit.
- A vulnerability has been reported in a related component and lateral impact must be assessed.

## Workflow

1. Define the audit scope: code paths, configurations, dependencies, and infrastructure under review.
2. Run automated static analysis (SAST) and dependency vulnerability scanners against the codebase.
3. Review authentication and authorization logic for bypass, escalation, or token mishandling.
4. Inspect input validation and output encoding for injection vulnerabilities (SQL, XSS, command injection).
5. Audit secrets management: confirm no hardcoded credentials, API keys, or tokens in source or configuration.
6. Check infrastructure configuration for misconfigurations (open ports, permissive IAM, missing encryption).
7. Classify each finding by severity (critical, high, medium, low) with a clear exploitation scenario.
8. Report findings to the engineering team with remediation recommendations and priority order.
   - **Deliverable**: Security audit report with classified findings, exploitation scenarios, and remediation plan.

## Anti-Patterns

- **Relying solely on automated scanners.** *Why*: Scanners catch known patterns but miss business-logic vulnerabilities, authorization flaws, and novel attack vectors.
- **Auditing only new code while ignoring legacy surfaces.** *Why*: Attackers do not distinguish old from new; legacy code with known patterns is often the easiest target.
- **Reporting findings without exploitation context.** *Why*: Severity without a concrete attack scenario makes it impossible for engineers to prioritize remediation.
- **Treating security audit as a one-time gate.** *Why*: Security is continuous; a single audit creates a false sense of safety that degrades as the codebase evolves.

## Output

**Success**: A security audit report with no critical or high findings, and a prioritized list of medium/low findings with remediation timelines.

**Failure**: A security audit report with critical or high findings, each including an exploitation scenario, affected component, and an urgent remediation recommendation that blocks release.

## Related Skills

*None defined yet.*
