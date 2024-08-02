import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import api
from fast_zero.models import Base


@pytest.fixture
def client():
    return TestClient(api)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    with Session(engine) as sess:
        yield sess

    Base.metadata.drop_all(engine)
