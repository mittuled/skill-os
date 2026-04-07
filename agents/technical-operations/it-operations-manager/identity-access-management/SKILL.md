---
name: identity-access-management
description: >
  This skill implements and manages the identity and access management system including SSO and MFA.
  Use when asked to set up single sign-on, enforce multi-factor authentication, or design access policies.
  Also consider when a security audit flags authentication weaknesses.
  Suggest when the company exceeds 20 employees and ad-hoc credential management becomes untenable.
department: technical-operations
agent: it-operations-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# identity-access-management

## Agent: IT Operations Manager

L1 IT operations manager (1x) reporting to the COO, responsible for SaaS stack management, access provisioning, hardware lifecycle, and identity and access management.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)

## Skill Description

The identity and access management skill implements and maintains the IAM infrastructure -- including SSO, MFA, and role-based access policies -- so the organisation has a centralised, secure, and auditable authentication layer across all systems.

## When to Use

- When the company is setting up SSO for the first time to unify authentication across SaaS tools.
- When a security audit or compliance requirement mandates MFA enforcement.
- When the organisation grows beyond the point where ad-hoc credential management is sustainable.
- When onboarding a new SaaS application that needs to integrate with the existing identity provider.

## Workflow

1. **Assess current state**: Inventory all systems and their current authentication methods (local accounts, SSO, MFA status). Deliverable: authentication landscape map.
2. **Select identity provider**: Evaluate and select an identity provider based on SaaS integrations, compliance needs, and budget. Deliverable: selected IdP with justification.
3. **Configure SSO**: Set up SSO connections for all supported applications using SAML or OIDC protocols. Deliverable: SSO-enabled applications list with connection status.
4. **Enforce MFA**: Enable and enforce MFA for all users, prioritising admin and privileged accounts. Deliverable: MFA enforcement policy with compliance report.
5. **Define access policies**: Create role-based access control policies mapping job roles to system permissions. Deliverable: RBAC policy document.
6. **Test and validate**: Verify SSO login flows, MFA prompts, and access policies work correctly across all systems. Deliverable: validation test results.
7. **Document and train**: Document the IAM setup and train employees on SSO login, MFA enrollment, and password policies. Deliverable: IAM documentation and training materials.

## Anti-Patterns

- **SSO without MFA**: Implementing SSO without requiring MFA, creating a single point of compromise. *Why*: SSO concentrates access behind one credential; without MFA, a compromised password exposes every connected system.
- **Over-permissive default roles**: Creating broad default roles that give all users access to everything. *Why*: least-privilege access is a security baseline; broad defaults create data exposure risk.
- **Ignoring non-SSO applications**: Leaving some applications on local authentication while SSO covers others. *Why*: unmanaged local accounts bypass all IAM controls and become the weakest link.

## Output

**On success**: A functioning IAM infrastructure with SSO configured across all supported applications, MFA enforced for all users, RBAC policies in place, and documentation for employee onboarding.

**On failure**: Report which systems could not be integrated (e.g., no SAML support, vendor limitation), what was configured, and recommend workarounds for non-integrated systems.

## Related Skills

- [`access-provisioning-manager`](../access-provisioning-manager/SKILL.md) -- access provisioning operates within the IAM infrastructure this skill builds.
- [`saas-stack-manager`](../saas-stack-manager/SKILL.md) -- SaaS stack management identifies the applications that need IAM integration.
