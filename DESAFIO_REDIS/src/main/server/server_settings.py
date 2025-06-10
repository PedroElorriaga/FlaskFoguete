from flask import Flask

from src.models.redis.settings.redis_settings import RedisSettingsHandler

redis_settings_handler = RedisSettingsHandler()
redis_settings_handler.connect()


def create_app():
    app = Flask(__name__)

    from src.main.routes.visitors_routes import visitors_router
    app.register_blueprint(visitors_router)

    return app
