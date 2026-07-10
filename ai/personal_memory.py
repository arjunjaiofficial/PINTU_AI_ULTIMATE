import re
from database.user_memory import remember, recall


def save_personal_memory(user_input):
    text = user_input.strip()

    patterns = [
        r"remember my (.+?) is (.+)",
        r"my (.+?) is (.+)"
    ]

    for pattern in patterns:
        match = re.fullmatch(pattern, text, re.IGNORECASE)

        if match:
            key = match.group(1).strip().lower()
            value = match.group(2).strip()

            remember(key, value)

            return key

    return None


def get_personal_memory(user_input):
    text = user_input.strip().lower()

    patterns = [
        r"what is my (.+)",
        r"what's my (.+)",
        r"tell me my (.+)",
        r"when is my (.+)"
    ]

    for pattern in patterns:
        match = re.fullmatch(pattern, text)

        if match:
            key = match.group(1).strip().rstrip("?")

            value = recall(key)

            if value:
                return key, value

    return None