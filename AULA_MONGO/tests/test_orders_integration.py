import pytest

from src.main.composers.order_composer import order_composer


@pytest.mark.skip(reason='Interação com banco de dados')
def test_insert_order_in_mongo():
    orders = order_composer()
    orders.insert_order({
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
    })


@pytest.mark.skip(reason='Interação com banco de dados')
def test_find_first_filter_order_in_mongo():
    orders = order_composer()
    orders.find_order({"produto": "celular"}, first=True)


@pytest.mark.skip(reason='Interação com banco de dados')
def test_find_all_filter_order_in_mongo():
    orders = order_composer()
    orders.find_order({"produto": "computador"})


@pytest.mark.skip(reason='Interação com banco de dados')
def test_find_all_orders_datas_in_mongo():
    orders = order_composer()
    orders.find_order()


@pytest.mark.skip(reason='Interação com banco de dados')
def test_find_orders_by_parameter_in_mongo():
    orders = order_composer()
    orders.find_orders_by_parameter("info_produto")


@pytest.mark.skip(reason='Interação com banco de dados')
def test_insert_many_orders_in_mongo():
    orders = order_composer()
    orders.insert_order([{
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
    },
        {
        "produto": "celular",
        "marca": "Iphone",
        "modelo": "16 Pro Max",
        "cor": "Cinza",
        "info_produto": {
            "valor": 10999.90,
            "peso": 0.123,
            "ano": "2025",
            "nacional": False
        }
    },
        {
        "produto": "monitor",
        "marca": "LG",
        "modelo": "XLI1142022",
        "cor": "Preto",
        "info_produto": {
            "valor": 550.00,
            "peso": 1.2,
            "ano": "2020",
            "nacional": True
        }
    },
        {
        "produto": "computador",
        "marca": "Dell",
        "modelo": "DELL I7",
        "cor": "Cinza",
        "info_produto": {
            "valor": 2870.90,
            "peso": 1.1,
            "ano": "2024",
            "nacional": False
        }
    },
        {
        "produto": "computador",
        "marca": "Generico",
        "modelo": "Asus Ryzen 7",
        "cor": "Branco",
        "info_produto": {
            "valor": 4190.90,
            "peso": 2.210,
            "ano": "2025",
            "nacional": True
        }
    }])


@pytest.mark.skip(reason='Interação com banco de dados')
def test_find_order_by_id():
    orders = order_composer()
    orders.find_order_by_id(
        "6852a7b5fa6338c7ece44b77",
        {"_id": 0}
    )


@pytest.mark.skip(reason='Interação com banco de dados')
def test_update_order_by_id():
    orders = order_composer()
    orders.update_order_by_id("6852a7b5fa6338c7ece44b77", {
        "info_produto.nacional": True,
        "info_produto.ano": "2022"
    })


@pytest.mark.skip(reason='Interação com banco de dados')
def test_delete_data_by_id():
    orders = order_composer()
    orders.delete_data_by_id('6852a7b5fa6338c7ece44b76')
