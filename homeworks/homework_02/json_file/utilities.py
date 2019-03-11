"""
Методы для работы с json
"""

import json


def check_json(f_name: str, f_encoding: str) -> bool:
    """Проверка на формат json"""
    try:
        with open(f_name, encoding=f_encoding) as f:
            json.load(f)
            return True
    except json.JSONDecodeError:
        return False


def read_json(f):
    """
    Считывает файл в формате json
    :param f: объекта файла
    :return: tuple(заголовки, содержимое) или tuple(None, None)
    """
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        return None, None

    # пустой json не считаем валидным
    if len(data) < 1:
        return None, None

    headers = data[0].keys()

    # проверка заголовков (лучше когда тут только чтение)
    for item in data:
        if len(headers) < len(item.keys()):
            return None, None

    return headers, data
