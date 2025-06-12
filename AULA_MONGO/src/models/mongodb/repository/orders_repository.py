from pymongo import MongoClient

from src.models.mongodb.repository.interface.mongo_interface import MongoInterface


class OrdersRepository(MongoInterface):
    def __init__(self, mongo_connection: MongoClient) -> None:
        self.__collection_name = 'orders'
        self.__mongo_connection = mongo_connection

    def insert_data(self, data: dict) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        mongo_collection.insert_one(data)

    def find_data(self, name: dict) -> None:
        mongo_collection = self.__mongo_connection[self.__collection_name]
        response = mongo_collection.find_one(name)

        print(response)
