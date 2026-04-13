# Roadmap

## Done

- **003 production-grade depth** — 527 skills enriched with `references/` and `assets/` subdirectories; every skill is practitioner-executable without leaving the repo
- **Public release** — repo open-sourced, community files added, validation script shipped
- **Department reorganization** — 15 departments canonicalized, ethos profiles written for each
- **Paperclip integration** — skill-os connected as a knowledge source; agents resolve skills at runtime via `instructionsFilePath`
- **Triggers field + discoverability** — `triggers` frontmatter populated on all 527 skills; `scripts/search.py` CLI for natural-language skill lookup
- **Skill quality scoring** — `scripts/score.py` grades every skill on 7 dimensions; leaderboard + department averages + contributor targets
- **LangGraph adapter** — `adapters/langgraph/`: any SKILL.md as a LangGraph node; `SkillGraph` fluent builder for multi-skill chains; complexity-aware model selection
- **CrewAI adapter** — `adapters/crewai/`: `skill_to_agent()`, `skill_to_task()`, `SkillCrew` fluent pipeline builder

## Ideas / Contributions Welcome

- **New departments** — HR / People Ops, Security & Compliance, Procurement
- **Skill translations** — localized versions of high-traffic skills (start with Spanish, French, Japanese)
- **Automated skill testing** — harness that runs a skill's workflow against a synthetic input and checks the output matches the expected template shape
- **Community skill registry** — versioned index of all skills with search, filtering by department/complexity/agent
