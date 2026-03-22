# phase_two/core/response_handler.py


from phase_one.modules.text_to_audio import convert_text_to_audio
from playsound3 import playsound


def deliver_response(response_text):
    """
    Prints response and converts it to audio
    """

    print("\nAI:", response_text)

    try:
        # Convert response to audio
        audio_path = convert_text_to_audio(response_text)

        print("Audio saved:", audio_path)

        # Play audio immediately
        playsound(audio_path)

    except Exception as e:
        print("Audio Error:", e)