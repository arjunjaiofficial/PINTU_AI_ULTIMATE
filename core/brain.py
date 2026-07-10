from openai import OpenAI

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
        response = client.chat.completions.create(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"