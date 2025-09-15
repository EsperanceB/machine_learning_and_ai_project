# This app will allow you to input your persona specifications
# Streamlit UI for creating, selecting, and chatting with GPT personas
import json
import os
import pathlib
from typing import Dict, Any

import streamlit as st
from persona_creator import Persona, save_persona

st.title("AI Persona Builder")
try:
    from openai import OpenAI
    
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    openai = True
except ImportError:  # pragma: no cover - only used when openai isn't installed
    openai = None

PERSONA_DIR = pathlib.Path("personas")
PERSONA_DIR.mkdir(parents=True, exist_ok=True)


def load_personas() -> Dict[str, Dict[str, Any]]:
    personas: Dict[str, Dict[str, Any]] = {}
    for file in PERSONA_DIR.glob("*.json"):
        with file.open("r", encoding="utf-8") as f:
            personas[file.stem] = json.load(f)
    return personas


def delete_persona(name: str) -> None:
    file = PERSONA_DIR / f"{name}.json"
    if file.exists():
        file.unlink()


personas = load_personas()
st.sidebar.title("Personas")
selected = st.session_state.get("selected_persona")

# Persona selection and deletion
for name in list(personas.keys()):
    if st.sidebar.button(name, key=f"select_{name}"):
        st.session_state["selected_persona"] = name
        st.session_state["messages"] = []
        st.rerun()
    if st.sidebar.button(f"Delete {name}", key=f"delete_{name}"):
        delete_persona(name)
        if st.session_state.get("selected_persona") == name:
            st.session_state["selected_persona"] = None
            st.session_state["messages"] = []
        st.rerun()

personas = load_personas()  # reload after potential deletions
selected = st.session_state.get("selected_persona")

name = st.text_input("Persona name")
role = st.text_input("Role (e.g., voice assistant, mentor)")
task = st.text_area("Main task")
tone = st.text_input("Communication tone (e.g., friendly, professional)")
constraints = st.text_input("Constraints or threats")
# Persona creation (limited to 8)
if len(personas) < 8:
    st.sidebar.subheader("Create Persona")
    new_name = st.sidebar.text_input("Name")
    new_role = st.sidebar.text_input("Role")
    new_task = st.sidebar.text_area("Task")
    new_tone = st.sidebar.text_input("Tone")
    new_constraints = st.sidebar.text_input("Constraints")
    if st.sidebar.button("Save Persona"):
        persona = Persona(new_name, new_role, new_task, new_tone, new_constraints)
        save_persona(persona)
        st.rerun()
else:
    st.sidebar.warning("Maximum of 8 personas reached. Delete one to add a new persona.")

if st.button("Create Persona"):
    persona = Persona(name, role, task, tone, constraints)
    path = save_persona(persona)
    st.success(f"Persona saved to {path}")
    st.json(persona.to_dict())
# Chat interface
if selected and selected in personas:
    persona_data = personas[selected]
    st.header(f"Chat with {persona_data['name']}")
    user_input = st.text_input("Your message")
    if st.button("Send"):
        if openai is None:
            st.error("The openai package is required to chat with the model.")
        elif not os.getenv("OPENAI_API_KEY"):
            st.error("OPENAI_API_KEY environment variable not set.")
        else:
            messages = st.session_state.get("messages", [])
            if not messages:
                messages.append({"role": "system", "content": persona_data["prompt_template"]})
            messages.append({"role": "user", "content": user_input})
            try:
                response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
                reply = response.choices[0].message.content
            except Exception as exc:  # pragma: no cover - API errors
                reply = f"API error: {exc}"
            messages.append({"role": "assistant", "content": reply})
            st.session_state["messages"] = messages
    for msg in st.session_state.get("messages", [])[1:]:
        st.write(f"**{msg['role'].capitalize()}:** {msg['content']}")
else:
    st.info("Select or create a persona to start chatting.")
