"""
Letter writer tool.
Generates formal letters (leave, request, apology) using templates.
You can expand these templates with more detail/variations later.
"""


def handle_letter(message: str) -> str:
    text = message.lower()

    if "leave" in text:
        reason = "personal reasons"
        if "fever" in text or "sick" in text or "ill" in text:
            reason = "fever and feeling unwell"

        return (
            "To,\nThe Principal,\n[Your College Name]\n\n"
            "Subject: Application for Leave\n\n"
            "Respected Sir/Madam,\n\n"
            f"I am writing to request leave due to {reason}. "
            "I kindly request you to grant me leave for [number of days] days, "
            "starting from [start date] to [end date].\n\n"
            "I will make sure to complete any missed academic work upon my return.\n\n"
            "Thank you for your consideration.\n\n"
            "Yours sincerely,\n[Your Name]\n[Your Class/Department]\n[Roll Number]"
        )

    if "apology" in text or "sorry" in text:
        return (
            "To,\nThe [Concerned Person/Professor],\n[Your College Name]\n\n"
            "Subject: Apology Letter\n\n"
            "Respected Sir/Madam,\n\n"
            "I sincerely apologize for [reason, e.g., submitting my assignment late]. "
            "This was unintentional, and I assure you it will not happen again.\n\n"
            "I request you to kindly excuse this lapse.\n\n"
            "Thank you for your understanding.\n\n"
            "Yours sincerely,\n[Your Name]\n[Your Class/Department]"
        )

    # Default: request letter
    return (
        "To,\nThe [Concerned Department/Office],\n[Your College Name]\n\n"
        "Subject: Request for [Purpose, e.g., Bonafide Certificate]\n\n"
        "Respected Sir/Madam,\n\n"
        "I kindly request you to issue [what you need] for the purpose of "
        "[reason]. I would be grateful if this could be processed at the earliest.\n\n"
        "Thank you for your time and consideration.\n\n"
        "Yours sincerely,\n[Your Name]\n[Your Class/Department]\n[Roll Number]"
    )