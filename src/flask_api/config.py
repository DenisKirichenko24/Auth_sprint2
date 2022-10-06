from datetime import timedelta
from os import environ
from pydantic import BaseSettings, Field


class Config(BaseSettings):
    # Flask
    FLASK_ENV: str = Field('production', env='FLASK_ENV')

    PROPAGATE_EXCEPTIONS: bool = Field(True)
    SECRET_KEY: str = Field('Super_key!', env='SECRET_KEY')

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI: str = Field(
        f'postgresql://{environ.get("DB_USERNAME")}:{environ.get("DB_PASSWORD")}@'
        f'{environ.get("DB_HOST")}:{environ.get("DB_PORT", 5432)}/{environ.get("DB_NAME")}_test')

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
    }
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = Field(True)

    # JWT Extended
    JWT_SECRET_KEY: str = Field(env='JWT_SECRET_KEY')
    JWT_ERROR_MESSAGE_KEY: str = Field(env='message')
    JWT_TOKEN_LOCATION: str = Field(env='headers')
    JWT_COOKIE_SECURE: bool = Field(True, env='JWT_COOKIE_SECURE')
    JWT_ACCESS_TOKEN_EXPIRES: timedelta = Field(timedelta(days=1))
    JWT_REFRESH_TOKEN_EXPIRES: timedelta = Field(timedelta(weeks=4))

    # REST-X
    RESTX_MASK_SWAGGER: bool = Field(False)

    # REDIS
    REDIS_URL: str = Field(env='REDIS_URL')

    # JAEGER
    JAEGER_URL: str = Field('localhost', env='JAEGER_URL')

    # Google OAuth2
    GOOGLE_CLIENT_ID: str = Field(env='GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET: str = Field(env='GOOGLE_CLIENT_SECRET')
    GOOGLE_CONF_URL: str = Field('https://accounts.google.com/.well-known/openid-configuration')

    # Yandex OAuth2
    YANDEX_CLIENT_ID: str = Field(env='YANDEX_CLIENT_ID')
    YANDEX_CLIENT_SECRET: str = Field(env='YANDEX_CLIENT_SECRET')
    YANDEX_API_BASE_URL: str = Field('https://login.yandex.ru/')
    YANDEX_ACCESS_TOKEN_URL: str = Field('https://oauth.yandex.ru/token')
    YANDEX_AUTHORIZE_URL: str = Field('https://oauth.yandex.ru/authorize')
