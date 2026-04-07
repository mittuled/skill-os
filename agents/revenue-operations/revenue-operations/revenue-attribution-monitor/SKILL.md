---
name: revenue-attribution-monitor
description: >
  This skill monitors multi-touch revenue attribution to ensure accurate channel and campaign credit.
  Use when asked to track marketing attribution, validate campaign ROI, or audit attribution data.
  Also consider when marketing and sales disagree on lead source credit.
  Suggest when attribution data is missing or inconsistent in pipeline reports.
department: revenue-operations
agent: revenue-operations
version: 1.0.0
complexity: medium
related-skills: []
---

# revenue-attribution-monitor

## Agent: Revenue Operations

L1 revenue operations function (1x) reporting to the COO, responsible for CRM infrastructure, billing, attribution, and funnel analytics. Maintains operational neutrality across all CBO revenue functions.

Department ethos: [ideal-revenue-operations.md](../../../../departments/revenue-operations/ideal-revenue-operations.md)

## Skill Description

The revenue attribution monitor tracks and validates multi-touch attribution data across channels and campaigns, ensuring accurate credit assignment so marketing and sales can make informed investment decisions.

## When to Use

- When marketing needs validated attribution data to justify campaign spend or reallocate budget.
- When attribution data in the CRM is incomplete, inconsistent, or disputed between teams.
- When a new channel or campaign launches and attribution tracking needs to be configured.
- When quarterly business reviews require accurate channel-level revenue contribution data.

## Workflow

1. **Define the attribution model**: Select and document the attribution model (first-touch, last-touch, linear, or custom multi-touch) aligned with business goals. Deliverable: attribution model specification.
2. **Configure tracking**: Ensure UTM parameters, tracking pixels, and CRM source fields are correctly configured across all channels. Deliverable: tracking configuration audit report.
3. **Monitor data quality**: Run periodic checks for missing attribution data, broken UTM links, and untagged leads. Deliverable: data quality report with issue counts.
4. **Validate attribution accuracy**: Cross-reference attributed revenue with actual deal data to identify misattribution. Deliverable: attribution validation report.
5. **Report and recommend**: Produce attribution reports by channel and campaign with recommendations for investment reallocation. Deliverable: attribution dashboard and recommendation memo.

## Anti-Patterns

- **Single-touch in a multi-touch world**: Using first-touch or last-touch attribution when the buyer journey involves multiple meaningful touchpoints. *Why*: single-touch models misallocate credit and cause underinvestment in mid-funnel channels.
- **Set-and-forget tracking**: Configuring attribution once and never auditing for data quality. *Why*: tracking breaks silently as campaigns change, UTM conventions drift, and new channels are added without tagging.
- **Attribution as a weapon**: Using attribution data to argue for departmental credit rather than to optimise the overall funnel. *Why*: politicised attribution undermines trust in the data and distorts investment decisions.

## Output

**On success**: Accurate, validated attribution data by channel and campaign, a data quality report confirming tracking integrity, and actionable recommendations for marketing investment reallocation.

**On failure**: Report which channels have attribution gaps (e.g., missing UTM parameters, broken integrations), what data was validated, and provide specific remediation steps for each gap.

## Related Skills

- [`revenue-funnel-analyst`](../revenue-funnel-analyst/SKILL.md) -- funnel analysis uses attribution data to understand conversion by channel.
- [`crm-setup-v1`](../crm-setup-v1/SKILL.md) -- CRM setup configures the source fields and integrations that attribution depends on.
