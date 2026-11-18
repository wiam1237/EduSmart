"""Contrats de la route de santé."""

from fastapi.testclient import TestClient

from app.main import app


def test_health_returns_application_status() -> None:
    with TestClient(app) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "pfa-student-productivity-api"
    assert body["database"] in {"up", "down"}


def test_unknown_route_stays_a_client_error() -> None:
    with TestClient(app) as client:
        response = client.get("/api/inexistant")

    assert response.status_code == 404


def test_health_is_documented_in_openapi() -> None:
    with TestClient(app) as client:
        response = client.get("/openapi.json")

    assert response.status_code == 200
    paths = response.json()["paths"]
    assert "/api/health" in paths
