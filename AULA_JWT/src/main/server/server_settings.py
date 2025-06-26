from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from src.main.routes.login_route import login_router
    app.register_blueprint(login_router)

    return app
