"""
Navigation tool.
EDIT the LOCATIONS dictionary below with your real campus locations/directions.
"""

LOCATIONS = {
    "library": "The library is on the ground floor, next to the main entrance.",
    "principal": "The Principal's office is on the first floor, Block A, Room 101.",
    "accounts": "The Accounts/Accountancy department is on the ground floor, Block A.",
    "computer science": "The Computer Science department is on the second floor, Block B.",
    # Add more departments/locations here
}


def handle_navigation(message: str) -> str:
    text = message.lower()

    for key, directions in LOCATIONS.items():
        if key in text:
            return directions

    return (
        "I'm not sure about that exact location yet. Could you tell me the "
        "department or place name again? (e.g., library, principal's office, "
        "accounts department)"
    )