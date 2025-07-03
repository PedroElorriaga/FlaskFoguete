from src.models.sqlite.repository.users_repository import UsersRepository
from src.http_types.http_response import HttpResponse
from src.security.password_handler import PasswordHandler
from src.security.jwt_handler import JWTHandler
from datetime import datetime, timedelta, timezone


class UsersController:
    def __init__(self, users_repository: UsersRepository) -> None:
        self.__users_repository = users_repository
        self.__jwt_handler = JWTHandler()

    def insert_user(self, data: dict) -> HttpResponse:
        if isinstance(data, dict):
            try:
                check_responses = [self.__check_if_user_already_exists(
                    {"nome_usuario": data['nome_usuario']}), self.__check_if_user_already_exists(
                    {"email": data['email']})]

                for check in check_responses:
                    if check:
                        if isinstance(check[0], HttpResponse):
                            return check[0]
                        key = list(check[1].keys())[0]
                        return HttpResponse(
                            {"message": f"O {key} ja existe"},
                            400
                        )

                password_handler = PasswordHandler()

                response = self.__users_repository.insert_data(
                    data['nome_usuario'],
                    data['agencia'],
                    data['conta'],
                    data['saldo'],
                    data['email'],
                    password_handler.hash_password(data['senha'])
                )
                if response:
                    return HttpResponse(
                        {"message": "Usuario criado com sucesso"},
                        200
                    )
            except Exception as exc:
                print(f'Ocorreu um erro no INSERT USER: {str(exc)}')
                return HttpResponse(
                    {"message": "Algo deu errado com sua solicitação"},
                    400
                )

    def find_all_users(self) -> HttpResponse:
        response = self.__users_repository.search_all_datas()
        for item in response:
            item.pop('hash_senha', None)

        if len(response) > 0:
            return HttpResponse(
                {
                    "message": f"{len(response)} usuarios encontrados",
                    "usuarios": response
                },
                200
            )

    def find_user(self, data: dict) -> HttpResponse:
        try:
            data_keys = ['id', 'nome_usuario', 'email']
            for key in data_keys:
                if data.get(key):  # SE DATA['ID'] EXISTE POR EXEMPLO
                    response = self.__users_repository.search_data(
                        **{key: data[key]})  # ARGUMENT UNPACKING -> {"id": 123} -> id=123
                    if response:
                        return HttpResponse(
                            {
                                "message": "Usuario encontrado!",
                                "usuario": {
                                    "id": response[0],
                                    "nome_usuario": response[1],
                                    "agencia": response[2],
                                    "conta": response[3],
                                    "saldo": response[4],
                                    "email": response[5]
                                }
                            },
                            200
                        )
                    return HttpResponse(
                        {
                            "message": "Usuario não encontrado"
                        },
                        400
                    )
            return HttpResponse(
                {
                    "message": "Parametro de busca inválido"
                },
                400
            )
        except Exception as exc:
            print(f'Ocorreu um erro no FIND USER: {str(exc)}')
            if str(exc) == 'Nenhum valor de consulta valido':
                return HttpResponse(
                    {"message": str(exc)},
                    400
                )
            return HttpResponse(
                {"message": "Algo deu errado com sua solicitação"},
                400
            )

    def login_user(self, data: dict) -> HttpResponse:
        if not data.get('senha'):
            return HttpResponse(
                {"message": "Senha obrigatoria"},
                400
            )

        data_keys = ['nome_usuario', 'email']
        for key in data_keys:
            if data.get(key):
                response = self.__users_repository.search_data(
                    **{key: data[key]})
                if response:
                    if self.__check_if_passwords_matches(data.get('senha'), response[6]):
                        token = self.__generate_token(response[0], response[5])
                        return HttpResponse(
                            {
                                "message": "Usuario logado com sucesso",
                                "id": response[0],
                                "email": response[5],
                                "token": token
                            },
                            200
                        )
                return HttpResponse(
                    {"message": "Credenciais invalidas"},
                    400
                )
        return HttpResponse(
            {
                "message": "Parametro de busca inválido"
            },
            400
        )

    def __check_if_user_already_exists(self, data: dict) -> bool | tuple:
        response = self.find_user(data)

        if response.status == 200:
            return (True, data)
        elif response.status == 400 and response.body == {"message": "Usuario não encontrado"}:
            return False
        else:
            return (response, data)

    def __check_if_passwords_matches(self, password: str, password_hashed: bytes) -> bool:
        password_handler = PasswordHandler()
        if password_handler.check_password(password, password_hashed):
            return True
        else:
            return False

    def __generate_token(self, id: int, email: str) -> str:
        token = self.__jwt_handler.encode_jwt(
            {'id': id, 'email': email, 'exp': datetime.now(timezone.utc) + timedelta(days=6)})

        return token
