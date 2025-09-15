# GPT Persona Creation Automation

This module provides utilities for defining GPT personas and storing them as
JSON files. Personas consist of a name, role, task focus, communication tone,
and optional constraints or "threats." The data can be integrated into
projects such as voice command systems or skill exchange platforms.

## Components

- **Persona_creator.py** – Contains the `Persona` class and helper function to
  save persona definitions.
- **cli.py** – Interactive command-line tool that prompts for persona details and
  generates the JSON configuration.
- **Sample Persona**: Demonstration persona file at `personas/voiceguide.json`, which can be regenerated with `python ai_personas_creation_automation_gpt/cli.py`
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

To manage personas in a browser and interact with them via a GPT model, run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

The app displays existing personas as selectable buttons (maximum of eight).
You can create new personas, delete unwanted ones, and chat with the model using the selected persona's prompt.
The chat feature requires the `openai` package and an `OPENAI_API_KEY` environment variable.

Feel free to extend these scripts with additional persona attributes or
alternative persistence mechanisms.
