"""skill_to_agent: convert a skill-os SKILL.md into a CrewAI Agent.

Mapping:
  role      <- frontmatter `agent`  (e.g. "sr-backend-developer")
  goal      <- frontmatter `description`  (the pushy one-liner)
  backstory <- full skill body (all 9 sections)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from .skill import Skill


def skill_to_agent(
    path_or_skill: "str | Path | Skill",
    llm: Optional[Any] = None,
    **kwargs: Any,
) -> Any:
    """Convert a skill-os SKILL.md into a CrewAI ``Agent``.

    Parameters
    ----------
    path_or_skill:
        Path to a ``SKILL.md`` file, or an already-parsed :class:`Skill`
        instance.
    llm:
        Optional LLM instance passed directly to the CrewAI ``Agent``
        constructor.  When ``None`` the agent uses CrewAI's default model.
    **kwargs:
        Any additional keyword arguments forwarded to the CrewAI ``Agent``
        constructor (e.g. ``tools``, ``max_iter``, ``allow_delegation``).

    Returns
    -------
    crewai.Agent
    """
    try:
        from crewai import Agent  # type: ignore[import]
    except ImportError as exc:
        raise ImportError(
            "crewai is required for skill_to_agent. "
            "Install it with: pip install crewai"
        ) from exc

    skill = Skill.from_path_or_skill(path_or_skill)

    agent_kwargs: dict[str, Any] = {
        "role": skill.agent,
        "goal": skill.description,
        "backstory": skill.body,
        "verbose": kwargs.pop("verbose", True),
        **kwargs,
    }
    if llm is not None:
        agent_kwargs["llm"] = llm

    return Agent(**agent_kwargs)
