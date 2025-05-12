import requests

def test_health_check():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    assert response.status_code == 201