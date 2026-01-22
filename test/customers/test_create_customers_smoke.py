import logging

import pytest

from src.generators.credentials import get_random_password_and_email
from src.clients.customers_client import CustomersClient
from src.payloads.customers_payloads import build_create_customer_payload
from src.assertions.customers_assertions import (assert_customer_exists_in_db,
                                                 assert_customer_with_existed_email_not_created,
                                                 assert_customer_created)
from src.db.dal.users_dal import get_existed_customer_email
import pdb

logger = logging.getLogger(__name__)


@pytest.mark.tc01
def test_create_customer_only_email_password():
    logger.info('-> test_create_customer_only_email_password')
    # get test data
    test_data = get_random_password_and_email()
    # create payload
    payload = build_create_customer_payload(test_data)
    # make a call
    c_client = CustomersClient()
    response = c_client.create_customer(payload)

    # verify status code
    # verify email in response
    # verify user name in response
    del test_data['password']
    assert_customer_created(response, expected_status=201,
                            expected_body=test_data)

@pytest.mark.skip(reason="Feature not implemented yet")
@pytest.mark.tc02
def test_customer_has_created_in_database():
    logger.info('-> test_customer_has_created_in_database')
    test_data = get_random_password_and_email()
    payload = build_create_customer_payload(test_data)
    c_client = CustomersClient()
    response = c_client.create_customer(payload)
    assert_customer_exists_in_db(test_data['email'])


@pytest.mark.tc03
def test_create_customer_with_existed_email():
    logger.info('-> test_create_customer_with_existed_email')
    test_data = get_random_password_and_email()
    test_data['email'] = get_existed_customer_email()
    payload = build_create_customer_payload(test_data)
    c_client = CustomersClient()
    response = c_client.create_customer(payload)
    assert_customer_with_existed_email_not_created(response, 400)
