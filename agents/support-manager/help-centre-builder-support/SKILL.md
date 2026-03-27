---
name: help-centre-builder-support
description: >
  This skill builds the help centre structure and initial content to enable customer self-service.
  Use when asked to create a knowledge base, set up help documentation, or launch self-service support.
  Also consider when support ticket volume on repetitive questions is high.
  Suggest when the team is preparing for a product launch and no help centre exists.
department: customer-support
agent: support-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "build the help center"
  - "create a knowledge base"
  - "set up self-service support docs"
  - "launch the help centre"
---

# help-centre-builder-support

## Agent: Support Manager

L1 support manager (1x) reporting to the COO, responsible for support runbooks, help centre, incident response planning, and support activation. Owns queue management, SLA adherence, and support tooling.

Department ethos: [ideal-customer-support.md](../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The help centre builder creates the help centre information architecture, writes foundational articles, and configures the self-service portal so customers can resolve common issues without filing a ticket.

## When to Use

- When the product is approaching launch and no customer-facing help centre exists.
- When support ticket analysis reveals that more than 30% of tickets are answerable by documentation.
- When a major feature release introduces new workflows that customers need to learn independently.
- When the team migrates to a new help centre platform and content must be restructured.

## Workflow

1. **Audit existing content**: Inventory all existing documentation, FAQs, and internal runbooks that could become customer-facing. Deliverable: content audit spreadsheet.
2. **Define taxonomy**: Create a category and subcategory structure based on product areas and common customer journeys. Deliverable: help centre sitemap.
3. **Prioritise articles**: Rank articles by ticket deflection potential using historical ticket theme data. Deliverable: prioritised article backlog.
4. **Draft foundational articles**: Write the top-priority articles using a consistent template (title, problem statement, step-by-step solution, related articles). Deliverable: draft article set.
5. **Configure the portal**: Set up the help centre platform with branding, search, navigation, and article publishing workflow. Deliverable: configured help centre environment.
6. **Review and publish**: Route articles through internal review, incorporate feedback, and publish the initial article set. Deliverable: live help centre with published articles.
7. **Measure baseline**: Establish baseline metrics for article views, search queries with no results, and ticket deflection rate. Deliverable: help centre analytics dashboard.

## Anti-Patterns

- **Building without ticket data**: Creating articles based on assumptions rather than actual ticket themes. *Why*: articles that do not address real customer pain points fail to deflect tickets and waste authoring effort.
- **Flat taxonomy**: Dumping all articles into a single category without structure. *Why*: customers cannot navigate a flat list, so search becomes the only path, and poor search queries yield no results.
- **Launch and forget**: Publishing articles without a maintenance cadence. *Why*: stale articles erode customer trust and generate tickets from users who followed outdated instructions.

## Output

**On success**: A live help centre with a defined taxonomy, a published set of foundational articles prioritised by ticket deflection potential, and a baseline analytics dashboard tracking views and deflection rate.

**On failure**: Report which articles could not be completed (missing product information, unclear workflows), what was attempted, and recommend specific subject-matter-expert reviews to unblock content.

## Related Skills

- [`support-runbook-builder`](../support-runbook-builder/SKILL.md) -- internal runbooks often supply source material for customer-facing help articles.
- [`ticket-theme-analyst`](../../support-agent/ticket-theme-analyst/SKILL.md) -- ticket theme analysis identifies which help articles to prioritise.
- [`help-content-reviewer`](../../support-agent/help-content-reviewer/SKILL.md) -- reviews help centre content for accuracy after product changes.
