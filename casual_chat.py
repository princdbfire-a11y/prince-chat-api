"""
Casual chat tool.
Handles greetings and anything that doesn't match a specific tool.
This is where, later, your fine-tuned model will generate more natural,
friendly replies (including mixed Tamil-English). For now, it uses
simple rule-based responses so the server works end-to-end today.
"""

import random

GREETING_WORDS = ["hi", "hello", "hey", "vanakkam", "vannakam"]

FALLBACK_REPLIES = [
    "I'm still learning that one! For now I can help with calculations, letters, "
    "college info, and directions around campus.",
    "Hmm, I don't have an answer for that yet. Try asking me about your subjects, "
    "letters, or campus navigation!",
]


def handle_casual_chat(message: str, student_name: str) -> str:
    text = message.lower()

    if any(word in text for word in GREETING_WORDS):
        return f"Hi {student_name}! How can I help you today?"

    if "thank" in text:
        return "You're welcome! Let me know if you need anything else."

    return random.choice(FALLBACK_REPLIES)