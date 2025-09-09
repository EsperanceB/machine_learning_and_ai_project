# persona_creator.py
from __future__ import annotations
import json
import pathlib
from typing import Dict, Any


class Persona:
    """
    Represents a GPT persona with user-defined traits (or "threats"/constraints).
    """
    def __init__(
        self,
        name: str,
        role: str,
        task: str,
        tone: str,
        constraints: str = "",
    ) -> None:
        self.name = name
        self.role = role
        self.task = task
        self.tone = tone
        self.constraints = constraints

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "role": self.role,
            "task": self.task,
            "tone": self.tone,
            "constraints": self.constraints,
            "prompt_template": self.build_prompt(),
        }

    def build_prompt(self) -> str:
        """
        Generates a prompt for configuring a GPT model.
        """
        prompt = (
            f"You are {self.name}, a {self.role}. "
            f"Your main task: {self.task}. "
            f"Communicate in a {self.tone} style."
        )
        if self.constraints:
            prompt += f" Consider the following constraints or threats: {self.constraints}."
        return prompt


def save_persona(persona: Persona, directory: str = "personas") -> pathlib.Path:
    """
    Saves the persona configuration as a JSON file.
    """
    path = pathlib.Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / f"{persona.name.lower().replace(' ', '_')}.json"
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(persona.to_dict(), f, indent=2)
    return file_path
