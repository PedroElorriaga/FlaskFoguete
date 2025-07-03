from flask import Blueprint, jsonify, request
from src.main.middlewares.auth_jwt import auth_jwt
from src.main.composers.users.users_composer import user_composer

user_router = Blueprint('user_router', __name__)


@user_router.route('/find_user', methods=['GET'])
def get_one_user():
    try:
        auth_jwt()
        data = request.json
        users = user_composer()
        response = users.find_user(data)

        return jsonify(response.body), response.status
    except Exception as exc:
        if str(exc) == 'Authorization failed':
            return jsonify({'message': 'Algo de errado em sua autorização'}), 401
        elif str(exc) == 'Security error':
            return jsonify({'message': 'Não autorizado'}), 401
        else:
            print(str(exc))
            return jsonify({'message': 'Ocorreu algum problema na solicitação'}), 500


@user_router.route('/find_all_users', methods=['GET'])
def get_all_users():
    auth_jwt()
    data = request.json
    users = user_composer()
    response = users.find_all_users()

    return jsonify(response.body)
