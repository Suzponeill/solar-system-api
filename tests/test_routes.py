import pytest


def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planet/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"id": 1,
        "name": "Pluto",
        "description": "Not a planet, still our friend.",
        "moons": False}

def test_get_one_planet_with_empty_db_run_404(client):
    # Act
    response = client.get("/planet/1")
    response_body = response.get_json()
    assert response.status_code == 404
    assert "message" in response_body

def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{"id": 1,
        "name": "Pluto",
        "description": "Not a planet, still our friend.",
        "moons": False} ,
        {"id": 2,
        "name": "Neptune",
        "description": "The sideways one.",
        "moons": True}]

def test_create_one_planet(client):
    # Act
    response = client.post("/planet", json={
        "name": "Neptune",
        "description": "The sideways one.",
        "moons": True})
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == f"Planet 1 successfully created"
    

