from tests.mocks.sqlite_mock import MockConnection
from src.models.sqlite.repository.users_repository import UsersRepository


def test_create_new_user():
    connection = MockConnection()
    user_repository = UsersRepository(connection)

    response = user_repository.insert_data(
        'John Doe', 1111, 7, 'johnDoe@test.py', '123abc')
    cursor = connection.cursor.return_value
    cursor_args = cursor.execute.call_args

    assert 'INSERT INTO users' in cursor_args[0][0]
    assert '(nome_usuario, agencia, conta, email, hash_senha, criado_em)' in cursor_args[
        0][0]
    assert 'VALUE' in cursor_args[0][0]
    assert ('John Doe', 1111, 7, 'johnDoe@test.py',
            '123abc') == cursor_args[0][1][:5]  # Isolado sem datetime
    assert response == True


def test_find_user():
    connection = MockConnection()
    user_repository = UsersRepository(connection)

    user_repository.search_data(nome_usuario='John Doe')
    cursor = connection.cursor.return_value
    cursor_args = cursor.execute.call_args

    assert 'SELECT * FROM users' in cursor_args[0][0]
    assert 'WHERE (id = ? OR nome_usuario = ? OR email = ?)' in cursor_args[0][0]
    assert (None, 'John Doe', None) == cursor_args[0][1]
