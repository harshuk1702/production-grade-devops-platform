from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "DevOps Demo API"
    assert data["version"] == "1.0.0"


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["service"] == "devops-demo-api"
    assert data["version"] == "1.0.0"


def test_products():
    response = client.get("/api/products")

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert len(data["products"]) == 3


def test_orders():
    response = client.get("/api/orders")

    assert response.status_code == 200

    data = response.json()

    assert "orders" in data
    assert len(data["orders"]) == 3


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200

    body = response.text

    assert "http_requests_total" in body
    assert "http_request_duration_seconds" in body
