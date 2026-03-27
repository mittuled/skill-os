---
name: developer-launch-packager
description: >
  This skill packages the developer launch assets including SDKs, sample apps, and documentation.
  Use when asked to prepare a developer launch kit, bundle SDK release assets, or coordinate documentation for a developer launch.
  Also consider when a new API version needs a coordinated asset package for release day.
  Suggest when the user is about to announce a developer product without prepared launch assets.
department: marketing
agent: developer-relations-lead
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "package the developer launch"
  - "prepare SDK release assets"
  - "bundle the launch kit for developers"
  - "get developer docs ready for launch"
---

# developer-launch-packager

## Agent: Developer Relations Lead

L2 developer relations lead responsible for developer community signal extraction, developer GTM, experience review, feedback synthesis, and community growth.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Packages the developer launch assets including SDKs, sample apps, documentation, and announcement content into a coordinated release kit.

## When to Use

- When a new developer product, API, or SDK is approaching launch and assets need to be bundled.
- When a major version release requires coordinated updates across documentation, samples, and announcement channels.
- When a partner integration launch needs a developer-facing asset package.
- When a conference or event keynote will announce developer capabilities and supporting materials must be ready.

## Workflow

1. **Inventory required assets**: List all assets needed for launch (SDK packages, API reference, quickstart guide, sample apps, changelog, blog post, social content, demo video, migration guide). Deliverable: asset checklist with owners and deadlines.
2. **Coordinate with engineering**: Confirm SDK and API readiness, version numbers, breaking changes, and deprecation notices. Deliverable: engineering sign-off document.
3. **Prepare documentation**: Ensure all docs are updated, reviewed, and published to staging (quickstart, reference, tutorials, migration guide). Deliverable: documentation readiness confirmation.
4. **Build sample applications**: Create or update sample apps that demonstrate key use cases and work with the released SDK version. Deliverable: tested sample apps in target languages.
5. **Draft announcement content**: Write the launch blog post, release notes, social media posts, and email to the developer newsletter. Deliverable: announcement content package.
6. **Assemble and test the kit**: Bundle all assets, verify links work, samples compile, and docs match the released API. Run through the complete developer first-run experience. Deliverable: tested launch kit.
7. **Execute launch sequence**: Publish assets in the correct order (SDK, docs, blog, social, email) according to the GTM timeline. Deliverable: launch execution confirmation with publish timestamps.

## Anti-Patterns

- **Last-minute documentation**: Starting documentation updates after the SDK is already released. *Why*: Developers arriving on launch day find incomplete or outdated docs, creating a negative first impression that is amplified by launch traffic volume.
- **Untested samples**: Shipping sample apps that were not tested against the final SDK version. *Why*: Broken samples are the single fastest way to destroy developer trust; developers who cannot run the sample will not try the product.
- **Uncoordinated publish sequence**: Publishing the blog announcement before the SDK or docs are live. *Why*: Excited developers click through to assets that do not exist yet, creating confusion and support burden during the highest-traffic window.

## Output

**On success**: Produces a complete developer launch kit containing SDK packages, documentation, sample apps, announcement content, and a launch execution log. Delivered to developer relations, marketing, and engineering teams.

**On failure**: Report which assets are not ready, what blocks completion, and recommend a revised launch date or partial launch strategy. Every error must be actionable.

## Related Skills

- [`developer-gtm-planner`](../developer-gtm-planner/SKILL.md) — Launch assets must align with the GTM channel strategy and messaging.
- [`api-documentation-designer`](../../technical-writer/api-documentation-designer/SKILL.md) — API documentation structure designed here feeds into the launch documentation package.
- [`developer-experience-reviewer`](../developer-experience-reviewer/SKILL.md) — Launch kit should be validated through a developer experience review before release.
