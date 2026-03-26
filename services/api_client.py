import requests
import json

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

    def set_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"

    def post(self, endpoint, payload):
        print(self.base_url)
        print(endpoint)
        print(f"{self.base_url}{endpoint}")
        payload = json.dumps(payload)
        return requests.post(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", headers=self.headers)

    def put(self, endpoint, payload):
        return requests.put(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)