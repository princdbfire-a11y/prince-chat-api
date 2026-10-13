"""
Calculator tool.
Handles simple math questions like "what's 45*12" or "calculate 200+350".
Does NOT use the AI model for math (small models are bad at arithmetic) -
uses Python's own safe math evaluation instead.
"""

import re


def handle_calculator(message: str) -> str:
    # Pull out only number/operator tokens, ignoring surrounding words like "what is"
    tokens = re.findall(r'\d+\.?\d*|[+\-*/x()]', message)
    if not tokens:
        return "I couldn't find a calculation in your message. Try something like 'what is 45*12'."

    expr = "".join(tokens)
    expr = expr.replace("x", "*")
    expr = expr.strip()

    # Only allow safe characters (numbers and math operators) - never eval raw user text
    if not re.fullmatch(r'[\d.+\-*/()]+', expr):
        return "Sorry, I can only calculate simple math expressions right now."

    try:
        result = eval(expr, {"__builtins__": {}}, {})
        return f"The answer is {result}"
    except Exception:
        return "Sorry, I couldn't calculate that. Please check the expression."