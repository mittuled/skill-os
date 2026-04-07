# Framework: Threat Model Sketch

Defines the lightweight STRIDE-based approach for rapid threat identification at the design phase.

## STRIDE Categories Reference

| Category | Threat Type | Typical Target | Mitigation Category |
|----------|------------|----------------|---------------------|
| **S** — Spoofing | Attacker impersonates a user or service | Authentication systems, API tokens, sessions | Authentication controls |
| **T** — Tampering | Attacker modifies data in transit or at rest | Data stores, API payloads, log files | Integrity controls (HMAC, signatures, checksums) |
| **R** — Repudiation | Attacker denies performing an action | Transaction systems, audit trails | Non-repudiation (audit logs, digital signatures) |
| **I** — Information Disclosure | Attacker accesses data they should not see | Databases, API responses, error messages | Confidentiality controls (encryption, access control) |
| **D** — Denial of Service | Attacker degrades or disrupts service availability | APIs, infrastructure, dependencies | Availability controls (rate limiting, circuit breakers) |
| **E** — Elevation of Privilege | Attacker gains permissions beyond their authorization | Authorization systems, IAM, admin functions | Authorization controls (RBAC, least privilege) |

## Threat Prioritization Matrix

Score each threat on two dimensions to derive a priority rank:

| Dimension | 1 (Low) | 2 (Medium) | 3 (High) |
|-----------|---------|------------|---------|
| **Impact** | No sensitive data, reversible | Moderate data exposure or service disruption | PII/PHI/financial data breach, irreversible damage, regulatory violation |
| **Likelihood** | Attacker needs sophisticated capability and persistence | Attacker needs moderate skill with public tools | Attacker needs only a browser or API client |

**Threat Score** = Impact × Likelihood (max 9)

Thresholds:
- Score 7–9: Top threat — must appear in the sketch
- Score 4–6: Include if within the 5-threat limit
- Score 1–3: Document as low priority; exclude from sketch if space-constrained

## Attack Surface Taxonomy

When enumerating the attack surface, classify each entry point:

| Entry Point Type | Examples | Default Threat Assumption |
|-----------------|----------|--------------------------|
| Unauthenticated API | Public REST endpoint, webhook receiver | Assume adversarial input on every call |
| Authenticated API | Logged-in user actions | Assume horizontal privilege escalation attempts |
| File / blob upload | Profile photos, document upload | Assume malicious file content |
| External data import | CSV import, webhook payload, RSS feed | Assume injection and oversized payload |
| Browser-rendered content | User-generated content, email previews | Assume XSS payload |
| Admin / internal API | Management endpoints, debug routes | Assume discovery attempts from compromised internal network |
| Third-party integration | OAuth callback, webhook, API key | Assume token theft and replay |

## Business Logic Threat Patterns

Business logic threats are commonly missed because they are invisible to automated scanners:

| Pattern | Example | STRIDE Category |
|---------|---------|----------------|
| Account enumeration | Login form reveals "account doesn't exist" vs. "wrong password" | Information Disclosure |
| Pricing manipulation | Cart total recalculated server-side vs. client-supplied | Tampering |
| Rate limit bypass | Distributing requests across accounts or IPs | Denial of Service |
| Workflow bypass | Skipping mandatory approval steps by direct API call | Elevation of Privilege |
| Mass assignment | Posting extra fields to API that updates privileged attributes | Elevation of Privilege |
| Time-of-check/time-of-use | Race condition on inventory reservation | Tampering |

## Sketch Scope Limiter

A sketch is not a full threat model. Apply these constraints:

| Constraint | Value |
|------------|-------|
| Maximum threats to document | 5 |
| Maximum time to complete sketch | 2 hours |
| Minimum scope definition before sketching | Feature boundary + at least 1 data flow diagram |
| When to escalate to full STRIDE model | Score 9 threat present, 3+ components, or regulated data in scope |
