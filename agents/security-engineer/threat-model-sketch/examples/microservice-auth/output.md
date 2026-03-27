# Threat Model Sketch: Microservice Authentication

## Architecture Diagram (Text)

```
┌──────────────┐     HTTPS/TLS 1.3     ┌──────────────────┐
│  Mobile App  │ ───────────────────>   │   API Gateway    │
│  (Untrusted) │   OAuth2 + PKCE       │  (JWT Validation)│
└──────────────┘                        └────────┬─────────┘
                                                 │
                              ┌──────────────────┼──────────────────┐
                              │ gRPC + mTLS      │ gRPC + mTLS     │
                              ▼                  ▼                  ▼
                    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
                    │ User Service │   │ Order Service│   │ Notification │
                    │              │   │              │   │   Service    │
                    └──────┬───────┘   └──────┬───────┘   └──────────────┘
                           │                  │
                    ┌──────▼───────┐   ┌──────▼───────┐
                    │  PostgreSQL  │   │    Redis     │
                    │  (Encrypted) │   │  (Sessions)  │
                    └──────────────┘   └──────────────┘
```

## Trust Boundaries

| Boundary | Components Inside | Components Outside |
|----------|------------------|--------------------|
| B1: Internet Edge | API Gateway | Mobile App |
| B2: Service Mesh | User/Order/Notification Services | API Gateway |
| B3: Data Layer | PostgreSQL, Redis | All services |

## Threat Surface by Boundary

### B1: Internet Edge

| # | Threat | Category | Mitigation |
|---|--------|----------|------------|
| 1 | Stolen OAuth tokens used to impersonate users | Spoofing | Use PKCE flow. Short-lived access tokens (15 min). Refresh token rotation with reuse detection. |
| 2 | JWT algorithm confusion attack (alg: none) | Tampering | Whitelist `RS256` only. Reject unsigned tokens. |
| 3 | Brute-force login attempts | DoS | Rate limit: 5 attempts/min per account. CAPTCHA after 3 failures. |

### B2: Service Mesh

| # | Threat | Category | Mitigation |
|---|--------|----------|------------|
| 4 | Compromised service sends forged gRPC requests | Spoofing | mTLS with per-service certificates. Certificate rotation via cert-manager. |
| 5 | Lateral movement from compromised container | Elevation | NetworkPolicy: each service can only reach its declared dependencies. No wildcard egress. |
| 6 | Sensitive data in gRPC metadata logged to stdout | Info Disclosure | Scrub PII from logs. Mark sensitive proto fields with `[(google.api.field_behavior) = INPUT_ONLY]`. |

### B3: Data Layer

| # | Threat | Category | Mitigation |
|---|--------|----------|------------|
| 7 | Redis session hijacking via network sniffing | Info Disclosure | Require TLS for Redis connections. `requirepass` enabled. Bind to private subnet only. |
| 8 | SQL injection through User Service | Tampering | Parameterized queries. DB user has no DDL permissions. |
| 9 | Database backup exfiltration | Info Disclosure | Encrypt backups with KMS. Restrict S3 bucket policy to backup service role only. |

## Data Flow Classification

| Flow | Data Classification | Protection |
|------|-------------------|------------|
| Mobile -> Gateway | Auth credentials, PII | TLS 1.3, certificate pinning |
| Gateway -> Services | JWT claims, request payload | mTLS, signed JWT forwarding |
| Services -> PostgreSQL | User PII, payment refs | TLS, column-level encryption for PII |
| Services -> Redis | Session tokens, temp cache | TLS, 1-hour TTL, no PII in cache values |

## Priority Actions

1. **Implement PKCE** for mobile OAuth flow (prevents authorization code interception)
2. **Enable mTLS** across all internal gRPC channels
3. **Add Redis TLS** and authentication
4. **Deploy NetworkPolicies** restricting service-to-service communication
