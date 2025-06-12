from src.data.orders.orders_data import OrdersData
from src.models.mongodb.settings.connection import MongoSettingsHandler
from src.models.mongodb.repository.orders_repository import OrdersRepository


def order_composer() -> OrdersData:
    mongo_setting_handler = MongoSettingsHandler()
    mongo_connection = mongo_setting_handler.connect()
    order_repository = OrdersRepository(mongo_connection)

    return OrdersData(order_repository)
