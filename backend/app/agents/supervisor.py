from typing import Any, Dict


class SupervisorAgent:
    def __init__(self):
        self.name = "supervisor"

    def handle(self, state: Dict[str, Any]) -> Dict[str, Any]:
        state.setdefault("errors", [])
        return state
