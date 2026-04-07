# Security Policy Lifecycle Framework

Reference framework for drafting, reviewing, approving, and maintaining security and compliance policy documents.

## Required Policy Library

### Core Security Policies (Required for SOC 2 / ISO 27001)

| Policy | SOC 2 Criteria | ISO 27001 Control | Review Cadence |
|--------|---------------|-------------------|---------------|
| Information Security Policy | CC1.1 | A.5.1 | Annual |
| Access Control Policy | CC6.1-6.3 | A.9.1-9.4 | Annual |
| Change Management Policy | CC8.1 | A.12.1, A.14.2 | Annual |
| Incident Response Policy | CC7.2-7.5 | A.16.1 | Annual + post-incident |
| Risk Management Policy | CC3.1-3.4 | A.6.1 | Annual |
| Data Classification Policy | CC6.5 | A.8.2 | Annual |
| Acceptable Use Policy | CC1.4 | A.8.1 | Annual |
| Vendor Management Policy | CC9.2 | A.15.1-15.2 | Annual |
| Business Continuity / DR Policy | A1.2 | A.17.1 | Annual + post-drill |
| Encryption Policy | CC6.1 | A.10.1 | Annual |

### Privacy Policies (Required for GDPR / CCPA)

| Policy | Regulation | Review Cadence |
|--------|-----------|---------------|
| Privacy Policy (external) | GDPR Art. 13-14, CCPA | Per product change, minimum annual |
| Data Retention Policy | GDPR Art. 5(1)(e) | Annual |
| Data Subject Request Policy | GDPR Art. 15-22, CCPA | Annual |
| Data Breach Notification Policy | GDPR Art. 33-34, state statutes | Annual |

## Policy Document Structure

Every security policy must contain these sections:

| Section | Purpose | Content |
|---------|---------|---------|
| Purpose | Why this policy exists | Business and regulatory justification |
| Scope | Who and what it covers | Roles, systems, data types |
| Roles and Responsibilities | Who does what | RACI: responsible, accountable, consulted, informed |
| Requirements | What must be done | Specific, measurable, enforceable requirements |
| Exceptions | How to handle non-compliance | Exception request process, approval authority, documentation |
| Enforcement | Consequences of violation | Disciplinary actions, escalation path |
| Definitions | Key terms | Glossary of terms used in the policy |
| Review History | Change tracking | Version, date, author, changes, approver |

## Policy Review Cycle

### Annual Review Process
1. **Pre-review preparation** (2 weeks before): Compile regulatory changes, audit findings, incident lessons learned, and organisational changes affecting the policy
2. **Content review**: Verify policy still reflects actual practice, update for regulatory changes, address any audit findings
3. **Stakeholder review** (2 weeks): Route to relevant stakeholders (engineering, legal, HR, executive)
4. **Approval**: Obtain formal approval from designated authority
5. **Publication**: Publish updated version, archive previous, trigger acknowledgement campaign
6. **Acknowledgement tracking**: Track employee acknowledgement within 30 days of publication

### Triggered Reviews (Outside Annual Cycle)
- Regulatory change affecting policy scope
- Security incident revealing policy gap
- Audit finding citing policy deficiency
- Major organisational change (acquisition, new market, infrastructure migration)

## Policy Quality Criteria

| Criterion | Standard | Anti-Pattern |
|-----------|---------|-------------|
| Actionability | Requirements are specific and measurable | "Employees should use strong passwords" without defining "strong" |
| Feasibility | Requirements are achievable with current resources | Requiring 24/7 SOC when the company has 3 engineers |
| Currency | Reflects current practices and regulations | References deprecated technology or repealed regulations |
| Accessibility | Written for the intended audience | Legal jargon for an all-employee acceptable use policy |
| Enforceability | Clear consequences and exception process | Requirements without enforcement mechanism |
