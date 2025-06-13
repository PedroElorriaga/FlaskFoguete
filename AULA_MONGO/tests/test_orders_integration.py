from src.main.composers.order_composer import order_composer


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


def test_find_order_in_mongo():
    orders = order_composer()
    orders.find_order({"produto": "celular"})


def test_find_orders_datas_in_mongo():
    orders = order_composer()
    orders.find_orders()


def test_find_orders_by_parameter_in_mongo():
    orders = order_composer()
    orders.find_orders_by_parameter("info_produto")
