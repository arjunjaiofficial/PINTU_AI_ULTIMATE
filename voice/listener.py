import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=2)

        try:
            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text

        except sr.WaitTimeoutError:
            print("PINTU AI: I didn't hear anything.")
            return ""

        except sr.UnknownValueError:
            print("PINTU AI: Sorry, I couldn't understand.")
            return ""

        except sr.RequestError:
            print("PINTU AI: Internet is required.")
            return ""