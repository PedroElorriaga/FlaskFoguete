from src.main.server.server_settings import redis_connection_handler, sqlite_connection_handler
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.sqlite.repository.product_repository import ProductRepository
from src.data.product_finder import ProductFinder


def product_finder_compose() -> ProductFinder:
    redis_connection = redis_connection_handler.connect()
    sqlite_connection = sqlite_connection_handler.connect()

    redis_repository = RedisRepository(redis_connection)
    product_repository = ProductRepository(sqlite_connection)

    return ProductFinder(redis_repository, product_repository)
