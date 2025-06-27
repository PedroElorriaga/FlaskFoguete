from sqlite3 import Connection
from datetime import datetime, timezone
from typing import Optional


class UsersRepository:
    def __init__(self, sqlite_connection: Connection) -> None:
        self.__sqlite_connection = sqlite_connection

    def insert_data(self, nome_usuario: str, agencia: int, conta: int, email: str, senha: str) -> bool:
        cursor = self.__sqlite_connection.cursor()
        cursor.execute(
            '''
                INSERT INTO users
                    (nome_usuario, agencia, conta, email, hash_senha, criado_em)
                VALUES
                    (?, ?, ?, ?, ?, ?)
            ''',
            (nome_usuario, agencia, conta, email,
             senha, datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
        )
        self.__sqlite_connection.commit()

        if cursor.lastrowid:
            return True

        return False

    def search_data(self, id: Optional[int] = None, nome_usuario: Optional[str] = None, email: Optional[str] = None) -> tuple:
        cursor = self.__sqlite_connection.cursor()
        response = cursor.execute(
            '''
                SELECT * FROM users
                WHERE (id = ? OR nome_usuario = ? OR email = ?)
            ''',
            (id, nome_usuario, email)
        )
        user = response.fetchone()
        return user
