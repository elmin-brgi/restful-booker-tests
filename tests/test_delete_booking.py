import pytest
import requests


@pytest.fixture
def created_booking_id(base_url, booking_payload):
    """Create a booking and return its ID"""
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert response.status_code == 200
    data = response.json()
    return data["bookingid"]


def test_delete_booking_with_cookie_token(base_url, created_booking_id, auth_token):
    """Test DELETE request with cookie token authorization"""
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
    
    # Send DELETE request
    response = requests.delete(
        f"{base_url}/booking/{created_booking_id}", 
        headers=headers
    )
    
    # Assert status code is 201 Created as per API documentation
    assert response.status_code == 201
    
    # Verify the booking no longer exists
    check_response = requests.get(f"{base_url}/booking/{created_booking_id}")
    assert check_response.status_code == 404


def test_delete_booking_with_basic_auth(base_url, created_booking_id):
    """Test DELETE request with Basic Authorization header"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # base64 encoded admin:password123
    }
    
    # Send DELETE request
    response = requests.delete(
        f"{base_url}/booking/{created_booking_id}", 
        headers=headers
    )
    
    # Assert status code is 201 Created as per API documentation
    assert response.status_code == 201
    
    # Verify the booking no longer exists
    check_response = requests.get(f"{base_url}/booking/{created_booking_id}")
    assert check_response.status_code == 404


def test_delete_booking_with_invalid_cookie_token(base_url, created_booking_id):
    """Test DELETE request with invalid cookie token"""
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=invalid_token_value"
    }
    
    # Send DELETE request
    response = requests.delete(
        f"{base_url}/booking/{created_booking_id}", 
        headers=headers
    )
    
    # Assert forbidden status code
    assert response.status_code == 403
    
    # Verify the booking still exists
    check_response = requests.get(f"{base_url}/booking/{created_booking_id}")
    assert check_response.status_code == 200


def test_delete_booking_with_invalid_basic_auth(base_url, created_booking_id):
    """Test DELETE request with invalid Basic Authorization header"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic aW52YWxpZDppbnZhbGlk"  # base64 encoded invalid:invalid
    }
    
    # Send DELETE request
    response = requests.delete(
        f"{base_url}/booking/{created_booking_id}", 
        headers=headers
    )
    
    # Assert forbidden status code
    assert response.status_code == 403
    
    # Verify the booking still exists
    check_response = requests.get(f"{base_url}/booking/{created_booking_id}")
    assert check_response.status_code == 200


def test_delete_booking_without_auth(base_url, created_booking_id):
    """Test DELETE request without any authorization"""
    headers = {
        "Content-Type": "application/json"
    }
    
    # Send DELETE request
    response = requests.delete(
        f"{base_url}/booking/{created_booking_id}", 
        headers=headers
    )
    
    # Assert forbidden status code
    assert response.status_code == 403
    
    # Verify the booking still exists
    check_response = requests.get(f"{base_url}/booking/{created_booking_id}")
    assert check_response.status_code == 200