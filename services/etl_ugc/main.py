import asyncio

from aiohttp import ClientSession

from utils.logger import logger
from db.clickhouse import ClickHouseAdapter
from dependencies.clickhouse import get_clickhouse_service
from core.settings import settings


async def main():
    session: ClientSession = ClientSession()
    clickhouse_service: ClickHouseAdapter = (
        await get_clickhouse_service(session, url=settings.clickhouse_url)
    )
    await clickhouse_service.health_check()

    try:
        logger.info("Starting ETL process")
        await clickhouse_service.init()
    finally:
        await session.close()


if __name__ == "__main__":
    asyncio.run(main())
