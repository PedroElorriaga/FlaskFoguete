from redis import Redis


class RedisRepository:
    def __init__(self, redis_connection: Redis) -> None:
        self.__redis_connection = redis_connection

    def insert(self, key: str, value: any) -> None:
        self.__redis_connection.set(key, value)

    def get_key(self, key: str) -> str:
        value = self.__redis_connection.get(key)
        if value:
            return value.decode('utf-8')
        return None

    def insert_with_expiration(self, key: str, value: any, ex: int) -> None:
        self.__redis_connection.set(key, value, ex=ex)
