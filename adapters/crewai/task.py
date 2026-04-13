"""skill_to_task: convert a skill-os SKILL.md into a CrewAI Task.

Mapping:
  description     <- "When to Use" section + optional context string
  expected_output <- "Output" section (success artifacts)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, List, Optional

from .skill import Skill


def skill_to_task(
    path_or_skill: "str | Path | Skill",
    agent: Any,
    context: Optional[str] = None,
    context_tasks: Optional[List[Any]] = None,
    **kwargs: Any,
) -> Any:
    """Convert a skill-os SKILL.md into a CrewAI ``Task``.

    Parameters
    ----------
    path_or_skill:
        Path to a ``SKILL.md`` file, or an already-parsed :class:`Skill`
        instance.
    agent:
        The CrewAI ``Agent`` that will execute this task.
    context:
        Optional free-text string appended to the task description.  Use
        this to supply runtime inputs (e.g. the feature name, user story,
        domain constraints).
    context_tasks:
        Optional list of upstream CrewAI ``Task`` objects whose outputs
        are passed as context to this task (CrewAI ``Task(context=...)``).
    **kwargs:
        Any additional keyword arguments forwarded to the CrewAI ``Task``
        constructor.

    Returns
    -------
    crewai.Task
    """
    try:
        from crewai import Task  # type: ignore[import]
    except ImportError as exc:
        raise ImportError(
            "crewai is required for skill_to_task. "
            "Install it with: pip install crewai"
        ) from exc

    skill = Skill.from_path_or_skill(path_or_skill)

    # Build description: "When to Use" section, optionally extended with caller context
    when_to_use = skill.when_to_use
    if context:
        description = f"{when_to_use}\n\n## Context\n\n{context}"
    else:
        description = when_to_use

    # expected_output: the "Output" section (success artifacts only)
    expected_output = skill.output

    task_kwargs: dict[str, Any] = {
        "description": description,
        "expected_output": expected_output,
        "agent": agent,
        **kwargs,
    }
    if context_tasks:
        task_kwargs["context"] = context_tasks

    return Task(**task_kwargs)
