from src.models.redis.repository.interface.redis_interface import RedisInterface


class Visitors:
    def __init__(self, redis_repository: RedisInterface):
        self.__redis_repository = redis_repository

    def insert_visitor(self) -> None:
        self.__increment_value()

    def get_visitor(self) -> str:
        return self.__get_value_in_redis()

    def __increment_value(self) -> None:
        redis_response = self.__get_value_in_redis()
        if redis_response:
            self.__redis_repository.increment_key('visitors_quantity')
            return None

        self.__insert_in_redis()

    def __get_value_in_redis(self) -> str:
        return self.__redis_repository.get_key('visitors_quantity')

    def __insert_in_redis(self) -> None:
        self.__redis_repository.insert_with_expiration(
            'visitors_quantity', '1', 60)
