from datetime import datetime, timezone, timedelta
from flask import Blueprint, jsonify, request
from src.security.jwt_handler import JWTHandler
from src.main.composers.users.users_composer import user_composer

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


@login_router.route('/test3', methods=['POST'])
def test3() -> jsonify:
    data = request.json
    users = user_composer()

    response = users.insert_user(data)

    return jsonify(response.body), response.status


@login_router.route('/test4', methods=['POST'])
def test4() -> jsonify:
    data = request.json
    users = user_composer()

    response = users.find_user(data)

    return jsonify(response.body), response.status
