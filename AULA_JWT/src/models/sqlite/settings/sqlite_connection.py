import sqlite3
from sqlite3 import Connection


class SqliteConnection:
    def __init__(self) -> None:
        self.__connection_string = 'jwtProject.db'

    def connect(self) -> Connection:
        sqlite_connection = sqlite3.connect(
            self.__connection_string,
            check_same_thread=False
        )

        return sqlite_connection
