# Threat Model: [System / Component Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Security Engineer |
| System Owner | [Team / Name] |
| Version | [1.0] |
| Skill | threat-modelling |
| Review Status | [Draft / Peer Reviewed / Approved] |
| Next Review | [YYYY-MM-DD or "Before next major release"] |

## Scope

**What is in scope?**
[System components, services, APIs, data stores, and user roles included in this model.]

**What is explicitly out of scope?**
[Systems, integrations, or threat categories deferred to another model or review.]

**Security objectives**
1. [Primary security objective, e.g., "Prevent unauthorized access to user PII"]
2. [Secondary objective]
3. [Tertiary objective]

## System Decomposition

### Level 0 Data Flow Diagram (Context)

```
[External User] ──HTTP──> [Load Balancer] ──> [App Service]
                                                    │
                                              [Database]
                                                    │
                                          [Audit Log Store]

[Admin User] ──HTTPS──> [Admin Portal] ──> [App Service]
```

### Level 1 Data Flow Diagram (System)

```
[Describe key processes, data stores, external entities, and trust boundaries at component level]
```

### Trust Boundaries

| Boundary | Separates | Auth Mechanism |
|----------|-----------|---------------|
| [TB-1] | Internet / DMZ | [TLS + WAF] |
| [TB-2] | DMZ / Internal network | [mTLS / VPC] |
| [TB-3] | Application / Database | [Service account + secret manager] |
| [TB-4] | User / Admin | [RBAC + MFA] |

## STRIDE Threat Enumeration

### Spoofing

| ID | Element | Threat | Likelihood | Impact | Score | Mitigation |
|----|---------|--------|-----------|--------|-------|------------|
| T-S01 | [Component] | [Threat: attacker impersonates authenticated user by stealing session token] | [H/M/L] | [H/M/L] | [1–25] | [Control: short-lived JWTs + refresh token rotation] |
| T-S02 | | | | | | |

### Tampering

| ID | Element | Threat | Likelihood | Impact | Score | Mitigation |
|----|---------|--------|-----------|--------|-------|------------|
| T-T01 | [Component] | [Threat: attacker modifies in-transit request payload] | [H/M/L] | [H/M/L] | [1–25] | [Control: TLS + HMAC request signing] |

### Repudiation

| ID | Element | Threat | Likelihood | Impact | Score | Mitigation |
|----|---------|--------|-----------|--------|-------|------------|
| T-R01 | [Component] | [Threat: user denies performing action — no audit trail] | [H/M/L] | [H/M/L] | [1–25] | [Control: immutable audit log with user ID and timestamp] |

### Information Disclosure

| ID | Element | Threat | Likelihood | Impact | Score | Mitigation |
|----|---------|--------|-----------|--------|-------|------------|
| T-I01 | [Component] | [Threat: PII returned in error responses or logs] | [H/M/L] | [H/M/L] | [1–25] | [Control: structured error responses with no stack traces; PII scrubbing in log pipeline] |

### Denial of Service

| ID | Element | Threat | Likelihood | Impact | Score | Mitigation |
|----|---------|--------|-----------|--------|-------|------------|
| T-D01 | [Component] | [Threat: unauthenticated endpoint exhausted by high-volume requests] | [H/M/L] | [H/M/L] | [1–25] | [Control: rate limiting at WAF + per-IP quotas] |

### Elevation of Privilege

| ID | Element | Threat | Likelihood | Impact | Score | Mitigation |
|----|---------|--------|-----------|--------|-------|------------|
| T-E01 | [Component] | [Threat: horizontal privilege escalation via IDOR on resource IDs] | [H/M/L] | [H/M/L] | [1–25] | [Control: server-side ownership check on every resource access] |

## Threat Prioritisation

Sorted by Risk Score descending (Likelihood × Impact, both 1–5):

| ID | Category | Threat Summary | Score | Status | Owner |
|----|----------|---------------|-------|--------|-------|
| T-xxx | [S/T/R/I/D/E] | [One-line description] | [25] | [Open/Mitigated] | [Role] |

## Mitigations Summary

| ID | Threat IDs | Control | Implementation | Owner | Target Date |
|----|-----------|---------|----------------|-------|-------------|
| M-01 | [T-S01, T-E01] | [Control name] | [How to implement] | [Role] | [Date] |

## Attack Trees

### High-Priority Attack: [Attack Goal]

```
Goal: [Attacker obtains admin access]
├── Path 1: Steal admin credentials
│   ├── Phishing campaign → (Mitigated: FIDO2 MFA)
│   └── Credential stuffing → (Mitigated: account lockout + breach detection)
└── Path 2: Exploit session management
    ├── Session fixation → (Mitigated: session rotation on auth)
    └── Token theft via XSS → (Mitigated: CSP + HttpOnly cookies)
```

## Residual Risk

| Risk | Accepted | Acceptance Rationale | Review Date |
|------|----------|---------------------|-------------|
| [Threat ID] | [Yes/No] | [Why this residual risk is acceptable] | [Date] |

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Engineer | Initial model |
