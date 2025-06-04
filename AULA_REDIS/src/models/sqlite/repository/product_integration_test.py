import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandler
from src.models.sqlite.repository.product_repository import ProductRepository


connection_instance = SqliteConnectionHandler()
connection = connection_instance.connect()


@pytest.mark.skip(reason='Implementação no banco')
def test_insert_product():
    repository = ProductRepository(connection)

    repository.insert_product('MockProduct', 99.90, 88)


@pytest.mark.skip(reason='Implementação no banco')
def test_get_product():
    repository = ProductRepository(connection)

    repository.find_product_by_name('MockProduct')
