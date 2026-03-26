---
name: earned-media-monitor
description: >
  This skill tracks press coverage, share of voice, and sentiment vs. competitors.
  Use when producing weekly or monthly media coverage reports, when a PR campaign needs
  performance measurement, or when sentiment shifts signal a brewing reputation issue.
  Also consider when competitor coverage spikes unexpectedly.
  Suggest when earned media goes untracked for more than two weeks.
department: marketing
agent: pr-communications-manager
version: 1.0.0
complexity: simple
related-skills:
  - ../crisis-communications-planner/SKILL.md
  - ../media-relationship-builder/SKILL.md
---

# earned-media-monitor

## Agent: PR and Communications Manager

L2 PR and communications manager (1x) responsible for earned media, press relationships, crisis communications, thought leadership programme, and executive visibility.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Tracks press coverage, share of voice, and sentiment versus competitors to measure PR effectiveness and detect emerging reputation risks.

## When to Use

- When producing the weekly or monthly earned media report for marketing leadership.
- When a PR campaign or press release needs post-launch coverage and sentiment analysis.
- When competitor media coverage spikes and requires context on what is driving the attention.

## Workflow

1. **Collect coverage data**: Pull all brand mentions, competitor mentions, and industry keyword hits from media monitoring tools. Categorize by outlet tier, topic, and sentiment. Deliverable: raw coverage dataset for the reporting period.
2. **Calculate share of voice**: Compute the company's share of voice relative to named competitors by mention count, outlet authority, and estimated reach. Deliverable: share of voice comparison table with trend line.
3. **Assess sentiment and themes**: Classify coverage as positive, neutral, or negative. Identify dominant themes and narratives. Flag any negative sentiment trends that may require response. Deliverable: sentiment analysis with theme breakdown.

## Anti-Patterns

- **Counting clips without context**: Reporting raw mention counts without weighting by outlet authority, reach, or sentiment. *Why*: ten mentions in low-authority blogs are not equivalent to one feature in a tier-one publication.
- **Ignoring competitor coverage**: Tracking only own-brand mentions without monitoring competitor media activity. *Why*: share of voice is relative; a stable mention count means decline if competitors are growing coverage.

## Output

**On success**: Produces an earned media report containing coverage summary, share of voice comparison, sentiment analysis, and flagged items requiring attention. Delivered weekly to VP Marketing and PR team.

**On failure**: Report which data sources were unavailable (monitoring tool gaps, missing competitor keywords), what coverage the partial report includes, and recommend tool or keyword configuration changes.

## Related Skills

- [`crisis-communications-planner`](../crisis-communications-planner/SKILL.md) — Negative sentiment trends detected here may trigger crisis protocol activation.
- [`media-relationship-builder`](../media-relationship-builder/SKILL.md) — Coverage gaps in target outlets inform where to invest relationship-building effort.
- [`press-release-writer`](../press-release-writer/SKILL.md) — Post-release coverage tracking measures the effectiveness of each press release.
