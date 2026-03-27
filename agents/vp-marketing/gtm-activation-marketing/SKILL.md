---
name: gtm-activation-marketing
description: >
  This skill activates the GTM plan at launch by coordinating execution across all marketing channels.
  Use when a product launch date is confirmed, a major campaign is going live, or a market expansion
  requires synchronized channel activation. Also consider when a competitive move demands an
  accelerated response campaign. Suggest when a GTM plan exists but no activation timeline has been set.
department: marketing
agent: vp-marketing
version: 1.0.0
complexity: complex
related-skills:
  - ../gtm-planner-marketing/SKILL.md
  - ../demand-gen-planner/SKILL.md
triggers:
  - "activate the GTM plan"
  - "coordinate the launch across channels"
  - "kick off the marketing campaign"
  - "execute the go-to-market"
---

# gtm-activation-marketing

## Agent: VP Marketing

L1 marketing leader (1x) reporting to the CBO, responsible for GTM planning, demand generation strategy, and marketing activation across all channels.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Activates the GTM plan at launch by coordinating execution across all marketing channels, ensuring synchronized messaging, asset delivery, and campaign go-live.

## When to Use

- When a product launch date is confirmed and marketing channels need synchronized activation.
- When a major campaign requires orchestrated go-live across paid, owned, and earned media.
- When a competitive threat demands a rapid coordinated marketing response across channels.
- When sales enablement materials, landing pages, and ad creatives must ship in lockstep with a launch.

## Workflow

1. **Lock activation timeline**: Convert the GTM plan into a day-by-day activation calendar with channel-specific deadlines. Identify the critical path and flag dependencies. Deliverable: activation timeline with owners and due dates.
2. **Confirm asset readiness**: Audit all required assets -- landing pages, ad creatives, email sequences, blog posts, sales decks, social copy. Flag gaps and assign owners with hard deadlines. Deliverable: asset readiness checklist with status per item.
3. **Brief channel owners**: Conduct activation briefings with each channel lead (paid, content, social, email, PR). Confirm messaging, audience segments, UTM conventions, and budget. Deliverable: channel activation briefs.
4. **Stage campaigns**: Load campaigns into platforms in draft/paused state. QA targeting, creative, tracking pixels, and attribution tags. Deliverable: staged campaigns ready for one-click activation.
5. **Execute launch sequence**: Activate channels in planned sequence. Monitor real-time dashboards for delivery issues, broken links, or tracking failures. Escalate blockers within 30 minutes. Deliverable: live campaigns across all channels.
6. **Run 48-hour war room**: Monitor launch performance in the first 48 hours. Track impressions, CTR, form fills, and early MQL signals. Adjust bids, budgets, or messaging in real time. Deliverable: 48-hour launch performance snapshot.
7. **Conduct launch retrospective**: Within one week post-launch, compile channel performance vs. targets. Document what worked, what broke, and process improvements. Deliverable: launch retrospective document.

## Anti-Patterns

- **Big-bang without staging**: Pushing campaigns live without staging and QA in platform. *Why*: broken tracking, wrong audiences, or typos in live campaigns burn budget and damage brand in the first critical hours.
- **Sequential channel activation**: Launching channels one at a time over weeks instead of coordinated activation. *Why*: staggered launches dilute the market impact and create inconsistent buyer experiences.
- **Skipping the war room**: Treating launch day as set-and-forget. *Why*: the first 48 hours surface 80% of execution issues; unmonitored launches compound errors silently.
- **Messaging drift across channels**: Allowing each channel to freestyle messaging instead of enforcing the approved positioning. *Why*: inconsistent messaging confuses buyers and fragments the brand narrative at the highest-visibility moment.

## Output

**On success**: Produces a completed activation timeline, asset readiness checklist, channel activation briefs, and a launch retrospective document. All channels go live on schedule with consistent messaging and functional tracking. Delivered to CBO, product marketing, and sales leadership.

**On failure**: Report which channels failed to activate on time, what assets were missing or broken, the impact on launch coverage, and immediate remediation steps. Escalate tracking or attribution failures to marketing operations.

## Related Skills

- [`gtm-planner-marketing`](../gtm-planner-marketing/SKILL.md) — Produces the GTM plan that this skill activates into market.
- [`demand-gen-planner`](../demand-gen-planner/SKILL.md) — Provides the channel investment plan and lead targets that activation executes against.
- [`press-release-writer`](../../pr-communications-manager/press-release-writer/SKILL.md) — Coordinates the earned media component of launch activation.
- [`content-marketing-operations`](../../content-marketer/content-marketing-operations/SKILL.md) — Produces the content assets required for activation.
