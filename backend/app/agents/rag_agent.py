from typing import Any, Dict


class KnowledgeBaseError(RuntimeError):
    pass


class RAGAgent:
    def __init__(self):
        self.name = "rag_agent"

    def answer(self, query: str, docs: list[dict]) -> str:
        if not docs:
            return "No grounded documents were found for the request."
        return "Grounded answer generated from retrieved knowledge."
