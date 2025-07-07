from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert "cpu_usage_percent" in response.json()

def test_logs_auth_fail():
    response = client.get("/logs?path=/tmp/test.log&lines=5")
    assert response.status_code == 422 or response.status_code == 401

def test_pods_status_with_auth():
    response = client.get(
        "/pods/status?namespace=default",
        headers={"x-api-key": "sremate123"}
    )
    assert response.status_code == 200
    body = response.json()
    
    # Should return list of pods or error if none
    assert isinstance(body, list) or "error" in body