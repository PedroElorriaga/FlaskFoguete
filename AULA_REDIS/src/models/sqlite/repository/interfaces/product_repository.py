from abc import ABC, abstractmethod


class ProductInterface(ABC):

    @abstractmethod
    def find_product_by_name(self, product_name: str) -> None:
        pass

    @abstractmethod
    def insert_product(self, name: str, price: float, quantity: int) -> None:
        pass
