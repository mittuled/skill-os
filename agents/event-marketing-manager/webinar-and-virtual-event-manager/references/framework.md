# Framework: webinar-and-virtual-event-manager

This framework defines platform selection criteria, registration-to-attendance optimisation, engagement techniques, performance benchmarks, and post-event nurture integration for the webinar programme.

## Webinar Format Selection

| Format | Best Use Case | Engagement Level | Production Complexity | Typical Duration |
|--------|-------------|-----------------|----------------------|-----------------|
| Single-speaker presentation | Product demo, thought leadership, how-to | Low | Low | 30–45 min |
| Panel discussion | Industry trends, customer perspectives, debate | Medium | Medium | 45–60 min |
| Fireside chat | Executive interview, customer story | Medium | Low | 30–45 min |
| Demo + Q&A | Product launch, feature release, integration walkthrough | High | Medium | 45–60 min |
| AMA (Ask Me Anything) | Community building, post-launch, roadmap preview | High | Low | 45–60 min |
| Virtual conference (multi-session) | Flagship virtual event, partner summit | High | High | Half-day to 2 days |

**Format selection rule**: Choose the format that maximises audience interaction, not the one that minimises speaker prep. Formats with live Q&A, polls, and demos consistently outperform lecture formats on attendance retention and lead conversion.

## Platform Selection Criteria

Score each platform 1–5. Use for annual platform review or initial selection.

| Criterion | Weight | Considerations |
|-----------|--------|---------------|
| Registration and landing page capability | 20% | Native landing page builder vs. third-party; custom branding; form field flexibility |
| Engagement tools (polls, Q&A, chat, reactions) | 20% | Live polls; moderated Q&A; chat moderation tools; emoji reactions |
| Recording and on-demand delivery | 15% | Auto-recording; on-demand replay page; chapter markers |
| Analytics and lead scoring | 20% | Attendance duration tracking; poll response capture; engagement score export; CRM sync |
| Integration with CRM and MAP | 15% | Native Salesforce, HubSpot, Marketo connectors; webhook support |
| Production quality (audio/video) | 10% | HD video support; custom studio mode; branded backgrounds; multi-speaker layout |

**Common platforms and positioning:**
- Zoom Webinars: Reliable, widely adopted, strong meeting-to-webinar upgrade path; limited engagement tools
- ON24: Enterprise webinar platform; strong analytics and engagement scoring; higher cost
- Hopin / RingCentral Events: Multi-format virtual events; expo hall and networking features; best for virtual conferences
- Goldcast: B2B-focused; strong CRM integration and engagement analytics; mid-market sweet spot
- StreamYard: Production-focused streaming; best for polished studio-quality broadcasts

## Registration-to-Attendance Optimisation

**Industry benchmarks:**
- Registration-to-attendance rate: 30–40% (live attendance)
- On-demand replay rate: 40–60% of registrants (within 7 days)
- Ideal total reach: Live attendance + on-demand views within 30 days

| Lever | Tactic | Expected Lift |
|-------|--------|--------------|
| Reminder cadence | Send reminders at 1 week, 1 day, and 1 hour before event | +10–15% attendance vs. no reminders |
| Calendar hold in first email | Include .ics calendar invite in registration confirmation | +5–8% attendance |
| Topic-to-audience match | Validate topic against ICP pain points; survey audience segments before committing | Core driver of registration quality |
| Day and time optimisation | Tuesday–Thursday, 10 AM–12 PM or 1–3 PM in target timezone | +10–20% vs. Friday afternoon |
| Social proof in promotion | Feature speaker credentials and past attendee count in promotional copy | +5–10% registration conversion |
| Co-host or partner promotion | Partner cross-promotes to their list; doubles top-of-funnel reach | +30–50% registrations |

## Engagement Scoring Model

Assign an engagement score to each attendee post-event. Use for lead prioritisation in post-event follow-up.

| Activity | Points |
|----------|--------|
| Attended live (any duration) | +10 |
| Attended ≥ 75% of live session duration | +15 |
| Answered poll | +5 per poll |
| Submitted Q&A question | +10 |
| Clicked resource link in chat | +5 |
| Downloaded post-event asset | +10 |
| Watched on-demand replay | +8 |
| Booked meeting from post-event CTA | +25 |

**Lead tier by engagement score:**
- Score ≥ 50: Hot — AE or SDR same-day follow-up
- Score 25–49: Warm — SDR sequence within 48 hours
- Score < 25: Cold — standard nurture sequence

## Post-Event Nurture Integration

### Sequence by Segment

| Segment | Email 1 (Day 1) | Email 2 (Day 4) | Email 3 (Day 8) | CTA |
|---------|----------------|----------------|----------------|-----|
| Hot attendees (score ≥ 50) | Personalised note + recording link + meeting ask | Relevant case study | Breakup or next event invite | Book a demo / meeting |
| Warm attendees (score 25–49) | Recording + slides + related resource | Blog post or guide on topic | Next webinar invite | Next webinar registration |
| Cold attendees (score < 25) | Recording and slides only | General newsletter | Next webinar invite | Newsletter subscription |
| No-shows (registered, didn't attend) | "Sorry we missed you" + recording link | Related resource | Next webinar invite | On-demand replay |

### CRM and MAP Handoff

- Sync all registrant and attendee data to CRM within 2 hours of event close
- Tag all records with: webinar title, date, attended (Y/N), engagement score, lead tier
- Trigger post-event nurture sequence via MAP based on engagement tier
- Hot leads (score ≥ 50): alert owning AE/SDR immediately; do not wait for next business day

## Webinar Performance Benchmarks

| Metric | Below Average | Average | Good | Excellent |
|--------|-------------|---------|------|-----------|
| Registration-to-attendance rate | < 25% | 25–35% | 35–45% | > 45% |
| Average session duration (% of total) | < 50% | 50–65% | 65–80% | > 80% |
| Poll response rate | < 20% | 20–35% | 35–55% | > 55% |
| Q&A participation rate | < 10% | 10–20% | 20–35% | > 35% |
| Post-event MQL conversion | < 5% of attendees | 5–12% | 12–20% | > 20% |
| Meeting booking rate (hot leads) | < 10% | 10–20% | 20–35% | > 35% |

## Webinar Calendar Cadence

| Cadence | Best For | Audience Expectation |
|---------|---------|---------------------|
| Weekly | High-volume product demo series; customer success onboarding | Regular, predictable; lower bar per event |
| Bi-weekly | Thought leadership series; partner co-marketing | Moderate investment; building series following |
| Monthly | Flagship thought leadership or product deep-dives | Higher perceived value per event |
| Quarterly | Flagship virtual event or virtual conference | High-production event; major promotion cycle |

**Principle**: Consistency compounds. A bi-weekly webinar series that runs for 12 months builds a predictable pipeline engine that no one-off event can match.
