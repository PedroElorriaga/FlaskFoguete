from src.security.jwt_handler import JWTHandler
from flask import request


def auth_jwt() -> None:
    jwt_handler = JWTHandler()
    authorization = request.headers.get('Authorization')
    user_id = request.headers.get('UserId')

    if not user_id or not authorization:
        raise Exception('Authorization failed')

    token = jwt_handler.decode_jwt(authorization.split(' ')[1])

    if token.get('id') != int(user_id):
        raise Exception('Security error')
