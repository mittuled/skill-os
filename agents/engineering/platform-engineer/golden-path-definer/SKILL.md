---
name: golden-path-definer
description: >
  This skill defines the golden paths that all engineering teams should follow for
  common development tasks. Use when asked to standardize how teams build services,
  deploy code, or implement common patterns. Also consider when teams diverge on
  tooling choices creating maintenance burden. Suggest when the user is starting a
  new service without consulting existing patterns.
department: engineering
agent: platform-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../developer-experience-enabler/SKILL.md
  - ../platform-capability-gap-detector/SKILL.md
---

# golden-path-definer

## Agent: Platform Engineer

L2 platform engineer (1x) responsible for detecting capability gaps, aligning the platform roadmap, defining golden paths, enabling developer experience, and preparing for platform scale.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Defines the golden paths -- recommended patterns, tooling, and templates -- that engineering teams should follow for common development tasks to maximize consistency, velocity, and supportability.

## When to Use

- When multiple teams are solving the same problem (service creation, CI/CD, database access, observability) with different approaches.
- When a new technology or pattern is adopted and needs to be codified into a repeatable, supported path.
- When onboarding friction stems from teams using inconsistent tooling and patterns that new engineers must learn individually.

## Workflow

1. **Pattern Discovery**: Audit how engineering teams currently handle each common task (service creation, deployment, testing, monitoring, database migrations). Document the variants and their trade-offs. Deliverable: current-state pattern inventory with variant analysis.
2. **Golden Path Design**: For each task, design the recommended path by selecting the best variant or creating a new one. Define the tooling, templates, documentation, and guardrails. Ensure the path is opinionated but escapable -- teams can deviate with justification. Deliverable: golden path specification per task.
3. **Template and Tooling Build**: Build the concrete artifacts: project templates, CLI generators, CI/CD pipeline templates, infrastructure-as-code modules, and documentation. Ensure templates are maintained as living code, not snapshots. Deliverable: golden path templates and tools.
4. **Validation with Pilot Team**: Deploy the golden path with one team building a real service. Observe where the path breaks, where documentation is insufficient, and where teams want to deviate. Deliverable: pilot feedback report.
5. **Migration Planning**: For existing services not on the golden path, create a migration guide and prioritize which services to migrate based on maintenance cost and risk. Do not force-migrate stable services with low change rates. Deliverable: migration guide and priority list.
6. **Governance and Evolution**: Establish a process for proposing changes to the golden path. Define who approves deviations and how successful deviations get promoted into the standard path. Deliverable: golden path governance process.

## Anti-Patterns

- **Mandating without value**: Forcing teams onto a golden path that is slower or less capable than their current approach. *Why*: golden paths must be genuinely better; mandates without value create resentment and drive shadow infrastructure.
- **Frozen paths**: Defining golden paths once and never updating them as tooling evolves. *Why*: stale paths push teams to deviate; the golden path must evolve faster than the ecosystem or it becomes the legacy path.
- **No escape hatch**: Making golden paths inescapable with no mechanism for justified deviation. *Why*: edge cases exist; teams that cannot deviate will either build workarounds that are worse than a clean deviation or abandon the platform entirely.
- **Template sprawl**: Creating too many golden paths covering every edge case rather than a small set of well-maintained paths. *Why*: each path has maintenance cost; a few excellent paths outperform many mediocre ones.

## Output

**On success**: Produces golden path specifications, templates, CLI tools, migration guides, and governance process covering the core development tasks. Delivered incrementally with pilot validation.

**On failure**: Report which golden paths could not be defined (e.g., too much legitimate variation across teams), what current patterns exist, and recommended intermediate standardization steps.

## Related Skills

- [`developer-experience-enabler`](../developer-experience-enabler/SKILL.md) -- Developer experience tooling implements and accelerates the golden paths.
- [`platform-capability-gap-detector`](../platform-capability-gap-detector/SKILL.md) -- Capability gaps may indicate missing golden paths for common tasks.
