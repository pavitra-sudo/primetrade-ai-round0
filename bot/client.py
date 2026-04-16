import time
import hmac
import hashlib
import httpx
from config import API_KEY, API_SECRET, BASE_URL
from bot.logging_config import logger

class BinanceClient:
    def __init__(self):
        self.base_url = BASE_URL

    def _sign(self, params: dict) -> dict:
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        signature = hmac.new(
            API_SECRET.encode(), #type: ignore
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, payload: dict):
        try:
            payload["timestamp"] = int(time.time() * 1000)
            signed_payload = self._sign(payload)

            headers = {"X-MBX-APIKEY": API_KEY}

            with httpx.Client(timeout=10.0) as client:
                response = client.post(
                    f"{self.base_url}/fapi/v1/order",
                    params=signed_payload,
                    headers=headers #type: ignore
                )

            logger.info(f"REQUEST: {payload}")
            logger.info(f"RESPONSE: {response.text}")

            response.raise_for_status()
            return response.json()

        except httpx.RequestError as e:
            logger.error(f"Network error: {str(e)}")
            raise

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e.response.text}")
            raise