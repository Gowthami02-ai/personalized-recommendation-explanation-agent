from typing import Any, Dict, List

from backend.app.tools.business_tools import get_customer_profile, get_inventory_lookup, get_product_catalog


def retrieval_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    query = state.get("user_query", "")
    customer_id = state.get("user_id", "CUST-1001")
    customer = get_customer_profile(customer_id)
    product_matches = get_product_catalog(query)
    inventory = get_inventory_lookup(product_matches[0].get("product_id") if product_matches else "SKU-1001")

    state["retrieved_data"] = {
        "customer": customer,
        "products": product_matches,
        "inventory": inventory,
    }
    state["tool_results"] = [
        {"tool": "get_customer_profile", "result": customer},
        {"tool": "get_product_catalog", "result": product_matches},
        {"tool": "get_inventory_lookup", "result": inventory},
    ]
    return state
