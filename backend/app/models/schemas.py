from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class ChatRequest(BaseModel):
    session_id: str = Field(default="session-default")
    user_id: str = Field(default="user-unknown")
    message: str
    conversation_history: Optional[List[ChatMessage]] = Field(default_factory=list)


class TriageResult(BaseModel):
    intent: str
    category: str
    priority: str
    entities: Dict[str, Any] = Field(default_factory=dict)
    missing_information: List[str] = Field(default_factory=list)
    confidence: float = 0.0
    recommended_route: str


class SourceCitation(BaseModel):
    document_id: str
    title: str
    source: str
    section: str
    excerpt: str
    page: Optional[str] = None
    version: Optional[str] = None
    effective_date: Optional[str] = None


class ValidationResult(BaseModel):
    status: Literal["PASS", "RETRY", "HUMAN_REVIEW", "BLOCK"]
    reasons: List[str] = Field(default_factory=list)
    needs_human_review: bool = False


class ChatResponse(BaseModel):
    session_id: Optional[str]
    final_response: str
    confidence: float
    validation_result: str
    evidence: List[Dict[str, Any]] = Field(default_factory=list)
    citations: List[SourceCitation] = Field(default_factory=list)


class SessionSnapshot(BaseModel):
    session_id: str
    status: str
    workflow_id: Optional[str] = None
