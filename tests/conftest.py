import pytest
from fastapi.testclient import TestClient

from fast_zero.app import api


@pytest.fixture
def client():
    return TestClient(api)
