from typing import Any, Dict, List


class KnowledgeVectorStore:
    def __init__(self):
        self.documents = [
            {
                "document_id": "doc-001",
                "title": "Recommendation quality policy",
                "source": "policy-manual",
                "content": "Recommendations must be grounded in verified product and customer attributes. Do not invent missing facts.",
                "metadata": {"section": "quality", "version": "v1", "effective_date": "2025-09-01"},
            },
            {
                "document_id": "doc-002",
                "title": "Customer explanation best practices",
                "source": "operations-manual",
                "content": "Explanations should cite product attributes, constraints, and evidence while protecting sensitive logic.",
                "metadata": {"section": "explanations", "version": "v1", "effective_date": "2025-08-15"},
            },
        ]

    def add_documents(self, docs: List[Dict[str, Any]]) -> None:
        self.documents.extend(docs)

    def search_documents(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        query_l = query.lower()
        matches = []
        for doc in self.documents:
            if query_l in doc["content"].lower() or query_l in doc["title"].lower():
                matches.append(doc)
        return matches[:limit]
