from flask import Blueprint, jsonify, request

from src.main.composer.product_creator_compose import product_creator_compose
from src.main.composer.product_finder_compose import product_finder_compose

from src.http_types.http_request import HttpRequest


products_route = Blueprint('products_route', __name__, url_prefix='/products')


@products_route.route('/create', methods=['POST'])
def create_product() -> jsonify:
    try:
        http_request = HttpRequest(body=request.json)
        product_creator = product_creator_compose()
        response = product_creator.create_product(http_request)

        return jsonify(response.body), response.status
    except Exception as excerror:
        return jsonify({"message": str(excerror)}), 401


@products_route.route('/<product_name>', methods=['GET'])
def get_product(product_name: str) -> jsonify:
    try:
        http_request = HttpRequest(params={"product_name": product_name})
        product_finder = product_finder_compose()
        response = product_finder.find_by_name(http_request)

        return jsonify(response.body), response.status
    except Exception as excerror:
        return jsonify({"message": str(excerror)}), 401
