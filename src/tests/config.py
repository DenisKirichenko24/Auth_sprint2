import datetime
from datetime import timedelta
from os import environ
from pydantic import BaseSettings, Field

from dotenv import load_dotenv

load_dotenv()


# Testing configuration------------------------------------------------------


class TestConfig(BaseSettings):
    # Flask
    FLASK_ENV: str = Field('production', env='FLASK_ENV')

    PROPAGATE_EXCEPTIONS: bool = Field(True)
    TESTING: bool = Field(True)

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
    JWT_TOKEN_LOCATION: str = Field(env='headers')
    JWT_ACCESS_TOKEN_EXPIRES: datetime.timedelta = Field(timedelta(seconds=2))
    JWT_REFRESH_TOKEN_EXPIRES: datetime.timedelta = Field(timedelta(seconds=2))

    # REST-X
    RESTX_MASK_SWAGGER: bool = Field(True)
