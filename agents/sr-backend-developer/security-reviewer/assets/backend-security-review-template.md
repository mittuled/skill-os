# Backend Security Review: [PR / Feature / Service Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Reviewer | Sr Backend Developer |
| PR / Feature | [PR number, link, or feature name] |
| Service | [Service name] |
| Skill | security-reviewer |
| Outcome | [Approved / Approved with conditions / Blocked] |

## Verdict

**Overall**: [APPROVED / BLOCKED — N critical / CONDITIONAL — fix X before merge]

---

## OWASP Top 10 Assessment

| Category | Applicable? | Status | Notes |
|----------|------------|--------|-------|
| A01 Broken Access Control | [Yes/No] | [Pass/Fail/N/A] | |
| A02 Cryptographic Failures | [Yes/No] | [Pass/Fail/N/A] | |
| A03 Injection | [Yes/No] | [Pass/Fail/N/A] | |
| A04 Insecure Design | [Yes/No] | [Pass/Fail/N/A] | |
| A05 Security Misconfiguration | [Yes/No] | [Pass/Fail/N/A] | |
| A06 Vulnerable and Outdated Components | [Yes/No] | [Pass/Fail/N/A] | |
| A07 Identification and Authentication Failures | [Yes/No] | [Pass/Fail/N/A] | |
| A08 Software and Data Integrity Failures | [Yes/No] | [Pass/Fail/N/A] | |
| A09 Security Logging and Monitoring Failures | [Yes/No] | [Pass/Fail/N/A] | |
| A10 SSRF | [Yes/No] | [Pass/Fail/N/A] | |

---

## Findings

### Critical Findings (Block merge)

| # | Finding | Location | CWE | Remediation |
|---|---------|----------|-----|-------------|
| 1 | [SQL injection via string concatenation in UserRepository.search()] | [File:line] | [CWE-89] | [Use parameterized query] |

### High Findings (Should fix before merge)

| # | Finding | Location | CWE | Remediation |
|---|---------|----------|-----|-------------|
| 1 | [Missing authorization check on DELETE /api/resources/{id}] | [File:line] | [CWE-862] | [Add ownership check before deletion] |

### Medium Findings (Fix in next sprint)

| # | Finding | Location | Remediation |
|---|---------|----------|-------------|
| 1 | [Error response exposes internal stack trace] | [File:line] | [Sanitize error responses] |

### Low Findings (Optional)

| # | Finding | Notes |
|---|---------|-------|
| 1 | [Debug endpoint not rate-limited] | [Low risk; internal only] |

---

## Input Validation Check

| Input Source | Validated? | Method | Missing Validation |
|-------------|-----------|--------|-------------------|
| Request body | [Yes/Partial/No] | [Zod / Joi / Pydantic / Manual] | [List unvalidated fields] |
| URL parameters | [Yes/Partial/No] | | |
| Query string | [Yes/Partial/No] | | |
| File uploads | [Yes/Partial/No] | [Type check / Size limit / Content scan] | |
| External API responses | [Yes/Partial/No] | | |

---

## Authentication and Authorization Check

- [ ] All endpoints requiring auth are protected (tested 401 without token)
- [ ] All endpoints with resource ownership check user is the owner (tested horizontal IDOR)
- [ ] Admin endpoints require admin role (not just authentication)
- [ ] Token validation is cryptographically sound (not just format check)
- [ ] Sensitive operations require re-authentication or MFA step

---

## Secrets and Config Check

- [ ] No hardcoded credentials in code (API keys, DB passwords, tokens)
- [ ] No secrets in log output
- [ ] No secrets in error messages returned to client
- [ ] Environment variable names follow standard (no secrets with misleading names)
- [ ] Config files excluded from source control (`.gitignore` up to date)

---

## Dependency Audit

**New/modified dependencies**:

| Package | Version | CVEs (Critical/High) | Verdict |
|---------|---------|---------------------|---------|
| [package-name] | [version] | [0 / N found] | [OK / Requires update] |

---

## Remediation Summary

| ID | Severity | Action Required | Owner | Due |
|----|----------|----------------|-------|-----|
| 1 | Critical | [Specific fix] | [Assignee] | [Before merge] |
| 2 | High | [Specific fix] | [Assignee] | [Before merge] |

**Sign-off**: Reviewer: [Name] | Date: [YYYY-MM-DD]
