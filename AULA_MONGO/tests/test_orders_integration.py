from src.main.composers.order_composer import order_composer


def test_insert_data_in_mongo():
    orders = order_composer()
    orders.insert_order({"nome": "pedrita"})


def test_find_data_in_mongo():
    orders = order_composer()
    orders.find_order({"nome": "pedrita"})
