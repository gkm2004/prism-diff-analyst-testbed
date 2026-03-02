import time
import requests

def call_payment_api(url: str, payload: dict, timeout: int = 5):
    try:
        r = requests.post(url, json=payload, timeout=timeout)
        return r.json()
    except Exception:
        return {}  # bad: hides failures