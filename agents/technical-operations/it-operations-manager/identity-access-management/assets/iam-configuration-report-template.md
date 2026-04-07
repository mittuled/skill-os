# IAM Configuration Report

**Prepared By**: `[IT Operations Manager]`
**Date**: `YYYY-MM-DD`
**Report Type**: `[ ] Initial Setup  [ ] Periodic Review  [ ] Audit Response`
**Identity Provider**: `[Okta / Azure AD / Google Workspace / Other]`

---

## 1. IAM Infrastructure Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Identity Provider (IdP) | `Configured / Not Configured` | |
| SSO enabled apps | `## of ## target apps` | |
| MFA enforcement — all users | `Enforced / Partial / Not Enforced` | |
| SCIM provisioning | `Enabled / Partial / Manual only` | |
| RBAC policies defined | `Yes / In Progress / No` | |
| Audit logging active | `Yes / No` | |

---

## 2. SSO Application Registry

| Application | Protocol | SSO Status | MFA Required? | SCIM Provisioning? | Enforced SSO-Only? | Integrated Date |
|------------|---------|-----------|--------------|-------------------|--------------------|----------------|
| `[App Name]` | `SAML / OIDC` | `Active / Testing / Planned` | `Yes / No` | `Yes / No` | `Yes / No` | `YYYY-MM-DD` |

**Applications with SSO Pending or Blocked**:

| Application | Blocker | Target Date | Owner |
|------------|---------|-------------|-------|
| `[App Name]` | `[Reason: no SAML support / vendor delay / etc.]` | `YYYY-MM-DD` | `[Owner]` |

---

## 3. MFA Compliance Report

| User Group | Total Users | MFA Enrolled | MFA Compliant % | Non-Compliant Users |
|-----------|------------|-------------|----------------|---------------------|
| All employees | `##` | `##` | `##%` | `##` |
| Admin / Tier 0 accounts | `##` | `##` | `##%` | `##` |
| Contractors / vendors | `##` | `##` | `##%` | `##` |

**MFA Method Distribution**:

| MFA Method | Users Enrolled | % of Total |
|-----------|--------------|-----------|
| FIDO2 hardware key | `##` | `##%` |
| Authenticator push | `##` | `##%` |
| TOTP app | `##` | `##%` |
| SMS OTP (legacy) | `##` | `##%` |

**Non-Compliant Users — Action Plan**:
```
[List non-compliant users, reason for non-compliance, and deadline for enrollment]
```

---

## 4. RBAC Policy Status

| Role Name | Department | Access Scope | Users Assigned | Last Reviewed | Reviewer |
|-----------|-----------|-------------|--------------|--------------|---------|
| `[Role]` | `[Dept]` | `[Systems]` | `##` | `YYYY-MM-DD` | `[Name]` |

**Roles Flagged for Review**:
```
[List any roles with overly broad permissions, no active users, or not reviewed in >12 months]
```

---

## 5. Applications Without SSO (Non-Integrated)

| Application | Auth Method | Users | Risk Level | Compensating Control | Owner | Target Integration Date |
|------------|------------|-------|-----------|---------------------|-------|------------------------|
| `[App Name]` | `Local` | `##` | `High / Medium / Low` | `[e.g., Network segment, MFA enforced at app level]` | `[Owner]` | `YYYY-MM-DD` |

---

## 6. Recent IAM Changes

| Change | Date | Changed By | Ticket Reference |
|--------|------|-----------|----------------|
| `[e.g., Added app X to SSO]` | `YYYY-MM-DD` | `[Name]` | `TICKET-####` |
| `[e.g., Enforced FIDO2 for admin group]` | `YYYY-MM-DD` | `[Name]` | `TICKET-####` |

---

## 7. Upcoming Actions

| Action | Target Date | Owner | Priority |
|--------|-------------|-------|---------|
| `[e.g., Migrate remaining apps to SSO]` | `YYYY-MM-DD` | `IT Ops` | `High / Medium / Low` |
| `[e.g., Annual RBAC policy review]` | `YYYY-MM-DD` | `IT Ops` | `Medium` |

---

## 8. Exceptions and Sign-Off

**Open Exceptions**:
```
[List any policy exceptions with justification, compensating controls, and review date]
```

**Report Reviewed By**: `[Name, Title]`
**Review Date**: `YYYY-MM-DD`

---

*Template version 1.0 — Technical Operations / IT Operations Manager*
