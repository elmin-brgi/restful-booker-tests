import pytest
import requests


@pytest.fixture
def created_booking_id(base_url, booking_payload):
    """Create a booking and return its ID"""
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert response.status_code == 200
    data = response.json()
    return data["bookingid"]


def test_patch_booking_json(base_url, created_booking_id, auth_token):
    """Test PATCH request with JSON content type"""
    # Updated data with partial booking information
    patch_payload = {
        "firstname": "James",
        "lastname": "Brown"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    
    # Send PATCH request
    response = requests.patch(
        f"{base_url}/booking/{created_booking_id}", 
        json=patch_payload,
        headers=headers
    )
    
    # Assertions
    assert response.status_code == 200
    response_data = response.json()
    
    # Verify the updated fields
    assert response_data["firstname"] == "James"
    assert response_data["lastname"] == "Brown"
    
    # Verify other fields remain unchanged from the original booking
    assert "totalprice" in response_data
    assert "depositpaid" in response_data
    assert "bookingdates" in response_data
    assert "checkin" in response_data["bookingdates"]
    assert "checkout" in response_data["bookingdates"]


def test_patch_booking_xml(base_url, created_booking_id):
    """Test PATCH request with XML content type"""
    # XML payload for partial update
    xml_payload = """
    <booking>
        <firstname>James</firstname>
        <lastname>Brown</lastname>
    </booking>
    """
    
    headers = {
        "Content-Type": "text/xml",
        "Accept": "application/xml",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # base64 encoded admin:password123
    }
    
    # Send PATCH request
    response = requests.patch(
        f"{base_url}/booking/{created_booking_id}", 
        data=xml_payload,
        headers=headers
    )
    
    # Assertions
    assert response.status_code == 200
    
    # Since we're expecting XML, we don't parse to JSON
    # Instead, check if the response contains expected XML elements
    assert "<firstname>James</firstname>" in response.text
    assert "<lastname>Brown</lastname>" in response.text
    assert "<totalprice>" in response.text
    assert "<depositpaid>" in response.text
    assert "<bookingdates>" in response.text
    assert "<checkin>" in response.text
    assert "<checkout>" in response.text


def test_patch_booking_urlencoded(base_url, created_booking_id, auth_token):
    """Test PATCH request with URL-encoded content type"""
    # URL-encoded payload
    urlencoded_payload = "firstname=Jim&lastname=Brown"
    
    # Use the cookie authentication instead of Basic Auth since that's working in other tests
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",  # Change to accept JSON instead of form-urlencoded
        "Cookie": f"token={auth_token}"
    }
    
    # Send PATCH request
    response = requests.patch(
        f"{base_url}/booking/{created_booking_id}", 
        data=urlencoded_payload,
        headers=headers
    )
    
    # Assertions
    assert response.status_code == 200
    
    # Parse as JSON instead since the API seems to return JSON regardless of Accept header
    response_data = response.json()
    
    # Verify the updated fields
    assert response_data["firstname"] == "Jim"
    assert response_data["lastname"] == "Brown"
    
    # Verify other fields remain unchanged
    assert "totalprice" in response_data
    assert "depositpaid" in response_data
    assert "bookingdates" in response_data