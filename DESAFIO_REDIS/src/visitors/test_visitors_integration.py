from src.models.redis.repository.redis_repositoy import RedisRepository
from src.models.redis.settings.redis_settings import RedisSettingsHandler
from src.visitors.visitors import Visitors


def test_visitors():
    redis_settings_handler = RedisSettingsHandler()
    redis_connection = redis_settings_handler.connect()
    redis_repository = RedisRepository(redis_connection)

    visitors_instance = Visitors(redis_repository)
    visitors_instance.insert_visitor()
