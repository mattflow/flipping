from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQSettings(BaseSettings):
    host: str
    username: str
    password: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="RABBITMQ_", extra="ignore"
    )


class RedisSettings(BaseSettings):
    host: str
    username: str
    password: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="REDIS_", extra="ignore"
    )
