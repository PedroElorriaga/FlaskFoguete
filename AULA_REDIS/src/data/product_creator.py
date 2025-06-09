from src.models.redis.repository.interfaces.redis_repository import RedisInterface
from src.models.sqlite.repository.interfaces.product_repository import ProductInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class ProductCreator:
    def __init__(self,
                 redis_repository: RedisInterface,
                 product_repository: ProductInterface
                 ) -> None:
        self.__redis_repository = redis_repository
        self.__product_repository = product_repository

    def create_product(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        name = body.get('name')
        price = body.get('price')
        quantity = body.get('quantity')

        self.__insert_in_sql(name, price, quantity)
        self.__insert_in_cache(name, price, quantity)

        return self.__format_http_response(name, price, quantity)

    def __insert_in_sql(self, name: str, price: float, quantity: int) -> None:
        if name and price and quantity:
            self.__product_repository.insert_product(name, price, quantity)
            return None

        raise Exception('Dados invalidos')

    def __insert_in_cache(self, name: str, price: float, quantity: int) -> None:
        if name and price and quantity:
            self.__redis_repository.insert_with_expiration(
                name, f'{price},{quantity}', 60)
            return None

        raise Exception('Dados invalidos')

    def __format_http_response(self, name: str, price: float, quantity: int) -> HttpResponse:
        return HttpResponse(
            body={
                "attributes": {
                    "product_name": name,
                    "price": price,
                    "quantity": quantity
                }
            },
            status=200
        )
