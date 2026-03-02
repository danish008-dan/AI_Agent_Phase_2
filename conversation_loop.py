from phase_two.core.input_handler import get_user_input
from phase_two.core.response_handler import deliver_response
from phase_two.brain.groq_client import generate_ai_response
from phase_two.config.settings import EXIT_COMMANDS


def start_conversation():
    """
    Main AI Agent Loop
    """

    print("\nUltra Fast AI Agent Started")
    print("Type 'exit' anytime to stop\n")

    while True:
        user_query = get_user_input()

        if not user_query:
            continue

        if user_query.lower() in EXIT_COMMANDS:
            print("\nStopping AI Agent...")
            break

        ai_response = generate_ai_response(user_query)

        deliver_response(ai_response)