import requests
import configuration

# Клиент создает заказ
def post_new_orders (order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# Запрос на получение информации о заказе по треку
def get_treck_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER, params={"t": track})










