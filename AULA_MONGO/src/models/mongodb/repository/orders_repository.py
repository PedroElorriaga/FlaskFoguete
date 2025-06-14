from pymongo import MongoClient

from typing import List
from bson.objectid import ObjectId


class OrdersRepository:
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
        response_len = 0

        # FAZEMOS ISSO QUANDO TEMOS UM RETORNO COMO UM CURSOR (RETORNO DE UM BANCO DE DADOS)
        for response_open in response:
            # print(response_open)
            response_len += 1

        print(response_len)

    def find_all_datas(self, data: dict = None) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find(data)
        response_len = 0

        for response_open in response:
            response_len += 1

        print(response_len)

    def insert_many_datas(self, data: List[dict]) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        mongo_collection.insert_many(data)

        print(f'{len(data)} dados foram inseridos na base de dados')

    def find_data_by_id(self, id: str, show_off: dict) -> dict:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        id_object = ObjectId(id)
        response = mongo_collection.find_one({"_id": id_object}, show_off)

        return response

    def update_data_by_id(self, id: str, data: dict) -> bool:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        id_object = ObjectId(id)
        response = mongo_collection.update_one({
            "_id": id_object
        }, {"$set": data})

        return response.raw_result.get('updatedExisting')

    def delete_data_by_id(self, id: str) -> int:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        id_object = ObjectId(id)
        response = mongo_collection.delete_one({
            "_id": id_object
        })

        return response.raw_result.get('n')
