# phase_two/core/input_handler.py

from phase_one.modules.audio_to_text import record_from_microphone


def get_user_input():
    """
    Handles text or voice input
    """

    print("\nSelect Input Mode:")
    print("1 Text Input")
    print("2 Voice Input")
    print("0 Exit")

    choice = input("Enter choice: ").strip().lower()

    # Exit directly from input screen
    if choice in ["0", "exit", "quit"]:
        return "exit"

    # TEXT INPUT
    if choice == "1":
        user_text = input("You: ")
        return user_text

    # VOICE INPUT
    elif choice == "2":
        print("Recording voice...")

        spoken_text = record_from_microphone()

        if not spoken_text:
            print("Speech not understood.")
            return None

        print("You (voice):", spoken_text)

        return spoken_text

    else:
        print("Invalid input")
        return None