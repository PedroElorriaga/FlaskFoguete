from src.models.redis.repository.redis_repository import RedisRepository
from src.models.sqlite.repository.product_repository import ProductRepository


class ProductFinder:
    def __init__(self,
                 redis_repository: RedisRepository,
                 product_repository: ProductRepository
                 ) -> None:
        self.__redis_repository = redis_repository
        self.__product_repository = product_repository
