# phase_two/memory/conversation_memory.py

"""
Conversation Memory System
Stores recent conversation for context awareness
"""

# Memory storage
conversation_history = []

# Maximum memory size
MAX_MEMORY = 15


def add_to_memory(role, content):
    """
    Adds message to memory
    """

    global conversation_history

    conversation_history.append({
        "role": role,
        "content": content
    })

    # Keep memory size limited for speed
    if len(conversation_history) > MAX_MEMORY:
        conversation_history.pop(0)


def get_memory():
    """
    Returns memory messages
    """

    return conversation_history