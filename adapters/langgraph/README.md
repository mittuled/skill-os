# skill-os-langgraph

LangGraph adapter for [Skill OS](../../README.md). Load any `SKILL.md` and expose it as a LangGraph node — a callable that receives a `MessagesState`, prepends the skill content as a system message, calls the LLM, and returns the updated state.

## Installation

```bash
# With Anthropic models
pip install "skill-os-langgraph[anthropic]"

# With OpenAI models
pip install "skill-os-langgraph[openai]"

# Core only (bring your own langchain-core + langgraph)
pip install "skill-os-langgraph[langgraph]"
```

Or install from source (from the repo root):

```bash
pip install -e "adapters/langgraph[anthropic]"
```

## Quickstart

### Single skill as a node

```python
from skill_os_langgraph import create_skill_node
from langchain_anthropic import ChatAnthropic
from langgraph.graph import StateGraph
from langgraph.graph.message import MessagesState

llm = ChatAnthropic(model="claude-sonnet-4-6")

# create_skill_node accepts a path string or a pre-loaded Skill object
node = create_skill_node(
    "agents/product/product-manager/requirements-extractor/SKILL.md",
    llm,
)

graph = StateGraph(MessagesState)
graph.add_node("extract_requirements", node)
graph.set_entry_point("extract_requirements")
app = graph.compile()

result = app.invoke({"messages": [{"role": "user", "content": "Build a user auth feature"}]})
print(result["messages"][-1].content)
```

### Pre-loading a skill

```python
from skill_os_langgraph import load_skill, create_skill_node

skill = load_skill("agents/engineering/sr-backend-developer/builder/SKILL.md")
print(skill.name)        # "builder"
print(skill.complexity)  # "complex"
print(skill.triggers)    # ["build feature", ...]

node = create_skill_node(skill, llm)
```

## Multi-skill chains

Use `SkillGraph` to wire multiple skills together with a fluent API:

```python
from skill_os_langgraph import SkillGraph
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-6")

app = (
    SkillGraph(llm)
    .add_node("research", "agents/engineering/sr-backend-developer/builder/SKILL.md")
    .add_node("review",   "agents/engineering/sr-backend-developer/security-reviewer/SKILL.md")
    .add_edge("research", "review")
    .compile()
)

result = app.invoke({"messages": [{"role": "user", "content": "Build OAuth2 login"}]})
```

### Three-stage pipeline

```python
app = (
    SkillGraph(llm)
    .add_node("plan",     "agents/product/product-manager/requirements-extractor/SKILL.md")
    .add_node("build",    "agents/engineering/sr-backend-developer/builder/SKILL.md")
    .add_node("review",   "agents/engineering/sr-backend-developer/code-reviewer/SKILL.md")
    # SkillGraph auto-wires sequential edges when none are declared
    .compile()
)
```

When no edges are declared, `SkillGraph` automatically chains nodes in registration order: `plan → build → review → END`.

### Explicit entry and finish points

```python
app = (
    SkillGraph(llm)
    .add_node("triage",  "agents/customer-support/support-manager/support-activation/SKILL.md")
    .add_node("resolve", "agents/customer-success/cs-manager/onboarding-coordinator/SKILL.md")
    .set_entry_point("triage")
    .set_finish_point("resolve")
    .add_edge("triage", "resolve")
    .compile()
)
```

## Async usage

```python
from skill_os_langgraph import create_async_skill_node, SkillGraph

# Async single node
anode = create_async_skill_node("agents/.../SKILL.md", llm)
graph.add_node("step", anode)
result = await graph.compile().ainvoke({"messages": [...]})

# Async SkillGraph
app = SkillGraph(llm, async_mode=True).add_node("step", "agents/.../SKILL.md").compile()
result = await app.ainvoke({"messages": [{"role": "user", "content": "..."}]})
```

## Model selection by complexity

Each `SKILL.md` carries a `complexity` field in its frontmatter (`simple`, `medium`, `complex`). Route to the right model to balance cost and quality:

```python
from skill_os_langgraph import load_skill, create_skill_node
from langchain_anthropic import ChatAnthropic

def model_for_skill(skill_path: str) -> ChatAnthropic:
    skill = load_skill(skill_path)
    if skill.complexity == "complex":
        # Deepest reasoning — architectural decisions, multi-step analysis
        return ChatAnthropic(model="claude-opus-4-5")
    elif skill.complexity == "medium":
        # Best coding model — main development work
        return ChatAnthropic(model="claude-sonnet-4-6")
    else:
        # Lightweight — frequent invocation, simple outputs
        return ChatAnthropic(model="claude-haiku-4-5")

node = create_skill_node(skill_path, model_for_skill(skill_path))
```

### Complexity reference

| Complexity | Word limit | Recommended model | Use case |
|------------|-----------|------------------|----------|
| `simple`   | 500 words | Haiku 4.5         | Lightweight agents, frequent invocation |
| `medium`   | 1,000 words | Sonnet 4.6      | Main development work, orchestration |
| `complex`  | 1,500 words | Opus 4.5         | Architectural decisions, deep research |

## API reference

### `load_skill(path) → Skill`

Parse a `SKILL.md` file into a `Skill` dataclass.

```python
@dataclass
class Skill:
    name: str
    description: str
    department: str
    agent: str
    version: str
    complexity: str          # "simple" | "medium" | "complex"
    related_skills: list[str]
    triggers: list[str]
    body: str                # full markdown body (used as system prompt)
    path: Path | None
    system_prompt: str       # property — alias for body.strip()
```

### `create_skill_node(skill_path_or_skill, llm) → NodeFn`

Returns a synchronous node function `(state: dict) -> dict`.

- Prepends skill content as `SystemMessage` (skips if one already exists)
- Calls `llm.invoke(messages)`
- Returns `{"messages": [response]}`

### `create_async_skill_node(skill_path_or_skill, llm) → AsyncNodeFn`

Same as above but calls `llm.ainvoke(messages)` — use with `graph.ainvoke()`.

### `SkillGraph(llm, *, async_mode=False)`

Fluent multi-skill graph builder.

| Method | Description |
|--------|-------------|
| `.add_node(name, skill)` | Register a skill as a named node |
| `.add_edge(source, target)` | Add a directed edge (`"END"` for terminal) |
| `.set_entry_point(name)` | Set graph entry (default: first node) |
| `.set_finish_point(name)` | Set graph finish point (default: last node) |
| `.compile()` | Build and return a compiled LangGraph app |

## How it works

1. `load_skill()` reads the `SKILL.md` file and parses YAML frontmatter using stdlib `re` — no external YAML parser needed.
2. `create_skill_node()` creates a closure that captures the skill's body as the system prompt.
3. At invocation time, the node prepends a `SystemMessage` to the conversation history and calls the LLM.
4. LangGraph's `MessagesState` automatically appends the response to the message list for downstream nodes.

The system prompt injection is idempotent — if the state already contains a `SystemMessage` as the first message (e.g. from a parent graph), it is not overwritten.

## Skill discovery

Use `scripts/search.py` to find skills before wiring them:

```bash
# Find skills matching a query
python3 scripts/search.py "requirements extraction" --top 5

# List all departments
python3 scripts/search.py --list-departments
```

## Directory layout

```
adapters/langgraph/
├── __init__.py     # Public API: load_skill, create_skill_node, SkillGraph
├── skill.py        # Skill dataclass + load_skill() parser
├── node.py         # create_skill_node() + create_async_skill_node()
├── graph.py        # SkillGraph fluent builder
├── pyproject.toml  # Package metadata + optional deps
└── README.md       # This file
```
