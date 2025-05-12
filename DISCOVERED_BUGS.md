# Known Issues in RESTful Booker API

## 🐞 Bug 1 – `checkin` Filter Does Not Include Matching Dates

**Endpoint:** `GET /booking?checkin=YYYY-MM-DD`

**Description:**  
When a `checkin` query parameter is provided, the API is expected to return all bookings where the check-in date is **equal to or greater than** the provided value. However, bookings with a check-in date exactly matching the parameter are not returned.

**Expected Behavior:**  
Bookings with `checkin >= provided_date` should be included.

**Observed Behavior:**  
Only bookings with `checkin > provided_date` are returned. Exact matches are excluded.

---

## 🐞 Bug 2 – `checkout` Filter Returns Earlier Dates

**Endpoint:** `GET /booking?checkout=YYYY-MM-DD`

**Description:**  
The API should return bookings with a checkout date **equal to or greater than** the provided value. However, bookings with an earlier checkout date are sometimes included in the response.

**Expected Behavior:**  
Bookings with `checkout >= provided_date` should be returned.

**Observed Behavior:**  
Bookings with `checkout < provided_date` are incorrectly included in the response.

---

## 🐞 Bug 3 – Combined `checkin` and `checkout` Filters Return Empty Response

**Endpoint:** `GET /booking?checkin=YYYY-MM-DD&checkout=YYYY-MM-DD`

**Description:**  
When both `checkin` and `checkout` filters are used simultaneously, the API returns an empty result set even when bookings matching both conditions exist.

**Expected Behavior:**  
Bookings that match both `checkin >= value` and `checkout >= value` should be returned.

**Observed Behavior:**  
The response is always an empty array (`[]`), regardless of available matching bookings.

---

## 🐞 Bug 4 – POST `/booking` with `text/xml` Headers Returns HTTP 418

**Endpoint:** `POST /booking`  
**Request Headers:**
```
Content-Type: text/xml  
Accept: text/xml
```

**Request Body:**
```xml
<booking>
    <firstname>name</firstname>
    <lastname>surname</lastname>
    <totalprice>111</totalprice>
    <depositpaid>true</depositpaid>
    <bookingdates>
        <checkin>2018-01-01</checkin>
        <checkout>2019-01-01</checkout>
    </bookingdates>
    <additionalneeds>Breakfast</additionalneeds>
</booking>
```
**Description:**  
When sending a valid booking payload using XML formatting with headers indicating `Content-Type: text/xml` and `Accept: text/xml`, the API responds with an HTTP `418 I'm a teapot` status code.

**Expected Behavior:**  
The API should:
- Accept the request and process the XML payload correctly, returning a `200 OK` or `201 Created` response with an XML body

**Observed Behavior:**  
API returns: 418 err code

Following combinations also won't work: 
Content-Type: application/x-www-form-urlencoded
Accept: text/xml
returns: 418

Content-Type: application/json
Accept: text/xml
returns: 418

---