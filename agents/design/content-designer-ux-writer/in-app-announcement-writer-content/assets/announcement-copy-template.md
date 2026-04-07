# In-App Announcement Copy Document

## Announcement Metadata (internal — remove before implementation)

| Field | Value |
|-------|-------|
| Announcement ID | [e.g. ANN-0031] |
| Feature / Change | [e.g. Dashboard redesign] |
| Announcement Type | [New feature / Update / Breaking change / Deprecation / Maintenance / Security] |
| Format | [Banner / Modal / Toast / Tooltip coach mark / Empty state] |
| Target Audience | [All users / Admins only / Free plan users / [Segment name]] |
| Trigger | [On login / Contextual — when user visits [page] / Immediate] |
| First Display Date | [YYYY-MM-DD] |
| Expiry / Removal Date | [YYYY-MM-DD or "Permanent dismiss only"] |
| CTA Destination | [URL or product location] |
| Dismissal Behaviour | [Session dismiss / Permanent dismiss / Mandatory acknowledgement / Auto-expire] |
| Coordinated With | [Support brief ref / Launch narrative ref / Related ANN IDs] |
| Author | [Content Designer name] |
| Created | [YYYY-MM-DD] |

---

## Copy Drafts

### Variant A — Primary

**Format**: [Banner / Modal / Toast / Tooltip / Empty state]

**Headline** (≤ 8 words):
> [e.g. Your dashboard has a new look]

**Body** (≤ character limit for chosen format):
> [e.g. We've redesigned the dashboard to surface your most important metrics at a glance. Your data and settings are unchanged.]

**CTA label** (≤ 4–6 words):
> [e.g. See what's new]

**Dismiss / secondary label** (if applicable):
> [e.g. Maybe later]

**Word count**: [X] / [limit]
**Tone**: [Celebratory / Informational / Urgent / Empathetic]

---

### Variant B — Alt (for A/B testing or format fallback)

**Format**: [Alternative format if primary cannot be implemented]

**Headline**:
> [Alternative headline]

**Body**:
> [Alternative body]

**CTA label**:
> [Alternative CTA]

**Dismiss label**:
> [Alternative dismiss]

**Word count**: [X] / [limit]
**Tone**: [Tone]

---

## Format Annotations

[Describe how the copy should be laid out within the component. This section is for the designer and engineer, not for publication.]

- **Headline**: [Placement, font weight, truncation behaviour at narrow viewport]
- **Body**: [Max lines before "read more" truncation, if applicable]
- **CTA button**: [Colour, icon if any, keyboard focus state label]
- **Dismiss control**: [X icon vs. text label, ARIA label for screen readers]
- **Mobile behaviour**: [Stack vertically / collapse to headline only / full modal]

---

## Tone Rationale

[One paragraph explaining tone choices. This helps reviewers evaluate the copy without guessing intent.]

[e.g. This announcement uses a warm, celebratory tone because the dashboard redesign is a high-effort release with no breaking changes. Users are not required to take any action, so the tone should feel like an invitation rather than an alert. The CTA "See what's new" is intentionally specific — "Learn more" would suggest the feature is complex or risky, which is the wrong signal for a visual update.]

---

## Review Sign-Offs

| Reviewer | Role | Date | Decision | Notes |
|----------|------|------|----------|-------|
| [Name] | [Content Design Lead] | [YYYY-MM-DD] | [Approved / Revision requested] | [e.g. Shorten body to ≤ 40 words for banner format] |
| [Name] | [Designer] | [YYYY-MM-DD] | [Approved / Revision requested] | [e.g. CTA label fits in button; confirm mobile truncation] |
| [Name] | [Engineer] | [YYYY-MM-DD] | [Approved / Revision requested] | [e.g. Dismissal logic confirmed — permanent for this segment] |

---

## Implementation Checklist

- [ ] Copy finalised and approved by Content Design Lead
- [ ] Format and placement confirmed with Designer
- [ ] Dismissal behaviour confirmed with Engineer
- [ ] Audience targeting rules verified
- [ ] Display date and expiry date set in announcement system
- [ ] Support team briefed (ref: [support brief ID])
- [ ] Coordinated with any simultaneous announcements — no overlap
- [ ] Tested in staging environment at narrow (375px), medium (768px), and wide (1280px) viewports
