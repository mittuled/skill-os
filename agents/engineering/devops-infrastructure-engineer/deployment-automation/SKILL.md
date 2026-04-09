---
name: deployment-automation
description: Eliminates manual deployment steps so releases are fast, repeatable, and free from human error. Use when asked to deployment automation. Suggest when relevant.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "automate deployments"
  - "remove manual deploy steps"
  - "make releases one-click"
  - "set up automated deploys"
---

# deployment-automation

## Agent: Social Media Manager

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer automates deployment processes to reduce manual steps and human error.

## When to Use

- Deployments currently require manual SSH, script execution, or console clicks.
- Deployment frequency is limited by human availability rather than technical readiness.
- A deployment error caused by a manual misstep needs to be prevented from recurring.
- The team is scaling and manual deployment processes will not keep pace.

## Workflow

1. **Process Audit**: Document every manual deployment step, decision point, and prerequisite. Map the current runbook to identify SSH sessions, console clicks, script executions, and tribal knowledge. Deliverable: current-state deployment map with automation candidates flagged.
2. **Strategy Selection**: Choose the deployment pattern based on infrastructure: **blue-green** for stateless services (swap ALB target groups or Kubernetes service selectors), **canary** for high-traffic services (route 1-5% via Istio traffic splitting or AWS weighted target groups), **rolling** for stateful workloads (Kubernetes rolling update with maxSurge/maxUnavailable tuning). Deliverable: deployment strategy document with pattern rationale.
3. **Pre-Deployment Automation**: Implement automated pre-flight checks: artifact version validation (SHA-tagged immutable images, never `latest`), dependency health verification (database connectivity, downstream API availability), environment drift detection (Terraform plan diff, Kubernetes config audit), and capacity headroom check. Deliverable: pre-deployment gate configuration.
4. **Deployment Execution Automation**: Replace manual steps with pipeline stages or infrastructure-as-code. For Kubernetes: Helm chart or Kustomize overlays with ArgoCD or Flux for GitOps-driven deploys. For VM-based: Ansible playbooks or Terraform with zero-downtime rolling replacement. Include **health check gates**: readiness probes (`/healthz` returning 200), startup probes for slow-initializing services, and liveness probes to catch post-deploy crashes. Deliverable: automated deployment pipeline or GitOps configuration.
5. **Post-Deployment Validation**: Automate smoke tests (critical user journey HTTP assertions), metric baseline comparison (compare p95 latency, error rate, and throughput against the previous 30-minute window), and synthetic monitoring triggers. If any check fails within the bake time window (10-15 minutes), trigger automatic **rollback**: revert the Kubernetes deployment revision, swap the blue-green target group back, or scale the canary to zero. Deliverable: post-deployment validation suite with automated rollback triggers.
6. **Human Gates**: Retain manual approval gates only where required: database migrations with backward-incompatible schema changes, breaking API version deprecations, and compliance-sensitive deployments. Implement approval via Slack-integrated workflow (approve/reject buttons) rather than SSH access. Deliverable: gate policy document specifying which deployments require human approval and why. [GATE]

## Anti-Patterns

- **Automating without understanding the manual process first.** *Why*: Automating a broken process just makes it fail faster; fix the process, then automate it.
- **Removing all human gates.** *Why*: Some deployments (database migrations, breaking changes) benefit from a human approval step; full automation is not always the goal.
- **Skipping rollback automation.** *Why*: Automated deploys without automated rollback increase risk because recovery still depends on manual intervention.
- **Not testing the automation in staging.** *Why*: Deployment automation that has only been tested in production is a live experiment with user-facing consequences.

## Output

**Success**: A fully automated deployment pipeline that deploys, validates, and can rollback without manual intervention, with documentation.

**Failure**: A partial automation report listing which steps remain manual, why they could not be automated, and a plan to address them.

## Related Skills

*None defined yet.*
