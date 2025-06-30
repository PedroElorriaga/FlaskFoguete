from src.security.jwt_handler import JWTHandler
from datetime import datetime, timedelta, timezone


def test_generate_jwt_token():
    jwt_handler = JWTHandler()
    data = {
        'email': 'pedrotest@test.com',
        'senha': '123456',
        'exp': datetime.now(timezone.utc) + timedelta(minutes=1)
    }
    token = jwt_handler.encode_jwt(data)
    token_decoded = jwt_handler.decode_jwt(token)

    assert isinstance(token, str)
    assert isinstance(token_decoded, dict)
    assert token_decoded['email'] == data['email']
    assert token_decoded['senha'] == data['senha']
