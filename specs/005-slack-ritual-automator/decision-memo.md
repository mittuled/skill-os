# Decision Memo: Slack Ritual Automator — Internal vs Marketplace

**Status**: Draft for review
**Date**: 2026-04-09
**Branch**: `claude/evaluate-slack-mcp-19Z0H`
**Decision owner**: TBD
**Context docs**: prior evaluations of Slack MCP and Slack API boundaries (see conversation on this branch)

## 1. What we're deciding

Whether to build the Slack Ritual Automator as:

- **Shape A — Marketplace-listed public app**: distributed via the Slack Marketplace to any workspace.
- **Shape C — Internal custom app**: installed only in our own Slack workspace, never distributed.

The job of the app (fixed): **automate a recurring team ritual — standups, on-call handoffs, or incident triage — using skill-os workflow skills as the execution layer.** The user experience lives inside Slack (App Home, slash command, scheduled messages, modals, canvases). skill-os skills run server-side and post their outputs back into Slack.

This memo does **not** cover Shape B (external web app consuming Slack). Prior evaluation ruled it out for this use case: a ritual automator's natural home is *inside* Slack at the moment of the ritual, not on a separate web surface.

## 2. Options compared

| Dimension | Shape A — Marketplace | Shape C — Internal custom |
|---|---|---|
| **Distribution reach** | Any Slack workspace | Our workspace only |
| **Rate limits** (`conversations.history`, `conversations.replies`) | Tier 3 (standard) | Not affected by May 2025 / Mar 2026 tightening |
| **Developer Policy risk** | Must pass Marketplace review; scope and data-use scrutinized | Narrower policy surface; internal apps get more latitude |
| **OAuth model** | Public distribution flow, per-workspace install store, token rotation | Single-workspace install, simpler token management |
| **Review burden** | Security review, DPIA, listing copy, support commitments | None beyond our own eng review |
| **Time to first usable version** | Slower (design must anticipate review) | Faster (can iterate freely) |
| **Product feedback loop** | External users, broader signal | Our team only, narrower signal |
| **Monetization path** | Yes, via Marketplace | None |
| **Data residency / retention** | Must publish and honor a policy | Governed by internal policy only |
| **Huddles / calls coverage** | Same limit (metadata only) | Same limit (metadata only) |
| **skill-os coupling** | Must abstract skill-os enough that external tenants aren't exposed to our internal structure | Can couple tightly to `agents/` and `departments/` layout |

## 3. Trade-off summary

- **Shape A is the right choice if** the ritual automator is a product we intend to ship externally, or if we want external usage to validate skill-os as a framework. Cost: slower start, review overhead, must generalize beyond our own org's rituals.
- **Shape C is the right choice if** the primary goal is operational leverage for our own team today and/or a testbed for skill-os integration patterns without committing to external distribution. Cost: no distribution path, work may need to be redone if we later re-target Marketplace.

## 4. Recommendation

**Start as Shape C, design with Shape A in mind.**

Rationale:

1. **Fastest feedback**. Internal install sidesteps Marketplace review and lets us iterate on the ritual UX (standup modal, canvas output format, scheduling) in days, not weeks.
2. **Rate-limit immunity**. Internal customer-built apps are unaffected by the Mar 3 2026 rate-limit tightening. We can build and evolve the history-touching parts without working around a 1-req/min ceiling.
3. **skill-os as the real product**. The ritual automator is a demonstration vehicle for skill-os. Internal deployment gives us a controlled environment to validate that skill-os workflow skills are production-ready before we expose them to third-party workspaces.
4. **Cheap upgrade path — if we design for it**. The upgrade from C → A is mostly a scope review, distribution flow, and policy/support docs. It is **not** cheap if we hardcode internal assumptions (team names, skill slugs, workspace IDs) into the app logic. So we adopt the discipline of Shape A from day one: no hardcoded IDs, all skill-os lookups go through a resolver, all outputs templated.

### Conditions for the recommendation to hold

- We commit to **one ritual** for v1 (recommend: **daily standup**, because it's the most predictable trigger and the easiest to measure value).
- We commit to **not** using any huddle/call content (ruled out by API).
- We commit to **Marketplace-safe scopes** from day one: `commands`, `chat:write`, `im:history`, `channels:read`, `users:read`, `canvases:write`. No user tokens unless a specific feature demands it.
- We commit to Bolt (Python, to match skill-os's existing Python script conventions in `scripts/`).
- We commit to Socket Mode for dev, HTTP Events for prod — even internally, because it forces correct signing-secret handling early.

## 5. Non-goals for v1

- Multi-workspace distribution
- Monetization / billing
- Huddle or voice integration
- Rendering any Slack message history outside Slack
- Training any model on workspace content

## 6. Open questions

1. **Which ritual?** Standup is the default recommendation; on-call handoff and incident triage are plausible alternatives. Pick one for v1.
2. **Which skill-os agent owns the ritual logic?** Likely candidates: an `engineering-manager` skill for standups, an `incident-commander` skill for triage. Needs a specific enriched skill to call.
3. **Where do outputs land?** Thread reply, channel message, canvas, or App Home block — v1 should pick one primary surface.
4. **Scheduling source of truth**: Slack's scheduled messages vs. a server-side cron calling `chat.postMessage`. Recommend server-side cron for auditability.
5. **Who is the decision owner** for approving the C → A upgrade when/if it happens?

## 7. Proposed next steps

1. Decision owner confirms **Shape C, design-for-A** recommendation (or picks differently).
2. Pick the v1 ritual and the skill-os skill that will back it.
3. Create a full feature spec at `specs/005-slack-ritual-automator/spec.md` following the pattern of `specs/004-skill-os-paperclip-integration/`.
4. Add a Slack entry to `allowed-tools.yaml` via the `tool-policy-manager` skill.
5. Scaffold a Bolt (Python) app in a new top-level directory (e.g. `slack-app/`) — not inside `agents/`, because it's infrastructure, not a skill.
