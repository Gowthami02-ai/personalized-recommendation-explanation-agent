from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.config import settings
from backend.app.graph.workflow import build_workflow
from backend.app.models.schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="Personalized Recommendation Explanation Agent",
    description="Multi-agent recommendation explanation system using LangGraph, FastAPI, retrieval, and guardrails.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = build_workflow()


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "personalized-recommendation-explanation-agent"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    state = workflow.invoke(
        {
            "session_id": request.session_id,
            "user_id": request.user_id,
            "user_query": request.message,
            "conversation_history": [m.model_dump() for m in request.conversation_history],
            "intent": {},
            "entities": {},
            "retrieved_data": {},
            "retrieved_documents": [],
            "investigation_result": {},
            "proposed_actions": [],
            "tool_results": [],
            "confidence": 0.0,
            "validation_result": "PENDING",
            "human_approval": {},
            "errors": [],
            "final_response": "",
        }
    )

    return ChatResponse(
        session_id=state.get("session_id"),
        final_response=state.get("final_response", ""),
        confidence=float(state.get("confidence", 0.0)),
        validation_result=state.get("validation_result", "PENDING"),
        evidence=state.get("investigation_result", {}).get("evidence", []),
        citations=state.get("retrieved_documents", []),
    )


@app.get("/api/sessions/{session_id}")
def get_session(session_id: str):
    return {"session_id": session_id, "status": "active"}


@app.get("/api/workflows/{workflow_id}")
def get_workflow(workflow_id: str):
    return {"workflow_id": workflow_id, "status": "running"}


@app.post("/api/approval/{workflow_id}")
def submit_approval(workflow_id: str):
    return {"workflow_id": workflow_id, "approval_status": "pending"}


@app.get("/api/metrics")
def metrics():
    return {"requests": 0, "status": "ok"}


@app.get("/")
def root():
    return {"message": "Personalized Recommendation Explanation Agent API"}
