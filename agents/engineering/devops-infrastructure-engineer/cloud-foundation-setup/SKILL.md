---
name: cloud-foundation-setup
description: Lays the secure, well-structured cloud foundation that every service and team will build on.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: complex
related-skills: []
---

# cloud-foundation-setup

## Agent

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer sets up the foundational cloud infrastructure including accounts, networking, and IAM.

## When to Use

- The organization is starting on a new cloud provider and needs the initial account structure.
- A new product or business unit requires isolated cloud infrastructure.
- The current cloud setup has grown organically and needs to be restructured for security and cost isolation.

## Workflow

1. Gather requirements: number of environments, isolation boundaries, compliance constraints, and expected workload types.
2. Design the account/project structure with separate accounts for production, staging, development, and shared services.
3. Configure the networking foundation: VPCs, subnets, CIDR ranges, peering, and DNS.
4. Implement IAM: define roles, policies, and permission boundaries following least-privilege principles.
5. Set up centralized logging and audit trails (CloudTrail, audit logs) for all accounts.
6. Configure billing alerts and cost allocation tags for each account and team.
7. Enable security baselines: encryption at rest, encryption in transit, and security group defaults.
8. Implement infrastructure-as-code (Terraform, CloudFormation) for all foundation resources.
9. Validate the setup by deploying a minimal workload across environments.
10. Document the cloud foundation architecture, naming conventions, and onboarding guide.
    - **Deliverable**: A production-ready cloud foundation with accounts, networking, IAM, security baselines, and IaC definitions.

## Anti-Patterns

- **Using a single account for all environments.** *Why*: Shared accounts make it impossible to enforce blast-radius isolation and complicate cost attribution.
- **Configuring IAM manually instead of through code.** *Why*: Manual IAM changes are unauditable, unreproducible, and drift from the intended state.
- **Skipping encryption defaults.** *Why*: Retrofitting encryption is expensive and risky; starting without it guarantees compliance gaps.
- **Not implementing cost controls from day one.** *Why*: Cloud costs grow exponentially; without early guardrails, the first bill shock will be severe.
- **Treating the foundation as a one-time setup.** *Why*: Cloud foundations require ongoing maintenance as the organization grows, new services launch, and security requirements evolve.

## Output

**Success**: A fully configured cloud foundation with isolated accounts, secure networking, least-privilege IAM, encryption, audit logging, and infrastructure-as-code for all resources.

**Failure**: A gap assessment listing which foundation components are missing or misconfigured, with a remediation plan and risk rating for each gap.

## Related Skills

*None defined yet.*
