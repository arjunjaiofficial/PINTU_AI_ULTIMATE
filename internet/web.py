import webbrowser

def web_command(command):

    cmd = command.lower()

    if cmd == "open youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif cmd == "open google":
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif cmd == "open chatgpt":
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT."

    elif cmd == "open gmail":
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    elif cmd.startswith("search "):
        query = command[7:]
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}."

    return None