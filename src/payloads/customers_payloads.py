# src/payloads/customers_payloads.py
def build_create_customer_payload(test_data):
    payload = {}
    for field, value in test_data.items():
        payload[field] = value

    return payload
