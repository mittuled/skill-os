# Integration Guide: `[Integration Name]`

**Status**: `[ ] GA  [ ] Beta  [ ] Early Access  [ ] Deprecated (EOL: YYYY-MM-DD)`
**Product Version**: `[Minimum version required]`
**Third-Party Version**: `[Minimum version of external system required]`
**Last Updated**: `YYYY-MM-DD`
**Reviewed By**: `[Implementation Lead]`

---

## Overview

**What this integration does**:
```
[1–2 sentences describing what data is synced and in which direction.
Example: "This integration syncs contact and deal data from HubSpot CRM into [Product],
allowing sales signals to trigger automated workflows without manual data entry."]
```

**Direction**: `[ ] One-way ([Source] → [Target])  [ ] Bidirectional`

**Sync Frequency**: `[Real-time / Every ## minutes / Daily / Manual trigger only]`

**Data Synced**:
| Object | Direction | Notes |
|--------|-----------|-------|
| `[e.g., Contacts]` | `[Source → Target]` | `[Notes on what fields]` |
| `[e.g., Deals]` | `[Source → Target]` | `[Notes]` |

---

## Prerequisites

### Plan Requirements
- **Product plan required**: `[Plan tier that includes this integration]`
- **Third-party plan required**: `[Minimum plan level in the external system, if applicable]`

### Access Requirements
- `[Who in the customer organisation needs to configure this: IT Admin / CRM Admin / etc.]`
- `[Any admin role or permission level required in the third-party system]`

### Technical Requirements
- `[Any network or firewall rules required]`
- `[IP allowlist addresses if applicable]`
- `[Any browser or OS requirements]`

---

## Step-by-Step Setup

### Step 1: `[Action — e.g., Generate API Credentials in [Third-Party System]]`

`[Instruction text. Be specific about navigation paths and field values.]`

```
Navigation: [Third-Party System] → Settings → API → Create Token
Token type: [Required token type]
Scopes required: [List exact permission scopes]
```

`[Screenshot placeholder: API credentials page in [Third-Party System]]`

---

### Step 2: `[Action — e.g., Open the Integration Settings in [Product]]`

`[Instruction text]`

```
Navigation: [Product] → Settings → Integrations → [Integration Name]
```

---

### Step 3: `[Action — e.g., Enter Credentials and Authenticate]`

`[Instruction text]`

Field values to enter:
| Field | Where to Get It | Format |
|-------|----------------|--------|
| `API Key / Client ID` | Step 1 output | `[Format description]` |
| `[Other field]` | `[Source]` | `[Format]` |

---

### Step 4: `[Action — e.g., Configure Sync Settings]`

`[Instruction text covering the main configuration options]`

| Setting | Recommended Value | Notes |
|---------|------------------|-------|
| `[Setting name]` | `[Value]` | `[Why this value]` |

---

### Step 5: Test the Integration

1. `[How to trigger a test sync]`
2. `[Where to verify the data appeared correctly]`
3. `[What a successful test looks like]`

**Verification checklist**:
- [ ] Test record synced from `[Source]` to `[Target]`
- [ ] Field mapping is correct (spot-check key fields)
- [ ] Sync status shows "Active" or equivalent
- [ ] No errors in integration log

---

## Data Mapping Reference

| `[Source System]` Field | `[Product]` Field | Type | Notes |
|-------------------------|-------------------|------|-------|
| `[Field Name]` | `[Field Name]` | `String / Number / Date` | `[Transformation applied, if any]` |
| `[Field Name]` | `[Field Name]` | `String` | `[Notes]` |

**Fields not synced**: `[List any fields in the source system that are intentionally not mapped]`

---

## Known Limitations

| Limitation | Details | Workaround |
|-----------|---------|-----------|
| `[Limitation description]` | `[Specifics]` | `[Workaround if available, or "None — contact support"]` |

---

## Troubleshooting

### Error: `[Error message or code]`
**Cause**: `[What typically causes this error]`
**Resolution**: `[Step-by-step fix]`

---

### Error: `[Error message or code]`
**Cause**: `[Cause]`
**Resolution**: `[Fix]`

---

### Error: `[Error message or code]`
**Cause**: `[Cause]`
**Resolution**: `[Fix]`

---

### Integration Not Syncing (No Errors Shown)
1. Check that the integration is enabled and status is Active
2. Verify API credentials have not expired (rotate and reconnect if needed)
3. Check third-party system for API usage limits or quota errors
4. Check that the record meets sync filter criteria
5. Contact support with integration log export if issue persists

---

## Related Resources

- [Integration Documentation Standards](../references/integration-documentation-standards.md)
- `[Link to third-party system's API documentation]`
- `[Link to support escalation process]`

---

*Template version 1.0 — Implementation / Implementation Lead*
