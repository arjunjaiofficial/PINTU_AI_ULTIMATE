from database.conversation import save_message, get_recent_messages


def remember_chat(role, message):
    save_message(role, message)


def get_chat_history(limit=20):
    chats = get_recent_messages(limit)

    history = []

    for chat in chats:
        history.append({
            "role": chat.role,
            "content": chat.message
        })

    return history