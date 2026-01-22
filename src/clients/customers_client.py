# src/clients/customers_client.py
from src.clients.base_client import BaseClient

class CustomersClient(BaseClient):

    def create_customer(self, payload):
        return self.post("/customers", json=payload)

    def get_customer(self, customer_id):
        return self.get(f"/customers/{customer_id}")

    def update_customer(self, customer_id, payload):
        return self.put(f"/customers/{customer_id}", json=payload)

    def delete_customer(self, customer_id):
        return self.delete(f"/customers/{customer_id}")

    def list_customers(self, params=None):
        return self.get("/customers", params=params)
