---
name: github-org-setup
description: Configures the GitHub organization so teams ship code securely with the right access and branch protections.
department: engineering
agent: devops-infrastructure-engineer
version: 1.0.0
complexity: medium
related-skills: []
---

# github-org-setup

## Agent

L2 DevOps and infrastructure engineer responsible for CI/CD pipelines, deployment automation, cloud infrastructure, monitoring, alerting, incident response, and rollout management.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The DevOps / Infrastructure Engineer configures the GitHub organisation with repositories, permissions, and branch protection rules.

## When to Use

- A new GitHub organization is being created for the company or a business unit.
- New repositories need to be provisioned with standardized settings.
- Team structure has changed and repository permissions need updating.
- Branch protection rules need to be added or tightened after a security or process incident.

## Workflow

1. Define the organizational structure: teams, their repository access levels, and admin ownership.
2. Create or update GitHub teams that mirror the engineering team structure.
3. Configure repository creation defaults: visibility, license, .gitignore, and template repositories.
4. Set branch protection rules on main/production branches: required reviews, status checks, and no force pushes.
5. Configure required status checks that must pass before merge (CI pipeline, linting, tests).
6. Set up CODEOWNERS files to enforce review requirements for critical paths.
7. Enable security features: Dependabot, secret scanning, and code scanning.
8. Document the organization setup, team permissions, and branch protection policies.
   - **Deliverable**: A configured GitHub organization with teams, permissions, branch protections, security features, and documentation.

## Anti-Patterns

- **Giving all developers admin access.** *Why*: Admin access allows bypassing branch protections and deleting repositories; use least-privilege roles.
- **Skipping branch protection on main.** *Why*: Unprotected main branches allow force pushes and unreviewed merges that bypass the entire quality process.
- **Not enabling secret scanning.** *Why*: Leaked secrets in repositories are a top security incident vector; scanning catches them before they cause damage.
- **Managing permissions manually instead of through teams.** *Why*: Individual permissions do not scale and create orphaned access when people change roles.

## Output

**Success**: A fully configured GitHub organization with teams, permissions, branch protections, security scanning, and documentation.

**Failure**: An audit report listing permission gaps, missing protections, or security features not enabled, with remediation steps.

## Related Skills

*None defined yet.*
