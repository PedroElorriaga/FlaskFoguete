from redis import Redis


class RedisSettingsHandler:
    def __init__(self) -> None:
        self.__redis_connection = None

    def connect(self) -> Redis:
        redis_connection = Redis(
            host='localhost',
            port=6379,
            db=0
        )

        self.__redis_connection = redis_connection
        return redis_connection
