from openai import OpenAI
from ai.conversation import remember_chat, get_chat_history

# Connect to local Ollama server
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama",
    timeout=60
)

SYSTEM_PROMPT = """
You are PINTU AI.

You are a smart, friendly, and helpful personal AI assistant.

Rules:
- Answer clearly and naturally.
- Keep answers concise unless the user asks for details.
- If you don't know something, say so honestly.
- Address the user as "Arjun Jai" when appropriate.
"""


def think(user_input):
    try:
        # Save user's message
        remember_chat("user", user_input)

        # Load recent conversation
        history = get_chat_history()

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(history)

        response = client.chat.completions.create(
            model="qwen2.5:3b",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )

        reply = response.choices[0].message.content.strip()

        # Save AI response
        remember_chat("assistant", reply)

        return reply

    except Exception as e:
        return f"Error: {str(e)}"