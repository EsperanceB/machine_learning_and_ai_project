# GPT Persona Creation Automation

This module provides utilities for defining GPT personas and storing them as
JSON files. Personas consist of a name, role, task focus, communication tone,
and optional constraints or "threats." The data can be integrated into
projects such as voice command systems or skill exchange platforms.

## Components

- `persona_creator.py` – Contains the `Persona` class and helper function to
  save persona definitions.
- `cli.py` – Interactive command-line tool that prompts for persona details and
  generates the JSON configuration.

## Usage

Run the CLI and follow the prompts:

```bash
python cli.py
```

Each persona file is written to the `personas/` directory. Example output:

```json
{
  "name": "VoiceGuide",
  "role": "voice assistant",
  "task": "help users navigate their devices via voice commands",
  "tone": "friendly",
  "constraints": "must clarify uncertain commands before acting",
  "prompt_template": "You are VoiceGuide, a voice assistant. Your main task: help users navigate their devices via voice commands. Communicate in a friendly style. Consider the following constraints or threats: must clarify uncertain commands before acting."
}
```

Feel free to extend these scripts with additional persona attributes or
alternative persistence mechanisms.
