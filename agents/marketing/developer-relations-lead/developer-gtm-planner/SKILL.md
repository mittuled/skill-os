---
name: developer-gtm-planner
description: >
  This skill plans the developer go-to-market strategy including acquisition, activation, and community channels.
  Use when asked to create a developer GTM plan, define developer acquisition channels, or plan a developer launch.
  Also consider when entering a new developer ecosystem or platform marketplace.
  Suggest when the user is about to launch a developer product without a structured GTM strategy.
department: marketing
agent: developer-relations-lead
version: 1.0.0
complexity: complex
related-skills:
  - developer-launch-packager
  - developer-community-grower
  - developer-experience-reviewer
triggers:
  - "plan the developer GTM"
  - "how do we reach developers"
  - "create a developer acquisition strategy"
  - "plan the developer launch"
---

# developer-gtm-planner

## Agent: Developer Relations Lead

L2 developer relations lead responsible for developer community signal extraction, developer GTM, experience review, feedback synthesis, and community growth.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Plans the developer go-to-market strategy including developer acquisition channels, activation flows, community channels, and success metrics to drive adoption at scale.

## When to Use

- When launching a new developer product, API, or platform and needing a comprehensive GTM strategy.
- When existing developer acquisition is underperforming and the strategy needs a reset.
- When expanding into a new developer ecosystem (e.g., mobile, AI/ML, embedded) and needing a tailored approach.
- When a competitor is gaining developer share and a competitive GTM response is required.

## Workflow

1. **Define developer audience**: Use the persona framework in [framework.md](references/framework.md) to document target developer personas with role, tech stack, motivations, watering holes, decision factors, and blockers. Deliverable: developer persona document.
2. **Map the developer journey**: Use the developer adoption funnel in the framework to define conversion metrics for each stage (discover, evaluate, integrate, build, scale, advocate). Deliverable: developer journey map with funnel metrics.
3. **Select acquisition channels**: Score and rank channels using the channel selection matrix in the framework by persona fit and scalability. Select the top 3–4 channels for initial GTM. Deliverable: channel strategy with budget allocation.
4. **Design activation experience**: Apply the activation experience design principles from the framework to define the onboarding flow targeting TTFHW < 10 minutes. Deliverable: activation flow design.
5. **Plan community and advocacy**: Define how the community programme supports GTM goals and how to convert successful developers into advocates using the advocate stage of the funnel. Deliverable: community-GTM integration plan.
6. **Set metrics and milestones**: Establish KPIs per the GTM metrics framework in the framework document, set quarterly milestones, and validate the measurement stack is in place. Deliverable: GTM metrics framework with targets.
7. **Build launch timeline**: Run through the anti-patterns checklist in the framework before finalizing the launch timeline. Create a phased plan with channel activation sequence, content calendar, and event schedule. Deliverable: developer GTM launch timeline.
8. **Execute and iterate**: Launch the GTM plan, run weekly metric reviews against funnel benchmarks, and iterate channel mix and messaging based on performance data. Deliverable: weekly GTM performance report.

## Anti-Patterns

- **Marketing-first, product-second**: Investing heavily in developer acquisition before the developer experience is ready for the traffic. *Why*: Sending developers to a broken or confusing experience creates negative word-of-mouth that is harder to overcome than building the audience more slowly with a polished experience.
- **Enterprise GTM for developers**: Applying enterprise sales motions (gated content, mandatory demos, sales follow-ups) to developers. *Why*: Developers expect self-serve, ungated access; sales friction drives them to competitors who respect their autonomy.
- **Channel cargo-culting**: Copying a competitor's channel strategy without validating it fits your developer audience. *Why*: Channel effectiveness depends on developer segment, product maturity, and brand trust; what works for an established platform fails for a new entrant.
- **Ignoring the activation gap**: Measuring acquisition (signups) without tracking activation (first successful API call or app deployment). *Why*: Signups without activation is vanity; the GTM plan succeeds only when developers derive value.

## Output

**On success**: Produces a developer GTM plan containing persona definitions, journey map, channel strategy, activation flow, community integration plan, metrics framework, and launch timeline. Delivered to developer relations, marketing, and product leadership.

**On failure**: Report which GTM components could not be defined, what data or decisions are missing, and recommend how to unblock planning. Every error must be actionable.

## Related Skills

- [`developer-launch-packager`](../developer-launch-packager/SKILL.md) — Launch assets must be packaged in alignment with the GTM channel strategy.
- [`developer-community-grower`](../developer-community-grower/SKILL.md) — Community growth programmes execute the community component of the GTM plan.
- [`developer-experience-reviewer`](../developer-experience-reviewer/SKILL.md) — Developer experience must be validated before GTM drives traffic to it.
