def test_index(client):
    response = client.get("/greet")
    assert response.status_code == 200

    expected = "<p>Now everyone can be a hero...</p>"
    assert expected == response.get_data(as_text=True)
