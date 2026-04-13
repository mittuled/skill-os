"""
node.py — LangGraph node factory for Skill OS skills.

Creates sync and async LangGraph-compatible node functions from a Skill
or a path to a SKILL.md file.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

from .skill import Skill, load_skill

# ---------------------------------------------------------------------------
# Type aliases (avoid hard import of langchain_core at module level so the
# adapter can be imported even when langchain-core is not installed — the
# error surfaces only when a node is actually created).
# ---------------------------------------------------------------------------
NodeFn = Callable[[dict], dict]
AsyncNodeFn = Callable[[dict], Any]  # coroutine


def _resolve_skill(skill_path_or_skill: str | Path | Skill) -> Skill:
    """Accept either a Skill object or a path and return a Skill."""
    if isinstance(skill_path_or_skill, Skill):
        return skill_path_or_skill
    return load_skill(skill_path_or_skill)


def create_skill_node(
    skill_path_or_skill: str | Path | Skill,
    llm: Any,
) -> NodeFn:
    """
    Create a synchronous LangGraph node function from a skill.

    The returned function:
    - Receives a MessagesState dict (``{"messages": [...]}``)
    - Prepends the skill content as a SystemMessage
    - Calls the LLM synchronously
    - Returns ``{"messages": [response]}``

    Args:
        skill_path_or_skill: Path to a SKILL.md file, or a pre-loaded Skill.
        llm: A LangChain chat model (e.g. ChatAnthropic, ChatOpenAI).

    Returns:
        A callable compatible with LangGraph's StateGraph.add_node().

    Example::

        from langchain_anthropic import ChatAnthropic
        node = create_skill_node("agents/engineering/.../SKILL.md", ChatAnthropic())
    """
    try:
        from langchain_core.messages import SystemMessage
    except ImportError as e:
        raise ImportError(
            "langchain-core is required: pip install 'skill-os-langgraph[langgraph]'"
        ) from e

    skill = _resolve_skill(skill_path_or_skill)
    system_content = skill.system_prompt

    def node(state: dict) -> dict:
        messages = list(state.get("messages", []))
        # Prepend skill instructions as a system message if not already present
        if not messages or not _is_system_message(messages[0]):
            messages = [SystemMessage(content=system_content)] + messages
        response = llm.invoke(messages)
        return {"messages": [response]}

    # Attach skill metadata to the function for introspection
    node.__name__ = f"skill_node_{skill.name}"
    node.__doc__ = f"Skill node for '{skill.name}' ({skill.complexity})"
    node._skill = skill  # type: ignore[attr-defined]

    return node


def create_async_skill_node(
    skill_path_or_skill: str | Path | Skill,
    llm: Any,
) -> AsyncNodeFn:
    """
    Create an asynchronous LangGraph node function from a skill.

    Identical to create_skill_node() but uses ``llm.ainvoke()`` for
    async execution within LangGraph's async graph runner.

    Args:
        skill_path_or_skill: Path to a SKILL.md file, or a pre-loaded Skill.
        llm: A LangChain chat model with async support.

    Returns:
        An async callable compatible with LangGraph's StateGraph.add_node().

    Example::

        from langchain_anthropic import ChatAnthropic
        anode = create_async_skill_node("agents/.../SKILL.md", ChatAnthropic())
        graph.add_node("step", anode)
        result = await graph.compile().ainvoke({"messages": [...]})
    """
    try:
        from langchain_core.messages import SystemMessage
    except ImportError as e:
        raise ImportError(
            "langchain-core is required: pip install 'skill-os-langgraph[langgraph]'"
        ) from e

    skill = _resolve_skill(skill_path_or_skill)
    system_content = skill.system_prompt

    async def anode(state: dict) -> dict:
        messages = list(state.get("messages", []))
        if not messages or not _is_system_message(messages[0]):
            messages = [SystemMessage(content=system_content)] + messages
        response = await llm.ainvoke(messages)
        return {"messages": [response]}

    anode.__name__ = f"async_skill_node_{skill.name}"  # type: ignore[attr-defined]
    anode.__doc__ = f"Async skill node for '{skill.name}' ({skill.complexity})"  # type: ignore[attr-defined]
    anode._skill = skill  # type: ignore[attr-defined]

    return anode


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_system_message(msg: Any) -> bool:
    """Return True if msg is a LangChain SystemMessage or a dict with role='system'."""
    try:
        from langchain_core.messages import SystemMessage
        if isinstance(msg, SystemMessage):
            return True
    except ImportError:
        pass
    if isinstance(msg, dict):
        return msg.get("role") == "system"
    return False
