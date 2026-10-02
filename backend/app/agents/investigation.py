from typing import Any, Dict


def investigation_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    retrieved_data = state.get("retrieved_data", {})
    customer = retrieved_data.get("customer", {})
    product = retrieved_data.get("products", [{}])[0]
    inventory = retrieved_data.get("inventory", {})

    findings = {
        "issue_type": "recommendation_explanation",
        "evidence": [
            f"Customer constraints: {customer.get('constraints', [])}",
            f"Recommended product: {product.get('name', 'Unknown product')}",
            f"Inventory status: {inventory.get('status', 'unknown')}",
        ],
        "policy_reference": [
            "Privacy-preserving recommendation policy",
            "Shopping explanation quality policy",
        ],
        "recommended_action": "Explain recommendation using verified product and customer attributes.",
        "confidence": 0.91,
        "requires_human_review": False,
    }
    state["investigation_result"] = findings
    state["confidence"] = findings["confidence"]
    return state
