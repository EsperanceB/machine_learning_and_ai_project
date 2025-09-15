import os
import json
import pathlib
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
from persona_creator import Persona

PERSONA_DIR = pathlib.Path("ai_personas_creation_automation_gpt/personas")

# Helper to load persona by name

def load_persona(name: str) -> Persona:
    file = PERSONA_DIR / f"{name.lower().replace(' ', '_')}.json"
    if not file.exists():
        raise FileNotFoundError(f"Persona '{name}' not found.")
    with file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        # Remove extra keys not accepted by Persona
        data.pop("prompt_template", None)
        return Persona(**data)

def main():
    print("Available personas:")
    personas = [p.stem.replace('_', ' ').title() for p in PERSONA_DIR.glob("*.json")]
    for idx, name in enumerate(personas):
        print(f"{idx+1}. {name}")
    persona_idx = int(input("Select persona by number: ")) - 1
    persona = load_persona(personas[persona_idx])
    print(f"Loaded persona: {persona.name}")


    # Robust TTS engine initialization: try all voices, skip any that fail
    engine = None
    try:
        engine = pyttsx3.init(driverName='espeak')
        voices = engine.getProperty('voices')
        print("Available voices:")
        for idx, voice in enumerate(voices):
            print(f"{idx}: {voice.name} ({voice.id})")
        # Try all voices until one works
        for idx, voice in enumerate(voices):
            try:
                print(f"Trying voice {idx}: {voice.id}")
                engine.setProperty('voice', voice.id)
                engine.say("Testing voice.")
                engine.runAndWait()
                print(f"Voice {voice.id} works!")
                break
            except Exception as ve:
                print(f"Voice {voice.id} failed: {ve}")
        else:
            print("No working voices found. TTS will be disabled.")
            engine = None
    except Exception as tts_init_error:
        print(f"TTS engine initialization error: {tts_init_error}")
        engine = None

    # Try to initialize microphone, fallback to text input if not available
    recognizer = sr.Recognizer()
    client = OpenAI()
    mic_available = True
    try:
        with sr.Microphone() as mic:
            pass
    except (OSError, AttributeError):
        mic_available = False
        print("No microphone detected. Falling back to text input mode.")

    print("Say 'quit' or 'exit' to end the conversation.")
    while True:
        try:
            if mic_available:
                with sr.Microphone() as mic:
                    print("Listening...")
                    audio = recognizer.listen(mic)
                try:
                    user_text = recognizer.recognize_google(audio)
                    print(f"You said: {user_text}")
                except sr.UnknownValueError:
                    print("Sorry, I did not understand that.")
                    continue
                except sr.RequestError as e:
                    print(f"Speech recognition error: {e}")
                    continue
            else:
                user_text = input("You: ")

            if user_text.strip().lower() in ["quit", "exit"]:
                print("Exiting. Goodbye!")
                break

            messages = [
                {"role": "system", "content": persona.build_prompt()},
                {"role": "user", "content": user_text},
            ]
            try:
                reply = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
                bot_text = reply.choices[0].message["content"]
            except Exception as e:
                print(f"OpenAI API error: {e}")
                continue

            print(f"Bot: {bot_text}")
            try:
                if engine:
                    engine.say(bot_text)
                    engine.runAndWait()
            except Exception as e:
                print(f"Speech synthesis error: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted by user. Exiting.")
            break

if __name__ == "__main__":
    main()
