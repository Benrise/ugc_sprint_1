from typing import Any, Optional

from utils.abstract import AnalyticDatabaseService

from aiochclient import ChClient


class ClickHouseAdapter(AnalyticDatabaseService):
    def __init__(self, client: ChClient):
        self.client = client

    async def execute(
            self,
            query: str,
            *args,
            params: Optional[Any] = None,
            query_id: Optional[str] = None
    ) -> Any:
        try:
            return await self.client.execute(
                query,
                args,
                params=params,
                query_id=query_id
            )
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    async def fetch(
        self,
        query: str,
        params: Optional[Any] = None,
        query_id: Optional[str] = None,
        decode: bool = True
    ) -> Any:
        try:
            return await self.client.fetch(
                query,
                params=params,
                query_id=query_id,
                decode=decode
            )
        except Exception as e:
            print(f"Error on fetch: {e}")
            return None
