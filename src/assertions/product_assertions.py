# src/assertions/product_assertions.py
import pdb


def assert_product_created_successfully(response, expected_body):
    assert response.status_code == 201
    body = response.json()
    pdb.set_trace()
    for field, expected_value in expected_body.items():
        assert field in body, f"Response missing field '{field}'"
        assert body[field] == expected_value, (
            f"Expected '{field}' = '{expected_value}', "
            f"got '{body[field]}'"
        )
