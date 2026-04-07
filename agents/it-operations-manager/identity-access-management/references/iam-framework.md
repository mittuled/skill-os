# Identity and Access Management Framework

Reference for the `identity-access-management` skill.

---

## 1. IAM Core Concepts

| Concept | Definition |
|---------|-----------|
| **Identity Provider (IdP)** | Central authority that stores and authenticates user identities (e.g., Okta, Azure AD, Google Workspace) |
| **Single Sign-On (SSO)** | Allows users to authenticate once and access multiple applications without re-entering credentials |
| **Multi-Factor Authentication (MFA)** | Requires two or more verification factors: something you know, have, or are |
| **SAML 2.0** | XML-based open standard for exchanging authentication data between IdP and service providers |
| **OIDC / OAuth 2.0** | Modern token-based protocol for authentication and authorisation; preferred for newer SaaS apps |
| **SCIM 2.0** | Protocol for automating user provisioning and deprovisioning between IdP and SaaS apps |
| **RBAC** | Role-Based Access Control: permissions assigned to roles, not individuals |
| **ABAC** | Attribute-Based Access Control: permissions based on user attributes, resource type, and context |

---

## 2. IdP Selection Decision Matrix

| Criterion | Weight | Okta | Azure AD | Google Workspace |
|-----------|--------|------|---------|-----------------|
| SSO app integrations (pre-built) | High | 7,000+ | 3,500+ | 1,000+ |
| SCIM provisioning support | High | Excellent | Excellent | Good |
| MFA options | High | TOTP, Push, Biometric | TOTP, Push, FIDO2 | TOTP, Push |
| Pricing (per user/month) | Medium | $6–15 | $6–22 | $6–18 |
| Compliance certifications | High | SOC2, ISO27001, FedRAMP | SOC2, ISO27001, FedRAMP | SOC2, ISO27001 |
| Developer / API extensibility | Medium | High | High | Medium |
| Best for | — | SaaS-heavy orgs | Microsoft-stack orgs | Google-native orgs |

---

## 3. MFA Tier Enforcement Policy

| User Group | MFA Required? | Minimum MFA Method | Exceptions |
|-----------|--------------|-------------------|-----------|
| All employees | Yes | Authenticator app (TOTP) | None |
| Admin / Tier 0 accounts | Yes | Hardware key (FIDO2) or push + PIN | None |
| Contractors / vendors | Yes | Authenticator app (TOTP) | None |
| Service accounts | N/A — use API keys | N/A | Must use short-lived tokens |
| Legacy systems (no MFA support) | Compensating control | Network segment isolation + allowlist | Document exception |

### MFA Method Strength Ranking (Best to Weakest)

1. FIDO2 hardware key (phishing-resistant) — required for admin accounts
2. Authenticator push with number matching — recommended for all employees
3. TOTP (time-based one-time password) — acceptable baseline
4. SMS OTP — not recommended (SIM-swap risk); only allow if no alternative
5. Email OTP — not acceptable for business accounts

---

## 4. SSO Integration Checklist

For each application being integrated into SSO:

- [ ] Confirm application supports SAML 2.0 or OIDC
- [ ] Identify the application's SSO documentation
- [ ] Create application in IdP with correct metadata (Entity ID, ACS URL)
- [ ] Configure attribute mapping (email, name, groups/roles)
- [ ] Enable SCIM provisioning if supported (auto-create/deprovision users)
- [ ] Set group assignment rules (which IdP groups get access)
- [ ] Test with a non-production account before enabling for all users
- [ ] Enforce SSO-only login (disable username/password bypass in app settings)
- [ ] Document the integration in the SSO application registry
- [ ] Set review date for the integration (annual)

---

## 5. RBAC Policy Design

### Role Hierarchy

```
Organisation
└── Department
    └── Function / Team
        └── Individual (assigned one or more roles)
```

### Role Design Principles

1. **Function-based naming**: Roles named for job function, not individual (e.g., `eng-developer`, not `john-doe`)
2. **Principle of least privilege**: Each role grants minimum access required for the function
3. **No role overlap abuse**: If a user legitimately needs two conflicting roles, flag for Separation of Duties review
4. **Documented purpose**: Every role has a documented description and access list

### Separation of Duties Examples

| Conflicting Roles | Risk | Control |
|-------------------|------|---------|
| Finance approver + payment initiator | Fraud | Require two separate identities |
| Code committer + code deployer (to production) | Accidental or malicious deployment | Enforce CI/CD approval gate |
| User admin + auditor | Covering tracks | Separate admin and audit accounts |

---

## 6. Authentication Landscape Audit Template

Before implementing or reviewing IAM:

| Application | Auth Method | SSO Connected? | MFA Enforced? | SCIM Provisioning? | Owner | Notes |
|------------|------------|--------------|--------------|-------------------|-------|-------|
| `[App Name]` | `Local / SSO / Both` | `Yes / No` | `Yes / No / Partial` | `Yes / No` | `[Owner]` | `[Notes]` |

---

## 7. Common IAM Anti-Patterns

| Anti-Pattern | Risk | Recommended Control |
|-------------|------|-------------------|
| SSO without MFA | One stolen credential = all systems compromised | Enforce MFA at IdP level before enabling SSO |
| Service accounts with human MFA bypass | Permanent backdoor if credentials leaked | Use API keys with short TTL; rotate regularly |
| Local admin accounts on SSO apps | Bypass IAM controls entirely | Disable local login in app settings; enforce SSO-only |
| Shared credentials for shared services | Cannot attribute actions; no deprovisioning path | Use role accounts or OAuth app credentials with audit logging |
| Never rotating API keys / tokens | Long-lived compromised keys | Set max key age policy; auto-rotate where supported |

---

*Reference version 1.0 — Technical Operations / IT Operations Manager*
