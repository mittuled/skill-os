# Roadmap

## Done

- **003 production-grade depth** — 528 skills enriched with `references/` and `assets/` subdirectories; every skill is practitioner-executable without leaving the repo
- **Public release** — repo open-sourced, community files added, validation script shipped
- **Department reorganization** — 15 departments canonicalized, ethos profiles written for each
- **Paperclip integration** — skill-os connected as a knowledge source; agents resolve skills at runtime

## Up Next

- **Triggers field + discoverability** — populate `triggers` frontmatter on all skills so platforms can surface the right skill from natural-language input
- **LangGraph adapter** — thin wrapper to load any skill as a LangGraph node with typed inputs/outputs
- **CrewAI adapter** — expose skills as CrewAI tools with descriptions auto-derived from frontmatter
- **Skill quality scoring** — automated script that grades each skill on completeness, specificity, and anti-pattern coverage; surfaces low-scoring skills for improvement

## Ideas / Contributions Welcome

- **New departments** — HR / People Ops, Security & Compliance, Procurement
- **Skill translations** — localized versions of high-traffic skills (start with Spanish, French, Japanese)
- **Automated skill testing** — harness that runs a skill's workflow against a synthetic input and checks the output matches the expected template shape
- **Community skill registry** — versioned index of all skills with search, filtering by department/complexity/agent
