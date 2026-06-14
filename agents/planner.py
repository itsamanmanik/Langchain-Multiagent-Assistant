from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage


SYSTEM_PROMPT = """You are a senior software architect and planning agent.
Your job is to analyze a user's coding request and produce a clear, structured plan.

Respond with:
1. A brief understanding of the problem
2. A numbered step-by-step plan to solve it
3. Any edge cases or important notes to keep in mind

Be concise and technical. Do NOT write any code — only the plan."""


def run_planner(user_request: str, model: str = "llama3") -> str:
    llm = ChatOllama(model=model, temperature=0.2)
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_request),
    ]
    response = llm.invoke(messages)
    return response.content
