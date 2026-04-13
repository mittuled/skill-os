# skill-os CrewAI Adapter

Turn any skill-os `SKILL.md` file into a CrewAI `Agent` or `Task` in one line.

## Install

```bash
pip install crewai>=0.51
# then add the adapter to your Python path (no PyPI package yet)
```

The adapter has zero dependencies beyond the Python stdlib — CrewAI is an
optional runtime dependency required only when `skill_to_agent`, `skill_to_task`,
or `SkillCrew` are actually called.

## How it works

| SKILL.md field / section | CrewAI mapping |
|---|---|
| frontmatter `agent` | `Agent.role` |
| frontmatter `description` | `Agent.goal` |
| full markdown body | `Agent.backstory` |
| `## When to Use` section | `Task.description` |
| `## Output` section | `Task.expected_output` |

## Single-agent example

```python
import sys
sys.path.insert(0, "/path/to/skill-os")   # adjust to your checkout

from adapters.crewai import skill_to_agent, skill_to_task
from crewai import Crew, Process

SKILL = "agents/customer-support/support-manager/support-activation/SKILL.md"

# Build agent and task from the same skill file
pm_agent = skill_to_agent(SKILL)
task = skill_to_task(
    SKILL,
    agent=pm_agent,
    context="Stand up support for a B2B SaaS product launching in 4 weeks.",
)

crew = Crew(agents=[pm_agent], tasks=[task], process=Process.sequential)
result = crew.kickoff()
print(result)
```

## Multi-agent pipeline with SkillCrew

```python
from adapters.crewai import SkillCrew
from crewai import Process

result = (
    SkillCrew()
    .add("pm",  "agents/product/product-manager/requirements-extractor/SKILL.md")
    .add("eng", "agents/engineering/sr-backend-developer/builder/SKILL.md")
    .add("sec", "agents/engineering/sr-backend-developer/security-reviewer/SKILL.md")
    .process(Process.sequential)
    .kickoff(inputs={"feature": "OAuth2 login"})
)

print(result)
```

`SkillCrew` wires tasks sequentially — each task receives the output of all
previous tasks as context via CrewAI's `Task(context=[...])` parameter.

## Passing a custom LLM

```python
from langchain_openai import ChatOpenAI
from adapters.crewai import skill_to_agent

llm = ChatOpenAI(model="gpt-4o", temperature=0)
agent = skill_to_agent("agents/.../SKILL.md", llm=llm)
```

Or with `SkillCrew`:

```python
from adapters.crewai import SkillCrew

result = (
    SkillCrew()
    .llm(llm)
    .add("pm", "agents/.../SKILL.md")
    .kickoff(inputs={"feature": "user auth"})
)
```

## Using a pre-parsed Skill object

```python
from adapters.crewai import Skill, skill_to_agent, skill_to_task

skill = Skill.from_file("agents/.../SKILL.md")
print(skill.name, skill.complexity)
print(skill.when_to_use)

agent = skill_to_agent(skill)
task  = skill_to_task(skill, agent=agent, context="Build for a fintech startup.")
```

## API reference

### `skill_to_agent(path_or_skill, llm=None, **kwargs) -> crewai.Agent`

| Parameter | Type | Description |
|---|---|---|
| `path_or_skill` | `str \| Path \| Skill` | Path to `SKILL.md` or parsed `Skill` |
| `llm` | optional | LLM instance forwarded to `Agent(llm=...)` |
| `**kwargs` | any | Forwarded to `Agent(...)` (e.g. `tools`, `max_iter`) |

Defaults: `verbose=True`.

### `skill_to_task(path_or_skill, agent, context=None, context_tasks=None, **kwargs) -> crewai.Task`

| Parameter | Type | Description |
|---|---|---|
| `path_or_skill` | `str \| Path \| Skill` | Path to `SKILL.md` or parsed `Skill` |
| `agent` | `crewai.Agent` | Agent that will execute the task |
| `context` | `str \| None` | Free-text appended to task description |
| `context_tasks` | `list[Task] \| None` | Upstream tasks whose output is passed as context |
| `**kwargs` | any | Forwarded to `Task(...)` |

### `SkillCrew`

Fluent builder.  Methods return `self` for chaining.

| Method | Description |
|---|---|
| `.add(alias, path_or_skill)` | Register a skill |
| `.process(crewai.Process)` | Set execution process |
| `.llm(llm)` | Set shared LLM for all agents |
| `.crew_kwargs(**kw)` | Extra kwargs for `Crew(...)` |
| `.kickoff(inputs={})` | Assemble and run — returns `CrewOutput` |

The `inputs` dict is forwarded to `Crew.kickoff()`.  A special `"context"` key
is also extracted and appended to every task description.

### `Skill` dataclass

```python
skill = Skill.from_file("path/to/SKILL.md")

skill.name            # frontmatter name
skill.description     # frontmatter description (pushy one-liner)
skill.agent           # frontmatter agent slug
skill.department      # frontmatter department
skill.complexity      # "simple" | "medium" | "complex"
skill.triggers        # list[str]
skill.related_skills  # list[str]
skill.body            # full markdown body
skill.when_to_use     # "When to Use" section
skill.workflow        # "Workflow" section
skill.anti_patterns   # "Anti-Patterns" section
skill.output          # "Output" section
```
