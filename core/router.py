from ai.learning import learn, get_knowledge
from ai.personal_memory import save_personal_memory, get_personal_memory
from ai.notes import save_note, show_notes
from desktop.control import open_app
from internet.web import web_command
from core.brain import think
from voice.speaker import speak


def handle_command(user, name):
    cmd = user.lower().strip()

    # Exit
    if cmd == "exit":
        speak(f"Goodbye {name}")
        return False

    # Name
    if cmd == "what is my name":
        speak(f"Your name is {name}")
        return True

    # ---------------- PERSONAL MEMORY ----------------

    saved = save_personal_memory(user)

    if saved:
        speak(f"Okay, I'll remember your {saved}.")
        return True

    result = get_personal_memory(user)

    if result:
        key, value = result
        speak(f"Your {key} is {value}.")
        return True

    # ---------------- NOTES ----------------

    if save_note(user):
        speak("Note saved.")
        return True

    if cmd == "show notes":
        notes = show_notes()

        print("\nPINTU AI:")
        print(notes)

        speak(notes)
        return True

    # ---------------- KNOWLEDGE ----------------

    if cmd.startswith("learn "):
        try:
            text = user[6:]
            topic, info = text.split("=", 1)

            learn(topic.strip(), info.strip())
            speak(f"I learned about {topic.strip()}")

        except ValueError:
            speak("Please use: learn topic = information")

        return True

    if cmd.startswith("what do you know about "):
        topic = cmd.replace("what do you know about ", "", 1).strip()

        info = get_knowledge(topic)

        if info:
            speak(info)
        else:
            speak("I don't know that yet.")

        return True

    # ---------------- DESKTOP ----------------

    result = open_app(cmd)

    if result:
        speak(result)
        return True

    # ---------------- INTERNET ----------------

    result = web_command(user)

    if result:
        speak(result)
        return True

    # ---------------- AI ----------------

    reply = think(user)

    print("PINTU AI:", reply)
    speak(reply)

    return True