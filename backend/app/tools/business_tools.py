from typing import Any, Dict, List


def get_customer_profile(customer_id: str) -> Dict[str, Any]:
    return {
        "customer_id": customer_id,
        "name": "Alicia Wells",
        "preferences": ["budget-friendly", "eco-conscious"],
        "constraints": ["Under $600", "Needs easy setup"],
    }


def get_product_catalog(query: str) -> List[Dict[str, Any]]:
    return [
        {
            "product_id": "SKU-1001",
            "name": "EcoSmart Home Speaker",
            "price": 449.99,
            "attributes": ["portable", "wireless", "budget-friendly", "eco-certified"],
            "compatibility": ["smart home hub"],
        }
    ]


def get_inventory_lookup(product_id: str) -> Dict[str, Any]:
    return {"product_id": product_id, "status": "in_stock", "warehouse": "W-12"}
