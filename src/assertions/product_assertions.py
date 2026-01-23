# src/assertions/product_assertions.py
import logging
import pdb
from src.db.dal.products_dal import get_product_from_db

logger = logging.getLogger(__name__)


def assert_product_created_successfully(response, expected_body):
    assert response.status_code == 201
    body = response.json()
    for field, expected_value in expected_body.items():
        assert field in body, f"Response missing field '{field}'"
        assert body[field] == expected_value, (
            f"Expected '{field}' = '{expected_value}', "
            f"got '{body[field]}'"
        )


def assert_product_exists_in_db(product_json):
    db_product = get_product_from_db(product_json)
    assert db_product is not None, f"Product '{product_json}' does not exist in db"
    assert len(
        db_product) == 1, f"Expected 1 record in db for product '{product_json}'"

    db_product = db_product[0]
    for key, expected_value in product_json.items():
        logger.debug(
            f"Asserting {key} exists in db -> Expected: '{expected_value} == '{db_product[key]}'")
        assert expected_value == db_product[key], (
            f"Field '{key}' mismatch:\n"
            f"Expected      : '{expected_value}'\n"
            f"Actual in DB  : '{db_product[key]}'"
        )
