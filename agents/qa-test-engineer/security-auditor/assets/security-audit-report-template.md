# Security Audit Report: [Scope]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Auditor | QA / Test Engineer |
| Scope | [Feature / Release / Full application] |
| Standard | [OWASP WSTG / Internal checklist] |
| Skill | security-auditor |
| Status | [Pass / Fail / Conditional Pass] |

## Verdict

**Result**: [PASS / FAIL / CONDITIONAL PASS]
**Critical findings**: [N]
**High findings**: [N]
**Medium findings**: [N]

## Findings

### Critical (Block release)

| # | Finding | Location | OWASP Category | Remediation |
|---|---------|----------|---------------|-------------|
| 1 | [Specific finding] | [File / Endpoint] | [A03 Injection] | [Specific fix] |

### High (Fix before release)

| # | Finding | Location | OWASP Category | Remediation |
|---|---------|----------|---------------|-------------|
| 1 | | | | |

### Medium (Fix in next sprint)

| # | Finding | Location | Remediation |
|---|---------|----------|-------------|
| 1 | | | |

## OWASP Quick Scan

| Category | Tested | Findings | Pass? |
|----------|--------|---------|-------|
| A01 Broken Access Control | [Yes/Partial] | [N] | [Yes/No] |
| A02 Cryptographic Failures | [Yes/Partial] | [N] | |
| A03 Injection | [Yes/Partial] | [N] | |
| A04 Insecure Design | [Yes/Partial] | [N] | |
| A05 Security Misconfiguration | [Yes/Partial] | [N] | |
| A06 Vulnerable Components | [Yes/Partial] | [N] | |
| A07 Auth Failures | [Yes/Partial] | [N] | |
| A08 Data Integrity Failures | [Yes/Partial] | [N] | |
| A09 Logging Failures | [Yes/Partial] | [N] | |
| A10 SSRF | [Yes/Partial] | [N] | |

## Auth and Access Control Tests

| Test | Method | Result |
|------|--------|--------|
| Unauthenticated access to protected endpoints | [GET /api/profile without token → expect 401] | [Pass/Fail] |
| IDOR on resource ownership | [Access another user's resource → expect 403] | [Pass/Fail] |
| Admin endpoint accessible to regular user | [POST /admin/... with user token → expect 403] | [Pass/Fail] |
| JWT algorithm confusion | [Modify alg to none → expect 401] | [Pass/Fail] |

## Input Validation Tests

| Input | Test | Result |
|-------|------|--------|
| SQL injection (basic) | `'; DROP TABLE users; --` in search field | [Pass: sanitized / Fail: error or data returned] |
| XSS | `<script>alert(1)</script>` in text field | [Pass: escaped / Fail: executed] |
| Path traversal | `../../etc/passwd` in file path param | [Pass: rejected / Fail: file returned] |
| Oversized payload | 10 MB JSON body | [Pass: 413 returned / Fail: accepted] |

## Remediation Plan

| # | Severity | Action | Owner | Due |
|---|----------|--------|-------|-----|
| 1 | Critical | [Specific fix] | [Role] | [Before release] |
| 2 | High | [Specific fix] | [Role] | [Before release] |
