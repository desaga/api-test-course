# test/products/test_create_product.py
import logging
import pytest
from src.generators.product_load_generator import \
    get_lorem_create_product_payload
from src.clients.products_client import ProductClient
from src.assertions.product_assertions import \
    (assert_product_created_successfully,
     assert_product_exists_in_db)

logger = logging.getLogger(__name__)


@pytest.mark.products
def test_create_product():
    pc = ProductClient()
    payload = get_lorem_create_product_payload()
    response = pc.create_new_product(payload)
    assert_product_created_successfully(response, payload)
    del payload['type']
    assert_product_exists_in_db(payload)
