from redis import Redis

from src.models.redis.repository.interface.redis_interface import RedisInterface


class RedisRepository(RedisInterface):
    def __init__(self, redis_connection: Redis) -> None:
        self.__redis_connection = redis_connection

    def insert_with_expiration(self, key: str, value: int, ex: int) -> None:
        self.__redis_connection.set(key, value, ex=ex)

    def get_key(self, key: str) -> str:
        value = self.__redis_connection.get(key)
        if value:
            return value.decode('utf-8')
        return None

    def increment_key(self, key: str) -> None:
        self.__redis_connection.incr(key)
