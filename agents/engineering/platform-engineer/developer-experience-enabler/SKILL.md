---
name: developer-experience-enabler
description: >
  This skill implements tools, templates, and automations that improve the developer
  experience. Use when asked to improve developer onboarding, reduce friction in
  development workflows, or automate repetitive engineering tasks. Also consider
  when developer satisfaction surveys flag tooling pain points. Suggest when the
  user is building custom tooling that duplicates existing platform capabilities.
department: engineering
agent: platform-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../golden-path-definer/SKILL.md
  - ../platform-capability-gap-detector/SKILL.md
---

# developer-experience-enabler

## Agent: Platform Engineer

L2 platform engineer (1x) responsible for detecting capability gaps, aligning the platform roadmap, defining golden paths, enabling developer experience, and preparing for platform scale.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Implements tools, templates, and automations that reduce developer friction, accelerate onboarding, and improve the daily development workflow across engineering teams.

## When to Use

- When developer surveys or feedback identify recurring friction points in the development workflow.
- When new engineers consistently take longer than expected to become productive due to tooling complexity.
- When teams are building ad hoc scripts and tools that should be standardized platform capabilities.

## Workflow

1. **Friction Identification**: Gather developer pain points through surveys, support ticket analysis, and direct observation of development workflows. Categorize by frequency, severity, and number of teams affected. Deliverable: prioritized friction inventory.
2. **Solution Design**: For each high-priority friction point, design a solution (CLI tool, template, automation, documentation, or platform feature). Evaluate build vs. buy. Prototype the solution with a pilot team. Deliverable: solution design document with pilot plan.
3. **Implementation and Rollout**: Build the solution, write documentation, and roll it out incrementally. Start with one team, gather feedback, iterate, then expand. Deliverable: deployed tool or automation with usage documentation.
4. **Adoption Tracking**: Measure adoption rates, time savings, and developer satisfaction impact. Remove or iterate on solutions with low adoption. Deliverable: adoption metrics and impact report.

## Anti-Patterns

- **Building without measuring**: Shipping developer tools without tracking whether anyone uses them or whether they save time. *Why*: unmeasured tools accumulate maintenance cost without proven value; adoption data drives prioritization of future investments.
- **Platform team as bottleneck**: Requiring all developer tooling to go through the platform team rather than enabling self-service. *Why*: centralizing all tooling creation creates a bottleneck; the platform team should build platforms that enable teams to build their own tools.
- **Ignoring the unhappy path**: Optimizing the golden path while neglecting error messages, debugging tools, and recovery workflows. *Why*: developers spend more time debugging failures than writing new code; poor error experiences drive workarounds that bypass the platform.

## Output

**On success**: Produces deployed developer tools, templates, or automations with documentation, adoption metrics, and measured time savings. Delivered incrementally as each solution ships.

**On failure**: Report which friction points could not be addressed, what solutions were attempted and why they failed, and recommended alternative approaches. Include developer feedback on why adoption was low.

## Related Skills

- [`golden-path-definer`](../golden-path-definer/SKILL.md) -- Golden paths define the recommended workflows that developer experience tooling supports and accelerates.
- [`platform-capability-gap-detector`](../platform-capability-gap-detector/SKILL.md) -- Capability gaps often manifest as developer experience friction points.
