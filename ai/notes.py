from database.notes import add_note, get_notes


def save_note(user_input):
    text = user_input.strip()

    if not text.lower().startswith("take note "):
        return False

    note = text[10:].strip()

    if not note:
        return False

    add_note(note)

    return True


def show_notes():
    notes = get_notes()

    if not notes:
        return "You don't have any notes."

    result = []

    for note in notes:
        result.append(f"{note.id}. {note.content}")

    return "\n".join(result)