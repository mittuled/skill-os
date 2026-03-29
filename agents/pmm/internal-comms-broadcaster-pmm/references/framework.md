# Framework: Internal Communications Broadcasting

Reference framework for structuring and distributing internal PMM communications effectively.

## Update Classification Matrix

| Update Type | Urgency | Distribution Channel | Audience | Response Expected |
|-------------|---------|---------------------|----------|-------------------|
| Competitive alert | High | Team channel @-mention + dedicated message | Sales, CS | Acknowledge within 4 hours |
| Positioning change | High | Dedicated all-hands slot + team channels | All customer-facing teams | Adopt new language within 1 week |
| Launch pre-announcement | Medium | Weekly PMM digest + team channel | Sales, CS, marketing | Review enablement materials |
| Battle card update | Medium | Sales channel + enablement platform notification | Sales | Reference in next deal |
| Pricing/packaging change | High | Dedicated briefing + team channels | Sales, CS, finance | Update talk tracks immediately |
| Market insight | Low | Weekly PMM digest | Product, sales, marketing | Optional read |
| Win/loss finding | Medium | Weekly PMM digest + relevant team channel | Sales, product | Discuss in next team meeting |

## Broadcast Template

```
## [UPDATE TYPE] [Urgency: HIGH/MEDIUM/LOW]

### What Changed
[One paragraph: what specifically changed and when it took effect.]

### Why It Matters
[One paragraph: why this change matters to the audience's daily work.]

### What To Do Differently
- [Action 1: specific behaviour change]
- [Action 2: specific language change]
- [Action 3: specific process change]

### New Approved Language
> [Exact phrasing to use in customer-facing interactions]

### What To Stop Saying
> [Previous phrasing that is now outdated]

### Full Document
[Link to the complete source document]

### Questions?
[Contact person and channel for follow-up]
```

## Distribution Channel Selection

| Factor | Slack/Teams Channel | Email Digest | All-Hands Slot | Enablement Platform |
|--------|-------------------|--------------|----------------|-------------------|
| Urgency | High (immediate visibility) | Low (batch delivery) | Medium (next scheduled meeting) | Medium (async reference) |
| Depth | Brief (scannable) | Moderate (2-3 paragraphs) | Detailed (presentation + Q&A) | Full (complete document) |
| Interaction | Quick reactions, questions | None expected | Live Q&A | Self-paced review |
| Persistence | Low (scrolls away) | Medium (inbox archive) | Low (meeting memory) | High (searchable repository) |

## Urgency Calibration Rules

To prevent urgency inflation:

| Urgency Level | Criteria | Frequency Cap |
|---------------|----------|---------------|
| High | Customer-facing language must change within 48 hours; competitive threat requires immediate response | No more than 2 per month |
| Medium | Teams should be aware within 1 week; no immediate deal impact | No more than 4 per month |
| Low | Informational; enriches understanding but does not require action | Unlimited (batched in digest) |

## Internal Comms Log Schema

| Field | Description | Example |
|-------|-------------|---------|
| Date | When the broadcast was sent | 2026-03-15 |
| Update type | Classification from the matrix above | Positioning change |
| Urgency | HIGH / MEDIUM / LOW | HIGH |
| Audience | Teams that received the broadcast | Sales, CS, Marketing |
| Channel | Distribution method used | Slack #sales + all-hands |
| Source document | Link to the underlying change document | /positioning/v4.md |
| Acknowledgement | Whether team leads confirmed receipt | Sales: confirmed, CS: confirmed |
| Author | Who sent the broadcast | PMM Lead |
