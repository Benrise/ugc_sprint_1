import os
from logging import config as logging_config

from pydantic import Field
from pydantic_settings import BaseSettings

from core.logger import LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    clickhouse_protocol: str = Field('http', alias='CLICKHOUSE_SERVICE_PROTOCOL')
    clickhouse_host: str = Field('clickhouse', alias='CLICKHOUSE_SERVICE_HOST')
    clickhouse_port: int = Field(8123, alias='CLICKHOUSE_SERVICE_PORT')
    kafka_bootstrap_servers: str = Field(..., alias='UGC_KAFKA_BOOTSTRAP_SERVERS')

    @property
    def clickhouse_url(self) -> str:
        url = f"{self.clickhouse_protocol}://{self.clickhouse_host}:{self.clickhouse_port}"
        print(url)
        return url


settings = Settings()
