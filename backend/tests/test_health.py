from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat():
    response = client.post(
        "/api/chat",
        json={
            "session_id": "s-001",
            "user_id": "u-001",
            "message": "Explain why this product is recommended for me.",
            "conversation_history": [],
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert "final_response" in payload
