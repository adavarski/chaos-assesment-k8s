def test_greet_without_name(client):
    # Test /greet without a 'name' query parameter
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.is_json
    assert response.json == {"message": "Now everyone can be a hero..."}
