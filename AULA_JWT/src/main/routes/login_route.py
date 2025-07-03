from flask import Blueprint, jsonify, request
from src.main.composers.users.users_composer import user_composer

login_router = Blueprint('login_router', __name__, url_prefix='/login')


@login_router.route('/create', methods=['POST'])
def create_account() -> jsonify:
    data = request.json
    users = user_composer()
    response = users.insert_user(data)

    return jsonify(response.body), response.status


@login_router.route('/enter', methods=['POST'])
def enter_in_account() -> jsonify:
    data = request.json
    users = user_composer()
    response = users.login_user(data)

    if response.status == 200:
        return jsonify({
            'message': response.body['message'],
            'user_id': response.body['id'],
            'token': response.body['token']
        })

    return jsonify(response.body), response.status
