# Framework: Support Pre-Briefing (Content)

Defines the methodology for briefing the support team on UX copy and terminology changes before a product release, ensuring consistent language between support agents and the product.

## Change Classification Matrix

### Change Type Impact Assessment

| Change Type | Support Impact Level | Briefing Lead Time Required |
|------------|--------------------|-----------------------------|
| Feature rename (product-wide) | Critical — users will reference old name | 5+ business days before release |
| Label / button text change | High — affects how users describe their navigation | 3+ business days |
| Error message rewrite | High — affects how users describe their problem | 3+ business days |
| Terminology addition (new term) | Medium — support must know the term before users ask | 2+ business days |
| Copy tone/style update | Low — no user-facing vocabulary change | 1 business day |
| Help article update | Medium — links and article names may change | 2+ business days |

### Change Inventory Fields

For each change, capture:

| Field | Description |
|-------|-------------|
| Surface | Where the copy appears (onboarding / settings / billing / navigation) |
| Element type | Button / heading / error / label / notification / empty state |
| Old copy | Exact previous string as it appeared in the product |
| New copy | Exact new string as it will appear in the product |
| Change type | Renamed / Reworded / Added / Removed |
| User visibility | Will users see this on first login, or only in specific workflows? |
| Support trigger | Will users contact support about this change? Yes / Maybe / Unlikely |

## Support Impact Assessment Model

### Trigger Mapping

For each change with support trigger = Yes or Maybe, identify:

| Trigger Type | What to Document in Brief |
|-------------|--------------------------|
| User confusion about new name | Old term → new term mapping; how to confirm with user which they mean |
| User cannot find moved feature | Old navigation path → new navigation path |
| User sees new error message | What the error means; step-by-step resolution guide |
| User asks about removed copy | Why it was removed; what the current state is |

### Anticipated User Phrasing

Document how users are likely to describe each change when contacting support. Users use the old vocabulary for months after a rename.

| Change | Old User Phrasing (likely) | New Product Vocabulary | Mapping Note |
|--------|--------------------------|----------------------|--------------|
| [Feature renamed from X to Y] | "Where is [X]?" | "[Y]" | "They're asking about [Y]" |

## Brief Structure

### Section Order

| Section | Purpose | Required |
|---------|---------|---------|
| Release summary | Date, version, one-line description of what's shipping | Yes |
| Copy changelist | Table of all copy changes (see inventory fields) | Yes |
| Deprecated term mapping | Old terms users will still use + current equivalent | Yes |
| Support impact assessment | Which changes trigger support contacts and why | Yes |
| Suggested responses | Pre-written response templates for anticipated questions | Yes — for high-impact changes |
| Help article updates | Links to updated/new articles with change summary | Yes if articles changed |
| Brief delivery date | When support received this and who confirmed | Yes |

### Suggested Response Template Format

For each high-impact change, provide a response template support agents can adapt:

```
Context: [Describe the scenario — user has contacted support about X]
Agent response template:
  "Thanks for reaching out. [Acknowledge what they're asking about using their vocabulary].
  In the latest update, [explain what changed in one sentence].
  To [achieve their goal], you can now [describe the new path/action].
  [Optional: link to updated help article]"
```

## Quality Gates

Before delivering a brief to the support team:

| Gate | Check |
|------|-------|
| Completeness | All copy changes in the release are in the changelist |
| Old-term coverage | Every renamed term has a deprecated-term mapping entry |
| Response templates | Every change with trigger = Yes has a response template |
| Help article links | All updated articles are live or staged for preview |
| Timing | Brief delivered at least the minimum lead time before release |
| Acknowledgement | Support team lead has confirmed receipt |

## Brief Versioning

When a brief requires updates after initial delivery:

- Append "-v2", "-v3" to the brief document version.
- Highlight changes from the previous version in bold or a "What changed since v1" section.
- Re-notify support lead when a material update is issued.
