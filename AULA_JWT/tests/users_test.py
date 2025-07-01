from tests.mocks.sqlite_mock import MockConnection
from src.models.sqlite.repository.users_repository import UsersRepository
from src.main.controllers.users_controller import UsersController
from src.security.password_handler import PasswordHandler


def test_create_new_user():
    connection = MockConnection()
    mock_cursor = connection.cursor()

    # Configura o comportamento simulado
    # Por exemplo: nenhum usuário encontrado
    mock_cursor.fetchone.side_effect = [None, None]
    mock_cursor.lastrowid = 1

    user_repository = UsersRepository(connection)
    users_controller = UsersController(user_repository)
    data = {
        'nome_usuario': 'John Doe',
        'agencia': 1111,
        'conta': 7,
        'email': 'johnDoe@test.py',
        'senha': '123abc'
    }

    response = users_controller.insert_user(data)

    assert response.body['message'] == 'Usuario criado com sucesso'
    assert response.status == 200


def test_create_new_exist_user():
    connection = MockConnection()
    mock_cursor = connection.cursor()

    # Configura o comportamento simulado
    # Por exemplo: Usuario encontrado
    mock_cursor.fetchone.side_effect = ['John Doe', 'johnDoe@test.py']
    mock_cursor.lastrowid = 1

    user_repository = UsersRepository(connection)
    users_controller = UsersController(user_repository)
    data = {
        'nome_usuario': 'John Doe',
        'agencia': 1111,
        'conta': 7,
        'email': 'johnDoe@test.py',
        'senha': '123abc'
    }

    response = users_controller.insert_user(data)

    assert response.body['message'] == 'O nome_usuario ja existe'
    assert response.status == 400


def test_find_user():
    connection = MockConnection()
    mock_cursor = connection.cursor()
    mock_cursor.fetchone.return_value = (1, 'John Doe', 1111, 7,
                                         'johnDoe@test.py', 'hash123')
    mock_cursor.lastrowid = 1

    user_repository = UsersRepository(connection)
    users_controller = UsersController(user_repository)

    response = users_controller.find_user({'id': 1})

    assert response.body['message'] == 'Usuario encontrado!'
    assert response.status == 200
    assert response.body['usuario']['id'] == 1


def test_not_find_user():
    connection = MockConnection()
    mock_cursor = connection.cursor()
    mock_cursor.fetchone.return_value = None
    mock_cursor.lastrowid = 1

    user_repository = UsersRepository(connection)
    users_controller = UsersController(user_repository)

    response = users_controller.find_user({'id': 1})

    assert response.body['message'] == 'Usuario não encontrado'
    assert response.status == 400


def test_login_user():
    password_handler = PasswordHandler()
    connection = MockConnection()
    mock_cursor = connection.cursor()
    mock_cursor.fetchone.return_value = (1, 'John Doe', 1111, 7,
                                         'johnDoe@test.py', password_handler.hash_password('hash123'))
    mock_cursor.lastrowid = 1

    user_repository = UsersRepository(connection)
    users_controller = UsersController(user_repository)
    data = {
        'nome_usuario': 'John Doe',
        'senha': 'hash123'
    }

    response = users_controller.login_user(data)

    assert response.body['message'] == 'Usuario logado com sucesso'
    assert response.status == 200


def test_login_wrong_user():
    password_handler = PasswordHandler()
    connection = MockConnection()
    mock_cursor = connection.cursor()
    mock_cursor.fetchone.return_value = (1, 'John Doe', 1111, 7,
                                         'johnDoe@test.py', password_handler.hash_password('hash123'))
    mock_cursor.lastrowid = 1

    user_repository = UsersRepository(connection)
    users_controller = UsersController(user_repository)
    data = {
        'nome_usuario': 'John Doe',
        'senha': '12345'
    }

    response = users_controller.login_user(data)

    assert response.body['message'] == 'Credenciais invalidas'
    assert response.status == 400
