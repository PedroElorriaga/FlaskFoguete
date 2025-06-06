from .product_finder import ProductFinder
from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandler
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.sqlite.repository.product_repository import ProductRepository
from src.http_types.http_request import HttpRequest

connection_redis_instance = RedisConnectionHandler()
connection_redis = connection_redis_instance.connect()
connection_sqlite_instance = SqliteConnectionHandler()
connection_sqlite = connection_sqlite_instance.connect()


def test_find_product():
    redis_repository_instance = RedisRepository(connection_redis)
    sqlite_repository_instance = ProductRepository(connection_sqlite)

    product_finder_instance = ProductFinder(
        redis_repository_instance, sqlite_repository_instance)

    http_request = HttpRequest(
        {"body": "teste"}, {"product_name": "MockProduct"})

    response = product_finder_instance.find_by_name(http_request)

    print(response.body)
    print(response.status)
