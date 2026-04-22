---
name: content-engine-builder-pmm
description: >
  This skill builds and operates the content production engine for ongoing PMM content.
  Use when the team needs a repeatable system for producing marketing content at a predictable cadence.
  Also consider when content output is inconsistent or dependent on ad-hoc heroics. Suggest when
  the PMM team is scaling and needs to shift from reactive content creation to a sustainable pipeline.
department: product
agent: pmm-analyst-content-strategist
version: 1.0.0
complexity: medium
related-skills:
  - ga-announcement
  - case-study-extractor-pmm
  - in-app-announcement-writer
triggers:
  - "build content engine"
  - "content strategy engine"
  - "pmm content system"
  - "content pipeline"
  - "content engine"
---

# content-engine-builder-pmm

## Agent: PMM Analyst Content Strategist
L3 PMM analyst and content strategist (multi-instance) responsible for in-app announcements, changelog publishing, case study creation, and content engine operations.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Builds and operates the content production engine for ongoing PMM content, establishing repeatable workflows that turn product knowledge into a steady stream of marketing assets.

## When to Use
- When the PMM team is producing content reactively and needs a systematic pipeline with predictable output cadence
- When a new product line or market segment requires a dedicated content stream that does not yet exist
- When content bottlenecks are delaying launches because there is no standard process for drafting, reviewing, and publishing

## Workflow
1. **Audit existing content operations**: Map current content types, production frequency, contributors, review gates, and distribution channels. Identify bottlenecks, single points of failure, and content gaps by funnel stage. Deliverable: content operations audit with gap analysis and throughput metrics.
2. **Define the content calendar**: Establish a rolling calendar tied to the product roadmap, seasonal campaigns, and sales cycle milestones. Assign content types to time slots and allocate owners. Deliverable: 90-day content calendar with deadlines, owners, and status tracking.
3. **Build templates and style guides**: Create reusable templates for each content type (blog post, one-pager, email sequence, social snippet). Document voice, tone, and formatting standards. Deliverable: template library and style guide published in the shared workspace.
4. **Establish the review pipeline**: Set up a lightweight review workflow with clear roles (drafter, subject-matter reviewer, final approver) and SLA targets for each stage. Deliverable: documented review process with SLAs and escalation paths.
5. **Launch and measure**: Activate the engine by running the first full cycle end-to-end. Track cycle time, publish rate, and content performance metrics. Deliverable: first cycle retrospective with throughput data and improvement backlog.
6. **Iterate quarterly**: Review engine performance against targets each quarter. Retire underperforming content types, add new formats based on channel data, and adjust cadence to match team capacity. Deliverable: quarterly engine health report with recommended adjustments.

## Anti-Patterns
- **Over-engineered process**: Building a heavyweight editorial workflow with excessive approval gates for a small team. *Why*: Process overhead kills velocity; the engine becomes a bottleneck instead of removing one, and contributors route around it.
- **Calendar without capacity**: Filling every slot on the content calendar without verifying that contributors have bandwidth to deliver. *Why*: Missed deadlines erode trust in the system and cause the team to abandon the calendar entirely.
- **Measuring vanity over impact**: Tracking content volume (pieces published) instead of content performance (pipeline influence, engagement, conversion). *Why*: A high-volume engine producing low-impact content wastes resources and crowds out higher-value work.

## Output
**On success**: An operational content engine with a rolling calendar, reusable templates, a documented review pipeline, and quarterly health metrics -- producing PMM content at a predictable cadence aligned to the product roadmap and sales cycle.

**On failure**: Report which components could not be stood up (missing contributors, undefined content types, tooling gaps), what partial infrastructure exists, and recommend a phased plan to close remaining gaps.

## Related Skills
- [`ga-announcement`](../ga-announcement/SKILL.md) — sibling skill under the same agent — combine with ga-announcement for end-to-end coverage
- [`case-study-extractor-pmm`](../case-study-extractor-pmm/SKILL.md) — sibling skill under the same agent — combine with case-study-extractor-pmm for end-to-end coverage
- [`in-app-announcement-writer`](../in-app-announcement-writer/SKILL.md) — sibling skill under the same agent — combine with in-app-announcement-writer for end-to-end coverage
