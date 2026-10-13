"""
Announcements tool (v2 — context-aware).
Can filter by department mentioned in the message, or just return the latest ones
for the student's own department + 'All'.
"""

import mysql.connector

KNOWN_DEPARTMENTS = [
    "tamil", "english", "business administration", "bba", "biochemistry",
    "computer science", "visual communication", "commerce", "library science",
]


def _connect():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="prince_db"
    )


def _find_department_in_message(text: str):
    text = text.lower()
    for dept in KNOWN_DEPARTMENTS:
        if dept in text:
            return dept
    return None


def handle_announcements(message: str, student_department: str = None) -> str:
    text = message.lower()
    mentioned_dept = _find_department_in_message(text)

    try:
        conn = _connect()
        cursor = conn.cursor(dictionary=True)

        if mentioned_dept:
            # Explicit department asked about — show that department's + All
            cursor.execute(
                "SELECT title, message, department, created_at FROM announcements "
                "WHERE department = 'All' OR LOWER(department) LIKE %s "
                "ORDER BY created_at DESC LIMIT 5",
                (f"%{mentioned_dept}%",)
            )
        elif student_department:
            cursor.execute(
                "SELECT title, message, department, created_at FROM announcements "
                "WHERE department = 'All' OR department = %s "
                "ORDER BY created_at DESC LIMIT 5",
                (student_department,)
            )
        else:
            cursor.execute(
                "SELECT title, message, department, created_at FROM announcements "
                "ORDER BY created_at DESC LIMIT 5"
            )

        rows = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception:
        return "Sorry, I couldn't fetch announcements right now. Please check the Announcements page."

    if not rows:
        return "There are no announcements right now for that." if mentioned_dept else "There are no announcements right now."

    reply = "Here are the latest announcements:\n\n"
    for row in rows:
        reply += f"- {row['title']} ({row['department']}): {row['message']}\n"

    return reply.strip()