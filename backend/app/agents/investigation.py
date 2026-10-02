from typing import Any, Dict


def investigation_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    retrieved_data = state.get("retrieved_data", {})
    customer = retrieved_data.get("customer", {})
    products = retrieved_data.get("products", [])
    inventory = retrieved_data.get("inventory", {})

    product = products[0] if products else {"name": "unknown product"}
    findings = {
        "issue_type": "recommendation_explanation",
        "evidence": [
            f"Customer constraints: {customer.get('constraints', [])}",
            f"Recommended product: {product.get('name', 'unknown product')}",
            f"Inventory status: {inventory.get('status', 'unknown')}",
        ],
        "policy_reference": [
            "Recommendation quality policy",
            "Customer explanation best practices",
        ],
        "recommended_action": "Explain the recommendation using verified attributes and customer constraints.",
        "confidence": 0.92,
        "requires_human_review": False,
    }

    state["investigation_result"] = findings
    state["confidence"] = findings["confidence"]
    return state
