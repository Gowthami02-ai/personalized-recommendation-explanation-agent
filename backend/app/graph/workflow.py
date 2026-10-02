from typing import Any, Dict

from langgraph.graph import END, START, StateGraph

from backend.app.agents.action import action_agent
from backend.app.agents.investigation import investigation_agent
from backend.app.agents.rag import rag_retrieval_agent
from backend.app.agents.response import response_agent
from backend.app.agents.retrieval import retrieval_agent
from backend.app.agents.triage import triage_agent
from backend.app.agents.validator import validation_agent


def route_after_triage(state: Dict[str, Any]) -> str:
    if state.get("intent", {}).get("missing_information"):
        return "response"
    return "retrieval"


def route_after_validation(state: Dict[str, Any]) -> str:
    status = state.get("validation_result", "PENDING").upper()
    if status == "PASS":
        return "response"
    if status == "HUMAN_REVIEW":
        return "action"
    if status == "RETRY":
        return "retrieval"
    return "response"


def build_workflow():
    workflow = StateGraph(dict)

    workflow.add_node("triage", triage_agent)
    workflow.add_node("retrieval", retrieval_agent)
    workflow.add_node("rag", rag_retrieval_agent)
    workflow.add_node("investigation", investigation_agent)
    workflow.add_node("action", action_agent)
    workflow.add_node("validation", validation_agent)
    workflow.add_node("response", response_agent)

    workflow.add_edge(START, "triage")
    workflow.add_conditional_edges("triage", route_after_triage, {"response": "response", "retrieval": "retrieval"})
    workflow.add_edge("retrieval", "rag")
    workflow.add_edge("rag", "investigation")
    workflow.add_edge("investigation", "validation")
    workflow.add_conditional_edges("validation", route_after_validation, {"response": "response", "action": "action", "retrieval": "retrieval"})
    workflow.add_edge("action", "response")
    workflow.add_edge("response", END)
    return workflow
