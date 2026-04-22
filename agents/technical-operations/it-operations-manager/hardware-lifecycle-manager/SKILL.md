---
name: hardware-lifecycle-manager
description: >
  This skill manages the hardware lifecycle including procurement, deployment, and end-of-life disposition.
  Use when asked to order equipment, track hardware assets, or plan device refresh cycles.
  Also consider when an employee joins or departs and hardware needs provisioning or retrieval.
  Suggest when hardware warranty expiration dates are approaching.
department: technical-operations
agent: it-operations-manager
version: 1.0.0
complexity: medium
related-skills:
  - saas-stack-manager
  - it-helpdesk-operator
triggers:
  - "manage hardware lifecycle"
  - "hardware procurement"
  - "track device inventory"
  - "equipment lifecycle"
  - "hardware refresh cycle"
---

# hardware-lifecycle-manager

## Agent: IT Operations Manager

L1 IT operations manager (1x) reporting to the COO, responsible for SaaS stack management, access provisioning, hardware lifecycle, and identity and access management.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)

## Skill Description

The hardware lifecycle manager tracks company hardware assets from procurement through deployment, maintenance, and end-of-life disposition to ensure every employee has functional, secure, and cost-effective equipment.

## When to Use

- When a new hire needs equipment procured and configured before their start date.
- When a departing employee's hardware needs to be retrieved, wiped, and recycled or redeployed.
- When hardware warranty periods are expiring and refresh decisions are needed.
- When the company needs to plan a hardware budget for the next fiscal year.

## Workflow

1. **Maintain asset inventory**: Keep an up-to-date registry of all hardware assets with serial numbers, assigned users, purchase dates, and warranty status. Deliverable: current asset inventory.
2. **Process procurement requests**: Evaluate hardware requests against standard configurations, approve or escalate, and place orders. Deliverable: purchase orders with delivery tracking.
3. **Configure and deploy**: Set up new hardware with standard OS image, security software, and user accounts before delivery. Deliverable: configured, deployment-ready devices.
4. **Track warranty and maintenance**: Monitor warranty expiration dates and schedule preventive maintenance or replacement. Deliverable: maintenance schedule and warranty alert log.
5. **Handle end-of-life**: Retrieve devices from departing employees, wipe data securely, and either redeploy or dispose responsibly. Deliverable: chain-of-custody log with data-wipe certification.

## Anti-Patterns

- **No asset tracking**: Deploying hardware without recording it in an inventory system. *Why*: untracked devices become security blind spots and budget black holes when replacement is needed.
- **Reactive-only procurement**: Ordering hardware only when an employee complains their device is failing. *Why*: rush orders cost more and leave employees unproductive during the wait.
- **Skipping data wipe**: Redeploying or disposing of devices without certified data erasure. *Why*: residual data on unwiped devices is a data breach waiting to happen.

## Output

**On success**: A current hardware asset inventory, timely procurement and deployment for new hires, proactive warranty tracking, and secure end-of-life disposition with data-wipe certification.

**On failure**: Report which lifecycle stage failed (e.g., vendor delivery delayed, device wipe tool unavailable), what was completed, and provide a workaround or escalation path.

## Related Skills

- [`saas-stack-manager`](../saas-stack-manager/SKILL.md) -- software stack runs on the hardware this skill manages.
- [`it-helpdesk-operator`](../../../technical-operations/it-support-specialist/it-helpdesk-operator/SKILL.md) -- helpdesk resolves day-to-day hardware issues that lifecycle management plans for.
