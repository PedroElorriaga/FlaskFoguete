from flask import Blueprint, json, jsonify, request
from bson import json_util

from src.main.composers.order_composer import order_composer

from bson.errors import InvalidId

orders_router = Blueprint('orders_router', __name__, url_prefix='/orders')


@orders_router.route('/find-all', methods=['GET'])
def find_all_orders() -> jsonify:
    # USERS INPUTS
    show_off = request.args.getlist('show_off')
    data = request.json

    orders = order_composer()
    response = json.loads(json_util.dumps(
        orders.find_order(data, show_off=show_off)))

    return jsonify(
        {"orders": response}
    ), 200


@orders_router.route('/find-first', methods=['GET'])
def find_fisrt_orders() -> jsonify:
    # USERS INPUTS
    show_off = request.args.getlist('show_off')
    data = request.json

    orders = order_composer()
    response = json.loads(json_util.dumps(
        orders.find_order(data, first=True, show_off=show_off)))

    return jsonify(
        {"orders": response}
    ), 200


@orders_router.route('/<id_order>', methods=['GET'])
def find_orders_by_id(id_order: str) -> jsonify:
    # USERS INPUTS
    show_off = request.args.getlist('show_off')
    id = id_order

    try:
        orders = order_composer()
        response = json.loads(json_util.dumps(
            orders.find_order_by_id(id, show_off=show_off)))

        return jsonify(
            {"orders": response}
        ), 200
    except InvalidId as err:
        print(err)
        return jsonify(
            {"erro": "o ID informado não é valido"}
        ), 400
    except Exception as err:
        print(err)

        if str(err) == 'o ID informado não existe':
            return jsonify(
                {"erro": str(err)}
            ), 400

        return jsonify(
            {"erro": "um erro inesperado aconteceu"}
        ), 400


@orders_router.route('/create', methods=['POST'])
def create_orders() -> jsonify:
    # USERS INPUTS
    data = request.json

    try:
        orders = order_composer()
        response = json.loads(
            json_util.dumps(orders.insert_order(data)))

        return jsonify(
            {
                "success": "order created",
                "orders": {
                    "produtos-criados": response
                }
            }
        ), 200
    except Exception as err:
        print(err)

        if str(err) == 'Tipos de dados invalidos':
            return jsonify(
                {"erro": str(err)}
            ), 400

        return jsonify(
            {"erro": "um erro inesperado aconteceu"}
        ), 400


@orders_router.route('/update/<id_order>', methods=['PUT'])
def update_order_by_id(id_order: str) -> jsonify:
    # USERS INPUTS
    id = id_order
    data = request.json

    try:
        orders = order_composer()
        response = json.loads(json_util.dumps(
            orders.update_order_by_id(id, data)))

        return jsonify(
            {
                "success": "order updated",
                "orders": {
                    "produto-atualizado": response
                }
            }
        ), 200
    except InvalidId as err:
        print(err)
        return jsonify(
            {"erro": "o ID informado não é valido"}
        ), 400
    except Exception as err:
        print(err)

        if str(err) == 'o ID informado não existe':
            return jsonify(
                {"erro": str(err)}
            ), 400

        return jsonify(
            {"erro": "um erro inesperado aconteceu"}
        ), 400
