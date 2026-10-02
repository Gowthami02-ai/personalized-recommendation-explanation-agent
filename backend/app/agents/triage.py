from typing import Any, Dict, List

from backend.app.models.schemas import TriageResult


class SupervisorAgent:
    def __init__(self):
        self.name = "supervisor"

    def handle(self, state: Dict[str, Any]) -> Dict[str, Any]:
        state.setdefault("errors", [])
        return state


def triage_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    user_query = state.get("user_query", "")
    text = user_query.lower()
    intent = "recommendation_explanation"
    if "refund" in text or "return" in text:
        intent = "return_or_refund"
    if "size" in text or "fit" in text:
        intent = "fit_support"

    triage = TriageResult(
        intent=intent,
        category="shopping_experience",
        priority="normal",
        entities={"query": user_query},
        missing_information=[],
        confidence=0.88,
        recommended_route="retrieval",
    )
    state["intent"] = triage.model_dump()
    return state
