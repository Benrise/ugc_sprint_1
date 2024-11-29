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

    try:
        response = await clickhouse_service.fetch("SELECT version()")
        if response:
            logger.info("Successfully connected to ClickHouse")
        else:
            logger.error(f"Failed to get response from ClickHouse: {response}")
    except Exception as e:
        logger.error(f"Error occurred while connecting to ClickHouse: {str(e)}")
    finally:
        await session.close()


if __name__ == "__main__":
    asyncio.run(main())
