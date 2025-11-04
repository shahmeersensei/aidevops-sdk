import os
import sys
from fastapi.testclient import TestClient

# Ensure backend package is importable when pytest is run from repo root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.main import app


def test_health_endpoint():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data.get("status") == "ok"
    assert "running smoothly" in data.get("message", "")
