from typing import Any, Dict


def response_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    intent = state.get("intent", {})
    investigation = state.get("investigation_result", {})
    docs = state.get("retrieved_documents", [])
    product = (state.get("retrieved_data", {}).get("products") or [{}])[0]

    response = (
        f"Based on the available evidence, the recommendation for {product.get('name', 'the product')} is grounded in "
        f"customer constraints and verified product attributes. The intent was classified as '{intent.get('intent', 'recommendation_explanation')}'. "
        f"Evidence: {', '.join(investigation.get('evidence', []))}. "
        f"Sources reviewed: {len(docs)} document(s)."
    )

    state["final_response"] = response
    return state
