def test_greet_with_name(client):
    # Test /greet with a 'name' query parameter
    response = client.get("/greet?name=John")
    assert response.status_code == 200
    assert response.is_json
    assert response.json == {"message": "Hello John!"}
