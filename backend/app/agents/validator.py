from typing import Any, Dict


def validation_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    investigation = state.get("investigation_result", {})
    docs = state.get("retrieved_documents", [])
    reasons = []
    if not investigation.get("evidence"):
        reasons.append("Missing evidence")
    if not docs:
        reasons.append("No grounded documentation retrieved")
    if investigation.get("confidence", 0) < 0.6:
        reasons.append("Low confidence")

    if reasons:
        status = "RETRY"
        if "Low confidence" in reasons:
            status = "HUMAN_REVIEW"
    else:
        status = "PASS"

    state["validation_result"] = status
    return state
