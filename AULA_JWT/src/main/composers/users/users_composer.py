from src.models.sqlite.settings.sqlite_connection import SqliteConnection
from src.data.users.users_data import UsersData
from src.models.sqlite.repository.users_repository import UsersRepository


def user_composer() -> UsersData:
    sqlite_handler_connection = SqliteConnection()
    sqlite_connection = sqlite_handler_connection.connect()
    user_repository = UsersRepository(sqlite_connection)

    return UsersData(user_repository)
