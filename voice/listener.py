import speech_recognition as sr

def listen():
    print("Available microphones:\n")

    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{i}: {name}")

    return ""