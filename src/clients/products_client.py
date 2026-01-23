# src/clients/products_client.py
from src.clients.base_client import BaseClient

class ProductClient(BaseClient):

    def create_new_product(self, payload):
        return self.post("/products", json=payload)
