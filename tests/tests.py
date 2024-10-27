import pytest
from app import app  # Import the app from the app.py file


@pytest.fixture
def client():
    # Set up a test client for the Flask app
    with app.test_client() as client:
        yield client


def test_greet_with_name(client):
    # Test /greet with a 'name' query parameter
    response = client.get("/greet?name=John")
    assert response.status_code == 200
    assert response.is_json
    assert response.json == {"message": "Hello John!"}


def test_greet_without_name(client):
    # Test /greet without a 'name' query parameter
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.is_json
    assert response.json == {"message": "Now everyone can be a hero..."}


def test_health(client):
    # Test /health endpoint
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"    
