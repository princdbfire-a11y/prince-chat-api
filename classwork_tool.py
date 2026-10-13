"""
Classwork tool (v2 — context-aware).
Knows WHO is asking (student_id) and can answer:
  - "any classwork?"              -> latest items, marked submitted/pending
  - "any pending/due assignments?" -> only items this student hasn't submitted
  - "did I submit <title>?"        -> checks their actual submission for that item
  - "computer science classwork"   -> filtered by department mentioned
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


def _submitted_ids(cursor, student_id):
    if not student_id:
        return set()
    cursor.execute(
        "SELECT classwork_id FROM classwork_submissions WHERE student_id = %s",
        (student_id,)
    )
    return {row["classwork_id"] for row in cursor.fetchall()}


def handle_classwork(message: str, student_id=None, student_department: str = None) -> str:
    text = message.lower()
    mentioned_dept = _find_department_in_message(text)
    asking_pending = any(w in text for w in ["pending", "due", "not submitted", "haven't submitted", "left"])
    asking_submitted = any(w in text for w in ["did i submit", "have i submitted", "already submitted", "my submission"])

    try:
        conn = _connect()
        cursor = conn.cursor(dictionary=True)

        # Build the base query
        where_clauses = []
        params = []

        if mentioned_dept:
            where_clauses.append("(department = 'All' OR LOWER(department) LIKE %s)")
            params.append(f"%{mentioned_dept}%")
        elif student_department:
            where_clauses.append("(department = 'All' OR department = %s)")
            params.append(student_department)

        where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""
        cursor.execute(
            f"SELECT id, title, type, department, due_date, created_at FROM classwork "
            f"{where_sql} ORDER BY created_at DESC LIMIT 10",
            tuple(params)
        )
        rows = cursor.fetchall()

        submitted = _submitted_ids(cursor, student_id)
        cursor.close()
        conn.close()
    except Exception:
        return "Sorry, I couldn't fetch classwork right now. Please check the Classwork page."

    if not rows:
        return "There's no classwork posted right now for that." if mentioned_dept else "There's no classwork posted right now."

    # Filter for pending-only if asked
    if asking_pending:
        rows = [r for r in rows if r["type"] != "material" and r["id"] not in submitted]
        if not rows:
            return "You're all caught up — no pending classwork right now! 🎉"
        reply = "Here's your pending classwork:\n\n"
        for r in rows[:5]:
            due = f" (Due: {r['due_date']})" if r["due_date"] else ""
            reply += f"- [{r['type'].title()}] {r['title']} ({r['department']}){due}\n"
        return reply.strip()

    # If asking about a specific submission status
    if asking_submitted:
        for r in rows:
            if r["title"].lower() in text or text in r["title"].lower():
                status = "✔ Yes, you've already submitted this." if r["id"] in submitted else "You haven't submitted this yet."
                return f"{r['title']}: {status}"
        return "I couldn't find that specific classwork item. Could you tell me the exact title?"

    # Default: list latest items with status
    reply = "Here's the latest classwork:\n\n"
    for r in rows[:5]:
        due = f" (Due: {r['due_date']})" if r["due_date"] else ""
        if r["type"] == "material":
            status = ""
        elif r["id"] in submitted:
            status = " — ✔ Submitted"
        else:
            status = " — Pending"
        reply += f"- [{r['type'].title()}] {r['title']} ({r['department']}){due}{status}\n"

    return reply.strip()