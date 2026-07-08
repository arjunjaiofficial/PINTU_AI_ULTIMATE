import os

def open_app(command):

    command = command.lower()

    if command == "open notepad":
        os.system("start notepad")
        return "Opening Notepad."

    elif command == "open calculator":
        os.system("start calc")
        return "Opening Calculator."

    elif command == "open paint":
        os.system("start mspaint")
        return "Opening Paint."

    elif command == "open chrome":
        os.system("start chrome")
        return "Opening Chrome."

    return None