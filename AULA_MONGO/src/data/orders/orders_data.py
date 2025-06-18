from src.models.mongodb.repository.orders_repository import OrdersRepository
from typing import List, Optional


class OrdersData:
    def __init__(self, orders_repository: OrdersRepository) -> None:
        self.__orders_repository = orders_repository

    def insert_order(self, data: dict | List[dict]) -> dict | List[dict]:
        if isinstance(data, dict):
            return self.__orders_repository.insert_one_data(data)

        for item in data:
            if not isinstance(item, dict):
                raise Exception('Tipos de dados invalidos')

        return self.__orders_repository.insert_many_datas(data)

    def find_order(self, name: dict = None, first: bool = False) -> dict | List[Optional[dict]]:
        if name and first:
            return self.__orders_repository.find_one_data(name)
        elif name:
            return self.__orders_repository.find_all_datas(name)

        return self.__orders_repository.find_all_datas()

    def find_orders_by_parameter(self, parameter: str) -> List[Optional[dict]]:
        return self.__orders_repository.find_datas_by_parameter(parameter)

    def find_order_by_id(self, id: str, show_off: dict = None) -> dict:
        response = self.__orders_repository.find_data_by_id(id, show_off)
        if self.__check_if_response_is_not_null(response):
            return response

        raise Exception('o ID informado não existe')

    def update_order_by_id(self, id: str, data: dict) -> bool:
        response = self.__orders_repository.update_data_by_id(id, data)
        if self.__check_if_response_is_not_null(response):
            return True

        raise Exception('o ID informado não existe')

    def delete_data_by_id(self, id: str) -> bool:
        response = self.__orders_repository.delete_data_by_id(id)
        if self.__check_if_response_is_not_null(response):
            return True

        raise Exception('o ID informado não existe')

    def __check_if_response_is_not_null(self, response: any) -> bool:
        if response or response == 1:
            return True
        return False
