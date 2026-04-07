# Feedback Loop Design

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Operations Analyst] |
| Scope | [Which product areas / teams this loop covers] |
| Version | [1.0] |
| Skill | feedback-loop-formaliser |

## Problem Statement

[1-2 sentences describing how feedback is currently lost or misrouted, and the business impact.
GUIDANCE: Quantify if possible — "Support tickets tagged 'feature request' are never reviewed by product; estimated 40+ signals per month going unactioned."]

## Signal Source Inventory

[Table of all feedback channels included in this loop.

GUIDANCE:
- Good: Table with Source, Signal Type, Capture Tool, Current State (Active/Broken/Missing), Owner
- Bad: "We get feedback from many places"
- Format: One row per source; flag gaps where capture is missing or inconsistent]

## Classification Schema

[The tagging taxonomy to be applied to all signals.

GUIDANCE: Adapt the standard taxonomy (Type / Severity / Segment / Frequency) to this product's context. Add product-specific types if needed.]

## Routing Matrix

[Who receives each type of signal and within what SLA.

GUIDANCE: Use the standard routing rules as defaults. Document any deviations with rationale.]

| Signal Type | Severity | Route To | SLA | Escalation Path |
|-------------|---------|---------|-----|----------------|
| Bug | Critical | | | |
| Bug | High/Med | | | |
| Feature Request | Any | | | |
| Churn Risk | Any | | | |
| Positive Signal | Any | | | |

## Tooling Setup

[The tools and integrations required to run this loop.

GUIDANCE: Specify helpdesk, CRM, survey platform, and any automation (e.g., Zapier/Make workflow, Slack channel, Notion database). Include configuration notes for setup.]

## Loop Health Baseline

[Current state measurements before formalisation, used to track improvement.

| Metric | Baseline | Target | Measurement Method |
|--------|---------|--------|-------------------|
| Capture rate | | 100% | |
| Classification lag (hours) | | <24h | |
| Routing compliance | | >90% | |
| Closure rate (30-day) | | >80% | |

## Review Cadence

| Review Type | Cadence | Owner | Output |
|-------------|---------|-------|--------|
| Signal triage | Weekly | Ops Analyst | Classified + routed backlog items |
| Loop health check | Monthly | PM + Ops | Health metric report |
| Taxonomy review | Quarterly | PM | Updated classification schema |

## Rollout Plan

[Steps to transition from current state to formalised loop.

GUIDANCE: List by week — Week 1: tooling setup; Week 2: team training; Week 3: soft launch; Week 4: full activation and baseline measurement.]
