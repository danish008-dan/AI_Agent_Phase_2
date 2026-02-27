from groq import Groq
from phase_two.config.settings import (
    GROQ_API_KEY,
    MODEL_NAME,
    MAX_TOKENS,
    TEMPERATURE,
    TOP_P
)
from phase_two.brain.system_prompt import SYSTEM_PROMPT
from phase_two.memory.conversation_memory import get_memory, add_to_memory


client = Groq(api_key=GROQ_API_KEY)


def generate_ai_response(user_message):
    """
    Sends user query to Groq with conversation memory
    """

    try:

        # Add user message to memory
        add_to_memory("user", user_message)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # Add conversation history
        messages.extend(get_memory())

        chat_completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            top_p=TOP_P
        )

        response = chat_completion.choices[0].message.content

        # Save AI response in memory
        add_to_memory("assistant", response)

        return response

    except Exception as e:
        print("AI Error:", e)
        return "Sorry, something went wrong while generating response."