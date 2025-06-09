from flask import Flask

from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandler

redis_connection_handler = RedisConnectionHandler()
sqlite_connection_handler = SqliteConnectionHandler()

redis_connection_handler.connect()
sqlite_connection_handler.connect()


def create_app() -> Flask:
    app = Flask(__name__)

    from src.main.routes.products_routes import products_route
    app.register_blueprint(products_route)

    return app
