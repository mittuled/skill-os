# Secure Code Review: [PR / Feature Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Reviewer | Security Engineer |
| PR / Feature | [PR number or feature name] |
| Language / Framework | [TypeScript / Python / Go / Java + framework] |
| Skill | secure-code-reviewer |
| Outcome | [Approved / Approved with conditions / Blocked] |

## Verdict

**Decision**: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED]
**Critical findings**: [N] **High findings**: [N] **Medium findings**: [N]

---

## OWASP Top 10 Coverage

| Category | Applicable | Reviewed | Findings | Pass? |
|----------|-----------|---------|---------|-------|
| A01 Broken Access Control | [Yes/No] | [Yes/No] | [N] | |
| A02 Cryptographic Failures | [Yes/No] | | [N] | |
| A03 Injection | [Yes/No] | | [N] | |
| A04 Insecure Design | [Yes/No] | | [N] | |
| A05 Security Misconfiguration | [Yes/No] | | [N] | |
| A06 Vulnerable and Outdated Components | [Yes/No] | | [N] | |
| A07 Identification and Authentication Failures | [Yes/No] | | [N] | |
| A08 Software and Data Integrity Failures | [Yes/No] | | [N] | |
| A09 Security Logging and Monitoring Failures | [Yes/No] | | [N] | |
| A10 SSRF | [Yes/No] | | [N] | |

---

## Language-Specific Risk Review ([Language])

| Risk Class | Applicable | Finding |
|-----------|-----------|---------|
| [SQL via ORM raw query (all)] | [Yes/No] | [None / Finding description] |
| [Prototype pollution (JS/TS)] | [Yes/No] | |
| [Deserialization (Java/Python)] | [Yes/No] | |
| [Path traversal via user input (all)] | [Yes/No] | |
| [Timing attacks in auth comparisons (all)] | [Yes/No] | |
| [eval() / exec() usage (JS/Python)] | [Yes/No] | |
| [Integer overflow (Go/C)] | [Yes/No] | |

---

## Dependency Audit

| Package | Version | CVE | CVSS | Action |
|---------|---------|-----|------|--------|
| [package-name] | [version] | [CVE-YYYY-XXXX or None] | [Score] | [Update / Accepted / Block] |

**Audit tool**: [npm audit / pip-audit / govulncheck / Snyk]
**New dependencies with unresolved High CVEs**: [None / List]

---

## Findings

### Critical (Block merge)

| # | CWE | Location | Finding | Fix |
|---|-----|----------|---------|-----|
| 1 | [CWE-89] | [file.ts:L42] | [SQL injection via string concatenation in search()] | [Use parameterized query] |

### High (Should fix before merge)

| # | CWE | Location | Finding | Fix |
|---|-----|----------|---------|-----|
| 1 | [CWE-862] | | [Missing ownership check on DELETE /resource/{id}] | [Add ownership check] |

### Medium (Fix in next sprint)

| # | Finding | Location | Fix |
|---|---------|----------|-----|
| 1 | [Error response exposes internal details] | | [Sanitize error response] |

---

## Context Review

**Code reviewed beyond the diff**: [Yes / No]
**Data flow traced from user input to output**: [Yes / No — partial]
**Authorization context reviewed for surrounding functions**: [Yes / No]

---

## Remediation Summary

| # | Severity | Action | Owner | Due |
|---|----------|--------|-------|-----|
| 1 | Critical | [Specific fix] | [Assignee] | Before merge |

**Security Engineer sign-off**: [Name] | Date: [YYYY-MM-DD]
