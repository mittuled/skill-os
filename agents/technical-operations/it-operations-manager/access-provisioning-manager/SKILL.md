---
name: access-provisioning-manager
description: >
  This skill manages user access provisioning and deprovisioning across all systems.
  Use when asked to grant system access, revoke access for departing employees, or audit user permissions.
  Also consider when a new SaaS tool is added and users need onboarding.
  Suggest when an employee changes roles and access rights need adjustment.
department: technical-operations
agent: it-operations-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "provision user access"
  - "manage access requests"
  - "onboard employee access"
  - "grant system access"
  - "access provisioning"
---

# access-provisioning-manager

## Agent: IT Operations Manager

L1 IT operations manager (1x) reporting to the COO, responsible for SaaS stack management, access provisioning, hardware lifecycle, and identity and access management.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The access provisioning manager handles the full lifecycle of user access -- granting, modifying, and revoking permissions across all company systems -- to ensure employees have the right access at the right time and former employees have none.

## When to Use

- When a new employee joins and needs access provisioned across all relevant systems.
- When an employee departs and all system access must be revoked within the security policy window.
- When an employee changes roles and their access rights need adjustment to match new responsibilities.
- When a periodic access review is due and stale permissions need to be identified and cleaned up.

## Workflow

1. **Receive access request**: Capture the request specifying the user, systems, permission level, and business justification. Deliverable: validated access request.
2. **Verify approval**: Confirm the request is approved by the appropriate manager or follows an automated approval policy. Deliverable: approval confirmation.
3. **Provision access**: Create or update user accounts in each target system with the specified permissions. Deliverable: provisioned accounts with confirmation log.
4. **Notify the user**: Inform the user of their new access, login credentials (via secure channel), and any setup steps required. Deliverable: user notification sent.
5. **Log the change**: Record the provisioning action in the access management log for audit purposes. Deliverable: audit log entry.
6. **Schedule review**: Set a review date for the access grant, especially for elevated or temporary permissions. Deliverable: scheduled access review.

## Anti-Patterns

- **Provisioning without approval**: Granting access based on verbal requests without documented approval. *Why*: unapproved access creates audit failures and security liability.
- **Delayed deprovisioning**: Allowing departed employees to retain access for days after their last day. *Why*: active credentials for former employees are a top security risk vector.
- **Copy-paste permissions**: Cloning another user's access profile instead of granting role-appropriate permissions. *Why*: permission creep accumulates, giving users access far beyond their role requirements.

## Output

**On success**: User access is provisioned or deprovisioned across all relevant systems with approval documentation, an audit log entry, and a scheduled review date for elevated permissions.

**On failure**: Report which systems could not be provisioned (e.g., API error, missing admin credentials), what was completed, and provide manual steps to finish provisioning.

## Related Skills

- [`identity-access-management`](../identity-access-management/SKILL.md) -- IAM provides the authentication infrastructure that access provisioning operates within.
- [`saas-stack-manager`](../saas-stack-manager/SKILL.md) -- SaaS stack management tracks the systems where access needs to be provisioned.
- [`it-helpdesk-operator`](../../../technical-operations/it-support-specialist/it-helpdesk-operator/SKILL.md) -- helpdesk escalates access issues that require provisioning changes.
