from abc import ABC, abstractmethod


class OrderInterface(ABC):
    @abstractmethod
    def insert_data(self, data: dict) -> None:
        pass

    @abstractmethod
    def find_data(self, name: dict) -> None:
        pass
