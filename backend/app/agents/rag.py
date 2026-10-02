from typing import Any, Dict, List

from backend.app.rag.vector_store import KnowledgeVectorStore


def rag_retrieval_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    store = KnowledgeVectorStore()
    query = state.get("user_query", "")
    docs = store.search_documents(query=query, limit=5)

    state["retrieved_documents"] = [
        {
            "document_id": doc["document_id"],
            "title": doc["title"],
            "source": doc["source"],
            "section": doc["metadata"].get("section", "general"),
            "excerpt": doc["content"],
            "page": doc["metadata"].get("page"),
            "version": doc["metadata"].get("version"),
            "effective_date": doc["metadata"].get("effective_date"),
        }
        for doc in docs
    ]
    return state
