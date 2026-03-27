# STRIDE Threat Model: Payment API

## System Components

| ID | Component | Trust Boundary |
|----|-----------|---------------|
| C1 | Web Frontend | Public Internet |
| C2 | Payment API | Internal Network |
| C3 | Stripe API | External Third-Party |
| C4 | PostgreSQL DB | Internal Data Store |
| C5 | Email Service | Internal Network |

## Threat Analysis

### Spoofing

| Threat | Target | Risk | Mitigation |
|--------|--------|------|------------|
| Attacker impersonates legitimate user | C1 -> C2 | High | Enforce JWT authentication with short-lived tokens. Require MFA for payment operations. |
| Forged webhook callbacks | C3 -> C2 | High | Verify Stripe webhook signatures using `stripe-signature` header. Pin to known Stripe IP ranges. |

### Tampering

| Threat | Target | Risk | Mitigation |
|--------|--------|------|------------|
| Man-in-the-middle modifies payment amount | C1 -> C2 | Critical | Enforce TLS 1.3. Server-side amount validation against catalog prices. |
| Transaction records altered in DB | C2 -> C4 | High | Append-only transaction table with row-level checksums. Database audit logging enabled. |

### Repudiation

| Threat | Target | Risk | Mitigation |
|--------|--------|------|------------|
| User denies making a payment | C2 | Medium | Log all payment requests with user ID, IP, timestamp, and idempotency key. Store Stripe `payment_intent` IDs. |
| Admin modifies transaction logs | C4 | Medium | Ship logs to immutable storage (S3 with Object Lock). |

### Information Disclosure

| Threat | Target | Risk | Mitigation |
|--------|--------|------|------------|
| Card numbers leaked from API logs | C2 | Critical | Never log raw card data. Use Stripe.js for client-side tokenization so PAN never touches your server. |
| Database breach exposes transaction history | C4 | High | Encrypt at rest (AES-256). Column-level encryption for PII. Restrict DB access to service accounts only. |

### Denial of Service

| Threat | Target | Risk | Mitigation |
|--------|--------|------|------------|
| Payment endpoint flooded | C2 | High | Rate limiting: 10 req/min per user, 100 req/min per IP. WAF rules for known attack patterns. |
| Stripe API outage blocks all payments | C3 | Medium | Circuit breaker pattern. Queue failed payments for retry. Display user-friendly degradation message. |

### Elevation of Privilege

| Threat | Target | Risk | Mitigation |
|--------|--------|------|------------|
| SQL injection via payment metadata | C2 -> C4 | Critical | Parameterized queries only. Input validation on all metadata fields. No dynamic SQL. |
| Compromised service account escalates to DB admin | C4 | High | Least-privilege DB roles. Payment API account has INSERT/SELECT only on `transactions` table. |

## Risk Summary

| Category | Critical | High | Medium |
|----------|----------|------|--------|
| Spoofing | 0 | 2 | 0 |
| Tampering | 1 | 1 | 0 |
| Repudiation | 0 | 0 | 2 |
| Info Disclosure | 1 | 1 | 0 |
| Denial of Service | 0 | 1 | 1 |
| Elevation of Privilege | 1 | 1 | 0 |
