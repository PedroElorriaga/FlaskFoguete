import pytest

from src.models.mongodb.repository.orders_repository import OrdersRepository
from src.data.orders.orders_data import OrdersData

from bson.objectid import ObjectId


class OrdersCollectionMock:
    def __init__(self) -> None:
        self.insert_one_attribute = {}
        self.find_one_attribute = {}

    # ESSA FUNÇÃO (insert_one) É MESMA QUE EU TENHO NO MEU REPOSITORY PORÉM AQUI MOCKADA
    def insert_one(self, user_input: dict) -> None:
        self.insert_one_attribute['dict'] = user_input

    def find_one(self, *args) -> None:
        self.find_one_attribute['args'] = args


def test_insert_one_data():
    # CONNECTION FALSA (MOCKADA)
    mongo_mock_colletion = OrdersCollectionMock()
    orders_repository = OrdersRepository({
        'orders': mongo_mock_colletion
    })
    orders = OrdersData(orders_repository)

    data = {
        "_id": "684e0202aa844353a9f12921",
        "produto": "celular",
        "marca": "Iphone",
        "modelo": "14 Pro Max",
        "cor": "Preto",
        "info_produto": {
            "valor": 8999.90,
            "peso": 0.142,
            "ano": "2023",
            "nacional": False
        }
    }

    response = orders.insert_order(data)

    assert response == data
    assert mongo_mock_colletion.insert_one_attribute['dict'] == data


def test_insert_one_with_wrong_data():
    mongo_mock_colletion = OrdersCollectionMock()
    orders_repository = OrdersRepository({
        'orders': mongo_mock_colletion
    })
    orders = OrdersData(orders_repository)

    data = 'wrong type'

    with pytest.raises(Exception) as excinfo:
        orders.insert_order(data)

    assert str(excinfo.value) == 'Tipos de dados invalidos'


def test_find_data_by_id():
    mongo_mock_colletion = OrdersCollectionMock()
    orders_repository = OrdersRepository({
        'orders': mongo_mock_colletion
    })
    orders = OrdersData(orders_repository)

    data = {
        "_id": "684e0202aa844353a9f12921",
        "produto": "celular",
        "marca": "Iphone",
        "modelo": "14 Pro Max",
        "cor": "Preto",
        "info_produto": {
            "valor": 8999.90,
            "peso": 0.142,
            "ano": "2023",
            "nacional": False
        }
    }
    orders.insert_order(data)

    with pytest.raises(Exception) as excinfo:
        orders.find_order_by_id('684e0202aa844353a9f12921')

    assert str(excinfo.value) == 'o ID informado não existe'
    assert mongo_mock_colletion.find_one_attribute['args'][0]['_id'] == ObjectId(
        data['_id'])


def test_find_data_by_wrong_id():
    mongo_mock_colletion = OrdersCollectionMock()
    orders_repository = OrdersRepository({
        'orders': mongo_mock_colletion
    })
    orders = OrdersData(orders_repository)

    data = {
        "_id": "684e0202aa844353a9f12921",
        "produto": "celular",
        "marca": "Iphone",
        "modelo": "14 Pro Max",
        "cor": "Preto",
        "info_produto": {
            "valor": 8999.90,
            "peso": 0.142,
            "ano": "2023",
            "nacional": False
        }
    }
    orders.insert_order(data)

    with pytest.raises(Exception) as excinfo:
        orders.find_order_by_id('684e0202aa844353a9f12900')

    assert str(excinfo.value) == 'o ID informado não existe'
    assert mongo_mock_colletion.find_one_attribute['args'][0]['_id'] != ObjectId(
        data['_id'])
