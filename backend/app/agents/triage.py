from typing import Any, Dict

from backend.app.models.schemas import TriageResult


def triage_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    user_query = state.get("user_query", "")
    lower_query = user_query.lower()

    intent = "recommendation_explanation"
    if "refund" in lower_query or "return" in lower_query:
        intent = "refund_support"
    elif "size" in lower_query or "fit" in lower_query:
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
