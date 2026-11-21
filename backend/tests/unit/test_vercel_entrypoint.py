import importlib.util
from pathlib import Path

from fastapi.testclient import TestClient

ENTRYPOINT = Path(__file__).resolve().parents[3] / "index.py"


def test_root_entrypoint_serves_the_api_and_the_snapshot():
    spec = importlib.util.spec_from_file_location("vercel_entrypoint", ENTRYPOINT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    client = TestClient(module.app)

    assert client.get("/health").json() == {"status": "healthy"}
    snapshot = client.get("/api/v1/snapshot").json()
    assert snapshot["coverage"]["matched_hours"] == 744