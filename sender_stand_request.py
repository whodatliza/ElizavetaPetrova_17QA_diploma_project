# Елизавета Петрова, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
from configuration import url_create, url_get

# Создание заказа
def create_order(order_data):
    response_create = requests.post(url_create, json=order_data)
    return response_create

# Получение заказа по номеру трекера
def get_order(track):
    return requests.get(url_get + str(track))
