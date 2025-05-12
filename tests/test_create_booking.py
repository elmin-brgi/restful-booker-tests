import requests
import urllib.parse

# Following tests are made to automate most common scenarios. All specific cases are tested manually with Postman and bugs are reported.

class TestCreateBooking:
    
    def test_create_booking_json(self, base_url, booking_payload):
        """Test creating a booking with JSON content type and accept"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        response = requests.post(
            f"{base_url}/booking",
            headers=headers,
            json=booking_payload
        )
        
        assert response.status_code == 200
        response_body = response.json()
        
        # Verify response structure
        assert "bookingid" in response_body
        assert "booking" in response_body
        
        # Verify booking details match what we sent
        assert response_body["booking"]["firstname"] == booking_payload["firstname"]
        assert response_body["booking"]["lastname"] == booking_payload["lastname"]
        assert response_body["booking"]["totalprice"] == booking_payload["totalprice"]
        assert response_body["booking"]["depositpaid"] == booking_payload["depositpaid"]
        assert response_body["booking"]["bookingdates"]["checkin"] == booking_payload["bookingdates"]["checkin"]
        assert response_body["booking"]["bookingdates"]["checkout"] == booking_payload["bookingdates"]["checkout"]
        assert response_body["booking"]["additionalneeds"] == booking_payload["additionalneeds"]
    
    def test_create_booking_xml(self, base_url, booking_payload):
        # Convert the booking payload to XML format
        booking_xml = f"""
        <booking>
            <firstname>{booking_payload["firstname"]}</firstname>
            <lastname>{booking_payload["lastname"]}</lastname>
            <totalprice>{booking_payload["totalprice"]}</totalprice>
            <depositpaid>{str(booking_payload["depositpaid"]).lower()}</depositpaid>
            <bookingdates>
                <checkin>{booking_payload["bookingdates"]["checkin"]}</checkin>
                <checkout>{booking_payload["bookingdates"]["checkout"]}</checkout>
            </bookingdates>
            <additionalneeds>{booking_payload["additionalneeds"]}</additionalneeds>
        </booking>
        """
        
        headers = {
            "Content-Type": "text/xml",
            "Accept": "application/json"
        }
        
        response = requests.post(
            f"{base_url}/booking",
            headers=headers,
            data=booking_xml
        )
        
        assert response.status_code == 200
        response_body = response.json()
        
        # Verify response structure
        assert "bookingid" in response_body
        assert "booking" in response_body
        
        # Verify booking details
        assert response_body["booking"]["firstname"] == booking_payload["firstname"]
        assert response_body["booking"]["lastname"] == booking_payload["lastname"]
        assert response_body["booking"]["totalprice"] == booking_payload["totalprice"]
        assert response_body["booking"]["depositpaid"] == booking_payload["depositpaid"]
        assert response_body["booking"]["bookingdates"]["checkin"] == booking_payload["bookingdates"]["checkin"]
        assert response_body["booking"]["bookingdates"]["checkout"] == booking_payload["bookingdates"]["checkout"]
        assert response_body["booking"]["additionalneeds"] == booking_payload["additionalneeds"]
    
    def test_create_booking_urlencoded(self, base_url, booking_payload):
        """Test creating a booking with URL-encoded content type and JSON accept"""
        # Prepare URL-encoded data
        flat_data = {
            "firstname": booking_payload["firstname"],
            "lastname": booking_payload["lastname"],
            "totalprice": booking_payload["totalprice"],
            "depositpaid": booking_payload["depositpaid"],
            "bookingdates[checkin]": booking_payload["bookingdates"]["checkin"],
            "bookingdates[checkout]": booking_payload["bookingdates"]["checkout"],
            "additionalneeds": booking_payload["additionalneeds"]
        }
        
        # Manually encode the data
        encoded_data = urllib.parse.urlencode(flat_data)

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }
        
        response = requests.post(
            f"{base_url}/booking",
            headers=headers,
            data=encoded_data
        )
        
        assert response.status_code == 200
        response_body = response.json()
        
        # Verify response structure
        assert "bookingid" in response_body
        assert "booking" in response_body
        
        # Verify booking details match what we sent
        assert response_body["booking"]["firstname"] == booking_payload["firstname"]
        assert response_body["booking"]["lastname"] == booking_payload["lastname"]
        assert response_body["booking"]["totalprice"] == booking_payload["totalprice"]
        assert response_body["booking"]["depositpaid"] == booking_payload["depositpaid"]
        assert response_body["booking"]["bookingdates"]["checkin"] == booking_payload["bookingdates"]["checkin"]
        assert response_body["booking"]["bookingdates"]["checkout"] == booking_payload["bookingdates"]["checkout"]
        assert response_body["booking"]["additionalneeds"] == booking_payload["additionalneeds"]