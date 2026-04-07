# Framework: Penetration Testing Methodology

Defines the structured approach for conducting penetration tests aligned with PTES (Penetration Testing Execution Standard) and OWASP testing guidelines.

## Testing Phases

### Phase 1: Pre-Engagement

| Activity | Deliverable | Required Before Next Phase |
|----------|-------------|---------------------------|
| Define scope (in-scope hosts, APIs, auth flows) | Signed scope document | Yes |
| Set test type (black-box, grey-box, white-box) | Rules of engagement | Yes |
| Define constraints (no-DoS, no-data-exfil, escalation contacts) | Rules of engagement | Yes |
| Establish timeline and communication channels | Test schedule | Yes |

### Phase 2: Reconnaissance

| Technique | Target | Tool Examples |
|-----------|--------|---------------|
| Subdomain enumeration | External attack surface | Amass, Subfinder |
| Port and service scanning | Open ports, running services | Nmap, Masscan |
| API endpoint discovery | REST/GraphQL surfaces | Burp Suite, ffuf |
| Technology fingerprinting | Stack identification | Wappalyzer, WhatWeb |
| Credential leak search | Leaked secrets | TruffleHog, GitLeaks, HIBP |

### Phase 3: Vulnerability Discovery

#### OWASP Top 10 Test Matrix

| Vulnerability | Test Technique | Tools |
|---------------|---------------|-------|
| A01 Broken Access Control | IDOR testing, privilege escalation paths, forced browsing | Burp Suite, manual |
| A02 Cryptographic Failures | TLS config audit, weak cipher detection, sensitive data in transit | testssl.sh, Burp |
| A03 Injection (SQLi, XSS, SSTI) | Payload injection across all input vectors | sqlmap, Burp Intruder |
| A04 Insecure Design | Business logic testing, state machine abuse | Manual testing |
| A05 Security Misconfiguration | Default credentials, verbose errors, unnecessary features | Nuclei templates |
| A06 Vulnerable Components | Dependency CVE scanning | OWASP Dependency-Check |
| A07 Auth Failures | Session fixation, weak tokens, credential stuffing | Burp, Hydra |
| A08 Integrity Failures | Deserialization attacks, CI/CD pipeline abuse | ysoserial, manual |
| A09 Logging Failures | Test for audit bypass, log injection | Manual |
| A10 SSRF | Internal resource probing via user-controllable URLs | Burp Collaborator |

### Phase 4: Exploitation

Exploitation must demonstrate real-world impact with minimal footprint. Only proceed after scope confirmation at each exploitation step.

| Impact Category | Demonstration Target | CVSS v3.1 Base Score Range |
|-----------------|---------------------|---------------------------|
| Unauthenticated data access | Customer record retrieval | 7.5–10.0 (High/Critical) |
| Authentication bypass | Access without valid credentials | 9.0–10.0 (Critical) |
| Privilege escalation | Regular user → admin access | 8.0–9.9 (High/Critical) |
| Lateral movement | Cross-tenant data access | 8.0–10.0 (High/Critical) |
| Remote code execution | Arbitrary command execution | 9.0–10.0 (Critical) |
| Denial of service | Service disruption | 5.0–7.5 (Medium/High) |

### Phase 5: Reporting

#### Finding Severity Classification (CVSS v3.1)

| Severity | CVSS Score | SLA for Remediation |
|----------|-----------|---------------------|
| Critical | 9.0–10.0 | 24 hours |
| High | 7.0–8.9 | 7 days |
| Medium | 4.0–6.9 | 30 days |
| Low | 0.1–3.9 | 90 days |
| Informational | 0.0 | Best effort |

#### Report Structure

1. Executive summary (business risk, critical finding count)
2. Scope and test methodology
3. Finding catalog (per finding: title, CVSS score, description, reproduction steps, evidence, remediation)
4. Risk-ranked remediation roadmap
5. Retest tracking table

### Phase 6: Remediation Verification

- Re-test each finding after fix is applied
- Issue pass/fail verdict per finding
- Produce retest report with updated CVSS scores for any residual risk

## Rules of Engagement Defaults

| Rule | Default |
|------|---------|
| Production data exfiltration | Prohibited — access only, no copy |
| DoS or destructive testing | Prohibited unless explicitly scoped |
| Social engineering | Prohibited unless explicitly scoped |
| Escalation contact | Security lead + on-call engineer |
| Finding disclosure | 30-day private disclosure before any public mention |
