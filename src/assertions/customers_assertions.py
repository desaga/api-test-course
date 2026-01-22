# src/assertions/customers_assertions.py
from src.db.dal.users_dal import user_exists

def assert_customer_created(response, expected_status=201, expected_body={}):
    # verify status code
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, got {response.status_code}\n response: {response}"
    )

    body = response.json()
    for field, expected_value in expected_body.items():
        assert field in body, f"Response missing field '{field}'"
        assert body[field] == expected_value, (
            f"Expected '{field}' = '{expected_value}', "
            f"got '{body[field]}'"
        )

def assert_customer_exists_in_db(email):
    assert user_exists(email)

def assert_customer_with_existed_email_not_created(response, expected_status=400):
    # verify status code
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, got {response.status_code}\n response: {response}"
    )
    assert "an account is already registered" in response.text.lower(), "Expected error message about duplicate email"
