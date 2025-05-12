# Plan of Testing for Restful Booker API

Base URL: https://restful-booker.herokuapp.com

## 1. Smoke Tests

Basic functionality executed first to check if the API is working:

- GET /ping  
  Expected: 201 Created

- POST /auth  
  Expected: 200 + token

- POST /booking  
  Creates a new booking with valid data  
  Expected: 200 OK + booking ID

- GET /booking/{id}  
  Retrieves the created booking  
  Expected: 200 OK + correct data

- PUT /id 
  Updates booking with specified id

- DELETE /id
  Deletes booking with specified id

## 2. Positive Test Cases

1. POST /booking  
   Create a booking with all required and optional fields

2. GET /booking/{id}  
   Retrieve a booking by ID

3. PUT /booking/{id}  
   Full update of a booking (token required)

4. PATCH /booking/{id}  
   Partial update (token required)

5. DELETE /booking/{id}  
   Delete a booking (token required) + confirmation that it was deleted

6. POST /auth  
   Generate an authentication token

7. GET /booking?firstname=X&lastname=Y  
   Filter bookings by first and last name

## 3. Negative Test Cases

1. Create a booking with missing required fields  
   Expected: 400 Bad Request

2. Create a booking with invalid data types (e.g., price = string)  
   Expected: 400 Bad Request

3. Retrieve a booking with a non-existing ID  
   Expected: 404 Not Found

4. Send an invalid JSON payload  
   Expected: 400 Bad Request

5. Ussage of an incorrect token  
   Expected: 403 Forbidden or 401 Unauthorized
