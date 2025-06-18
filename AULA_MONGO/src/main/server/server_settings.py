from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from src.main.routes.orders_route import orders_router
    app.register_blueprint(orders_router)

    return app
