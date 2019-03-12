"""
Методы для определения формата файла и считывания данных
"""

import json


def read_tsv(data: str):
    """
    Считывает данные в формате tsv
    :param data: содержимое файла
    :return: заголовки и содержимое файла, tuple или None
    """
    # разбор tsv данных
    data = data.strip().split('\n')
    data = [line.split('\t') for line in data]

    headers = None
    content = []

    # получение заголовков и данных
    for line in data:
        if headers:
            # проверка заголовков
            if len(headers) < len(line):
                return None, []
            content.append(dict(zip(headers, line)))
        else:
            headers = line

    # tsv без заголовка не считаем валидным
    if not headers:
        return None, []

    return headers, content


def read_json(data: str):
    """
    Считывает данные в формате json
    :param data: содержимое файла
    :return: заголовки и содержимое файла, tuple или None
    """
    try:
        content = json.loads(data)
    except json.JSONDecodeError:
        return None, []

    # пустой json не считаем валидным
    if len(content) < 1:
        return None, []

    headers = list(content[0].keys())

    return headers, content


formats = {
    'json': read_json,
    'tsv': read_tsv,
}


def read_file_content(f_name: str, f_encoding: str) -> tuple:
    """
    Функция получения формата файла
    :param f_name: имя файла для проверки
    :param f_encoding: кодировка файла
    :return: заголовки и содержимое файла, tuple или None
    """
    # чтение файла целиком
    with open(f_name, mode='r', encoding=f_encoding) as f:
        data = f.read()

    # определение формата и преобразование к нужному виду
    for f_format, func in formats.items():
        headers, content = func(data=data)
        if headers:
            return headers, content

    raise TypeError("Не удалось получить содержимое файла")
