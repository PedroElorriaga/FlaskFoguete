from src.models.mongodb.repository.interface.order_interface import OrderInterface
from typing import List


class OrdersData:
    def __init__(self, orders_repository: OrderInterface) -> None:
        self.__orders_repository = orders_repository

    def insert_order(self, data: dict | List[dict]) -> None:
        if type(data) == dict:
            self.__orders_repository.insert_one_data(data)
            return

        for item in data:
            if type(item) != dict:
                raise Exception('Tipos de dados invalidos')

        self.__orders_repository.insert_many_datas(data)

    def find_order(self, name: dict = None, first: bool = False) -> None:
        if name and first:
            self.__orders_repository.find_one_data(name)
            return
        elif name:
            self.__orders_repository.find_all_datas(name)
            return

        self.__orders_repository.find_all_datas()

    def find_orders_by_parameter(self, parameter: str) -> None:
        self.__orders_repository.find_datas_by_parameter(parameter)

    def find_order_by_id(self, id: str) -> None:
        self.__orders_repository.find_data_by_id(id)
