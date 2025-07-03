from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from src.main.routes.login_route import login_router
    from src.main.routes.user_route import user_router
    app.register_blueprint(login_router)
    app.register_blueprint(user_router)

    return app
