from datetime import datetime, timezone, timedelta

from flask import Blueprint, jsonify, request
from src.main.security.jwt_handler import JWTHandler

login_router = Blueprint('login_router', __name__, url_prefix='/login')


@login_router.route('/test1', methods=['POST'])
def test1() -> jsonify:
    jwt_instance = JWTHandler()
    jwt = jwt_instance.encode_jwt(
        {
            "email": "pedro@test.com",
            "exp": datetime.now(timezone.utc) + timedelta(minutes=1)
        })

    return jsonify({"message": jwt}), 200


@login_router.route('/test2', methods=['POST'])
def test2() -> jsonify:
    jwt_encoded = request.headers['Authorization'].split()[1]

    jwt_instance = JWTHandler()
    jwt = jwt_instance.decode_jwt(jwt_encoded)

    return jsonify({"message": jwt}), 200
