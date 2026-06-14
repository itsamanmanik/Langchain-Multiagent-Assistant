from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents import run_planner, run_coder, run_debugger


# ── State shared across all agents ──────────────────────────────────────────
class AgentState(TypedDict):
    user_request: str
    model: str
    plan: str
    code: str
    final_code: str


# ── Node functions ───────────────────────────────────────────────────────────
def planner_node(state: AgentState) -> AgentState:
    plan = run_planner(state["user_request"], model=state["model"])
    return {**state, "plan": plan}


def coder_node(state: AgentState) -> AgentState:
    code = run_coder(state["user_request"], state["plan"], model=state["model"])
    return {**state, "code": code}


def debugger_node(state: AgentState) -> AgentState:
    final_code = run_debugger(state["user_request"], state["code"], model=state["model"])
    return {**state, "final_code": final_code}


# ── Build the graph ──────────────────────────────────────────────────────────
def build_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("coder", coder_node)
    graph.add_node("debugger", debugger_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "coder")
    graph.add_edge("coder", "debugger")
    graph.add_edge("debugger", END)

    return graph.compile()


# ── Public runner ────────────────────────────────────────────────────────────
def run_pipeline(user_request: str, model: str = "llama3") -> AgentState:
    app = build_graph()
    initial_state: AgentState = {
        "user_request": user_request,
        "model": model,
        "plan": "",
        "code": "",
        "final_code": "",
    }
    return app.invoke(initial_state)
