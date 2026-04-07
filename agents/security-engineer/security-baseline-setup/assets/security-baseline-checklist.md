# Security Baseline Setup Checklist: [Service / Product Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Security Engineer |
| Service | [Service name and team] |
| Environment | [All environments / Production / Staging] |
| Skill | security-baseline-setup |
| Status | [In Progress / Complete] |
| Compliance Target | [SOC 2 Type II / ISO 27001 / PCI DSS / HIPAA / None] |

## Completion Summary

| Category | Total Items | Complete | Incomplete | N/A |
|----------|------------|---------|-----------|-----|
| Identity and Access | [N] | [N] | [N] | [N] |
| Secrets Management | [N] | [N] | [N] | [N] |
| Network Security | [N] | [N] | [N] | [N] |
| Application Security | [N] | [N] | [N] | [N] |
| Data Protection | [N] | [N] | [N] | [N] |
| Logging and Monitoring | [N] | [N] | [N] | [N] |
| Incident Response | [N] | [N] | [N] | [N] |
| **Total** | **[N]** | **[N]** | **[N]** | **[N]** |

---

## Category 1: Identity and Access Management

- [ ] MFA enabled for all human accounts (cloud console, GitHub, SaaS tools)
- [ ] MFA enforced at organization level (cannot be disabled by individual users)
- [ ] Service accounts use IAM roles, not long-lived credentials
- [ ] Principle of least privilege applied to all IAM roles
- [ ] No wildcard permissions (`*`) on production IAM policies
- [ ] Admin access limited to < 3 named individuals
- [ ] Access reviews scheduled quarterly for all privileged accounts
- [ ] Offboarding checklist includes access revocation (tested in last 90 days)
- [ ] SSH key authentication only (password auth disabled on all servers)

---

## Category 2: Secrets Management

- [ ] All secrets stored in secrets manager (Vault / AWS Secrets Manager / GCP Secret Manager)
- [ ] No secrets in source code, CI environment variables, or Docker images
- [ ] No secrets in application logs
- [ ] Secret rotation policy defined and automated for database credentials (≤ 90 days)
- [ ] Secret rotation policy defined for API keys (≤ 90 days)
- [ ] Emergency secret rotation procedure documented and tested
- [ ] `.gitignore` contains `.env` and credential file patterns
- [ ] Git history scanned for leaked secrets (TruffleHog / gitleaks run on all repos)

---

## Category 3: Network Security

- [ ] All external traffic over HTTPS (TLS 1.2+); HTTP → HTTPS redirect
- [ ] TLS certificate auto-renewal configured
- [ ] Internal service communication over mTLS or within VPC (no plaintext inter-service)
- [ ] WAF configured on public endpoints
- [ ] Security groups / firewall rules follow allowlist (deny-by-default)
- [ ] No 0.0.0.0/0 ingress rules except on ports 80/443 (WAF terminates)
- [ ] Database not directly accessible from internet (VPC only)
- [ ] SSH access restricted to bastion host or VPN (not directly to prod)
- [ ] DDoS protection enabled (AWS Shield / Cloudflare / equivalent)

---

## Category 4: Application Security

- [ ] SAST integrated in CI (Semgrep / CodeQL / Snyk Code)
- [ ] Dependency vulnerability scanning in CI (npm audit / pip-audit / govulncheck / Snyk)
- [ ] SAST findings: 0 Critical, 0 High in production
- [ ] Dependency CVEs: 0 Critical, 0 High in production
- [ ] CSP (Content Security Policy) headers on all web responses
- [ ] HSTS header configured
- [ ] X-Content-Type-Options: nosniff
- [ ] CSRF protection on all state-changing endpoints
- [ ] Rate limiting on authentication endpoints (login, password reset, signup)
- [ ] Secure cookie flags: HttpOnly, Secure, SameSite=Strict

---

## Category 5: Data Protection

- [ ] Encryption at rest enabled on all databases and storage
- [ ] Encryption key management documented (who manages, how rotated)
- [ ] PII data fields identified and catalogued
- [ ] PII handling documented: retention, access controls, deletion
- [ ] Data retention policy implemented (automated deletion / archival)
- [ ] Database backups encrypted
- [ ] Backup restore tested in last 90 days

---

## Category 6: Logging and Monitoring

- [ ] Centralized log aggregation (all services → single platform)
- [ ] Audit log for all authentication events (login, logout, failed auth)
- [ ] Audit log for all admin/privileged actions
- [ ] Logs retained for ≥ [90 days / 1 year per compliance requirement]
- [ ] Logs are immutable (cannot be modified or deleted by application)
- [ ] Alert: Failed authentication spike (> N failed logins from same IP in Y minutes)
- [ ] Alert: Unusual admin activity outside business hours
- [ ] Alert: Mass data access or export anomaly

---

## Category 7: Incident Response

- [ ] Incident response playbook documented and accessible
- [ ] On-call rotation includes security incidents
- [ ] Security incident severity classification defined (P1/P2/P3)
- [ ] Escalation path defined (including when to notify legal / executive team)
- [ ] Contact information for security@company.com and vendor security teams documented
- [ ] Incident response tabletop exercise completed in last 12 months
- [ ] Breach notification procedure documented (GDPR: 72-hour window)

---

## Open Items

| # | Category | Item | Owner | Due |
|---|----------|------|-------|-----|
| 1 | [Category] | [Specific item not yet complete] | [Role] | [Date] |

**Baseline approved by**: Security Engineer: [Name] | Date: [YYYY-MM-DD]
