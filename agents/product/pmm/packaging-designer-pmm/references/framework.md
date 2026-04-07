# Framework: Product Packaging Design

Reference framework for designing product tiers, naming, and feature allocation from a marketing and positioning perspective.

## Good-Better-Best Packaging Model

The standard SaaS packaging model uses three to four tiers:

| Tier | Purpose | Target Buyer | Characteristics |
|------|---------|-------------|-----------------|
| Starter/Free | Land and activate | Individual contributors, small teams | Self-serve, limited features, low/no cost |
| Professional | Convert and expand | Growing teams, mid-market | Core features, team collaboration, moderate price |
| Business | Primary revenue tier | Established teams, department-level | Advanced features, integrations, admin controls |
| Enterprise | Capture upmarket | Large organisations, compliance-driven | Custom pricing, SSO/SAML, SLAs, dedicated support |

## Packaging Principles

| Principle | Description | Anti-Pattern |
|-----------|-------------|-------------|
| Segment alignment | Each tier serves a distinct buyer segment with different needs | All tiers serve the same buyer at different price points |
| Clear upgrade triggers | One to two obvious reasons to outgrow each tier | Upgrade requires convincing multiple stakeholders of marginal value |
| Feature fencing by value | Gate features that deliver differentiated value, not basic functionality | Gating core features that frustrate users without driving upgrades |
| Simplicity | Three to four tiers maximum; buyer can self-select in under 60 seconds | Five or more tiers with overlapping feature sets |
| Name clarity | Tier names signal the intended buyer without explanation | Abstract names (Alpha, Tier 2, Professional Plus Premium) |

## Feature Allocation Matrix

Allocate features using this decision framework:

| Feature Type | Allocation Rule | Reasoning |
|-------------|----------------|-----------|
| Core (table-stakes) | All tiers | Required for the product to be useful; gating creates frustration |
| Growth triggers | Professional+ | Features buyers need as they scale; natural upgrade conversation |
| Power features | Business+ | Advanced capabilities for mature teams; justifies price premium |
| Compliance/control | Enterprise only | SSO, audit logs, role-based access; required by procurement |
| Nice-to-have | Add-on or highest tier | Valuable but not essential; do not gate core workflow |

## Upgrade Trigger Design

Each tier boundary should have clear triggers:

| Boundary | Trigger Category | Example |
|----------|-----------------|---------|
| Free → Starter | Usage limit | "You have reached 100 records; upgrade to continue" |
| Starter → Professional | Team need | "Invite your team to collaborate" |
| Professional → Business | Scale/control | "Advanced permissions and audit logs for growing teams" |
| Business → Enterprise | Compliance/custom | "SSO, dedicated support, and custom contracts" |

## Naming Guidelines

| Rule | Good | Bad |
|------|------|-----|
| Signal the buyer | "Team", "Business", "Enterprise" | "Silver", "Gold", "Platinum" |
| One word per tier | "Starter" | "Starter Professional Plan" |
| Consistent pattern | All audience-based or all capability-based | Mix of audience ("Team") and capability ("Advanced") |
| Avoid superlatives | "Professional" | "Ultimate", "Supreme", "Maximum" |

## Packaging Comparison Table Rules

1. List 5-8 features per tier (not every feature)
2. Highlight differentiating features with a visual marker
3. Use checkmarks for included; dashes for excluded; "Add-on" for optional
4. Include the upgrade trigger feature prominently at each tier boundary
5. Show pricing with both monthly and annual options

## Packaging Validation Questions

Ask sales before finalising:

1. Can a buyer self-select the right tier in under 60 seconds?
2. Do the upgrade triggers match how deals actually close?
3. Are any deal-closing features in the wrong tier?
4. Does the enterprise tier include everything procurement requires?
5. Is any tier "dead" (nobody buys it or everybody skips past it)?
