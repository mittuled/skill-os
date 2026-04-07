# Security Audit Report — API Gateway v2

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | QA Test Engineer |
| Scope | API Gateway v2 — pre-SOC2 review |
| Audit Score | 20 / 100 |
| Recommendation | RELEASE BLOCKED |
| Skill | security-auditor |

## Recommendation

**RELEASE BLOCKED** — 2 blocking vulnerabilities found (1 critical, 1 high). Release cannot proceed and the SOC 2 review cannot be scheduled until both are remediated and re-audited.

---

## Finding Summary

| Severity | Count |
|---|---|
| Critical | 1 |
| High | 1 |
| Medium | 1 |
| Low | 1 |
| **Total** | **4** |

---

## Blocking Findings (Must Fix)

### CRITICAL — JWT tokens never expire

**Component:** `AuthMiddleware.verify_token`
**Category:** Authentication
**Exploitation:** Stolen JWT token remains valid indefinitely. An attacker who obtains a token through any means (phishing, XSS, MitM) retains access to the account permanently until the password is changed or the token is manually revoked. This is a complete authentication bypass for stolen credentials.

**Remediation:**
1. Set `exp` claim on all issued tokens (recommended: 15 minutes for access tokens, 7 days for refresh tokens)
2. Implement token refresh flow
3. Add token revocation endpoint for logout
4. Audit all existing issued tokens — consider forced re-login for all users post-fix

### HIGH — SQL Injection via String Concatenation

**Component:** `UserRepository.search`
**Category:** Injection
**Exploitation:** An authenticated user submits `'; DROP TABLE users; --` as a search term, destroying the users table. Alternatively, `' OR '1'='1` returns all user records, bypassing authorization.

**Remediation:**
1. Replace string concatenation with parameterized queries immediately
2. Run SAST scan across all repository methods for similar patterns
3. Add input validation for search term (alphanumeric + limited special chars)

---

## Non-Blocking Findings (Track for Next Sprint)

### MEDIUM — Missing Rate Limiting on /auth/login

**Remediation:** Implement rate limiting (max 10 attempts/minute per IP). Use Redis-backed sliding window. Target: resolved in next sprint before SOC 2 review.

### LOW — Stack Traces in Error Responses

**Remediation:** Disable stack trace exposure in production `GlobalErrorHandler`. Log stack traces server-side only. Target: resolved in the same sprint as rate limiting.

---

## Remediation Priority

| # | Finding | Owner | Target |
|---|---|---|---|
| 1 | JWT token expiry | Backend Lead | Immediate — blocks release |
| 2 | SQL injection in search | Backend Developer | Immediate — blocks release |
| 3 | Rate limiting on login | Backend Developer | Next sprint |
| 4 | Stack trace suppression | Backend Developer | Next sprint |

Re-audit required after items 1 and 2 are resolved before SOC 2 review can be scheduled.
