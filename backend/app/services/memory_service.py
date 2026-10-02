from typing import Any, Dict, Optional


class MemoryService:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        return self.sessions.get(session_id)

    def save_session(self, session_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        self.sessions[session_id] = data
        return data

    def append_message(self, session_id: str, message: Dict[str, Any]) -> None:
        session = self.sessions.setdefault(session_id, {"messages": []})
        session.setdefault("messages", []).append(message)
