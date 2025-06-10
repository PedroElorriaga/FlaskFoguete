from flask import Blueprint, jsonify
from src.main.composer.visitors_compose import visitor_compose

visitors_router = Blueprint(
    'visitors_router', __name__, url_prefix='/visitors')


@visitors_router.route('/', methods=['GET'])
def get_visitors() -> jsonify:
    visitor = visitor_compose()
    visitor.insert_visitor()

    return jsonify({"message": "Visitou a pagina"})


@visitors_router.route('/quantity', methods=['GET'])
def get_visitors_quantity() -> jsonify:
    visitor = visitor_compose()
    response = visitor.get_visitor() or 0

    return jsonify(
        {
            "response": f"Quantidades de acessos nos ultimos 60 segundos {response}"
        }
    )
