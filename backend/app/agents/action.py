from typing import Any, Dict, List


def action_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    proposed = [
        {
            "action": "create_support_case",
            "status": "not_executed",
            "reason": "No support case required for a recommendation explanation request.",
        }
    ]
    state["proposed_actions"] = proposed
    return state
