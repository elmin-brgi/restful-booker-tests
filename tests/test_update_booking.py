import pytest
import requests


@pytest.fixture
def created_booking_id(base_url, booking_payload):
    """Create a booking and return its ID"""
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert response.status_code == 200
    data = response.json()
    return data["bookingid"]


def test_update_booking_with_token(base_url, created_booking_id, auth_token):
    # Update payload
    update_payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    
    # Set cookie token header
    print("TOKEN -> ", auth_token)
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
    
    # Send PUT request to update booking
    response = requests.put(
        f"{base_url}/booking/{created_booking_id}",
        json=update_payload,
        headers=headers
    )
    
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "James"
    assert data["lastname"] == "Brown"
    assert data["totalprice"] == 111
    assert data["depositpaid"] is True
    assert data["bookingdates"]["checkin"] == "2018-01-01"
    assert data["bookingdates"]["checkout"] == "2019-01-01"
    assert data["additionalneeds"] == "Breakfast"


def test_update_booking_with_wrong_token(base_url, created_booking_id):
    update_payload = {
        "firstname": "Wrong",
        "lastname": "Token",
        "totalprice": 222,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-02"
        },
        "additionalneeds": "Nothing"
    }
    
    # Set incorrect token
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=wrong_token_value"
    }
    
    # Send PUT request with wrong token
    response = requests.put(
        f"{base_url}/booking/{created_booking_id}",
        json=update_payload,
        headers=headers
    )
    
    # Assert forbidden status
    assert response.status_code == 403
    assert "Forbidden" in response.text


def test_update_booking_with_xml(base_url, created_booking_id, auth_token):
    xml_payload = """<booking>
    <firstname>James</firstname>
    <lastname>Brown</lastname>
    <totalprice>111</totalprice>
    <depositpaid>true</depositpaid>
    <bookingdates>
        <checkin>2018-01-01</checkin>
        <checkout>2019-01-01</checkout>
    </bookingdates>
    <additionalneeds>Breakfast</additionalneeds>
    </booking>"""
    
    # Set headers with XML content type and Cookie token
    headers = {
        "Content-Type": "text/xml",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    
    # Send PUT request with XML body
    response = requests.put(
        f"{base_url}/booking/{created_booking_id}",
        data=xml_payload,
        headers=headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "James"
    assert data["lastname"] == "Brown"
    assert data["totalprice"] == 111
    assert data["depositpaid"] is True
    assert data["bookingdates"]["checkin"] == "2018-01-01"
    assert data["bookingdates"]["checkout"] == "2019-01-01"
    assert data["additionalneeds"] == "Breakfast"

def test_update_booking_with_urlencoded(base_url, created_booking_id, auth_token):
    """Test updating a booking using URL encoded form data and Authorization header"""
    # URL encoded form data
    form_data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": "111",
        "depositpaid": "true",
        "bookingdates[checkin]": "2018-01-01",
        "bookingdates[checkout]": "2019-01-01",
        "additionalneeds": "Breakfast"
    }
    
    # Set headers with form-urlencoded content type and authorization
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    
    # Send PUT request with URL encoded form data
    response = requests.put(
        f"{base_url}/booking/{created_booking_id}",
        data=form_data,
        headers=headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "James"
    assert data["lastname"] == "Brown"
    assert data["totalprice"] == 111
    assert data["depositpaid"] is True
    assert data["bookingdates"]["checkin"] == "2018-01-01"
    assert data["bookingdates"]["checkout"] == "2019-01-01"
    assert data["additionalneeds"] == "Breakfast"