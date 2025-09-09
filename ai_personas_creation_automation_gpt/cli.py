"""Command-line interface for creating GPT persona definitions.

This script prompts the user for persona characteristics and stores the
resulting configuration as a JSON file using :mod:`persona_creator`.
"""

from __future__ import annotations

from persona_creator import Persona, save_persona


def main() -> None:
    """Collect persona details from the user and write them to disk."""
    print("Create a GPT Persona")
    name = input("Persona name: ").strip()
    role = input("Persona role (e.g., 'voice assistant', 'mentor'): ").strip()
    task = input("Main task: ").strip()
    tone = input("Communication tone (e.g., 'friendly', 'professional'): ").strip()
    threats = input("Constraints or threats (leave blank if none): ").strip()

    persona = Persona(name, role, task, tone, threats)
    path = save_persona(persona)
    print(f"Persona saved to {path}")


if __name__ == "__main__":
    main()
