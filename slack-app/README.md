# Skill OS Slack ritual automator (MVP)

A Bolt (Python) Slack app that runs recurring per-user rituals designed to attack Slack's biggest daily pain points — identified from public research on this branch (see `specs/005-slack-ritual-automator/`).

## What it does

Four rituals, each triggered on a cron and runnable on-demand from the App Home tab or a slash command:

| Ritual | Pain point addressed | Default schedule (UTC) | Output |
|---|---|---|---|
| `morning_digest` | Morning catch-up overwhelm | Daily 09:00 | DM summary of overnight activity |
| `followup_sweep` | Lost follow-ups, unanswered mentions | Weekdays 17:00 | DM list of pending replies with suggested responses |
| `thread_triage` | Hidden thread unreads, phantom badges | Weekdays 11:00 | DM list of stale threads with close/defer buttons |
| `decision_log` | Decisions lost in threads | Fridays 16:00 | DM weekly decision summary for a watched channel |

All ritual output is posted to the user's DM with the bot — never to shared channels — so the app reduces notification load instead of adding to it.

## Architecture

- **Slack Bolt (Python)** + Socket Mode for dev (HTTP Events for prod — future work)
- **SQLite** for per-user ritual preferences and run history
- **APScheduler** for cron-driven execution
- **Anthropic Claude** (Sonnet 4.6) for summarization and extraction

```
slack-app/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── app.py                    # Bolt handlers, App Home, slash command
├── scheduler.py              # APScheduler loop
├── storage.py                # SQLite for prefs and run history
├── llm.py                    # Claude API wrapper
├── rituals/
│   ├── __init__.py           # Registry
│   ├── base.py               # Ritual ABC + RitualContext / RitualResult
│   ├── morning_digest.py
│   ├── followup_sweep.py
│   ├── thread_triage.py
│   └── decision_log.py
└── tests/
    └── test_rituals.py       # Smoke tests for registry + contracts
```

## Setup

1. Create a Slack app at https://api.slack.com/apps (from manifest or from scratch).
2. Bot token scopes:
   - `app_mentions:read`
   - `channels:history`
   - `channels:read`
   - `chat:write`
   - `commands`
   - `groups:history`
   - `groups:read`
   - `im:history`
   - `im:read`
   - `im:write`
   - `users:read`
3. Enable **Socket Mode** and generate an App-Level Token with `connections:write`.
4. Create slash command `/skillos` (Request URL can be anything — Socket Mode routes it).
5. Subscribe to bot events: `app_home_opened`.
6. Enable the App Home tab.
7. Install the app to your workspace.

## Run

```bash
cd slack-app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in tokens
python app.py
```

## Usage

- Open the app's **Home** tab → toggle rituals you want → click *Run now* to test.
- Or from any channel: `/skillos help`, `/skillos run morning_digest`.

## Test

```bash
pytest tests/
```

## MVP scope and deliberate limits

- **Single-workspace only.** Token from env. No multi-tenant OAuth install store yet.
- **Global default schedules.** Per-user schedule/timezone overrides are future work.
- **Decision log posts to DM**, not a canvas. Canvas output (`canvases.create`) is a follow-up — decision memo calls this out explicitly.
- **Socket Mode only.** Production deployment uses HTTP Events — see Bolt docs.
- **No retry/backoff** on Claude calls; no custom rate-limit handling on Slack calls beyond Bolt's built-in.
- **Mentions scan uses `conversations.history`** per channel. Marketplace-listed apps keep Tier 3 limits; distributing this outside the Marketplace will hit the 1 req/min cap on that method (see `../specs/005-slack-ritual-automator/decision-memo.md`).
- **Thread triage close/defer buttons** currently just acknowledge — persistence of "closed" state is a follow-up.

## Next steps (post-MVP)

1. Multi-workspace OAuth install flow with token rotation.
2. Canvas output for `decision_log` (`canvases.create`, `canvases.edit`).
3. Per-user schedule + timezone overrides via a modal in App Home.
4. HTTP Events mode behind a real URL for production.
5. Marketplace listing + scope pruning (MVP requests more than strictly needed to make testing easier).
6. Persist triage close/defer so "closed" threads are suppressed in future runs.
7. Back rituals with enriched skill-os skills (replace inline prompts with calls to specific skills in `agents/`).
