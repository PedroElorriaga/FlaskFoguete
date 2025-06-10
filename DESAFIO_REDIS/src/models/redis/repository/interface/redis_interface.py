from abc import ABC, abstractmethod


class RedisInterface(ABC):
    @abstractmethod
    def insert_with_expiration(self, key: str, value: any, ex: int) -> None:
        pass

    @abstractmethod
    def get_key(self, key: str) -> None:
        pass

    @abstractmethod
    def increment_key(self, key: str) -> None:
        pass
