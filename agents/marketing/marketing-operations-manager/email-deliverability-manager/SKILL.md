---
name: email-deliverability-manager
description: >
  This skill manages sender reputation, list hygiene, and deliverability across all marketing email.
  Use when deliverability rates drop, when onboarding a new sending domain, or when running
  quarterly list hygiene. Also consider when bounce rates spike or spam complaints increase.
  Suggest when a major email campaign is planned and deliverability has not been audited recently.
department: marketing
agent: marketing-operations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../martech-stack-manager/SKILL.md
  - ../campaign-analytics-reporter/SKILL.md
---

# email-deliverability-manager

## Agent: Marketing Operations Manager

L2 marketing operations manager (1x) responsible for martech stack, lead scoring, campaign analytics, attribution modelling, and email deliverability.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Manages sender reputation, list hygiene, authentication protocols, and inbox placement rates across all marketing email to maximize deliverability and protect domain reputation.

## When to Use

- When inbox placement rates or open rates drop below established baselines.
- When onboarding a new sending domain or IP address that requires warmup.
- When quarterly list hygiene is due to suppress invalid, bounced, or unengaged contacts.
- When bounce rates spike or spam complaint rates approach ISP thresholds.

## Workflow

1. **Audit current deliverability**: Pull inbox placement rates, bounce rates, spam complaint rates, and blacklist status across all sending domains. Compare against the health thresholds in [`references/framework.md`](references/framework.md). Deliverable: deliverability health scorecard using [`assets/deliverability-health-report-template.md`](assets/deliverability-health-report-template.md).
2. **Verify authentication**: Confirm SPF, DKIM, and DMARC records meet the authentication protocol standards in [`references/framework.md`](references/framework.md). Fix any misalignment or failures. Deliverable: authentication compliance section of the report.
3. **Execute list hygiene**: Apply the list hygiene cadence from [`references/framework.md`](references/framework.md) — suppress hard bounces, remove spam traps, sunset unengaged contacts per the 90-day rule, and remove role-based addresses. Deliverable: cleaned list with suppression log.
4. **Monitor sender reputation**: Check domain and IP reputation using the ISP-specific tools in [`references/framework.md`](references/framework.md). If reputation degrades, execute the remediation steps in order. Deliverable: reputation status per ISP in the health report.
5. **Optimize sending practices**: Review send frequency, segmentation, and warmup status against the domain warmup schedule in [`references/framework.md`](references/framework.md). Implement throttling for large sends. Deliverable: updated sending best practices document.

## Anti-Patterns

- **Ignoring unengaged contacts**: Continuing to email contacts who have not engaged in 90+ days. *Why*: ISPs interpret low engagement as spam signal, degrading sender reputation for the entire domain and hurting deliverability to engaged contacts.
- **Skipping domain warmup**: Sending at full volume from a new domain or IP without a gradual warmup period. *Why*: ISPs flag sudden volume spikes from unknown senders as spam, potentially blacklisting the domain before it establishes reputation.
- **Authentication neglect**: Failing to maintain SPF, DKIM, and DMARC records as sending infrastructure changes. *Why*: broken authentication causes emails to land in spam or be rejected outright, regardless of content quality.

## Output

**On success**: Produces a deliverability health scorecard, authentication compliance report, cleaned suppression log, and updated sending best practices. Inbox placement rates meet or exceed benchmarks. Delivered to marketing operations team and VP Marketing.

**On failure**: Report which deliverability issues were identified (blacklisting, authentication failures, reputation degradation), what remediation was attempted, and escalate unresolved issues with specific ISP contact steps.

## Related Skills

- [`martech-stack-manager`](../martech-stack-manager/SKILL.md) — Email sending infrastructure and ESP configuration are managed by the martech stack.
- [`campaign-analytics-reporter`](../campaign-analytics-reporter/SKILL.md) — Email campaign performance metrics feed into the weekly report and flag deliverability issues.
- [`lead-scoring-model-builder`](../lead-scoring-model-builder/SKILL.md) — Email engagement signals are a key input to lead scoring models.
