# Transactional Email Template Library

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Lifecycle Email Marketing Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | transactional-email-designer |

## Executive Summary

[2-3 sentences summarising the template library scope, number of templates, and deliverability standards applied.
GUIDANCE: Lead with the number of transactional email types covered and the inbox placement target.]

## Template Inventory

[Complete list of transactional email templates with category and trigger.

GUIDANCE:
- Good: Table with template name, category (authentication/confirmation/notification/billing/system), trigger event, send priority, and secondary CTA (yes/no)
- Bad: "Various email templates"
- Format: Inventory table with one row per template type]

## Template Specifications

[Per-template design specifications.

GUIDANCE:
- Good: For each template: subject line pattern, preheader text, body structure (sections in order), primary content block, secondary CTA if applicable, and plain-text fallback structure
- Bad: "Standard email layout"
- Format: One subsection per template with field-level specifications]

## Sender Configuration

[Authentication and domain setup details.

GUIDANCE:
- Good: Table with sending domain, SPF record, DKIM selector, DMARC policy, and bounce handling rules
- Bad: "Set up email authentication"
- Format: Configuration table with specific values or patterns for each standard]

## Rendering Test Results

[Cross-client rendering verification.

GUIDANCE:
- Good: Table with email client (Gmail, Outlook, Apple Mail, mobile), test result (pass/fail), and notes on any rendering fixes applied
- Bad: "Tested on major clients"
- Format: Test matrix with at least 6 clients/devices]

## Recommendations

[Prioritized actions for template deployment and monitoring.

GUIDANCE: Each recommendation should be:
- Specific (not "improve emails" but "add BIMI record for transactional subdomain to display brand logo in Gmail by Q2")
- Actionable (assignable to email ops, engineering, or brand)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Design principles applied, accessibility standards referenced, and rendering testing tools used.]

### B. Supporting Data

[Current deliverability metrics, email client market share data for the user base, and any brand guidelines referenced.]
