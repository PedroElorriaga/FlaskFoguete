from tests.mocks.sqlite_mock import MockConnection
from src.models.sqlite.repository.users_repository import UsersRepository


def test_create_new_user():
    connection = MockConnection()
    user_repository = UsersRepository(connection)
