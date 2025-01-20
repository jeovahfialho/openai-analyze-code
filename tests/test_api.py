from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_analyze_code():
    code = """
def test_function():
    pass
    """
    response = client.post(
        "/analyze-code",
        json={"code": code}
    )
    assert response.status_code == 200
    assert "suggestions" in response.json()
    assert "analysis_id" in response.json()
    assert "created_at" in response.json()

def test_analyze_invalid_code():
    code = "def invalid syntax here"
    response = client.post(
        "/analyze-code",
        json={"code": code}
    )
    assert response.status_code == 200
    suggestions = response.json()["suggestions"]
    assert any(s["type"] == "error" for s in suggestions)