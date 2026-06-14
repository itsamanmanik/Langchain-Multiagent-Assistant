from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage


SYSTEM_PROMPT = """You are a meticulous code reviewer and debugging agent.
You will receive a user's original request and a piece of Python code written by a coder agent.

Your job:
1. Review the code for bugs, logical errors, or missing edge case handling
2. Check if it fully satisfies the user's request
3. Return the corrected, improved code

Rules:
- Output the final corrected code block (use ```python ... ```)
- Below the code, add a short "🐛 Debug Notes:" section listing what you fixed or confirmed
- If the code is already correct, still return it with a note saying "No issues found" """


def run_debugger(user_request: str, code: str, model: str = "llama3") -> str:
    llm = ChatOllama(model=model, temperature=0.1)
    prompt = f"""User's Original Request:
{user_request}

Code to Review:
{code}

Review, debug, and return the final corrected code."""

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ]
    response = llm.invoke(messages)
    return response.content
