import requests

def test_auth_success(auth_token):
    # Token should be set in fixture, here we are testing if it exists.
    assert isinstance(auth_token, str)
    assert len(auth_token) > 0


def test_auth_invalid_password(base_url):
    payload = {
        "username": "admin",
        "password": "wrongpassword"
    }
    response = requests.post(f"{base_url}/auth", json=payload)

    assert response.status_code == 200
    assert "reason" in response.json()
    assert response.json()["reason"] == "Bad credentials"


def test_auth_missing_both_fields(base_url):
    payload = {}  # no username, no password
    response = requests.post(f"{base_url}/auth", json=payload)

    assert response.status_code == 200
    assert "reason" in response.json()
    assert response.json()["reason"] == "Bad credentials"

def test_auth_missing_username(base_url):
    payload = {
        "username": "admin",
        "password": ""
    }
    response = requests.post(f"{base_url}/auth", json=payload)

    assert response.status_code == 200
    assert "reason" in response.json()
    assert response.json()["reason"] == "Bad credentials"

def test_auth_missing_password(base_url):
    payload = {
        "username": "",
        "password": "password123"
    }
    response = requests.post(f"{base_url}/auth", json=payload)

    assert response.status_code == 200
    assert "reason" in response.json()
    assert response.json()["reason"] == "Bad credentials"
    