from pymongo import MongoClient

from src.models.mongodb.repository.interface.order_interface import OrderInterface

from typing import List
from bson.objectid import ObjectId


class OrdersRepository(OrderInterface):
    def __init__(self, mongo_connection: MongoClient) -> None:
        self.__collection_name = 'orders'
        self.__mongo_connection = mongo_connection

    def insert_one_data(self, data: dict) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        mongo_collection.insert_one(data)

        product = data['produto'].capitalize()

        print(f'{product} criado com sucesso')

    def find_one_data(self, data: dict) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find_one(data)

        print(response)

    def find_datas_by_parameter(self, parameter: str) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find(
            {parameter: {"$exists": True}}
        )

        # FAZEMOS ISSO QUANDO TEMOS UM RETORNO COMO UM CURSOR (RETORNO DE UM BANCO DE DADOS)
        for response_open in response:
            print(response_open)

    def find_all_datas(self, data: dict = None) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find(data)

        for response_open in response:
            print(response_open)

    def insert_many_datas(self, data: List[dict]) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        mongo_collection.insert_many(data)

        print('Os dados foram inseridos com sucesso')

    def find_data_by_id(self, id: str) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        id_object = ObjectId(id)
        response = mongo_collection.find_one({"_id": id_object})

        print(response)
