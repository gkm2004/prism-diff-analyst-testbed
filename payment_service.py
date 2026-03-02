import time
import requests

def call_payment_api(url: str, payload: dict, timeout: int = 5):
    for attempt in range(3):
        try:
            r = requests.post(url, json=payload, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)  # backoff