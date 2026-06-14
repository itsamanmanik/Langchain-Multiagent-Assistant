from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage


SYSTEM_PROMPT = """You are an expert Python developer and coding agent.
You will receive a user's coding request along with a structured plan.

Your job is to write clean, efficient, well-commented Python code that fulfills the request.

Rules:
- Output ONLY the code block (use ```python ... ```)
- Add brief inline comments for clarity
- Follow PEP8 standards
- Do NOT include explanations outside the code block"""


def run_coder(user_request: str, plan: str, model: str = "llama3") -> str:
    llm = ChatOllama(model=model, temperature=0.2)
    prompt = f"""User Request:
{user_request}

Plan to follow:
{plan}

Now write the Python code."""

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ]
    response = llm.invoke(messages)
    return response.content
