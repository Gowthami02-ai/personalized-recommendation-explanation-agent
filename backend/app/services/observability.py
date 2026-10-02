from typing import Any, Dict, List


class ObservabilityService:
    def __init__(self):
        self.events: List[Dict[str, Any]] = []

    def log_event(self, **payload: Any) -> None:
        self.events.append(payload)
