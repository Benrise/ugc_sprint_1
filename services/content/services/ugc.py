import httpx
from fastapi import Request
from utils.logger import logger


class UGCEventService:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def send_event(self, request: Request, event_type: str, data: dict):
        query_event_data = "&".join([f"{key}={value}" for key, value in data.items()])
        url = f"{self.base_url}/send_to_broker/{event_type}?event_data={query_event_data}"

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=request.headers)
            if response.status_code != 200:
                logger.error(f"Failed to send event: {response.status_code}")
            return response
