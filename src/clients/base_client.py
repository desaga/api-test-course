# src/clients/base_client.py
import requests
from requests_oauthlib import OAuth1
import os
from src.configs.hosts_config import API_HOST


class BaseClient:
    def __init__(self, headers=None):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOST[self.env]
        self.headers = headers or {'Content-Type': 'application/json'}
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')
        if not wc_key or not wc_secret:
            raise RuntimeError(
                "WC_KEY and WC_SECRET must be set in environment variables"
            )
        self.auth = OAuth1(wc_key, wc_secret)

    def get(self, path, **kwargs):
        return requests.get(self.base_url + path, auth=self.auth, headers=self.headers, **kwargs)

    def post(self, path, **kwargs):
        return requests.post(self.base_url + path, auth=self.auth, headers=self.headers, **kwargs)

    def put(self, path, **kwargs):
        return requests.put(self.base_url + path, auth=self.auth, headers=self.headers, **kwargs)

    def delete(self, path, **kwargs):
        return requests.delete(self.base_url + path, auth=self.auth, headers=self.headers, **kwargs)
