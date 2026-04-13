"""
skill-os-langgraph — LangGraph adapter for Skill OS.

Load any SKILL.md and expose it as a LangGraph node.

Quick start::

    from skill_os_langgraph import create_skill_node, SkillGraph, load_skill
    from langchain_anthropic import ChatAnthropic
    from langgraph.graph import StateGraph
    from langgraph.graph.message import MessagesState

    llm = ChatAnthropic(model="claude-sonnet-4-6")

    # Single skill node
    node = create_skill_node("agents/.../SKILL.md", llm)
    graph = StateGraph(MessagesState)
    graph.add_node("my_skill", node)
    graph.set_entry_point("my_skill")
    app = graph.compile()
    result = app.invoke({"messages": [{"role": "user", "content": "..."}]})

    # Multi-skill chain
    app = (
        SkillGraph(llm)
        .add_node("research", "agents/.../SKILL.md")
        .add_node("review",   "agents/.../SKILL.md")
        .add_edge("research", "review")
        .compile()
    )
"""

from .graph import SkillGraph
from .node import create_async_skill_node, create_skill_node
from .skill import Skill, load_skill

__all__ = [
    "load_skill",
    "create_skill_node",
    "create_async_skill_node",
    "SkillGraph",
    "Skill",
]

__version__ = "0.1.0"
