from abc import ABC, abstractmethod


class OrderInterface(ABC):
    @abstractmethod
    def insert_one_data(self, data: dict) -> None:
        pass

    @abstractmethod
    def find_one_data(self, name: dict) -> None:
        pass

    @abstractmethod
    def find_datas_by_parameter(self, parameter: str) -> None:
        pass

    @abstractmethod
    def find_all_datas(self) -> None:
        pass
