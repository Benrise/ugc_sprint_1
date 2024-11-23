import os
from logging import config as logging_config

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.logger import LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QUERY_DESC = "Поисковая строка"
QUERY_ALIAS = "query"

SORT_ORDER_DESC = "Сортировка. asc - по возрастанию, desc - по убыванию"
SORT_ORDER_ALIAS = "sort_order"

SORT_FIELD_DESC = "Поле для сортировки"
SORT_FIELD_ALIAS = "sort_field"

PAGE_DESC = "Номер страницы"
PAGE_ALIAS = "page"

SIZE_DESC = "Количество элементов на странице"
SIZE_ALIAS = "size"

GENRE_DESC = "Фильтр по жанру фильма"
GENRE_ALIAS = "genre_id"

MAX_PAGE_SIZE = 100
MAX_GENRES_SIZE = 50

logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AUTH_",
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
    project_name: str = Field(..., alias='PROJECT_NAME')
    redis_host: str = Field('redis', alias='REDIS_HOST')
    redis_port: int = Field(6379, alias='REDIS_PORT')
    redis_version: str = Field(None, alias='REDIS_VERSION')
    echo_var: bool = Field(..., alias='ECHO_VAR')
    debug: bool = Field(..., alias='DEBUG')
    secret_key_session: str = Field(..., alias='SECRET_KEY_SESSION')
    enable_tracing: bool = Field(..., alias='ENABLE_TRACING')
    tracer_host: str = Field(..., alias='TRACER_HOST')
    tracer_port: int = Field(..., alias='TRACER_PORT')


settings = Settings()


class OAuthYandexSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AUTH_",
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
    client_id: str = Field(..., alias='YANDEX_CLIENT_ID')
    client_secret: str = Field(..., alias='YANDEX_CLIENT_SECRET')
    scope: str = 'login:email'
    api_base_url: str = 'https://login.yandex.ru/'
    authorize_url: str = 'https://oauth.yandex.ru/authorize'
    access_token_url: str = 'https://oauth.yandex.ru/token'
    redirect_uri: str = Field(..., alias='YANDEX_REDIRECT_URI')


oauth_yandex = OAuthYandexSettings()


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='AUTH_POSTGRES_',
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
    db: str = Field(..., alias='DB')
    user: str = Field(..., alias='USER')
    password: str = Field(..., alias='PASSWORD')
    host: str = Field(..., alias='HOST')
    port: int = Field(..., alias='PORT')


pg = PostgresSettings()
