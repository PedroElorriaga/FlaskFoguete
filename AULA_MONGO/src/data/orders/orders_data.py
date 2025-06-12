from src.models.mongodb.repository.interface.order_interface import OrderInterface


class OrdersData:
    def __init__(self, orders_repository: OrderInterface) -> None:
        self.__orders_repository = orders_repository

    def insert_order(self, data: dict) -> None:
        self.__orders_repository.insert_data(data)

    def find_order(self, name: dict) -> None:
        self.__orders_repository.find_data(name)
