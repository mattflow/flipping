from celery import Celery
from .config import RabbitMQSettings, RedisSettings

rabbitmq_settings = RabbitMQSettings()  # pyright: ignore[reportCallIssue]
redis_settings = RedisSettings()  # pyright: ignore[reportCallIssue]


backend = f"redis://{redis_settings.username}:{redis_settings.password.get_secret_value()}@{redis_settings.host}:6379/0"
broker = f"amqp://{rabbitmq_settings.username}:{rabbitmq_settings.password.get_secret_value()}@{rabbitmq_settings.host}:5672//"

app = Celery(
    "tasks",
    backend=backend,
    broker=broker,
)


@app.task
def add(x, y):
    return x + y
