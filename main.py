from database.user_memory import remember, recall
from voice.speaker import speak
from voice.listener import listen
from core.router import handle_command


print("=" * 45)
print("         PINTU AI ULTIMATE")
print("=" * 45)

name = recall("name")

if not name:
    name = input("What is your name? : ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("What is your name? : ").strip()

    remember("name", name)
    speak("I will remember your name forever.")

print(f"Welcome back, {name}! 👋")
speak(f"Welcome back {name}")

print("PINTU AI is ONLINE.")
print("Type:")
print("  text  -> keyboard")
print("  voice -> microphone")
print("  exit  -> close")


while True:

    mode = input("\nMode (text/voice): ").strip().lower()

    if mode == "exit":
        speak(f"Goodbye {name}")
        break

    if mode == "text":
        user = input(f"{name}: ").strip()

    elif mode == "voice":
        user = listen()

        if not user:
            continue

    else:
        print("Please type text or voice.")
        continue

    if user.lower().strip() == "exit":
        speak(f"Goodbye {name}")
        break

    if handle_command(user, name) is False:
        break