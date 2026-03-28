# Framework: inter-phase-retrospective

Guides the facilitation of engineering retrospectives between delivery phases using structured data collection, pattern analysis, and action-item tracking.

## Retrospective Structure

### Phase 1: Data Collection (Before Session)

Collect the following before the retrospective meeting:

| Data Source | Metrics to Gather |
|-------------|-------------------|
| Sprint tracker | Velocity per sprint, planned vs. actual, carryover rate |
| CI/CD pipeline | Deployment frequency, change failure rate, build times |
| Incident tracker | Incident count, MTTR, severity distribution |
| Scope change log | Number of scope changes, source, impact on timeline |
| DORA dashboard | Lead time, deployment frequency, CFR, MTTR trends |

### Phase 2: Structured Feedback (During Session)

Use four categories for feedback collection:

| Category | Prompt | Expected Output |
|----------|--------|-----------------|
| What went well | "What practices or decisions from this phase should we continue?" | Positive patterns to reinforce |
| What didn't go well | "What caused friction, delays, or rework this phase?" | Pain points to investigate |
| What to change | "What specific process change would you make for the next phase?" | Actionable improvement proposals |
| Surprises | "What happened that was unexpected, positive or negative?" | Emerging risks or opportunities |

### Phase 3: Pattern Analysis

1. **Cluster feedback**: Group related items from all four categories.
2. **Cross-reference with data**: Validate subjective feedback against objective metrics (e.g., "builds were slow" + build time data).
3. **Classify findings**:
   - **Systemic**: Recurring across 2+ phases or reported by 3+ people
   - **One-off**: Specific to this phase's circumstances
   - **Emerging**: New pattern not seen before — monitor in next phase
4. **Rate impact**: High (affected delivery timeline or quality), Medium (caused friction but manageable), Low (minor annoyance).

### Phase 4: Action Items

Every action item must follow this format:

| Field | Required |
|-------|----------|
| Description | Specific, measurable change (not "improve testing") |
| Owner | Named individual |
| Deadline | Calendar date or "by sprint N of next phase" |
| Definition of Done | How we know this action is complete |
| Finding Reference | Which retrospective finding it addresses |

## Anti-Pattern Detection

Flag these patterns automatically if they appear in the data:

| Pattern | Detection Signal | Recommended Discussion Topic |
|---------|-----------------|------------------------------|
| Velocity decay | Velocity decreased >15% over the phase | Team capacity, scope creep, or tech debt drag |
| Incident spikes | >2x baseline incident rate | Quality gates, testing gaps, or operational readiness |
| Scope churn | >20% of tasks added/removed mid-phase | Requirements stability, change control process |
| Estimation drift | Actual effort >1.5x estimated for >30% of tasks | Estimation methodology, hidden complexity |
| Carryover accumulation | Carryover rate increased each sprint | Overcommitment, blocking dependencies |

## Action Item Tracking

Track completion of retrospective action items using this lifecycle:

```
Open → In Progress → Done → Verified
```

Review action item status at the start of the next retrospective. Unresolved items from previous retros should be re-prioritized or explicitly closed with rationale.
