from abc import ABC, abstractmethod
from typing import List


class OrderInterface(ABC):
    @abstractmethod
    def insert_one_data(self, data: dict) -> None:
        pass

    @abstractmethod
    def find_one_data(self, data: dict) -> None:
        pass

    @abstractmethod
    def find_datas_by_parameter(self, parameter: str) -> None:
        pass

    @abstractmethod
    def find_all_datas(self, data: dict = None) -> None:
        pass

    @abstractmethod
    def insert_many_datas(self, data: List[dict]) -> None:
        pass

    @abstractmethod
    def find_data_by_id(self, id: str) -> None:
        pass
