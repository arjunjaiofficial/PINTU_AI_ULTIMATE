def get_response(message):
    message = message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "Hello Arjun Jai! 😊"

    elif "how are you" in message:
        return "I am doing great. Ready to help you anytime!"

    elif "who are you" in message:
        return (
            "I am PINTU AI Ultimate.\n"
            "Your Personal Intelligent Assistant."
        )

    elif "your name" in message:
        return "My name is PINTU AI."

    elif "thank you" in message:
        return "You're welcome, Arjun Jai!"

    else:
        return "I am still learning. Please teach me more."