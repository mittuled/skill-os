# Activation Checklist: support-activation

Use this checklist when standing up the customer support function from scratch or for a new product line.

## Phase 1 — Tooling Selection and Configuration

- [ ] Define support channel mix: email, live chat, phone, social (based on customer segment)
- [ ] Select ticketing platform (Zendesk / Intercom / Freshdesk) based on expected volume and tier requirements
- [ ] Configure helpdesk workspace: brand name, subdomain, email routing, business hours
- [ ] Enable and configure live chat widget on relevant product pages (if applicable)
- [ ] Set up internal Slack/Teams integration for ticket notifications

## Phase 2 — Queue and Routing Configuration

- [ ] Create ticket queues by product area (e.g., Billing, Technical, General)
- [ ] Create ticket queues by customer tier (Enterprise priority queue)
- [ ] Configure auto-routing rules based on ticket tags, subject keywords, and customer tier
- [ ] Set up round-robin or load-balanced assignment for Tier-1 queue
- [ ] Configure escalation queue with assignment to senior agents or on-call engineer
- [ ] Test routing: submit test tickets for each category and verify correct queue assignment

## Phase 3 — SLA Definition

| Priority | First Response | Resolution | Conditions |
|----------|---------------|------------|------------|
| P0 | 1 hour | 4 hours | Full outage or data loss |
| P1 | 4 hours | 8 hours | Core feature broken, no workaround |
| P2 | 8 hours | 24 hours | Degraded, workaround available |
| P3 | 24 hours | 72 hours | Questions, cosmetic issues |

- [ ] SLA policy created in ticketing platform for each priority
- [ ] SLA breach alerts configured (notify Support Manager at 75% of SLA window)
- [ ] Customer SLA tiers created (Enterprise: P1 response = 2h vs. standard 4h)
- [ ] SLA policy documented and shared with agents

## Phase 4 — Macros and Templates

- [ ] Create macros for top 10 anticipated ticket types (based on product knowledge or early beta feedback)
- [ ] Write acknowledgement templates for each priority level
- [ ] Write escalation notification templates (to customer and to engineering)
- [ ] Write resolution templates for common issue types
- [ ] Test all macros in the ticketing system

## Phase 5 — Team Readiness

- [ ] All agents have ticketing platform access with correct permission level
- [ ] All agents have access to the product environment for reproduction and verification
- [ ] Support runbooks published and accessible to all agents
- [ ] Help centre live (or internal knowledge base if help centre not yet ready)
- [ ] Readiness briefing delivered and attendance confirmed

## Phase 6 — Dry Run

- [ ] Create test tickets covering each category and priority
- [ ] Process test tickets through the full workflow (triage → queue → assignment → resolution → close)
- [ ] Verify SLA timers start correctly on ticket creation
- [ ] Verify escalation routing fires at correct thresholds
- [ ] Verify macros and templates send correctly
- [ ] Document all issues found and resolved

## Phase 7 — Go Live

- [ ] Customer-facing support channels enabled
- [ ] Real-time queue dashboard live and visible to Support Manager
- [ ] Volume monitoring alert configured (spike > 2× baseline triggers alert)
- [ ] CSAT survey enabled on ticket close
- [ ] Post-launch monitoring scheduled: 30-min check at 1h, 4h, end-of-day

## Quality Gate

Before signing off on activation, confirm:

- [ ] All 7 phases completed
- [ ] Dry-run report reviewed and all blocking issues resolved
- [ ] SLA timers validated against at least one test ticket per priority
- [ ] Support Manager has visibility into real-time queue health
