from core.brain import get_response
from data.memory import remember, recall
from ai.learning import learn, get_knowledge
from voice.speaker import speak
from voice.listener import listen
from desktop.control import open_app
from internet.web import web_command

print("=" * 45)
print("         PINTU AI ULTIMATE")
print("=" * 45)

name = recall("name")

if not name:
    name = input("What is your name? : ")
    remember("name", name)
    speak("I will remember your name forever.")

print(f"Welcome back, {name}! 👋")
speak(f"Welcome back {name}")

print("PINTU AI is ONLINE.")
print("Type:")
print("  text  -> keyboard")
print("  voice -> microphone")
print("  exit  -> close\n")

while True:

    mode = input("\nMode (text/voice): ").lower().strip()

    if mode == "exit":
        speak(f"Goodbye {name}")
        break

    if mode == "voice":
        user = listen()

        if user == "":
            continue
    else:
        user = input(f"{name}: ")

    cmd = user.lower().strip()

    if cmd == "exit":
        speak(f"Goodbye {name}")
        break

    if cmd == "what is my name":
        speak(f"Your name is {name}")
        continue

    if cmd.startswith("learn "):
        try:
            text = user[6:]
            topic, info = text.split("=", 1)

            learn(topic.strip(), info.strip())
            speak(f"I learned about {topic.strip()}")

        except ValueError:
            speak("Please use: learn topic = information")

        continue

    if cmd.startswith("what do you know about "):
        topic = cmd.replace("what do you know about ", "", 1).strip()

        info = get_knowledge(topic)

        if info:
            speak(info)
        else:
            speak("I don't know that yet.")

        continue

    # Desktop Commands
    result = open_app(cmd)
    if result:
        speak(result)
        continue

    # Internet Commands
    result = web_command(user)
    if result:
        speak(result)
        continue

    # AI Brain
    reply = get_response(user)
    speak(reply)