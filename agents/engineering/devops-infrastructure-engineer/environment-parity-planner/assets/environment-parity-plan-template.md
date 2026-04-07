# Environment Parity Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | environment-parity-planner |
| Environments in Scope | [dev / staging / production] |

## Executive Summary

[2-3 sentences summarizing the current state of environment parity, the most critical drift found, and the primary outcome of this plan.
GUIDANCE: Lead with the risk — "Staging and production have diverged on 3 critical dimensions including runtime version and security group rules, creating a high probability of production-only failures. This plan establishes shared IaC modules and automated drift detection to eliminate these gaps."]

## Parity Inventory

[List all environment-specific differences discovered during inventory.

GUIDANCE:
- Good: "Database version: staging=PostgreSQL 14.8, production=PostgreSQL 15.2 — UNINTENTIONAL DRIFT, remediate immediately"
- Bad: "Database configuration differs"
- Format: Table with dimension, dev value, staging value, production value, classification (intentional/drift), risk]

| Dimension | Dev | Staging | Production | Classification | Risk Level |
|-----------|-----|---------|------------|----------------|------------|
| [Dimension] | [value] | [value] | [value] | [Intentional / Drift] | [Critical/High/Medium/Low] |

## Parity Policy

[Define which dimensions must be identical and which may differ with justification.

GUIDANCE:
- Good: "Runtime versions (OS, language, container base image) must be identical across all environments. Instance sizes may differ: dev=t3.medium, staging=m5.xlarge, production=m5.4xlarge."
- Bad: "Environments should be as similar as possible."]

### Must-Match Dimensions

[List dimensions that are non-negotiable for parity, with remediation required if they differ]

### Permitted Variances

| Dimension | Dev Value | Staging Value | Production Value | Business Justification |
|-----------|-----------|---------------|-----------------|----------------------|
| [Dimension] | [value] | [value] | [value] | [Why this difference is acceptable] |

## IaC Shared Module Structure

[Describe how the IaC is or will be structured to enforce parity through shared modules.

GUIDANCE:
- Good: Show the directory structure with shared modules and environment-specific variable files (see references/framework.md for the pattern)
- Bad: "We will use Terraform"]

## Drift Detection Configuration

[Specify the automated drift detection setup: what is checked, how often, and where alerts go.

GUIDANCE:
- Good: "Daily Driftctl scan comparing terraform state against cloud resources, results posted to #infra-drift Slack channel. PR gate: terraform plan must show 0 unexpected changes before merge."
- Bad: "We will check for drift regularly"]

| Check | Frequency | Tool | Alert Target | Severity |
|-------|-----------|------|-------------|---------|
| [Check name] | [Daily/Weekly/Per-PR] | [Tool] | [Channel/email] | [Critical/High/Medium] |

## Recommendations

[Prioritized list of actions to achieve and maintain parity.

GUIDANCE:
- P1: [Immediate drift that poses production incident risk — specific action, owner, deadline]
- P2: [Configuration gap that could cause "works in staging, fails in prod" issues — specific action]
- P3: [Process improvement to prevent future drift — specific action]]

## Appendices

### A. Drift Audit Log

[List of all drift items found during inventory, their current state, and remediation status]

### B. Intentional Difference Justification Register

[Each permitted variance with the approver's name, date of approval, and review schedule]
