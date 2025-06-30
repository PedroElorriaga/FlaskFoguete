from src.models.sqlite.settings.sqlite_connection import SqliteConnection
from AULA_JWT.src.main.controllers.users_controller import UsersController
from src.models.sqlite.repository.users_repository import UsersRepository


def user_composer() -> UsersController:
    sqlite_handler_connection = SqliteConnection()
    sqlite_connection = sqlite_handler_connection.connect()
    user_repository = UsersRepository(sqlite_connection)

    return UsersController(user_repository)
