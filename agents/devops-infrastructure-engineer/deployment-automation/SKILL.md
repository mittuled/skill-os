---
name: deployment-automation
description: Eliminates manual deployment steps so releases are fast, repeatable, and free from human error.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills: []
---

# deployment-automation

## Agent

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer automates deployment processes to reduce manual steps and human error.

## When to Use

- Deployments currently require manual SSH, script execution, or console clicks.
- Deployment frequency is limited by human availability rather than technical readiness.
- A deployment error caused by a manual misstep needs to be prevented from recurring.
- The team is scaling and manual deployment processes will not keep pace.

## Workflow

1. Audit the current deployment process: document every manual step, decision point, and prerequisite.
2. Identify which steps can be automated immediately vs. which require infrastructure changes first.
3. Implement deployment scripts or pipeline stages that replace each manual step.
4. Add pre-deployment checks: version validation, dependency verification, and environment health.
5. Add post-deployment checks: smoke tests, health endpoint verification, and metric baseline comparison.
6. Implement rollback automation triggered by failed post-deployment checks.
7. Test the automated deployment end-to-end in a non-production environment.
8. Document the automated deployment process and any remaining manual gates.
   - **Deliverable**: An automated deployment pipeline with pre/post checks, rollback capability, and documentation.

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
