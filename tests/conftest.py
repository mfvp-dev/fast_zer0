import pytest
from fastapi.testclient import TestClient

from fast_zer0.app import app


@pytest.fixture
def client():
    return TestClient(app)
