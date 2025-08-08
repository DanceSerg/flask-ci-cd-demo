import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    rv = client.get('/')
    assert b'Hello, Vercel with Flask!' in rv.data












