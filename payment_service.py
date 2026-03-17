import time
import requests

API_KEY = "sk-FAKEFAKEFAKEFAKEFAKEFAKE"  # intentionally fake for testing
def call_payment_api(url: str, payload: dict, timeout: int = 5):
    r = requests.post(url, json=payload, timeout=timeout)
    r.raise_for_status()
    return r.json()