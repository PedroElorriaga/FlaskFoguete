from pymongo import MongoClient

from typing import List, Optional
from bson.objectid import ObjectId


class OrdersRepository:
    def __init__(self, mongo_connection: MongoClient) -> None:
        self.__collection_name = 'orders'
        self.__mongo_connection = mongo_connection

    def insert_one_data(self, data: dict) -> dict:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        mongo_collection.insert_one(data)

        return data

    def find_one_data(self, data: dict, show_off: dict = None) -> dict:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find_one(data, show_off)

        return response

    def find_datas_by_parameter(self, parameter: str, show_off: dict = None) -> List[Optional[dict]]:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find(
            {parameter: {"$exists": True}},
            show_off
        )
        response_list = []

        # FAZEMOS ISSO QUANDO TEMOS UM RETORNO COMO UM CURSOR (RETORNO DE UM BANCO DE DADOS)
        for response_open in response:
            # print(response_open)
            response_list.append(response_open)

        return response_list

    def find_all_datas(self, data: dict = None, show_off: dict = None) -> List[Optional[dict]]:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find(data, show_off)
        response_list = []

        for response_open in response:
            response_list.append(response_open)

        return response_list

    def insert_many_datas(self, data: List[dict]) -> List[dict]:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        mongo_collection.insert_many(data)

        return data

    def find_data_by_id(self, id: str, show_off: dict = None) -> dict:
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
