from pymongo import MongoClient

from src.models.mongodb.repository.interface.order_interface import OrderInterface


class OrdersRepository(OrderInterface):
    def __init__(self, mongo_connection: MongoClient) -> None:
        self.__collection_name = 'orders'
        self.__mongo_connection = mongo_connection

    def insert_one_data(self, data: dict) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        mongo_collection.insert_one(data)

        product = data['produto']

        print(f'{product} criado com sucesso')

    def find_one_data(self, name: dict) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find_one(name)

        print(response)

    def find_datas_by_parameter(self, parameter: str) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find(
            {parameter: {"$exists": True}}
        )

        # FAZEMOS ISSO QUANDO TEMOS UM RETORNO COMO UM CURSOR (RETORNO DE UM BANCO DE DADOS)
        for response_open in response:
            print(response_open)

    def find_all_datas(self) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find()

        for response_open in response:
            print(response_open)
