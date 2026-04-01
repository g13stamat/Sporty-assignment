import requests

class ApiClient:
    BASE_URL = "https://qae-assignment-tau.vercel.app/api"
    USER_ID = "candidate-5b1a0f3d"

    def get(self, path, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["X-User-Id"] = self.USER_ID
        return requests.get(f"{self.BASE_URL}{path}", headers=headers, **kwargs)

    def post(self, path, json=None, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["X-User-Id"] = self.USER_ID
        return requests.post(f"{self.BASE_URL}{path}", json=json, headers=headers, **kwargs)
