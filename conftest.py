import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    return "https://restful-booker.herokuapp.com"

@pytest.fixture
def auth_token(base_url):
    creds = {"username": "admin", "password": "password123"}
    response = requests.post(f"{base_url}/auth", json=creds)
    return response.json().get("token")

@pytest.fixture(scope="module")
def booking_payload():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
