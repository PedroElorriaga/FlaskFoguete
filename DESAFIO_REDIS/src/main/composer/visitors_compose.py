from src.main.server.server_settings import redis_settings_handler
from src.visitors.visitors import Visitors
from src.models.redis.repository.redis_repositoy import RedisRepository


def visitor_compose() -> Visitors:
    redis_connection = redis_settings_handler.connect()
    redis_repository = RedisRepository(redis_connection)

    return Visitors(redis_repository)
