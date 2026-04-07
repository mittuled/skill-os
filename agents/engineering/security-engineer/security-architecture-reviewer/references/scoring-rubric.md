# Scoring Rubric: security-architecture-reviewer

Evaluates the security posture of a system architecture across defense-in-depth layering, trust boundary enforcement, data protection controls, compliance alignment, and architectural risk documentation.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Defense-in-Depth Layering | 25% | Security controls at every layer: network, transport, application, data, and identity |
| 2 | Trust Boundary Enforcement | 25% | Every trust boundary crossing enforces authentication, authorization, and input validation |
| 3 | Data Protection Controls | 20% | Encryption at rest and in transit, secrets management, and data classification alignment |
| 4 | Compliance Alignment | 15% | Architecture satisfies applicable regulatory and framework requirements |
| 5 | Risk Documentation | 15% | Security findings are identified, classified by severity, and have remediation recommendations |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent, 5 = partially present with significant gaps, 10 = fully present, comprehensive, no gaps.

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | All layers protected, every boundary enforced with mTLS, encryption everywhere, full compliance alignment, risks documented with mitigations | Approve architecture; schedule annual re-review |
| A | 8.0–8.9 | Strong | All major layers protected, minor implicit trust between low-sensitivity internal services, encryption at rest and in transit, major compliance controls present | Approve with minor remediation plan; re-review before next major architecture change |
| B | 7.0–7.9 | Good | Network and transport secured, 1–2 application-layer auth gaps, encryption on sensitive stores, most compliance controls present | Conditional approval pending gap remediation; re-review before production launch |
| C | 5.0–6.9 | Adequate | Perimeter security present but internal segmentation missing, some implicit trust between services, encryption inconsistent, compliance gaps | Significant remediation required; do not ship to regulated markets until addressed |
| D | 3.0–4.9 | Weak | Minimal security controls, broad implicit trust, critical data stores unencrypted, compliance non-compliant | Security redesign required; escalate to security lead |
| F | 0.0–2.9 | Failing | No meaningful security controls, flat network, no authentication between services, no encryption, compliance non-starters | Block architecture approval; full security redesign mandatory |

## Signal Tables

### Defense-in-Depth Layering

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Network segmentation with security groups per tier; WAF at perimeter; mTLS between all services; input validation at every service boundary; output encoding at render; data-layer access controls; secrets not in code or environment variables |
| 7–8 | Network segmentation present; TLS 1.2+ on all external connections; input validation at API layer; service-to-service auth on sensitive paths; secrets in vault but some services use environment variables |
| 5–6 | Perimeter firewall but flat internal network; TLS on external connections only; input validation inconsistent across services; no mTLS between internal services; secrets in environment variables |
| 3–4 | Basic perimeter firewall; TLS on externally-facing services only; input validation absent on several internal APIs; some plaintext internal traffic |
| 0–2 | No network segmentation; no TLS on some services; no input validation; secrets hardcoded in source or config files |

### Trust Boundary Enforcement

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every trust boundary crossing documented in architecture diagram; each enforces: mutual authentication, authorization check, rate limiting, input schema validation; no implicit internal trust |
| 7–8 | All external-to-internal boundaries fully enforced; internal service-to-service boundaries enforced for sensitive operations; 1–2 low-sensitivity internal boundaries use implicit trust |
| 5–6 | External boundaries enforced; internal service boundaries assume trust after perimeter; authorization at ingress only, not re-validated at each service |
| 3–4 | External authentication present; all internal services trust each other without authentication; no authorization at internal service calls |
| 0–2 | No documented trust boundaries; services accept requests from any internal IP; authorization absent beyond login check |

### Data Protection Controls

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All data classified (public/internal/confidential/restricted); AES-256 at rest for confidential+; TLS 1.3 in transit; HSM or managed KMS for key management; PII field-level encryption; data masking in non-production |
| 7–8 | Most data classified; encryption at rest for sensitive stores; TLS 1.2+ in transit; managed KMS for key storage; PII not in logs; minor field-level encryption gaps |
| 5–6 | High-sensitivity data encrypted; some internal stores unencrypted; TLS on external paths; keys stored in secrets manager but rotation not automated; PII occasionally appears in logs |
| 3–4 | Only explicitly regulated data encrypted; significant unencrypted internal data stores; key rotation manual and infrequent; PII in development logs |
| 0–2 | Data stored in plaintext; no encryption at rest; TLS absent on internal paths; no key management; PII in logs |

### Compliance Alignment

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All applicable frameworks identified (SOC 2, GDPR, HIPAA, PCI-DSS); every required control mapped to architecture component; no gap between required and implemented controls |
| 7–8 | Applicable frameworks identified; 90%+ of required controls implemented in architecture; 1–2 minor controls planned for post-launch remediation |
| 5–6 | Primary framework addressed; secondary frameworks partially addressed; 3–5 controls require architectural change to comply |
| 3–4 | Framework identified but < 70% of required controls implemented; data residency and audit trail controls absent |
| 0–2 | No compliance framework mapped; architecture would fail audit on multiple critical controls |

### Risk Documentation

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All findings have: severity (Critical/High/Medium/Low), affected component, attack scenario, business impact, and specific remediation recommendation with cost estimate |
| 7–8 | All findings have severity and affected component; most have specific remediation; 1–2 findings lack business impact statement |
| 5–6 | Findings listed with severity; component identification incomplete for some; remediation is generic ("add authentication") without specifics |
| 3–4 | Findings listed without severity; no business impact; remediation absent or vague |
| 0–2 | No findings documented despite architectural gaps; or findings listed as a raw checklist without analysis |
