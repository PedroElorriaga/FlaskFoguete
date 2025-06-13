from src.models.mongodb.repository.interface.order_interface import OrderInterface


class OrdersData:
    def __init__(self, orders_repository: OrderInterface) -> None:
        self.__orders_repository = orders_repository

    def insert_order(self, data: dict) -> None:
        self.__orders_repository.insert_one_data(data)

    def find_order(self, name: dict) -> None:
        self.__orders_repository.find_one_data(name)

    def find_orders_by_parameter(self, parameter: str) -> None:
        self.__orders_repository.find_datas_by_parameter(parameter)

    def find_orders(self) -> None:
        self.__orders_repository.find_all_datas()
