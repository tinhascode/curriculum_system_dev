from fastapi.testclient import TestClient

from app.core.config import settings


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "version": settings.VERSION,
    }
