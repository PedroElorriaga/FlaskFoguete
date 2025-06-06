from src.models.redis.repository.interfaces.redis_repository import RedisInterface
from src.models.sqlite.repository.interfaces.product_repository import ProductInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class ProductFinder:
    def __init__(self,
                 redis_repository: RedisInterface,
                 product_repository: ProductInterface
                 ) -> None:
        self.__redis_repository = redis_repository
        self.__product_repository = product_repository

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params['product_name']

        product = self.__find_product_by_redis(product_name)
        if not product:
            product = self.__find_product_by_sql(product_name)
            self.__insert_product_in_redis(product)

        return self.__format_http_reponse(product)

    def __find_product_by_redis(self, product_name: str) -> tuple:
        product_info = self.__redis_repository.get_key(product_name)
        if product_info:
            product_info_list = product_info.split(",")
            return (0, product_name, product_info_list[0], product_info_list[1])

        return None

    def __find_product_by_sql(self, product_name: str) -> tuple:
        product_info = self.__product_repository.find_product_by_name(
            product_name)
        if not product_info:
            raise Exception("Produto nao econtrado")

        return product_info

    def __insert_product_in_redis(self, product: tuple) -> None:
        self.__redis_repository.insert_with_expiration(
            product[1], f"{product[2]},{product[3]}", 10)

    def __format_http_reponse(self, product: tuple) -> HttpResponse:
        return HttpResponse(
            body={
                "attributes": {
                    "product_name": product[1],
                    "price": product[2],
                    "quantity": product[3]
                }
            },
            status=200
        )
