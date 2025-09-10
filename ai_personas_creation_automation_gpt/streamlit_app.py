# This app will allow you to input your persona specifications
import streamlit as st
from persona_creator import Persona, save_persona

st.title("GPT Persona Builder")

name = st.text_input("Persona name")
role = st.text_input("Role (e.g., voice assistant, mentor)")
task = st.text_area("Main task")
tone = st.text_input("Communication tone (e.g., friendly, professional)")
constraints = st.text_input("Constraints or threats")

if st.button("Create Persona"):
    persona = Persona(name, role, task, tone, constraints)
    path = save_persona(persona)
    st.success(f"Persona saved to {path}")
    st.json(persona.to_dict())
