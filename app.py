"""
PRINCE Local AI Server
-----------------------
This is your own AI backend. It runs on YOUR machine, not on Gemini/OpenAI.
It receives a message from chat_api.php, decides which "tool" should handle it,
and returns a reply. No data ever leaves this server.

HOW TO RUN:
1. Install Python 3.10+ (https://www.python.org/downloads/)
2. Open terminal/cmd in this folder and run:
       pip install flask
3. Run:
       python app.py
4. Server starts at http://127.0.0.1:5005

Your chat_api.php will call this instead of Gemini's API.
"""

from flask import Flask, request, jsonify
import re

from tools.calculator import handle_calculator
from tools.letter_writer import handle_letter
from tools.college_info import handle_college_info
from tools.navigation import handle_navigation
from tools.casual_chat import handle_casual_chat
from tools.announcements_tool import handle_announcements
from tools.classwork_tool import handle_classwork

app = Flask(__name__)

# ---------------------------------------------------------
# STEP 1: Intent detection
# This looks at the student's message and decides which tool should handle it.
# This is a simple keyword-based router for now.
# Later, once you fine-tune a real model, THIS function is what the
# trained model will replace/improve — it will "decide" more smartly.
# ---------------------------------------------------------
def detect_intent(message: str) -> str:
    text = message.lower()

    if re.search(r'\d+\s*[\+\-\*/x×]\s*\d+', text) or "calculate" in text or "percentage" in text:
        return "calculator"

    if any(word in text for word in ["leave letter", "request letter", "apology letter", "write a letter"]):
        return "letter"

    if any(word in text for word in ["library", "principal", "office", "department", "how to reach", "where is", "which floor"]):
        return "navigation"

    if any(word in text for word in ["prince", "college", "history", "staff", "hod", "who is", "about our college"]):
        return "college_info"

    if any(word in text for word in ["announcement", "announcements", "notice", "update", "notification"]):
        return "announcements"

    if any(word in text for word in ["classwork", "assignment", "assignments", "homework", "quiz", "quizzes", "submission"]):
        return "classwork"

    # Fallback: casual chat / anything else
    return "casual_chat"


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True)
    message = data.get("message", "").strip()
    student_name = data.get("student_name", "Student")

    if not message:
        return jsonify({"reply": "Please type a question."})

    intent = detect_intent(message)

    if intent == "calculator":
        reply = handle_calculator(message)
    elif intent == "letter":
        reply = handle_letter(message)
    elif intent == "navigation":
        reply = handle_navigation(message)
    elif intent == "college_info":
        reply = handle_college_info(message)
    elif intent == "announcements":
        reply = handle_announcements(message)
    elif intent == "classwork":
        reply = handle_classwork(message)
    else:
        reply = handle_casual_chat(message, student_name)

    return jsonify({"reply": reply, "intent": intent})


if __name__ == "__main__":
    # Runs locally only — not exposed to the internet.
    app.run(host="127.0.0.1", port=5005, debug=True)