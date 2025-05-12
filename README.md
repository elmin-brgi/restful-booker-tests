# restful-booker-tests

Automated and manual test cases for the Restful Booker API.

## Technologies

Python: Used for writing automated API tests.
requests: HTTP client for sending requests to the Restful Booker API.
pytest: Test framework for organizing and executing tests.

## Installation

Before running the tests, make sure you have **Python** installed. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

1. **Clone the repository**:
   Open terminal
   Git clone https://github.com/elmin-brgi/restful-booker-tests.git
   Navigate to restful-booker-tests

2. **Install following dependencies**
    requests
    pytest

3. **Run tests**
    python -m pytest tests/
    (this will run all tests inside the folder)
    
## 📌 Contents
- `tests/` – Automated tests using Pytest and Requests libraries
- `conftest.py` – Common functions and similar
- `README.md` - Short info about project and explanation on how to run tests
- `PlanOfTesting.txt` - Test cases focused on user flow. This file is used as a guide for automation