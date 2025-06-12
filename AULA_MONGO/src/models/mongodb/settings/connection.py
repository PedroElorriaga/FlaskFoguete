from pymongo import MongoClient


class MongoSettingsHandler:
    def __init__(self):
        self.__connection_string = 'mongodb://localhost:27017'
        self.__db_name = 'mongo_foguete'
        self.__client = None
        self.__db_connection = None

    def connect(self) -> MongoClient:
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__db_name]

        return self.__get_db_connection()

    def __get_db_connection(self) -> MongoClient:
        return self.__db_connection
